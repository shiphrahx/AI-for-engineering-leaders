# Team Weekly Summary

## Situation

End of the week. You want to send your team a wrap-up that acknowledges what shipped, what's carrying over, and what to expect next week. This isn't for execs — it's for your engineers, so the tone is more direct and the detail is more technical.

## The Prompt

```
You are an engineering manager writing a Friday weekly summary for your direct team of engineers. The tone should be warm but direct — celebrate what shipped, be honest about what didn't, and set clear expectations for next week.

Structure:
1. **What shipped** — specific PRs, features, or milestones with credit to individuals
2. **What's carrying over** — unfinished work with brief context on why and adjusted ETAs
3. **Shoutouts** — call out specific people for going above and beyond (be specific about what they did)
4. **Next week priorities** — numbered list, who owns what
5. **Heads up** — anything the team should know (upcoming on-call rotation, planned maintenance, holidays, visitors)

Context:
- Team: [TEAM_NAME], [TEAM_SIZE] engineers
- Sprint/cycle: [SPRINT_INFO]
- This week's original goals: [PLANNED_GOALS]

What actually happened this week:
[PASTE_NOTES]
```

## Example Input

```
- Team: Checkout Squad, 6 engineers
- Sprint: Sprint 14 (week 1 of 2)
- This week's goals: Start Apple Pay integration, fix cart persistence bug, deploy A/B test for new checkout flow

What actually happened:
- Apple Pay: Alex and Riya paired on the payment token flow, got it working in sandbox. Still need production certs from Apple (waiting on finance to approve the merchant account, could take a few days)
- Cart persistence bug: Dmitri found the root cause — race condition in the session store when tabs sync. Fix is in review, should merge Monday
- A/B test: Deployed on Wednesday for 10% of traffic. Early numbers look positive — 3.2% lift in completion rate but need more data. Sam set up the monitoring dashboard
- Unplanned: Spent ~1.5 days investigating a Stripe webhook reliability issue. Turned out to be an idempotency key collision. Noor patched it Thursday evening
```

## Example Output

> **Checkout Squad — Week 14.1 Wrap-up**
>
> Good week — we made real progress on Apple Pay, squashed a long-standing cart bug, and got our checkout A/B test live with promising early signal.
>
> **What Shipped**
> - A/B test for the new checkout flow is live at 10% traffic. Early read: +3.2% completion rate lift. Dashboard is up for anyone who wants to watch the numbers.
> - Stripe webhook idempotency fix deployed Thursday — resolves the intermittent double-charge alerts we'd been seeing.
>
> **Carrying Over**
> - Apple Pay: sandbox integration works, blocked on production certs (finance → Apple merchant account approval). ETA depends on finance but we're tracking it daily. Once certs land, we're ~2 days from a staging deploy.
> - Cart persistence fix: root cause identified (session store race condition on tab sync), PR in review. Expecting merge Monday.
>
> **Shoutouts**
> - Noor for jumping on the Stripe webhook issue unprompted and shipping a clean fix in one afternoon
> - Alex and Riya for the Apple Pay pairing session — the token flow is solid and well-tested
> - Sam for setting up the A/B monitoring dashboard before anyone had to ask
>
> **Next Week Priorities**
> 1. Merge cart persistence fix and verify in staging — Dmitri
> 2. Apple Pay: chase production certs, start production integration once unblocked — Alex + Riya
> 3. A/B test: let it run, review data mid-week, decide on ramp-up — Sam
> 4. Start scoping guest checkout flow (Sprint 14.2 goal) — Noor
>
> **Heads Up**
> - Dmitri is on-call next week
> - Wednesday is a company all-hands at 2pm — no afternoon standup

## Tuning Notes

- **Remote/async teams:** Add timezone context and specify async check-in expectations for next week.
- **After a rough week:** Lean into the "carrying over" section honestly, but always find at least one shoutout. Teams need to see that effort is noticed even when outcomes slip.
- **Large teams (10+):** Group by workstream rather than listing individual items. Keep shoutouts to 3-4 to avoid dilution.
- **New manager:** Err on the side of more detail in "next week priorities" — explicit ownership and ETAs build trust early.
