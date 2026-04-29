# Team Health Survey Analysis

## Situation

You've run a team health survey (or received engagement survey results) and have a spreadsheet of scores and comments. You need to find patterns, identify actionable issues, and create a plan — not just present the data back to the team.

## The Prompt

```
You are an engineering manager analysing team health or engagement survey results. Go beyond the numbers — identify root causes behind low scores, connect themes across questions, and produce an action plan that addresses systemic issues, not just symptoms.

Structure:
1. **Executive summary** — overall health in 2-3 sentences, biggest strength, biggest concern
2. **Score overview** — categorised scores with trend data if available
3. **Qualitative themes** — patterns from free-text responses, grouped by theme
4. **Root cause analysis** — for the bottom 2-3 scores, hypothesise why and connect to qualitative data
5. **Action plan** — 3-5 specific actions with owners and timelines
6. **What to share with the team** — how to communicate results transparently

Team: [TEAM_NAME], [TEAM_SIZE]
Survey tool: [TOOL_NAME]
Response rate: [RESPONSE_RATE]

Survey results:
[PASTE_SCORES_AND_COMMENTS]
```

## Example Input

```
Team: Backend Platform, 9 engineers
Survey: Quarterly pulse survey (1-5 scale)
Response rate: 8/9 (89%)

Scores (this quarter / last quarter):
- "I understand how my work connects to company goals": 3.1 / 3.4
- "I have the tools and resources to do my job well": 2.8 / 3.0
- "I feel I can grow in my career here": 3.5 / 3.6
- "I trust my manager": 4.6 / 4.5
- "I'd recommend this team to a friend": 3.8 / 4.0
- "Meetings are a good use of my time": 2.4 / 2.6
- "I feel my contributions are recognised": 3.2 / 3.0

Comments:
- "Too many meetings, not enough deep work time"
- "I don't understand why we're building [project X] when [project Y] seems more important"
- "Our dev environment is painfully slow. I lose 30+ minutes a day waiting for builds"
- "Manager is great but I don't know what the larger org is doing or why"
- "Recognition is getting better since the shoutouts channel started"
- "Sprint planning takes 2 hours and half of it is rehashing decisions"
- "I like this team but I'm not sure where I'm going next in my career here"
```

## Example Output

> **Backend Platform — Q1 Pulse Survey Analysis**
>
> **Executive Summary**
> Trust in leadership is a clear strength (4.6), and career growth sentiment is stable. The two areas needing attention are meeting effectiveness (2.4, lowest score, declining) and tooling/dev environment (2.8, declining). Both are connected: poor tooling wastes time, and excessive meetings cut into what's left. The free-text comments suggest a broader theme of time being consumed by low-value activities.
>
> **Score Overview**
> | Category | Score | Trend | Signal |
> |----------|-------|-------|--------|
> | Manager trust | 4.6 | ↑ +0.1 | 🟢 Strong |
> | Career growth | 3.5 | ↓ -0.1 | 🟡 Stable but watch |
> | Team recommendation | 3.8 | ↓ -0.2 | 🟡 Slight decline |
> | Recognition | 3.2 | ↑ +0.2 | 🟡 Improving |
> | Work-to-goals connection | 3.1 | ↓ -0.3 | 🟡 Declining — needs action |
> | Tools & resources | 2.8 | ↓ -0.2 | 🔴 Below threshold |
> | Meeting effectiveness | 2.4 | ↓ -0.2 | 🔴 Lowest score, declining |
>
> **Qualitative Themes**
> - **Time waste** (4 comments): Meetings are too long, dev environment is slow, sprint planning rehashes decisions. The common thread: engineers feel their productive time is being eroded.
> - **Strategic clarity** (2 comments): People don't understand why certain projects are prioritised. "I don't understand why we're building X when Y seems more important" signals a communication gap, not a prioritisation problem.
> - **Career direction** (1 comment): One person wants clearer career pathing. This is a weaker signal (single comment) but worth monitoring given the slight decline in the career growth score.
>
> **Root Cause Analysis**
> - **Meetings (2.4):** Sprint planning at 2 hours is the likely driver. Comments suggest decisions are being re-litigated in planning that should be resolved beforehand. Additionally, the general "too many meetings" sentiment suggests the team may have accumulated recurring meetings that haven't been audited.
> - **Tools (2.8):** The dev environment build time issue (30+ min/day lost) is concrete and quantifiable. At 9 engineers, that's potentially 4.5 engineer-hours lost per day. This isn't a perception problem — it's a productivity tax.
> - **Work-to-goals (3.1, declining):** This dropped 0.3 points, the biggest decline. Combined with the comment about not understanding project priorities, it suggests the team needs more context about *why* they're building what they're building, not just *what*.
>
> **Action Plan**
> | Action | Owner | Timeline | Addresses |
> |--------|-------|----------|-----------|
> | Restructure sprint planning: pre-read with decisions documented async, live session capped at 45 min for alignment only | EM | Next sprint | Meetings |
> | Meeting audit: list all recurring meetings, cancel any without a clear purpose, make attendance optional where possible | EM | This week | Meetings |
> | Dev environment spike: allocate 2 engineering days to diagnose and propose a fix for build times | Senior Eng | Next sprint | Tools |
> | Monthly "why we're building this" context session: 30-min async doc or short meeting connecting current work to company strategy | EM | Start next month | Work-to-goals |
> | Schedule career conversations with anyone who hasn't had one in 90 days | EM | Within 2 weeks | Career growth |
>
> **Sharing with the Team**
> Share the scores and themes transparently in the next team meeting. Present the action plan alongside the results — showing you've already started acting on the feedback signals that you take it seriously. Explicitly thank the team for the high response rate and honest comments. Don't identify or speculate about who wrote which comment.

## Tuning Notes

- **Low response rate (< 70%):** Note that results may not be representative. Focus on themes from comments rather than small score differences.
- **Scores are all high:** Don't celebrate and move on. Ask: "What would make a 4 into a 5?" The gap between good and great is often where the most valuable feedback lives.
- **One very low outlier:** If one score is dramatically lower than the rest, investigate in 1:1s (not group settings). It may reflect one person's strong negative experience rather than a team-wide issue.
- **Multi-team comparison:** If you're reviewing results across multiple teams, resist the urge to rank teams. Instead, identify cross-team themes that suggest org-level issues.
