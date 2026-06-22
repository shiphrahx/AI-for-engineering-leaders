---
name: database-selection-guide
description: >
  Produces a database recommendation for a specific workload — workload analysis, a 3-4 candidate
  comparison matrix, operational considerations, a justified recommendation with reconsider-if
  conditions, and an anti-recommendation. Use when the user says "which database should I use",
  "Postgres vs Dynamo vs ...", "pick a datastore for [workload]", or describes a new workload
  needing storage. Use this to CHOOSE the database; use data-model-design to design the schema once
  chosen, and caching-strategy when the read-latency answer is a cache rather than a new datastore.
---

# Database Selection Guide

Choose a datastore from the workload, not the marketing — weighing operational cost and team expertise, because every database you add is another thing to monitor, back up, upgrade, and debug at 3am.

## Inputs to gather

Gather these before recommending. If any are missing, ask in a single batched question — never invent scale, consistency needs, or team expertise. Mark anything genuinely unavailable as **Unknown** in the output.

- **Workload** — what the data is and what the service does
- **Access patterns** — read/write ratio, query shapes, fan-out
- **Scale** — data volume and throughput, now and projected
- **Consistency requirements** — strong vs eventual, latency targets
- **Team context** — expertise, operational capacity, cloud provider

## Steps

1. Confirm inputs. If scale, consistency needs, or team expertise are unstated, ask — team expertise in particular is decisive. Mark gaps **Unknown**.
2. Write the **Workload analysis** — data shape, access patterns (including fan-out), consistency, latency targets, and projected scale.
3. Pick **3-4 candidate databases** and assess each against every requirement. Always include the "just use Postgres" option as a baseline — it's the right answer more often than not.
4. Build the **Comparison matrix** — candidates as columns, scored on data-model fit, write throughput, read latency, scale/storage, operational complexity, and cost at scale.
5. Cover **Operational considerations** — who manages it, team expertise, cost, ecosystem; weigh operational burden heavily and default to managed services (RDS, DynamoDB, ElastiCache) unless there's a specific reason to self-host.
6. Make the **Recommendation** — which database (or hybrid: source-of-truth DB + materialised read store, which often beats forcing one DB to do everything), mapped to each requirement, with explicit reconsider-if conditions.
7. Give the **Anti-recommendation** — the tempting-but-wrong option and exactly why it fails this workload.
8. Adapt to context: factor the new operational burden heavily (monitoring, backups, upgrades, 3am debugging). Default to managed over self-hosted. Recommend a POC with realistic data volumes before committing — benchmark real query performance, not marketing claims. For uncertain scale, recommend the simpler option now with a documented trigger for migrating later.
9. Assemble the output in the format below.

## Output format

```
**Database Selection: [Workload]**

**Workload Summary**
[Data shape, access pattern, consistency, scale]

**Candidates**
| | [DB A] | [DB B] | [DB C] | [DB D] |
|---|---|---|---|---|
| Data model fit | | | | |
| Write throughput | | | | |
| Read latency | | | | |
| Scale/storage | | | | |
| Operational complexity | | | | |
| Cost at scale | | | | |

**Recommendation: [DB or hybrid]**
[Why, mapped to each requirement]

**Anti-Recommendation: [Tempting option]**
[Why it's wrong for this workload]

**Reconsider If:**
- [Condition → alternative]
```

## Boundaries

- Never fabricate scale numbers, consistency needs, or cost figures — mark them **Unknown**; cost estimates are rough and require the user to model real pricing.
- Never recommend a database the team can't operate without naming the operational burden and the skill gap.
- Never claim a winner from marketing claims alone — recommend a POC benchmark before committing.
- Team expertise is decisive and only the user knows it — weight familiarity heavily and surface it as a deciding factor.

## Chaining

- After this, offer **data-model-design** to design the schema and indexes for the chosen database.
- If the real problem is read latency rather than the wrong database, offer **caching-strategy** instead.
