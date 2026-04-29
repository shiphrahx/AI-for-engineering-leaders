# Candidate Closing Pitch

## Situation

You've extended an offer and the candidate is deliberating — maybe weighing a competing offer or just nervous about a job change. You need to make a genuine, personalised pitch that addresses their specific concerns and motivations.

## The Prompt

```
You are a hiring manager preparing a closing pitch for a candidate who's deciding on your offer. Be genuine — don't oversell. Address their specific motivations and concerns. The best pitch connects the role to what THEY want, not just what you need.

Structure:
1. **Their motivations** — what this person is actually looking for (from interviews and conversations)
2. **Personalised pitch points** — 3-4 points connecting the role to their specific goals
3. **Concern mitigation** — address any hesitations they've expressed
4. **Social proof** — what would a current team member say about working here?
5. **The ask** — a clear, low-pressure next step

Candidate: [NAME]
Their motivations: [WHAT_THEY_WANT]
Their concerns: [WHAT_THEY_HESITATE_ABOUT]
Competing offer: [IF_KNOWN]
```

## Example Input

```
Candidate: Jordan
Motivations: Wants to work on a hard technical problem, not just maintain systems. Interested in the billing domain specifically. Values small teams where they have direct impact. Mentioned wanting to grow toward Staff Engineer.
Concerns: Worried about Series B stability (they've been burned by a startup that ran out of funding). Stripe offer feels "safer."
Competing offer: Stripe, ~£115-120K, infrastructure team
```

## Example Output

> **Closing Pitch — Jordan**
>
> **Key message:** Stripe is a great company, but the role you'd have here — owning a greenfield billing engine end to end — is the kind of work that accelerates your career toward Staff. At Stripe, you'd be one senior engineer among thousands. Here, you'd be the person who built the billing system.
>
> **Pitch Points:**
>
> 1. *"You said you want hard technical problems, not maintenance."* This is literally that. Usage-based billing from scratch — metering, aggregation, reconciliation, pricing engine. You'd architect it. At Stripe, the billing system already exists. You'd be maintaining and iterating someone else's architecture.
>
> 2. *"You want to grow toward Staff."* The fastest path to Staff is owning a system that matters. Here, you'd own billing for 800 companies within your first 6 months. The scope and visibility are Staff-track work. I'd actively support your growth toward that level.
>
> 3. *"You value impact on a small team."* Six engineers. Your architectural decisions directly shape the product. There's no "design committee" between you and shipping. At a company Stripe's size, that kind of direct impact is much harder to find.
>
> **Addressing the stability concern:**
> "I understand the worry about startup risk — and it's smart to ask about it. Here's our situation honestly: $18M ARR growing at 40% year-over-year, 112% net revenue retention (customers are spending more each year), 18 months of runway even if growth stopped tomorrow (it won't). We're not pre-revenue hoping for product-market fit. We're a revenue-generating company investing in the billing infrastructure to support the next stage of growth. Happy to connect you with our CFO if you'd like to see the numbers yourself."
>
> **Social proof:**
> "If you talked to Priya on our team, she'd tell you that the thing she values most is that the problems here are real. When she designs a system, it goes into production serving paying customers, and she sees the impact within weeks. She came from a FAANG company and says she's shipped more meaningful work in 18 months here than in 3 years there."
>
> **The ask:**
> "Would it help to have a casual chat with Priya or Marcus on the team — not another interview, just a conversation with someone who'd be your peer? Sometimes hearing it from a teammate is more useful than hearing it from me."

## Tuning Notes

- **They're leaning toward the other offer:** Don't badmouth the competitor. Focus on what's different about your opportunity: "Both are good options. Here's what we offer that they don't."
- **They need more time:** Give it. "Take the time you need. I'd rather you join excited than rushed." Pressure-closing candidates leads to early attrition.
- **Money is the gap:** If you can't match on comp, be honest. "I can't match £120K base. What I can offer is [equity upside / role scope / growth trajectory]. Here's how I'd think about the total picture."
- **They're not responding:** One follow-up is fine. Two is the max. If they ghost, they've decided — respect it.
