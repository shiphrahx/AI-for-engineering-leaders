# Skip-Level Meeting Prep

## Situation

You're meeting with someone who reports to one of your direct reports — a skip-level 1:1. The goal isn't to undermine the middle manager; it's to build trust, get unfiltered signal about team health, and support career development from a broader perspective.

## The Prompt

```
You are a senior engineering leader preparing for a skip-level 1:1. These meetings serve three purposes: build a direct relationship with the person, get unfiltered signal about team health and their manager's effectiveness, and offer career perspective that their direct manager may not have. Be careful not to undermine the middle manager or create a "shadow management" dynamic.

Structure:
1. **Relationship check-in** — warm, specific opener showing you know what they work on
2. **Their perspective on the team** — open-ended questions about team dynamics and culture
3. **Career development** — broader career conversation that complements their manager's coaching
4. **Signal questions** — tactful questions that surface team health without putting them in an uncomfortable position
5. **Close** — what they should expect from these meetings going forward

Person: [NAME], [ROLE], [LEVEL]
Their manager: [MANAGER_NAME]
What they're working on: [CURRENT_WORK]
Any context: [RELEVANT_CONTEXT]
Meeting frequency: [FREQUENCY]
```

## Example Input

```
Person: Nadia, Frontend Engineer, L4
Manager: Craig (EM of the Web Platform team)
Current work: Leading the design system migration — moving from the legacy component library to the new one. It's a 2-month project and she's halfway through.
Context: Craig mentioned that Nadia has been doing well but seems a bit disengaged in the last few retros. This is our first skip-level — I meet with each of Craig's reports quarterly.
Frequency: Quarterly
```

## Example Output

> **Skip-Level Prep — Nadia (First Meeting)**
>
> **Opening**
> "Thanks for making time for this. I try to meet with everyone in the org quarterly — it's a chance for me to hear directly from you and for you to ask me anything about the broader team or company direction. There's no agenda you need to prepare, and anything you share stays between us unless you'd like me to act on it."
>
> "I know you're leading the design system migration — how's that going? What's been the most interesting challenge so far?"
>
> **Team Perspective** *(pick 2-3, don't interrogate)*
> - "What's one thing about how your team works that you'd keep no matter what?"
> - "If you could change one thing about your team's day-to-day, what would it be?"
> - "How does information flow on your team — do you feel like you generally know what's going on and why?"
>
> **Career Development**
> - "Where do you see yourself heading in the next 1-2 years — are you thinking more depth in frontend, or are you curious about other directions?"
> - "Is there anything you'd like to be working on that you're not getting the chance to?"
> - "From my position I can sometimes see opportunities across the org that your manager might not — is there anything you'd want me to keep an eye out for?"
>
> **Signal Questions** *(these are the questions you're really here to ask, phrased gently)*
> - "Do you feel like you get enough feedback to know how you're doing? And is it timely — or do surprises show up in reviews?"
> - "When you're blocked on something, how easy is it to get unblocked? Are there any recurring friction points?"
> - "Is there anything I should know about that you think might not be reaching me through the normal channels?"
>
> **Close**
> "I'll follow up on anything you'd like me to. If there's nothing specific — that's fine too, these are meant to be low-pressure. I'll reach out again next quarter, but you're welcome to ping me anytime between now and then if something comes up."
>
> *(Note to self: Craig mentioned Nadia seems disengaged in retros. Don't lead with this — let it come up naturally. If it does, explore gently. If it doesn't, raise it with Craig as a coaching topic in our next 1:1 rather than investigating through Nadia.)*

## Tuning Notes

- **First skip-level ever:** Spend more time setting expectations. People worry these meetings are a "check on my manager" — be explicit that it's not. You're here to listen and support.
- **Signal of manager issues:** If you hear consistent concerns about a manager across multiple skip-levels, that's a coaching conversation with the manager, not something you fix by going around them.
- **High performer:** Ask about retention risk signals: "Are you learning? Are you challenged? Is there anything that would make you think about leaving?" — asked directly but warmly.
- **Large org (many skip-levels):** Keep notes and look for cross-team themes. If 3 of 8 skip-levels mention the same process problem, it's an org-level issue.
