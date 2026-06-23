---
name: exec-status-update
description: >
  Produces a concise weekly/bi-weekly executive status update — health indicator, top-line
  summary, business-framed wins, severity-rated risks with mitigations, decisions needed, and
  next-week focus — synthesized from raw team-lead updates. Use when the user says "write my
  exec update", "weekly status for my VP/CTO", "synthesize these team updates", or pastes a mix
  of Slack messages, doc bullets, and Jira summaries. Use this for an internal leadership-up
  update across a team or org — use board-engineering-summary for investor-level board sections,
  and stakeholder-project-update for cross-functional PM/design/business audiences.
---

# Exec Status Update

Synthesize messy team-lead updates into a crisp leadership update an executive can read in two minutes — leading with whether we're on track, what the risk is, and what's needed from them, framed in business impact rather than technical output.

## Inputs to gather

Gather these before writing. If any are missing, ask for them in a single batched question — never invent an org name, headcount, goal, metric, or status. Mark anything genuinely unavailable as **Unknown** in the output.

- **Org context** — org/team name, number of teams, engineer headcount
- **Quarter goals** — the current goals the update tracks against
- **Audience** — recipient's role (direct manager, VP, CTO, board) and what they care about (delivery timelines, headcount efficiency, customer impact)
- **Raw updates** — team-lead notes in whatever form (Slack, bullets, Jira), plus any metrics and blockers
- **Asks** — anything needed from leadership this period

## Steps

1. Read all raw updates fully before writing. Separate signal (progress, risk, decisions) from noise (status chatter, social detail).
2. Set a **health indicator** with a one-line reason: 🟢 Green (on track, no significant risk), 🟡 Yellow (minor delays/risks being managed), 🔴 Red (significant risk to timeline/scope/quality, needs leadership attention). When unsure between Yellow and Red, err toward transparency.
3. Write a **top-line summary** (2-3 sentences): on track, behind, or ahead against the quarter goals? Name how many of N goals are tracking. Front-load the headline — status first, detail second.
4. Extract **key wins** (3-5 bullets) as outcomes, not activity: "Shipped X, reducing Y from A to B" not "Worked on X". Emphasize business impact over technical output; quantify wherever possible.
5. Surface **risks & blockers**, each rated 🟢 / 🟡 / 🔴, stating the timeline/customer impact and what is being done about it — every blocker includes a mitigation.
6. List **decisions needed** — anything required from leadership — each with a clear recommendation and one-line rationale. Make asks specific and actionable ("3 days behind" not "slightly delayed"). If nothing is needed, say "None this week".
7. State **next week focus** per team or workstream.
8. Adapt to context: for a **board/C-suite audience**, strip technical detail and lead with metrics tied to company goals (translate "serialisation rewrite" → "backend optimisation to improve response times"). For a **skip-level**, frame more strategically with less tactical detail. For a **Slack-first culture**, cut to summary + risks only and link a doc. For a **bad week**, do not bury bad news — move Risks above Wins and lead the summary with the blocker. For **large orgs (10+ teams)**, group by theme (delivery, reliability, platform) rather than per-team.
9. Assemble the output in the format below.
10. Run the validator:
   ```
   python scripts/validate.py "$(cat draft.md)"
   ```
   Fix every listed failure. Re-run until PASS. Do not return output to the user until the script exits 0.

Run the script. Fix every failure. Do not return output until the script passes.

## Output format

```
**[Org/Team] Status — [Week/Date]**

**Health: 🟢/🟡/🔴 [GREEN/YELLOW/RED]** — [One sentence why]

**Summary:** [2-3 sentences: on track / behind / ahead against goals; flag the one thing that needs escalation.]

**Key Wins**
- [Outcome-focused, business-framed, quantified where possible]
- [...]

**Risks & Blockers**
- 🟢/🟡/🔴 **[Risk]:** [Timeline/customer impact] — *Mitigation:* [what's being done]
- [...]

**Decisions Needed**
- **[Decision]:** [Options.] *Recommendation: [action] — [one-line rationale].*
(or "None this week")

**Next Week Focus**
- [Team/workstream]: [priority]
```

## Boundaries

- Never fabricate org details, headcount, goals, metrics, owners, or status — mark anything unavailable as **Unknown**.
- Never verify or vouch for metric accuracy; the user supplies reliable data — surface, don't invent, numbers.
- Never inflate a win or soften a risk to manage the reader's mood — leadership acts on this; distortion costs trust.
- Never leave a "decision needed" without a recommendation, or a risk without a mitigation.
- Never include raw technical detail an executive can't act on — translate it or cut it.

## Chaining

- After this, offer **board-engineering-summary** when the same period needs an investor-level board section.
- This is often assembled from per-team inputs produced by **team-weekly-summary**.
