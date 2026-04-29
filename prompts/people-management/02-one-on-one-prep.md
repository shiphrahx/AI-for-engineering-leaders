# One-on-One Prep

## Situation

You have a 1:1 with a direct report in 30 minutes. You want to be prepared — with specific topics, not just "how are things going?" You need to review recent context and prepare thoughtful questions.

## The Prompt

```
You are an engineering manager preparing for a 1:1 with a direct report. Generate an agenda that's personalised to this person's current situation. Mix tactical check-ins with career development. The 1:1 should feel like a conversation, not an interrogation.

Structure:
1. **Opening** — a specific, genuine check-in question (not "how are you?")
2. **Their topics first** — leave space for what they want to discuss
3. **Project/work check-in** — 1-2 questions about current work, focused on unblocking them
4. **Growth topic** — one developmental question tied to their goals or recent feedback
5. **Relationship/team check-in** — one question about team dynamics or how they're feeling about the team
6. **Close** — any FYIs or upcoming things they should know about

Person: [NAME], [ROLE], [LEVEL]
Current projects: [CURRENT_WORK]
Recent context: [RECENT_EVENTS]
Development goals: [THEIR_GOALS]
Last 1:1 notes: [PREVIOUS_TOPICS]
```

## Example Input

```
Person: Sana, Backend Engineer, L4 (mid-level, 10 months at company)
Current projects: Working on the notification service refactor. Also picked up a bug fix for the billing API last week.
Recent context: Sana seemed quiet in the last retro. She mentioned in our last 1:1 that she's interested in system design but doesn't feel confident leading design reviews. She's also been doing a lot of code reviews for the team.
Development goals: Wants to grow toward L5 (senior). Interested in system design and cross-team collaboration.
Last 1:1: Discussed notification service architecture choices. She was excited about the project. I suggested she present the design at the team's architecture review.
```

## Example Output

> **1:1 Prep — Sana (Thursday)**
>
> **Opening**
> "How did the notification service design work go this week — did you hit any decision points that felt tricky?"
> *(Ties to her current project and avoids generic openers. Shows I remember what she's working on.)*
>
> **Her Topics**
> "What's on your mind this week — anything you want to start with?"
> *(Always give them the floor first.)*
>
> **Project Check-in**
> - Notification refactor: "Last time we talked about you presenting the design at architecture review. Have you had a chance to think about that? What would make you feel more prepared?"
> - Billing bug fix: "I saw you picked up the billing API bug. How was that — was the codebase easy enough to navigate, or did you hit any walls?"
>
> **Growth Topic**
> "You mentioned wanting to build confidence in system design. One thing I've noticed is that your code reviews are really thorough — you're already doing design thinking in reviews. Have you noticed that connection? I think your next step could be writing up a short design doc for the notification service and walking the team through it."
>
> **Team Check-in**
> "You were a bit quieter than usual in last week's retro. No pressure to share anything, but I wanted to check — is there anything on your mind about the team or how things are going that you'd want to talk about?"
> *(Direct but not pushy. Opens the door without forcing it.)*
>
> **FYIs**
> - Review cycle starts in 3 weeks — I'll be asking for peer feedback nominations next week. Think about who you'd like feedback from.
> - We're planning a team offsite for next month — any preferences on format?

## Tuning Notes

- **New report (first 90 days):** Focus more on onboarding experience, early blockers, and relationship building. Career development conversations can wait until they've settled in.
- **High performer:** Skip the tactical check-in (they're managing their work fine). Spend more time on career growth, stretch opportunities, and what keeps them engaged.
- **Performance concerns:** Add a specific, evidence-based feedback item. Don't save feedback for the review — deliver it in the 1:1 while it's actionable.
- **Remote 1:1:** Add an explicit "energy check" — "How's your week been energy-wise?" Remote engineers are more likely to mask burnout.
