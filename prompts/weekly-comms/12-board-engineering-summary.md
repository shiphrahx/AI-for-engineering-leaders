# Board Engineering Summary

## Situation

The board meeting is coming up and you need to contribute the engineering section. Board members think in terms of revenue, risk, and competitive position — not sprints and deploys. Your job is to translate engineering progress into business language.

## The Prompt

```
You are a senior engineering leader preparing the engineering section of a board update. Board members are investors and experienced operators. They want to know: is engineering a strategic advantage or a liability? Are we shipping, are we reliable, and are we efficient?

Structure:
1. **Engineering headline** — one sentence framing engineering's contribution to the business this period
2. **Delivery highlights** — 3-4 items tied to business outcomes (revenue, retention, efficiency), not technical outputs
3. **Reliability & security** — uptime, incident trends, any security posture updates
4. **Team & talent** — headcount, attrition, key hires, hiring pipeline health
5. **Investment areas** — where engineering is spending time and why (product, platform, tech debt, reliability)
6. **Risks & mitigations** — 1-2 strategic risks the board should be aware of

Period: [TIME_PERIOD]
Company stage: [STARTUP / GROWTH / ENTERPRISE]
Key business metrics: [BUSINESS_METRICS]

Engineering data:
[PASTE_ENG_DATA]
```

## Example Input

```
Period: Q1 2025
Company stage: Growth (Series B, 180 employees, 45 engineers)
Key business metrics: ARR $18M, 1,200 customers, NRR 112%

Engineering data:
- Shipped: self-service onboarding (reduced time-to-value from 5 days to 2hrs), bulk import feature (unblocked 3 enterprise deals worth $400K combined ARR), SOC 2 Type II audit passed
- Reliability: 99.95% uptime (target 99.9%), 2 P1 incidents (down from 5 last quarter), MTTR improved from 45min to 22min
- Team: 45 engineers (started Q at 42, hired 5, lost 2). Attrition: 4.4% quarterly. Pipeline: 23 active candidates, 4 offers pending. Key hire: new Head of Infrastructure starts April 1.
- Time allocation: 55% product features, 20% platform/infra, 15% tech debt, 10% reliability
- Risks: main application is a monolith and we're starting to hit scaling bottlenecks at current customer growth rate. Migration to services will take 3-4 quarters and require 2-3 additional engineers.
```

## Example Output

> **Engineering — Q1 2025 Board Summary**
>
> **Headline:** Engineering accelerated customer time-to-value by 95%, directly supported $400K in new ARR, and achieved SOC 2 Type II — all while improving reliability and growing the team.
>
> **Delivery**
> - **Self-service onboarding** reduced customer time-to-value from 5 days to under 2 hours, removing the #1 friction point in our sales-to-activation funnel
> - **Bulk data import** unblocked 3 enterprise deals representing $400K in combined ARR — these were stalled on the inability to migrate data from competitors
> - **SOC 2 Type II certification achieved** — this was a gating requirement for 60% of our enterprise pipeline and is now a competitive advantage in procurement conversations
>
> **Reliability**
> - 99.95% uptime vs. 99.9% target
> - P1 incidents: 2 (down from 5 in Q4) — trend driven by investment in monitoring and on-call process improvements
> - Mean time to resolution improved from 45 minutes to 22 minutes
>
> **Team**
> - 45 engineers (net +3). Hired 5, lost 2 (one to FAANG, one relocation)
> - Quarterly attrition: 4.4% (industry benchmark: ~5-7%)
> - Head of Infrastructure joining April 1 — this hire fills a critical leadership gap as we scale our platform
> - Active pipeline healthy: 23 candidates, 4 offers pending
>
> **Engineering Investment Mix**
> - 55% product features (customer-facing value)
> - 20% platform and infrastructure (scaling and reliability)
> - 15% tech debt reduction (long-term velocity)
> - 10% reliability and incident prevention
>
> **Strategic Risk**
> Our core application architecture will become a scaling bottleneck within 2-3 quarters at current customer growth rates. We've begun planning a phased migration to a services architecture, estimated at 3-4 quarters of effort requiring 2-3 additional engineers. I'll present a detailed proposal and investment ask at the next board meeting.

## Tuning Notes

- **Early-stage (pre-Series A):** Focus on velocity and customer evidence. Boards want to see you shipping fast and responding to customer feedback. Drop the reliability section unless there was a notable incident.
- **Enterprise/public company:** Add compliance and security posture as a standalone section. Include engineering cost per customer or per revenue dollar if the board tracks efficiency metrics.
- **Fundraising context:** Emphasise technical moat, proprietary technology, and team quality. The board will use this in investor conversations.
- **Bad quarter:** Don't spin. State what happened, what you learned, and what you're doing differently. Boards respect honesty and a plan far more than spin.
