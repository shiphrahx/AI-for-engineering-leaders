---
name: sprint-planning-breakdown
description: >
  Produces a sprint-ready breakdown of an epic: well-scoped tickets (each with description,
  acceptance criteria, day estimate, dependencies, and suggested assignee level), a dependency
  graph, a sprint allocation across the team, and risk flags. Use when the user says "break
  this epic into tickets", "split this into stories", or pastes an epic with a definition of
  done, team makeup, and sprint length. Use this for slicing one epic into tickets — use
  capacity-planning for cross-project bandwidth and quarterly-roadmap for the quarter's plan.
---

# Sprint Planning Breakdown

Break an epic or large feature into sprint-sized tickets — each independently deliverable (or clearly blocked), estimated, with acceptance criteria — optimised for parallel work.

## Inputs to gather

Gather these before breaking down. If any are missing, ask for them in a single batched question — never invent the definition of done, team makeup, or sprint length. Mark anything genuinely unavailable as **Unknown**.

- **Epic** — what's being built
- **Definition of done** — what "complete" means for the whole epic
- **Team** — size and composition (seniority, frontend/backend split)
- **Sprint length** — e.g. 2 weeks
- **Open product questions** — anything (like role definitions) that needs product input before work starts

## Steps

1. Write the **epic summary** — what's being built and the definition of done for the whole epic.
2. Break into **tickets**, each scoped to roughly 1–3 days for a single engineer. For each ticket give: title, description, acceptance criteria (specific and testable), estimate in days, dependencies (or "None"), and suggested assignee level (senior/mid/junior). Group by area (e.g. backend/frontend) where it aids clarity.
3. Draw a **dependency graph** — a simple list or ASCII diagram showing which tickets block others and which can run in parallel.
4. Produce a **sprint allocation** — map tickets across sprints given team capacity and the dependency order, sequencing so engineers can start in parallel on day one and noting where capacity is free.
5. Flag **risks** — what's underestimated or uncertain (e.g. large-dataset performance, unanswered product questions, novel complexity), with a fallback where one exists.
6. Adapt to context: for uncertain scope, add a timeboxed (1–2 day) spike ticket up front to investigate and re-estimate. For a solo developer, drop parallelism and sequence linearly — still break into small tickets for focus and clear commit points. For a non-technical PM reviewer, add a user-story line per ticket ("As an admin, I can …"). For a tech-debt epic, include acceptance criteria like "existing tests still pass" and "no regression in [metric]".
7. Assemble the output in the format below.

## Output format

```
**Epic: [Name]**

**Summary:** [What's being built and the epic's definition of done]

**Ticket Breakdown**
| # | Title | Description | Acceptance Criteria | Est. | Dep. | Level |
|---|-------|-------------|---------------------|------|------|-------|
| [B1] | [title] | [what] | [- criterion ...] | [Nd] | [None / #] | [Senior/Mid/Junior] |

**Dependency Graph**
```
[B1 ──→ B2]
[F1 (parallel)]
```

**Sprint Allocation**
*Sprint 1:*
- [Role/engineer]: [ticket] ([Nd]) → [ticket] ([Nd])

*Sprint 2:*
- [remaining work, integration, polish; note free capacity]

**Risks**
- [Underestimated or uncertain item, with fallback]
```

## Boundaries

- Never invent the definition of done, team composition, or sprint length — mark them **Unknown**.
- Never leave a ticket without acceptance criteria or an estimate — an unestimated, unspecified ticket isn't sprint-ready.
- Never bury a cross-ticket dependency — if a ticket is blocked, mark it so explicitly.
- Estimates are the model's starting point; flag them for the user to validate with the team rather than presenting them as committed.

## Chaining

- No natural successor — this is usually a terminal artifact handed straight into the team's tracker for the sprint.
