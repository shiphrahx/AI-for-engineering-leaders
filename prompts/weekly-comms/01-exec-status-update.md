# Exec Status Update

## Situation

It's Monday morning. Your team leads have sent you their weekly updates — a mix of Slack messages, bullet points in docs, and half-finished Jira summaries. You need to synthesise these into a crisp update for your VP or CTO that surfaces what matters: progress against goals, risks, and decisions needed.

## The Prompt

```
You are a senior engineering leader preparing a weekly status update for executive leadership.

Synthesise the following raw updates from my team leads into a concise executive status update. Structure it as:

1. **Top-line summary** (2-3 sentences: are we on track, behind, or ahead?)
2. **Key wins this week** (3-5 bullets, emphasise business impact not just technical output)
3. **Risks & blockers** (flag anything that could affect timelines, with severity: 🟢 managed / 🟡 needs attention / 🔴 escalation needed)
4. **Decisions needed** (anything you need from leadership, with a recommended action)
5. **Next week focus** (what the teams are prioritising)

Context:
- My org: [ORG_NAME], [TEAM_COUNT] teams, [HEADCOUNT] engineers
- Current quarter goals: [Q_GOALS]
- Audience: [AUDIENCE_ROLE] — they care about delivery timelines, headcount efficiency, and customer impact

Raw updates from team leads:
[PASTE_RAW_UPDATES]
```

## Example Input

```
- My org: Platform Engineering, 4 teams, 28 engineers
- Current quarter goals: Ship auth v2, reduce API latency p99 < 200ms, migrate 3 services to K8s
- Audience: VP of Engineering — cares about delivery timelines and customer-reported incidents

Raw updates from team leads:

Team Auth (Sarah): Finished OIDC integration, in QA now. Found edge case with enterprise SSO 
that might push launch by 3-5 days. Need decision on whether to ship without enterprise SSO 
and patch later. One engineer out sick, didn't affect sprint.

Team Perf (Marcus): p99 latency down to 240ms from 310ms last week. Main bottleneck is the 
legacy serialisation layer — rewrite is 60% done. Should hit 200ms target by end of Q. 
Might need to borrow a senior eng from another team for 2 weeks.

Team Infra (Priya): Migrated payments service to K8s (service 1 of 3). Monitoring looks clean 
after 48hrs. Starting on notifications service next week. Blocked on DevOps team for 
production namespace config — filed ticket 3 days ago, no response.

Team DX (Jordan): Launched internal CLI tool for service scaffolding. 14 teams adopted in first 
week. Working on CI pipeline template library next. No blockers.
```

## Example Output

> **Platform Engineering — Weekly Update (W14)**
>
> **Summary:** Tracking well on 2 of 3 quarterly goals. Auth v2 is in QA with a potential 3-5 day slip on enterprise SSO; latency reduction is progressing steadily; K8s migration is 1/3 complete. One cross-team dependency needs escalation.
>
> **Key Wins**
> - Auth v2 OIDC integration complete and in QA — on track for customer-facing launch this quarter
> - API p99 latency reduced from 310ms → 240ms (target: 200ms), driven by serialisation layer rewrite
> - Payments service successfully migrated to K8s with clean monitoring after 48hrs
> - Internal CLI tool launched to 14 adopting teams in week one — accelerating developer velocity across the org
>
> **Risks & Blockers**
> - 🟡 Auth v2 enterprise SSO edge case may slip launch 3-5 days — team has a workaround proposal (see Decisions below)
> - 🟡 Latency team may need a senior engineer loan for 2 weeks to hit the Q target — Marcus assessing this week
> - 🔴 K8s migration blocked on DevOps namespace config — ticket open 3 days with no response, at risk of delaying service 2
>
> **Decisions Needed**
> - **Auth v2 SSO:** Ship without enterprise SSO support and patch within 2 weeks, or hold for full launch? *Recommendation: ship and patch — affects <5% of auth flows and unblocks the broader rollout.*
>
> **Next Week Focus**
> - Auth: Complete QA pass, prep for staged rollout
> - Perf: Finish serialisation rewrite (target: 80% complete)
> - Infra: Begin notifications service migration (pending DevOps unblock)
> - DX: CI pipeline template library — first 3 templates

## Tuning Notes

- **Board-level audience:** Remove technical detail, lead with metrics and customer impact. Replace "serialisation layer rewrite" with "backend optimisation to improve response times."
- **Slack-first culture:** Shorten dramatically — summary + risks only, link to a doc for detail.
- **Bad week:** Don't bury the bad news. Move Risks above Wins and lead the summary with the blocker.
- **Large orgs (10+ teams):** Group updates by theme (delivery, reliability, platform) rather than listing every team.
