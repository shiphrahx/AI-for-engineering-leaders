# Phone Screen Script

## Situation

You have 30 minutes to assess whether a candidate should advance to the full interview loop. You need to evaluate fit efficiently without wasting either party's time. The screen should also sell the role — strong candidates are evaluating you too.

## The Prompt

```
You are an engineering manager running a 30-minute phone screen. Balance evaluation with selling. You're assessing: baseline technical competence, motivation, communication skills, and mutual fit. You're also answering their questions about the role and team.

Structure:
1. **Opening (3 min)** — introduce yourself, set expectations for the call
2. **Their story (7 min)** — understand their background and what they're looking for
3. **Technical calibration (10 min)** — lightweight technical questions to assess level and domain knowledge
4. **Role fit (5 min)** — mutual fit assessment
5. **Their questions (5 min)** — let them interview you

Role: [ROLE_AND_LEVEL]
Key technical areas: [WHAT_TO_PROBE]
Team selling points: [WHAT_MAKES_THE_ROLE_ATTRACTIVE]
```

## Example Input

```
Role: Senior Backend Engineer (L5), Payments team
Key technical areas: Distributed systems understanding, API design, data consistency patterns, Go or similar language proficiency
Team selling points: Greenfield billing engine, small senior team, Series B stability, real technical problems
```

## Example Output

> **Phone Screen: Senior Backend Engineer, Payments**
>
> **Opening (3 min)**
> "Thanks for taking the time. I'm [name], EM for the Payments team. I'll spend about 30 minutes with you — I'd like to learn about your background, ask a few technical questions, and then leave time for your questions about us. Sound good?"
>
> **Their Story (7 min)**
> - "Walk me through your career arc — what are you working on now and what are you looking for next?"
> - Listen for: motivation (why leaving?), self-awareness, ability to communicate clearly about technical work
> - Follow-up: "What's the most technically interesting problem you've worked on recently?"
>
> **Technical Calibration (10 min)**
> Pick 2-3 based on their background:
>
> - *API design:* "If you were designing a webhook delivery API, what would the key endpoints look like and how would you handle retries for failed deliveries?" (Looking for: idempotency awareness, retry strategies, practical design thinking)
>
> - *Distributed systems:* "How would you handle a scenario where a payment charge succeeds but the order confirmation fails to save? What patterns would you use?" (Looking for: saga pattern, compensation, eventual consistency awareness)
>
> - *Scaling:* "Tell me about a system you've worked on that needed to scale significantly. What broke first and how did you address it?" (Looking for: real experience, not textbook answers)
>
> - *Go-specific (if applicable):* "What's your experience with Go concurrency? Can you describe a situation where goroutines and channels solved a real problem for you?"
>
> **Role Fit (5 min)**
> - "This role involves owning the billing engine for 800 companies. How does that level of ownership and responsibility feel to you?"
> - "Our team is 6 engineers. Does the team size appeal to you, or would you prefer something larger?"
> - "We're building a usage-based billing system from scratch. What excites or concerns you about greenfield work?"
>
> **Their Questions (5 min)**
> "What questions do you have for me about the team, the work, or the company?"
> Be honest. If they ask something you don't know, say so. Strong candidates are evaluating your authenticity.
>
> **Evaluation Criteria**
> After the call, assess:
> - [ ] Can they communicate technical concepts clearly?
> - [ ] Do they have relevant domain experience or transferable skills?
> - [ ] Did their technical answers demonstrate senior-level thinking?
> - [ ] Is their motivation aligned with what we offer?
> - [ ] Would I want them in our interview loop? (gut check)

## Tuning Notes

- **Junior role:** Drop the technical calibration depth. Focus on learning ability, enthusiasm, and communication. Ask about a project they're proud of and go deep on their contribution.
- **Passive candidate (they didn't apply):** Spend more time selling (10 min) and less on evaluation (5 min). They need to be interested before they'll engage with evaluation.
- **Volume hiring:** Standardise the questions exactly. Consistency matters when you're screening 20+ candidates for the same role.
- **Red flags to watch for:** Can't explain their own work clearly, badmouths current employer extensively, doesn't ask any questions about the role, or gives textbook answers with no real examples.
