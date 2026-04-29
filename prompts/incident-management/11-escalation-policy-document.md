# Escalation Policy Document

## Situation

It's 3am, something is broken, and the on-call engineer doesn't know who to call next. Your escalation policy needs to answer: who gets paged, when, through what channel, and what authority they have to make decisions. This document should eliminate all ambiguity from the "who do I call?" question.

## The Prompt

```
You are an engineering leader creating an escalation policy. It should be a single-page reference that any on-call engineer can follow under stress. Cover both technical escalation (getting the right experts) and management escalation (getting decision-making authority). Include after-hours expectations.

Structure:
1. **Escalation tiers** — who to contact at each level, with contact methods
2. **Trigger criteria** — when to escalate from one tier to the next
3. **Decision authority** — who can approve what (rollbacks, customer comms, vendor contacts, spending)
4. **After-hours policy** — what changes at night and weekends
5. **Cross-team escalation** — how to engage other teams' on-calls
6. **External escalation** — vendor support contacts and how to reach them

Org structure: [ORG_STRUCTURE]
Services and owners: [SERVICE_OWNERS]
On-call structure: [ON_CALL_STRUCTURE]
Communication tools: [TOOLS]
```

## Example Input

```
Org: 40 engineers across 5 teams (API, Payments, Data, Infrastructure, Frontend). Each team has a tech lead and an EM.
On-call: Each team has a primary on-call (weekly rotation). IC rotation is shared across senior engineers and EMs.
Tools: PagerDuty, Slack, Zoom, Statuspage
Vendors: AWS (Enterprise Support), Stripe (24/7 support), SendGrid, Datadog
```

## Example Output

> **Escalation Policy**
>
> ---
>
> **Tier 1: On-Call Engineer (first responder)**
> - *Who:* Primary on-call for the affected service
> - *Contact:* PagerDuty auto-pages. If no response in 5 min, PagerDuty escalates to Tier 2.
> - *Authority:* Can restart services, scale resources, revert last deploy, apply documented runbook fixes
> - *Escalate to Tier 2 when:* Issue not resolved in 20 minutes, issue spans multiple services, issue requires a decision outside their authority, they need help debugging
>
> **Tier 2: Incident Commander + Tech Lead(s)**
> - *Who:* IC rotation (see PagerDuty schedule) + tech lead of the affected team
> - *Contact:* Page via PagerDuty "Incident Commander" schedule. Slack DM as backup.
> - *Authority:* Can open a war room, pull in engineers from other teams, authorise emergency deploys, approve customer comms. Can approve rollbacks that affect data (with Tech Lead confirmation).
> - *Escalate to Tier 3 when:* P0 incident, incident not resolved in 45 minutes, potential data breach or data loss, customer SLA at risk, decision needed on customer credits or public communications
>
> **Tier 3: Engineering Manager**
> - *Who:* EM of the affected team
> - *Contact:* PagerDuty (EM on-call schedule) or phone (numbers in PagerDuty contact cards)
> - *Authority:* Can approve customer-facing communications, authorise cross-team resource reallocation, approve spending (up to £5,000 for emergency vendor support or cloud resources), engage vendor premium support
> - *Escalate to Tier 4 when:* P0 lasting > 1 hour, confirmed data breach, incident requiring legal or PR involvement, decision beyond EM authority
>
> **Tier 4: VP Engineering / CTO**
> - *Who:* VP Engineering (primary), CTO (secondary)
> - *Contact:* Phone call. Numbers in PagerDuty. Text first: "P0 incident — calling you in 2 minutes."
> - *Authority:* All decisions. Can engage legal, PR, and executive team. Can authorise unlimited spending. Can make public statements.
>
> ---
>
> **Cross-Team Escalation**
>
> | Service | On-Call Team | PagerDuty Service | Slack Channel |
> |---------|-------------|-------------------|---------------|
> | API Gateway | API team | "API On-Call" | #team-api |
> | Payments, Billing | Payments team | "Payments On-Call" | #team-payments |
> | Data Pipeline, Analytics | Data team | "Data On-Call" | #team-data |
> | AWS, Databases, Networking | Infra team | "Infra On-Call" | #team-infra |
> | Web App, Mobile | Frontend team | "Frontend On-Call" | #team-frontend |
>
> To page another team's on-call: trigger their PagerDuty service directly. Don't Slack first — if it's urgent enough to need them, it's urgent enough to page them.
>
> ---
>
> **Vendor Support Contacts**
>
> | Vendor | Support Level | How to Reach | Auth Needed |
> |--------|-------------|-------------|-------------|
> | AWS | Enterprise Support | AWS Console → Support → Create Case (Severity: Critical) | Any Tier 2+ |
> | Stripe | 24/7 Support | support.stripe.com + emergency phone line (in 1Password) | Any Tier 1+ |
> | SendGrid | Standard Support | support.sendgrid.com (email only) | Any Tier 1+ |
> | Datadog | Priority Support | In-app chat + support@datadoghq.com | Any Tier 1+ |
>
> ---
>
> **After-Hours Policy (7pm–8am local, weekends, holidays)**
> - P0 and P1: Same response expectations as business hours. Everyone on the escalation path is expected to respond.
> - P2: On-call acknowledges and assesses. If no customer impact, can defer to next business day. If customer-impacting, treat as P1.
> - P3: Next business day. Do not page anyone.
> - *Key difference:* After-hours, default to Tier 2 escalation faster (after 15 minutes instead of 20). Night-time debugging takes longer; get help sooner.

## Tuning Notes

- **Small startup (< 15 engineers):** You probably have 2 tiers: on-call engineer and CTO. That's fine. The document is still valuable for setting expectations and contact methods.
- **Print it:** Put this on a physical card or a pinned Slack message. Under stress, people don't search Confluence.
- **Test the phone numbers:** Quarterly. Nothing is worse than discovering a number is wrong during a P0.
- **Rotations change:** Link to the live PagerDuty schedule rather than listing names. Names go stale; schedule links don't.
