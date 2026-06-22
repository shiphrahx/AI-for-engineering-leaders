---
name: team-health-survey-analysis
description: >
  Produces a root-cause analysis and action plan from team health or engagement survey results
  — executive summary, scored overview with trends, qualitative themes, root causes for the
  lowest scores, owned actions, and a transparent share-back plan. Use when the user pastes
  survey scores and free-text comments and says "analyse our pulse survey", "what's the action
  plan from these results", or "find the themes". Use this for interpreting results and acting
  on them, not for designing the survey or tracking action items over time.
---

# Team Health Survey Analysis

Go beyond the numbers: connect themes across questions, hypothesise root causes behind the low scores, and produce an action plan that addresses systemic issues rather than symptoms.

## Inputs to gather

Gather these before analysing. If any are missing, ask in a single batched question — never invent scores, trends, comments, or a response rate. Mark anything genuinely unavailable as **Unknown**.

- **Team** — name and size
- **Survey tool** — what was used
- **Response rate** — how many responded
- **Scores by question** — ideally with the previous period for comparison
- **Free-text comments** — however messy or raw

## Steps

1. Read scores and comments together before analysing. Categorise scores: strong (4+), watch (3-3.9), concern (<3). Track each as improving, stable, or declining — a declining score matters more than its absolute value, and a high score that drops still warrants attention.
2. Group the free-text comments by theme. Treat a single comment as a weak signal and 3+ similar comments as a pattern.
3. Write an **Executive Summary** — overall health in 2-3 sentences, the biggest strength, the biggest concern. Connect related findings (poor tooling and too many meetings both erode productive time).
4. Build a **Score Overview** table with score, trend arrow, and a signal indicator per question.
5. Write **Qualitative Themes** — patterns from comments, grouped, with a count per theme.
6. Do **Root Cause Analysis** for the bottom 2-3 scores: hypothesise *why*, connect to comment evidence, and quantify the cost where you can ("30 min/day across 9 engineers = ~4.5 engineer-hours/day"). A low score alone is not insight — tie it to evidence. "I don't know" responses on manager/strategy questions usually signal a communication gap, not a real deficiency.
7. Build an **Action Plan** of 3-5 specific actions, each with an owner, a timeline, and the score/theme it addresses.
8. Write **Sharing with the Team** — how to present results transparently, present the action plan alongside them to show you're already acting, thank the team for honesty, and never identify or speculate about who wrote which comment.
9. Handle edge cases: for a **low response rate (<70%)**, note results may not be representative and focus on comment themes over score decimals. For **all-high scores**, ask "what would make a 4 a 5?". For **one very low outlier**, investigate in 1:1s, not group settings. For **multi-team comparison**, resist ranking teams; surface cross-team themes that suggest org-level issues.
10. Assemble the output in the format below.

## Output format

```
**[Team] — [Survey Period] Analysis**

**Executive Summary**
[2-3 sentences: overall health, top strength, top concern]

**Score Overview**
| Category | Score | Trend | Signal |
|----------|-------|-------|--------|
| [question] | [X.X] | [↑/↓/→] | [🟢/🟡/🔴] |

**Qualitative Themes**
- **[Theme]** ([N] comments): [Pattern summary]

**Root Cause Analysis**
- **[Low-score item] ([X.X]):** [Why it's low, connected to comment evidence, quantified if possible]

**Action Plan**
| Action | Owner | Timeline | Addresses |
|--------|-------|----------|-----------|
| [specific action] | [who or Unknown] | [when] | [which score/theme] |

**Sharing with the Team**
[How to present results transparently without identifying any commenter]
```

## Boundaries

- Never fabricate scores, trends, comments, owners, or response rates. Mark unknowns as **Unknown** and ask.
- Never identify or speculate about who wrote a given comment — anonymity is the basis of honest survey input.
- Don't treat a single comment as a team-wide pattern, and don't celebrate high scores into complacency.
- Cannot verify comment authenticity or whether previous action items were completed — flag that explicitly.
- Score interpretation depends on company and survey norms — the user provides that context.

## Chaining

- After this, offer **one-on-one-prep** to follow up on individual or sensitive signals (especially a single low outlier) privately rather than in a group setting.
- For a team-culture theme that needs a deliberate reset, offer **team-values-workshop**.
