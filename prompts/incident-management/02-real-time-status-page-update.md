# Real-Time Status Page Update

## Situation

An incident is in progress and you need to update your public status page. Customers, partners, and internal stakeholders are watching. You need to be honest about the impact without causing panic, and you need to write it in under 2 minutes because every minute counts.

## The Prompt

```
You are an engineer or engineering leader writing a real-time status page update during an active incident. Be honest, specific, and calm. Never minimise the impact, never speculate on root cause until confirmed, and always include when the next update will be. Customers reading this are anxious — give them facts and a timeline, not corporate fluff.

Phase: [INVESTIGATING / IDENTIFIED / MONITORING / RESOLVED]

Fill in:
- Service(s) affected: [SERVICES]
- Customer impact: [WHAT_CUSTOMERS_EXPERIENCE]
- What we know: [CURRENT_UNDERSTANDING]
- What we're doing: [CURRENT_ACTIONS]
- Duration so far: [DURATION]
- Next update: [WHEN]
```

## Example Input

```
Phase: Identified
Services affected: API and web dashboard
Customer impact: API requests returning 503 errors for approximately 40% of requests. Dashboard loading intermittently. Mobile app partially affected (cached data still works, but real-time data is stale).
What we know: The issue is caused by elevated load on our primary database cluster following a configuration change at 14:22 UTC. The configuration change has been reverted.
What we're doing: Database cluster is recovering. We're monitoring connection pool health and query latency as the system stabilises.
Duration: 35 minutes
Next update: 15 minutes
```

## Example Output

> **Degraded Performance — API and Web Dashboard**
> *Updated: 14:57 UTC | Status: Identified*
>
> **Impact:** Approximately 40% of API requests are returning errors. The web dashboard is loading intermittently. Mobile app users may see stale data but cached functionality remains available.
>
> **What we know:** We identified a database configuration change deployed at 14:22 UTC as the cause. The change has been reverted and the database is recovering.
>
> **Current action:** We are monitoring database recovery and expect service to stabilise as connection pools return to normal levels.
>
> **Next update in 15 minutes or sooner if status changes.**

## Tuning Notes

- **First update (Investigating):** Keep it very short. "We are investigating reports of [impact]. We will provide an update within [15/30] minutes." Don't speculate.
- **Resolution update:** Include total duration, a one-line summary of what happened, and a link to where you'll publish a full postmortem. "We will publish a detailed incident report within 48 hours."
- **Recurring incident:** Acknowledge the pattern. "We recognise this is the second occurrence this month. We are prioritising a permanent fix and will share details in our incident report."
- **Data/security incident:** Coordinate with legal before posting. Include explicit statements about what data was/wasn't affected. Never say "no data was compromised" until you're certain.
