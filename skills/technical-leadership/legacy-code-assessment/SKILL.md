---
name: legacy-code-assessment
description: >
  Assesses an inherited, aging, or unloved area of code and lands a defensible call: invest
  (improve in place), rewrite (replace it), or leave (don't touch it yet) — with the evidence,
  the cost of each path, and the trigger that would change the answer. Use when the user says
  "should we rewrite this", "what do we do with this legacy service", "is this worth fixing", or
  inherited a system and must decide how to treat it. Use this to make the invest/rewrite/leave
  call on existing code — use codebase-orientation-brief first to understand unfamiliar code, and
  tech-debt-prioritisation to rank many debt items across the codebase.
variants: [startup, growth, enterprise]
---

# Legacy Code Assessment

Make the call on a piece of legacy code — invest, rewrite, or leave — on evidence, not disgust. Ugly code that works and rarely changes is often best left alone; the assessment weighs real cost of ownership against the cost and risk of change, and names the trigger that would flip the decision.

## Inputs to gather

Gather these before assessing. If any are missing, ask for them in a single batched question — never invent change frequency, incident history, or business criticality. Mark anything genuinely unavailable as **Unknown**.

- **The code** — the system/module in question (path or description the agent can inspect)
- **Business role** — how critical it is, who depends on it, and what breaks if it's down or wrong
- **Change pressure** — how often it changes now and whether upcoming work needs to touch it (dead code is cheap to leave; hot code is not)
- **Pain evidence** — bug/incident history, time lost working in it, onboarding difficulty, test coverage
- **Constraints** — team capacity, deadlines, and any hard limits (compliance, data migration risk)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Establish **cost of ownership now**: how much pain this code actually causes — change frequency × difficulty, incidents, time lost, risk carried. Separate "offends me aesthetically" from "costs us real time or reliability". Only the latter justifies spend.
2. Establish **business role and blast radius**: criticality, dependents, and what a mistake here costs. High-criticality code raises the bar for a rewrite (more risk) and can also justify investment (more at stake).
3. Assess **changeability**: test coverage, coupling, documentation, and whether the team understands it. This sets how safe *any* change is and heavily shapes rewrite risk.
4. Cost the three paths honestly:
   - **Invest** — refactor/harden in place: cost, and whether the code is structured enough that investment compounds rather than polishing something doomed.
   - **Rewrite** — replace it: full cost including migration, parallel-run, and the well-known risk that rewrites take longer than expected and reintroduce old bugs.
   - **Leave** — do nothing now: valid when the code is stable and rarely touched; state the risk you're accepting.
5. Weigh against **capacity and timing** — the right call also depends on what else the team must ship. A rewrite that's technically ideal but starves the roadmap is the wrong call.
6. Land a clear **verdict** — Invest, Rewrite, or Leave — leading with it and the single strongest reason. Avoid the trap of defaulting to rewrite because reading old code is unpleasant.
7. Name the **trigger** that would change the decision ("leave — but if we need to add multi-currency, reassess for a rewrite") so the call has a shelf life and a review point.
8. Adapt to context (see Variants) and assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Legacy Assessment: [system]** — Verdict: [Invest / Rewrite / Leave]

_[One-line strongest reason.]_

**Cost of ownership now**
- Change frequency / difficulty: [evidence]
- Incidents / time lost: [evidence or Unknown]

**Business role & blast radius**
- [Criticality, dependents, cost of a mistake]

**Changeability**
- Tests / coupling / understanding: [state]

**The three paths**
| Path | Cost | Risk | Notes |
|------|------|------|-------|
| Invest | [..] | [..] | [..] |
| Rewrite | [..] | [..] | [..] |
| Leave | [..] | [..] | [..] |

**Verdict:** [Invest/Rewrite/Leave — why.]
**Trigger to reassess:** [What would change this call.]
```

## Variants

Optional org-size tuning (see [`docs/VARIANTS.md`](../../../docs/VARIANTS.md)). Default to **growth** if the user doesn't state a stage.

- **startup** (≤ ~15 engineers): bias toward Leave or targeted Invest — rewrites are expensive bets a small team rarely affords; keep the memo to cost-now, verdict, and trigger.
- **growth** (~15–80): the full three-path costing above.
- **enterprise** (80+): add migration/compliance risk, cross-team dependents, and required sign-off for a rewrite; note strangler-fig incremental-replacement as a middle path between invest and full rewrite.

## Boundaries

What the skill must never do.

- Never recommend a rewrite on aesthetics — require evidence of real cost of ownership.
- Never fabricate incident history, change frequency, or coverage — mark **Unknown** and note it weakens the call.
- Never ignore migration and parallel-run cost when costing a rewrite — that's where rewrites overrun.
- Never treat "leave" as failure — for stable, rarely-touched code it's often the correct, disciplined call.
- Never make the call without a reassess trigger — decisions on legacy code expire.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- After this, offer **migration-plan** when the verdict is Rewrite and needs a phased, safe replacement plan.
- After this, offer **tech-debt-prioritisation** when the verdict is Invest and the work should be ranked against other debt.
