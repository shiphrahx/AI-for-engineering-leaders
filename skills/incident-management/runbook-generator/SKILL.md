---
name: runbook-generator
description: >
  Produces a step-by-step operational runbook for a single service — service overview,
  trigger alerts, prerequisites, diagnostic steps with expected outputs, per-scenario
  resolution with copy-pasteable commands, verification, escalation, and appendix —
  followable by an on-call engineer at 3am with no prior context. Use when the user says
  "write a runbook", "turn tribal knowledge into a runbook", "document how to fix X", or
  pastes notes from the person who knows a service. Use this for a single service's
  operational fix procedure, not for the cross-incident IC coordination playbook
  (incident-commander-runbook). Requires real operational knowledge as input — it
  structures expertise, it cannot invent commands or thresholds.
---

# Runbook Generator

Turn tribal knowledge into a runbook any on-call engineer can follow at 3am without prior context. Every step is explicit — no "you'll know what to do," no "use your judgment." Exact commands, expected outputs, decision trees.

## Inputs to gather

This skill structures an expert's knowledge; it cannot generate operational detail without it. Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent commands, thresholds, ARNs, hostnames, or escalation names. Mark unavailable fields as **Unknown** and leave **[bracketed placeholders]** for values the expert must supply.

- **Service name** and **what it does** — in two sentences, for someone who's never seen it
- **Common failure modes** — what typically goes wrong (e.g. queue backlog, rate limiting, connection exhaustion, crashes)
- **Environment details** — cloud/platform, queues, databases, monitoring tools, dashboards
- **Knowledge holder** — who runs this today (becomes the primary escalation)
- **Access/tools** — what permissions and consoles are needed to operate it

## Steps

1. Write the runbook with these sections in order: **Service Overview**, **When to Use This Runbook**, **Prerequisites**, **Diagnostic step (Assess the Situation)**, per-scenario **Resolution steps**, **Verification**, **Escalation**, **Appendix**.
2. **Service Overview**: two plain sentences — what it does and what breaks for customers if it stops.
3. **When to Use**: list the exact triggering alerts (with the alerting tool) and the customer-reported symptoms that map here.
4. **Prerequisites**: concrete access, consoles, and credential locations (e.g. 1Password vault name) needed before starting.
5. **Diagnostic step**: a metrics table with **Healthy** vs **Investigate** thresholds, ending with "based on what you see, go to the relevant scenario below."
6. For each common failure mode, write a **Scenario** with a likely-cause line and numbered steps. Each step that runs a command includes the **exact command in a code block** and the expected output or effect. Use copy-pasteable real commands — never pseudocode.
7. Flag any destructive command with a ⚠️ warning and state the safe alternative. Never default to a whole-fleet/whole-queue destructive operation (e.g. prefer deleting one confirmed poison message over purging a queue); spell out the data-loss risk.
8. **Verification**: a checklist confirming the fix held (metric recovering, no restarts, a positive test action like sending a test request).
9. **Escalation**: the conditions to stop following the runbook (tried the scenario and it failed, something not covered, >30 min without improvement, any sign of data loss) and the ordered page list (knowledge holder → secondary → manager).
10. **Appendix**: dashboard, console, log, and architecture-diagram links as placeholders.
11. Recommend keeping it alive: add a "Last verified" date at the top, re-test quarterly, and have someone who's never touched the service follow it step-by-step — every point of confusion is a fix. Note that each service gets its own runbook (not a mega-runbook), linked where services interact.
12. Assemble the output in the format below.

## Output format

```
**Runbook: [Service Name]**   (Last verified: [date])

**Service Overview**
[2 sentences: what it does, what breaks for customers if it stops]

**When to Use This Runbook**
- Alert: "[alert name]" ([tool])
- Symptom: [customer-reported symptom]

**Prerequisites**
- [Access / console / credential location]

---

**Step 1: Assess the Situation**
Dashboard: [link]
| Metric | Healthy | Investigate |
|--------|---------|-------------|
| [...] | [...] | [...] |
Based on what you see, go to the relevant scenario.

---

**Scenario A: [Failure Mode]**
*Likely cause:* [...]
1. [Step]
   \`\`\`
   [exact command]
   \`\`\`
   Expected: [output / effect]
2. [...]   ⚠️ [destructive-command warning + safe alternative, if any]

**Scenario B: [Failure Mode]**
...

---

**Verification**
- [ ] [metric recovering]
- [ ] [no restarts in last N minutes]
- [ ] [positive test action]

**Escalation**
Stop and page if: [conditions, incl. >30 min no improvement, any data-loss signal]
Page: [knowledge holder] → [secondary] → [manager]

**Appendix**
- Dashboard / Logs / Console / Architecture diagram: [links]
```

## Boundaries

- Never invent commands, metric thresholds, ARNs, queue names, hostnames, or escalation names — leave **[bracketed placeholders]** and mark **Unknown**. Quality depends entirely on input quality.
- Never present a destructive command without a ⚠️ warning and the data-loss consequence; never default to a fleet-wide or queue-wide destructive operation.
- Never write a step that requires judgment the runbook doesn't supply ("restart the service" must become the exact restart command).
- Never claim a command is tested — the user validates in staging.

## Chaining

- No natural successor — a runbook is usually a terminal operational artifact. (Pair it with **on-call-handoff**, which links to runbooks, and **incident-readiness-review**, which audits whether runbooks are current.)
