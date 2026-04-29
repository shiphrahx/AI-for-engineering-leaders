# Skip-Level Update

## Situation

You need to write an update for your boss's boss — someone who oversees your area but doesn't have day-to-day visibility into your work. This update needs to be concise, strategically framed, and demonstrate that you're running your area well without being asked.

## The Prompt

```
You are an engineering leader writing an update for your skip-level manager (your boss's boss). This person manages a large organisation and has limited attention. They want to know: is this area healthy, are there risks I should know about, and is this leader handling things well?

Structure:
1. **One-line health check** — "My area is [on track / needs attention / thriving] because [reason]"
2. **Strategic progress** — 2-3 bullets on how your work connects to org/company goals
3. **Risk I'm managing** — one proactive flag showing you see around corners
4. **Ask or FYI** — one thing they should know or one thing you need from them
5. **Metric snapshot** — 2-3 numbers that tell the story

My role: [YOUR_ROLE]
Skip-level: [THEIR_ROLE]
Org-level goals: [ORG_GOALS]

Current status and context:
[PASTE_CONTEXT]
```

## Example Input

```
My role: Engineering Manager, Search Team (8 engineers)
Skip-level: VP of Engineering (oversees 5 EMs, ~40 engineers total)
Org goals: Improve user engagement metrics, reduce infrastructure costs by 15%, ship AI-powered features

Context:
- Search relevance improvements shipped last month are showing +12% in click-through rate
- We're prototyping an AI-powered search suggestions feature, early results promising but need GPU budget approval
- Lost one senior engineer (Marta) to a competitor. Backfill req is approved but hiring is slow — 3 weeks, no strong candidates
- Team morale is good but the on-call rotation is tight with the vacancy. I've temporarily joined the rotation myself to ease the load.
- Infrastructure costs: we've reduced our search cluster costs by 8% through index optimisation. On track for the 15% target by Q end.
```

## Example Output

> **Search Team — Skip-Level Update**
>
> **Health: On track with one watch item.** Delivery is strong and we're tracking well on cost reduction. The backfill for our senior vacancy is my top concern — I'm managing the gap but it's not sustainable past 6 weeks.
>
> **Strategic Progress**
> - *User engagement:* Search relevance improvements from last month are delivering +12% CTR. This directly contributes to the engagement metric and we have a second round of improvements scoped for next sprint.
> - *AI features:* We have a working prototype for AI-powered search suggestions. Early internal testing shows high promise. I'll need GPU budget approval to move this to production — I'm preparing the business case and will bring it to you next week.
> - *Cost reduction:* Search cluster costs down 8% through index optimisation, on track for the 15% org target by end of quarter.
>
> **Risk I'm Managing**
> Senior engineer departure (Marta, left 3 weeks ago). Backfill approved but pipeline is thin — no strong candidates yet. I've joined the on-call rotation to cover the gap and redistributed her project work. This is manageable for another 3-4 weeks but I may need recruiting support or approval to level up the req if the pipeline doesn't improve.
>
> **Ask**
> If you have connections to strong senior search engineers, I'd welcome intros. The req is open and I can share the JD. Separately, I'll send you the GPU budget request for the AI search prototype next week — a heads-up that it's coming.
>
> **Metrics**
> - Search CTR: +12% month-over-month
> - Cluster cost reduction: 8% (target: 15% by Q-end)
> - Backfill pipeline: 12 applicants, 0 strong candidates (3 weeks open)

## Tuning Notes

- **Things are going great:** Don't just report sunshine. Find one forward-looking risk or investment ask. Skip-levels value proactive leaders who aren't complacent.
- **Things are rough:** Be honest but pair every problem with your plan. "Here's the risk, here's what I'm doing, here's what I need from you."
- **You don't know your skip-level well:** Err on the side of more context and less jargon. They may not know your team's projects by name.
- **Written vs. meeting prep:** If this is prep for a live skip-level meeting, add 2-3 questions you want their input on. Meetings are more valuable when you drive the agenda.
