# Team Wins Celebration

## Situation

You want to highlight your team's accomplishments to leadership and peers. This is visibility work — it builds morale, helps your reports get recognised, and ensures your team's impact isn't invisible.

## The Prompt

```
You are an engineering leader writing a "team wins" post to share with leadership and the broader engineering org. The goal is to make your team's impact visible and give individuals credit. Avoid generic praise — tie every win to a specific outcome.

Structure:
1. **Opening** — one-line framing of the week/sprint theme
2. **Wins** — 3-5 specific accomplishments, each with: what happened, who did it, and why it matters (business impact or technical significance)
3. **By the numbers** (optional) — any metrics that underscore impact
4. **Unsung hero** — one callout for work that's typically invisible (code reviews, mentoring, documentation, on-call saves)

Team: [TEAM_NAME]
Period: [TIME_PERIOD]

Wins to highlight:
[PASTE_RAW_WINS]
```

## Example Input

```
Team: Data Platform
Period: Sprint 22

Wins:
- Completed the migration of our analytics pipeline from Airflow to Dagster. 6 months of work, zero data loss during cutover. Hannah led the architecture, Evan handled the migration tooling.
- Reduced daily pipeline runtime from 4.5hrs to 1.8hrs by parallelising the transformation layer. Rajesh figured out the dependency graph optimisation.
- Onboarded 3 new data consumers (marketing, finance, product analytics) to the self-service query layer. Zero support tickets from any of them in the first week.
- Evan reviewed 47 PRs this sprint across 3 teams while maintaining his own delivery commitments.
```

## Example Output

> **Data Platform Wins — Sprint 22**
>
> Big sprint: we closed out a 6-month migration, nearly tripled our pipeline speed, and onboarded three new teams to self-service analytics — all without a single data incident.
>
> **Wins**
> - 🏆 **Airflow → Dagster migration complete.** Six months of planning and execution, zero data loss during cutover. Hannah designed the migration architecture and Evan built the tooling that made the cutover seamless. This gives us a modern orchestration layer that's significantly easier to maintain and extend.
> - ⚡ **Pipeline runtime: 4.5hrs → 1.8hrs.** Rajesh redesigned the transformation dependency graph to enable parallelisation. This means our stakeholders get fresh data before their morning standup instead of after lunch.
> - 📊 **3 new self-service consumers onboarded.** Marketing, finance, and product analytics are now running their own queries — and generated zero support tickets in their first week. That's a direct result of the documentation and guardrails the team built into the query layer.
>
> **By the Numbers**
> - 60% reduction in daily pipeline runtime
> - 0 data incidents during migration cutover
> - 0 support tickets from new self-service users
> - 47 PRs reviewed across 3 teams
>
> **Unsung Hero**
> Evan reviewed 47 PRs this sprint across three different teams while hitting all his own commitments. That kind of cross-team code review work is invisible in sprint metrics but directly improves code quality and unblocks other teams. Thanks, Evan.

## Tuning Notes

- **Slack format:** Shorten to emoji + one-liner per win. Save the narrative for monthly roundups.
- **Executive audience:** Lead with business metrics, drop the technical detail. "Pipeline now delivers data 2.5x faster, enabling same-day analytics for 3 new teams."
- **Quiet sprint:** Don't force wins. Highlight reliability ("zero incidents for 4th consecutive sprint"), learning (tech spikes, proof of concepts), or investment work (documentation, test coverage).
- **Remote teams:** Tag people's handles so the recognition reaches them directly in the channel.
