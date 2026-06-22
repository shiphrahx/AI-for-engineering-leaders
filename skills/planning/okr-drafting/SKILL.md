---
name: okr-drafting
description: >
  Produces team-level OKRs — 2-3 ambitious qualitative Objectives, each with 2-4 specific,
  measurable Key Results (metric, baseline, target, measurement method), with cross-team
  dependencies flagged. Use when the user says "draft OKRs", "turn these company goals into
  team OKRs", or pastes vague department goals plus current baselines. Use this for the
  measurable goal-setting layer — use quarterly-roadmap for the work that delivers the goals,
  and engineering-strategy-one-pager for the higher-level direction behind them.
---

# OKR Drafting

Translate vague company or department goals into team-level OKRs — Objectives that are ambitious and qualitative, Key Results that are specific, measurable, and verifiable at quarter-end as definitively achieved or not.

## Inputs to gather

Gather these before drafting. If any are missing, ask for them in a single batched question — never invent baselines, targets, or measurement methods. Mark anything genuinely unavailable as **Unknown**.

- **Team** — name and size
- **Quarter** — the period
- **Company / department goals** — the higher-level goals to translate (even if vague)
- **Current baselines** — present values for the metrics in play
- **Team context** — relevant capabilities, recent work, constraints

## Steps

1. Read the company goals and baselines. Each Objective should be ambitious and qualitative; each Key Result must be outcome-based and verifiable.
2. Draft **2–3 Objectives**, each a qualitative statement of the change the team is driving.
3. Under each Objective, write **2–4 Key Results**. For each KR give: the metric, the baseline (current value), the target, and how it will be measured. Mark a baseline **Unknown** rather than guessing — an unmeasurable KR is not a KR.
4. Avoid the output-vs-outcome trap: "ship feature X" is an output, not a KR. Reframe as the outcome ("reduce support tickets related to X by 40%"). If you can't articulate the outcome, flag that the work itself may be questionable. Avoid vanity metrics.
5. Set ambitious targets — OKRs are meant to stretch; hitting 70% is healthy, hitting 100% means the targets were too easy. Note this when targets look conservative.
6. Flag any KR that **depends on another team** (e.g. legal sign-off, a platform capability) so the dependency gets coordinated early.
7. Adapt to context: for a first-time OKR team, start with 2 Objectives and 2 KRs each — fewer and clearer beats a long list no one tracks. For inherited/mandated KRs handed down from above, keep the "what" but have the team own the "how".
8. Assemble the output in the format below.

## Output format

```
**[Team] — [Quarter] OKRs**

**Objective 1: [Ambitious, qualitative statement]**

| Key Result | Baseline | Target | Measurement |
|-----------|----------|--------|-------------|
| [outcome metric] | [current or Unknown] | [target] | [how/where measured, cadence] |

**Objective 2: [...]**

| Key Result | Baseline | Target | Measurement |
|-----------|----------|--------|-------------|

[2–3 Objectives total]

*Dependency note: [Objective N KR M] depends on [team/function] — coordinate by [when].*
```

## Boundaries

- Never invent baselines, targets, or measurement methods — mark them **Unknown**; an unmeasurable KR is not a KR.
- Never write an output as a Key Result — every KR must be an outcome verifiable as achieved or not at quarter-end.
- Never use vanity metrics (raw activity counts disconnected from impact).
- Never let the set grow past 2–3 Objectives — sprawl kills tracking.

## Chaining

- After this, offer **quarterly-roadmap** to plan the concrete deliverables that will move each Key Result.
