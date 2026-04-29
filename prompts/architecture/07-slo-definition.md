# SLO Definition

## Situation

You need to define Service Level Objectives that give your team a clear reliability target and your stakeholders a shared language for "how reliable is reliable enough?" SLOs bridge the gap between engineering metrics and business expectations.

## The Prompt

```
You are a senior engineer defining SLOs for your services. Each SLO must be measurable, meaningful to the business, and actionable by the engineering team. Include the SLI (what you measure), the target, the error budget, and what happens when the budget is exhausted.

Structure:
1. **Service overview** — what the service does and who depends on it
2. **SLIs** — the specific metrics that indicate service health (what to measure)
3. **SLOs** — the target for each SLI over a rolling window
4. **Error budget** — how much failure is acceptable and how to calculate burn rate
5. **Error budget policy** — what happens when the budget is spent (slow down features? reliability sprint?)
6. **Measurement** — how each SLI is actually calculated (data source, query)
7. **Review cadence** — when to review and adjust SLOs

Service: [SERVICE_NAME]
Users/consumers: [WHO_USES_THIS]
Current reliability: [CURRENT_METRICS]
Business expectations: [WHAT_STAKEHOLDERS_EXPECT]
```

## Example Input

```
Service: Checkout API — handles the complete purchase flow from cart to payment confirmation
Users: Web and mobile clients, ~8K transactions/day
Current reliability: 99.7% success rate, p99 latency 1.2 seconds
Business expectations: "Checkout should just work. Every failed checkout is lost revenue."
```

## Example Output

> **SLO Definition: Checkout API**
>
> **Service:** Handles the complete purchase flow. Every failed request is a potentially lost sale. This is the most revenue-critical service in the platform.
>
> **SLIs and SLOs**
>
> | SLI | Definition | SLO Target | Window |
> |-----|-----------|------------|--------|
> | Availability | % of checkout requests returning non-5xx responses | 99.95% | 30-day rolling |
> | Latency | % of checkout requests completing in < 2 seconds | 99% | 30-day rolling |
> | Correctness | % of completed checkouts with accurate order and charge | 99.99% | 30-day rolling |
>
> **Error Budget**
>
> At 8K transactions/day over 30 days = 240K transactions per window.
> - Availability: 99.95% → 120 allowed failures per 30 days (4/day)
> - Latency: 99% → 2,400 slow requests allowed per 30 days (80/day)
> - Correctness: 99.99% → 24 incorrect transactions per 30 days (~1/day)
>
> **Error Budget Policy**
> - **Budget > 50% remaining:** Normal development. Ship features, take calculated risks.
> - **Budget 25-50% remaining:** Caution. No risky deploys without extra review. Team begins investigating the burn.
> - **Budget < 25% remaining:** Reliability mode. Feature work pauses. Team focuses exclusively on reliability improvements until budget recovers.
> - **Budget exhausted:** Incident review with leadership. Mandatory reliability sprint. No new features until budget is positive for 1 week.
>
> **Measurement**
> - Availability: Datadog synthetic monitor + real user success rate from API gateway logs. Exclude client errors (4xx) — only 5xx and timeouts count as failures.
> - Latency: p99 from API gateway request duration metric. Measured server-side (excludes network transit to client).
> - Correctness: Reconciliation job compares orders placed vs charges made vs inventory adjusted. Runs every 15 minutes.
>
> **Review Cadence:** Monthly SLO review in the reliability sync. Quarterly adjustment if targets are consistently too easy or too hard.

## Tuning Notes

- **First SLOs:** Start with availability only. Add latency and correctness SLOs once the team is comfortable with the concept.
- **Internal services:** SLOs still apply. The "customer" is the team that depends on your service. Agree on SLOs together.
- **Customer-facing SLAs:** SLOs should be stricter than SLAs. If you promise 99.9% uptime to customers, your internal SLO should be 99.95%+ to give yourself a buffer.
- **SLOs feel too abstract:** Make the error budget visible. A dashboard showing "42 failures remaining this month" is more visceral than "99.95% availability."
