# Sourcing Outreach Message

## Situation

You've found a candidate on LinkedIn or through a referral and need to write a cold outreach message that actually gets a response. Most sourcing messages are ignored because they're generic. Yours needs to be specific to this person and lead with what's in it for them.

## The Prompt

```
You are an engineering leader writing a personalised outreach message to a potential candidate. Lead with what's relevant to THEM (their background, interests, recent work), not what you need. Keep it under 150 words. Be genuine, not salesy. Include one specific reason you reached out to THIS person.

Inputs:
- Candidate: [NAME], [CURRENT_ROLE], [COMPANY]
- What caught your eye: [SPECIFIC_REASON]
- Role: [YOUR_OPEN_ROLE]
- Hook: [WHAT_WOULD_INTEREST_THEM]
- Channel: [LINKEDIN / EMAIL / OTHER]
```

## Example Input

```
Candidate: Sara, Senior Backend Engineer at Monzo
What caught your eye: She gave a talk at GopherCon about building idempotent payment systems. Her blog post about Monzo's billing architecture was excellent.
Role: Senior Backend Engineer, Payments team
Hook: We're building a usage-based billing engine from scratch in Go — the exact problem space she's publicly passionate about.
Channel: LinkedIn
```

## Example Output

> Hi Sara,
>
> I watched your GopherCon talk on idempotent payment systems — the section on reconciliation patterns was especially useful for a problem we're solving right now.
>
> I lead the Payments team at [Company]. We're building a usage-based billing engine from scratch in Go, and your experience designing billing infrastructure at Monzo is exactly the kind of thinking we need.
>
> It's a small, senior team (6 engineers), Series B, $18M ARR. You'd own the architecture for a system that 800 companies will depend on for their revenue.
>
> Would you be open to a 20-minute chat? No pressure — happy to share what we're building even if the timing isn't right.
>
> [Your name]

## Tuning Notes

- **No public signal (no blog, no talks):** Reference their company's work instead. "I've been following how [Company] scaled their payment infrastructure — I'd love to hear your perspective."
- **Referral intro:** Lead with the mutual connection. "Maria mentioned you'd be a great person to talk to about [topic]. She and I work together at [Company]."
- **Follow-up (no response):** One follow-up after 5-7 days is fine. Add one new piece of information (a blog post from your team, a specific project detail). Three messages with no response = stop.
- **Don't do this:** Don't send the job description. Don't open with "I have an exciting opportunity." Don't list requirements. The goal is a conversation, not an application.
