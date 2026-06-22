---
name: team-weekly-summary
description: >
  Produces a Friday wrap-up for an engineering manager's own team — what shipped (with
  individual credit), what's carrying over (with adjusted ETAs), specific shoutouts, next-week
  priorities with owners, and a heads-up section. Warm-but-direct tone, technical detail welcome.
  Use when the user says "write my team's weekly summary", "Friday wrap-up", "end-of-week update
  for my engineers", or pastes the week's notes. Use this for the team-internal, downward update —
  use exec-status-update for the leadership-up version and engineering-newsletter for the
  company-wide non-technical version.
---

# Team Weekly Summary

Write a Friday wrap-up for your own engineers that acknowledges what shipped, is honest about what didn't, and sets clear expectations for next week — warm but direct, with technical detail your team can actually use.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent shipped work, names, ETAs, or credit. Mark anything genuinely unavailable as **Unknown** in the output.

- **Team** — name and size
- **Sprint/cycle** — which sprint and where in it (e.g. week 1 of 2)
- **Planned goals** — this week's original goals
- **What actually happened** — the week's notes, including unplanned work, who did what, and current state of each item

## Steps

1. Read the week's notes fully. Map each item to: shipped, carrying over, or unplanned-but-done.
2. Open with one warm, honest line setting the week's overall tone.
3. **What shipped** — specific PRs, features, or milestones, with credit to the individuals who did them. Include unplanned wins (e.g. an incident handled well).
4. **Carrying over** — unfinished work with brief context on *why* and an adjusted ETA. Be honest about blockers; don't paper over slips.
5. **Shoutouts** — call out specific people for going above and beyond, naming the specific thing they did (not generic praise).
6. **Next week priorities** — a numbered list with an explicit owner per item.
7. **Heads up** — on-call rotation, planned maintenance, holidays, all-hands, visitors, anything that changes the week's rhythm.
8. Adapt to context: for **remote/async teams**, add timezone context and async check-in expectations. **After a rough week**, lean honestly into "carrying over" but always find at least one genuine shoutout — effort must be seen even when outcomes slip. For **large teams (10+)**, group by workstream rather than listing every item, and keep shoutouts to 3-4 to avoid dilution. For a **new manager**, err toward more detail in next-week priorities — explicit ownership and ETAs build trust early.
9. Assemble the output in the format below.

## Output format

```
**[Team] — Week [N] Wrap-up**

[One warm, honest line on how the week went.]

**What Shipped**
- [Specific item + individual credit]

**Carrying Over**
- [Item: why unfinished, adjusted ETA]

**Shoutouts**
- [Name] for [specific thing they did]

**Next Week Priorities**
1. [Priority] — [owner]
2. [...]

**Heads Up**
- [On-call / maintenance / holidays / all-hands / visitors]
```

## Boundaries

- Never fabricate shipped work, names, credit, ETAs, or blockers — mark anything unavailable as **Unknown**.
- Never give a shoutout to someone for something they didn't do, or omit a real contributor — credit must be accurate.
- Never spin a slipped item as on-track; the team will know, and trust erodes.
- Never invent an ETA for blocked work — state the blocker and that the ETA depends on it.

## Chaining

- After this, offer **exec-status-update** to roll this team's week up into a leadership-facing update.
- For a company-wide, non-technical version, offer **engineering-newsletter**.
