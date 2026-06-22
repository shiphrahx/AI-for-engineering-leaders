# Job Description

## Situation

You're hiring and need a job description that attracts the right candidates — not a keyword dump that reads like every other JD on the internet. A good JD sells the role honestly, filters effectively, and respects the candidate's time.

## The Prompt

```
You are an engineering leader writing a job description that will attract strong candidates. Be specific about what the person will actually do, not generic competencies. Separate must-haves from nice-to-haves honestly. Show what makes this role interesting — not just what you need from the candidate.

Structure:
1. **Role in one sentence** — what this person will do and why it matters
2. **What you'll work on** — 3-5 specific projects or problem areas (not responsibilities lists)
3. **What we're looking for** — must-haves (keep to 4-5) and nice-to-haves (keep to 3-4)
4. **What we offer** — comp, benefits, but also: team culture, interesting technical challenges, growth opportunities
5. **About the team** — who they'll work with, team size, how the team works
6. **How to apply** — process overview so candidates know what to expect

Role: [ROLE_TITLE]
Level: [LEVEL]
Team: [TEAM_DESCRIPTION]
Key projects: [WHAT_THEY_WILL_WORK_ON]
Must-haves: [REAL_REQUIREMENTS]
Nice-to-haves: [PREFERRED_BUT_NOT_REQUIRED]
Comp range: [COMP_RANGE]
```

## Example Input

```
Role: Backend Engineer
Level: Senior (L5)
Team: 6-person Payments team at a B2B SaaS company (Series B, 150 employees). We process ~$2M in transactions daily.
Key projects: Rebuilding our billing engine to support usage-based pricing (our #1 customer request), building integrations with 3 new payment providers for EU expansion, improving payment reliability (currently 98.2%, target 99.9%)
Must-haves: Strong backend skills (we use Go), experience with financial/payment systems, comfortable with distributed systems and data consistency challenges
Nice-to-haves: Stripe/Adyen experience, experience at high-growth startups, familiarity with PCI compliance
Comp range: £95,000-£125,000 + equity
```

## Example Output

> **Senior Backend Engineer — Payments**
>
> **The Role**
> We're looking for a senior backend engineer to help us rebuild how our customers pay and get paid. You'll own critical payment infrastructure that processes $2M daily and is about to get a lot more complex — we're launching usage-based billing and expanding into 3 new European markets.
>
> **What You'll Work On**
> - **Usage-based billing engine:** Our customers' #1 request. You'll design and build the metering, aggregation, and invoicing pipeline that replaces our current flat-rate billing model. This is a greenfield system with interesting data consistency challenges.
> - **EU payment expansion:** Integrate SEPA, iDEAL, and Bancontact payment methods. You'll work with external provider APIs, handle currency conversion edge cases, and navigate the wonderful world of cross-border payment regulations.
> - **Payment reliability:** Take our success rate from 98.2% to 99.9%. This means building smart retry logic, better error classification, and real-time monitoring for a system where every failed payment is lost revenue.
> - **System design:** Contribute to the technical direction of the payments platform. We're a small team making big architectural decisions — you'll have real influence over how this system evolves.
>
> **What We're Looking For**
>
> *Must-haves:*
> - Several years of backend engineering experience with a strong track record of shipping reliable systems
> - Proficiency in Go (or strong in another backend language with willingness to work in Go)
> - Experience working with payment systems, billing, or financial infrastructure — you understand why idempotency matters and what double-charging looks like
> - Comfort with distributed systems concepts: eventual consistency, saga patterns, event sourcing
> - You write code that other people can maintain, debug, and extend
>
> *Nice-to-haves:*
> - Direct experience with Stripe, Adyen, or similar payment provider APIs
> - Background at a high-growth startup where systems needed to scale quickly
> - Familiarity with PCI-DSS compliance requirements
>
> **What We Offer**
> - £95,000–£125,000 base salary + meaningful equity (we're Series B)
> - Hybrid working (London office 2-3 days/week, flexible on which days)
> - The interesting part: you'll work on a system where correctness really matters, the technical challenges are genuine, and your work directly impacts revenue. Our payments team has high autonomy and ships fast.
>
> **About the Team**
> You'll join a team of 6 engineers (2 senior, 3 mid, 1 junior) led by a hands-on EM who still reviews code. We work in 2-week sprints, do blameless postmortems, and believe that on-call should be boring (because the systems are reliable, not because we ignore alerts). We pair frequently and invest in code review as a teaching tool.
>
> **Hiring Process**
> 1. Application review (1-2 business days)
> 2. 30-minute intro call with the hiring manager
> 3. Take-home exercise (scoped to 2-3 hours, payments-related, reviewed anonymously)
> 4. 2-hour technical interview (system design + code walkthrough of your exercise)
> 5. 45-minute team culture conversation
> 6. Offer
>
> We aim to complete the process in 2-3 weeks and we'll give you feedback at every stage, whether you advance or not.

## Tuning Notes

- **Junior role:** Drop the "must-haves" to 2-3 and emphasise learning opportunities, mentorship, and growth. Junior candidates are evaluating whether they'll grow, not whether the work is technically interesting.
- **Remote role:** Be explicit about timezone expectations, communication norms, and how the team bonds. "We're remote" is a fact; "here's how we make remote work" is a selling point.
- **Competitive market:** Lead with what makes the role unique. Every company says "we're growing fast." Instead: "You'll be the first payments engineer and will define the architecture from scratch."
- **Internal JD (for levelling/backfill):** Skip the marketing and focus on the "what you'll work on" and "what we're looking for" sections. Internal JDs are for alignment, not attraction.
