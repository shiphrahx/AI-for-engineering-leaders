# Remediation Tracker

## Situation

Your postmortems generate action items but too many fall through the cracks. You need a system for tracking remediation items to completion — with clear ownership, deadlines, and visibility into what's actually getting done.

## The Prompt

```
You are an engineering leader creating a remediation tracking system from postmortem action items. Group items by theme and priority, assign clear ownership, and create a review cadence that ensures follow-through. The output should be a living document that's reviewed weekly.

Structure:
1. **Summary dashboard** — total items, completion rate, overdue items
2. **Grouped items** — categorised by theme (monitoring, deploy safety, process, code fix, etc.)
3. **Each item** — description, source incident, priority, owner, deadline, status, blockers
4. **Review cadence** — how and when to review this tracker
5. **Escalation criteria** — when an overdue item gets escalated and to whom

Source incidents and action items:
[PASTE_POSTMORTEM_ACTION_ITEMS]
```

## Example Input

```
From incident INC-041 (API outage, P0, Jan 8):
- P0: Implement canary deploy pipeline for API gateway (Owner: SRE team, Due: Feb 15)
- P1: Add rollback automation to deploy pipeline (Owner: SRE team, Due: Mar 1)
- P2: Document deploy verification checklist (Owner: API team, Due: Feb 28)

From incident INC-043 (Auth cert expiry, P1, Feb 3):
- P0: Set up automated cert expiry monitoring and alerting at 30 days (Owner: SRE team, Due: Feb 20)
- P1: Audit all TLS certificates across services and document renewal dates (Owner: SRE team, Due: Mar 15)

From incident INC-044 (DB failover, P0, Feb 10):
- P0: Validate failover configuration monthly via automated test (Owner: DBA, Due: Mar 1)
- P1: Run quarterly failover drill (Owner: SRE team + DBA, Due: Mar 30)
- P2: Document failover procedure in runbook (Owner: DBA, Due: Mar 15)

From incident INC-047 (Payment double-charges, P1, Mar 5):
- P0: Fix retry logic idempotency bug (Owner: Payments team, Due: Mar 12) — DONE
- P1: Add integration test for retry scenarios (Owner: Payments team, Due: Mar 30)
- P1: Implement duplicate charge detection alert (Owner: Payments team, Due: Apr 15)

Current date: March 20
```

## Example Output

> **Incident Remediation Tracker — As of March 20**
>
> **Dashboard**
> | Metric | Value |
> |--------|-------|
> | Total items | 11 |
> | Completed | 1 (9%) |
> | On track | 4 (36%) |
> | Overdue | 4 (36%) |
> | At risk | 2 (18%) |
> | **P0 items overdue** | **2** ⚠️ |
>
> ---
>
> **🔴 Overdue Items (require immediate attention)**
>
> | Item | Source | Priority | Owner | Due | Days Overdue | Blocker |
> |------|--------|----------|-------|-----|-------------|---------|
> | Canary deploy pipeline for API gateway | INC-041 | P0 | SRE team | Feb 15 | **33 days** | SRE team capacity — competing with infra migration |
> | Cert expiry monitoring + alerting | INC-043 | P0 | SRE team | Feb 20 | **28 days** | Same capacity constraint |
> | Rollback automation | INC-041 | P1 | SRE team | Mar 1 | **19 days** | Depends on canary pipeline |
> | Validate failover config monthly | INC-044 | P0 | DBA | Mar 1 | **19 days** | DBA out sick, returned Mar 15 |
>
> **⚠️ This is a problem.** Two P0 remediation items from January are over a month overdue, both blocked on SRE capacity. These items directly address our two most severe incident categories (deploy safety and configuration drift). If we have another P0 caused by either of these, we'll be writing a postmortem about something we already knew how to prevent.
>
> ---
>
> **🟡 At Risk**
>
> | Item | Source | Priority | Owner | Due | Status |
> |------|--------|----------|-------|-----|--------|
> | TLS cert audit across all services | INC-043 | P1 | SRE team | Mar 15 | 5 days overdue, in progress |
> | Deploy verification checklist | INC-041 | P2 | API team | Feb 28 | 20 days overdue, not started |
>
> ---
>
> **🟢 On Track**
>
> | Item | Source | Priority | Owner | Due | Status |
> |------|--------|----------|-------|-----|--------|
> | Quarterly failover drill | INC-044 | P1 | SRE + DBA | Mar 30 | Scheduled for Mar 28 |
> | Failover runbook documentation | INC-044 | P2 | DBA | Mar 15 | In progress, ~80% done |
> | Retry integration tests | INC-047 | P1 | Payments | Mar 30 | In progress |
> | Duplicate charge detection alert | INC-047 | P1 | Payments | Apr 15 | Scoped, starting next sprint |
>
> **✅ Completed**
>
> | Item | Source | Completed |
> |------|--------|-----------|
> | Fix retry idempotency bug | INC-047 | Mar 10 ✅ |
>
> ---
>
> **Thematic View**
>
> | Theme | Total | Done | Overdue | Key Insight |
> |-------|-------|------|---------|-------------|
> | Deploy safety | 3 | 0 | 2 | SRE capacity is the bottleneck. Most impactful theme. |
> | Configuration management | 3 | 0 | 1 | Cert monitoring and failover validation both overdue. |
> | Code fixes | 2 | 1 | 0 | Payments team executing well. |
> | Monitoring / alerting | 2 | 0 | 1 | Cert monitoring overdue, duplicate charge alert on track. |
> | Documentation | 1 | 0 | 1 | Low priority but easy to close out. |
>
> ---
>
> **Review Cadence**
> - **Weekly:** IC rotation lead reviews this tracker in Monday standup. Any item > 7 days overdue gets discussed.
> - **Bi-weekly:** EM reviews with SRE and affected team leads. Update statuses, unblock items, re-prioritise if needed.
> - **Monthly:** VP Engineering reviews completion rate and overdue P0 items.
>
> **Escalation Criteria**
> - P0 item overdue > 14 days → escalate to VP Engineering
> - P1 item overdue > 30 days → escalate to EM
> - Any item overdue > 60 days → close it (if it's been deprioritised for 2 months, it's not getting done — either reprioritise or accept the risk explicitly)
>
> **Recommendation**
> The SRE team is carrying 6 of 11 remediation items and is the bottleneck. Consider: (1) temporarily dedicating an SRE to remediation for 2 weeks, (2) shifting the deploy verification checklist to the API team (it's documentation, not SRE-specific), or (3) bringing in a contractor for the infra migration to free SRE capacity.

## Tuning Notes

- **Tracking tool:** This format works in a spreadsheet, Notion database, or Jira board. The format matters less than the review cadence — pick whatever tool your team actually checks.
- **Too many items:** If you have 30+ open remediation items, you have a prioritisation problem, not a tracking problem. Force-rank and cut anything below the top 15.
- **Items that never get done:** After 60 days, make a decision: either explicitly prioritise it in the next sprint, or close it and document the accepted risk. Zombie action items erode trust in the postmortem process.
- **Celebrating completion:** When a high-priority item is completed, announce it. "We shipped the canary deploy pipeline — this directly addresses the root cause of our Jan 8 P0." This closes the loop and motivates the team.
