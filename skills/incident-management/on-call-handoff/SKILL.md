---
name: on-call-handoff
description: >
  Produces an on-call handoff note for the incoming engineer — rotation summary, active
  issues that might page, recent changes (last ~7 days), things to watch that haven't yet
  alerted, useful context, and escalation contacts — readable in 5 minutes so the next
  person knows what's fragile and who to call. Use when the user says "write my on-call
  handoff", "end-of-rotation note", "shift handover", or pastes their rotation's incidents
  and changes. Use this for the rotation-boundary handover, not for live incident
  coordination (incident-commander-runbook) or a post-incident postmortem.
---

# On-Call Handoff

Hand the incoming on-call exactly what they need to not be blindsided: what's fragile, what might page them, and who to call. The goal is that they read it in five minutes and skip the first hour of figuring out "what's going on?"

## Inputs to gather

Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent incidents, deploys, metrics, or contacts. Mark unavailable fields as **Unknown**.

- **Rotation dates** — the outgoing window and the incoming window
- **Incidents during rotation** — what fired, severity, resolution, root cause, customer impact
- **Recent changes** — deploys, config changes, infra work in the last ~7 days, with rollback plans
- **Known issues** — anything unresolved or trending that might page the next person
- **Contacts** — per-service escalation owners, including who's on leave and their backup

## Steps

1. Write the note in six sections: **Rotation Summary**, **Active Issues**, **Recent Changes**, **Things to Watch**, **Useful Context**, **Escalation Contacts**.
2. **Rotation Summary**: overall stability in 1–2 lines — incident count by severity and whether the pager was quiet. Write this even for a quiet week; "nothing happened" is useful context.
3. **Active Issues**: each unresolved item that could page, with a status indicator, the current behavior, the trend, the ticket reference, and an explicit page-trigger ("if this crosses X%, page the Y team"). Explain why it hasn't paged yet (e.g. below alert threshold).
4. **Recent Changes (last ~7 days)**: each deploy/config/infra change, what to watch for if it's buggy, and its rollback plan. Flag new monitors that may surface unfamiliar (but real) alerts.
5. **Things to Watch**: metrics, services, or trends that are concerning but haven't alerted — with the specific check (e.g. "check the search dashboard at 11am daily") and any upcoming events that raise risk (planned marketing blast, batch windows).
6. **Useful Context**: anything learned this week that saves the next person time — auto-resolve behaviors, expected-but-noisy alerts and their windows, and links to the relevant runbooks.
7. **Escalation Contacts**: a service × contact × notes table; explicitly note anyone on leave and name the backup.
8. Adapt to context as a sub-step: for a chaotic week, be thorough — distinguish fires that are out, smouldering, and likely to reignite, and explain current state rather than just listing incidents; recommend both the written doc and a 15-minute live walkthrough (doc is the record, meeting is for nuance); for a new on-call engineer, add a quick-reference block linking dashboards, runbooks, and the escalation policy.
9. Assemble the output in the format below.

## Output format

```
**On-Call Handoff: [outgoing window] → [incoming window]**

**Rotation Summary**
[Overall stability; incident count by severity; pager quiet or not.]

**Active Issues**
- 🟡 **[Issue]:** [current behavior, trend, ticket]. **Page-trigger: [if X → page Y].** [Why it hasn't paged yet.]

**Recent Changes (last 7 days)**
- **[Change]** ([date]): [what to watch]. Rollback: [plan].
- [New monitors / expected new alert types]

**Things to Watch**
- [Metric/service/trend] — [specific check / cadence]
- [Upcoming event that raises risk]

**Useful Context**
- [Learned behavior, auto-resolve note, runbook link]

**Escalation Contacts**
| Service | Contact | Notes |
|---------|---------|-------|
| [...] | [...] | [on-leave / backup notes] |
```

## Boundaries

- Never invent incidents, deploys, metric values, ticket numbers, or contact names — mark **Unknown**.
- Never omit a known fragile area to make the rotation look clean; the next person inherits the risk.
- Never state a page-trigger threshold or rollback plan you weren't given — mark it **Unknown** rather than guessing.
- Never assume the incoming engineer knows where dashboards/runbooks live if they're new — link them.

## Chaining

- No natural successor — a handoff is a terminal artifact for the rotation boundary. (If an active issue escalates into a live incident, pick up **incident-commander-runbook**.)
