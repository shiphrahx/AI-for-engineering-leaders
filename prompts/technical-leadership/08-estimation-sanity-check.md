# Estimation Sanity Check

## Situation

An engineer or team gave you an estimate and you're about to commit it upward — but you want to pressure-test it against the actual code and scope first. You want the hidden work, the optimistic assumptions, and a realistic range with a confidence level.

## The Prompt

```
You are stress-testing an estimate before an engineering leader commits it upward. Don't re-estimate from scratch — find what the number MISSES. Be collaborative, not gotcha; the estimator is usually closer to the work than the reviewer.

Produce:
1. Original — the estimate and its assumed scope.
2. Hidden / likely-omitted work — tests, migrations, edge cases, error handling, review/rework, rollout, docs, coordination. Say whether each is plausibly in the number.
3. Assumptions that may not hold — happy-path only? assumes the estimator does it? no interruptions/on-call?
4. Revised range — best / likely / worst (NOT a single number), with the drivers of the spread.
5. Confidence — High / Medium / Low, and what would raise it.
6. Recommendation — commit / commit-with-buffer / de-risk-first (spike or slice).

Estimate: [NUMBER_AND_WHO_GAVE_IT]
The work: [WHAT_S_BEING_BUILT_AND_CODE_IT_TOUCHES]
Assumptions stated: [WHAT_THE_ESTIMATE_ASSUMED]
Track record: [HOW_PAST_ESTIMATES_LANDED_IF_KNOWN]
```

## Example Input

```
Estimate: "1 week", from a mid-level engineer, to add CSV export to the reporting page.
The work: New export button, generate CSV from the existing report query, stream download.
Assumptions stated: None — it was a gut estimate in standup.
Track record: This engineer's estimates usually run ~50% over.
```

## Example Output

> **Estimate Sanity Check: CSV export on reporting page**
>
> **Original:** "1 week", mid-level engineer, gut estimate, scope assumed = button + query-to-CSV + download.
>
> **Hidden / likely-omitted work**
> - Large-report handling (streaming vs timeout) — not in the number; the report query is already slow.
> - Escaping/encoding edge cases (commas, unicode, formulas) — not accounted for.
> - Tests + a rollout behind a flag — not counted.
>
> **Assumptions that may not hold**
> - Assumes the existing report query returns fast enough to export synchronously — for big accounts it may not.
> - Assumes uninterrupted work; estimator's history runs ~50% over.
>
> **Revised range**
> - Best: 1 week · Likely: 1.5-2 weeks · Worst: 3 weeks (if async generation is needed).
> - Spread driven by: whether large reports force async/background generation.
>
> **Confidence: Medium** — a half-day check of the report query's performance at the largest account would raise it to High.
>
> **Recommendation:** Commit the likely case (2 weeks) with a buffer, or spend half a day confirming the large-report path first to tighten it.

## Tuning Notes

- **Not a blame exercise:** Frame it as stress-testing the estimate, not the estimator. Keep the tone collaborative.
- **Track record is data:** If the team chronically underestimates, say so and widen the range — don't pretend the pattern isn't there.
- **Common pitfall:** The model may replace the estimate with a confident single number. Insist on a range and named uncertainty.
- **Low confidence:** When confidence is low, the right answer is often "de-risk first with a spike," not a padded number nobody believes.
