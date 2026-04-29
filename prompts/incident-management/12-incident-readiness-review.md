# Incident Readiness Review

## Situation

You're about to ship a major launch, run a migration, or enter a high-traffic period (Black Friday, product launch). You want to audit your team's incident readiness — are the runbooks current, is monitoring in place, does the on-call know what to expect?

## The Prompt

```
You are an engineering leader conducting a pre-launch incident readiness review. Systematically assess whether your team is prepared to handle incidents related to the upcoming event. The output is a checklist with clear pass/fail for each item and a go/no-go recommendation.

Structure:
1. **Event context** — what's happening and why it increases risk
2. **Monitoring readiness** — are the right alerts in place for the expected failure modes?
3. **Runbook readiness** — are runbooks current and tested for the affected systems?
4. **On-call readiness** — does the on-call team know what's coming and have the context?
5. **Rollback readiness** — can you quickly undo the change if things go wrong?
6. **Communication readiness** — is the comms plan in place for if things go sideways?
7. **Go/No-Go recommendation** — based on the audit, are we ready?

Event: [DESCRIBE_EVENT]
Affected systems: [SYSTEMS]
Risk factors: [RISKS]
Timeline: [EVENT_TIMELINE]
```

## Example Input

```
Event: Black Friday / Cyber Monday sales event. Expected 4x normal traffic. Marketing is running email + social campaigns starting Thursday at midnight. New checkout flow (shipped 2 weeks ago) will handle its first high-traffic test.
Affected systems: Web frontend, API gateway, payment processing, order service, email notifications, CDN
Risk factors: 4x traffic is unprecedented for us. New checkout flow hasn't been load-tested beyond 2x. Payment provider (Stripe) has had Black Friday issues in previous years. Email pipeline has a known queue backlog issue under high volume.
Timeline: Thursday midnight through Monday midnight (4 days of elevated traffic)
```

## Example Output

> **Incident Readiness Review: Black Friday / Cyber Monday**
>
> ---
>
> **Event Context**
> Four days of 4x normal traffic with concurrent marketing campaigns. First high-traffic test of the new checkout flow. Known risk factors with email pipeline and payment provider. This is a high-risk period that warrants thorough preparation.
>
> ---
>
> **Monitoring Readiness**
>
> | Check | Status | Notes |
> |-------|--------|-------|
> | API gateway latency alerts (p99) set for traffic-adjusted thresholds | ⬜ Verify | Current thresholds may false-alarm at 4x traffic. Adjust to 4x headroom. |
> | Payment processing success rate alert | ✅ In place | Alert at < 98% success rate |
> | New checkout flow error rate alert | ⬜ Create | No specific alert exists for the new flow. Add one. |
> | Email queue depth alert | ✅ In place | Alert at > 10K. Consider lowering to 5K given known backlog issue. |
> | CDN cache hit rate alert | ⬜ Create | If cache hit rate drops, origin servers will get slammed. Need an alert. |
> | Database connection pool utilisation | ✅ In place | Alert at 80%. |
> | Synthetic monitoring for checkout flow | ⬜ Create | End-to-end synthetic test running every 60 seconds during the event. |
> | Stripe API health check | ⬜ Create | External monitoring for Stripe's status. Don't rely only on our error rates. |
>
> **Verdict: 🟡 NOT READY** — 4 new alerts needed before Thursday.
>
> ---
>
> **Runbook Readiness**
>
> | System | Runbook Exists | Last Updated | Tested | Status |
> |--------|---------------|-------------|--------|--------|
> | API gateway — traffic overload | Yes | 3 months ago | Untested | 🟡 Review and update |
> | Payment processing — Stripe failures | Yes | 6 months ago | Untested | 🔴 Outdated, update urgently |
> | New checkout flow — rollback to old flow | No | — | — | 🔴 Create immediately |
> | Email pipeline — queue backlog | Yes | 1 month ago | Tested | ✅ Ready |
> | CDN — cache purge and failover | No | — | — | 🟡 Create before Thursday |
> | Database — connection exhaustion | Yes | 2 months ago | Untested | 🟡 Review |
>
> **Verdict: 🔴 NOT READY** — 2 critical runbooks missing, 1 outdated.
>
> ---
>
> **On-Call Readiness**
>
> | Check | Status |
> |-------|--------|
> | On-call schedule covers full Thursday midnight–Monday midnight window | ⬜ Verify |
> | On-call engineers briefed on Black Friday risks and expected failure modes | ⬜ Schedule briefing |
> | Backup on-call identified in case primary is overwhelmed | ⬜ Assign |
> | IC identified and available for the full window | ⬜ Assign |
> | On-call engineers have tested VPN/access from wherever they'll be (holiday travel?) | ⬜ Verify |
> | War room Zoom link pre-created and shared | ⬜ Create |
>
> **Verdict: 🟡 NOT READY** — briefing and logistics need to be confirmed.
>
> ---
>
> **Rollback Readiness**
>
> | Scenario | Rollback Available | Rollback Time | Tested |
> |----------|-------------------|---------------|--------|
> | New checkout flow → old checkout flow | Feature flag exists | < 1 minute | ⬜ Test before Thursday |
> | Scale down if traffic causes cascading failures | Auto-scaling configured | Automatic | ✅ Tested at 2x |
> | Disable marketing email sending to reduce email load | Kill switch exists | < 1 minute | ✅ Tested |
> | Emergency CDN bypass | Manual process | ~10 minutes | ⬜ Document and test |
>
> **Verdict: 🟡 MOSTLY READY** — feature flag rollback needs a test run.
>
> ---
>
> **Communication Readiness**
>
> | Check | Status |
> |-------|--------|
> | Statuspage pre-drafted "investigating" and "monitoring" updates saved as templates | ⬜ Create |
> | Customer Success briefed on potential issues and talking points | ⬜ Schedule briefing |
> | Executive notification plan (who to text if we have a P0 on Black Friday) | ⬜ Confirm |
> | Social media team briefed on what to do if customers report issues publicly | ⬜ Confirm |
> | Internal #black-friday-war-room Slack channel created | ⬜ Create |
>
> **Verdict: 🟡 NOT READY** — all items are quick to resolve but none are done yet.
>
> ---
>
> **Overall Go/No-Go: 🟡 CONDITIONAL GO**
>
> We can proceed with Black Friday if the following are completed by Wednesday EOD:
>
> **Must-do (blocking):**
> 1. Create checkout flow rollback runbook and test the feature flag
> 2. Update payment processing runbook for Stripe failure scenarios
> 3. Create 4 missing monitoring alerts (checkout error rate, CDN cache hit, Stripe health, synthetic checkout test)
> 4. Brief on-call team on risks and expected failure modes
>
> **Should-do (strongly recommended):**
> 5. Load test new checkout flow at 4x traffic
> 6. Create CDN failover runbook
> 7. Pre-draft Statuspage templates
> 8. Create #black-friday-war-room channel and pre-stage war room Zoom link
>
> **Owner:** [EM name] to track completion. Final go/no-go check Wednesday at 4pm.

## Tuning Notes

- **Regular launches (not seasonal events):** Scale this down to the monitoring, runbook, and rollback sections. Communication readiness is less critical for a standard feature launch.
- **First time doing this:** Don't let perfect be the enemy of good. Even a partial readiness review catches the biggest gaps. Do it imperfectly rather than not at all.
- **Post-event:** Run this review again after the event. "How did our preparation hold up?" Compare the predicted failure modes to what actually happened. This calibrates future readiness reviews.
- **Make it a template:** After your first review, save it as a reusable template. The checklist items will be 80% the same for every event — you just need to add event-specific items.
