---
name: project-pre-mortem
description: >
  Produces a project pre-mortem: failure modes across technical, people, process, and
  external dimensions — each with likelihood, impact, and a preventive action — plus the
  top kill risks and a before-we-start action plan. Use when the user says "run a
  pre-mortem", "what could go wrong with this project", "how could this fail", or pastes a
  project description, timeline, and team before kickoff. Use this prospectively before a
  project starts — use incident-postmortem for analysing a failure that already happened.
---

# Project Pre-Mortem

Imagine it's three months out and the project has failed, then work backward to the most likely failure modes — so the team can prevent them instead of writing postmortems about them later.

## Inputs to gather

Gather these before generating risks. If any are missing, ask for them in a single batched question — never invent the project's scope, timeline, or team. Mark anything genuinely unavailable as **Unknown**.

- **Project** — what's being built
- **Timeline** — duration and key dates
- **Team** — composition and seniority mix
- **Success criteria** — what "done and successful" means
- **Known concerns** — any worries the user already holds

## Steps

1. Restate the **project context** — project, timeline, and success criteria — so the reader is grounded.
2. Generate **failure modes** in four categories. For each mode write what went wrong, likelihood (high/medium/low), impact (high/medium/low), and a specific preventive action:
   - *Technical* — architecture, data integrity, performance, integration
   - *People/Team* — capacity, key-person risk, burnout, under-utilised juniors
   - *Process* — scope creep, untested rollback, coordination, decision-making
   - *External* — dependencies, vendors, undocumented downstream consumers, incidents consuming capacity
3. Lean on common patterns by project type: migrations (dual-write data inconsistency, undocumented dependencies, untested rollback); new features (scope creep, integration harder than expected, performance at scale untested); platform/infra (downstream teams break on undocumented APIs, unclear user migration path, team lacks production experience with new tech).
4. Identify the **top 3 kill risks** — highest likelihood × impact, the failures most likely to actually sink the project.
5. Write a **pre-mortem action plan** — specific steps to take before or early in the project to address the top risks, each with an owner and a due date (mark **Unknown** if not provided).
6. Adapt to context: for a short project (<4 weeks), cover the top ~5 failure modes only. For hardware/infra, add a supply-chain/procurement category. Frame the output as input to a team session — generate the list, then prompt the user to bring it to the team and ask "what did we miss?", since domain experts will see risks the model cannot.
7. Assemble the output in the format below.

## Output format

```
**Pre-Mortem: [Project Name]**

**Context**
[Project, timeline, and success criteria restated]

**Failure Modes**

*Technical*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

*People/Team*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

*Process*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

*External*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

**Top 3 Kill Risks**
1. **[Risk]** — [why it's highest combined likelihood × impact]

**Pre-Mortem Action Plan (Before / Early in the Project)**
1. [Action] (Owner: [who or Unknown], Due: [when or Unknown])
```

## Boundaries

- Never invent project scope, timeline, team members, or success criteria — mark them **Unknown**.
- Never assign an owner who wasn't named — mark **Unknown** rather than volunteering someone.
- Never present this as a complete risk list — it covers foreseeable risks; black swans and domain-specific risks need the team's review.
- Likelihood and impact ratings are judgment calls — present them as such, not as measured probabilities.

## Chaining

- No natural successor — this is usually a terminal artifact. (When a project later fails despite the pre-mortem, the natural follow-up is **incident-postmortem**.)
