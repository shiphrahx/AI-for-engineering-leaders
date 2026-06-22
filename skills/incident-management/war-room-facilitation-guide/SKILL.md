---
name: war-room-facilitation-guide
description: >
  Produces a war-room facilitation guide for a live incident — room setup, a verbatim
  first-5-minutes opening script, the check-in cadence for running parallel workstreams,
  decision templates (roll back / escalate / risky fix), facilitator anti-patterns, and a
  closing script. Use when the user says "I'm facilitating a war room", "running a P0
  call", "how do I keep the war room focused", or pastes live incident context (severity,
  service, who's on the call, what's known). Use this for facilitating one specific live
  call, not for the standing IC playbook (incident-commander-runbook) or severity
  definitions (severity-classification-guide).
---

# War Room Facilitation Guide

Give the IC a script and structure to facilitate a live war room — keep the right people on the right things, keep information flowing, and drive to resolution without micromanaging the debugging. The IC coordinates; the IC does not debug.

## Inputs to gather

Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent the severity, the service, who's present, or what's known. Mark unavailable fields as **Unknown** and use **[bracketed placeholders]** for names/roles to fill in live.

- **Severity** — the assigned level (P0–P3)
- **Service affected** — what's degraded and the customer-facing symptom
- **People in the room** — roles present (engineers, SRE, EM, VP, CS)
- **What's known so far** — current status, error signatures, recent changes, what's ruled out

## Steps

1. Write the guide in six sections: **Room Setup**, **First 5 Minutes (opening script)**, **Running the Room**, **Decision Templates**, **Anti-Patterns**, **Closing the Room**.
2. **Room Setup**: where the call lives (Zoom/Slack), the posted join message, mute-on-entry with IC controlling the floor, the shared screen (relevant dashboard), and a Slack thread for async notes/links (not discussion — discussion happens on the call).
3. **First 5 Minutes**: a verbatim opening script the IC can read aloud when nervous. It states what's known, then assigns roles by name — Tech Lead (diagnose/fix, narrate), supporting engineers (directed by Tech Lead, check before running prod commands), Comms Lead (status updates on a stated cadence), observers (escalation targets only) — and sets the rule that nobody runs prod commands without the Tech Lead's sign-off.
4. **Running the Room**: the IC's repeating round (every ~10 min) — status check from Tech Lead (tried / learned / trying next), update the thread, hand Comms Lead the update, ask "does anyone have info the Tech Lead doesn't?". Include how to split parallel workstreams without overlap and how to triage a proposed fix (what's the fix, the risk, the rollback).
5. **Decision Templates**: pre-built scripts for the three recurring calls — *should we roll back* (recent change + safe rollback → roll back first, debug second), *should we escalate* (no progress in 30 min, scope expanding, data/security implications), and *should we try a risky fix* (state the fix, the success case, the failure case, the rollback, then approve and assign).
6. **Anti-Patterns**: the things the IC must not do — debug alongside the Tech Lead, let everyone talk at once, ignore observers' questions (defer to the next update), go silent for 15+ minutes (post "no change, next update in 10" anyway), or let the room grow unchecked.
7. **Closing the Room**: the close criteria (metrics at baseline 15+ min, Tech Lead confirms fix is holding, no new errors) and a verbatim closing script declaring resolution with duration, naming the postmortem owner and review date, and thanking the room. End with the final #incidents post.
8. Adapt to context as a sub-step: if the IC is also the only person who knows the system, they may have to debug and facilitate — narrate aloud and delegate comms; if the room is overcrowded, use the script to release non-essential people; if a senior leader tries to take over, redirect authority calmly back to the Tech Lead's assessment; recommend rehearsing via a tabletop exercise so it's muscle memory.
9. Assemble the output in the format below.

## Output format

```
**War Room Facilitation — [Service] [Severity]**

**Room Setup**
- [Call location + posted join message]
- Mute on entry; IC controls the floor
- Shared screen: [dashboard]
- Slack thread: [#incident-thread] for async notes/links (not discussion)

**First 5 Minutes — Opening Script**
"[Verbatim script: what's known → role assignments by name → prod-command rule → 'Let's go.']"

**Running the Room**
Every ~10 min, IC does a round:
1. "[Tech Lead], what have you tried / learned / trying next?"
2. Update the thread.
3. Hand Comms Lead the customer-facing update.
4. "Does anyone have info the Tech Lead doesn't?"
Parallel workstreams: [how to split without overlap]
Proposed fix: "What's the fix? The risk? The rollback?"

**Decision Templates**
Roll back: [criteria + IC script]
Escalate: [criteria + IC script]
Risky fix: [criteria + IC script]

**Anti-Patterns — Do NOT**
- ❌ Debug alongside the Tech Lead
- ❌ Let everyone talk at once
- ❌ Ignore observers' questions
- ❌ Go silent for 15+ minutes
- ❌ Let the room grow unchecked

**Closing the Room**
Close when: [criteria]
Closing script: "[Verbatim: resolution + duration + postmortem owner + review date + thanks.]"
Post to #incidents: [final summary]
```

## Boundaries

- Never put the IC in a debugging seat unless they're the sole expert — and then require narration plus delegated comms.
- Never fabricate names, the service, the severity, or what's known — use **[placeholders]** and **Unknown**.
- Never close the room before metrics have held at baseline and the Tech Lead confirms the fix.
- Never approve a fix in the templates without stating its rollback.
- This facilitates one live call — do not use it to author the standing playbook.

## Chaining

- After the incident resolves, offer **planning/incident-postmortem** to capture the timeline and root cause while it's fresh.
- For the standing coordination playbook this draws on, see **incident-commander-runbook**.
