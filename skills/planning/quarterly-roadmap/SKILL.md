---
name: quarterly-roadmap
description: >
  Produces a defensible quarterly engineering roadmap balancing customer-facing features,
  platform investment, tech debt, and reliability — every item tied to a business outcome
  or risk it mitigates. Use when the user says "build a roadmap", "plan the quarter",
  "what should we commit to this quarter", or pastes business objectives, a backlog, and
  known tech debt. Use this for the whole-quarter plan across all work types — use
  okr-drafting for the measurable goals themselves, capacity-planning for the
  bandwidth math, and tech-debt-prioritisation for ranking debt items alone.
---

# Quarterly Roadmap

Turn vague business goals, a backlog, and lingering tech debt into a structured quarterly roadmap that balances feature, platform, debt, and reliability work — defensible to stakeholders.

## Inputs to gather

Gather these before drafting. If any are missing, ask for them in a single batched question — never invent objectives, dates, owners, or constraints. Mark anything genuinely unavailable as **Unknown** in the output.

- **Team** — name and number of engineers
- **Quarter** — which quarter/cycle this covers
- **Business objectives** — what the business needs this quarter
- **Backlog / requests** — the candidate work items
- **Known tech debt** — outstanding debt competing for capacity
- **Constraints** — leave, audits, freezes, dependencies, hiring/headcount changes

## Steps

1. Read the objectives, backlog, and tech debt fully. Every roadmap item must connect to a business outcome or a named risk it mitigates — flag anything that does not.
2. Write a one-sentence **quarter theme** framing what the quarter is about.
3. Define **3–5 measurable goals** tied to the business objectives.
4. Sort candidate work into **committed work** (high-confidence, with target dates, owners, and business impact) and **stretch goals** (tackled only if committed work finishes early).
5. Write **explicitly not doing**: things stakeholders asked for that are intentionally deferred, each with reasoning. This is the section that protects the team from scope creep — do not omit it.
6. State the **investment mix** as a percentage split across feature / platform / tech debt / reliability, grounded in the listed work.
7. List **key dependencies** (what's needed from other teams, by when) and **risks** (what could derail the plan, and the trigger).
8. Adapt to context: for a small/startup team, cap commitments at 2–3 and keep it to one page — "explicitly not doing" matters most. For a large org, add a RACI matrix for cross-team dependencies and a roadmap-review cadence. For an executive audience, lead with business outcomes and strip technical detail (e.g. version migrations). Under high uncertainty, replace dates with "early/mid/late quarter" and add confidence levels (high/medium/low) per committed item.
9. Assemble the output in the format below.
10. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Team] — [Quarter] Roadmap**

**Theme:** [One sentence framing the quarter]

**Goals**
1. [Measurable goal] — [business tie]

**Committed Work**
| Deliverable | Target | Owner | Business Impact |
|-------------|--------|-------|-----------------|
| [item] | [date or early/mid/late quarter] | [owner or Unknown] | [outcome/risk] |

**Stretch Goals**
- [Item tackled only if committed work finishes early]

**Explicitly Not Doing**
- **[Request]:** [Why it's being deferred and to when]

**Investment Mix:** [X]% features / [X]% platform / [X]% tech debt / [X]% reliability

**Dependencies**
- [Team/function]: [what's needed] (needed by [date])

**Risks**
- [What could derail the plan and its trigger]
```

## Boundaries

- Never invent business objectives, target dates, owners, or constraints — mark them **Unknown**.
- Never include a roadmap item that lacks a stated business outcome or risk it mitigates.
- Never drop the "explicitly not doing" section — deferred work with reasoning is what makes a roadmap a plan and not a wishlist.
- Never present aspirational percentages as the investment mix without grounding them in the listed work.
- Capacity estimates depend on real velocity; dependency commitments need confirmation from the other teams — flag both for the user to validate, do not assert them as certain.

## Chaining

- After this, offer **capacity-planning** to check the committed work fits the team's real bandwidth.
- Offer **okr-drafting** to turn the goals into measurable, verifiable Key Results.
- For ranking the tech debt that feeds the investment mix, offer **tech-debt-prioritisation**.
