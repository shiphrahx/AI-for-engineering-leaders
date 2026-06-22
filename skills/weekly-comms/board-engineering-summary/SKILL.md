---
name: board-engineering-summary
description: >
  Produces the engineering section of a board update — a business-language summary translating
  delivery, reliability, team/talent, investment mix, and strategic risk into the terms
  investors and operators care about (revenue, retention, efficiency, risk). Use when the user
  says "board engineering summary", "engineering section for the board deck", "quarterly board
  prep", or pastes delivery highlights, uptime/incident data, headcount and business metrics.
  Use this for investor-level board reporting — use exec-status-update for weekly leadership-up
  updates, not detailed technical reports.
---

# Board Engineering Summary

Translate a quarter of engineering progress into board language that answers the only question a board has: is engineering a strategic advantage or a liability — are we shipping, reliable, and efficient?

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent a metric, headcount, attrition figure, or business outcome. Mark anything genuinely unavailable as **Unknown** in the output.

- **Period** — the reporting period (e.g. Q1 2025)
- **Company stage** — startup / growth / enterprise (and funding stage if relevant)
- **Key business metrics** — ARR, customer count, NRR, growth rate
- **Delivery highlights** — what shipped, ideally with the business outcome it enabled
- **Reliability data** — uptime vs. target, incident counts/trend, MTTR, security posture
- **Team data** — headcount and net change, attrition, key hires, pipeline health
- **Investment allocation** — where engineering time went (product / platform / tech debt / reliability)
- **Strategic risks** — known risks with intended mitigation or investment ask

## Steps

1. Read all engineering data before writing. Identify the one strategic story of the period — that becomes the headline.
2. Write the **engineering headline** — a single sentence framing engineering's contribution to the business this period.
3. List **delivery highlights** (3-4), each tied to a business outcome (revenue, retention, efficiency), never a technical output: "Shipped X, which [unblocked $400K ARR / cut time-to-value 95%]". Translate every feature into what it enabled.
4. Summarize **reliability & security**: uptime vs. target (frame as customer trust), incident count and trend, MTTR, and any security/compliance posture change.
5. Present **team & talent** as organizational health: headcount and net change, attrition with a benchmark comparison, key hires and why they matter, pipeline health.
6. Show the **investment mix** as percentages across product / platform / tech debt / reliability, with a one-line "why" if it tells a story.
7. State **1-2 strategic risks** with mitigation and, if applicable, a timeline or investment ask — never a problem without a plan.
8. Adapt to context: **early-stage (pre-Series A)** — focus on velocity and customer evidence; drop reliability unless there was a notable incident. **Enterprise/public** — add compliance and security as a standalone section and include cost-per-customer or cost-per-revenue-dollar if the board tracks efficiency. **Fundraising context** — emphasize technical moat, proprietary tech, and team quality. **Bad quarter** — do not spin; state what happened, what you learned, and what you're doing differently.
9. Assemble the output in the format below.

## Output format

```
**Engineering — [Period] Board Summary**

**Headline:** [One sentence on engineering's strategic contribution this period]

**Delivery**
- **[Feature/Initiative]** — [Business outcome it enabled, quantified]

**Reliability**
- Uptime: [%] vs. [target]
- Incidents: [P0/P1 count] ([trend vs. previous period])
- MTTR: [time] ([trend])
- Security: [Notable update or "No material changes"]

**Team**
- Headcount: [N] ([net change]) — hired [N], lost [N]
- Attrition: [%] ([benchmark comparison])
- Key hire: [Role] — [why this matters]
- Pipeline: [health assessment]

**Engineering Investment Mix**
- [X]% product features
- [X]% platform/infrastructure
- [X]% tech debt
- [X]% reliability

**Strategic Risk**
[Risk description] — *Mitigation:* [what you're doing]. [Timeline or investment ask if applicable.]
```

## Boundaries

- Never fabricate metrics, headcount, attrition, business outcomes, or hire details — mark anything unavailable as **Unknown**.
- Never present a technical metric without its business meaning (e.g. translate uptime into customer downtime minutes).
- Never spin a bad quarter — boards respect honesty and a plan over polish.
- Never claim a business impact that requires PM/finance attribution the user hasn't provided — attribute or mark **Unknown**.
- Never state a strategic risk without a mitigation or plan.

## Chaining

- No natural successor — this is usually a terminal artifact. It is typically assembled from a period's **exec-status-update**.
