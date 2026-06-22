---
name: migration-plan
description: >
  Produces a phased, reversible migration plan from System A to System B: overview,
  measurable success criteria, phases (each with scope, duration, rollback, go/no-go gates,
  and owner), a risk register, a communication plan, and resource requirements. Use when the
  user says "plan a migration", "migrate from X to Y", or describes a database migration,
  framework upgrade, service decomposition, or cloud switch. Use this for the execution plan
  of a decided move — use rfc-outline to propose it and project-pre-mortem to stress-test it.
---

# Migration Plan

Turn a move from System A to System B into a phased plan that prioritises safety (zero data loss, minimal downtime), stays reversible at every phase, and reads clearly to both technical and non-technical stakeholders.

## Inputs to gather

Gather these before planning. If any are missing, ask for them in a single batched question — never invent scale figures, constraints, or team makeup. Mark anything genuinely unavailable as **Unknown**.

- **Migration** — from-system → to-system
- **Reason** — why migrating now
- **Scale** — data volume, traffic, services affected
- **Constraints** — downtime budget, data-loss tolerance, compliance/residency, code-change limits
- **Team** — who's available (SREs, DBAs, application engineers, consultants)

## Steps

1. Write the **overview** — what's moving, from where to where, and why, with the scale and services affected.
2. Write **success criteria** — measurable targets for "done" (e.g. downtime < 5 min, zero data loss, latency within 10% of baseline).
3. Break the work into **phases** — typically preparation, shadow/dual-run, cutover, decommission. Each phase states: scope, duration, rollback plan, go/no-go criteria for the next phase, and the owner. Every phase must be reversible; if a phase can't roll back, say so explicitly and treat it as a top risk.
4. Build a **risk register** — top risks with likelihood, impact, and mitigation; tie compliance/residency risks to a verification step.
5. Write a **communication plan** — who needs to know what, and when (kickoff, shadow-start, maintenance-window notice, cutover real-time channel, all-clear).
6. State **resource requirements** — people, tools, budget, and the cost delta (e.g. new infra cost offset by decommission savings).
7. Adapt to context: for an application-level migration (e.g. framework upgrade), replace replication phases with a feature-flag rollout (shadow → canary → full cutover). For a cloud-to-cloud move, add a data-transfer/egress cost line. For a smaller migration, condense to three phases (prep, migrate, verify) — not every migration needs a shadow period. For multiple stakeholders, add a RACI table per phase.
8. Assemble the output in the format below.

## Output format

```
**Migration Plan: [From System] → [To System]**

**Overview**
[What's moving, from/to, why, scale, services affected]

**Success Criteria**
- [Measurable target]

**Phase 1: [Name] ([Timeframe])**
- [Scope steps]
- *Go/no-go for Phase 2:* [criteria]
- *Rollback:* [procedure and production impact]
- *Owner:* [who or Unknown]

[Repeat per phase: ... Cutover ... Decommission]

**Risk Register**
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| [risk] | [L/M/H] | [L/M/H] | [mitigation] |

**Communication Plan**
- [Timing]: [audience and message]

**Resources**
[People, tools, budget, cost delta]
```

## Boundaries

- Never invent data volumes, traffic figures, downtime budgets, or compliance requirements — mark them **Unknown**.
- Never define a phase without a rollback plan and a go/no-go gate — if a step is genuinely irreversible, flag it as a top risk rather than omitting the rollback line.
- Never claim zero downtime or zero data loss as fact — state them as criteria to be verified, with the mechanism that achieves them.
- Never skip the communication plan for a migration touching multiple teams.

## Chaining

- After this, offer **project-pre-mortem** to stress-test the plan — imagine the migration failed and surface the failure modes before Phase 1 starts.
