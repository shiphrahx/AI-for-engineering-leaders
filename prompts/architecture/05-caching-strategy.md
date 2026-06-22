# Caching Strategy

## Situation

Your system is hitting performance limits on reads, and the answer is caching — but caching done wrong creates more problems than it solves (stale data, cache stampedes, inconsistency). You need a deliberate strategy that covers what to cache, where, how to invalidate, and what failure modes to handle.

## The Prompt

```
You are a senior engineer designing a caching strategy for a system. For each cacheable resource, specify: where the cache lives, what the TTL is, how it's invalidated, and what happens when the cache is unavailable. Address cache stampedes, consistency, and cold-start scenarios explicitly.

Structure:
1. **Caching goals** — what problem caching solves (latency, throughput, cost, or all three)
2. **What to cache** — ranked list of cacheable resources with read frequency and staleness tolerance
3. **Cache layers** — where caches live (CDN, application-level, database query cache, etc.)
4. **Per-resource strategy** — for each cached resource: TTL, invalidation method, storage location, serialisation format
5. **Failure modes** — cache unavailability, thundering herd, stale data scenarios, and how to handle each
6. **Monitoring** — cache hit rate, latency comparison, invalidation lag
7. **Cold start plan** — how the system behaves when caches are empty

System: [SYSTEM_DESCRIPTION]
Current bottleneck: [WHAT_IS_SLOW]
Read patterns: [READ_PATTERNS]
Write patterns: [WRITE_PATTERNS]
Staleness tolerance: [HOW_STALE_IS_ACCEPTABLE]
Infrastructure: [AVAILABLE_CACHE_INFRASTRUCTURE]
```

## Example Input

```
System: Product catalogue API for an e-commerce platform
Bottleneck: Product detail page takes 400ms (target: <100ms). 80% of the time is spent on 3 database queries (product details, pricing, reviews aggregate).
Read patterns: 10K product detail views/minute at peak. Top 1% of products account for 40% of views. Product listing pages (100 products per page) are also slow.
Write patterns: Products updated ~500 times/day (admin edits). Prices change ~50 times/day. Reviews added ~2,000/day.
Staleness tolerance: Product details can be 5 minutes stale. Prices must be fresh within 30 seconds. Review aggregates can be 15 minutes stale.
Infrastructure: Redis cluster available (ElastiCache), CloudFront CDN in front of API.
```

## Example Output

> **Caching Strategy: Product Catalogue API**
>
> **Goal:** Reduce product detail page latency from 400ms to <100ms by caching the three database queries that account for 80% of response time.
>
> **What to Cache (by impact)**
> | Resource | Read Freq | Write Freq | Staleness OK | Priority |
> |----------|-----------|------------|-------------|----------|
> | Product details | 10K/min | 500/day | 5 min | P0 |
> | Review aggregates | 10K/min | 2K/day | 15 min | P0 |
> | Product pricing | 10K/min | 50/day | 30 sec | P0 |
> | Product listing pages | 2K/min | varies | 5 min | P1 |
>
> **Cache Layers**
> 1. **CDN (CloudFront):** Static assets, product images. TTL: 24 hours.
> 2. **Application cache (Redis):** Product details, pricing, review aggregates. Primary caching layer.
> 3. **In-process cache (local memory):** Configuration data, category tree. TTL: 5 minutes. Avoids Redis round-trip for data that rarely changes.
>
> **Per-Resource Strategy**
>
> | Resource | Cache | TTL | Invalidation | Key Pattern |
> |----------|-------|-----|-------------|-------------|
> | Product details | Redis | 5 min | Write-through (invalidate on admin edit) | `product:{id}:detail` |
> | Product pricing | Redis | 30 sec | Write-through (invalidate on price change) + short TTL as safety net | `product:{id}:price` |
> | Review aggregates | Redis | 15 min | TTL-based only (no active invalidation — staleness is acceptable) | `product:{id}:reviews` |
> | Product listing | Redis | 5 min | Invalidate on any product change in the listing's category | `listing:{category}:{page}:{sort}` |
>
> **Failure Modes**
>
> | Failure | Impact | Handling |
> |---------|--------|----------|
> | Redis unavailable | All cache misses, DB takes full load | Circuit breaker: if Redis is down, bypass cache entirely. DB can handle 100% load for short periods (tested at 2x). Alert immediately. |
> | Cache stampede (popular product expires, 1000 concurrent requests hit DB) | DB overload on expiration | Use a soft-TTL / stale-while-revalidate scheme: keep entries with a soft expiry shorter than the hard expiry. After soft expiry, the first request acquires a refresh lock and repopulates while everyone else serves the still-valid stale value. The hard TTL is the real eviction bound. |
> | Stale price served after price change | Customer sees wrong price | Write-through invalidation on price change + 30-sec max TTL = maximum staleness of 30 seconds. Price at checkout is always read from DB (never cached). |
> | Cold start (empty cache after deploy/restart) | Burst of DB queries | Cache warming: on deploy, pre-populate top 1,000 products (covers 40% of traffic). Remaining cache fills organically. |
>
> **Monitoring**
> - Cache hit rate per resource type (target: >95% for product details, >90% for listings)
> - p99 latency comparison: cached vs uncached responses
> - Cache invalidation lag (time from write to cache eviction)
> - Redis memory utilisation and eviction rate
> - DB query rate (should drop proportionally to cache hit rate)
>
> **Cold Start Plan**
> The cache is empty after any deploy, Redis restart, or failover. Plan for it explicitly rather than hoping traffic refills it gracefully:
> - **Warm the hot set on startup:** a post-deploy job pre-populates the top 1,000 products (≈40% of traffic) before the instance takes traffic. This caps the initial DB burst.
> - **Stagger, don't thunder:** warm in batches with jitter so warming itself doesn't stampede the DB.
> - **Protect the DB during fill:** keep the circuit breaker and per-key refresh locks active so the organic fill of the long tail can't overload the DB.
> - **Expected behaviour:** elevated p99 and DB load for the first 1–2 minutes after a cold start, returning to >95% hit rate as the tail fills. Alert only if it persists beyond ~5 minutes (signals warming failed).

## Tuning Notes

- **Write-heavy system:** Caching is less effective when data changes frequently. Consider caching at the query result level rather than the entity level — cache the rendered response, not the individual objects.
- **Multi-region:** Add a "cache consistency across regions" section. Cross-region cache invalidation is a common source of bugs.
- **Cost-driven caching:** If the goal is reducing database costs rather than latency, focus on the most expensive queries, not the most frequent ones.
- **Starting simple:** If you don't have Redis yet, start with in-process caching (e.g., an LRU cache in your application). It's less powerful but zero infrastructure overhead.
