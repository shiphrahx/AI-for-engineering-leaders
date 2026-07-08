---
name: incident-code-triage
description: >
  Reads the failing code path during a live incident and produces a fast, ranked set of
  hypotheses with the cheapest check for each and the safest next action — so a leader can direct
  the response or dig in without thrashing. Optimised for speed and honesty under pressure, not
  completeness. Use when the user says "help me debug this incident", "what's causing this
  outage", "read this stack trace / error / code path", or is triaging a production failure in
  real time. Use this to form a hypothesis mid-incident — use incident-stakeholder-comms to
  update people during it, and incident-postmortem to analyse root cause after it's resolved.
---

# Incident Code Triage

Read the failing code path fast and hand back ranked hypotheses, the cheapest way to confirm or kill each, and the safest next move — so the response is directed, not flailing. Under pressure the discipline is honesty: rank by likelihood, mark what you're guessing, and never propose a risky action without saying it's risky.

## Inputs to gather

Gather what's available fast — in an incident you act on partial information. Ask only for what's cheap and decisive; never block triage waiting for perfect data. Mark what you don't have as **Unknown** and factor it into confidence.

- **Symptom** — what's observably wrong (errors, latency, wrong output, down) and the blast radius
- **Signal** — stack traces, error messages, logs, metrics, alerts (paste the actual text, exact)
- **Change** — what deployed or changed recently (most incidents follow a change) and when the symptom started
- **The code** — the suspected path/service if known (agent can read it)
- **Constraints** — what actions are safe right now (can we roll back? is data at risk? peak traffic?)

## Steps

Numbered, imperative, specific enough that the agent cannot skip a step.

1. Pin the **symptom and timeline** in one line: what's wrong, how big, since when. Correlate the start time with any recent deploy/config change — a change just before the symptom is the first suspect.
2. Read the **signal literally** — parse the actual stack trace/error/log, don't pattern-match to a guess. Trace it to the specific code location if the code is available; quote the line.
3. Form **ranked hypotheses** (most to least likely) with a confidence tag. Base rank on evidence and recent change, not on what's most interesting. Include the boring likely cause (bad deploy, config, dependency, resource limit) before the exotic one.
4. For each hypothesis give the **cheapest check** that confirms or kills it — a log query, a metric, a one-line test, a rollback probe — fastest and least risky first. Triage is about ordering cheap discriminating checks.
5. Recommend the **safest next action**: usually stop-the-bleeding (roll back, disable flag, failover) over root-causing live, especially if data is at risk. State explicitly if an action is risky or irreversible and get a human to confirm before proposing it as automatic.
6. Flag **data-integrity or security** exposure prominently if the failure could corrupt data or leak — that changes priority immediately.
7. Say what you **can't tell yet** and what signal would resolve it, so the responder knows where the uncertainty is.
8. Keep it short and scannable — an incident is not the place for prose. Assemble the output in the format below.

## Output format

```
**Incident Triage: [symptom]** — Blast radius: [scope] — Since: [time]

**Recent change:** [Deploy/config just before onset, or "none known".]

**Ranked hypotheses**
1. [Most likely] — confidence [H/M/L]. Check: [cheapest confirm/kill]. (`path:line` if known)
2. [Next] — confidence [..]. Check: [..]
3. [..]

**Safest next action:** [Stop-the-bleeding step. ⚠️ flag if risky/irreversible — confirm with a human.]

**Data/security exposure:** [Any corruption/leak risk, or "none identified".]

**Can't tell yet:** [Open unknown + the signal that would resolve it.]
```

## Boundaries

What the skill must never do.

- Never present a guess as a confirmed cause — rank by likelihood and tag confidence; say what's inferred.
- Never propose a risky or irreversible action (data deletion, forced failover, schema change) as automatic — flag it and require human confirmation.
- Never invent log lines, metrics, or stack frames — work only from what's provided; mark gaps **Unknown**.
- Never chase the exotic cause before ruling out the boring likely one (bad deploy, config, resource limit).
- Never bury a data-integrity or security exposure — surface it first, it reprioritises everything.
- Never let the writeup slow the response — brevity is the point mid-incident.

## Chaining

If there is a natural next skill after this one, name it and offer it at the end.

- During the incident, offer **incident-stakeholder-comms** to keep stakeholders updated while triage continues.
- After resolution, offer **incident-postmortem** to turn the timeline and root cause into a blameless writeup with action items.
