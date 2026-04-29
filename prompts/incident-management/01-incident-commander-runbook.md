# Incident Commander Runbook

## Situation

You've been paged as Incident Commander (IC). You need a structured framework for running the incident — triaging, coordinating, communicating, and driving to resolution — without losing track of the big picture while others debug.

## The Prompt

```
You are an engineering leader creating an Incident Commander runbook for your organisation. The IC's job is NOT to fix the problem — it's to coordinate the response, manage communication, and make decisions. The runbook should be usable by anyone on the rotation, including engineers who've never been IC before.

Structure:
1. **First 5 minutes** — immediate actions upon being paged
2. **Triage** — how to assess severity and decide response level
3. **Coordination** — how to run the war room and assign roles
4. **Communication cadence** — who to update, how often, through what channels
5. **Decision framework** — when to escalate, when to roll back, when to declare resolved
6. **Post-incident handoff** — what to do immediately after resolution

Organisation context:
- Team size: [TEAM_SIZE]
- On-call structure: [ON_CALL_STRUCTURE]
- Communication tools: [TOOLS]
- Key services: [SERVICES]
- Existing severity levels: [SEVERITY_LEVELS]
```

## Example Input

```
- Team size: 45 engineers across 6 teams
- On-call structure: Primary and secondary on-call per team, rotating weekly. IC rotation is separate (senior engineers and EMs).
- Communication tools: Slack (#incidents channel), PagerDuty, Statuspage, Zoom for war rooms
- Key services: API gateway, payment processing, user authentication, notification service, data pipeline
- Severity levels: P0 (full outage), P1 (major feature degraded), P2 (minor feature degraded), P3 (cosmetic/low impact)
```

## Example Output

> **Incident Commander Runbook**
>
> ---
>
> **First 5 Minutes — You've Been Paged**
>
> 1. **Acknowledge the page** in PagerDuty within 2 minutes
> 2. **Open #incidents in Slack.** Post: "IC online. Assessing. Stand by for severity call." This tells everyone you're engaged.
> 3. **Read the alert context.** What service? What metric? When did it start? What's the blast radius?
> 4. **Check Statuspage and Datadog.** Is this already known? Is it a cascade from something else?
> 5. **Make a severity call** within 5 minutes (see Triage below). Don't overthink it — you can re-classify later. It's better to over-classify and scale down than under-classify and scramble.
>
> ---
>
> **Triage — Severity Assessment**
>
> Ask these questions in order:
>
> | Question | If Yes → |
> |----------|----------|
> | Are customers unable to use the product at all? | **P0** — full outage |
> | Is a revenue-critical flow broken (payments, signups, core feature)? | **P1** — major degradation |
> | Is a non-critical feature broken or significantly degraded? | **P2** — minor degradation |
> | Is this cosmetic, low-traffic, or internal-only? | **P3** — low impact |
>
> **Response level by severity:**
> - **P0:** War room immediately. All relevant on-calls engaged. Exec notification within 15 minutes. Statuspage updated within 10 minutes.
> - **P1:** War room within 10 minutes. Primary on-call for affected service engaged. Statuspage updated within 20 minutes.
> - **P2:** Async coordination in #incidents. On-call investigates. No war room unless it escalates.
> - **P3:** Ticket created, handled in normal sprint flow. No IC coordination needed.
>
> ---
>
> **Coordination — Running the Response**
>
> **Assign roles immediately.** You need three people, not twenty.
>
> | Role | Who | Responsibility |
> |------|-----|---------------|
> | **IC (you)** | Incident Commander | Coordinate, communicate, make decisions. Do NOT debug. |
> | **Tech Lead** | Strongest debugger for the affected service | Diagnose and fix. Narrates their findings to IC. |
> | **Comms Lead** | Anyone available (EM, senior eng) | Updates Statuspage, drafts customer comms, handles internal updates |
>
> **War room rules:**
> - Keep the Zoom/Slack thread focused. Side conversations go elsewhere.
> - Tech Lead narrates what they're trying and what they're seeing. IC listens and asks clarifying questions.
> - IC makes the calls: "Roll back," "Try the fix," "Escalate to the database team."
> - Every 15 minutes, IC posts a summary to #incidents: what we know, what we're trying, next update ETA.
>
> **If you're stuck:**
> - "What changed in the last 2 hours?" (deploys, config changes, traffic patterns)
> - "Can we roll back the last deploy?"
> - "Is there a workaround that restores service while we debug the root cause?"
> - "Who else has context on this system?" (page them)
>
> ---
>
> **Communication Cadence**
>
> | Audience | Channel | P0 Frequency | P1 Frequency |
> |----------|---------|-------------|-------------|
> | Engineering team | #incidents Slack | Every 15 min | Every 30 min |
> | Customers | Statuspage | Every 15 min | Every 30 min |
> | Executives | #exec-incidents Slack or DM | Every 30 min | At start and resolution |
> | Customer Success / Sales | #cs-alerts Slack | Every 30 min | At start and resolution |
>
> **Update template (copy-paste and fill):**
> ```
> 🔴 Incident Update — [TIME]
> Status: [INVESTIGATING / IDENTIFIED / MITIGATING / RESOLVED]
> Impact: [What customers are experiencing]
> Current action: [What we're doing right now]
> Next update: [Time of next update]
> ```
>
> ---
>
> **Decision Framework**
>
> **When to roll back:**
> - You've identified a recent deploy as the likely cause AND rollback is safe (no data migrations in the deploy)
> - You've been investigating for 20+ minutes with no root cause AND a rollback is available
> - Default: roll back first, debug second. Restoring service is always the priority.
>
> **When to escalate:**
> - The affected system is outside your team's domain and the on-call for that team isn't responding
> - You've been in the war room for 45+ minutes with no progress
> - The incident scope is expanding (more services affected, customer data potentially impacted)
> - **Escalation path:** Page the Engineering Manager for the affected team → VP Engineering → CTO
>
> **When to declare resolved:**
> - The root cause is fixed OR a stable workaround is in place
> - Monitoring confirms metrics have returned to baseline for at least 15 minutes
> - The Tech Lead confirms the fix is holding
> - IC posts final update to all channels: impact summary, duration, follow-up plan
>
> ---
>
> **Post-Incident Handoff (do within 1 hour of resolution)**
>
> 1. Post a final summary to #incidents with: duration, impact, root cause (if known), and who's writing the postmortem
> 2. Update Statuspage to "Resolved" with a brief customer-facing summary
> 3. Create a postmortem document from the template (link to Planning #11) and assign an author (usually the Tech Lead)
> 4. Schedule the postmortem review meeting within 3 business days
> 5. Thank everyone who helped. Publicly, in the channel. This matters more than you think.
> 6. If it's late at night: go to bed. The postmortem can wait until tomorrow. The retrospective is not urgent.

## Tuning Notes

- **Small team (< 15 engineers):** Combine IC and Comms Lead into one role. The Tech Lead debugs; you do everything else.
- **First-time IC:** Print this runbook. Literally. Having it on paper next to you during a 3am incident removes cognitive load when you're stressed.
- **Distributed/remote team:** Default to a Slack thread over Zoom for P1s. War rooms work better for P0s where real-time verbal communication is faster.
- **Regulated industry (fintech, healthcare):** Add a "Regulatory notification" step to the communication cadence. Some incidents require notifying regulators within specific timeframes.
