# Engineering All-Hands Agenda

## Situation

You're running a quarterly or monthly engineering all-hands. You have topics to cover, updates to share, and maybe some Q&A. You need a tight agenda that respects everyone's time and doesn't turn into a status meeting nobody needed.

## The Prompt

```
You are an engineering leader planning an all-hands meeting for your engineering organisation.

Draft a structured agenda for the all-hands. For each item include:
- Time allocation
- Owner
- Format (present / discuss / Q&A / demo)
- One-line goal for that segment

Then write 2-3 opening remarks the leader can use to set the tone — what this meeting is for and what you want people to leave with.

Rules:
- Keep total time to [DURATION]
- Reserve at least 10 minutes for open Q&A
- Avoid pure status updates that could be an email
- Every item should answer: why does this need to be live and synchronous?

Context:
- Audience: [ORG_NAME], [HEADCOUNT] engineers, [REMOTE/HYBRID/IN-PERSON]
- Frequency: [QUARTERLY / MONTHLY]
- Duration: [DURATION]
- Key topics to cover: [LIST_TOPICS]
- Tone you want to set: [e.g. energising after a hard quarter / celebratory / refocusing after reorg]
```

## Example Input

```
- Audience: Platform Eng org, 45 engineers, hybrid (30 remote, 15 in-person)
- Frequency: Quarterly
- Duration: 60 minutes
- Key topics:
  - Q1 results vs. OKRs
  - Announce new team structure (splitting infra into two pods)
  - Demo: new internal developer portal
  - Preview Q2 priorities
  - Open Q&A
- Tone: Honest about a mixed Q1, forward-looking, energising
```

## Example Output

> **Platform Engineering All-Hands — Q1 2025**
> *60 minutes | Hybrid*
>
> ---
>
> **Opening remarks** *(2 min — Engineering Lead)*
> "Q1 was a mixed bag — I'll be straight with you about that. We hit some targets, missed others, and learned things we needed to learn. What I want you to leave today with is a clear picture of where we landed, why some things changed, and a real sense of what Q2 is about. We'll have time for questions at the end — nothing is off limits."
>
> ---
>
> | Time | Item | Owner | Format | Goal |
> |------|------|-------|--------|------|
> | 0:00 | Opening & agenda | You | Present | Set tone, frame the meeting |
> | 0:02 | Q1 OKR review | You | Present | Honest assessment — what we hit, what we missed, why |
> | 0:12 | Team structure update | You | Present + Q&A | Announce infra split, explain the why, address concerns |
> | 0:22 | Developer portal demo | Platform team | Demo | Show — don't tell — what shipped |
> | 0:32 | Q2 priorities preview | You | Present | 3-4 bets for the quarter, not an exhaustive list |
> | 0:42 | Open Q&A | All | Q&A | Unfiltered questions — staff the room for hard ones |
> | 0:55 | Close | You | Present | One sentence on what you need from the team |
>
> ---
>
> **Facilitator notes**
> - Seed Q&A with 1-2 anticipated hard questions if the room goes quiet ("One thing I've been asked is…")
> - Have a Slack channel open for async questions from remote attendees during the meeting
> - Share the OKR slide deck in advance so time isn't spent reading numbers live

## Tuning Notes

- **Monthly cadence:** Drop the OKR review, tighten to 30-45 min. Focus on one highlight demo and one decision or change to communicate.
- **Post-reorg:** Give more time to the structural change — aim for 15 min including Q&A. People need to process.
- **Large org (100+):** Pre-collect questions via a form. Designate a co-host to monitor chat for remote attendees.
- **Low energy team:** Open with wins only, even if brief. Don't lead with bad news before you've reminded them what they've accomplished.
