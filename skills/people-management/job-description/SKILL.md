---
name: job-description
description: >
  Produces an honest, specific engineering job description that attracts strong candidates —
  role in one line, what they'll actually work on, must-haves vs nice-to-haves, what the team
  offers, who they'll work with, and the hiring process. Use when the user says "write a job
  description", "draft a JD for [role]", or pastes a role title, team context, key projects,
  and requirements. Use this to attract and filter candidates for an open role; use
  interview-rubric to design how you'll evaluate them, and career-ladder-draft for internal
  level definitions rather than an external posting.
---

# Job Description

Write a JD that sells the role honestly, filters effectively, and respects the candidate's time — specific about what the person will actually do, not a keyword dump of generic competencies.

## Inputs to gather

Gather these before drafting. If any are missing, ask in a single batched question — never invent the comp range, team details, or requirements. Mark anything genuinely unavailable as **Unknown** rather than guessing.

- **Role** — title and level
- **Team** — size, stage, what it does
- **Key projects** — the 3-5 specific things this person will work on
- **Must-haves** — the real requirements (aim for 4-5)
- **Nice-to-haves** — preferred but not required (aim for 3-4)
- **Comp range** — salary and equity, if shareable

## Steps

1. Write **The Role** in one sentence: what this person will do and why it matters.
2. Write **What You'll Work On** — 3-5 specific projects or problem areas, framed as interesting problems, not a responsibilities list.
3. Write **What We're Looking For** — separate must-haves (4-5, honestly required) from nice-to-haves (3-4). Resist requirement inflation; every must-have filters out real candidates.
4. Write **What We Offer** — comp and benefits, plus the genuinely interesting part: team culture, technical challenges, autonomy, growth.
5. Write **About the Team** — who they'll work with, team size and composition, how the team actually works.
6. Write the **Hiring Process** — the stages, so candidates know what to expect and roughly how long it takes; commit to feedback.
7. Adapt to context: for a **junior role**, cut must-haves to 2-3 and emphasise learning, mentorship, and growth. For a **remote role**, be explicit about timezone expectations, communication norms, and how the team bonds — "here's how we make remote work" is a selling point. For a **competitive market**, lead with what makes the role unique, not "we're growing fast". For an **internal JD** (levelling/backfill), skip the marketing and keep "what you'll work on" and "what we're looking for".
8. Assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Level Title] — [Team]**

**The Role**
[One sentence: what this person does and why it matters]

**What You'll Work On**
- **[Project/problem]:** [Specific description framed as an interesting problem]

**What We're Looking For**

*Must-haves:*
- [Real requirement]

*Nice-to-haves:*
- [Preferred but not required]

**What We Offer**
- [Comp + equity]
- [Working model]
- [The genuinely interesting part]

**About the Team**
[Who they'll work with, team size, how the team works]

**Hiring Process**
1. [Stage and rough timing]
...
```

## Boundaries

- Never invent the comp range, team facts, or requirements. Mark unknowns as **Unknown** and ask — never publish a guessed salary or fabricated benefit.
- Don't inflate must-haves or use coded language ("rockstar", "works hard plays hard", "young team", "culture fit") that deters qualified or underrepresented candidates; describe the work and the requirements neutrally.
- Don't promise comp, equity, timelines, or process steps the user hasn't confirmed are real.
- Keep requirements job-related and lawful — avoid proxies for age, gender, nationality, or other protected characteristics.

## Chaining

- After this, offer **interview-rubric** to design the structured evaluation for the loop you've described.
- For the broader hiring funnel and headcount, see **hiring-pipelines/hiring-plan**.
