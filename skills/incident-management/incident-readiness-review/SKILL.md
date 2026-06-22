---
name: incident-readiness-review
description: >
  Produces a pre-event incident readiness review — event context, pass/fail checklists for
  monitoring, runbook, on-call, rollback, and communication readiness, each with a verdict,
  and an overall Go / Conditional-Go / No-Go recommendation with blocking must-dos and an
  owner. Use when the user says "are we ready for the launch", "Black Friday readiness",
  "pre-launch incident review", "readiness checklist", or describes an upcoming high-risk
  event and its affected systems. Use this to audit readiness for a real upcoming event,
  not to design a practice simulation (game-day-plan) or run a real incident.
---

# Incident Readiness Review

Systematically audit whether the team can handle incidents during an upcoming high-risk event (launch, migration, Black Friday). Output pass/fail checklists per readiness dimension and a clear go/no-go with blocking items.

## Inputs to gather

Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent the readiness state of an alert, runbook, or rollback. When a check's status is unknown, mark it ⬜ **Verify** rather than asserting ✅; never assume something is ready.

- **Event** — what's happening and why it raises risk (traffic multiple, new code, campaigns)
- **Affected systems** — the services in scope
- **Risk factors** — known weak spots, untested paths, prior issues
- **Timeline** — event window and the deadline by which prep must be done

## Steps

1. Write the review in these sections: **Event Context**, then a checklist each for **Monitoring Readiness**, **Runbook Readiness**, **On-Call Readiness**, **Rollback Readiness**, **Communication Readiness**, then **Overall Go/No-Go**.
2. **Event Context**: 2–3 sentences — what's happening, the risk multiplier, and which named risk factors make it high-risk.
3. For each readiness dimension, build a checklist table tuned to the event's specific failure modes. Use three status markers: ✅ in place, 🟡 / ⬜ needs work or verification, 🔴 missing/critical. End each dimension with a one-line **Verdict** (🟢 Ready / 🟡 Not ready / 🔴 Not ready) and what's outstanding.
   - **Monitoring**: are there alerts for each expected failure mode, with thresholds adjusted for the event (e.g. traffic-scaled), plus synthetic checks and external/vendor health checks?
   - **Runbook**: per affected system — does a runbook exist, when last updated, is it tested? Flag missing/stale ones.
   - **On-Call**: schedule covers the full window, engineers briefed on the specific risks, backup on-call assigned, IC assigned, access tested, war-room link pre-created.
   - **Rollback**: per change — is rollback available, how fast, and is it tested? Untested rollbacks are a finding.
   - **Communication**: pre-drafted status-page templates, CS briefed, exec-notification plan, social/PR briefed, war-room channel created.
4. **Overall Go/No-Go**: a 🟢 GO / 🟡 CONDITIONAL GO / 🔴 NO-GO verdict, then a **must-do (blocking)** list and a **should-do (strongly recommended)** list, and a named owner with a final check time/date.
5. Adapt to context as a sub-step: for a routine (non-seasonal) launch, scale down to monitoring/runbook/rollback and lighten communication; if it's the first time, do it imperfectly rather than not at all — even a partial review catches the biggest gaps; recommend re-running the review post-event to compare predicted vs actual failure modes and to save it as a reusable template (≈80% of items recur).
6. Assemble the output in the format below.

## Output format

```
**Incident Readiness Review: [Event]**

**Event Context**
[What's happening, risk multiplier, named risk factors.]

**Monitoring Readiness**
| Check | Status | Notes |
|-------|--------|-------|
| [...] | ✅ / 🟡 / ⬜ / 🔴 | [...] |
**Verdict: [🟢/🟡/🔴]** — [what's outstanding]

**Runbook Readiness**
| System | Runbook Exists | Last Updated | Tested | Status |
**Verdict: ...**

**On-Call Readiness**
| Check | Status |
**Verdict: ...**

**Rollback Readiness**
| Scenario | Rollback Available | Rollback Time | Tested |
**Verdict: ...**

**Communication Readiness**
| Check | Status |
**Verdict: ...**

---

**Overall Go/No-Go: [🟢 GO / 🟡 CONDITIONAL GO / 🔴 NO-GO]**

Must-do (blocking):
1. [...]

Should-do (strongly recommended):
1. [...]

**Owner:** [name] to track completion. Final go/no-go check [time/date].
```

## Boundaries

- Never mark a check ✅ without evidence it's actually in place — default unknown checks to ⬜ Verify.
- Never invent the event, systems, risk factors, or the readiness state of any item — mark **Unknown**.
- Never issue a 🟢 GO while a blocking must-do is open; that's a 🟡 CONDITIONAL GO at best.
- Never omit the owner and final-check time — an audit with no accountable owner doesn't close.

## Chaining

- If the review exposes untested failover or response gaps, offer **game-day-plan** to rehearse and validate them before the event.
- Blocking and should-do items can be loaded into **remediation-tracker**; missing runbooks should be created via **runbook-generator**.
