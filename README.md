# AI for Engineering Leaders — Prompt Library

A curated collection of battle-tested prompts for engineering managers, directors, and VPs who use AI to move faster without losing quality.

## The Problem

Engineering leaders spend 60%+ of their time on communication, planning, and people work — not building. Most of that work follows patterns: the weekly status update, the quarterly roadmap, the performance review. These patterns are perfect for AI augmentation, but generic prompts produce generic output.

This library gives you **situation-specific prompts** designed for the way engineering leaders actually work.

## Before & After

**Without this library** — You open Claude, type "help me write a status update," get a vague template, spend 20 minutes re-editing it to match your org's expectations.

**With this library** — You grab the exec status update prompt, paste in your team leads' raw updates, and get a draft that's structured for your VP audience with risks surfaced and metrics highlighted. Five minutes, done.

---

## 📂 Prompt Categories

### [Weekly Comms](prompts/weekly-comms/) — 12 prompts
The communication layer of leadership. Status updates, stakeholder emails, launch announcements, incident comms, and more.

| # | Prompt | When to Use |
|---|--------|-------------|
| 01 | [Exec Status Update](prompts/weekly-comms/01-exec-status-update.md) | Monday morning, synthesising team leads' updates for your VP/CTO |
| 02 | [Team Weekly Summary](prompts/weekly-comms/02-team-weekly-summary.md) | Friday wrap-up for your direct team |
| 03 | [Stakeholder Project Update](prompts/weekly-comms/03-stakeholder-project-update.md) | Keeping PMs, design, and business leads aligned on delivery |
| 04 | [Cross-Team Dependency Update](prompts/weekly-comms/04-cross-team-dependency-update.md) | Flagging blockers and handoffs across teams |
| 05 | [Internal Launch Announcement](prompts/weekly-comms/05-launch-announcement-internal.md) | Announcing a shipped feature or service to the company |
| 06 | [External Launch Announcement](prompts/weekly-comms/06-launch-announcement-external.md) | Customer-facing or public comms for a release |
| 07 | [Team Wins Celebration](prompts/weekly-comms/07-team-wins-celebration.md) | Highlighting team accomplishments to leadership and peers |
| 08 | [Org Change Announcement](prompts/weekly-comms/08-org-change-announcement.md) | Communicating reorgs, new hires, or structural shifts |
| 09 | [Incident Stakeholder Comms](prompts/weekly-comms/09-incident-stakeholder-comms.md) | Real-time or post-incident updates for non-technical stakeholders |
| 10 | [Meeting Recap & Action Items](prompts/weekly-comms/10-meeting-recap-action-items.md) | Turning messy meeting notes into clear follow-ups |
| 11 | [Skip-Level Update](prompts/weekly-comms/11-skip-level-update.md) | Writing upward comms for your boss's boss |
| 12 | [Board Engineering Summary](prompts/weekly-comms/12-board-engineering-summary.md) | Distilling engineering progress for board-level audiences |

### [Planning Artifacts](prompts/planning/) — 12 prompts
The documents that shape what gets built and when. Roadmaps, RFCs, retros, decision records, and operational playbooks.

