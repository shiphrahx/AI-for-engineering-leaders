---
name: build-vs-buy-analysis
description: >
  Produces a balanced build-vs-buy analysis over a 2-year total cost of ownership — build
  option, vendor option(s), a comparison matrix, hidden costs, and a stated recommendation
  with conditions that would reverse it. Use when the user says "should we build or buy X",
  "evaluate these vendors", or pastes a capability need, vendor list, and team context. Use
  this for the make-or-buy decision itself — once decided, use architecture-decision-record
  to capture the choice durably; not for contract negotiation or post-purchase vendor management.
---

# Build vs Buy Analysis

Weigh building a capability in-house against buying or adopting a vendor solution, on total cost of ownership, engineering opportunity cost, operational burden, and strategic fit — laid out honestly, without bias toward either side.

## Inputs to gather

Gather these before analysing. If any are missing, ask for them in a single batched question — never invent vendor pricing, effort estimates, or team capacity. Mark anything genuinely unavailable as **Unknown**.

- **Capability needed** — the problem being solved, with must-haves vs nice-to-haves
- **Business context** — why now (the triggering pain or opportunity)
- **Vendors evaluated** — the candidate solutions, if any are named
- **Team context** — skills, capacity, and whether they could realistically build it
- **Constraints** — timeline, budget, compliance, data residency

## Steps

1. State the **decision summary** upfront: what capability, why now, and your recommendation — do not bury the lede.
2. Lay out the **build option**: estimated effort (MVP and full), ongoing maintenance burden, team expertise required, advantages, and the opportunity cost of what the team would not do instead.
3. Lay out the **buy option(s)**: each vendor with pricing, integration effort, limitations, and advantages.
4. Build a **comparison matrix** scoring options side-by-side on time to value, 2-year total cost, maintenance burden, customisation, vendor risk, and opportunity cost. Include the open-source/self-hosted option's ops overhead in its cost, not just its license.
5. Surface **hidden costs** both options underestimate — build: edge cases and the management UI usually skimped on; buy: per-seat pricing scaling with headcount and SDK/vendor lock-in migration cost.
6. State the **recommendation** with reasoning, and name the explicit conditions that would reverse it (e.g. "revisit if seat cost exceeds $X/yr or we need custom logic the vendor can't support").
7. Adapt to context: cost-sensitive startup — weight toward cash cost and surface the open-source option prominently. Enterprise/regulated — add a Compliance & Security row (data residency, SOC 2, audit); these often eliminate options fast. Strong internal platform team with capacity and charter fit — build becomes more attractive; factor team morale. Non-technical audience — drop SDK/implementation detail, lead with cost, time-to-value, and risk.
8. Assemble the output in the format below.

## Output format

```
**[Capability]: Build vs Buy Analysis**

**Recommendation:** [Build / Buy (vendor) / Hybrid] — [1–2 sentence why, stated upfront]

**Build Option**
- *Effort:* [MVP and full estimate]
- *Ongoing maintenance:* [burden]
- *Advantages:* [...]
- *Risks / opportunity cost:* [what the team won't do instead]

**Buy Options**
| | [Vendor A] | [Vendor B] | [Vendor C] |
|---|---|---|---|
| Cost (annual) | [...] | [...] | [...] |
| Integration effort | [...] | [...] | [...] |
| [key capability] | [...] | [...] | [...] |

**Comparison Matrix**
| Dimension | Build | [Vendor A] | [Vendor B] |
|-----------|-------|-----------|-----------|
| Time to first value | [...] | [...] | [...] |
| 2-year total cost | [...] | [...] | [...] |
| Maintenance burden | [...] | [...] | [...] |
| Customisation | [...] | [...] | [...] |
| Vendor risk | [...] | [...] | [...] |
| Opportunity cost | [...] | [...] | [...] |

**Hidden Costs**
- *Build:* [underestimated complexity]
- *Buy:* [scaling cost, lock-in]

**Recommendation: [Choice]**
[Reasoning. Revisit if: (a) [condition], (b) [condition].]
```

## Boundaries

- Never invent vendor pricing, build effort, or reliability claims — mark them **Unknown**; vendor quotes and reference checks are the user's to obtain.
- Never write a one-sided analysis — be genuinely generous to the option you don't recommend, especially for a controversial or contested decision.
- Never present opportunity-cost or TCO figures as precise — use ranges and state the assumptions.
- Never reduce TCO to sticker price — include maintenance, integration, ops overhead, and opportunity cost.

## Chaining

- After the decision is made, offer **architecture-decision-record** to capture the choice, alternatives, and reversal conditions durably for future engineers.
