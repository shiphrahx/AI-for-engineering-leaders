---
name: stakeholder-project-update
description: >
  Produces a jargon-free project status update for cross-functional stakeholders (PMs, designers,
  business leads) — status-at-a-glance with target date, visible progress they can verify, what's
  coming next, a "what we need from you" asks table with deadlines, and a planned-vs-actual
  timeline. Use when the user says "project update for stakeholders", "update for the PM/design
  lead", "where's the project at", or pastes progress notes plus blockers. Use this for the
  cross-functional, business-audience project update — use cross-team-dependency-update when the
  audience is other engineering teams you depend on, and exec-status-update for leadership-up org status.
---

# Stakeholder Project Update

Update cross-functional stakeholders who don't speak engineering fluently on a project they care about — translating everything into business and user impact, and making crystal clear whether it's on track, what they can see, and what they need to do.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent progress, dates, blockers, or stakeholder names. Mark anything genuinely unavailable as **Unknown** in the output.

- **Project** — name
- **Target launch** — the launch/target date
- **Stakeholders** — names and roles
- **Last update** — date of the previous update (for "what's new since")
- **Progress since last update** — visible progress, demos, staging links, metrics
- **Blockers/dependencies on stakeholders** — what's stuck and who can unblock it

## Steps

1. Read progress notes and blockers fully. Translate every technical item into what a non-engineer can see, test, or care about — strip jargon.
2. Set **status at a glance**: one line, 🟢 On Track / 🟡 At Risk / 🔴 Off Track, with the target date. If at risk or off track, state how many days and why.
3. **What's new since last update** — visible progress they can verify: demos, staging links, early metrics. Anchor to what they can check themselves.
4. **What's coming next** — what will be true by the next update.
5. **What we need from you** — a table of specific asks, each with a named owner and a hard deadline, and the consequence of slipping (e.g. "engineering needs 5 days to implement"). Make the launch-impact of each ask explicit.
6. **Timeline view** — a milestone table showing planned vs. actual/revised and status.
7. Adapt to context: if **everything is on track**, drop the "what we need" urgency and replace with a "feedback welcome on" section — stakeholders love ahead-of-schedule updates. If the **project is off track**, lead with the revised date and explain what changed; never bury a date change mid-update. For **multiple workstreams**, replace the single narrative with a workstream-by-workstream grid. For an **executive audience**, cut the timeline table and replace with one line: "On track for [DATE] assuming [KEY_DEPENDENCY] lands by [DATE]".
8. Assemble the output in the format below.

## Output format

```
**[Project] — Update ([Date])**

**Status: 🟢/🟡/🔴 [On Track / At Risk / Off Track]** — target launch [date][, currently tracking N days behind because …].

**What's New**
- [Visible progress, with staging link / metric they can verify]

**Coming Next (by [date])**
- [What will be true by the next update]

**What We Need From You**
| Who | What | By When |
|-----|------|---------|
| [Name (role)] | [specific ask] | **[date]** — [why / launch impact] |

*[One line on how these dates map to the launch date.]*

**Timeline**
| Milestone | Planned | Actual/Revised | Status |
|-----------|---------|----------------|--------|
| [milestone] | [date] | [date] | ✅/🔄/⏳/⬜ |
```

## Boundaries

- Never fabricate progress, staging links, metrics, dates, blockers, or stakeholder names — mark anything unavailable as **Unknown**.
- Never use engineering jargon — translate to business/user impact or cut it.
- Never bury a slipped or revised launch date; lead with it.
- Never assign an ask to a stakeholder without a date and a stated consequence of missing it.
- Never present a workaround's cost (latency, rework) as invisible — name it so stakeholders can weigh it.

## Chaining

- After this, offer **cross-team-dependency-update** when the project's risks trace to other engineering teams' deliverables and those teams need a direct, collaborative ask.
