# Engineering Strategy One-Pager

## Situation

You need to communicate your engineering strategy to a mixed audience — senior engineers, product partners, or new hires — in a single page. Not a vision deck, not a detailed roadmap: a crisp document that explains what you're optimising for, what you're not doing, and why.

## The Prompt

```
You are an engineering leader writing a one-page strategy document for your organisation.

Draft a strategy one-pager with these sections:

1. **Context** (2-3 sentences: where the business is, what engineering's role is right now)
2. **What we're optimising for** (3 priorities, each with a one-sentence rationale — not a list of goals, but the tradeoffs you're consciously making)
3. **What we're explicitly not doing** (2-3 things you're deprioritising and why — this is what makes a strategy a strategy)
4. **How we'll know it's working** (3-4 leading or lagging indicators, not vanity metrics)
5. **Implications for teams** (2-3 sentences on how this should change day-to-day decisions)

Keep it to one page. No bullet soup. Every sentence should carry weight.

Context:
- Org: [ORG_NAME], [HEADCOUNT] engineers
- Business stage: [e.g. scaling post-product-market fit, pre-IPO, post-acquisition, cost-reduction mode]
- Biggest engineering challenge right now: [CHALLENGE]
- Time horizon: [e.g. next 6 months, next year]
- Who will read this: [AUDIENCE]
```

## Example Input

```
- Org: Core Platform, 30 engineers
- Business stage: Scaling rapidly — revenue growing 3x YoY, headcount doubling
- Biggest challenge: System reliability degrading as load increases; new engineers struggle to contribute safely
- Time horizon: Next 12 months
- Audience: Staff engineers, team leads, product partners
```

## Example Output

> **Core Platform Engineering Strategy — 2025**
>
> **Context**
> We are in a growth phase where the volume of customers and transactions is outpacing the systems we built to serve them. Engineering's primary job this year is to make sure our infrastructure scales with the business without becoming a constraint on it.
>
> **What we're optimising for**
>
> *Reliability over feature velocity.* We will slow down in the short term to avoid the kind of outages that erode customer trust and consume engineering time in fire-fighting. Every significant new capability goes through an architecture review.
>
> *Developer leverage over headcount.* As we double the team, we're investing in the foundations that let new engineers contribute safely and quickly — internal tooling, documentation, and automated guardrails. One senior engineer improving the platform is worth more than two mid-level engineers navigating a confusing system.
>
> *Depth over breadth.* We will say no to new workstreams until our core systems are stable and well-understood. Spreading ownership too thin is how we got here.
>
> **What we're explicitly not doing**
> - Building net-new product features in Platform — that belongs in product teams. We are infrastructure.
> - Rewriting anything that isn't actively causing incidents. Greenfield rewrites have a poor track record; we'll refactor incrementally.
> - Taking on cross-team projects that don't directly serve reliability or developer experience.
>
> **How we'll know it's working**
> - P1/P2 incident rate trending down quarter-over-quarter
> - Mean time to productivity for new engineers (first meaningful PR) under 2 weeks
> - On-call load per engineer below 2 hours/week (from 6+ today)
> - Engineering satisfaction score on "I can ship with confidence" above 4.0/5.0
>
> **Implications for teams**
> When you're deciding whether to take on a piece of work, ask: does this make our systems more reliable, or does it make engineers more effective? If neither, it probably belongs somewhere else. Bring tradeoff decisions up rather than defaulting to yes — it's faster to align early than to undo later.

## Tuning Notes

- **For a new leader:** Add a "What I've heard from the team" section before the priorities — signals that the strategy is grounded in listening, not handed down.
- **For board or exec audience:** Cut implications, add a risk section (what could prevent this from working).
- **Annual planning context:** Pair with the quarterly roadmap prompt to translate strategy into concrete execution.
