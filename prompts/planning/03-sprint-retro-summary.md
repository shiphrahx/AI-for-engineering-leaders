# Sprint Retro Summary

## Situation

The retro just ended. You have a Miro board full of sticky notes, or a doc full of raw comments from the team. You need to distill this into actionable themes with clear owners, and share it with the team and stakeholders so the retro actually leads to change.

## The Prompt

```
You are an engineering manager synthesising sprint retrospective feedback into an actionable summary. Group raw feedback into themes, identify root causes where possible, and propose specific actions with owners. The tone should be constructive and team-oriented.

Structure:
1. **Sprint at a glance** — one-line summary: what went well overall, what was the main challenge
2. **What went well** — 2-3 themes with supporting evidence from feedback
3. **What didn't go well** — 2-3 themes with supporting evidence, framed constructively
4. **Root causes** — for the top 1-2 issues, go one level deeper into why
5. **Action items** — specific, measurable actions with owners and timelines
6. **Trends** — how this retro compares to the last 2-3 (are things improving or recurring?)

Sprint: [SPRINT_NAME]
Team: [TEAM_NAME]
Sprint goal: [SPRINT_GOAL]
Goal achieved: [YES/NO/PARTIAL]

Raw retro feedback:
[PASTE_RAW_FEEDBACK]
```

## Example Input

```
Sprint: Sprint 18
Team: Notifications team (5 engineers)
Sprint goal: Ship email digest feature and fix SMS delivery reliability
Goal achieved: Partial — email digest shipped, SMS reliability improved but not at target

Raw feedback:
WENT WELL:
- "Pairing with Omar on the digest template engine was really productive"
- "We shipped the digest feature on time despite the scope change mid-sprint"
- "Better estimation this sprint — only one story spilled"
- "QA caught the timezone bug before it hit prod, nice save"
- "Team energy is good, standups feel focused"

DIDN'T GO WELL:
- "SMS reliability investigation ate 3 days because we had no observability into the third-party provider"
- "Scope change on digest (adding the unsubscribe flow) came from PM on Wednesday with no heads up"
- "I spent a full day on the SMS issue and it turned out to be a vendor-side problem we couldn't fix"
- "Our staging environment doesn't have SMS capabilities so we can't test properly"
- "The PM joining standup and asking for status updates right after we gave status is frustrating"
- "Deploy pipeline was flaky again — 3 failed deploys due to test timeout"
```

## Example Output

> **Sprint 18 Retro Summary — Notifications Team**
>
> **At a Glance:** Strong delivery sprint — we shipped the email digest on time despite a mid-sprint scope change. SMS reliability work was hampered by poor vendor observability and a missing staging capability, which are systemic issues worth addressing.
>
> **What Went Well**
> - **Pairing is working.** The digest template engine was delivered faster and with higher quality through Omar's pairing sessions. This is the third sprint where pairing has been called out positively — worth making it a default practice rather than ad hoc.
> - **Estimation is improving.** Only one story spilled this sprint (down from four in Sprint 16). The team's calibration sessions are paying off.
> - **QA as a safety net.** The timezone bug catch before production validates our investment in pre-release testing.
>
> **What Didn't Go Well**
> - **Vendor observability gap.** Three engineer-days went into diagnosing an SMS issue that turned out to be vendor-side. We had no visibility into the third-party provider's delivery pipeline, so we were debugging blind.
> - **Mid-sprint scope injection.** The unsubscribe flow was added Wednesday with no prior discussion. The team absorbed it and still shipped, but this pattern erodes trust in sprint commitments.
> - **Staging environment limitations.** No SMS testing capability in staging means we're partially testing in production, which is both risky and slow.
>
> **Root Causes**
> - *Vendor observability:* We integrated the SMS provider 8 months ago with no monitoring beyond "did the API return 200?" We need vendor-side delivery metrics and alerting to avoid repeating this blind debugging pattern.
> - *Scope injection:* This is the second sprint in a row with a mid-sprint scope addition from PM. The root issue isn't the PM — it's that we don't have a clear process for handling urgent requests that arrive after sprint commitment.
>
> **Action Items**
> | Action | Owner | By When |
> |--------|-------|---------|
> | Add SMS vendor delivery monitoring (dashboard + alerts) | Omar | Sprint 19 |
> | Propose a "mid-sprint escalation" process to PM and bring to next planning | [You] | Next Monday |
> | Investigate SMS staging capability — scope and estimate | Tara | Sprint 19 (spike) |
> | Fix deploy pipeline test timeout (flaky test audit) | Kai | Sprint 19 |
>
> **Trends**
> - ✅ Estimation accuracy: improving for 3 consecutive sprints
> - ✅ Team energy and standup quality: consistently positive
> - ⚠️ Scope changes mid-sprint: recurring (Sprint 17 and 18)
> - ⚠️ Deploy pipeline reliability: mentioned in 2 of last 3 retros — needs dedicated attention

## Tuning Notes

- **Team morale is low:** Spend more space on "what went well" — even small wins matter when the team is tired. Keep action items to 2-3 maximum so the team doesn't feel overwhelmed.
- **Recurring themes:** If the same issue shows up for the third time, escalate it. "We've raised this in 3 retros without resolution — I'm escalating to [person/process]."
- **New team or new manager:** Add a "team feedback on process" section. Ask explicitly: "Is this retro format working? What would make it better?"
- **Sharing with stakeholders:** Remove individual-level feedback and personal frustrations. Share themes and action items only.
