---
name: feedback-synthesis
description: >
  Produces a fair, anonymised synthesis of peer feedback for one person — an overall narrative,
  consistent strengths and growth areas (themes echoed by 2+ reviewers), outlier comments, and
  actionable takeaways. Use when the user pastes feedback from several colleagues and says
  "synthesise this peer feedback", "find the patterns", or "what are the themes across these
  reviews". Use this to distil multiple raw inputs before a review; use performance-review-draft
  to write the actual review, and one-on-one-prep for a single live conversation.
---

# Feedback Synthesis

Distil a mix of praise, criticism, and vague platitudes from several reviewers into a coherent narrative that separates signal from noise — fair, specific, actionable, and anonymous.

## Inputs to gather

Gather these before synthesising. If any are missing, ask in a single batched question — never invent feedback, invent a reviewer, or attribute a quote you weren't given. Mark anything genuinely unavailable as **Unknown**.

- **Person** — name and role
- **Reviewers** — how many, and their relationship (team member, cross-team, PM, designer, etc.)
- **Raw feedback** — each reviewer's comments, however unstructured

## Steps

1. Read all feedback before synthesising. Tag each comment by theme and by how many reviewers echo it.
2. Weigh the signal: a theme from 2+ reviewers is a **pattern**; a single comment is a **data point** (could be insightful or context-specific). 4 of 5 reviewers naming something is stronger than 2 of 5 — say so.
3. Write a 2-3 sentence **Overall Narrative** capturing the consensus view.
4. List **Consistent Strengths** (2+ reviewers) with anonymised evidence.
5. List **Consistent Growth Areas** (2+ reviewers) with evidence and a suggested constructive framing — look for the systemic pattern, not "they did X wrong".
6. List **Outlier Feedback** — notable single-reviewer comments worth considering, flagged as weaker signal.
7. Write 2-3 specific, behavioural **Actionable Takeaways**.
8. Handle edge cases: for **conflicting feedback**, note the contradiction and offer a plausible explanation ("Reviewer A found them communicative while Reviewer C didn't — may reflect within-team vs cross-team patterns"). For **sparse or vague feedback** ("great engineer"), note that it lacked specifics and don't inflate it; consider asking for examples. For **negative-heavy feedback**, check your own bias and add the manager's own observations as a counterweight if appropriate. For **all-positive feedback**, look harder — even high performers have development areas.
9. Assemble the output in the format below. When used in a review conversation, share the themes, not the raw quotes.

## Output format

```
**Feedback Synthesis: [Name]**

**Overall Narrative**
[2-3 sentences on the consensus view]

**Consistent Strengths ([N]+ reviewers)**
- **[Theme]:** [Anonymised evidence drawn from multiple sources]

**Consistent Growth Areas ([N]+ reviewers)**
- **[Theme]:** [Evidence and a constructive framing]

**Outlier Feedback**
- [Notable single-source comment, flagged as weaker signal, with context on why it's worth noting]

**Actionable Takeaways**
1. [Specific, behavioural recommendation]
2. [Another]
3. [Third if warranted]
```

## Boundaries

- Never attribute a quote to a named reviewer in the output. Maintain anonymity — "multiple peers noted X" is sufficient.
- Never fabricate feedback, reviewers, or counts. Distinguish a pattern (2+ sources) from a single data point; don't present one voice as consensus.
- Don't inflate vague praise into a strength or a single gripe into a systemic flaw. Mark gaps as **Unknown** and ask for examples.
- Cannot verify feedback against actual events or assess reviewer credibility — flag where the synthesis depends on unverified claims.
- This is sensitive people data. Keep it private and redact identifying details before sharing.

## Chaining

- After this, offer **performance-review-draft** — the synthesised themes feed directly into the review's strengths and growth areas.
- For a specific behavioural concern surfaced here, offer **difficult-conversation-prep** to plan how to raise it.
