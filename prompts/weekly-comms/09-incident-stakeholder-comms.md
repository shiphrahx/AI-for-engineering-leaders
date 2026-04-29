# Incident Stakeholder Comms

## Situation

There's been an incident — outage, data issue, security event — and non-technical stakeholders (execs, sales, CS, customers) need to know what happened, what the impact was, and what you're doing about it. They don't need a root cause analysis; they need confidence that you have it handled.

## The Prompt

```
You are an engineering leader writing an incident communication for non-technical stakeholders. Be honest about the impact, clear about the timeline, and confident about next steps. Never minimise or use weasel words ("minor issue," "brief interruption") if the impact was real. Never speculate on root cause until you're sure.

Phase: [DURING_INCIDENT / INCIDENT_RESOLVED / POST_INCIDENT_SUMMARY]

Structure (adapt based on phase):
1. **Status** — current state in one line
2. **Impact** — who was affected, what they experienced, duration
3. **Timeline** — what happened and when (plain language)
4. **What we're doing / what we did** — immediate actions and longer-term fixes
5. **Customer talking points** (if applicable) — what sales/CS can tell customers

Incident details:
[PASTE_INCIDENT_DETAILS]

Audience: [AUDIENCE]
```

## Example Input

```
Phase: Post-incident summary

Incident: Our payment processing service was down for 47 minutes on Tuesday between 2:13pm and 3:00pm GMT. During this time, customers could not complete purchases. The checkout page showed a spinning loader and then timed out. Approximately 2,300 customers were affected (attempted checkout during the window). Root cause was a database connection pool exhaustion triggered by a traffic spike from a marketing email blast that went out at 2pm. We didn't have auto-scaling configured for the connection pool. The fix was to manually increase the pool size and restart the service. We've since added auto-scaling and an alert.

Audience: VP of Sales, Head of CS, CFO
```

## Example Output

> **Incident Summary: Payment Processing Outage (Tuesday, 2:13–3:00pm GMT)**
>
> **Status:** Fully resolved. Payments are processing normally. A preventive fix is in place.
>
> **Impact**
> For 47 minutes on Tuesday afternoon, customers were unable to complete purchases. The checkout page timed out instead of processing payment. Approximately 2,300 customers attempted to check out during this window and were affected. Orders attempted during the outage were not lost — customers who return to their cart will find it intact.
>
> **Timeline**
> - 2:00pm — Marketing email blast sent, driving a surge in site traffic
> - 2:13pm — Payment service began failing under increased load
> - 2:18pm — Monitoring alerts fired, on-call engineer engaged
> - 2:35pm — Root cause identified: the payment database couldn't handle the connection volume from the traffic surge
> - 2:52pm — Fix applied (database capacity increased and service restarted)
> - 3:00pm — Full service restored, all payments processing normally
>
> **What We've Done**
> - *Immediate:* Increased database capacity and restarted the service
> - *This week:* Added automatic scaling so the database adjusts to traffic surges without manual intervention
> - *This week:* Added an early warning alert that triggers when we reach 70% of capacity (previously, we only alerted at failure)
> - *Next sprint:* Coordinating with Marketing to add an engineering review step before large email blasts that may drive traffic spikes
>
> **Customer Talking Points**
> - "We experienced a 47-minute payment processing interruption on Tuesday. It's fully resolved and we've put safeguards in place to prevent recurrence."
> - "No payment data was compromised. Carts were preserved — customers can return and complete their purchase."
> - "We've added automatic scaling to handle traffic surges without service interruption going forward."
>
> If any customer reports an issue related to this incident, please route to #incident-support and we'll prioritise it.

## Tuning Notes

- **During incident (real-time):** Strip to: Status, Impact, What we're doing, Next update ETA. Do NOT include root cause speculation. Update every 30 minutes or when status changes.
- **Security incident:** Add "Data Impact" section explicitly stating what data was/wasn't affected. Coordinate with legal before sending.
- **Customer-facing email:** Remove internal details. Lead with "what happened to you" and "what we're doing about it." Keep it under 200 words.
- **Recurring issue:** Acknowledge the pattern. "This is the second time this quarter we've seen this type of issue. Here's what's different about our response this time."
