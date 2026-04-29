# Scalability Assessment

## Situation

Your system is working fine now, but growth is coming — a big customer, a viral launch, international expansion. You need to evaluate whether your current architecture can handle 5x or 10x load, and identify the bottlenecks that will break first.

## The Prompt

```
You are a senior engineer conducting a scalability assessment of an existing system. Identify the bottlenecks, failure points, and capacity limits. For each, estimate when it becomes a problem and recommend a fix. Prioritise by what breaks first, not what's most interesting to fix.

Structure:
1. **Current state** — system overview, current traffic, resource utilisation
2. **Growth scenario** — the expected load increase and timeline
3. **Component-by-component analysis** — for each major component: current capacity, breaking point, symptoms when overloaded, and recommended fix
4. **Bottleneck ranking** — ordered by what breaks first under growth
5. **Investment roadmap** — phased plan to address bottlenecks before they hit
6. **Quick wins** — changes that buy significant headroom with minimal effort

System: [SYSTEM_DESCRIPTION]
Current load: [CURRENT_METRICS]
Growth target: [EXPECTED_GROWTH]
Architecture: [ARCHITECTURE_OVERVIEW]
Known pain points: [KNOWN_ISSUES]
```

## Example Input

```
System: E-commerce order processing pipeline
Current load: 500 orders/hour peak, 3,000 orders/day, 50K product catalogue
Growth target: 5x in 12 months (enterprise sales pipeline closing). 10x for Black Friday spike.
Architecture: Rails monolith → PostgreSQL (primary + 1 read replica) → Redis (caching + sessions) → Sidekiq (background jobs) → S3 (media). Single-region AWS deployment.
Known pain points: Database queries slow during product catalogue imports, Sidekiq queue backs up when processing bulk orders, image serving is slow for international customers.
```

## Example Output

> **Scalability Assessment: Order Processing Pipeline**
>
> **Current State**
> Serving 500 orders/hour peak on a Rails monolith with PostgreSQL, Redis, and Sidekiq. Resource utilisation during peak: DB CPU ~45%, Redis memory ~30%, application servers 3 of 5 at ~60% CPU. The system is healthy today but has limited headroom.
>
> **Growth Scenario**
> 5x sustained growth (2,500 orders/hour) within 12 months. 10x spike (5,000 orders/hour) for seasonal events. 250K product catalogue (5x current).
>
> **Component Analysis**
>
> | Component | Current Capacity | Breaks At | Symptom | Fix | Effort |
> |-----------|-----------------|-----------|---------|-----|--------|
> | PostgreSQL primary | ~1,200 orders/hr | ~2x current | Query timeouts, connection pool exhaustion | Read replica for reporting, connection pooler (PgBouncer), query optimisation | Medium |
> | Sidekiq workers | ~800 jobs/hr | ~1.5x current ⚠️ | Queue backlog, delayed order confirmations | Scale workers horizontally, separate queues by priority (critical vs bulk) | Low |
> | Rails app servers | ~3,000 req/sec | ~4x current | 503 errors, slow responses | Auto-scaling group, consider breaking out hot paths to dedicated services | Medium |
> | Redis | ~5GB / 16GB | ~10x current | Unlikely bottleneck at 5x | Monitor memory, add eviction policy for cache keys | Low |
> | Product catalogue queries | Slow at 50K products | Already pain point | Slow search, import blocking writes | Add search index (Elasticsearch), async catalogue imports | Medium |
> | Image serving | CDN in single region | International users affected now | Slow image loads for EU/APAC | Multi-region CDN (CloudFront with edge locations) | Low |
>
> **Bottleneck Ranking (what breaks first)**
> 1. **Sidekiq queue** — breaks at ~1.5x. This is the most urgent.
> 2. **PostgreSQL primary** — breaks at ~2x. Connection exhaustion during peak.
> 3. **Product catalogue queries** — already slow. Gets worse with 5x catalogue size.
> 4. **Rails app servers** — breaks at ~4x. Adequate headroom for now.
> 5. **Image serving** — already impacting international users. Gets worse with any growth.
> 6. **Redis** — unlikely to be a problem at 5x.
>
> **Investment Roadmap**
> - **Month 1-2:** Split Sidekiq into priority queues, add workers. Add PgBouncer connection pooler. CDN edge locations for international media.
> - **Month 3-5:** Elasticsearch for product search. Read replica for reporting queries. Async catalogue imports.
> - **Month 6-9:** App server auto-scaling. Evaluate breaking out order processing into a dedicated service.
> - **Month 10-12:** Load test at 10x. Address any newly discovered bottlenecks.
>
> **Quick Wins (< 1 week each)**
> - Add PgBouncer (connection pooling) — buys 2-3x database headroom
> - Split Sidekiq into critical and bulk queues — prevents bulk operations from blocking order confirmations
> - Enable CloudFront edge caching for product images — immediate improvement for international users

## Tuning Notes

- **Presenting to executives:** Translate bottlenecks into business risk. "The Sidekiq queue backs up" becomes "Order confirmation emails will be delayed by hours during peak periods, causing customer support ticket spikes."
- **Startup with limited resources:** Focus on the quick wins and the #1 bottleneck only. You don't need a 12-month roadmap if you might pivot in 3 months.
- **After a scaling incident:** This assessment becomes urgent. Lead with the incident, show the bottleneck that caused it, and use the momentum to get investment.
- **Microservices architecture:** Same approach, but add network latency and service-to-service communication as a component to assess.
