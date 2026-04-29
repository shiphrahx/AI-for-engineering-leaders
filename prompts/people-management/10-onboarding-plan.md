# Onboarding Plan

## Situation

A new hire is starting in two weeks and you want them set up for success — not just with access and tools, but with a structured path to their first meaningful contribution. A good onboarding plan reduces time-to-productivity and makes the new hire feel welcome and oriented.

## The Prompt

```
You are an engineering manager creating a 30/60/90-day onboarding plan for a new engineering hire. The plan should balance learning (codebase, architecture, processes) with doing (shipping something real, building relationships). Every week should have clear goals so the new hire always knows what "good" looks like.

Structure:
- **Pre-day-one** — what to prepare before they start
- **Week 1** — orientation, setup, first codebase exploration
- **Weeks 2-4 (30 days)** — first contribution, key relationships, process understanding
- **Weeks 5-8 (60 days)** — independent work, deeper technical context, first project ownership
- **Weeks 9-12 (90 days)** — full contributor, feedback loop, career conversation

New hire: [NAME], [ROLE], [LEVEL]
Team: [TEAM_NAME], [TEAM_SIZE]
Key systems: [SYSTEMS_THEY_WILL_WORK_ON]
Onboarding buddy: [BUDDY_NAME]
First project: [PLANNED_FIRST_PROJECT]
```

## Example Input

```
New hire: Elena, Backend Engineer, L4 (mid-level)
Team: Notifications team, 5 engineers
Key systems: Notification service (Go), email delivery pipeline (SQS + Lambda), SMS gateway, user preference service
Onboarding buddy: Omar (Senior Engineer)
First project: Add support for in-app notification preferences (users can choose which notification types they receive in-app vs email vs SMS)
```

## Example Output

> **Onboarding Plan: Elena — Backend Engineer, Notifications Team**
>
> **Pre-Day-One**
> - [ ] Laptop configured with dev environment, VPN, and required access
> - [ ] Accounts created: GitHub, Jira, Slack, AWS (read-only), Datadog
> - [ ] Onboarding buddy (Omar) briefed on the plan and first-week schedule
> - [ ] Welcome message sent to team Slack channel
> - [ ] First-week calendar loaded: 1:1s with each team member, architecture walkthrough, first standup
> - [ ] "Starter ticket" prepared (small, well-scoped, real — not a toy)
>
> ---
>
> **Week 1: Orient and Connect**
> *Goal: Elena knows the team, can run the codebase locally, and has merged her first PR.*
>
> - Day 1: Welcome session with manager. Team introductions. Set up dev environment (Omar pairing).
> - Day 2: Architecture walkthrough — notification service, email pipeline, SMS gateway. Whiteboard session with Omar.
> - Day 3: Read team's top 5 ADRs and runbooks. Shadow a code review.
> - Day 4: Pick up starter ticket (e.g., add a new notification template). Pair with Omar if needed.
> - Day 5: Submit first PR. 1:1 with manager — check in on experience so far, answer questions.
>
> **Success at Day 5:** Can explain the notification service architecture at a high level. Has merged one PR. Knows everyone's name and what they work on.
>
> ---
>
> **Weeks 2-4: First Real Contribution**
> *Goal: Elena completes 2-3 meaningful tickets independently and understands team processes.*
>
> - Week 2: Complete 1-2 tickets from the backlog (scoped by manager). Start attending sprint ceremonies. 1:1 with PM to understand product context.
> - Week 3: Start exploring the in-app preferences project — read the spec, review the relevant code, write questions. Pair with Omar on a related area of the codebase.
> - Week 4: Begin initial design for the in-app preferences feature (small design doc or RFC). Present to the team for feedback.
>
> Key relationships to build: PM (product context), QA engineer (testing expectations), on-call lead (operational context).
>
> **Success at Day 30:** Shipped 3+ PRs independently. Can navigate the codebase without hand-holding. Has a draft design for the first project. Feels comfortable asking questions and participating in team discussions.
>
> ---
>
> **Weeks 5-8: Independent Delivery**
> *Goal: Elena is delivering the in-app preferences project and beginning to operate like a full team member.*
>
> - Weeks 5-6: Build the in-app preferences feature — implement the backend, write tests, work with frontend engineer on the integration.
> - Week 7: Code review and testing. Fix bugs. Deploy to staging.
> - Week 8: Ship to production. Write deployment notes. Join the on-call shadow rotation for one cycle.
>
> **Success at Day 60:** First project shipped to production. Participates in code reviews as both author and reviewer. Has shadowed on-call and understands the incident process. Comfortable with the deploy pipeline.
>
> ---
>
> **Weeks 9-12: Full Contributor**
> *Goal: Elena is picking up work independently, contributing to planning, and starting to think about growth.*
>
> - Weeks 9-10: Pick up a second project from the backlog (self-selected or manager-suggested). Start contributing to sprint planning with estimates and technical input.
> - Week 11: Write or update one piece of documentation (runbook, architecture doc, or README). This solidifies knowledge and helps the next new hire.
> - Week 12: 90-day career conversation with manager — how's the role matching expectations? What are Elena's growth goals for the next 6 months?
>
> **Success at Day 90:** Operating as a fully independent L4 contributor. Has shipped 2+ features. Is in the on-call rotation. Has identified at least one area of the system she wants to go deeper on. Feels like a full member of the team, not "the new person."
>
> ---
>
> **Ongoing Support**
> - Weekly 1:1s with manager (30 min) — more coaching-focused in the first 60 days
> - Bi-weekly pairing sessions with Omar through the first 90 days
> - 30-day, 60-day, and 90-day check-ins with structured feedback in both directions

## Tuning Notes

- **Senior hire (L5+):** Accelerate the timeline. By day 30 they should be leading a project, not just contributing. Give them more autonomy and less hand-holding, but don't skip the relationship-building.
- **Junior hire (L3):** Extend the "guided" phase to 60 days. More pairing, smaller tickets, more frequent check-ins. Assign a mentor (not just a buddy).
- **Remote new hire:** Over-invest in the social/relationship parts. Schedule virtual coffees with every team member. Consider flying them in for week 1 if budget allows.
- **Existing employee transferring teams:** Skip the company orientation but don't skip the team onboarding. "I know how the company works" doesn't mean "I know how this team and codebase work."
