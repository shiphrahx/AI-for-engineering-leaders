# Code to Exec Translation

## Situation

You need to explain a technical change — a diff, PR, merged feature, or migration — to a non-technical audience (VP, board, PM, sales, a customer). You want the business framing: what changed, why it matters, and what's needed from them, without the jargon or false precision.

## The Prompt

```
You are translating a specific technical change into the language a non-technical audience acts on. Stay honest to what the change actually does — reframe, never inflate.

Produce:
1. So what — one sentence in the reader's terms (faster/cheaper/lower-risk/unblocked), the outcome not the mechanism.
2. What changed — plain language, mechanism only as far as needed to trust the claim.
3. Why it matters — tie to customer / revenue / risk / cost. If the benefit is indirect (risk paydown, enabling future work), say so plainly rather than overselling.
4. Status & risk — shipped / in progress / behind a flag; what's being watched. Never imply done when it isn't.
5. Needed from you — a decision, awareness, or "Nothing — FYI".

Strip jargon the reader can't act on. Mark anything you don't know as Unknown.

Change: [PASTE_DIFF_PR_OR_DESCRIPTION]
Audience: [WHO_AND_WHAT_THEY_CARE_ABOUT]
Why it was done: [THE_PROBLEM_OR_GOAL]
Impact evidence: [ANY_NUMBERS_YOU_CAN_STAND_BEHIND]
```

## Example Input

```
Change: Migrated session storage from in-memory to Redis, so sessions survive server restarts and scale across instances.
Audience: VP Product — cares about reliability and user experience.
Why it was done: Users were getting logged out during deploys.
Impact evidence: Logout-during-deploy complaints were ~20/week. Not yet measured post-change.
```

## Example Output

> **Session storage change — for VP Product**
>
> **So what:** Users will stop getting logged out when we deploy — removing a weekly source of complaints.
>
> **What changed:** We moved where login sessions are kept so they're no longer tied to a single server. Restarting or scaling servers no longer drops people's sessions.
>
> **Why it matters:** We were getting ~20 logout complaints a week, almost all during deploys. This removes that cause. Post-change numbers not yet measured (Unknown until a week of data).
>
> **Status & risk:** Shipped to all traffic. Watching session error rates for the first week; low risk, rollback is straightforward.
>
> **Needed from you:** Nothing — FYI. Will confirm the complaint drop next week.

## Tuning Notes

- **Audience shift:** For a board, lead with the metric tied to a company goal and drop all mechanism. For a PM, a little more "how" is fine if it affects their planning.
- **Bad news:** If the change is a fix for something that broke, state the impact honestly and don't bury it under the win.
- **Common pitfall:** The model may keep engineering jargon ("Redis", "session store") or oversell an indirect benefit as a user-visible feature. Push it to translate and to name indirect benefits for what they are.
- **Status honesty:** Make sure "shipped" isn't claimed for something behind a flag or partially rolled out.
