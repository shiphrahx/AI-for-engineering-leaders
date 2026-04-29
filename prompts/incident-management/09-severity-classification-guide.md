# Severity Classification Guide

## Situation

Your team argues about incident severity every time something breaks. "Is this a P1 or P2?" wastes 10 minutes in a war room that should be spent fixing the problem. You need a clear, unambiguous classification guide that anyone can apply in under 60 seconds.

## The Prompt

```
You are an engineering leader defining incident severity levels for your organisation. Each level needs: a clear definition, concrete examples, expected response times, communication requirements, and who gets involved. The guide should eliminate debate — someone reading it at 3am should be able to classify an incident in under a minute.

Structure per level:
1. **Definition** — one sentence, unambiguous
2. **Examples** — 3-4 specific scenarios at this severity
3. **Response expectations** — time to acknowledge, time to assemble, target resolution time
4. **Communication** — who to notify, how often, through what channel
5. **Who's involved** — required roles in the response

Organisation context:
- Product type: [PRODUCT_TYPE]
- Customer base: [CUSTOMER_BASE]
- SLAs (if any): [SLAS]
- Team size: [TEAM_SIZE]
- Business hours: [BUSINESS_HOURS]
```

## Example Input

```
- Product: B2B SaaS platform (project management tool)
- Customer base: 800 companies, 15,000 daily active users, enterprise tier has contractual 99.9% uptime SLA
- SLAs: Enterprise customers guaranteed 99.9% uptime, < 1hr response for P0s
- Team size: 35 engineers, 24/7 on-call rotation
- Business hours: Most customers are US/EU, peak usage 9am-6pm EST / 9am-6pm CET
```

## Example Output

> **Incident Severity Classification Guide**
>
> *Rule of thumb: classify based on customer impact, not technical complexity. A complex bug that affects no customers is P3. A simple bug that blocks all logins is P0.*
>
> ---
>
> **P0 — Critical: Complete service outage or data integrity risk**
>
> *The product is fully down, or a core workflow is completely broken for all or most users, or customer data may be corrupted/lost.*
>
> | | |
> |---|---|
> | **Examples** | All users unable to log in. Core workflow (e.g., creating/editing projects) completely broken. Data loss or corruption confirmed or suspected. Security breach with active data exposure. |
> | **Acknowledge** | Within 5 minutes |
> | **Assemble** | War room within 15 minutes |
> | **Target resolution** | < 1 hour |
> | **Communication** | Statuspage update within 10 minutes. Internal updates every 15 minutes. Exec notification within 15 minutes. Customer Success notified immediately. Enterprise account managers notified. |
> | **Who's involved** | Incident Commander, on-call engineer(s) for affected service(s), Comms Lead, Engineering Manager (informed), VP Engineering (informed for P0). |
>
> ---
>
> **P1 — Major: Core feature significantly degraded**
>
> *A critical feature is broken or severely degraded for a significant subset of users. The product is usable but a major workflow is impaired.*
>
> | | |
> |---|---|
> | **Examples** | Project creation fails for 30% of users. File uploads timing out. Real-time collaboration (co-editing) completely broken. Search returns no results. Payment processing failing for enterprise tier. Integrations (Slack, Jira) down for all users. |
> | **Acknowledge** | Within 10 minutes |
> | **Assemble** | Investigation within 15 minutes, war room if not resolved in 30 |
> | **Target resolution** | < 2 hours |
> | **Communication** | Statuspage update within 20 minutes. Internal updates every 30 minutes. Exec notification at start and resolution. |
> | **Who's involved** | Incident Commander, on-call engineer for affected service, Comms Lead (optional, IC can cover). |
>
> ---
>
> **P2 — Minor: Non-critical feature degraded or minor UX issue**
>
> *A secondary feature is broken or degraded. Workarounds exist. Most users unaffected or mildly inconvenienced.*
>
> | | |
> |---|---|
> | **Examples** | Notification emails delayed by 30+ minutes. Dashboard analytics loading slowly. CSV export failing. Admin panel partially broken. Cosmetic rendering issue on one browser. Mobile app crashes on a specific device/OS combination affecting < 5% of mobile users. |
> | **Acknowledge** | Within 30 minutes |
> | **Assemble** | On-call investigates asynchronously |
> | **Target resolution** | < 8 hours (or next business day if outside hours) |
> | **Communication** | Statuspage update if customer-visible. Internal Slack post in #incidents. No exec notification unless it escalates. |
> | **Who's involved** | On-call engineer. No IC required unless it escalates. |
>
> ---
>
> **P3 — Low: Cosmetic issue, internal tooling, or edge case**
>
> *Minimal customer impact. Internal tooling issues. Edge cases affecting very few users. No workaround needed because the impact is negligible.*
>
> | | |
> |---|---|
> | **Examples** | Typo in an error message. Internal admin tool slow. Log formatting broken (no customer impact). A feature works incorrectly for users with locale set to a rare timezone. CI/CD pipeline flaky (affects developer productivity, not customers). |
> | **Acknowledge** | Next business day |
> | **Assemble** | Handled in normal sprint flow |
> | **Target resolution** | Within the current sprint or next sprint |
> | **Communication** | No external communication. Internal ticket created. |
> | **Who's involved** | Owning team picks it up in normal prioritisation. No on-call involvement. |
>
> ---
>
> **Quick Classification Flowchart**
>
> ```
> Is the entire product down or is customer data at risk?
>   → YES → P0
>   → NO ↓
> Is a core workflow broken or severely degraded for many users?
>   → YES → P1
>   → NO ↓
> Is a secondary feature broken? Are there workarounds?
>   → YES → P2
>   → NO ↓
> Is the impact cosmetic, internal, or edge-case only?
>   → YES → P3
> ```
>
> **Reclassification:** The IC can upgrade or downgrade severity at any time as more information becomes available. It's better to overclassify initially and downgrade than to underclassify and scramble.

## Tuning Notes

- **"But is it a P1 or a P2?":** If you're debating for more than 30 seconds, it's a P1. Classify high and downgrade. Wasting time debating severity during an incident is worse than slightly overreacting.
- **SLA-aware classification:** If you have contractual SLAs, add a column showing which severity levels count against SLA time. Typically P0 and P1 count; P2 and P3 don't.
- **After-hours policy:** Some organisations downgrade response expectations outside business hours for P2 and below. If so, document it explicitly. P0 and P1 response is always the same regardless of time.
- **Adapt to your product:** These examples are for a B2B SaaS tool. If you're running payment infrastructure, healthcare software, or anything safety-critical, your P1 threshold should be lower (more things are P0/P1).
