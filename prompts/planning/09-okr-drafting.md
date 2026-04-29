# OKR Drafting

## Situation

Your VP just shared the company or department goals for the quarter and you need to translate these into team-level OKRs. The goals are vague ("improve platform reliability"), and you need to make them specific, measurable, and achievable within the quarter.

## The Prompt

```
You are an engineering leader drafting OKRs (Objectives and Key Results) for your team. Objectives should be ambitious and qualitative. Key Results should be specific, measurable, and verifiable — someone should be able to look at each KR at the end of the quarter and say definitively whether it was achieved or not. Avoid vanity metrics and output-based KRs (features shipped); focus on outcomes.

Structure:
- 2-3 Objectives per team, each with 2-4 Key Results
- For each KR: the metric, baseline, target, and how you'll measure it
- Flag any KRs that depend on other teams

Team: [TEAM_NAME]
Quarter: [QUARTER]
Company/department goals: [COMPANY_GOALS]
Current baselines: [CURRENT_METRICS]
Team context: [RELEVANT_CONTEXT]
```

## Example Input

```
Team: Reliability Engineering, 6 engineers
Quarter: Q4 2025
Company goals: "Improve platform reliability to enterprise grade" and "Reduce customer churn from technical issues"
Current baselines: 99.8% uptime (target should be higher), MTTR 38 minutes, 12 P1 incidents last quarter, 3 customers churned citing reliability as primary reason, no SLAs published to customers
Team context: We just finished instrumenting all core services with structured logging and distributed tracing. We have good observability now but haven't operationalised it yet.
```

## Example Output

> **Reliability Engineering — Q4 2025 OKRs**
>
> **Objective 1: Make our platform reliability a competitive advantage, not a churn driver**
>
> | Key Result | Baseline | Target | Measurement |
> |-----------|----------|--------|-------------|
> | Achieve 99.95% uptime across all customer-facing services | 99.8% (Q3) | 99.95% | Datadog synthetic monitoring, measured monthly |
> | Reduce P1 incidents from 12 to ≤4 per quarter | 12 (Q3) | ≤4 | Incident tracker, counted at quarter end |
> | Zero customers cite reliability as primary churn reason | 3 (Q3) | 0 | CS exit survey data, reviewed monthly |
>
> **Objective 2: Detect and resolve incidents before customers notice**
>
> | Key Result | Baseline | Target | Measurement |
> |-----------|----------|--------|-------------|
> | Reduce MTTR from 38 minutes to under 15 minutes | 38 min (Q3 avg) | <15 min | Incident tracker, median MTTR |
> | 80% of P1 incidents detected by monitoring before customer report | ~30% estimated | 80% | Tag each incident as "monitoring-detected" vs "customer-reported" |
> | Every core service has a runbook that's been tested via game day | 0 of 8 services | 8 of 8 | Runbook repo + game day log |
>
> **Objective 3: Establish SLAs that build enterprise customer confidence**
>
> | Key Result | Baseline | Target | Measurement |
> |-----------|----------|--------|-------------|
> | Publish external SLAs for the top 5 customer-facing services | No SLAs published | 5 SLAs live on status page | Status page audit |
> | Internal SLO dashboards live for all 8 core services | 0 | 8 dashboards | Dashboard inventory |
> | SLA breach rate <1% across all published SLAs | N/A (new) | <1% | Automated SLA tracking |
>
> *Dependency note: Objective 3 KR1 (publishing SLAs) requires legal review and sign-off. Coordinate with Legal by week 3.*

## Tuning Notes

- **Output vs. outcome trap:** "Ship feature X" is an output, not a key result. Reframe as the outcome: "Reduce support tickets related to X by 40%." If you can't articulate the outcome, question whether the feature is the right work.
- **Stretch targets:** OKRs are meant to be ambitious. Achieving 70% of your KRs is healthy. If you hit 100%, your targets were too easy.
- **Inherited OKRs (mandated from above):** If your boss hands you a KR, push back on the "how" even if you can't change the "what." Your team should own the approach.
- **First time writing OKRs:** Start with 2 objectives and 2 KRs each. Fewer, clearer OKRs are always better than a long list that no one tracks.
