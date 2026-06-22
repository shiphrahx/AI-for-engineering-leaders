---
name: hiring-plan
description: >
  Produces a structured engineering hiring plan that justifies headcount against business
  need, defines and prioritizes roles, and sets a realistic timeline, sourcing strategy,
  budget, and 6-month success criteria. Use when the user says "build a hiring plan",
  "plan headcount", "what roles should I hire", "justify these hires", or pastes a current
  team makeup plus business goals and budget. Use this for deciding WHICH roles to open and
  in what order — not for briefing a recruiter on a single already-decided role
  (recruiter-kickoff-brief), nor for diagnosing an existing funnel (pipeline-analytics-review).
---

# Hiring Plan

Turn business goals, a current team, and a budget into a defensible hiring plan — every role justified by what it unlocks, prioritized by impact, not by wish list.

## Inputs to gather

Gather these before planning. If any are missing, ask for them in a single batched question — never invent a team makeup, a budget, or a comp range. Mark anything genuinely unavailable as **Unknown** in the output.

- **Current team** — size, seniority distribution, skills present, and gaps
- **Business goals** — what the business needs to achieve this period
- **Gaps / risks** — what is missing or at risk without new hires
- **Budget** — approved headcount or hiring budget, and comp bands if known

## Steps

1. Read team, goals, and gaps together before planning. Map each gap to a business goal it blocks; flag any gap with no clear business driver.
2. Write the **current state**: team size, seniority skew, and what is at risk without new hires. Be concrete about the risk (e.g. "P0 incidents handled ad hoc").
3. Define **roles to fill**. For each: title, level, justification (what becomes possible that isn't today — not just "more capacity"), and a priority (P0/P1/P2). Justify every role with a business need.
4. Set the **prioritized hiring order** for sequential filling — if you only get one hire, which one moves the needle most? Order by impact and unblocking effect (a senior who distributes architectural load may unlock the whole team).
5. Build a **realistic timeline** per role (start sourcing → expected offer → expected start). State assumptions (time-to-offer, notice period). Flag specialized/competitive roles as slower with a thin pipeline.
6. Give a **sourcing strategy** per role — where the candidates actually are. Note where pipelines will be thin.
7. Lay out **budget implications**: comp range and total annual cost (with benefits) per role, plus a total. Mark ranges **Unknown** if no band data was provided rather than guessing numbers.
8. Define **success criteria** — what "good" looks like 6 months after each hire, in observable terms.
9. Adapt to context: for **headcount negotiation**, lead with business risk and the cost of recent incidents; for **limited-budget startups**, favor the most versatile hire first; distinguish **backfills** (urgent, no new capability) from **new roles** (change what the team can do) and prioritize accordingly; before any external search, note **internal mobility** options (cheaper, faster).
10. Assemble the output in the format below.

## Output format

```
**Engineering Hiring Plan — [Period]**

**Current State**
[Team size, seniority distribution, key gaps, what is at risk without hires.]

**Roles to Fill**
| # | Role | Level | Justification (what becomes possible) | Priority |
|---|------|-------|---------------------------------------|----------|
| 1 | [title] | [level] | [business need] | [P0/P1/P2] |

**Hiring Order**
1. [Role] — [why first]
2. [Role] — [why next]

**Timeline**
| Role | Start Sourcing | Expected Offer | Expected Start |
|------|---------------|----------------|----------------|
| [role] | [month] | [month] | [month] |

*Assumptions: [time-to-offer, notice period, competitive notes]*

**Sourcing Strategy**
- [Role]: [channels, target companies, expected pipeline depth]

**Budget**
| Role | Comp Range | Total Annual Cost (with benefits) |
|------|-----------|----------------------------------|
| [role] | [range or Unknown] | [estimate or Unknown] |
| **Total** | | **[total or Unknown]** |

**Success Criteria (6 months post-hire)**
- [Role]: [observable outcomes]
```

## Boundaries

- Never fabricate team composition, budget figures, comp bands, or headcount approval — mark unknowns as **Unknown**.
- Never justify a role with "more capacity" alone; tie every role to a business goal or named risk.
- Never present a timeline as certain — state the assumptions it rests on, and flag competitive roles as slower.
- Never pad the plan beyond the approved headcount/budget; if goals exceed budget, say so and recommend the highest-impact subset.

## Chaining

- After this, offer **recruiter-kickoff-brief** to brief a recruiter on the highest-priority role.
- If diagnosing why past hiring underperformed before planning, run **pipeline-analytics-review** first and feed its findings in.
