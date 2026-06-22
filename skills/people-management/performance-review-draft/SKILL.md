---
name: performance-review-draft
description: >
  Produces an evidence-based, developmental performance review for a direct report —
  summary, accomplishments, strengths, growth areas, forward goals, and an overall rating.
  Use when the user says "write a performance review", "draft my review for [name]", "review
  cycle", or pastes 1:1 notes, peer feedback, and project outcomes for an engineer. Use this
  for the full periodic review of one person; use feedback-synthesis to first distil raw peer
  input into themes, promotion-case to argue for a level change, and pip-documentation when
  the person is underperforming and needs a formal improvement plan rather than a review.
---

# Performance Review Draft

Turn scattered observations into a clear, fair review the engineer can learn from — every claim backed by a specific example, tone supportive and developmental rather than evaluative and distant.

## Inputs to gather

Gather these before drafting. If any are missing, ask for them in a single batched question — never invent an accomplishment, a metric, a rating, or a quote. Mark anything genuinely unavailable as **Unknown** in the output.

- **Review period** — the dates covered
- **Engineer** — name, level, and tenure
- **Role expectations** — what their level is expected to deliver
- **Raw notes and observations** — 1:1 notes, project outcomes, incidents, your own observations
- **Peer feedback summary** — themes or quotes from colleagues, if collected (feedback-synthesis output works well here)

## Steps

1. Read all notes and feedback before writing. Map each observation to a strength, a growth area, or an accomplishment. Flag claims you cannot back with an example as **Unknown** rather than asserting them.
2. Write a 2-3 sentence **Summary** capturing the overall performance narrative — the through-line, not a list.
3. List 3-5 **Key Accomplishments**, each with concrete impact described (numbers where available, scope and outcome otherwise). Frame against level expectations: "strong L5 work", "this is Staff-level impact".
4. Identify 2-3 **Strengths**, each with evidence — prefer a specific instance or peer observation over an adjective.
5. Identify 2-3 **Growth Areas**. State the evidence, not the conclusion: "the project shipped 3 weeks late" beats "time management is an issue." Pair each with a specific, actionable suggestion ("Try X...", "Practice Y...").
6. Write 2-3 forward-looking **Goals** for the next period — concrete and observable, tied to growth areas or next-level expectations.
7. Assign an **Overall Rating** on the org's scale with a brief, evidence-grounded justification. Even high performers have a growth area; even struggling engineers have a strength.
8. Adapt to context: for an **underperformer**, be direct but kind, lead with evidence not conclusions, include concrete improvement steps. For a **high performer to retain**, name the promotion path explicitly ("here's what I'd need to see to advocate for [level]"). For a **first review** of this person, caveat the shorter observation window and ask them to self-review first as input. If the **company's format differs**, adapt the content to fit but keep the principle: every claim backed by evidence, every growth area paired with a suggestion.
9. Assemble the output in the format below.

## Output format

```
**Performance Review: [Name] — [Period]**

**Summary**
[2-3 sentences: the overall performance narrative and key theme]

**Key Accomplishments**
- **[Project/area]:** [What they did and its measurable impact. Tie to level expectations.]

**Strengths**
- **[Strength]:** [Evidence — a specific instance from the period]

**Growth Areas**
- **[Area]:** [Observable evidence, not a label.] *Suggestion: [specific, actionable step]*

**Goals for Next Period**
1. [Forward-looking, observable objective]
2. [Second goal]
3. [Third goal if appropriate]

**Rating: [Scale value]**
[Brief justification grounded in the evidence above]
```

## Boundaries

- Never fabricate accomplishments, metrics, quotes, ratings, or dates. Mark unavailable inputs as **Unknown** and ask for them. Project outcomes and level rubrics are org-specific — the user must provide them.
- Never state a conclusion without evidence — every strength and growth area is backed by a specific, observable example.
- Base the review on documented behaviour, not impressions or personality. Avoid culture- or style-based judgments ("not assertive enough") that disadvantage introverts or non-native speakers; assess impact and outcomes.
- Never use a review to justify a predetermined decision (e.g. retroactively building a case for termination — that is pip-documentation territory, done with HR).
- This is a sensitive people document. Do not store unreviewed drafts in shared spaces; keep them private until finalised. Maintain peer anonymity — share themes, not which colleague said what.

## Chaining

- For a strong performer ready for the next level, offer **promotion-case** to build the formal argument.
- For an underperformer, offer **pip-documentation** (and involve HR) or **difficult-conversation-prep** to plan the delivery.
- If you have raw peer feedback not yet distilled, run **feedback-synthesis** first and feed its themes into this review.
