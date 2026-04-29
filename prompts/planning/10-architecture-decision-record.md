# Architecture Decision Record (ADR)

## Situation

Your team just made a significant technical decision — choosing a database, selecting an architecture pattern, picking a framework. You need to document the decision so future engineers understand not just *what* was decided, but *why* — and what context made it the right call.

## The Prompt

```
You are an engineering leader documenting an architecture decision. Write an ADR (Architecture Decision Record) that captures the context, decision, and trade-offs. The audience is future engineers who will inherit this system and wonder "why did they do it this way?"

Structure:
1. **Title** — ADR-NNN: [Decision statement]
2. **Status** — Proposed / Accepted / Deprecated / Superseded
3. **Context** — what situation or problem led to this decision? Include constraints and forces at play
4. **Decision** — what we decided and why
5. **Alternatives considered** — what else we evaluated, with brief pros/cons
6. **Consequences** — positive and negative outcomes of this decision
7. **Revisit triggers** — conditions under which we should reconsider this decision

Decision made: [DESCRIBE_DECISION]
Context: [DESCRIBE_CONTEXT]
Alternatives: [DESCRIBE_ALTERNATIVES]
```

## Example Input

```
Decision: Use Redis Cluster for session storage instead of DynamoDB or in-memory sessions
Context: Our session storage is currently in-memory on each app server. When we auto-scale or deploy, sessions are lost and users get logged out. We need external session storage that handles 15K concurrent sessions, sub-5ms reads, and works with our existing Node.js stack. Budget is a consideration — we're a 30-person startup.
Alternatives: DynamoDB (AWS managed), Memcached, PostgreSQL (we already have it)
```

## Example Output

> **ADR-017: Use Redis Cluster for Session Storage**
>
> **Status:** Accepted (March 2025)
>
> **Context**
> Sessions are currently stored in-memory on application servers. This means sessions are lost during deployments and auto-scaling events, causing users to be logged out unexpectedly. This has generated 43 support tickets in the last quarter and is our #3 complaint in NPS surveys. We need an external session store that supports 15K concurrent sessions, sub-5ms read latency, and integrates with our Node.js/Express stack. As a 30-person startup, we need to balance operational simplicity with cost.
>
> **Decision**
> We will use Redis Cluster (AWS ElastiCache) for session storage. Sessions will be stored as JSON with a 24-hour TTL. The existing `express-session` middleware will be configured with `connect-redis` — a well-maintained adapter that requires minimal code changes.
>
> **Why Redis over the alternatives:**
> - Closest fit to our requirements on latency (<1ms typical vs. 5-10ms for DynamoDB)
> - The team already has Redis experience from our caching layer
> - `connect-redis` is the most battle-tested session adapter in the Node.js ecosystem
> - Cost: ~$150/month for our expected usage on ElastiCache
>
> **Alternatives Considered**
> - **DynamoDB:** Fully managed, scales well, but latency is 5-10ms (above our comfort zone for session reads on every request). DynamoDB's pricing model (per-request) could get expensive at 15K concurrent sessions. Also requires a custom session adapter.
> - **Memcached:** Similar performance to Redis but lacks persistence. If the cluster restarts, all sessions are lost — the same problem we're trying to solve. No native data structure support for future session enrichment.
> - **PostgreSQL (existing):** We already run it, so no new infrastructure. But adding 15K concurrent session reads to our primary database is a latency and load risk. Session access patterns (high-frequency small reads) are a poor fit for a relational database.
>
> **Consequences**
> *Positive:*
> - Users will no longer be logged out during deployments or scaling events
> - Sub-millisecond session reads improve response times across the application
> - Redis can be reused for other use cases (rate limiting, feature flags) later
>
> *Negative:*
> - New infrastructure to manage (ElastiCache cluster), though managed service reduces ops burden
> - Redis is single-threaded per shard — if we grow past 100K concurrent sessions, we'll need to revisit sharding strategy
> - Team needs to handle Redis connection failures gracefully (circuit breaker pattern)
>
> **Revisit Triggers**
> - Concurrent sessions exceed 100K (Redis sharding complexity may warrant DynamoDB)
> - AWS releases a low-latency DynamoDB option (<2ms) that changes the cost-latency trade-off
> - We move off AWS (Redis is portable, but ElastiCache is not)

## Tuning Notes

- **Controversial decision:** Expand "Alternatives Considered" and be generous to the rejected options. The ADR should demonstrate that the decision was thoughtful, not predetermined.
- **Reversible decision:** Note the reversal cost. "Switching from Redis to DynamoDB later would require ~2 days of work and a session migration script." Low reversal cost = less rigour needed.
- **Template for your org:** Adopt a consistent numbering scheme (ADR-001, ADR-002) and keep them in a `docs/decisions/` folder in your repo. Link to ADRs from code comments where relevant.
- **Quick decisions:** Not every choice needs a full ADR. Reserve them for decisions that are expensive to reverse, affect multiple teams, or that you've seen debated more than once.
