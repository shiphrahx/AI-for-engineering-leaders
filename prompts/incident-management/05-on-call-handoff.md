# On-Call Handoff

## Situation

You're either starting or ending an on-call rotation and need to hand off context to the next person. A good handoff prevents the next engineer from being blindsided by known issues and saves them the first hour of figuring out "what's going on."

## The Prompt

```
You are an on-call engineer writing a handoff note for the incoming on-call. Be specific about open issues, recent changes, and anything that might page them. The goal is: the incoming engineer reads this in 5 minutes and knows exactly what to watch, what's fragile, and who to call if things break.

Structure:
1. **Rotation summary** — dates, any incidents during your shift, overall stability assessment
2. **Active issues** — anything unresolved that might page the next person
3. **Recent changes** — deploys, config changes, or infra work in the last 7 days that could cause issues
4. **Things to watch** — metrics, services, or trends that are concerning but haven't triggered alerts yet
5. **Useful context** — anything you learned this week that the next on-call should know
6. **Contacts** — who to escalate to for specific services if needed

Rotation dates: [YOUR_ROTATION_DATES]
Incidents during rotation: [INCIDENTS]
Recent changes: [CHANGES]
Known issues: [KNOWN_ISSUES]
```

## Example Input

```
Rotation: March 10-17
Incidents: One P2 on Tuesday — notification service latency spike, auto-resolved after 20 minutes. Root cause: Redis connection pool exhaustion during a marketing email blast. No customer impact.
Recent changes: Deployed v2.14 of the order service on Wednesday (new retry logic for payment failures). Infra team migrated the staging database to Aurora on Thursday. New Datadog monitors added for API latency percentiles.
Known issues: The search service has been showing intermittent 504s during peak hours (11am-1pm GMT) — about 0.3% of requests. Not yet paged but trending upward. Ticket filed with the search team.
Contacts: For payment issues escalate to Marcus (payments team lead). For infra/database escalate to Priya (SRE lead). Priya is on holiday March 18-20, backup is Tariq.
```

## Example Output

> **On-Call Handoff: March 10-17 → March 17-24**
>
> **Rotation Summary**
> Generally stable week. One P2 incident (Tuesday, auto-resolved). No P0 or P1 incidents. Pager was quiet outside the one event.
>
> **Active Issues**
> - 🟡 **Search service 504s during peak:** Intermittent 504s (0.3% of requests) between 11am-1pm GMT. Not yet at alert threshold but trending upward over the last 5 days. Ticket SEARCH-442 filed with the search team. **If this crosses 1%, page the search team on-call.** It hasn't triggered PagerDuty yet because the alert threshold is 1%.
>
> **Recent Changes (last 7 days)**
> - **Order service v2.14** deployed Wednesday. New payment retry logic. Metrics look clean but keep an eye on the payment success rate dashboard — if retry logic has bugs, it could cause double charges. Rollback plan: revert to v2.13 via standard deploy pipeline.
> - **Staging DB migrated to Aurora** Thursday. Production is unaffected but if staging behaves oddly, it's probably related.
> - **New Datadog monitors** added for API latency p95 and p99. You may see new alert types you haven't seen before — they're real alerts, not noise.
>
> **Things to Watch**
> - Search 504s (see above) — check the dashboard at 11am daily
> - Order service payment retry metrics — first full week in production
> - Redis connection pool utilisation on the notification service — Tuesday's P2 was caused by pool exhaustion during a traffic spike. If marketing is planning another email blast, check Redis headroom beforehand.
>
> **Useful Context**
> - The notification service P2 on Tuesday auto-resolved because the Redis connections timed out and recycled. If it happens again and doesn't auto-resolve within 20 minutes, restart the notification service pods (runbook: [link]).
> - The new Datadog monitors may fire during the daily batch processing window (4-5am GMT). This is expected — the thresholds are being tuned. If it fires outside that window, investigate.
>
> **Escalation Contacts**
> | Service | Contact | Notes |
> |---------|---------|-------|
> | Payments | Marcus (team lead) | Available all week |
> | Infrastructure / DB | Tariq (SRE) | Priya is on holiday March 18-20, Tariq is covering |
> | Search | Yuki (search team on-call) | For the 504 issue specifically |
> | Notification service | Omar (team lead) | Knows the Redis issue well |

## Tuning Notes

- **Quiet week:** Still write the handoff. "Nothing happened" is useful context — it means the incoming on-call can relax slightly. Mention recent changes and things to watch even if nothing is actively broken.
- **Chaotic week:** Be thorough. The incoming on-call needs to know which fires are out, which are smouldering, and which might reignite. Don't just list incidents — explain the current state.
- **Handoff meeting vs. async doc:** Both. Write the doc first, then have a 15-minute sync to walk through it. The doc is the record; the meeting is for questions and nuance.
- **New on-call engineer:** Add a "quick reference" section with links to dashboards, runbooks, and the escalation policy. Don't assume they know where everything lives.
