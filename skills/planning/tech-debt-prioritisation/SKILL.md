---
name: tech-debt-prioritisation
description: >
  Produces a prioritised tech debt backlog with a business case for each item — cost of
  inaction, benefit of resolution, effort, and recommended priority — presentable to product
  and business stakeholders. Use when the user says "prioritise our tech debt", "make the
  case for paying down debt", or pastes a list of debt items with a velocity-impact note.
  Use this for ranking and justifying known debt — use quarterly-roadmap to fold the result
  into the quarter's plan, not for discovering debt or tracking paydown progress.
---

# Tech Debt Prioritisation

Turn a list of tech debt into a prioritised backlog that quantifies the cost of inaction and the benefit of resolution, prioritised by business impact rather than engineering frustration — so the user can negotiate for capacity.

## Inputs to gather

Gather these before ranking. If any are missing, ask for them in a single batched question — never invent metrics, effort estimates, or incident history. Mark anything genuinely unavailable as **Unknown**.

- **Team** — name and size
- **Velocity impact** — how debt currently affects the team (e.g. "~15% of each sprint working around debt")
- **Tech debt inventory** — the list of items (can be unstructured)
- **Upcoming work** the debt might block or enable, if known
- **Capacity** available for debt work, if known

## Steps

1. Read the inventory. For each item, assess: how it hurts (velocity, reliability, security, hiring), what happens if left unaddressed (incident likelihood, compounding cost), rough effort, and whether it blocks or enables other work.
2. Write a **summary** — total item count, estimated cost of carry (developer-hours or sprint-fraction wasted), and risk exposure (call out active security/compliance items).
3. Rank into a **prioritised backlog**. Prioritise by business impact: weigh pain frequency (daily > weekly > monthly > rare), blast radius (whole team > single team > individual), trend (getting worse > stable > improving), and effort (smaller wins rank higher). Override the score with judgment for security/compliance items — they rise regardless of frequency.
4. Assign each item a priority (P0–P3) with: description, risk if unaddressed, estimated effort, and a one-line business case stated in stakeholder terms (revenue, compliance, delivery speed) — not "the code is ugly".
5. Write a **recommended investment** — how much sprint capacity to allocate and how to sequence the work across sprints.
6. Identify **quick wins** — items resolvable in under a day with outsized impact.
7. Adapt to context: presenting to product/business — lead with the velocity-tax number and security risks, frame as "investing in delivery speed". For skeptical stakeholders, add a "cost of doing nothing" projection over 2–3 quarters. For a small team, pick only the top 3 — boiling the ocean is worse than nothing. After a debt-caused incident, lead with that incident as the leverage to get capacity approved.
8. Assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Team] — Tech Debt Assessment**

**Summary:** [N items. Estimated velocity tax: [figure]. [Security/risk callouts].]

**Prioritised Backlog**
| Priority | Item | Risk if Unaddressed | Effort | Business Case |
|----------|------|---------------------|--------|---------------|
| P0 | [item] | [cost of inaction] | [days or S/M/L] | [why now, in business terms] |
| P1 | [...] | [...] | [...] | [...] |
| P2 | [...] | [...] | [...] | [...] |
| P3 | [...] | [...] | [...] | [...] |

**Recommended Investment**
[X% of sprint capacity for N sprints. Sequencing: P0 in Sprint 1, ...]

**Quick Wins (< 1 day each)**
- [Item with outsized impact]
```

## Boundaries

- Never fabricate velocity-tax figures, incident history, effort estimates, or revenue numbers — mark them **Unknown** and use ranges where the user can refine.
- Never prioritise by engineering frustration over business impact — frustration is a signal, not the ranking.
- Never bury active security or compliance debt below cosmetic items because it's infrequent.
- Effort estimates and business-case quality depend on the user's data and team validation — say so rather than asserting precision.

## Chaining

- After this, offer **quarterly-roadmap** to fold the prioritised debt into the quarter's investment mix alongside feature and platform work.
