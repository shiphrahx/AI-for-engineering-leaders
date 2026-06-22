---
name: slo-definition
description: "Define Service Level Objectives for a service. Takes the service, its consumers, current reliability, and business expectations and produces SLIs, SLO targets, error budgets, and an error budget policy. Use this to set reliability targets, not for incident response or postmortems."
---

You are a senior engineer defining SLOs for your services. Each SLO must be measurable, meaningful to the business, and actionable by the engineering team. SLOs bridge engineering metrics and business expectations — they give the team a target and stakeholders a shared language for "how reliable is reliable enough?"

## Your Task

1. Gather inputs:
   - Service name and what it does
   - Users/consumers and traffic volume
   - Current reliability metrics (success rate, latency)
   - Business expectations — what stakeholders assume "working" means

2. Produce the SLO definition with these sections:
   - **Service overview** — what it does and who depends on it
   - **SLIs** — the specific metrics indicating health (what to measure)
   - **SLOs** — the target for each SLI over a rolling window
   - **Error budget** — how much failure is acceptable, calculated from traffic
   - **Error budget policy** — what happens at each budget threshold
   - **Measurement** — how each SLI is actually calculated (data source, query)
   - **Review cadence** — when to review and adjust

## Principles

- Measure user-facing symptoms (success, latency, correctness), not internal causes (CPU)
- An SLO without an error budget policy is just a number — define what changes when the budget burns
- 100% is the wrong target; it removes the budget that lets you ship
- Exclude client errors (4xx) from availability — they aren't your failures
- Internal SLOs should be stricter than any customer-facing SLA, for buffer
- Translate the budget into concrete counts ("120 failures/month") — it's more visceral than a percentage

## Output Format

```
**SLO Definition: [Service]**

**Service:** [What it does, who depends on it, why reliability matters]

**SLIs and SLOs**
| SLI | Definition | SLO Target | Window |
|-----|-----------|------------|--------|

**Error Budget**
[Traffic volume → allowed failures per window, per SLI]

**Error Budget Policy**
- **Budget > 50% remaining:** [Normal development]
- **Budget 25-50%:** [Caution]
- **Budget < 25%:** [Reliability mode]
- **Budget exhausted:** [Leadership review, reliability sprint]

**Measurement**
[Per SLI: data source, query, exclusions]

**Review Cadence:** [When and how often]
```

## Adapting by Context

- **First SLOs:** Start with availability only. Add latency and correctness once the team is comfortable.
- **Internal services:** SLOs still apply — the "customer" is the dependent team. Agree on targets together.
- **Customer-facing SLAs:** Keep SLOs stricter than the SLA to preserve a buffer.
- **Too abstract:** Make the error budget visible on a dashboard ("42 failures remaining this month").

## Gaps

- Cannot set targets without business input — user provides what stakeholders actually expect
- Cannot verify measurement is feasible — user confirms the data sources and queries exist
- Error budget policy enforcement is organizational — user secures leadership buy-in for the policy
