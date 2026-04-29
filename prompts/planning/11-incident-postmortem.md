# Incident Postmortem

## Situation

An incident is fully resolved and you need to write a blameless postmortem. You have raw timeline notes, Slack messages, and maybe a Datadog dashboard. You need to turn this into a structured document that helps the org learn from the incident without pointing fingers.

## The Prompt

```
You are an engineering leader writing a blameless incident postmortem. The document should help the organisation learn and improve, not assign blame. Focus on systemic causes (processes, tools, architecture) not individual errors. If a person made a mistake, ask what about the system made that mistake easy to make.

Structure:
1. **Incident summary** — what happened, in one paragraph
2. **Impact** — who was affected, for how long, and the business cost (if known)
3. **Timeline** — chronological events with timestamps
4. **Root cause** — the underlying systemic issue (not "someone did X wrong")
5. **Contributing factors** — other conditions that made the incident possible or worse
6. **What went well** — things that worked during the response
7. **What could be improved** — response gaps or process failures
8. **Action items** — specific, owned, and prioritised (P0: must do, P1: should do, P2: nice to have)
9. **Lessons learned** — broader takeaways for the organisation

Incident details:
[PASTE_TIMELINE_AND_NOTES]

Impact data:
[PASTE_IMPACT_DATA]
```

## Example Input

```
Incident: Production database ran out of disk space at 3:47am GMT on March 8. All write operations failed, which meant no new orders could be placed and user account updates silently failed. The on-call engineer was paged, identified the issue, and expanded the disk at 4:22am. Full service was restored by 4:31am.

Timeline:
- 3:47am: Disk usage hit 100%, PG started rejecting writes
- 3:48am: PagerDuty alert fired for API 500 error rate spike
- 3:52am: On-call (Dev) acknowledged alert, started investigating
- 4:05am: Dev identified disk full on primary DB from Datadog
- 4:10am: Discovered a nightly analytics job had been writing 80GB of temp tables that weren't being cleaned up (job was added 3 weeks ago)
- 4:15am: Dev expanded EBS volume from 500GB to 1TB via AWS console
- 4:22am: Volume expansion complete, writes resumed
- 4:31am: Error rates back to baseline, all services confirmed healthy
- Next morning: Analytics job fixed to clean up temp tables. Added a disk usage alert at 80%.

Impact: 44 minutes of write failures. ~180 customers attempted orders during the window and received errors. Unknown number of account updates silently dropped. Estimated revenue impact: ~$8,500 in failed orders (most customers retried later).
```

## Example Output

> **Postmortem: Production Database Disk Exhaustion (March 8)**
>
> **Summary**
> On March 8 at 3:47am GMT, the production PostgreSQL database ran out of disk space, causing all write operations to fail for 44 minutes. Approximately 180 customers were unable to place orders and an unknown number of account updates were silently dropped. The root cause was an analytics job, deployed 3 weeks prior, that accumulated temporary tables without cleanup. A disk usage monitoring gap meant no one was alerted until writes failed.
>
> **Impact**
> - Duration: 44 minutes (3:47am – 4:31am GMT)
> - 180 customers received errors when attempting to place orders
> - Unknown number of account updates silently failed (non-transactional writes)
> - Estimated revenue impact: ~$8,500 in failed orders
> - No data loss in existing records; issue was isolated to new writes
>
> **Timeline**
> | Time (GMT) | Event |
> |-----------|-------|
> | 3:47 | Disk usage reaches 100%. PostgreSQL rejects all write operations |
> | 3:48 | PagerDuty alert fires on API 500 error rate spike |
> | 3:52 | On-call engineer (Dev) acknowledges alert, begins investigation |
> | 4:05 | Root cause identified: disk full on primary database |
> | 4:10 | Source identified: analytics job creating uncleanable temp tables (deployed 3 weeks ago) |
> | 4:15 | Mitigation started: EBS volume expansion from 500GB to 1TB |
> | 4:22 | Volume expansion complete, write operations resume |
> | 4:31 | Error rates at baseline, all services confirmed healthy |
>
> **Root Cause**
> A nightly analytics job, added 3 weeks prior, was creating large temporary tables (~80GB) in the production database without a cleanup step. The disk filled gradually over 3 weeks until it reached capacity. The system failure was not the analytics job itself — it was the absence of disk usage monitoring and alerts that would have caught the trend weeks before it became an outage.
>
> **Contributing Factors**
> - No disk usage alert existed. We had CPU and memory alerts but no storage monitoring.
> - The analytics job was deployed via a standard code review but there was no checklist item for "does this job create temporary data that needs cleanup?"
> - The production database had no disk auto-scaling configured.
> - Silent write failures for non-transactional operations meant some impact wasn't immediately visible.
>
> **What Went Well**
> - Alert fired within 1 minute of the failure starting
> - On-call acknowledged and began investigating within 4 minutes
> - Root cause identified in 18 minutes — good use of Datadog dashboards
> - Mitigation (volume expansion) was executed cleanly with no complications
> - Total time to resolution: 44 minutes for an infrastructure issue at 4am — solid response
>
> **What Could Be Improved**
> - No one noticed the disk filling over 3 weeks. We should have caught this trend, not the cliff.
> - The deploy review for the analytics job didn't consider storage impact. This is a process gap.
> - Silent write failures are dangerous — we need circuit breakers or explicit error surfacing for non-transactional writes.
>
> **Action Items**
> | Priority | Action | Owner | Due |
> |----------|--------|-------|-----|
> | P0 | Add disk usage alerts at 70% and 85% for all databases | SRE team | This week |
> | P0 | Enable EBS auto-scaling for production database | SRE team | This week |
> | P1 | Add "storage impact" checkbox to deploy review template | [EM] | Next sprint |
> | P1 | Audit all scheduled jobs for temp table cleanup | Data team | Next sprint |
> | P1 | Implement explicit error handling for non-transactional write failures | Backend team | Next 2 sprints |
> | P2 | Investigate disk usage trending dashboard with forecasting | SRE team | This quarter |
>
> **Lessons Learned**
> - Gradual resource exhaustion is a class of problem that point-in-time monitoring misses. We need trend-based alerts, not just threshold alerts.
> - Every job that writes data should have a corresponding cleanup mechanism. "Create" without "delete" is a latent incident.
> - Our deploy review process covers functionality and performance but not resource consumption. This is a gap worth closing.

## Tuning Notes

- **Blameless framing:** If you catch yourself writing "Engineer X should have..." rewrite as "The system allowed X to happen because..." Every human error has a systemic enabler.
- **Customer-facing postmortem:** Shorten to: what happened, impact, what we did, what we're doing to prevent recurrence. Remove internal timeline details and action item assignments.
- **Recurring incident type:** Add a "History" section showing similar past incidents and what changed (or didn't) since each one.
- **Minor incident:** Scale down to summary, root cause, and action items. Not every P3 needs a full postmortem.
