---
name: data-model-design
description: >
  Produces a data model for a new domain — access patterns, entity definitions with fields and
  constraints, relationships and cardinality, indexes tied to access patterns, evolution
  considerations, and explicit trade-offs. Use when the user says "design the schema/data model",
  "tables for [feature]", "how should I model X", or describes a domain needing storage. Use this to
  design the schema for a chosen database; use database-selection-guide to choose the database first,
  and api-contract-design for the request/response shapes rather than the storage layout.
---

# Data Model Design

Design the schema optimised for the actual query patterns, not theoretical normalisation purity — documenting the access patterns that drove each decision and the trade-offs made.

## Inputs to gather

Gather these before designing. If any are missing, ask in a single batched question — never invent access patterns, scale, or the database technology. Mark anything genuinely unavailable as **Unknown** in the output.

- **Domain** — what the data represents in business terms
- **Database technology** — the chosen datastore
- **Access patterns** — the key queries the application will run
- **Expected scale** — data volume per entity

## Steps

1. Confirm inputs. If the access patterns or database aren't given, ask — the model is driven by queries, not entities. Mark gaps **Unknown**.
2. Write the **Domain overview** — what this data represents in business terms.
3. List the **Access patterns** — the top 5-10 read and write queries, each tagged with frequency and latency sensitivity. These drive every later decision; state which query each is optimising for.
4. Define the **Entities** — each with fields, types, constraints, keys, and a rationale for non-obvious decisions (e.g. why a status is denormalised onto a row). Use the target database's idioms (SQL DDL for relational; document/key shapes for NoSQL).
5. Document the **Relationships** — how entities relate, with cardinality.
6. Specify the **Indexes** — each tied explicitly to the access pattern it serves; note where one index covers several patterns.
7. Cover **Evolution considerations** — how the model absorbs likely future requirements (subtasks, labels, soft deletes, partitioning) with minimal disruption.
8. State the **Trade-offs** — what you optimised for and what you sacrificed (normalisation vs query speed, audit table vs triggers, hard vs soft deletes).
9. Adapt to context: for a NoSQL database, replace the relational model with document/key structures designed around the access patterns, not entities. For an event-sourced model, replace mutable entities with an event log where current state is a replay. For a migration (not greenfield), add a migration plan showing how to evolve from the old schema without downtime. Recommend sharing the access patterns with the team for review before locking the model.
10. Assemble the output in the format below.

## Output format

```
**Data Model: [Domain]**

**Access Patterns (driving design decisions)**
1. [Query] → [frequency, latency sensitivity]

**Entities**
[DDL or document/key structures with fields, types, constraints; inline rationale for key decisions]

**Relationships**
[Entity ↔ entity with cardinality]

**Indexes**
[Each index tied to the access pattern it serves]

**Trade-offs**
- **[Decision]:** [what was optimised vs sacrificed]

**Evolution Considerations**
- *[Future requirement]:* [how the model absorbs it]
```

## Boundaries

- Never fabricate access patterns, scale, or the database choice — mark them **Unknown**; the access patterns are what justify the whole model.
- Never optimise for normalisation purity over the stated query patterns — every denormalisation must name the query it serves.
- Never add an index that isn't tied to a documented access pattern.
- Make trade-offs explicit — never present one design as the only option without naming what it sacrifices.

## Chaining

- This commonly follows **database-selection-guide** (which picks the datastore this schema targets).
- After this, offer **api-contract-design** to design the API surface over these entities.
