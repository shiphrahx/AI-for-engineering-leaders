# Layoff Communication

## Situation

You've been informed that members of your team are being let go. You need to communicate this — to the affected individuals, and to the team that remains. This is one of the hardest things a manager does. The goal is to be humane, honest, and clear.

## The Prompt

```
You are an engineering manager preparing communications for a workforce reduction.

Draft two pieces of communication:

**1. The individual notification (spoken, for the 1:1 meeting)**
A script or talking points for the conversation with the affected employee. It should:
- Get to the point quickly — do not bury the news
- Be clear that the decision is final
- Express genuine appreciation without making it feel performative
- Cover what they need to know: last day, severance/benefits (use placeholders), references, equipment return
- Leave space for their reaction — this is not a monologue

**2. The team message (written, sent after notifications are complete)**
A message to the remaining team. It should:
- Acknowledge what happened directly — don't euphemise
- Be honest about what you can and can't share
- Acknowledge that this is hard, without over-dramatising
- State what comes next for the team

Do not use corporate euphemisms ("right-sizing," "restructuring," "difficult decision"). Be a human.

Context:
- Number affected on your team: [N]
- Reason you can share: [e.g. company-wide cost reduction / org restructure / role elimination]
- Severance: [DETAILS or "HR will follow up with details"]
- Last day: [DATE]
- What's happening to the work: [e.g. backlog paused / redistributed / handed to another team]
```

## Example Input

```
- Number affected: 2 engineers on a team of 8
- Reason: Company-wide cost reduction, not performance-related
- Severance: 8 weeks, HR will send details
- Last day: Today (standard for reductions)
- What's happening to work: Backlog being reviewed; sprint commitments will be re-scoped
```

## Example Output

> **Individual notification — talking points**
>
> *[Sit down. Get to it within 30 seconds.]*
>
> "I have some very difficult news. Your role is being eliminated as part of a company-wide cost reduction. This is not a reflection of your performance — this decision was made above the team level and it's final.
>
> Your last day is today. HR will be in touch within the hour with the specifics of your severance package — it's 8 weeks. You'll have time to say goodbye and return equipment by end of day.
>
> I want to say clearly: you've done good work here. I'll be a strong reference for you, and I mean that.
>
> I know this is a shock. Take a moment. What questions do you have?"
>
> *[Let them respond. Don't fill the silence. Answer what you can; be honest about what you don't know.]*
>
> ---
>
> **Team message — to be sent after all individuals have been notified**
>
> Team,
>
> I need to share some hard news. As part of a company-wide cost reduction, two members of our team have had their roles eliminated today. I've spoken with both of them directly.
>
> I'm not going to pretend this is easy to hear or that there's a way to make it feel okay. Losing colleagues is hard — especially people who've been part of this team.
>
> What I can tell you: this was a cost decision, not a performance one. It was not about anything anyone on this team did or didn't do.
>
> There are things I can't share, including details of their packages — that's between them and HR and it's theirs to keep private.
>
> For the team: we'll meet tomorrow to talk through what this means for our current sprint and backlog. I don't have all the answers yet, but we'll figure it out together.
>
> If you want to talk — about this, or anything — my door is open.
>
> [Name]

## Tuning Notes

- **Performance-related reduction:** Do not use this prompt as-is. Performance separations require different framing and typically more HR involvement in the communication.
- **Large-scale layoff (10%+ of company):** There will likely be a company-wide message before or concurrent with yours. Coordinate timing with your People team. Your role is to be the human follow-up, not the announcement.
- **Remote teams:** The individual conversation should still be video, not written. A message for a layoff is not acceptable.
- **Legal review:** Run all communications through HR/legal before use. Laws around what can and cannot be said vary significantly by jurisdiction.
