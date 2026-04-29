# Tech Debt Prioritisation

## Situation

You have a growing list of tech debt items, limited capacity, and stakeholders asking why you're spending time on "non-feature work." You need a prioritised backlog that makes the business case for each item and helps you negotiate for capacity.

## The Prompt

```
You are an engineering leader building a prioritised tech debt backlog. For each item, quantify the cost of inaction and the benefit of resolution. Prioritise by business impact, not engineering frustration. The output should be presentable to product and business stakeholders.

Structure:
1. **Tech debt summary** — total count, estimated cost of carry (developer-hours wasted per sprint), risk exposure
2. **Prioritised backlog** — ranked list, each item with: description, impact if left unaddressed, estimated effort, recommended priority (P0-P3), business justification
3. **Recommended investment** — how much capacity to allocate and how to sequence the work
4. **Quick wins** — items that can be resolved in <1 day with outsized impact

Team: [TEAM_NAME]
Current velocity impact: [HOW_DEBT_AFFECTS_VELOCITY]

Tech debt inventory:
[PASTE_TECH_DEBT_LIST]
```

## Example Input

```
Team: Orders Service, 8 engineers
Velocity impact: Estimates suggest we spend ~15% of each sprint working around or debugging tech debt issues

Tech debt:
- Node 14 (EOL, security patches stopped)
- No integration test suite — relies on manual QA
- Monolithic order processing function (3,200 lines, everyone's afraid to touch it)
- Database queries use raw SQL strings (SQL injection risk, hard to maintain)
- Logging is inconsistent — half the services use structured logging, half don't
- No circuit breaker on payment provider calls — when Stripe blips, we cascade fail
- Deprecated React class components in admin dashboard (can't use hooks, slows feature work)
- API rate limiting is hardcoded per route (takes a deploy to change limits)
- No database migrations tool — schema changes are applied manually in production
- Shared test database causes flaky tests (30% of CI runs fail on unrelated data)
```

## Example Output

> **Orders Service — Tech Debt Assessment**
>
> **Summary:** 10 items identified. Estimated velocity tax: ~15% of sprint capacity (roughly 1.2 engineer-sprints per 2-week cycle). Two items carry active security risk. Three items directly slow feature delivery.
>
> **Prioritised Backlog**
>
> | Priority | Item | Risk if Unaddressed | Effort | Business Case |
> |----------|------|---------------------|--------|---------------|
> | **P0** | Node 14 upgrade | Active security vulnerability exposure; compliance risk | 3-5 days | Compliance blocker; any security incident tied to EOL software is an unforced error |
> | **P0** | Circuit breaker for payment calls | Cascade failures on every Stripe blip; last incident cost 23 minutes of downtime | 2-3 days | Revenue protection — each minute of payment downtime costs ~$X in failed orders |
> | **P1** | Database migrations tool | Manual prod schema changes = high risk of human error and downtime | 3-5 days | Every schema change is currently a high-risk manual operation; one mistake = data incident |
> | **P1** | Parameterised SQL queries | SQL injection vulnerability in 4 endpoints | 5-8 days | Security risk; would be a critical finding in any security audit |
> | **P1** | Fix shared test database / CI flakiness | 30% CI failure rate → engineers waste ~45 min/day retrying or investigating | 3-5 days | Returns ~4 engineer-hours per week in recovered productivity |
> | **P2** | Refactor order processing function | Slows every feature touching order flow; highest bug-introduction rate in codebase | 10-15 days | The #1 source of bugs filed against the team; affects feature delivery speed for the core flow |
> | **P2** | Integration test suite | Manual QA cycle is 2 days per release; limits deploy frequency | 8-12 days | Enables daily deploys (currently weekly); faster feedback loop for features |
> | **P2** | Structured logging standardisation | Incident debugging takes 2-3x longer with inconsistent logs | 3-5 days | Reduces MTTR; directly improves incident response capability |
> | **P3** | API rate limiting configuration | Deploy required to adjust limits; no flexibility during traffic spikes | 2-3 days | Operational flexibility; low urgency but cheap to fix |
> | **P3** | React class → functional components | Slows admin dashboard feature work by ~20% | 5-8 days | Internal tooling only; migrate incrementally as features touch components |
>
> **Recommended Investment**
> Allocate 20% of sprint capacity (1.5 engineers) to tech debt for the next 3 sprints. Sequence: P0 items in Sprint 1 (5-8 days total), P1 items across Sprints 2-3, P2 items begin in Sprint 3 or become next quarter's allocation.
>
> **Quick Wins (< 1 day each)**
> - Add circuit breaker to payment calls using existing resilience library
> - Enable structured logging in the 3 services that don't have it (config change)
> - Isolate test databases per CI run (parallel test DBs via Docker)

## Tuning Notes

- **Presenting to product/business:** Lead with the velocity tax number and the security risks. Frame tech debt as "investing in delivery speed" not "cleaning up code."
- **Skeptical stakeholders:** Add a "cost of doing nothing" row showing the projected impact over 2-3 quarters if debt continues to compound.
- **Small team:** Pick only the top 3 items. Trying to boil the ocean with a small team is worse than doing nothing.
- **After an incident caused by tech debt:** This is your leverage moment. Lead with the incident, show the debt item that caused it, and use the momentum to get capacity approved.
