# Incident Trend Analysis

## Situation

You're doing a quarterly review of incidents and want to find patterns — recurring root causes, vulnerable services, and whether your reliability investments are working. This isn't about individual incidents; it's about systemic learning.

## The Prompt

```
You are an engineering leader analysing incident trends across a quarter. Identify patterns that individual postmortems miss. Group incidents by root cause category, service, time-of-day, and whether they were preventable. Produce actionable recommendations, not just charts.

Structure:
1. **Quarter summary** — total incidents, trend vs previous quarter, severity breakdown
2. **Patterns** — recurring root causes, most-affected services, time-based patterns
3. **Prevention analysis** — what % of incidents were preventable with existing action items?
4. **Action item follow-through** — are postmortem action items actually getting done?
5. **Recommendations** — top 3 systemic investments that would reduce incident volume
6. **Metrics to track** — what should you measure next quarter to gauge improvement

Quarter: [QUARTER]
Incident data: [PASTE_INCIDENT_LIST]
Previous quarter comparison: [PREVIOUS_DATA]
```

## Example Input

```
Quarter: Q1 2025
Previous quarter: Q4 2024 had 18 incidents (3 P0, 7 P1, 8 P2)

Q1 2025 incidents:
1. P0, Jan 8 — API gateway outage, 35min. Root cause: failed deploy with no canary. Service: API gateway.
2. P1, Jan 14 — Payment failures, 20min. Root cause: third-party Stripe blip. Service: Payments.
3. P2, Jan 22 — Search latency spike, 45min. Root cause: index corruption after rebalance. Service: Search.
4. P1, Feb 3 — Auth service down, 15min. Root cause: expired TLS certificate. Service: Auth.
5. P0, Feb 10 — Database failover failure, 52min. Root cause: failover config was stale. Service: Primary DB.
6. P2, Feb 14 — Notification delays, 2hrs. Root cause: SQS queue backlog from marketing blast. Service: Notifications.
7. P1, Feb 21 — API 500s, 25min. Root cause: bad deploy (null pointer in new endpoint). Service: API gateway.
8. P2, Feb 28 — Dashboard timeouts, 30min. Root cause: N+1 query in new analytics page. Service: Admin dashboard.
9. P1, Mar 5 — Payment double-charges, 40min. Root cause: retry logic bug. Service: Payments.
10. P0, Mar 12 — Full outage, 28min. Root cause: config change to load balancer without canary. Service: Infrastructure.
11. P2, Mar 18 — Email delivery failures, 1hr. Root cause: SendGrid rate limit hit. Service: Notifications.
12. P1, Mar 25 — Auth latency spike, 20min. Root cause: Redis connection exhaustion. Service: Auth.
13. P2, Mar 28 — Data pipeline stall, 3hrs. Root cause: disk full on pipeline worker. Service: Data platform.

Postmortem action items from Q4: 28 items total. As of March 31: 14 completed, 8 in progress, 6 not started.
```

## Example Output

> **Incident Trend Analysis — Q1 2025**
>
> **Summary**
> 13 incidents in Q1 (3 P0, 5 P1, 5 P2) compared to 18 in Q4 (3 P0, 7 P1, 8 P2). Total count is down 28%, but P0 count is unchanged. We're reducing minor incidents but not preventing the most severe ones. Total customer-facing downtime: approximately 6 hours across the quarter.
>
> **Pattern 1: Deploy Safety (3 incidents, including 2 P0s)**
> Incidents #1, #7, and #10 were all caused by deploys or config changes without adequate safeguards. Two of the three P0s this quarter fall into this category. This is our highest-leverage area for improvement.
> - Jan 8: API gateway deploy with no canary → P0
> - Feb 21: Bad deploy with null pointer → P1
> - Mar 12: Load balancer config change without canary → P0
>
> **Pattern 2: Resource Exhaustion (3 incidents)**
> Incidents #6, #12, and #13 were all caused by running out of a resource (queue depth, connections, disk space). These are slow-building failures that should be caught by monitoring long before they become incidents.
> - Feb 14: SQS queue backlog → P2
> - Mar 25: Redis connection exhaustion → P1
> - Mar 28: Disk full on pipeline worker → P2
>
> **Pattern 3: Configuration Drift (2 incidents)**
> Incidents #4 and #5 were caused by stale configuration (expired cert, outdated failover config). These are preventable with automated checks.
> - Feb 3: Expired TLS certificate → P1
> - Feb 10: Stale DB failover config → P0
>
> **Service Breakdown**
> | Service | Incidents | Severity | Trend |
> |---------|-----------|----------|-------|
> | API Gateway / Infra | 3 | 2× P0, 1× P1 | ⬆️ Worsening |
> | Payments | 2 | 2× P1 | ➡️ Stable |
> | Auth | 2 | 2× P1 | New this quarter |
> | Notifications | 2 | 2× P2 | ➡️ Stable |
> | Search | 1 | P2 | ⬇️ Improving |
> | Admin | 1 | P2 | New |
> | Data Platform | 1 | P2 | New |
> | Database | 1 | P0 | ⬆️ Worsening |
>
> **Prevention Analysis**
> Of the 13 incidents, **9 were clearly preventable** with mechanisms we either don't have or aren't using consistently:
> - 3 prevented by mandatory canary/progressive deploys
> - 3 prevented by resource utilisation monitoring and alerting at 70-80% thresholds
> - 2 prevented by automated configuration checks (cert expiry, failover validation)
> - 1 prevented by better testing (payment retry logic bug)
>
> **Action Item Follow-Through**
> Of 28 action items from Q4 postmortems: 14 completed (50%), 8 in progress (29%), **6 not started (21%)**. The 6 not-started items include 2 that directly relate to Q1 incidents (deploy safety improvements and monitoring gaps). This means we had incidents this quarter that we already knew how to prevent but hadn't yet addressed.
>
> **Top 3 Recommendations**
>
> 1. **Mandatory progressive deploys (prevents 2 of 3 P0s)**
>    Require canary or blue-green deployment for all production changes. No config change or deploy goes to 100% without a staged rollout. This is the single highest-impact investment we can make — it would have prevented our two worst incidents this quarter.
>
> 2. **Resource utilisation alerting at 70% and 85% thresholds (prevents 3 incidents)**
>    Add predictive alerts for disk usage, connection pools, and queue depth. We currently only alert when things break, not when they're trending toward breaking.
>
> 3. **Automated configuration validation (prevents 2 incidents)**
>    Weekly automated checks for: TLS certificate expiry (alert at 30 days), database failover config validity, DNS record consistency. These are silent failures that only surface during an incident.
>
> **Metrics to Track in Q2**
> - % of deploys using progressive rollout (target: 100%)
> - Mean time to detection (goal: detect before customer impact)
> - Postmortem action item completion rate (goal: >80% by quarter end)
> - P0 incident count (goal: ≤1)

## Tuning Notes

- **Small incident count (< 5):** Individual analysis is more useful than trend analysis. Review each incident deeply rather than looking for patterns.
- **Present to executives:** Lead with the prevention analysis. "9 of 13 incidents were preventable" is a powerful framing for getting investment in reliability.
- **Combine with SLO data:** Pair incident trends with SLO burn rates. A quarter with fewer incidents but more SLO burn suggests the incidents that do happen are worse.
- **Team morale:** Don't make this feel punitive. Frame as "here's how we get better" not "here's what we did wrong." Celebrate improvements from previous quarters.
