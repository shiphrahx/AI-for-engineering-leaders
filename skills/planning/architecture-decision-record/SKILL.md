---
name: architecture-decision-record
description: >
  Produces an Architecture Decision Record (ADR) capturing a significant technical decision:
  title, status, context and forces, the decision and why, alternatives considered with
  pros/cons, positive and negative consequences, and revisit triggers. Use when the user says
  "write an ADR", "document this decision", or describes a database/framework/architecture
  choice already made and wants the rationale recorded. Use this to record a decision already
  taken — use rfc-outline to propose one not yet decided, or build-vs-buy-analysis to make a
  make/buy call.
---

# Architecture Decision Record (ADR)

Capture a significant technical decision so future engineers understand not just *what* was decided but *why* — and what context made it the right call at the time.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent the context, constraints, or alternatives. Mark anything genuinely unavailable as **Unknown**.

- **Decision made** — what was decided
- **Context** — the situation/problem that led to it, including constraints and forces at play
- **Alternatives** — what else was evaluated
- **Status** — proposed / accepted / deprecated / superseded, and the date
- **Reversal cost** — how hard it would be to undo, if known

## Steps

1. Write the **title** — `ADR-NNN: [decision statement]` — stated as a decision, not a question.
2. State the **status** (proposed / accepted / deprecated / superseded) and date.
3. Write the **context** — the situation or problem that forced the decision, with constraints and competing forces (cost, latency, team experience, scale). Ground it in evidence (tickets, NPS, incidents) where available; mark missing data **Unknown**.
4. State the **decision** — what was chosen and the specific reasons it beat the alternatives.
5. Write **alternatives considered** — each option with brief pros and cons and why it lost. Be generous to the rejected options; the ADR should show the decision was thoughtful, not predetermined.
6. Write **consequences** — split into positive and negative; name the real downsides and the conditions under which they bite (e.g. "Redis is single-threaded per shard — revisit past 100K concurrent sessions").
7. Write **revisit triggers** — concrete conditions under which the decision should be reconsidered.
8. Adapt to context: for a controversial decision, expand the alternatives and be especially fair to them. For a reversible decision, note the reversal cost ("~2 days plus a migration script") — low reversal cost means less rigour is warranted. Keep a consistent numbering scheme and a `docs/decisions/` home; reserve full ADRs for decisions that are costly to reverse, span multiple teams, or have been debated more than once.
9. Assemble the output in the format below.

## Output format

```
**ADR-[NNN]: [Decision statement]**

**Status:** [Proposed / Accepted / Deprecated / Superseded] ([date])

**Context**
[Situation/problem, constraints, forces. Evidence where available.]

**Decision**
[What was chosen and why it beat the alternatives.]

**Alternatives Considered**
- **[Alternative]:** [pros; cons; why not chosen]

**Consequences**
*Positive:*
- [outcome]

*Negative:*
- [downside and when it bites]

**Revisit Triggers**
- [Concrete condition under which to reconsider]
```

## Boundaries

- Never invent the context, evidence, constraints, or alternatives — mark them **Unknown**.
- Never strawman the rejected alternatives — record them at their strongest so the decision reads as considered.
- Never omit the negative consequences — an ADR with only upside isn't trustworthy or useful later.
- Never record a decision as accepted if the user described it as still under debate — set status to Proposed.

## Chaining

- No natural successor — this is usually a terminal artifact, the durable record of a decision.