| # | Prompt | When to Use |
|---|--------|-------------|
| 01 | [Quarterly Roadmap](prompts/planning/01-quarterly-roadmap.md) | Start of quarter, turning goals into a structured plan |
| 02 | [RFC Outline](prompts/planning/02-rfc-outline.md) | Proposing a technical change that needs cross-team buy-in |
| 03 | [Sprint Retro Summary](prompts/planning/03-sprint-retro-summary.md) | Turning retro discussion into actionable themes |
| 04 | [Tech Debt Prioritisation](prompts/planning/04-tech-debt-prioritisation.md) | Building a case for paying down debt with a ranked backlog |
| 05 | [Build vs Buy Analysis](prompts/planning/05-build-vs-buy-analysis.md) | Evaluating whether to build in-house or use a vendor |
| 06 | [Project Pre-Mortem](prompts/planning/06-project-pre-mortem.md) | Identifying risks before a project starts |
| 07 | [Capacity Planning](prompts/planning/07-capacity-planning.md) | Mapping team bandwidth against committed work |
| 08 | [Migration Plan](prompts/planning/08-migration-plan.md) | Structuring a phased approach to a system migration |
| 09 | [OKR Drafting](prompts/planning/09-okr-drafting.md) | Writing measurable OKRs from vague business goals |
| 10 | [Architecture Decision Record](prompts/planning/10-architecture-decision-record.md) | Documenting a technical decision with context and trade-offs |
| 11 | [Incident Postmortem](prompts/planning/11-incident-postmortem.md) | Writing a blameless postmortem from timeline notes |
| 12 | [Sprint Planning Breakdown](prompts/planning/12-sprint-planning-breakdown.md) | Breaking epics into well-scoped sprint tickets |

### [People Management](prompts/people-management/) — 12 prompts
The human side of leadership. Reviews, career conversations, hiring, and the difficult moments.

| # | Prompt | When to Use |
|---|--------|-------------|
| 01 | [Performance Review Draft](prompts/people-management/01-performance-review-draft.md) | Review cycle, synthesising a half or full year of work |
| 02 | [One-on-One Prep](prompts/people-management/02-one-on-one-prep.md) | Before your weekly 1:1 with a direct report |
| 03 | [Feedback Synthesis](prompts/people-management/03-feedback-synthesis.md) | Combining peer feedback into a coherent narrative |
| 04 | [Career Ladder Draft](prompts/people-management/04-career-ladder-draft.md) | Creating or refining engineering level expectations |
| 05 | [Job Description](prompts/people-management/05-job-description.md) | Writing a compelling, specific job posting |
| 06 | [Interview Rubric](prompts/people-management/06-interview-rubric.md) | Creating structured evaluation criteria for interviews |
| 07 | [PIP Documentation](prompts/people-management/07-pip-documentation.md) | Drafting a fair, clear performance improvement plan |
| 08 | [Promotion Case](prompts/people-management/08-promotion-case.md) | Building a compelling case for a direct report's promotion |
| 09 | [Team Health Survey Analysis](prompts/people-management/09-team-health-survey-analysis.md) | Finding patterns and actions from survey results |
| 10 | [Onboarding Plan](prompts/people-management/10-onboarding-plan.md) | Creating a structured first 30/60/90 days for a new hire |
| 11 | [Skip-Level Meeting Prep](prompts/people-management/11-skip-level-meeting-prep.md) | Preparing for 1:1s with your reports' reports |
| 12 | [Difficult Conversation Prep](prompts/people-management/12-difficult-conversation-prep.md) | Structuring hard feedback or sensitive discussions |

---

## 🧱 Prompt Structure

Every prompt in this library follows a consistent format:

```
## Situation        — When you'd reach for this prompt
## The Prompt       — Copy-paste ready, with [PLACEHOLDERS]
## Example Input    — Realistic data you'd paste in
## Example Output   — What the AI produces (so you can calibrate)
## Tuning Notes     — How to adjust for your context
```

---

## 🚀 Getting Started

1. **Browse by situation** — scan the tables above, find what matches your current task
2. **Copy the prompt** — each file has a ready-to-use prompt with clear placeholders
3. **Paste your context** — replace `[PLACEHOLDERS]` with your real data
4. **Review and adjust** — use the tuning notes to tailor the output

---

## 🗺️ Roadmap

- [x] V1: 36 prompts across comms, planning, and people management
- [ ] V2: CLI tool via Claude Code (`ai-eng fetch postmortem --timeline "..."`)
- [ ] V2: Additional categories (incident management, architecture, hiring pipelines)
- [ ] V3: Prompt chaining (multi-step workflows)
- [ ] V3: Org-size variants (startup, growth, enterprise)

