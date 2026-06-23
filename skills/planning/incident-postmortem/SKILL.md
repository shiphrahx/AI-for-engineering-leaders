---
name: incident-postmortem
description: >
  Produces a blameless, structured incident postmortem with root-cause analysis,
  contributing factors, and prioritized action items. Use when the user says "write
  a postmortem", "post-incident review", "RCA", or pastes an incident timeline,
  Slack logs, or impact data after an incident is resolved. Use this for internal,
  learning-focused documentation — not for real-time incident comms (incident-commander-runbook)
  or customer-facing explanations (a status update or apology email).
---

# Incident Postmortem

Turn the raw record of an incident into a document the organization can learn from — blameless throughout, focused on systemic causes rather than individual error.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent a timeline, a metric, or a cause. Mark anything genuinely unavailable as **Unknown** in the output.

- **What happened** — a short description of the incident
- **Timeline** — timestamped events, actions taken, and who/what triggered each
- **Impact** — duration, users/customers affected, revenue or data implications
- **Communication logs** — Slack/war-room messages, if available
- **Severity** — the assigned level (P0–P3), if classified

## Steps

1. Read the full timeline and impact data before writing a word. Reconstruct the sequence; flag gaps as **Unknown** rather than filling them.
2. Write a one-paragraph summary: what happened, the root cause, and how it was resolved.
3. Identify the **root cause** as a systemic issue (a process, tool, or architecture gap), never as a person's mistake. For every human action that contributed, ask "what about the system made this easy to do?" and record that instead.
4. List **contributing factors** — the conditions that made the incident possible or worse.
5. Note **what went well** (effective response, not individual heroics) and **what could be improved** (process or response gaps).
6. Derive **action items** that prevent recurrence. Make each one specific, owned, and prioritized (P0/P1/P2). Mark owner/date **Unknown** if not provided rather than assigning someone.
7. Adapt to context: for a customer-facing version, cut internal detail to what-happened / impact / what-we-did / prevention. For a recurring incident type, add a "History" section of similar past incidents. For a P3, scale down to summary, root cause, and action items only. For regulated industries, add a compliance-notification section.
8. Assemble the output in the format below.
9. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**Postmortem: [Brief Title] ([Date])**

**Summary**
[One paragraph: what happened, root cause, resolution]

**Impact**
- Duration: [time]
- Users/customers affected: [scope]
- Business impact: [or Unknown]
- Data implications: [or None/Unknown]

**Timeline**
| Time | Event |
|------|-------|
| [timestamp] | [what happened] |

**Root Cause**
[Systemic issue, not individual blame. 1–2 paragraphs.]

**Contributing Factors**
- [Factor — why it mattered]

**What Went Well**
- [Effective aspect of the response]

**What Could Be Improved**
- [Gap in process or response]

**Action Items**
| Priority | Action | Owner | Due |
|----------|--------|-------|-----|
| P0 | [must do] | [team/person or Unknown] | [timeframe or Unknown] |
| P1 | [should do] | [...] | [...] |
| P2 | [nice to have] | [...] | [...] |

**Lessons Learned**
- [Broader organizational takeaway]
```

## Boundaries

- Never name an individual as the cause. Every human error has a systemic enabler — find and state that instead.
- Never fabricate timeline entries, metrics, owners, or dates. Mark unknowns as **Unknown**.
- Never soften or inflate severity or impact to make the response look better or worse than it was.
- Never turn the document into a punishment record — its only purpose is preventing recurrence.

## Chaining

- After this, offer **remediation-tracker** to track the action items through to completion.
- For systemic patterns across many incidents, offer **incident-trend-analysis**.
