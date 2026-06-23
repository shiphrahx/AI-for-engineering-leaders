---
name: pipeline-analytics-review
description: >
  Produces a hiring-funnel analysis — stage-by-stage conversion (with an ASCII funnel), a
  one-sentence key finding, bottleneck and drop-off diagnosis, source effectiveness, quality
  indicators, and the top 3 improvements — to cut time-to-hire and lift conversion. Use when
  the user says "review my hiring pipeline", "where are candidates dropping off", "analyze the
  funnel", "quarterly hiring review", or pastes pipeline metrics. Use this for AGGREGATE funnel
  diagnosis across many candidates — not for evaluating one candidate (candidate-evaluation-summary),
  nor for deciding which roles to open (hiring-plan).
---

# Pipeline Analytics Review

Turn pipeline metrics into a diagnosis: where candidates are lost, whether to speed or quality, which sources work, and the three changes that move the funnel most.

## Inputs to gather

Gather these before analyzing. If any are missing, ask for them in a single batched question — never invent counts, conversion rates, or drop-off reasons. Mark anything genuinely unavailable as **Unknown** in the output.

- **Time period and roles** — what window and which roles the data covers
- **Funnel data** — counts at each stage (applied → screen → take-home → on-site → offer → accepted)
- **Time metrics** — days at each stage and total time-to-hire
- **Source data** — where candidates came from and which sources produced hires
- **Drop-off reasons** — where known
- **Quality data** — offer acceptance, 90-day retention, recent-hire performance, if instrumented

## Steps

1. Calculate **conversion rates** at each stage and render an ASCII funnel with bars and percentages.
2. Compare conversions and timings against healthy benchmarks to spot bottlenecks (low conversion or long delays). Benchmarks: Application→Screen 20-30% (investigate if <15% or >50%), Screen→Technical 60-80% (<50%), Technical→Onsite 50-70% (<40%), Onsite→Offer 30-50% (<20%), Offer→Accept 70-90% (<60%); screen scheduling <5 days (>7), total time-to-hire 21-35 days (>45).
3. Write a **one-sentence key finding** that names the dominant problem ("We're losing candidates to speed, not quality").
4. Diagnose **bottlenecks**: for each, the stage, the metric, and the candidate-experience reason it matters — connect delays to drop-off where the data supports it.
5. Build **source effectiveness** as a table: applied, hired, conversion-to-hire, and a quality note per source. Watch the common pattern that referrals convert 3-5x job boards.
6. Do **drop-off analysis**: per leaky stage, how many left and the known reasons or a clearly-labeled hypothesis. Map the common patterns — high-apply/low-screen (wrong-fit JD or over-strict screen), low take-home return (too long / too slow / competing offers), low offer-accept (comp, speed, or experience).
7. Cover **quality indicators**: offer acceptance, 90-day retention, recent-hire performance. If quality isn't instrumented, say so explicitly and flag it as a gap — funnel efficiency says nothing about whether hires are good; recommend a 90-day check-in so the next review can correlate source/process against quality.
8. Give the **top 3 (or 4) recommendations**, each with the expected impact ("recovers X candidates" or "saves Y days") and a concrete mechanism.
9. Adapt to context: for **small samples** (<20 candidates), treat percentages as noisy and lead with qualitative patterns; for **multiple roles**, break the funnel out per role — a combined funnel masks junior-vs-senior differences; if the ATS tracks it, review **conversion by demographic group** at each stage, since uneven drop-off can indicate stage-specific bias; recommend **sharing metrics with interviewers** to motivate fast reviews.
10. Assemble the output in the format below.
11. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Pipeline Analytics: [Role], [Period]**

**Funnel**
```
Applied        [N]  ████████████████ 100%
[Stage]        [N]  ████             [%]
...
```

**Key Finding:** [One sentence: "We're losing candidates to X, not Y."]

**Bottlenecks**
1. **[Stage]: [metric]** — [why it matters, candidate impact]

**Source Effectiveness**
| Source | Applied | Hired | Conversion | Quality |
|--------|---------|-------|------------|---------|
| [source] | [N] | [N] | [%] | [note] |

**Drop-off Analysis**
- [Stage]: [count] dropped — reasons: [known or labeled hypothesis]

**Quality Indicators**
- [Acceptance / retention / performance, or "not yet measurable — gap"]

**Recommendations**
1. **[Change]** — [expected impact: recovers X candidates / saves Y days] via [mechanism]
```

## Boundaries

- Never fabricate counts, conversion rates, timings, source data, or drop-off reasons — mark unknowns as **Unknown** and label any inferred drop-off cause as a hypothesis.
- Never present noisy small-sample percentages as firm conclusions; say when n is too small.
- Never assess hire quality beyond what the user instrumented — funnel data alone cannot tell you if hires are good.
- Never optimize for speed at the expense of quality without flagging the trade-off; recommend quality instrumentation if it's missing.

## Chaining

- After this, offer **hiring-plan** to act on the findings (re-prioritize roles, reallocate sourcing investment).
- If a specific stage is leaking (e.g. take-home non-returns), offer the relevant fix skill — **take-home-exercise-design** to shorten the exercise, or **phone-screen-script** to speed screening.
