# Quarterly Roadmap

## Situation

Quarter starts in two weeks. You have vague business goals, a backlog of requests, and some tech debt you've been promising to address. You need a structured roadmap that balances feature work, platform investment, and reliability — and that you can defend to your stakeholders.

## The Prompt

```
You are a senior engineering leader creating a quarterly roadmap. Balance customer-facing features, platform investment, and tech debt. Every item should connect to a business outcome or risk mitigation.

Structure:
1. **Quarter theme** — one sentence framing what this quarter is about
2. **Goals** — 3-5 measurable goals tied to business objectives
3. **Committed work** — high-confidence deliverables with target dates and owners
4. **Stretch goals** — items we'll tackle if committed work finishes early
5. **Explicitly not doing** — things stakeholders have asked for that we're intentionally deferring, with reasoning
6. **Investment mix** — percentage split across feature / platform / tech debt / reliability
7. **Key dependencies** — what we need from other teams to deliver
8. **Risks** — what could derail the plan

Context:
- Team: [TEAM_NAME], [TEAM_SIZE] engineers
- Quarter: [QUARTER]
- Business objectives: [BUSINESS_OBJECTIVES]
- Backlog/requests: [PASTE_BACKLOG]
- Known tech debt: [PASTE_TECH_DEBT]
- Constraints: [CONSTRAINTS]
```

## Example Input

```
Team: Payments team, 7 engineers
Quarter: Q3 2025
Business objectives: Expand to 3 new EU markets, reduce payment failure rate from 4.2% to under 2%, support enterprise annual billing
Backlog: EU payment methods (SEPA, iDEAL, Bancontact), annual billing for enterprise, payment retry logic, dunning email improvements, subscription pause feature, Apple Pay support
Known tech debt: Payment service is on Node 16 (EOL), test coverage at 62%, no staging environment for payment flows (test in prod)
Constraints: One engineer on parental leave (returns mid-August), PCI audit in September
```

## Example Output

> **Payments Team — Q3 2025 Roadmap**
>
> **Theme:** Make payments work seamlessly across borders and reduce revenue leakage from failed transactions.
>
> **Goals**
> 1. Launch EU payment methods (SEPA, iDEAL, Bancontact) for 3 target markets — directly enables EU expansion
> 2. Reduce payment failure rate from 4.2% to <2% through retry logic and failure analysis
> 3. Ship enterprise annual billing — unblocks $320K in pipeline waiting on this feature
> 4. Pass PCI audit with zero critical findings
>
> **Committed Work**
> | Deliverable | Target | Owner | Business Impact |
> |-------------|--------|-------|-----------------|
> | SEPA Direct Debit integration | July 31 | Anika + Chen | Unlocks DE, NL, BE markets |
> | iDEAL + Bancontact | Aug 15 | Anika + Chen | Completes EU payment coverage |
> | Smart payment retry with exponential backoff | Aug 1 | Priya | Targets 50% of current failures |
> | Enterprise annual billing | Aug 31 | Marcus + Jess | Unblocks $320K pipeline |
> | Node 16 → 20 migration | Sept 1 | Tariq | Security compliance (EOL risk) |
> | Payment staging environment | July 15 | Tariq | Eliminates test-in-prod risk before PCI audit |
>
> **Stretch Goals**
> - Dunning email improvements (better copy, retry timing)
> - Payment failure analytics dashboard for CS team
>
> **Explicitly Not Doing**
> - **Subscription pause:** Requested by Product but affects <2% of customers. Deferring to Q4 to focus on EU launch and failure rate.
> - **Apple Pay:** High customer demand but requires a new payment processor integration. Scoping in Q3, building in Q4.
>
> **Investment Mix:** 60% features / 15% platform / 15% tech debt / 10% reliability
>
> **Dependencies**
> - Legal: EU entity setup and compliance signoff for SEPA (needed by July 15)
> - Design: Annual billing UI flows (needed by Aug 1)
> - DevOps: Staging environment infrastructure provisioning (needed by July 1)
>
> **Risks**
> - EU payment processor integration is new vendor territory — estimating with 30% buffer but could still surprise us
> - Team at reduced capacity until mid-August (parental leave). If another engineer goes out, stretch goals are cut and annual billing slips.
> - PCI audit in September — if prep work surfaces issues, we may need to redirect capacity in late August

## Tuning Notes

- **Startup (small team):** Focus on 2-3 commitments maximum. Roadmap should fit on one page. "Explicitly not doing" is the most important section — it protects your team from scope creep.
- **Large org:** Add a RACI matrix for cross-team dependencies. Include a "roadmap review cadence" section (monthly check-ins with stakeholders).
- **Executive presentation:** Lead with business outcomes, then show the work that delivers them. Remove technical details like Node version migrations.
- **High uncertainty:** Replace target dates with "early/mid/late quarter" and add confidence levels (high/medium/low) to each committed item.
