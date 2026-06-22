---
name: technical-vision-document
description: >
  Produces an opinionated 12-24 month technical vision for a domain — honest current state, business
  context, a concrete vision, 3-5 architectural principles, 4-6 key initiatives, what to stop doing,
  success metrics, and risks. Use when the user says "write a technical vision/strategy", "where
  should our architecture go", "north star for [domain]", or asks for multi-year engineering
  direction. Use this for the multi-year direction across systems; use system-design-document for one
  system's blueprint, technology-radar for the adopt/hold tooling calls, and a roadmap for quarterly
  execution rather than direction.
---

# Technical Vision Document

Write an opinionated 12-24 month vision for where the architecture should head and why — bold calls backed by evidence, guiding decisions and aligning teams. This is direction, not a roadmap.

## Inputs to gather

Gather these before writing. If any are missing, ask in a single batched question — never invent the current architecture, business direction, or team facts. Mark anything genuinely unavailable as **Unknown** in the output.

- **Domain** — the area this vision covers
- **Current architecture** — honest current state
- **Business direction** — where the business is heading in 1-2 years
- **Team** — size and skills
- **Time horizon** — months

## Steps

1. Confirm inputs. If the business direction or current state isn't given, ask — a vision unanchored to business need is a wishlist. Mark gaps **Unknown**.
2. Write the **Current state** honestly — strengths and weaknesses both; name what's working and what's constraining.
3. Write the **Business context** — the forces (market expansion, new product surface, growth target) that shape the technical direction.
4. Write the **Vision** — where the architecture should be in 18-24 months, described concretely (region count, service count, deploy time, capabilities), not in slogans. Be opinionated; take a position.
5. State 3-5 **Principles** — durable architectural rules that guide decisions toward the vision (e.g. "extract at the boundary, not in the core", "boring technology by default", "multi-region is not optional").
6. Name the **Key initiatives** — the 4-6 major efforts that get from here to there, each scoped to a rough time window and tied to a business force.
7. State **What we stop doing** — patterns, technologies, or approaches to phase out. A vision that only adds is incomplete.
8. Define **Success metrics** — concrete, measurable signals that the vision is being realised (deploy time, region live, incidents from deploys, independently deployable services).
9. Name the **Risks** — what could prevent getting there (team capacity, unfamiliar complexity, deceptive coupling).
10. Adapt to context: for a board audience, extract a one-page executive summary (current pain, vision in one sentence, 3 key investments, the business outcome each enables). To get buy-in, circulate as a draft RFC for staff engineers and EMs to co-create. Recommend a 6-month review cadence. For a small team (< 10 engineers), cap at 2-3 initiatives — eight initiatives is a wishlist, not a strategy.
11. Assemble the output in the format below.

## Output format

```
**[Domain] Technical Vision — [Time Range]**

**Current State**
[Honest strengths and weaknesses]

**Business Context**
[The forces shaping direction]

**Vision: [N] Months From Now**
[Concrete description of the target architecture]

**Principles**
1. **[Principle].** [What it means in practice.]

**Key Initiatives**
1. **[Initiative]** ([time window]): [What and why]

**What We Stop Doing**
- [Pattern/technology to phase out]

**Success Metrics ([horizon])**
- [Measurable signal, from → to]

**Risks**
- [Risk and why it matters]
```

## Boundaries

- Never fabricate the current architecture, business direction, or team capacity — mark them **Unknown**; the vision is only credible if anchored to real facts.
- Never list more initiatives than the team can sequence — an over-long list is a wishlist, not a strategy; cap it to the team's capacity.
- Never write a vision that only adds — "what we stop doing" is mandatory.
- This is direction, not a roadmap — do not produce quarterly task breakdowns or ticket-level plans here.

## Chaining

- After this, offer **technology-radar** to turn the "boring technology" principle and "what we stop doing" into concrete adopt/trial/assess/hold calls.
- Initiatives that are full systems feed into **system-design-document**.
