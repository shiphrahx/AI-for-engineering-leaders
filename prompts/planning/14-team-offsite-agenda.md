# Team Offsite Agenda

## Situation

You're planning a team offsite — half day, full day, or multi-day. You want it to be substantive and energising, not a series of forced activities that people resent. The goal is alignment, decisions, and connection — things that are genuinely hard to get in day-to-day remote or async work.

## The Prompt

```
You are an engineering leader designing an offsite agenda for your team.

Create a structured offsite agenda. For each session include:
- Duration
- Session name
- Format (workshop / discussion / decision / social / working session)
- Facilitator
- Desired output (what should exist or be decided at the end)

Then add a 3-5 bullet facilitation guide for the most important session.

Principles to apply:
- Start with something that gets people talking, not a slide deck
- Reserve the hardest decision or most contentious topic for the morning when energy is highest
- Build in genuine breaks — not 10 minutes, actual recovery time
- End with clarity on next steps, not more discussion

Context:
- Team: [TEAM_NAME], [HEADCOUNT] people, [REMOTE/HYBRID/IN-PERSON day-to-day]
- Duration: [HALF-DAY / FULL-DAY / 2 DAYS]
- Primary goal: [what this offsite needs to achieve above all else]
- Topics to cover: [LIST]
- Any known tensions or dynamics to be aware of: [OPTIONAL]
```

## Example Input

```
- Team: Search & Discovery, 8 engineers + EM + PM
- Duration: Full day
- Primary goal: Align on Q3 technical direction after two competing approaches emerged
- Topics:
  - Alignment on search architecture: index-time vs. query-time ranking
  - Team working norms (async vs. sync, review SLAs)
  - Celebrate Q2 wins
  - Q3 roadmap priorities
- Dynamics: Two staff engineers have been publicly disagreeing on the architecture. Need to get to a decision, not just more debate.
```

## Example Output

> **Search & Discovery Offsite — Full Day**
>
> | Time | Session | Format | Facilitator | Output |
> |------|---------|--------|-------------|--------|
> | 9:00 | Q2 wins retrospective | Discussion | EM | Shared list of what went well — sets positive tone |
> | 9:30 | Architecture decision: index-time vs. query-time | Decision workshop | External facilitator or EM | A decided direction, written down, with rationale |
> | 11:00 | Break | — | — | — |
> | 11:15 | Q3 roadmap prioritisation | Working session | PM | Ranked list of Q3 bets with rough sizing |
> | 12:30 | Lunch | Social | — | — |
> | 13:30 | Team working norms | Discussion | Rotating | Written team agreement on 3-5 norms |
> | 14:30 | Break | — | — | — |
> | 14:45 | Next steps & owners | Decision | EM | Every output from today has an owner and a date |
> | 15:15 | Optional: early finish or social activity | Social | — | — |
>
> ---
>
> **Facilitation guide: Architecture decision session (90 min)**
>
> - Open by naming the elephant: "We've had two strong views on this. Today's goal is a decision we can all execute on — not consensus for its own sake."
> - Give each approach 10 minutes to present: problem it solves, tradeoffs, what it makes harder.
> - Then open 20 minutes for questions only — no advocacy. Force the room to interrogate both positions.
> - Ask the group to identify the 2-3 criteria that matter most for this decision (performance, maintainability, speed to ship, etc). Write them on a whiteboard.
> - Score each approach against the criteria as a group. This externalises the disagreement from the people onto the options.
> - Make the call. If it's still split, the EM decides and explains why. Document the decision and the rationale immediately.

## Tuning Notes

- **Multi-day:** Day 1 = strategy and alignment, Day 2 = execution planning and team time. Don't mix them.
- **Fully remote team:** A 4-hour virtual offsite beats a full day of Zoom fatigue. Focus on decisions only — connection happens in shorter async touchpoints.
- **High tension dynamics:** Consider bringing an external facilitator for the contentious session so the leader can participate rather than referee.
- **Half-day:** Pick one primary goal only. One good decision is worth more than four inconclusive discussions.
