# Architecture Review Prep

## Situation

You're presenting a technical design to an architecture review board, a staff engineer group, or a cross-team review. You need to prepare not just the design, but for the tough questions. The best-prepared presenter has already thought through the objections.

## The Prompt

```
You are an engineer preparing to present a technical design for peer review. Anticipate the hard questions reviewers will ask and prepare concise answers. Structure your presentation for a 30-minute review with 15 minutes of Q&A.

Structure:
1. **Presentation outline** — what to cover in 30 minutes, timed
2. **Key decisions to highlight** — the 3-4 design choices most likely to generate discussion
3. **Anticipated questions** — 10-15 tough questions reviewers might ask, with prepared answers
4. **"I don't know yet" list** — questions you genuinely haven't resolved (it's okay to say this)
5. **What you need from reviewers** — specific feedback you're asking for

Design: [DESCRIBE_YOUR_DESIGN]
Audience: [WHO_ARE_THE_REVIEWERS]
Controversial aspects: [WHAT_MIGHT_PEOPLE_DISAGREE_WITH]
```

## Example Input

```
Design: Moving from a monolithic PostgreSQL database to an event-sourced architecture with separate read/write models (CQRS) for the order management system. Events stored in Kafka, read models projected into PostgreSQL and Elasticsearch.
Audience: 3 Staff engineers, 2 EMs, 1 Principal engineer. Mix of experience — some have done event sourcing before, some haven't.
Controversial: Event sourcing adds significant complexity. Some reviewers will ask "why not just optimise the existing database?" Also, introducing Kafka is a new operational dependency we haven't run before.
```

## Example Output

> **Architecture Review Prep: Order Management CQRS + Event Sourcing**
>
> **Presentation Outline (30 minutes)**
> - 0-5 min: Problem statement and why the current approach won't scale (data + charts)
> - 5-12 min: Proposed architecture with component diagram
> - 12-18 min: Data flow walkthrough for the 2 key use cases (order placement, order query)
> - 18-23 min: Alternatives considered and why they were rejected
> - 23-27 min: Migration plan (phased, with rollback)
> - 27-30 min: Open questions and what you need from reviewers
>
> **Key Decisions to Highlight**
> 1. Event sourcing over traditional CRUD — enables full audit trail and temporal queries but adds complexity
> 2. Kafka as the event store — operational dependency vs. purpose-built event store
> 3. Separate read models in PostgreSQL and Elasticsearch — eventual consistency trade-off
> 4. Phased migration — dual-write period with reconciliation
>
> **Anticipated Questions and Prepared Answers**
>
> *"Why not just optimise PostgreSQL? Have you tried read replicas / better indexing / query optimisation?"*
> → "We've done all three. Read replicas helped with analytics, but the core problem is that our write model and read model have fundamentally different access patterns. Optimising for one hurts the other. The numbers: [specific metrics showing the conflict]."
>
> *"Event sourcing is complex. How does the team ramp up?"*
> → "Acknowledged. We're planning a 2-week spike for the two engineers who'll build the core, and we'll pair extensively. The event sourcing patterns we need are well-scoped — we're not building a generic framework."
>
> *"What happens during the eventual consistency window?"*
> → "Read models may be up to 2 seconds behind writes. For the order detail page, this is acceptable — a user placing an order sees a confirmation immediately (from the write path), and the order list updates within 2 seconds. We'll add UI indicators where freshness matters."
>
> *"Why Kafka and not [Pulsar / EventStoreDB / SQS]?"*
> → "Kafka because: (a) 3 teams at the company already use it, so operational knowledge exists, (b) it serves as both the event log and the pub/sub transport, (c) our infrastructure team has capacity to support it. EventStoreDB was considered but adds a technology nobody knows."
>
> *"What's the rollback plan if event sourcing doesn't work?"*
> → "During the dual-write phase, the original PostgreSQL database stays the source of truth. We can revert by simply turning off the event pipeline and removing the new read models. There's no point of no return until we decommission the old write path, which is Phase 3."
>
> **"I Don't Know Yet" List**
> - Exact Kafka partition strategy for order events (need to benchmark key distribution)
> - Whether we need schema registry from day one or can add it later
> - How to handle event schema evolution (versioning strategy TBD)
>
> **What I Need From Reviewers**
> 1. Is the phased migration plan credible? Are the go/no-go criteria for each phase the right ones?
> 2. Are there failure modes I haven't considered in the eventual consistency model?
> 3. Does the team's skill gap concern you enough to recommend a different approach?

## Tuning Notes

- **Friendly review (your own team):** Focus less on anticipating objections and more on getting design input. Bring options, not a finished proposal.
- **Adversarial review (principal engineers, architecture board):** Over-prepare. Know your numbers. The worst answer is "I haven't thought about that."
- **Remote review:** Send the design doc 48 hours before the meeting. This lets reviewers read in advance and come with specific questions rather than spending the meeting reading.
- **You're the reviewer, not the presenter:** Ask "what's the simplest version of this that achieves the goal?" and "what happens when X fails?" These two questions surface more issues than any other.
