---
name: take-home-exercise-design
description: >
  Produces a fair, 2-3-hour take-home exercise: a realistic brief, an explicit and enforced
  time cap, what you ARE and are NOT evaluating, a strong-hire/hire/no-hire rubric, and
  candidate submission instructions. Use when the user says "design a take-home", "coding
  exercise for candidates", "build an evaluation rubric for a take-home", or gives a role plus
  the skills and domain to assess. Use this to create the exercise and rubric — not to score a
  returned submission or synthesize loop feedback (candidate-evaluation-summary), nor to run
  the live screen (phone-screen-script).
---

# Take-Home Exercise Design

Design a take-home that demonstrates real skill, is completable in 2-3 hours, and is scored against a rubric — respecting candidate time, because over-scoped exercises are the top reason strong candidates drop out.

## Inputs to gather

Gather these before designing. If any are missing, ask for them in a single batched question — never invent the role's skills or domain. Mark anything genuinely unavailable as **Unknown** in the output.

- **Role** — title and level
- **Skills to assess** — the specific competencies this exercise must surface
- **Domain** — the team's problem space, so the task is realistic
- **Accepted languages / format** — if the team has constraints

## Steps

1. Design the **brief** around a realistic, scaled-down version of the team's actual work — a task that exercises the named skills without requiring setup the candidate shouldn't have to build.
2. State the **time expectation** explicitly (2-3 hours max) and mean it: tell candidates an incomplete-but-well-structured solution beats a complete-but-rushed one, and to note what they'd improve with more time.
3. List **what you're evaluating** — map each named skill to an observable aspect of the submission (design, error handling, data consistency, testing, code quality).
4. List **what you're NOT evaluating** — explicitly remove worry items (UI, deployment config, performance tuning, specific frameworks) so candidates don't over-invest.
5. Build the **rubric** as a table: one row per criterion, columns for Strong Hire / Hire / No Hire, each cell describing observable behavior — not adjectives.
6. Write **submission instructions**: what to submit, format (repo or zip), required README contents (how to run, key decisions, what they'd improve), accepted languages, and a generous due window with no penalty for early submission.
7. Adapt to context: address the **time complaint** head-on (be brutally honest about hours; a 6-hour exercise loses good candidates); offer a **pair-programming alternative** for candidates who prefer live collaboration; instruct **blind review** (strip names before the panel sees submissions) to reduce bias; consider **compensating** for time to signal respect and lift completion rates.
8. Assemble the output in the format below.

## Output format

```
**Take-Home Exercise: [Title]**

**Brief**
[What the candidate builds, with clear requirements and provided assets.]

**Time:** Please spend no more than [2-3] hours. We mean this. [Incomplete-but-structured > complete-but-rushed. Note what you'd improve with more time.]

**What We're Evaluating**
- [Skill]: [observable aspect]

**What We're NOT Evaluating**
- [Out-of-scope item]

**Rubric**
| Criteria | Strong Hire | Hire | No Hire |
|----------|------------|------|---------|
| [criterion] | [observable] | [observable] | [observable] |

**Submission**
- [Format: repo or zip]
- README with: how to run, key design decisions, what you'd do differently with more time
- Language: [accepted languages]
- Due: [generous window, no penalty for early submission]
```

## Boundaries

- Never invent the role's skills, domain, or accepted languages — mark unknowns as **Unknown** and ask.
- Never design an exercise that genuinely takes longer than the stated cap; if the skills can't be assessed in 2-3 hours, narrow the skills, not the candidate's time.
- Never require candidates to do real production or unpaid client work disguised as an exercise.
- Never write a rubric in adjectives ("good code"); every cell must describe observable behavior so reviewers score consistently.

## Chaining

- After this, offer **interviewer-calibration-guide** so reviewers score the rubric consistently.
- Once the full loop completes, **candidate-evaluation-summary** synthesizes the take-home and interview signals.
