# Recruiter Kickoff Brief

## Situation

You're kicking off a search with a recruiter (internal or external) and want to set them up for success. The brief should give them everything they need to source effectively: what the role actually involves, what a great candidate looks like, and how to pitch the opportunity.

## The Prompt

```
You are an engineering manager writing a kickoff brief for a recruiter. Go beyond the job description — give them the insider context that helps them identify and pitch to the right candidates. Include what makes this role uniquely interesting and what red flags to watch for in applications.

Structure:
1. **Role summary** — what this person will actually do day-to-day (not the JD language)
2. **Ideal candidate profile** — skills, experience patterns, and personality traits that predict success
3. **Anti-patterns** — types of candidates who look good on paper but won't succeed in this role
4. **Selling points** — the 3-5 things that make this role attractive to strong candidates
5. **Common objections** — what might make a candidate hesitate, and how to address it
6. **Sourcing guidance** — where to look, companies to target, keywords to search
7. **Process overview** — interview stages and timeline

Role: [ROLE]
Team: [TEAM_CONTEXT]
Urgency: [TIMELINE]
```

## Example Input

```
Role: Senior Backend Engineer, Payments team
Team: 6-person team building payment infrastructure for a B2B SaaS company (Series B, 150 people). We process $2M/day. Stack is Go, PostgreSQL, Stripe, AWS.
Urgency: High — we need someone started within 8 weeks. A key engineer just left and we have a major project (usage-based billing) launching in Q3.
```

## Example Output

> **Recruiter Brief: Senior Backend Engineer, Payments**
>
> **What this person actually does**
> They'll own critical payment infrastructure that processes $2M daily. First project: build our usage-based billing engine (our customers' #1 request). Day-to-day: designing systems for financial accuracy, writing Go code, working with Stripe APIs, and being the person who makes sure money flows correctly. This is not a CRUD role — it's distributed systems work where correctness is non-negotiable.
>
> **Ideal Candidate**
> - 5+ years of backend engineering, at least 2 in a payments, billing, or fintech context
> - Thinks about edge cases instinctively. When you describe a system, they immediately ask "what happens when this fails?"
> - Go experience strongly preferred, but strong Python/Java engineers who want to work in Go are fine
> - Comfortable with financial accuracy requirements (idempotency, reconciliation, audit trails)
> - Has worked at a company between 50-500 people — understands startup pace but has seen some scale
>
> **Anti-Patterns (skip these candidates)**
> - "I want to build billing from scratch" — we use Stripe. We need someone who integrates well with vendors, not someone who wants to rewrite everything
> - Pure FAANG background with no startup experience — our environment requires more autonomy and less structure than they're used to
> - Can't articulate what "idempotent" means or why it matters for payments
>
> **Selling Points (use these in outreach)**
> 1. "You'll build the billing system that 800 companies rely on for their revenue operations"
> 2. "Usage-based billing is a greenfield project — you'd design the architecture from scratch"
> 3. Series B with strong revenue ($18M ARR) — stability of a growing company with the impact of an early-stage role
> 4. Small, senior team — no layers of management between you and the work
> 5. The technical problems are genuinely interesting (distributed metering, real-time aggregation, financial reconciliation)
>
> **Common Objections**
> - "Go? I've been writing Python/Java..." → "We'll invest in your Go ramp-up. Several team members transitioned to Go here and were productive within a month."
> - "Series B sounds risky" → "$18M ARR, 112% NRR, 800 paying customers. This is a growing, revenue-positive company."
> - "I've never done payments before" → If they have strong distributed systems experience and financial domain interest, that's fine. But they need to have the instinct for correctness.
>
> **Where to Source**
> - Companies: Stripe, Adyen, GoCardless, Paddle, Chargebee, Wise, Revolut alumni (they know payments + startup pace)
> - Also: fintech startups that recently scaled or were acquired
> - Keywords: "payments engineer," "billing systems," "fintech backend," "Go payments"
> - Channels: LinkedIn (targeted outreach), Go community meetups, fintech Slack groups
>
> **Process**
> 1. Recruiter screen (20 min) → 2. Hiring manager screen (30 min) → 3. Take-home (2-3 hours, payments-related) → 4. Technical interview (2 hours) → 5. Culture conversation (45 min) → Offer
> Target: 2-3 weeks from first screen to offer.

## Tuning Notes

- **External recruiter:** Be even more specific about the selling points and anti-patterns. External recruiters have less context about your company and will pattern-match based on what you tell them.
- **Hard-to-fill role:** Add a "creative sourcing" section. Can you target adjacent roles (backend engineers interested in fintech)? Can you sponsor conference talks to attract passive candidates?
- **Multiple open roles:** Give the recruiter a priority ranking. If they can only focus on one role this week, which one?
- **Follow-up:** Schedule a weekly 15-minute sync with the recruiter to review pipeline, adjust sourcing, and share feedback from interviews. Recruiters who get fast, specific feedback source better.
