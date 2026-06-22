---
name: career-ladder-draft
description: >
  Produces a concrete engineering career ladder — per-level descriptions covering scope,
  technical expectations, collaboration, leadership, and observable example behaviours, plus
  the distinguishing behaviours between adjacent levels. Use when the user says "draft a career
  ladder", "define our engineering levels", "our level expectations are too vague", or pastes
  org context and a list of levels. Use this for the org-wide framework that defines levels;
  use promotion-case to argue one person fits a level, and staff-engineer-scope-doc to define
  a single staff role's concrete remit.
---

# Career Ladder Draft

Define engineering levels with clear, observable expectations — so someone reading a level can tell whether they meet it. Focus on scope of impact, autonomy, and leadership, not just technical skill.

## Inputs to gather

Gather these before drafting. If any are missing, ask in a single batched question — never invent the org's size, level names, or existing pain points. Mark anything genuinely unavailable as **Unknown**.

- **Organisation context** — size, stage, and team mix (product/platform)
- **Levels to define** — the list of levels and their names/titles
- **Current pain points** — what's wrong with the existing ladder, if any

## Steps

1. For each level, write a one-sentence **summary** of what the level means.
2. Define **Scope** — the typical sphere of influence (task, feature, project, team, multiple teams, org, company).
3. Define **Technical** expectations — what technical work looks like at this level, in observable terms.
4. Define **Collaboration & communication** — how they work with others, across teams, and with non-technical stakeholders.
5. Define **Leadership** — how they lead (not manage): mentoring, standards, driving improvements, building consensus.
6. Give 3-4 concrete **Example behaviours** — "you'd see this person doing..." statements, not competencies.
7. After the levels, write the **distinguishing behaviours** between the trickiest adjacent levels (e.g. Senior→Staff): name the difference in scope of impact and ambiguity, not "bigger projects".
8. Adapt to context: for a **startup (<30 engineers)** you may only need junior through senior — adding Staff before ~50 engineers creates a title without a role. For a **management track**, mirror the IC ladder with an EM track that has overlapping scope but a divergent "how" (lead through people vs technical influence). For an **existing ladder being updated**, keep the level names and add 2-3 distinguishing behaviours per boundary. For **diverse team backgrounds**, avoid culture-specific expectations like "speaks up in meetings" (disadvantages introverts and non-native speakers) — focus on impact and outcomes, not style.
9. Assemble the output in the format below.

## Output format

```
**Engineering Career Ladder**

---

**[Level code] — [Title]**
*[One-sentence description of what this level means]*

**Scope:** [Sphere of influence]
**Technical:** [Observable technical expectations]
**Collaboration:** [How they work with others]
**Leadership:** [How they lead, not manage]

**Example behaviours:**
- [Concrete "you'd see this person doing..." example]
- [Another]

---
[repeat per level]

**The [Level A]→[Level B] Distinction**
[What most clearly separates the two — scope of impact and ambiguity, not project size]
```

## Boundaries

- Never invent the org's size, stage, level names, or pain points. Mark unknowns as **Unknown** and ask.
- Never write vague competencies ("demonstrates technical excellence") — every expectation must be observable enough that a person can self-assess against it.
- Avoid culture- or style-based expectations that disadvantage introverts, non-native speakers, or neurodivergent engineers; frame on impact and outcomes.
- Don't conflate levelling with compensation — comp banding is org- and jurisdiction-specific and out of scope.
- A ladder describes expectations, not individuals — never reference a specific person's performance in the framework itself.

## Chaining

- After this, offer **performance-review-draft** — reviews should be written against these level expectations.
- For an individual who fits the next rung, offer **promotion-case**; for a staff IC's concrete remit, offer **staff-engineer-scope-doc**.
