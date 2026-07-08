# Spike Readout

## Situation

A spike or prototype is finished and you need to convert the learning into a decision — before it evaporates or the code quietly gets merged. You want a short memo: the answer, the evidence, a recommendation, and what's still open.

## The Prompt

```
You are writing up a finished spike as a decision memo. A spike that isn't written up is wasted. Report what happened honestly, including "inconclusive" when that's the truth.

Produce:
1. Question — what the spike set out to answer.
2. Answer — yes / no / inconclusive, in one or two sentences, up front.
3. What we did — briefly, enough to trust the answer.
4. Evidence — observations and numbers (mark anything not measured as Unknown; separate observed from inferred).
5. Recommendation — proceed / don't / proceed-with-conditions / one-more-spike (which).
6. Still open — risks the spike did not resolve.
7. Disposal — what's thrown away; what needs a proper build.

Question: [WHAT_THE_SPIKE_ASKED]
What was built/done: [PASTE]
Findings: [OBSERVATIONS_AND_NUMBERS]
Decision it feeds: [WHAT_CALL_BY_WHEN]
Time spent: [RAN_TO_TIMEBOX / CUT_SHORT]
```

## Example Input

```
Question: Can Postgres full-text search return relevant catalogue results under 200ms at 2M rows?
What was built/done: Loaded 2M rows, added a tsvector index, ran 20 representative queries.
Findings: p95 latency 140ms. Relevance good on exact terms, poor on typos/plurals. Index build took 4 min. Didn't test concurrent load.
Decision it feeds: Q3 search architecture, decide this week.
Time spent: Ran to the full 2 days.
```

## Example Output

> **Spike Readout: Postgres full-text search**
>
> **Question:** Can Postgres full-text search return relevant results under 200ms at 2M rows?
> **Answer:** Yes on latency, with a caveat — p95 was 140ms, but relevance is weak on typos and plurals.
>
> **What we did**
> - Loaded 2M rows, added a `tsvector` index, ran 20 representative queries.
>
> **Evidence**
> - p95 latency 140ms (well under target). Exact-term relevance good; typo/plural relevance poor. Index build 4 min. Concurrent load not tested (Unknown).
>
> **Recommendation:** Proceed with conditions — adopt Postgres FTS for v1, but plan a follow-up on typo tolerance (trigram index or a query-time fuzzy layer) before launch.
>
> **Still open**
> - Behaviour under concurrent production load, relevance quality past 2M rows, and typo handling.
>
> **Disposal:** Prototype thrown away. The 20-query test set is worth keeping as a relevance benchmark — needs a proper rebuild to reuse.

## Tuning Notes

- **Inconclusive is valid:** If the spike didn't settle the question, the honest answer is "inconclusive" plus the next smallest spike — don't let the model manufacture certainty.
- **Confidence from time:** If the spike was cut short, say so; the readout should temper its confidence accordingly.
- **Common pitfall:** Watch for a clean recommendation that hides the open risks. The "still open" section is the point — it stops a short experiment from being over-read.
- **Audience shift:** If this feeds a formal decision, follow it with an architecture-decision-record to capture the trade-offs.
