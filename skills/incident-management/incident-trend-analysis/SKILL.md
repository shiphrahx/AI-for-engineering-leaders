---
name: incident-trend-analysis
description: >
  Produces a cross-incident trend analysis for a time period — period summary vs prior
  period, recurring root-cause patterns with evidence, a per-service fragility breakdown,
  a preventability percentage, action-item follow-through, the top 3 systemic reliability
  investments, and metrics to track next period. Use when the user says "analyze our
  incidents this quarter", "incident trends", "reliability review", or pastes a list of
  incidents with root causes. Use this for systemic patterns across many incidents, not
  for a single incident's postmortem (planning/incident-postmortem) or live response.
---

# Incident Trend Analysis

Find the patterns that individual postmortems miss — recurring root causes, fragile services, and whether reliability investments are working. Output actionable recommendations, not just charts. Frame as "here's how we get better," never as a punishment record.

## Inputs to gather

Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent incidents, root causes, durations, or completion rates. Mark unavailable fields as **Unknown**.

- **Time period** — the quarter/half/year under review
- **Incident list** — for each: date, severity, service, root cause, duration
- **Previous-period data** — counts and severity breakdown for comparison, if available
- **Action-item status** — completion state of prior postmortems' action items, if available

## Steps

1. If the incident count is small (< ~5), say so and recommend deep per-incident review instead of trend analysis — patterns aren't meaningful at that volume.
2. **Summary**: total incidents and severity breakdown, the trend vs the previous period (with the percentage change), and total customer-facing downtime. Note where counts move differently by severity (e.g. fewer total but unchanged P0s).
3. **Patterns**: group incidents by root-cause category (deploy safety, resource exhaustion, configuration drift, third-party, code defect, etc.). A category is a pattern at 3+ incidents. Weight P0/P1 patterns over P2. For each pattern, cite the specific incidents as evidence and name the prevention mechanism.
4. **Service Breakdown**: a table of service × incident count × severity mix × trend arrow (worsening/stable/improving/new). Services with repeated incidents are fragile systems needing investment.
5. **Prevention Analysis**: state how many of N incidents were preventable with mechanisms the org either lacks or isn't using consistently, broken down by mechanism. Preventable incidents where the fix was already known are process failures, not technical ones.
6. **Action Item Follow-Through**: completion rate of prior action items, and — critically — call out any incident this period that an already-known-but-unshipped action item would have prevented.
7. **Top 3 Recommendations**: the highest-leverage systemic investments, each tagged with how many incidents (and which severities) it would prevent. Lead with the one preventing the most/worst.
8. **Metrics to Track Next Period**: 3–5 measurable targets (e.g. % deploys using progressive rollout, MTTD, action-item completion rate, P0 count).
9. Adapt the framing to audience as a sub-step: for executives, lead with the preventability headline ("9 of 13 were preventable") to justify reliability investment; for the board, foreground business impact (downtime hours, customers, revenue); pair with SLO burn data if available (fewer incidents but more burn means the ones that happen are worse). Keep it non-punitive and celebrate improvement over prior periods.
10. Assemble the output in the format below.

## Output format

```
**Incident Trend Analysis — [Period]**

**Summary**
[Total + severity breakdown; trend vs previous period with %; total downtime]

**Pattern 1: [Category] ([N] incidents, [severity mix])**
- [Incident date — root cause → severity]
- Prevention: [mechanism]

**Pattern 2 / 3: ...**

**Service Breakdown**
| Service | Incidents | Severity | Trend |
|---------|-----------|----------|-------|
| [name] | [n] | [mix] | [⬆️/➡️/⬇️/new] |

**Prevention Analysis**
Of [N] incidents, [X] were preventable:
- [n] by [mechanism]
- [n] by [mechanism]

**Action Item Follow-Through**
[Completion rate]. [Which incidents a known-but-unshipped item would have prevented.]

**Top 3 Recommendations**
1. **[Investment]** (prevents [N] incidents incl. [severities]) — [why high-leverage]
2. ...
3. ...

**Metrics to Track Next [Period]**
- [Metric]: [target]
```

## Boundaries

- Never fabricate incidents, root causes, durations, downtime totals, or action-item completion figures — mark **Unknown** and analyze only what is provided.
- Never name individuals as causes or make the analysis punitive; root causes are systemic.
- Never assert a pattern from fewer than 3 incidents, or claim preventability without naming the specific mechanism that would have stopped it.
- Trusts the inputs as given — flag that severity calibration and root-cause accuracy are the user's responsibility (garbage in, garbage out).

## Chaining

- After this, offer **remediation-tracker** to drive the top recommendations and any open action items to completion.
- For a single incident rather than a trend, redirect to **planning/incident-postmortem**.
