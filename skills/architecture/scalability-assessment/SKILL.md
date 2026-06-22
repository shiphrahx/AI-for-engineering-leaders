---
name: scalability-assessment
description: >
  Produces a scalability assessment of an existing system — current state, growth scenario, a
  component-by-component breaking-point analysis, a bottleneck ranking by what breaks first, a phased
  investment roadmap, and quick wins. Use when the user says "can we handle 5x/10x", "scalability
  assessment", "where will this break under load", "prep for Black Friday / a big customer", or
  describes anticipated growth. Use this to find what breaks first under growth; use caching-strategy
  to fix a read-latency bottleneck and database-selection-guide when the bottleneck is the datastore
  choice itself.
---

# Scalability Assessment

Evaluate whether the current architecture survives 5x or 10x load and identify the bottleneck that breaks first — prioritised by what breaks first, not by what's most interesting to fix.

## Inputs to gather

Gather these before assessing. If any are missing, ask in a single batched question — never invent current metrics, growth targets, or architecture details. Mark anything genuinely unavailable as **Unknown** in the output.

- **System description** — what it is
- **Current load** — current traffic and resource utilisation metrics
- **Growth target** — expected load increase and timeline
- **Architecture overview** — components and topology
- **Known pain points** — what already strains

## Steps

1. Confirm inputs. If current utilisation metrics or the growth target are unstated, ask — the analysis is meaningless without them. Mark gaps **Unknown**.
2. Write the **Current state** — system overview, current peak traffic, and resource utilisation per major component; note how much headroom exists.
3. Write the **Growth scenario** — the sustained multiple and any spike multiple, with timeline and data-size growth.
4. Do the **Component-by-component analysis** as a table: for each component give current capacity, the breaking point (as a multiple of current), the symptom when overloaded, the recommended fix, and the effort. Flag components already at their limit.
5. Produce the **Bottleneck ranking** — ordered strictly by what breaks first under growth, not by interest or ease.
6. Build the **Investment roadmap** — phased by time window, sequencing fixes so the earliest-breaking bottleneck is addressed first; end with a load test at the target multiple.
7. List **Quick wins** — changes (each under ~1 week) that buy significant headroom with minimal effort.
8. Adapt to context: for an executive audience, translate each bottleneck into business risk ("queue backs up" → "order confirmation emails delayed hours during peak, support ticket spike"). For a startup with limited runway, focus only on the quick wins and the #1 bottleneck — skip the 12-month roadmap. After a scaling incident, lead with the incident and the bottleneck that caused it. For microservices, add network latency and service-to-service communication as components to assess.
9. Assemble the output in the format below.

## Output format

```
**Scalability Assessment: [System]**

**Current State**
[Overview, current peak load, per-component utilisation, headroom]

**Growth Scenario**
[Sustained multiple + spike multiple, timeline, data growth]

**Component Analysis**
| Component | Current Capacity | Breaks At | Symptom | Fix | Effort |
|-----------|------------------|-----------|---------|-----|--------|

**Bottleneck Ranking (what breaks first)**
1. [Component] — breaks at [multiple]. [Why it's first.]

**Investment Roadmap**
- **[Time window]:** [fixes, ordered by breaking point]

**Quick Wins (< 1 week each)**
- [Change → headroom it buys]
```

## Boundaries

- Never fabricate current utilisation, capacity numbers, or breaking points — mark them **Unknown**; estimates need real metrics.
- Never rank by what's interesting or easy to fix — rank strictly by what breaks first under the stated growth.
- Never recommend a re-architecture when a quick win buys the needed headroom — call out the cheap option first.
- State breaking points as estimates to validate with load testing, not guarantees.

## Chaining

- If a read-path component (DB reads, hot keys) breaks first, offer **caching-strategy** to buy headroom.
- If the datastore itself is the bottleneck, offer **database-selection-guide** to evaluate alternatives.
- After addressing bottlenecks, offer **observability-strategy** to monitor the new capacity limits.
