---
name: engineering-strategy-one-pager
description: >
  Produces a one-page engineering strategy: context, what you're optimising for (the
  tradeoffs being consciously made), what you're explicitly not doing, leading/lagging
  indicators of success, and implications for teams. Use when the user says "write our
  engineering strategy", "strategy one-pager", or wants to communicate direction and tradeoffs
  to a mixed audience on a single page. Use this for the why-and-tradeoffs direction layer —
  use quarterly-roadmap for the concrete work and okr-drafting for measurable goals.
---

# Engineering Strategy One-Pager

Communicate engineering strategy to a mixed audience — senior engineers, product partners, new hires — on a single page: what you're optimising for, what you're not doing, and why. Not a vision deck, not a roadmap. Every sentence carries weight; no bullet soup.

## Inputs to gather

Gather these before drafting. If any are missing, ask for them in a single batched question — never invent the business stage, the core challenge, or the audience. Mark anything genuinely unavailable as **Unknown**.

- **Org** — name and headcount
- **Business stage** — e.g. scaling post-PMF, pre-IPO, post-acquisition, cost-reduction
- **Biggest engineering challenge** right now
- **Time horizon** — e.g. next 6 months, next year
- **Audience** — who will read this

## Steps

1. Write **context** — 2–3 sentences: where the business is and what engineering's role is right now.
2. Write **what we're optimising for** — exactly 3 priorities, each with a one-sentence rationale. Frame each as a conscious tradeoff (X over Y), not a goal — "reliability over feature velocity", not "improve reliability".
3. Write **what we're explicitly not doing** — 2–3 things being deprioritised, with why. This is the section that makes a strategy a strategy; do not soften or omit it.
4. Write **how we'll know it's working** — 3–4 leading or lagging indicators, not vanity metrics (e.g. on-call load per engineer, time-to-first-meaningful-PR for new hires — not lines of code or features shipped).
5. Write **implications for teams** — 2–3 sentences on how this should change day-to-day decisions (e.g. the question to ask before taking on work).
6. Keep it to one page. Cut any sentence that doesn't carry weight.
7. Adapt to context: for a new leader, add a "What I've heard from the team" section before the priorities, to signal the strategy is grounded in listening. For a board/exec audience, cut implications and add a risk section (what could prevent this from working). When this pairs with annual planning, note that the quarterly roadmap will translate it into execution.
8. Assemble the output in the format below.

## Output format

```
**[Org] Engineering Strategy — [Horizon]**

**Context**
[2–3 sentences: business position and engineering's role now]

**What we're optimising for**

*[Priority A] over [tradeoff].* [One-sentence rationale.]

*[Priority B] over [tradeoff].* [One-sentence rationale.]

*[Priority C] over [tradeoff].* [One-sentence rationale.]

**What we're explicitly not doing**
- [Deprioritised thing — and why]

**How we'll know it's working**
- [Leading or lagging indicator — not a vanity metric]

**Implications for teams**
[2–3 sentences: how this changes day-to-day decisions]
```

## Boundaries

- Never invent the business stage, headcount, core challenge, or audience — mark them **Unknown**.
- Never drop or soften the "explicitly not doing" section — without conscious tradeoffs it's a vision statement, not a strategy.
- Never use vanity metrics as success indicators — choose measures of leverage and reliability, not activity.
- Never let it sprawl past one page or dissolve into bullet soup — every sentence must earn its place.

## Chaining

- After this, offer **quarterly-roadmap** to translate the strategy's priorities into concrete, dated execution for the next cycle.
