# Prototype Spike Plan

## Situation

You're about to spike a throwaway prototype to answer a technical question — feasibility, performance, integration — and want it framed so it ends in a decision instead of quietly becoming production code.

## The Prompt

```
You are planning a throwaway prototype (a spike) for an engineering team. A spike answers one question and then dies — it is not a stealth start on the real system. Keep it small and time-boxed.

Produce:
1. Question — the single thing this spike answers, in one sentence (yes/no or a number).
2. Build (smallest thing) — the minimum to produce that evidence; list what to skip/fake (auth, persistence, UI, error handling).
3. Timebox — hours or a few days, and what happens when it's hit (decide with what you have, don't extend).
4. Success / kill criteria — what result means proceed, what means stop, what means inconclusive (and the next smallest spike).
5. Disposal — the code is thrown away; name any part that might survive and flag it needs a proper rebuild.
6. Will NOT tell us — the risks the spike leaves open.

Question / uncertainty: [WHAT_YOURE_UNSURE_ABOUT]
Decision it feeds: [WHAT_CALL_THIS_UNBLOCKS_BY_WHEN]
Time available: [HOURS_OR_DAYS]
Constraints: [STACK / DATA_ACCESS / WHO_DOES_IT]
```

## Example Input

```
Question / uncertainty: Can we do full-text search on our existing Postgres, or do we need a separate search engine?
Decision it feeds: Search architecture for the Q3 catalogue revamp — decide in two weeks.
Time available: 2 days.
Constraints: Must use our current Postgres; one engineer.
```

## Example Output

> **Spike: Postgres full-text search** — Timebox: 2 days
>
> **Question:** Can Postgres full-text search return relevant catalogue results under 200ms at our data size (2M rows)?
>
> **Build (smallest thing)**
> - Load a copy of the 2M-row catalogue, add a `tsvector` index, run 20 representative queries, measure latency and eyeball relevance.
> - Skip / fake: the UI, ranking tuning, typo tolerance, any API layer.
>
> **Timebox:** 2 days. At the limit, decide on the evidence gathered — do not roll into building search.
>
> **Success / kill criteria**
> - ✅ Proceed if: p95 < 200ms and relevance is "good enough" on the 20 queries.
> - ❌ Stop (need a search engine) if: latency blows past 200ms or relevance is poor.
> - 🤔 Inconclusive → next spike: test with typo tolerance only.
>
> **Disposal:** Thrown away. The query set is worth keeping as a reference — needs a proper rebuild if reused.
>
> **Will NOT tell us:** Behaviour as the catalogue grows past 2M, ranking quality at scale, or operational cost.

## Tuning Notes

- **Scale shift:** At a startup, keep it to Question, Build, and a tight timebox — but still write the kill criterion. At a large org, add who signs off on the decision the spike feeds.
- **One-way-door:** If the decision is hard to reverse (a platform bet), spend the spike budget on the riskiest assumption, not the easiest to build.
- **Common pitfall:** The model may plan a spike that answers several questions. Force it to one primary question and list the rest as out of scope.
- **Disposal pressure:** If there's real pressure to keep the code, say so — the plan should then explicitly name what must be rebuilt before it ships.
