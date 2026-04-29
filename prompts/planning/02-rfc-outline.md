# RFC Outline

## Situation

You need to propose a technical change that requires cross-team buy-in. Maybe it's a new service, a migration, or a change in architecture. An RFC (Request for Comments) gives the proposal structure and invites feedback before you commit engineering time.

## The Prompt

```
You are a senior engineer or engineering leader drafting an RFC (Request for Comments) for a proposed technical change. The RFC should be thorough enough to make a decision on, but concise enough that reviewers will actually read it. Optimise for clarity and decision-making, not comprehensiveness.

Structure:
1. **Title and metadata** — RFC number, author, date, status (draft/review/approved/rejected), reviewers
2. **Summary** — 3-4 sentences: what you're proposing, why, and the expected outcome
3. **Motivation** — what problem are we solving? Include data, customer complaints, or incidents that demonstrate the need
4. **Proposed solution** — what you want to build, with enough technical detail for reviewers to evaluate trade-offs
5. **Alternatives considered** — 2-3 other approaches you evaluated and why you didn't choose them
6. **Risks and mitigations** — what could go wrong and how you'd handle it
7. **Rollout plan** — how you'd ship this incrementally and safely
8. **Open questions** — things you want reviewer input on specifically
9. **Success criteria** — how you'll know this worked, with measurable outcomes

Proposed change:
[DESCRIBE_THE_CHANGE]

Problem context:
[DESCRIBE_THE_PROBLEM]

Technical constraints:
[CONSTRAINTS]
```

## Example Input

```
Proposed change: Replace our current REST API gateway with a GraphQL layer for our mobile and web clients. The GraphQL layer would sit in front of our existing microservices and handle query composition, caching, and rate limiting.

Problem: Mobile clients make 8-12 REST calls per screen load. This causes waterfall loading, excessive data transfer (we over-fetch by ~60%), and makes it hard to optimise per-client. Our mobile app's time-to-interactive is 3.2s and we need to get it under 1.5s.

Constraints: 14 microservices behind the current gateway, team has no GraphQL experience, can't disrupt existing web client during migration, must maintain backward compatibility for 6+ months.
```

## Example Output

> **RFC-042: GraphQL API Gateway for Client Optimisation**
>
> | Field | Value |
> |-------|-------|
> | Author | [Your name] |
> | Status | Draft |
> | Reviewers | [API Platform lead, Mobile lead, Security lead] |
> | Date | March 2025 |
>
> **Summary**
> We propose adding a GraphQL gateway layer in front of our existing microservices to reduce client-side API calls, eliminate over-fetching, and bring mobile time-to-interactive from 3.2s to under 1.5s. The GraphQL layer would compose data from existing REST services — no microservice changes required for the initial rollout.
>
> **Motivation**
> Our mobile app makes 8-12 REST calls per screen, creating waterfall loading patterns that directly impact time-to-interactive (currently 3.2s, target <1.5s). Analysis shows we over-fetch by approximately 60% — mobile receives full REST payloads when it needs a subset of fields. This wastes bandwidth (critical for users on slower connections) and increases parse time. Three of our top 10 mobile NPS complaints reference loading speed.
>
> **Proposed Solution**
> Introduce an Apollo-based GraphQL gateway that: (a) composes data from existing REST microservices using schema stitching, (b) allows clients to request exactly the fields they need, (c) implements server-side response caching with a 30-second TTL for read-heavy queries, (d) provides per-client rate limiting. The gateway runs as a standalone service; existing REST endpoints remain unchanged. Mobile migrates first, web follows.
>
> **Alternatives Considered**
> 1. **BFF (Backend for Frontend) per client** — custom REST endpoints per client type. Solves over-fetching but creates maintenance burden (N clients × M endpoints). Rejected due to long-term cost.
> 2. **REST API optimisation (sparse fieldsets, compound endpoints)** — lower risk but doesn't solve the waterfall problem and requires changes to every microservice. Estimated 2x the engineering effort for a partial solution.
> 3. **gRPC between clients and gateway** — high performance but poor browser support and steeper learning curve for frontend engineers.
>
> **Risks and Mitigations**
> - *Team has no GraphQL experience:* Mitigate with 2-week spike/training before full development. Consider hiring one GraphQL-experienced contractor for the first 3 months.
> - *N+1 query problem:* Mitigate with DataLoader pattern for batching downstream REST calls.
> - *Single point of failure:* Deploy with horizontal auto-scaling and circuit breakers to downstream services. Fallback: clients can hit REST directly if gateway is down.
>
> **Rollout Plan**
> 1. Spike: 2 weeks — prototype with 2 microservices, measure performance (Month 1)
> 2. MVP: GraphQL gateway for mobile home screen (3 services) (Month 2)
> 3. Expand: Cover all mobile screens (Month 3-4)
> 4. Web migration: Opt-in per page (Month 5-6)
> 5. REST deprecation: begin after 6 months of dual-running
>
> **Open Questions**
> 1. Should we build our own gateway or use a managed service (Apollo Router, AWS AppSync)?
> 2. How do we handle authentication — pass-through to existing JWT validation, or add a layer at the gateway?
> 3. What's our caching invalidation strategy for real-time data (e.g., order status)?
>
> **Success Criteria**
> - Mobile time-to-interactive < 1.5s (from 3.2s)
> - API calls per screen load < 3 (from 8-12)
> - Data transfer per screen load reduced by 50%+
> - No increase in P1 incidents attributable to the gateway

## Tuning Notes

- **Smaller change:** Scale down to just Summary, Motivation, Proposed Solution, and Rollout Plan. Not every RFC needs alternatives and open questions.
- **Controversial proposal:** Expand "Alternatives Considered" significantly and be generous to the alternatives. Reviewers will trust you more if they see you seriously considered other options.
- **Time-sensitive:** Add a "Decision deadline" to the metadata and a "Cost of delay" section in Motivation.
- **Your org doesn't do RFCs:** This format works equally well as a "Technical Design Doc" or "Architecture Proposal."
