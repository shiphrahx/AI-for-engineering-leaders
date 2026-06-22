---
name: incident-commander-runbook
description: >
  Produces a reusable Incident Commander (IC) runbook — first-5-minutes actions, triage,
  role assignment, communication cadence, decision framework, and post-incident handoff —
  usable by anyone on the rotation, including a first-time IC at 3am. Use when the user
  says "create an IC runbook", "incident commander playbook", "how should we run
  incidents", or pastes org/on-call/tooling context and asks for a coordination framework.
  Use this to build the standing playbook, not to define severity tiers
  (severity-classification-guide), not to facilitate a specific live war room
  (war-room-facilitation-guide), and not to write a postmortem afterward.
---

# Incident Commander Runbook

Produce a coordination playbook that lets anyone on the rotation run an incident calmly — keeping the big picture while others debug. The IC's job is to coordinate, communicate, and decide; it is never to fix the problem.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a SINGLE batched question — never invent team names, tools, services, or severity levels. Mark anything genuinely unavailable as **Unknown** in the output.

- **Team size** — headcount and team structure
- **On-call structure** — rotation shape (primary/secondary, separate IC rotation)
- **Communication tools** — e.g. Slack channels, PagerDuty, Statuspage, Zoom
- **Key services** — the systems most likely to be involved
- **Severity levels** — existing P0–P3 definitions, if classified

## Steps

1. Write the runbook in six sections, in this order: **First 5 Minutes**, **Triage**, **Coordination**, **Communication Cadence**, **Decision Framework**, **Post-Incident Handoff**.
2. **First 5 Minutes**: numbered immediate actions on being paged — acknowledge, post "IC online" to the incident channel, read alert context, check dashboards/status page, make a severity call within 5 minutes. Reinforce: over-classify and scale down beats under-classify and scramble.
3. **Triage**: a question→severity table and a response-level-per-severity list (war room, who to engage, status-page/exec timing) keyed to the org's severity levels.
4. **Coordination**: assign exactly three roles — IC (coordinate, do NOT debug), Tech Lead (diagnose/fix, narrate findings), Comms Lead (status page, customer/internal comms). Add war-room rules and an "if you're stuck" prompt list (what changed in last 2 hours, can we roll back, is there a workaround, who else has context).
5. **Communication Cadence**: an audience × channel × P0-frequency × P1-frequency table plus a copy-paste update template (time, status, impact, current action, next update).
6. **Decision Framework**: explicit criteria for when to roll back (default: roll back first, debug second), when to escalate (with the named escalation path), and when to declare resolved (metrics at baseline 15+ min, Tech Lead confirms, final update posted).
7. **Post-Incident Handoff** (within 1 hour): final summary, status page to resolved, create postmortem doc and assign author, schedule review within ~3 business days, thank everyone publicly, and explicitly permit deferring the postmortem if it's the middle of the night.
8. Adapt to context as a sub-step: small team (<15) — combine IC and Comms Lead; first-time IC — recommend printing the runbook; remote team — default to a Slack thread for P1s, reserve war-room calls for P0s; regulated industry (fintech/healthcare) — add a regulatory-notification step with required timeframes.
9. Assemble the output in the format below.

## Output format

```
**Incident Commander Runbook**

**First 5 Minutes — You've Been Paged**
[Numbered immediate actions]

**Triage — Severity Assessment**
| Question | If Yes → |
|----------|----------|
| [...] | [P0/P1/P2/P3] |

Response level by severity:
- P0: [war room, who, comms timing]
- P1 / P2 / P3: [...]

**Coordination — Running the Response**
| Role | Who | Responsibility |
|------|-----|----------------|
| IC (you) | [...] | Coordinate, communicate, decide. Do NOT debug. |
| Tech Lead | [...] | Diagnose and fix; narrate findings. |
| Comms Lead | [...] | Status page, customer/internal comms. |

War room rules: [...]
If you're stuck: [diagnostic prompt list]

**Communication Cadence**
| Audience | Channel | P0 Frequency | P1 Frequency |
|----------|---------|--------------|--------------|
| [...] | [...] | [...] | [...] |

Update template:
[Time / Status / Impact / Current action / Next update]

**Decision Framework**
When to roll back: [...]
When to escalate: [...]  Escalation path: [...]
When to declare resolved: [...]

**Post-Incident Handoff (within 1 hour of resolution)**
[Numbered steps]
```

## Boundaries

- Never write the IC into a debugging role — the IC coordinates and decides; if the IC debugs, no one is commanding.
- Never fabricate team member names, channel names, tools, services, or severity definitions — mark them **Unknown**.
- Never recommend declaring resolved before metrics have held at baseline and the Tech Lead has confirmed the fix.
- Never omit the escalation path — "who do I call next" must be answerable from the runbook.
- This builds the standing playbook; do not use it to make live calls on a specific incident in progress.

## Chaining

- This runbook references severity levels — if they don't exist yet, run **severity-classification-guide** first.
- When a real incident opens, offer **war-room-facilitation-guide** to facilitate the live call.
- After resolution, offer **planning/incident-postmortem** to capture learnings from the incident.
