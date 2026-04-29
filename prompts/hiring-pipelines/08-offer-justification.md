# Offer Justification

## Situation

You want to make an offer and need to justify the compensation package to your compensation review process, HR, or leadership. The justification should tie the candidate's experience and interview performance to a specific level and comp range.

## The Prompt

```
You are a hiring manager writing an offer justification for a candidate. Connect their interview performance and experience to the proposed level and compensation. Address any edge cases (above-band comp, level disagreement, competing offers). The audience is your HR partner or compensation committee.

Structure:
1. **Candidate summary** — who they are, what role, proposed level
2. **Interview performance** — brief summary of debrief outcome
3. **Level justification** — why this level, with evidence mapped to level expectations
4. **Comp proposal** — base, equity, bonus, sign-on if applicable, with rationale
5. **Market context** — competing offers or current comp if known
6. **Risk if we don't act** — what happens if we lose this candidate

Candidate: [NAME]
Role: [ROLE]
Proposed level: [LEVEL]
Interview outcome: [SUMMARY]
Comp proposal: [PROPOSED_COMP]
Market data: [COMPETING_OFFERS_OR_CURRENT_COMP]
```

## Example Input

```
Candidate: Jordan
Role: Senior Backend Engineer, Payments
Proposed level: L5 (Senior)
Interview outcome: Hire (3 Hire, 1 Strong Hire). Strong code quality, good system design, relevant domain experience.
Comp proposal: £110K base + standard equity package
Market data: Jordan's current comp is £95K. They mentioned having a verbal offer from Stripe at approximately £115K-£120K.
```

## Example Output

> **Offer Justification: Jordan — Senior Backend Engineer (L5)**
>
> **Summary**
> Jordan interviewed for Senior Backend Engineer on the Payments team. The debrief was unanimously positive (3 Hire, 1 Strong Hire). They bring 6 years of backend experience with 3 years in payments/fintech, including leading a database migration at their current company. They have a competing offer from Stripe.
>
> **Level: L5 (Senior)**
> Jordan demonstrated L5 behaviours across all interviews: drove the system design independently with minimal guidance, showed mentoring instinct through constructive code review feedback, and provided concrete examples of leading multi-engineer projects. The team is confident in an L5 placement.
>
> **Compensation Proposal**
> | Component | Proposed | Band (L5) | Position in Band |
> |-----------|---------|-----------|-----------------|
> | Base salary | £110,000 | £95K-£125K | 60th percentile |
> | Equity | Standard L5 grant | Per equity grid | Midpoint |
> | Sign-on bonus | £5,000 | Discretionary | To offset unvested equity at current employer |
>
> **Rationale:** £110K base sits at the 60th percentile of our L5 band. This is above midpoint because: (a) Jordan has directly relevant payments domain experience that reduces our ramp-up time, (b) we need to be competitive against the Stripe offer, and (c) the payments team urgently needs senior capacity following a recent departure.
>
> **Market Context**
> Jordan's current base is £95K. They have a verbal offer from Stripe at approximately £115-120K (we have not verified this). Our offer at £110K + equity + sign-on represents a meaningful increase over current comp and positions us competitively against Stripe when total compensation is considered (our equity upside at Series B is arguably stronger than Stripe's public stock at this stage).
>
> **Risk**
> If we lose Jordan, the payments team remains understaffed at a critical time. The usage-based billing project (Q3 target) is at risk without another senior engineer. Our pipeline for this role has been open for 6 weeks with only 2 other candidates reaching the final stage, neither as strong. Losing Jordan likely means 8+ additional weeks to find a comparable candidate.

## Tuning Notes

- **Above-band comp:** Be explicit about why. "This is above the 75th percentile because of [specific rare skill / competing offer / strategic urgency]." Above-band offers without justification erode compensation integrity.
- **Competing offer you can't match:** Don't try. Explain what you offer that the other company doesn't (equity upside, team culture, role scope, growth trajectory). If you can't compete on total comp, compete on opportunity.
- **No competing offer:** Don't anchor to the bottom of the band just because there's no pressure. Pay fairly for the level and experience. Underpaying creates retention risk.
- **Counter-offer risk:** If the candidate might use your offer to negotiate at their current company, address this in the justification. "We recommend extending the offer with a 48-hour decision window to reduce counter-offer risk."
