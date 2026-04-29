# Performance Review Draft

## Situation

Review cycle is here. You have notes from 1:1s, peer feedback, project outcomes, and your own observations scattered across 6 months. You need to write a clear, fair review that the engineer can learn from and that supports compensation or level decisions.

## The Prompt

```
You are an engineering manager drafting a performance review for a direct report. The review should be specific and evidence-based — every statement should be backed by an example. Balance strengths and growth areas. The tone should be supportive and developmental, not evaluative and distant.

Structure:
1. **Summary** — 2-3 sentences capturing the overall performance narrative
2. **Key accomplishments** — 3-5 specific achievements with impact described
3. **Strengths** — 2-3 core strengths with evidence
4. **Growth areas** — 2-3 areas for development with specific, actionable feedback
5. **Goals for next period** — 2-3 forward-looking objectives
6. **Overall rating** — based on your org's scale, with brief justification

Review period: [PERIOD]
Engineer: [NAME], [LEVEL], [TENURE]
Role expectations: [WHAT_THEIR_LEVEL_EXPECTS]

Raw notes and observations:
[PASTE_NOTES]

Peer feedback summary:
[PASTE_PEER_FEEDBACK]
```

## Example Input

```
Review period: H2 2024 (July-December)
Engineer: Alex, Senior Engineer (L5), 2 years at company
Role expectations: L5 should drive complex projects with minimal guidance, mentor mid-level engineers, contribute to technical direction, and have influence beyond their immediate team.

Notes:
- Led the payment retry system redesign — reduced failed payment rate from 4.2% to 1.8%. Drove the technical design, coordinated with 2 other teams, and mentored Jun (L3) through their first major backend project.
- Took on the on-call improvements initiative voluntarily. Rewrote 6 runbooks, added monitoring alerts, and reduced false-positive pages by 40%.
- Code review quality is excellent — peers consistently say Alex's reviews are thorough and educational.
- Struggled with the Q4 planning process — was asked to write the team's technical roadmap and the first draft lacked business context. Needed significant coaching to connect technical priorities to business goals.
- Can be too heads-down — sometimes doesn't surface blockers or risks early enough. The Stripe integration delay could have been flagged 2 weeks earlier.
- Participated in 3 hiring loops and gave consistently good interview feedback.

Peer feedback:
- "Alex is my go-to for code reviews. They explain the 'why' not just the 'what'." (from Jun, L3)
- "Great technical partner on the payment retry project. Very organised." (from Priya, L5, Billing team)
- "Sometimes I don't know what Alex is working on or if they need help until it's late." (from team lead)
- "Alex's runbook overhaul has made on-call so much less stressful." (from Maya, L4)
```

## Example Output

> **Performance Review: Alex — H2 2024**
>
> **Summary**
> Alex had a strong half delivering high-impact technical work and growing as a mentor. The payment retry redesign was a standout project that demonstrated L5-calibre technical leadership and cross-team coordination. The primary growth area is developing strategic communication skills — connecting technical work to business context and surfacing risks proactively.
>
> **Key Accomplishments**
> - **Payment retry redesign:** Led end-to-end design and delivery of the payment retry system, reducing failed payments from 4.2% to 1.8%. Coordinated with the Billing and Notifications teams and mentored Jun through their first backend project. This is strong L5 work — owning a complex cross-team project from design through delivery.
> - **On-call improvements:** Voluntarily took on rewriting 6 runbooks and adding monitoring alerts, reducing false-positive pages by 40%. This was unglamorous but high-impact work that improved the team's quality of life.
> - **Hiring contributions:** Participated in 3 hiring loops with consistently high-quality, well-structured interview feedback. This helps the team hire well and is a valued L5 contribution.
>
> **Strengths**
> - **Technical excellence with a teaching mindset:** Alex's code reviews are frequently cited as educational — Jun specifically noted that Alex explains the reasoning, not just the correction. This mentoring quality is what separates a strong senior engineer from a great one.
> - **Ownership and initiative:** The on-call improvements were self-identified and self-driven. Alex sees problems and solves them without being asked, which is exactly the behaviour we need at L5.
> - **Cross-team collaboration:** The payment retry project required coordinating across three teams. Priya's feedback confirms that Alex is an effective and organised technical partner.
>
> **Growth Areas**
> - **Strategic framing:** The Q4 roadmap draft focused on technical priorities without connecting them to business goals. At L5 and moving toward Staff, Alex needs to be able to articulate *why* work matters to the business, not just *what* the work is. *Suggestion: Before writing the next planning doc, start with "What business outcome does this enable?" and work backward to the technical plan.*
> - **Proactive communication:** The Stripe integration delay could have been flagged 2 weeks earlier. Alex tends to work through blockers independently rather than signalling early. This is admirable but risky at the scale of projects Alex is now leading. *Suggestion: Adopt a "flag at 60% confidence" rule — if you're more than 60% sure something is a risk, raise it in standup that day, even if you're still investigating.*
>
> **Goals for Next Period**
> 1. Lead a technical planning document that explicitly connects technical work to business outcomes — reviewed and approved by PM and engineering leadership
> 2. Mentor one additional engineer (beyond Jun) on a project with measurable scope
> 3. Practice proactive risk communication — aim for zero "late surprise" flags in the next quarter
>
> **Rating: Exceeds Expectations**
> Alex is performing at a strong L5 level with early signals of Staff-level impact (cross-team technical leadership, mentoring). The strategic communication gap is the key area to develop for a future Staff Engineer conversation.

## Tuning Notes

- **Underperforming engineer:** Be direct but kind. Lead with specific evidence, not conclusions. "The project was delivered 3 weeks late" is better than "time management is an issue." Include concrete steps for improvement.
- **High performer you want to retain:** Be explicit about the promotion path. "Here's what I'd need to see to advocate for Staff" gives them a clear target and signals that you're invested.
- **First review you're writing for this person:** Caveat that you're working from a shorter observation window. Ask the engineer to self-review first and use that as input alongside your notes.
- **Your company's review format doesn't match this structure:** Adapt the content to fit your form, but keep the principle: every claim is backed by evidence, and growth areas include specific suggestions.
