---
name: sprint-retro-summary
description: >
  Produces an actionable sprint retrospective summary: grouped themes, root causes for the
  top issues, owned action items, and a trend read versus prior retros. Use when the user
  says "summarise the retro", "synthesise this retro feedback", or pastes raw sticky notes,
  retro comments, or vote counts after a retrospective. Use this for distilling completed
  retro feedback into change — use sprint-planning-breakdown to break the next epic into
  tickets, not to run or facilitate the retro session itself.
---

# Sprint Retro Summary

Distill a board of raw retro feedback into actionable themes with clear owners — constructive and team-oriented throughout, so the retro actually leads to change.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent feedback, owners, or trends. Mark anything genuinely unavailable as **Unknown**.

- **Sprint** — identifier (e.g. Sprint 18, Q1 Week 3)
- **Team** — name and size
- **Sprint goal** and whether it was achieved (yes / no / partial)
- **Raw retro feedback** — what went well, what didn't, ideas; vote counts if available
- **Prior retros** — the last 2–3 summaries or recurring themes, if available (for the trends section)

## Steps

1. Read all the feedback. Group similar items into themes; distinguish symptoms from root causes and actionable items from venting.
2. Write a one-line **at a glance**: what went well overall and the main challenge.
3. Write **what went well** — 2–3 themes, each with supporting evidence from the feedback. Items that worked but could regress become "keep doing".
4. Write **what didn't go well** — 2–3 themes with evidence, framed constructively (systemic, not personal).
5. For the top 1–2 issues, write **root causes** — go one level deeper into why. Frame the cause as a process or system gap, never as a named person's fault.
6. Weight signals: 3+ people raising the same issue is strong; high votes plus specific examples gets prioritised; vague complaints ("communication is bad") need specificity before becoming an action item.
7. Derive **action items** — specific, measurable, owned, with a timeframe. Cap at 2–3 (or fewer when morale is low) so they actually get done. Mark owner **Unknown** rather than assigning someone not named.
8. Write **trends** — how this retro compares to the last 2–3 (improving, stable, or recurring), marking improving items and warning signs. If a theme recurs for a third time, escalate it explicitly.
9. Adapt to context: when morale is low, give more space to wins and keep action items to 2–3 max. For a new team or manager, add a "feedback on the retro process" section. When sharing with stakeholders, strip individual-level feedback and personal frustrations — share themes and action items only. Keep interpersonal friction out of the written summary; flag it for offline handling.
10. Assemble the output in the format below.

## Output format

```
**[Sprint] Retro Summary — [Team]**

**At a Glance:** [One line: overall outcome and the main challenge]

**What Went Well**
- **[Theme].** [Evidence — what specifically worked]

**What Didn't Go Well**
- **[Theme].** [Evidence, framed constructively]

**Root Causes**
- *[Issue]:* [One level deeper — the process/system gap behind it]

**Action Items**
| Action | Owner | By When |
|--------|-------|---------|
| [specific, measurable step] | [name or Unknown] | [sprint/date] |

**Trends**
- ✅ [Improving theme — vs prior retros]
- ⚠️ [Recurring or worsening theme — escalate if 3rd time]
```

## Boundaries

- Never name an individual as the cause of a problem — find and state the systemic enabler instead.
- Never fabricate feedback, owners, dates, or trend history — mark unknowns as **Unknown**.
- Never include interpersonal friction or personal frustrations in a summary shared beyond the team.
- Never let the action-item list balloon past what the team can realistically do — more than 2–3 means none get done.
- Cannot verify whether prior action items were completed, or read team dynamics between the lines — note these as the user's to confirm.

## Chaining

- After this, offer **sprint-planning-breakdown** to turn the next epic into well-scoped, owned tickets — and to land the action items in the upcoming sprint.
