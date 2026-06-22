---
name: game-day-plan
description: >
  Produces a game day (incident-response simulation / chaos exercise) plan — objective,
  the simulated scenario and safe injection method, rules of engagement and blast-radius
  limits, participant roles, a T-minus/T-plus timeline, measurable evaluation criteria,
  and a debrief plan. Use when the user says "plan a game day", "chaos engineering
  exercise", "incident simulation", "fire drill for on-call", or describes systems and
  suspected weaknesses they want to stress-test. Use this to design a controlled
  practice exercise, not to audit readiness for a real upcoming event
  (incident-readiness-review) or to facilitate a real live incident.
---

# Game Day Plan

Design an incident-response simulation realistic enough to surface real gaps in runbooks, monitoring, and coordination — but controlled enough to cause no actual customer impact.

## Inputs to gather

Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent team composition, systems, or injection methods. Mark unavailable fields as **Unknown** and use **[bracketed placeholders]** for assignees.

- **Team** — name, size, and roles available
- **Systems to test** — the services in scope
- **Last game day** — when, or never (drives complexity)
- **Known/suspected gaps** — weaknesses you want the exercise to expose (untested failover, stale runbooks, inexperienced ICs)

## Steps

1. Write the plan in seven sections: **Objective**, **Scenario**, **Rules of Engagement**, **Roles**, **Timeline**, **Evaluation Criteria**, **Debrief Plan**.
2. **Objective**: what you're testing and the specific questions to answer (does monitoring detect it before customers do? can on-call follow the runbook? does the app recover? how long does the cycle take?).
3. **Scenario**: the simulated failure and a **safe injection method** that mimics a real failure without breaking anything for real — prefer network-level or controlled simulation over destructive action (e.g. block the DB security-group port rather than killing the database). Then list the **expected cascade** step by step.
4. **Rules of Engagement**: explicit safety boundaries — low-traffic window, the Controller can abort anytime by reverting the injection, who knows it's a drill, CS informed in advance, no production data changes, abort immediately if a real incident occurs, and a hard maximum exercise duration.
5. **Roles**: a table — Game Day Controller (triggers, monitors safety, can abort), On-Call (responds as if real), IC (runs response, practicing), Observers (watch and note where the process breaks, don't help unless asked), Safety Monitor (watches real customer metrics, calls abort if real impact exceeds thresholds).
6. **Timeline**: a T-minus / T-plus table from pre-brief through injection, expected detection/ack/diagnosis/resolution milestones, a mid-point hint checkpoint, the hard stop, and debrief start.
7. **Evaluation Criteria**: a measurable table — time to detection, time to acknowledgement, time to diagnosis, time to resolution, runbook accuracy (could on-call follow it?), monitoring coverage (did the right alerts fire?), communication (were stakeholders updated on cadence?), and any unexpected side effects — each with a target and a blank "actual" column.
8. **Debrief Plan**: round-robin participant experiences, review the criteria results, identify the top 3 gaps, create owned action items with deadlines, pick the next scenario, and share the writeup with the broader org.
9. Adapt to context as a sub-step: for a **first** game day keep it simple — one failure mode, business hours, everyone knows it's a drill; for an **experienced** team make it harder — don't announce the scenario, inject a second failure midway, add a "customer escalation" role; if production simulation is uncomfortable, run against staging with realistic load; recommend quarterly cadence so response becomes muscle memory.
10. Assemble the output in the format below.

## Output format

```
**Game Day Plan: [Scenario Name]**

**Objective**
[What's tested + specific questions to answer]

**Scenario**
[The simulated failure]
*Injection method:* [safe, reversible method that mimics real failure]
*Expected cascade:* [numbered steps]

**Rules of Engagement**
- ✅ [Low-traffic window; abort mechanism; who knows; CS informed]
- ❌ [No prod data changes; abort on real incident; max duration]

**Roles**
| Role | Person | Responsibility |
|------|--------|----------------|
| Game Day Controller | [...] | Triggers, monitors safety, can abort |
| On-Call (participant) | [...] | Responds as if real |
| IC (participant) | [...] | Runs response |
| Observers | [...] | Watch, note breakdowns |
| Safety Monitor | [...] | Watches real metrics, calls abort |

**Timeline**
| Time | Event |
|------|-------|
| T-30min | Pre-brief |
| T-0 | Injection |
| T+Nmin | [expected milestones] |
| T+[max] | Hard stop / abort |
| T+[...] | Debrief begins |

**Evaluation Criteria**
| What We're Measuring | Target | Actual |
|----------------------|--------|--------|
| Time to detection | [...] | |
| ... | ... | |

**Debrief Plan**
[Round-robin → review criteria → top 3 gaps → owned action items → next scenario → share writeup]
```

## Boundaries

- Never propose an injection method that risks real customer data or that can't be instantly reverted by the Controller.
- Never omit the abort conditions, the hard time limit, or the Safety Monitor role — safety boundaries are mandatory.
- Never invent team members, systems, or thresholds — use **[placeholders]** and mark **Unknown**.
- Never run a surprise (unannounced) exercise for a first-time team; surprise is an experienced-team variant only.

## Chaining

- After running the exercise, offer **incident-readiness-review** to audit whether the gaps it found are closed before a real high-risk event.
- The gaps found here often become entries for **remediation-tracker**.
