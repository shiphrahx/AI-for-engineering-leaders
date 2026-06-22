---
name: cross-team-dependency-update
description: >
  Produces a collaborative, blame-free dependency status update shared across engineering teams —
  a dependency-map summary, "on track" vs. "needs attention" (with impact-if-delayed and a
  proposed path forward), and a per-team asks table with dates. Use when the user says "dependency
  update", "we're blocked on another team", "cross-team status", or pastes notes about handoffs
  and what teams owe each other. Use this when the audience is other engineering teams you depend
  on (or that depend on you) — use stakeholder-project-update for business/PM/design audiences and
  exec-status-update for leadership-up org status.
---

# Cross-Team Dependency Update

Surface cross-team blockers and handoff status in a way that is collaborative and solution-oriented — never blame, always a path forward — so every team knows what it needs to know and do.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent dependencies, dates, or team commitments. Mark anything genuinely unavailable as **Unknown** in the output.

- **My team** — the team sending the update
- **Dependent teams** — the other teams involved (depended-on or depending)
- **Project/initiative** — name
- **Key dates** — beta, launch, or hard deadlines the dependencies feed
- **Dependency status notes** — what's needed from whom, current state, any workarounds and their cost

## Steps

1. Read the dependency notes fully. For each dependency, identify the direction (who needs what from whom), its state, the impact if it slips, and any workaround already in hand.
2. Open with one line framing the sync against the key date.
3. **Dependency map summary** — one line per dependency in "Team A ← Team B: [thing]" form.
4. **On track** — dependencies that are healthy, briefly.
5. **Needs attention** — for each at-risk dependency: the specific impact if delayed (quantified where possible — latency, rework, missed beta), and a *proposed path forward* (a check-in, a decision point, a plan-for-the-workaround date). Frame as a shared problem, never as the other team's fault.
6. **Asks** — a table with exactly one clear action per team and a date.
7. Close with a low-friction offer to sync, reinforcing "no surprises, just keeping us aligned."
8. Adapt to context: if **escalation is needed** (the update has gone out twice with no movement), CC your skip-level and the other team's manager — keep the same collaborative language; the CC is the escalation, not harsher words. If **your team is the blocker**, use the same format but lead with your own status and what you're doing to unblock others. For a **Slack-native culture**, shorten to a table (Dependency | Status | Ask | Date), post in a shared channel, and @ the relevant leads. For a **large org**, add a RACI-style column naming the decision-maker when timelines can't be met.
9. Assemble the output in the format below.

## Output format

```
**[Project] — Dependency Check-in ([Date])**

[One line framing the sync against the key date.]

**Dependency Map**
- [My Team] ← [Other Team]: [what's needed]

**On Track**
- ✅ [Dependency]: [brief healthy status]

**Needs Attention**
- 🟡 **[Team — dependency]:** [impact if delayed, quantified]. *Proposed path:* [check-in / decision point / workaround plan].

**Asks**
| Team | Action | By When |
|------|--------|---------|
| [team] | [one clear action] | [date] |

[Low-friction offer to sync — collaborative close.]
```

## Boundaries

- Never fabricate dependencies, dates, team commitments, or impact figures — mark anything unavailable as **Unknown**.
- Never assign blame or use accusatory framing — every at-risk item gets a proposed path forward, not a finger pointed.
- Never list a needs-attention item without stating the concrete impact if it slips.
- Never escalate by changing the tone — escalation is a CC, not harsher language.
- Never hide a workaround's cost (latency, rework) — name it so teams can decide knowingly.

## Chaining

- No natural successor — this is usually a terminal artifact. It is often triggered by risks first surfaced in a **stakeholder-project-update**.
