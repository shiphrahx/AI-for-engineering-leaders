# Project Pre-Mortem

## Situation

You're about to kick off a significant project. Before the team dives in, you want to imagine all the ways it could fail — so you can prevent those failures instead of writing postmortems about them later.

## The Prompt

```
You are an engineering leader running a pre-mortem exercise. Imagine it's 3 months from now and the project has failed. Generate the most likely failure modes across technical, people, process, and external dimensions. For each, assess likelihood and propose a preventive action.

Structure:
1. **Project context** — restate the project, timeline, and success criteria
2. **Failure modes** — categorised list (technical, people/team, process, external/dependencies), each with: what went wrong, likelihood (high/medium/low), impact (high/medium/low), and a preventive action
3. **Top 3 kill risks** — the failures most likely to actually sink the project
4. **Pre-mortem action plan** — specific steps to take before or during the project to address the top risks

Project: [PROJECT_DESCRIPTION]
Timeline: [TIMELINE]
Team: [TEAM_COMPOSITION]
Success criteria: [SUCCESS_CRITERIA]
Known concerns: [ANY_EXISTING_WORRIES]
```

## Example Input

```
Project: Migrate our monolithic user service to three microservices (auth, profile, preferences) while maintaining zero downtime for customers
Timeline: 12 weeks
Team: 5 engineers (2 senior, 2 mid, 1 junior), 1 PM
Success criteria: All user-facing functionality migrated with no customer-visible disruption, latency unchanged or improved, zero data loss
Known concerns: The user service handles 50K requests/minute at peak. No one on the team has done a live migration at this scale before. The user table has 8 years of schema evolution and some undocumented columns.
```

## Example Output

> **Pre-Mortem: User Service Migration**
>
> **Context:** Decomposing the monolithic user service into auth, profile, and preferences microservices over 12 weeks. Team of 5 engineers. Must maintain zero downtime, zero data loss, and current latency SLAs throughout.
>
> **Failure Modes**
>
> *Technical*
> | What Went Wrong | Likelihood | Impact | Preventive Action |
> |---|---|---|---|
> | Data inconsistency during dual-write period — user updates split across old and new services | High | High | Implement event sourcing with a reconciliation job. Run dual-write in shadow mode for 2 weeks before cutover |
> | Undocumented columns cause data loss during migration — fields exist that no current code references but downstream systems depend on | Medium | High | Audit every column in the user table. Query production logs for any reads on "unknown" columns before migration |
> | Latency regression when new services add network hops | Medium | Medium | Set latency budget per service. Load test at 2x peak traffic before any traffic shift |
> | Service discovery/routing issues during incremental cutover | Medium | Medium | Canary routing at 1%, 5%, 25%, 50%, 100% with automatic rollback triggers |
>
> *People/Team*
> | What Went Wrong | Likelihood | Impact | Preventive Action |
> |---|---|---|---|
> | Key engineer leaves or goes on extended leave mid-migration | Low | High | Document all decisions in ADRs. Ensure no single person owns a critical path without a backup |
> | Junior engineer is blocked or underutilised because work is too senior-heavy | Medium | Low | Explicitly scope migration tooling and testing work appropriate for junior level. Pair with a senior |
> | Team burns out from 12 weeks of high-stakes migration work | Medium | Medium | Build in a "breather sprint" at week 8. Celebrate milestones visibly. No weekend work expectation |
>
> *Process*
> | What Went Wrong | Likelihood | Impact | Preventive Action |
> |---|---|---|---|
> | Scope creep — stakeholders want to "also improve" things during the migration | High | Medium | Establish a strict "migrate, don't improve" rule. Any improvements go to a post-migration backlog |
> | No clear rollback plan — a failure at week 8 and we can't go back | Medium | High | Define rollback criteria and a tested rollback procedure for every phase before starting that phase |
>
> *External*
> | What Went Wrong | Likelihood | Impact | Preventive Action |
> |---|---|---|---|
> | Downstream teams break because they were consuming internal APIs we didn't know about | Medium | High | Publish migration timeline 4 weeks ahead. Audit API access logs for unexpected consumers |
> | Production incident during migration consumes team capacity | Medium | Medium | Reduce on-call burden during migration weeks. Have a "migration pause" protocol if a P1 hits |
>
> **Top 3 Kill Risks**
> 1. **Data inconsistency during dual-write** — highest combined likelihood × impact. A data integrity issue during migration could force a halt and rollback.
> 2. **Undocumented schema dependencies** — we don't know what we don't know about 8 years of schema evolution.
> 3. **Scope creep** — "while we're in there" is the enemy of a clean migration.
>
> **Pre-Mortem Action Plan (Do Before Sprint 1)**
> 1. Full user table audit — document every column, its consumers, and its migration path (Owner: [Senior eng], Due: Week -1)
> 2. Write and test rollback procedures for each migration phase (Owner: [Tech lead], Due: Week 1)
> 3. Announce migration to all downstream teams, identify undocumented API consumers (Owner: [EM], Due: Week -2)
> 4. Establish "migrate, don't improve" ground rule with PM and stakeholders (Owner: [EM], Due: Week -1)
> 5. Set up dual-write shadow mode infrastructure (Owner: [Senior eng], Due: Week 2)

## Tuning Notes

- **Run as a team exercise:** This prompt works well as prep for a team pre-mortem session. Generate the list, then bring it to the team and ask "what did we miss?" The team will add the risks that only domain experts can see.
- **Short project (< 4 weeks):** Focus on top 5 failure modes only. Lightweight pre-mortems are better than skipping the exercise entirely.
- **Hardware/infrastructure project:** Add a "supply chain / procurement" failure category.
- **First time doing a pre-mortem:** Share the output and action plan with stakeholders. It builds confidence that you've thought through the risks, and it creates a paper trail if one of the predicted failures actually occurs.
