# Database Selection Guide

## Situation

You need to choose a database for a new service or workload. The wrong choice means a painful migration later; the right choice means the database disappears into the background and just works. This prompt helps you evaluate options systematically based on your actual requirements, not marketing.

## The Prompt

```
You are a senior engineer evaluating database options for a specific workload. Analyse the requirements (data model, access patterns, scale, consistency needs) and recommend a database with clear reasoning. Consider operational cost and team expertise, not just technical fit.

Structure:
1. **Workload analysis** — data model shape, read/write ratio, access patterns, consistency requirements, expected scale
2. **Candidate databases** — 3-4 options with fit assessment for each requirement
3. **Comparison matrix** — side-by-side on the dimensions that matter
4. **Operational considerations** — who manages it, team expertise, cost, ecosystem
5. **Recommendation** — which database and why, with conditions for reconsidering
6. **Anti-recommendation** — which popular option is tempting but wrong for this workload, and why

Workload: [DESCRIBE_THE_WORKLOAD]
Access patterns: [READ_WRITE_PATTERNS]
Scale: [EXPECTED_DATA_VOLUME_AND_THROUGHPUT]
Consistency requirements: [CONSISTENCY_NEEDS]
Team context: [TEAM_EXPERTISE_AND_OPERATIONAL_CAPACITY]
```

## Example Input

```
Workload: Activity feed / timeline service. Each user has a feed of events from people and projects they follow. Events include: task updates, comments, status changes, file uploads. The feed is personalised — each user sees a different set of events based on their subscriptions.
Access patterns: Write-heavy ingestion (every platform action generates 1-3 events), read-heavy for feed queries (every page load fetches the latest 50 events for that user). Fan-out on write: one event may appear in 100+ user feeds. Need to support "mark as read" and "filter by type."
Scale: 15K events/hour written, 50K feed reads/hour. 100M events total within a year. Average user has 5K events in their feed.
Consistency: Eventual consistency is fine — a 5-second delay before an event appears in a feed is acceptable. Feed reads must be fast (< 50ms p99).
Team: Strong PostgreSQL expertise. Some DynamoDB experience. No Cassandra experience. Run on AWS.
```

## Example Output

> **Database Selection: Activity Feed Service**
>
> **Workload Summary**
> High-volume event ingestion with fan-out on write. Read-heavy feed queries with per-user personalisation. Eventual consistency acceptable. Latency-sensitive reads (< 50ms p99). 100M events projected in year one.
>
> **Candidates**
>
> | | PostgreSQL | DynamoDB | Redis (Sorted Sets) | Cassandra |
> |---|---|---|---|---|
> | Data model fit | Good (relational events + subscriptions) | Good (key-value feed per user) | Good (sorted set per user feed) | Good (wide-column, time-series) |
> | Write throughput | Adequate at 15K/hr but fan-out writes strain connections | Excellent (auto-scaling, provisioned WCUs) | Excellent (in-memory) | Excellent (distributed writes) |
> | Read latency < 50ms | Possible with proper indexing and caching | Consistent single-digit ms | Sub-millisecond | Good (single-partition reads) |
> | Fan-out on write | Expensive (100+ inserts per event) | Manageable (batch writes) | Efficient (ZADD to sorted sets) | Efficient (distributed writes) |
> | 100M events storage | Fine | Fine | Expensive (in-memory) | Fine |
> | Operational complexity | Low (team knows it) | Medium (DynamoDB quirks, capacity planning) | Low (ElastiCache managed) | High (team has no experience) |
> | Cost at scale | $$ | $$$ (write-heavy = high WCU cost) | $$$ (100M events in-memory is expensive) | $$ |
>
> **Recommendation: DynamoDB for feed storage + PostgreSQL for event ingestion**
>
> Use a hybrid approach:
> - **PostgreSQL** stores the canonical event log (what happened, to whom, when). This is the source of truth. Writes are single-row inserts — no fan-out.
> - **DynamoDB** stores the materialised feed per user. A background worker reads from the event log, applies subscription rules, and writes fan-out entries to DynamoDB. Reads go directly to DynamoDB.
>
> **Why this combination:**
> - PostgreSQL handles the event ingestion workload it's good at (relational writes, strong consistency for the source of truth) and the team already knows it
> - DynamoDB handles the read pattern it's good at (key-value lookup by user_id, sorted by timestamp, consistent low latency at scale)
> - The fan-out happens asynchronously, decoupling write latency from fan-out complexity
> - DynamoDB auto-scales for read spikes without capacity planning anxiety
>
> **Anti-Recommendation: Pure PostgreSQL**
> It's tempting because the team knows it well, but the fan-out-on-write pattern (100+ inserts per event into per-user feed tables) will strain connection pools and make write latency unpredictable at scale. PostgreSQL is the right tool for the event log but not for the materialised feed at this volume.
>
> **Reconsider If:**
> - Scale stays under 10K events/hour: PostgreSQL alone is sufficient. Don't add DynamoDB complexity for a workload PostgreSQL can handle.
> - Team struggles with DynamoDB: Redis Sorted Sets are a simpler alternative for the feed layer, but watch memory costs as the event corpus grows.
> - Read latency requirements relax to 200ms+: PostgreSQL with aggressive caching may suffice.

## Tuning Notes

- **"Just use Postgres":** For most workloads at most scales, this is the right answer. Only reach for a specialised database when PostgreSQL can't meet a specific, measured requirement.
- **New database = new operational burden:** Every database you add is another thing to monitor, back up, upgrade, and debug at 3am. Factor this into the decision heavily.
- **Managed vs. self-hosted:** Default to managed (RDS, DynamoDB, ElastiCache) unless you have a specific reason to self-host. The operational cost of managing databases is almost always higher than the licensing cost.
- **Proof of concept first:** Before committing, build a small POC with realistic data volumes and access patterns. Benchmark the actual query performance — don't rely on marketing claims.
