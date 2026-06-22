---
name: caching-strategy
description: >
  Produces a caching strategy for a system — goals, what to cache ranked by impact, cache layers,
  a per-resource strategy (TTL, invalidation, key pattern), failure modes including stampede and
  staleness, monitoring, and a cold-start plan. Use when the user says "caching strategy", "what
  should we cache", "reads are slow", "add Redis/CDN", or describes read-latency pain. Use this to
  fix read latency with caching; use scalability-assessment to find which component is the
  bottleneck first, and database-selection-guide when the real fix is a different datastore.
---

# Caching Strategy

Design a deliberate caching strategy — what to cache, where, how to invalidate, and what happens when the cache is unavailable — because caching done wrong creates more problems (stale data, stampedes, inconsistency) than it solves.

## Inputs to gather

Gather these before designing. If any are missing, ask in a single batched question — never invent read/write patterns, staleness tolerance, or available infrastructure. Mark anything genuinely unavailable as **Unknown** in the output.

- **System description** — what it is
- **Current bottleneck** — what is slow and by how much
- **Read patterns** — volume, hot-key skew
- **Write patterns** — change frequency per resource
- **Staleness tolerance** — how stale is acceptable, per resource
- **Infrastructure** — available cache infrastructure (Redis, CDN, etc.)

## Steps

1. Confirm inputs. If staleness tolerance or write frequency per resource is unstated, ask — they decide TTL and invalidation. Mark gaps **Unknown**.
2. State the **Caching goal** — the specific problem caching solves (latency, throughput, cost) tied to the measured bottleneck.
3. List **What to cache**, ranked by impact, as a table: resource, read frequency, write frequency, staleness tolerance, priority.
4. Define the **Cache layers** — where caches live (CDN, application/Redis, in-process) and what belongs in each.
5. Write the **Per-resource strategy** — for each cached resource: TTL, invalidation method (write-through vs TTL-only), storage location, and key pattern. Tie TTL to the stated staleness tolerance; use short TTL as a safety net behind active invalidation.
6. Enumerate **Failure modes** as a table: cache unavailability (circuit-breaker / bypass), cache stampede (stale-while-revalidate with a per-key refresh lock), stale data after a write, and cold start — each with handling. Reads that must never be stale (e.g. price at checkout) bypass the cache.
7. Define **Monitoring** — hit rate per resource type with targets, cached-vs-uncached latency, invalidation lag, memory/eviction, and DB query rate.
8. Write the **Cold start plan** — behaviour when caches are empty (deploy, restart, failover): warm the hot set on startup, stagger with jitter so warming doesn't stampede, keep the circuit breaker and refresh locks active during fill, and state the expected transient and when to alert.
9. Adapt to context: for a write-heavy system, cache the rendered query result rather than individual entities. For multi-region, add a cache-consistency-across-regions section (cross-region invalidation is a common bug source). For cost-driven caching, target the most expensive queries, not the most frequent. To start simple without Redis, use an in-process LRU cache.
10. Assemble the output in the format below.

## Output format

```
**Caching Strategy: [System]**

**Goal:** [Problem caching solves, tied to the measured bottleneck]

**What to Cache (by impact)**
| Resource | Read Freq | Write Freq | Staleness OK | Priority |
|----------|-----------|------------|--------------|----------|

**Cache Layers**
1. **[Layer]:** [what lives here, TTL]

**Per-Resource Strategy**
| Resource | Cache | TTL | Invalidation | Key Pattern |
|----------|-------|-----|--------------|-------------|

**Failure Modes**
| Failure | Impact | Handling |
|---------|--------|----------|

**Monitoring**
- [Hit rate per resource w/ target, latency comparison, invalidation lag, eviction, DB query rate]

**Cold Start Plan**
- [Warm hot set, stagger, protect DB, expected transient, alert threshold]
```

## Boundaries

- Never fabricate read/write rates or staleness tolerances — mark them **Unknown**; TTL and invalidation depend on them.
- Never cache data that must always be fresh (e.g. price at checkout, auth decisions) — name what bypasses the cache.
- Never design a cache without its failure modes — stampede, unavailability, and cold start are mandatory, not optional.
- Never set a TTL longer than the stated staleness tolerance, and never rely on TTL alone where active invalidation is feasible for tight-staleness data.

## Chaining

- This commonly follows **scalability-assessment** (which identifies the read-path bottleneck a cache addresses).
- After this, offer **observability-strategy** to monitor hit rate, invalidation lag, and the cache's own failure modes.
