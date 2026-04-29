# Stakeholder Project Update

## Situation

You're running a cross-functional project and need to update PMs, design leads, and business stakeholders who don't speak engineering fluently. They want to know: is it on track, what do they need to do, and when will they see results?

## The Prompt

```
You are an engineering leader writing a project status update for cross-functional stakeholders (product managers, designers, business leads). They care about timelines, what they can see/test, and what they need to unblock. Avoid technical jargon — translate everything into business and user impact.

Structure:
1. **Status at a glance** — one line: On Track 🟢 / At Risk 🟡 / Off Track 🔴, with target date
2. **What's new since last update** — visible progress they can verify (demos, staging links, metrics)
3. **What's coming next** — what will be true by the next update
4. **What we need from you** — specific asks with deadlines
5. **Timeline view** — simple milestone table showing planned vs. actual

Project: [PROJECT_NAME]
Target launch: [LAUNCH_DATE]
Stakeholders: [STAKEHOLDER_LIST]
Last update: [LAST_UPDATE_DATE]

Progress since last update:
[PASTE_PROGRESS_NOTES]

Blockers or dependencies on stakeholders:
[PASTE_BLOCKERS]
```

## Example Input

```
Project: Customer Self-Service Portal
Target launch: March 15
Stakeholders: VP Product (Lisa), Head of CS (Tom), Design Lead (Aisha)
Last update: Feb 7

Progress since last update:
- Account settings page complete, in staging
- Billing history page 80% done, API integration working, UI polish remaining
- Password reset flow shipped to 5% of users for testing
- Performance testing started, no issues so far

Blockers:
- Need final copy for the cancellation flow from Product (asked Feb 3, no response)
- Design hasn't delivered the empty state illustrations (promised for Feb 5)
- CS team needs to validate the help article links we're embedding
```

## Example Output

> **Customer Self-Service Portal — Update (Feb 14)**
>
> **Status: 🟡 At Risk** — target launch March 15, currently tracking 3-5 days behind due to pending deliverables from Product and Design.
>
> **What's New**
> - Account settings page is complete — you can test it now at [staging link]
> - Billing history is nearly done (UI polish this week, functional backend live)
> - Password reset flow is live for 5% of users. Early results: 92% success rate, no support tickets
> - Performance tests running clean — no scaling concerns
>
> **Coming Next (by Feb 21)**
> - Billing history page fully complete and in staging
> - Cancellation flow built (pending copy from Product)
> - Help article integration complete (pending CS validation)
>
> **What We Need From You**
> | Who | What | By When |
> |-----|------|---------|
> | Lisa (Product) | Final copy for cancellation flow | **Feb 17** — engineering needs 5 days to implement |
> | Aisha (Design) | Empty state illustrations (3 screens) | **Feb 16** — originally due Feb 5 |
> | Tom (CS) | Validate help article links (we'll send the list Monday) | **Feb 19** |
>
> *If these land by the dates above, we hold the March 15 launch. Each day of delay shifts launch 1:1.*
>
> **Timeline**
> | Milestone | Planned | Actual/Revised | Status |
> |-----------|---------|----------------|--------|
> | Account settings in staging | Feb 7 | Feb 10 | ✅ Done |
> | Billing history complete | Feb 14 | Feb 19 (revised) | 🔄 In progress |
> | Cancellation flow complete | Feb 21 | Blocked | ⏳ Waiting on Product |
> | Full regression testing | Feb 28 | Feb 28 | ⬜ Not started |
> | Staged rollout begins | Mar 8 | Mar 8 | ⬜ Not started |
> | Full launch | Mar 15 | Mar 15-20 (at risk) | ⬜ Not started |

## Tuning Notes

- **Everything on track:** Drop the "what we need" urgency and replace with a "feedback welcome on" section. Stakeholders love getting ahead-of-schedule updates.
- **Project is off track:** Lead with the revised date, then explain what changed. Don't bury the date change in the middle.
- **Multiple workstreams:** Add a workstream-by-workstream breakdown instead of a single narrative. Use a grid format.
- **Executives in the audience:** Cut the timeline table. Replace with one sentence: "On track for [DATE] assuming [KEY_DEPENDENCY] lands by [DATE]."
