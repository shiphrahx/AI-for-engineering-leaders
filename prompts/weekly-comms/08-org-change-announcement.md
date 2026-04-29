# Org Change Announcement

## Situation

You need to communicate a structural change — a reorg, team merger, new hire joining, or reporting line shift. These announcements need to be clear about what's changing, why, and what people should expect. Ambiguity breeds anxiety.

## The Prompt

```
You are an engineering leader writing an announcement about an organisational change. The tone should be confident but empathetic — acknowledge that change creates uncertainty while being clear about the reasoning and next steps. Never be vague about reporting lines or responsibilities.

Structure:
1. **What's changing** — one paragraph, plain language, no corporate euphemisms
2. **Why** — the business or organisational reason, be honest
3. **What this means for you** — address each affected group specifically
4. **What's NOT changing** — reduce anxiety by being explicit about stability
5. **Timeline** — when changes take effect, key transition dates
6. **Questions?** — how to reach you, when the Q&A session is

Change details:
[DESCRIBE_THE_CHANGE]

Reason for the change:
[EXPLAIN_WHY]

Who's affected:
[LIST_AFFECTED_PEOPLE_OR_TEAMS]

Timeline:
[KEY_DATES]
```

## Example Input

```
Change: Merging the Frontend Platform team (6 people, reports to me) and the Design Systems team (4 people, currently reports to Design Director). The combined team will be called "UI Platform" and will report to me. Sarah, the current Design Systems lead, will become the tech lead of the combined team. Two frontend platform engineers will shift focus to component library work.

Reason: Frontend Platform and Design Systems have been duplicating effort on component architecture. Combining them gives us one team owning the full stack from design tokens to React components. This was Sarah and my idea — we've been informally collaborating for months and want to make it official.

Affected: Frontend Platform team (6), Design Systems team (4), Design Director (losing a team), all frontend engineers who consume the component library.

Timeline: Effective March 1. Transition period through March, fully integrated sprints starting April 1.
```

## Example Output

> **Team Update: Frontend Platform + Design Systems → UI Platform**
>
> **What's Changing**
> Starting March 1, we're combining the Frontend Platform team and the Design Systems team into a single team called UI Platform. This team will own the full lifecycle from design tokens through to shipped React components. The combined team of 10 will report to me, with Sarah stepping into the tech lead role for the unified team.
>
> **Why**
> This isn't a cost-cutting move — it's about removing friction. Frontend Platform and Design Systems have been collaborating on component architecture for months, but the split ownership has led to duplicated work and misaligned priorities. Sarah and I have been discussing this since November, and the teams' informal collaboration has already proven the model works. Making it official lets us move faster and ship a more coherent component library.
>
> **What This Means For You**
> - **Frontend Platform team:** Your day-to-day work doesn't change immediately. Over March, you'll start joining UI Platform ceremonies. Two of you will shift focus toward component library work — I'll discuss specifics in 1:1s this week.
> - **Design Systems team:** You'll move under my reporting line on March 1. Sarah remains your tech lead — her role is expanding, not changing. Your roadmap stays intact; what changes is that you'll now be working side-by-side with the engineers who consume your output.
> - **Design Director (James):** James and I have discussed this and he's supportive. This frees his org to focus on product design without the platform engineering overhead.
> - **All frontend engineers:** You'll have one team to go to for everything component-related. Expect a unified component library roadmap by April.
>
> **What's NOT Changing**
> - Sarah's leadership of the design systems work
> - The component library roadmap and existing commitments
> - Anyone's compensation, level, or title
> - Where you sit (for now — we'll figure out seating in March)
>
> **Timeline**
> - **March 1:** Reporting lines officially change
> - **March 1-31:** Transition month — joint standups, getting-to-know-you sessions, shared retro
> - **April 1:** Fully integrated sprints begin
>
> **Questions?**
> I'm holding an open Q&A on Thursday at 3pm. I'll also be reaching out to each of you for a 1:1 this week. If anything is unclear or concerning, please come to me directly — my door is open and I'd rather address concerns now than let them fester.

## Tuning Notes

- **Layoffs or role eliminations:** This prompt is not designed for reduction-in-force communications. Those require HR and legal involvement. Use this only for structural changes where no one is losing their job.
- **New hire announcement:** Simplify dramatically — who's joining, what they'll work on, their background (2-3 lines), when they start, and how to welcome them.
- **Remote/async teams:** Post the written announcement first, then schedule a live Q&A. Don't announce live and then write it up — people need time to process.
- **Multiple changes at once:** Resist the urge to bundle. One announcement per major change, even if they're related.
