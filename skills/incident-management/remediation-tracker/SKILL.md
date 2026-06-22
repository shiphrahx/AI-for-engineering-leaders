---
name: remediation-tracker
description: >
  Produces a living remediation tracker from postmortem action items — a summary dashboard
  (totals, completion rate, overdue/at-risk counts), items grouped by status and theme with
  owner/due/blocker, a thematic view, a review cadence, escalation criteria, and a
  bottleneck recommendation. Use when the user says "track our action items", "remediation
  tracker", "are our postmortem follow-ups getting done", or pastes a list of action items
  with owners and due dates. Use this to drive open items to completion, not to write the
  postmortem itself (planning/incident-postmortem) or to find cross-incident patterns
  (incident-trend-analysis).
---

# Remediation Tracker

Turn scattered postmortem action items into a single tracked system with clear ownership, deadlines, and visibility — so fewer items fall through the cracks. The format matters less than the review cadence; build something the team will actually check.

## Inputs to gather

Gather these before writing. If any are missing, ask in a SINGLE batched question — never invent items, owners, due dates, or statuses. Mark unavailable fields as **Unknown** rather than assigning a default owner or date.

- **Action items** — each with description, source incident, priority (P0–P2), owner, due date, and current status
- **Current date** — to compute overdue/at-risk (ask if not provided; do not assume)
- **Known blockers** — dependencies or capacity constraints, if known

## Steps

1. Compute the **Dashboard** first: total items, and counts (with percentages) for completed, on track, at risk, and overdue — plus a flagged count of **P0 items overdue**.
2. Sort every item into a status bucket against the current date: **Overdue** (past due, incomplete), **At Risk** (in progress but slipping, or not started near the deadline), **On Track**, **Completed**.
3. **Overdue Items** table: item, source incident, priority, owner, due date, days overdue, blocker. Below it, write a plain-language risk call-out — especially if P0/P1 items addressing known incident categories are weeks overdue (we'd be writing a postmortem about something we already knew how to prevent).
4. **At Risk** and **On Track** tables: item, source, priority, owner, due, status. **Completed** table: item, source, completion date.
5. **Thematic View**: group items by theme (deploy safety, configuration, code fixes, monitoring/alerting, documentation, process) with per-theme total/done/overdue counts and a one-line key insight (e.g. which theme is the bottleneck).
6. **Review Cadence**: who reviews this and how often — weekly (rotation lead reviews items >7 days overdue), bi-weekly (EM with team leads to unblock/reprioritise), monthly (VP reviews completion rate and overdue P0s).
7. **Escalation Criteria**: thresholds for escalating an overdue item (e.g. P0 >14 days → VP; P1 >30 days → EM) and a kill rule (anything >60 days overdue → reprioritise into the next sprint or explicitly close and accept the risk; zombie items erode trust in the postmortem process).
8. **Recommendation**: identify the owner/team carrying a disproportionate share (the bottleneck) and offer concrete unblocking options (dedicate capacity, reassign documentation-type items, bring in help).
9. Adapt to context as a sub-step: this format works in a spreadsheet, Notion, or Jira — pick the tool the team actually checks; if there are 30+ open items, that's a prioritisation problem — force-rank and cut below the top ~15; when a high-priority item completes, recommend announcing it and tying it to the incident it prevents, to close the loop.
10. Assemble the output in the format below.

## Output format

```
**Incident Remediation Tracker — As of [date]**

**Dashboard**
| Metric | Value |
|--------|-------|
| Total items | [n] |
| Completed | [n] ([%]) |
| On track | [n] ([%]) |
| At risk | [n] ([%]) |
| Overdue | [n] ([%]) |
| **P0 items overdue** | **[n]** ⚠️ |

**🔴 Overdue Items**
| Item | Source | Priority | Owner | Due | Days Overdue | Blocker |
|------|--------|----------|-------|-----|--------------|---------|
[risk call-out paragraph]

**🟡 At Risk**
| Item | Source | Priority | Owner | Due | Status |

**🟢 On Track**
| Item | Source | Priority | Owner | Due | Status |

**✅ Completed**
| Item | Source | Completed |

**Thematic View**
| Theme | Total | Done | Overdue | Key Insight |

**Review Cadence**
- Weekly / Bi-weekly / Monthly: [who reviews what]

**Escalation Criteria**
- [P0 overdue > X days → ...; kill rule at 60 days]

**Recommendation**
[Bottleneck + concrete unblocking options]
```

## Boundaries

- Never invent action items, owners, due dates, or statuses, and never assign an owner who wasn't named — mark **Unknown**.
- Never compute overdue/at-risk without a confirmed current date — ask for it.
- Never silently keep zombie items alive; force a decision at the kill threshold (reprioritise or explicitly accept the risk).
- Never inflate or deflate completion rates to manage perception — report the real numbers.

## Chaining

- No natural successor — this is a living tracker reviewed on a cadence rather than a one-shot artifact. Upstream, it's fed by **planning/incident-postmortem** (which generates the action items) and **incident-trend-analysis** (which surfaces systemic recommendations to track).
