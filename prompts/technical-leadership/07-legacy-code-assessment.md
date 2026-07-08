# Legacy Code Assessment

## Situation

You've inherited an aging or unloved piece of code and must decide how to treat it: invest (improve in place), rewrite (replace it), or leave (don't touch it yet). You want the call made on evidence — cost of ownership, blast radius, changeability — not on how unpleasant the code is to read.

## The Prompt

```
You are helping an engineering leader decide what to do with a piece of legacy code: invest, rewrite, or leave. Decide on evidence, not aesthetics. Ugly code that works and rarely changes is often best left alone.

Produce:
1. Cost of ownership now — real pain: change frequency × difficulty, incidents, time lost. Separate "offends me" from "costs us".
2. Business role & blast radius — criticality, dependents, cost of a mistake.
3. Changeability — tests, coupling, whether the team understands it.
4. The three paths — cost and risk of Invest, Rewrite, and Leave (rewrite cost MUST include migration + parallel-run).
5. Verdict — Invest / Rewrite / Leave, leading with the strongest reason.
6. Trigger to reassess — what would change this call.

System: [WHAT_IT_IS]
Business role: [CRITICALITY_AND_DEPENDENTS]
Change pressure: [HOW_OFTEN_IT_CHANGES_AND_UPCOMING_WORK]
Pain evidence: [BUGS_INCIDENTS_TIME_LOST_COVERAGE]
Constraints: [TEAM_CAPACITY_DEADLINES]
```

## Example Input

```
System: The CSV import pipeline for bulk customer uploads.
Business role: Used by ~15 enterprise customers weekly; a bad import corrupts their data.
Change pressure: Touched roughly monthly; sales keeps requesting new column formats.
Pain evidence: 4 incidents in 6 months, all data-mapping bugs. No tests. One engineer understands it.
Constraints: Team of 5, mid-roadmap.
```

## Example Output

> **Legacy Assessment: CSV import pipeline** — Verdict: Invest
>
> _It's business-critical, changes monthly, and causes real incidents — but it's too load-bearing to risk a rewrite mid-roadmap._
>
> **Cost of ownership now**
> - Change frequency / difficulty: ~monthly, awkward each time due to no tests.
> - Incidents / time lost: 4 in 6 months, all data-mapping — high, and customer-facing.
>
> **Business role & blast radius:** 15 enterprise customers; a bad import corrupts their data. High criticality.
>
> **Changeability:** No tests, single-owner knowledge — any change is currently risky.
>
> **The three paths**
> | Path | Cost | Risk | Notes |
> |------|------|------|-------|
> | Invest | ~2-3 wks: tests + refactor mapping layer | Low-medium | Compounds — cuts the incident rate |
> | Rewrite | ~8 wks + migration + parallel-run | High | Risks the same customer data mid-flight |
> | Leave | 0 | Unacceptable | Incidents are customer-facing and recurring |
>
> **Verdict:** Invest — add tests around the mapping layer first (stops the bleeding), then refactor. Don't rewrite mid-roadmap on critical customer data.
> **Trigger to reassess:** If format requests keep growing and the mapping layer stays fragile after investment, reassess for a rewrite next planning cycle.

## Tuning Notes

- **Resist the rewrite reflex:** The model (and you) will be tempted to rewrite ugly code. Require evidence of real cost of ownership before a rewrite verdict.
- **Scale shift:** At a startup, bias toward Leave or targeted Invest — rewrites are expensive bets. At enterprise, consider a strangler-fig incremental replacement as a middle path.
- **Common pitfall:** Watch for a rewrite estimate that omits migration and parallel-run — that's where rewrites overrun.
- **Leave is a real answer:** For stable, rarely-touched code, "leave it" is the disciplined call, not a cop-out. But always attach a reassess trigger.
