---
name: promotion-case
description: >
  Produces a committee-ready promotion case for a direct report — a summary recommendation,
  evidence of next-level performance mapped to the target level, peer perspective, growth
  trajectory, readiness ("why now"), and pre-empted concerns. Use when the user says "build a
  promotion case", "write up [name] for promo", or pastes accomplishments and target-level
  expectations. Use this to argue one person is already operating at the next level; use
  career-ladder-draft to define the levels themselves, and performance-review-draft for the
  routine periodic review.
---

# Promotion Case

Build a case that demonstrates the person is *already* operating at the next level — with concrete evidence, not aspiration. Focus on impact, scope, and influence, not just output.

## Inputs to gather

Gather these before drafting. If any are missing, ask in a single batched question — never invent accomplishments, peer quotes, or impact. Mark anything genuinely unavailable as **Unknown**.

- **Person** — name, current level, proposed level
- **Target level expectations** — what the target level requires
- **Evidence** — accomplishments and specific examples from the review period
- **Peer perspectives** — feedback and quotes from colleagues and stakeholders

## Steps

1. Test the evidence first: if you can't find 3+ concrete examples at the next level, the person likely isn't ready — say so and recommend the "here's what you need to do" conversation instead of a thin case.
2. Write a one-paragraph **Summary Recommendation** — who, from what level to what level, and why, ending on "they're not growing into it, they're already operating there".
3. Write **Evidence of Next-Level Performance** — 3-5 examples, each mapped explicitly to a target-level expectation (drives complex projects, contributes to technical direction, mentors, influence beyond team). Use measurable impact.
4. Write **Peer and Stakeholder Perspective** — what others say, especially recognition from outside the immediate team and from respected senior people. Use direct quotes.
5. Write **Growth Trajectory** — how they've grown during the period; name behaviours that are new, not always-present.
6. Write **Readiness Signals** ("Why Now") — why now and not in six months; note recognition debt and retention risk.
7. Write **Potential Concerns** — pre-empt the objections the committee will raise (scope, tenure) and answer each with evidence.
8. Adapt to context: for a **conservative committee**, front-load the strongest, most clearly-mapped example and include quotes from respected peers. For a **skip-level promotion** (e.g. L3→L5), note it's extremely rare and check feasibility with your skip-level first. If the **org has no formal committee**, this still works as an alignment doc for your manager before you tell the engineer.
9. Assemble the output in the format below.
10. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Promotion Recommendation: [Name], [Current] → [Target]**

**Summary**
[One paragraph: who, the move, and why — already operating at the level]

**Evidence of [Target] Performance**

*[Target-level expectation]:*
[Specific example with measurable impact, mapped to the expectation]

[repeat per expectation]

**Peer and Stakeholder Perspective**
[What others say, with quotes; emphasise cross-team and senior recognition]

**Growth Trajectory**
[How they've grown; which behaviours are new]

**Why Now**
[Readiness, recognition debt, retention risk]

**Potential Concerns**
- *"[Likely objection]":* [Evidence-based rebuttal]
```

## Boundaries

- Never fabricate accomplishments, impact, peer quotes, or stakeholder names. Mark unknowns as **Unknown** and ask.
- Never inflate current-level work into next-level evidence. If the evidence isn't there, recommend waiting — a thin case that gets rejected hurts the person.
- Tenure is not a promotion criterion; argue from demonstrated behaviour and impact against the ladder, not time served.
- Keep the case based on documented work; avoid style- or likeability-based reasoning that can carry bias.
- This is a confidential people document — keep it private until shared through the proper channel.

## Chaining

- For a newly promoted (or promotion-bound) staff IC, offer **staff-engineer-scope-doc** to define their concrete remit at the new level.
- If the evidence falls short, offer **difficult-conversation-prep** to plan the "here's the path forward" conversation, or **performance-review-draft** to anchor the gap in the next review.
