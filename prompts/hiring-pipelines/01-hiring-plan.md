# Hiring Plan

## Situation

You need to plan your hiring for the next quarter or half. You have business goals, a current team, and a sense of what's missing. You need a structured plan that justifies headcount, defines roles, prioritises hiring order, and sets a realistic timeline.

## The Prompt

```
You are an engineering leader building a hiring plan. Justify every role with a business need, not just a wish list. Prioritise by impact — if you only get to hire one person, which one moves the needle most? Include timeline, sourcing strategy, and success criteria.

Structure:
1. **Current state** — team size, skills, gaps, and what's at risk without new hires
2. **Roles to fill** — each with: title, level, justification (what becomes possible that isn't today), and priority
3. **Prioritised hiring order** — if you can only fill roles sequentially, what order?
4. **Timeline** — realistic hiring timeline per role (sourcing → offer → start)
5. **Sourcing strategy** — where to find candidates for each role
6. **Budget implications** — comp ranges and total cost
7. **Success criteria** — what "good" looks like 6 months after each hire

Team: [CURRENT_TEAM]
Business goals: [WHAT_THE_BUSINESS_NEEDS]
Gaps: [WHAT_IS_MISSING]
Budget: [HIRING_BUDGET_OR_HEADCOUNT_APPROVED]
```

## Example Input

```
Team: 8 backend engineers (1 senior, 5 mid, 2 junior), 1 EM. No SRE, no data engineer.
Business goals: Scale from 1K to 10K customers this year. Launch real-time analytics feature. Achieve SOC 2 compliance. Reduce incident response time.
Gaps: No one owns infrastructure or reliability. Data pipeline is managed by a mid-level backend engineer who's stretched thin. Senior engineering capacity is low — the one senior engineer is the bottleneck on all technical decisions.
Budget: Approved for 4 headcount this year.
```

## Example Output

> **Engineering Hiring Plan — 2025**
>
> **Current State**
> Team of 8 engineers with a skewed seniority distribution (1 senior, 5 mid, 2 junior). Key gaps: no dedicated reliability/infrastructure ownership (P0 incidents are handled ad hoc), no data engineering expertise (one mid-level engineer is stretched across backend and data work), and a senior engineering bottleneck (one senior engineer reviews all designs and makes all architectural decisions).
>
> **Roles to Fill**
>
> | # | Role | Level | Justification | Priority |
> |---|------|-------|---------------|----------|
> | 1 | Site Reliability Engineer | Senior (L5) | No one owns infrastructure, monitoring, or incident response. 10x customer growth requires scaling confidence we don't have today. SOC 2 compliance needs an owner. | **P0** |
> | 2 | Senior Backend Engineer | Senior (L5) | Our one senior engineer is the bottleneck on all technical decisions. Adding a second senior distributes architectural ownership, accelerates code review, and reduces bus factor. | **P0** |
> | 3 | Data Engineer | Mid (L4) | Real-time analytics is a core business goal. The current backend engineer handling data work is at 120% capacity. This role unblocks both the analytics feature and the engineer currently stretched across two jobs. | **P1** |
> | 4 | Backend Engineer | Mid (L4) | General delivery capacity. With 10x customer growth, we need more hands building features. This hire rounds out the team. | **P2** |
>
> **Hiring Order**
> 1. SRE (most urgent — reliability gaps create existential risk at 10x scale)
> 2. Senior Backend Engineer (unlocks technical capacity for the rest of the team)
> 3. Data Engineer (unblocks a specific business goal)
> 4. Backend Engineer (general capacity — can wait until other hires are onboarded)
>
> **Timeline**
> | Role | Start Sourcing | Expected Offer | Expected Start |
> |------|---------------|----------------|----------------|
> | SRE | January | March | April |
> | Senior Backend | February | April | May-June |
> | Data Engineer | March | May | June-July |
> | Backend Engineer | May | July | August-September |
>
> *Assumptions: 8-week average time-to-offer, 4-week notice period. SRE and senior roles may take longer — pipeline is competitive.*
>
> **Sourcing Strategy**
> - SRE: LinkedIn outreach (targeted), SRE-specific job boards, referrals. This is a specialised role — expect a thin pipeline.
> - Senior Backend: Referrals (highest quality), direct sourcing from competitors and adjacent companies, engineering blog audience.
> - Data Engineer: Data engineering communities, referrals, job boards.
> - Backend Engineer: Standard job posting, referrals, university pipeline for strong mid-levels.
>
> **Budget**
> | Role | Comp Range | Total Annual Cost (with benefits) |
> |------|-----------|----------------------------------|
> | Senior SRE | £90K-£115K | ~£125K-£155K |
> | Senior Backend | £95K-£125K | ~£130K-£165K |
> | Mid Data Engineer | £70K-£90K | ~£95K-£120K |
> | Mid Backend | £65K-£85K | ~£90K-£115K |
> | **Total** | | **~£440K-£550K annual** |
>
> **Success Criteria (6 months post-hire)**
> - SRE: On-call rotation established, monitoring coverage at 100%, incident response time improved by 50%, SOC 2 compliance on track
> - Senior Backend: Owns a technical domain independently, unblocked architectural decisions, mentoring 2+ mid-level engineers
> - Data Engineer: Real-time analytics feature shipped or in beta, data pipeline reliability improved
> - Backend Engineer: Contributing independently to feature delivery at expected velocity

## Tuning Notes

- **Headcount negotiation:** If you need to justify more headcount to leadership, lead with the business risk: "Without an SRE, our current incident response capability cannot support 10x growth. Here's what the last 3 incidents cost us."
- **Startups with limited budget:** Hire the most versatile person first. A senior full-stack engineer who can also do infrastructure is more valuable than two specialists when you're small.
- **Backfills vs. new roles:** Backfills are urgent but don't change team capabilities. New roles change what the team can do. Prioritise accordingly.
- **Internal mobility:** Before opening an external search, check if anyone on the team wants to transition (backend → SRE, mid → senior with a stretch assignment). Internal moves are faster and cheaper.
