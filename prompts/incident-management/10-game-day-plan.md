# Game Day Plan

## Situation

You want to test your team's incident response before a real incident forces you to. A game day (also called chaos engineering exercise or incident simulation) lets you find gaps in runbooks, monitoring, and team coordination in a safe environment.

## The Prompt

```
You are an engineering leader planning a game day exercise to test your team's incident response capability. The exercise should feel realistic enough to surface real gaps but controlled enough to not cause actual customer impact. Design the scenario, the rules of engagement, and the evaluation criteria.

Structure:
1. **Objective** — what you're testing and what you hope to learn
2. **Scenario** — the simulated incident, including how it will be triggered
3. **Rules of engagement** — safety boundaries, who knows it's a drill, blast radius limits
4. **Roles** — who participates and in what capacity
5. **Timeline** — exercise schedule with milestones
6. **Evaluation criteria** — what you're measuring and what "good" looks like
7. **Debrief plan** — how to review the exercise and capture learnings

Team: [TEAM_NAME]
Systems to test: [SYSTEMS]
Last game day: [WHEN_OR_NEVER]
Known gaps: [SUSPECTED_WEAKNESSES]
```

## Example Input

```
Team: Platform Engineering, 8 engineers + 3 SREs
Systems: API gateway, primary database, cache layer (Redis), notification service
Last game day: Never — this is our first one
Known gaps: We suspect our database failover hasn't been tested in production in 6+ months, our runbooks are outdated, and half the team has never been IC
```

## Example Output

> **Game Day Plan: Database Failover Simulation**
>
> **Objective**
> Test our team's ability to detect, diagnose, and recover from a primary database failure. Specifically:
> - Does our monitoring detect the failure before customers report it?
> - Can the on-call follow the failover runbook successfully?
> - Does the application recover gracefully after failover?
> - How long does the full cycle take?
>
> **Scenario**
> Simulate a primary database becoming unresponsive. We'll trigger this by promoting the read replica to primary in a controlled manner that mimics a real failure.
>
> *Injection method:* At the scheduled time, the Game Day Controller will modify the primary database's security group to block application connections (port 5432). This simulates the database becoming unreachable without actually breaking it. The database itself stays healthy — only the network path is disrupted.
>
> *Expected cascade:*
> 1. Application connections to primary fail → API errors begin
> 2. Monitoring alerts fire (expected: within 2 minutes)
> 3. On-call is paged, investigates, identifies DB connectivity as the issue
> 4. On-call follows failover runbook to promote the replica
> 5. Application reconnects to the new primary
> 6. Service recovers
>
> **Rules of Engagement**
> - ✅ Run during low-traffic hours (Tuesday 10am, after morning peak)
> - ✅ Game Day Controller can abort at any time by reverting the security group change
> - ✅ All engineers and EMs know this is a drill (first game day — no surprise exercises)
> - ✅ CS team informed in advance to handle any customer questions
> - ❌ No changes to production data. The simulation is network-level only.
> - ❌ If a real incident occurs during the exercise, immediately abort the game day
> - ❌ Maximum exercise duration: 45 minutes. If not resolved by then, Controller aborts.
>
> **Roles**
> | Role | Person | Responsibility |
> |------|--------|---------------|
> | Game Day Controller | [SRE Lead] | Triggers the simulation, monitors safety, can abort |
> | On-Call (participant) | [Assigned on-call] | Responds as if this is a real incident. Follows normal process. |
> | IC (participant) | [IC rotation member] | Runs incident response. This is practice for them. |
> | Observers | [Remaining team] | Watch, take notes, don't help unless asked. Note where the process breaks down. |
> | Safety Monitor | [EM] | Watches real customer metrics. If real customers are impacted beyond expected thresholds, calls for abort. |
>
> **Timeline**
> | Time | Event |
> |------|-------|
> | T-30min | Pre-brief: remind everyone of the plan, confirm roles, verify abort procedure |
> | T-10min | Controller confirms: low-traffic window, no real incidents in progress, all participants ready |
> | T-0 | Controller triggers the simulation (blocks DB connections) |
> | T+2min | Expected: monitoring alerts fire |
> | T+5min | Expected: on-call acknowledges and begins investigation |
> | T+15min | Check-in: has the on-call identified the DB issue? If not, observer can hint. |
> | T+30min | Expected: failover complete, service recovering |
> | T+45min | Hard stop. Controller aborts if not resolved. |
> | T+60min | Debrief begins |
>
> **Evaluation Criteria**
> | What We're Measuring | Target | Actual (fill in) |
> |---------------------|--------|-------------------|
> | Time to detection (alert fires) | < 3 minutes | |
> | Time to acknowledgement (on-call responds) | < 5 minutes | |
> | Time to diagnosis (identifies DB as root cause) | < 15 minutes | |
> | Time to resolution (failover complete, service restored) | < 30 minutes | |
> | Runbook accuracy — could on-call follow it step-by-step? | Yes / No | |
> | Monitoring coverage — did the right alerts fire? | All expected alerts fire | |
> | Communication — were stakeholders updated per the process? | Updates at expected intervals | |
> | Any unexpected side effects (cache stampede, connection storms)? | None | |
>
> **Debrief Plan (immediately after exercise)**
> 1. Round-robin: each participant shares their experience (5 min each)
> 2. Review evaluation criteria results together
> 3. Identify the top 3 gaps found (runbook issues, monitoring gaps, process confusion)
> 4. Create action items for each gap with owners and deadlines
> 5. Decide: what's the next game day scenario? (suggestion: cache layer failure or API gateway overload)
> 6. Document everything and share with the broader eng org — transparency builds credibility

## Tuning Notes

- **First game day:** Keep it simple. One failure mode, during business hours, everyone knows it's a drill. Build confidence before adding complexity.
- **Experienced team:** Make it harder. Don't announce the exact scenario. Inject a second failure midway through. Add a "customer escalation" role who messages the IC with panicked customer reports.
- **Production concerns:** If you're not comfortable simulating in production, run the exercise against staging with a realistic traffic load. It's less realistic but still valuable for testing process and runbooks.
- **Frequency:** Quarterly is ideal. Monthly is great if your team is large enough. The goal is that incident response becomes muscle memory, not a once-a-year event.
