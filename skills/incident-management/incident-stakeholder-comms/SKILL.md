---
name: incident-stakeholder-comms
description: >
  Produces a short, plain-language incident update for executives and non-technical stakeholders
  — what happened, who is affected, current status, and the committed time for the next update.
  Use when the user says "draft a stakeholder update", "write the exec comms for this incident",
  or pastes incident facts mid-incident. Use this for the audience-facing status note — use
  incident-postmortem for the after-the-fact analysis and remediation-tracker for the action list.
---

# Incident Stakeholder Comms

Write a calm, jargon-free incident update for an executive or non-technical audience. The goal is to convey impact and control, not technical detail — and to always commit to a specific next-update time.

## Inputs to gather

Gather these before writing. If any are missing, ask in a single batched question — never invent impact figures, causes, or timelines. Mark anything genuinely unavailable as **Unknown**.

- **What happened** — in plain terms, no internal jargon
- **Who is affected** — which customers, regions, or services, and roughly how many
- **Current status** — what the team is doing right now
- **Next update** — the specific time you will send the next update

## Steps

1. Lead with **what happened** in one or two plain sentences — no stack traces, no internal component names.
2. State **who is affected** and the scale, concretely — "checkout is down for EU customers", not "elevated error rates".
3. Describe **current status** — what is being done and whether the situation is contained, without speculating on cause.
4. Commit to a **next update** time explicitly — a clock time or a "within N minutes" window. Never leave it open-ended.
5. Keep the whole note under 150 words and free of technical jargon — translate any engineering term into business impact.
6. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Incident Update — [System/Service] — [Time]**

**What happened:** [Plain-language summary.]

**Who is affected:** [Customers/regions/services and rough scale.]

**Current status:** [What the team is doing; contained or ongoing.]

**Next update:** [Specific time or window.]
```

## Boundaries

- Never use technical jargon (race condition, deadlock, null pointer, stack trace) for this audience — translate to business impact.
- Never speculate on root cause mid-incident — that belongs in the postmortem.
- Never invent affected-customer counts or impact figures — mark unknowns as **Unknown**.
- Always commit to a specific next-update time, even if the answer will be "still investigating".

## Chaining

- After the incident resolves, offer **incident-postmortem** for the analysis and **remediation-tracker** for the follow-up actions.
