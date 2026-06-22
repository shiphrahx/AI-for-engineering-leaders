<div align="center">

<img src="assets/ai-robot.png" width="140" alt="AI for Engineering Leaders" />

# AI for Engineering Leaders — Prompt Library

![Prompts](https://img.shields.io/badge/prompts-81-blue) ![Skills](https://img.shields.io/badge/skills-69-orange) ![Categories](https://img.shields.io/badge/categories-6-green) ![License](https://img.shields.io/badge/license-MIT-lightgrey) [![GitHub Last Commit](https://img.shields.io/github/last-commit/shiphrahx/AI-for-engineering-leaders?style=flat-square&color=8b5cf6)](https://github.com/shiphrahx/AI-for-engineering-leaders/commits/main)

81 situation-specific **prompts** and 69 agent-ready **skills** for engineering managers, directors, and VPs.

- **[Prompts](prompts/)** — copy-paste-and-fill templates for recurring leadership tasks (status updates, roadmaps, reviews, incident comms), each with placeholders, an example, and tuning notes.
- **[Skills](skills/)** — the same expertise packaged so an agent (Claude Code, Copilot, Cursor, or any LLM) can *act*: gather inputs, apply structure, and produce the finished artifact. Portable plain-markdown files with a small YAML header.

</div>

## Prompt Categories

### [Weekly Comms](prompts/weekly-comms/) - 15 prompts
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
| 13 | [Engineering Newsletter](prompts/weekly-comms/13-engineering-newsletter.md) | Monthly or bi-weekly update for a non-technical company-wide audience |
| 14 | [Vendor Escalation Email](prompts/weekly-comms/14-vendor-escalation-email.md) | Escalating a blocked vendor issue in writing |
| 15 | [Engineering All-Hands Agenda](prompts/weekly-comms/15-engineering-all-hands-agenda.md) | Planning a quarterly or monthly all-hands meeting |

### [Planning Artifacts](prompts/planning/) - 14 prompts
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
| 13 | [Engineering Strategy One-Pager](prompts/planning/13-engineering-strategy-one-pager.md) | Communicating what you're optimising for and why, in one page |
| 14 | [Team Offsite Agenda](prompts/planning/14-team-offsite-agenda.md) | Planning a substantive team offsite that produces real decisions |

### [People Management](prompts/people-management/) - 16 prompts
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
| 13 | [Manager README](prompts/people-management/13-manager-readme.md) | Writing a working guide to yourself for your direct reports |
| 14 | [Layoff Communication](prompts/people-management/14-layoff-communication.md) | Individual and team messaging for a workforce reduction |
| 15 | [Team Values Workshop](prompts/people-management/15-team-values-workshop.md) | Facilitating a session to define real, usable team values |
| 16 | [Staff Engineer Scope Document](prompts/people-management/16-staff-engineer-scope-doc.md) | Defining what a staff engineer owns and how success is measured |

### [Incident Management](prompts/incident-management/) - 12 prompts
The operational backbone of engineering reliability. From alert fires through to organisational learning.

| # | Prompt | When to Use |
|---|--------|-------------|
| 01 | [Incident Commander Runbook](prompts/incident-management/01-incident-commander-runbook.md) | You're IC for a live incident and need a structured framework |
| 02 | [Real-Time Status Page Update](prompts/incident-management/02-real-time-status-page-update.md) | Writing public status updates during an active incident |
| 03 | [Customer Apology Email](prompts/incident-management/03-customer-apology-email.md) | Post-incident customer communication that rebuilds trust |
| 04 | [War Room Facilitation Guide](prompts/incident-management/04-war-room-facilitation-guide.md) | Running an effective incident response call |
| 05 | [On-Call Handoff](prompts/incident-management/05-on-call-handoff.md) | Handing off context at the start/end of an on-call rotation |
| 06 | [Runbook Generator](prompts/incident-management/06-runbook-generator.md) | Extracting operational knowledge into step-by-step runbooks |
| 07 | [Incident Trend Analysis](prompts/incident-management/07-incident-trend-analysis.md) | Quarterly review of incident patterns and systemic issues |
| 08 | [Remediation Tracker](prompts/incident-management/08-remediation-tracker.md) | Tracking postmortem action items to completion |
| 09 | [Severity Classification Guide](prompts/incident-management/09-severity-classification-guide.md) | Defining P0-P3 severity levels for your organisation |
| 10 | [Game Day Plan](prompts/incident-management/10-game-day-plan.md) | Planning a chaos engineering or incident simulation exercise |
| 11 | [Escalation Policy Document](prompts/incident-management/11-escalation-policy-document.md) | Defining who to call, when, and through what channel |
| 12 | [Incident Readiness Review](prompts/incident-management/12-incident-readiness-review.md) | Auditing preparedness before a launch or high-traffic event |

### [Architecture](prompts/architecture/) - 12 prompts
The technical decisions that shape your systems for years. Design, evaluate, document, and communicate architectural choices.

| # | Prompt | When to Use |
|---|--------|-------------|
| 01 | [System Design Document](prompts/architecture/01-system-design-document.md) | Before building a new service or system |
| 02 | [API Contract Design](prompts/architecture/02-api-contract-design.md) | Designing a new API (internal or external) |
| 03 | [Scalability Assessment](prompts/architecture/03-scalability-assessment.md) | Evaluating whether a system can handle growth |
| 04 | [Data Model Design](prompts/architecture/04-data-model-design.md) | Designing schemas for a new domain |
| 05 | [Caching Strategy](prompts/architecture/05-caching-strategy.md) | Deciding what to cache, where, and how to invalidate |
| 06 | [Observability Strategy](prompts/architecture/06-observability-strategy.md) | Designing monitoring, logging, and tracing for a system |
| 07 | [SLO Definition](prompts/architecture/07-slo-definition.md) | Setting Service Level Objectives for your services |
| 08 | [Architecture Review Prep](prompts/architecture/08-architecture-review-prep.md) | Preparing to present a design for peer review |
| 09 | [Dependency Mapping](prompts/architecture/09-dependency-mapping.md) | Documenting service dependencies and blast radius |
| 10 | [Technical Vision Document](prompts/architecture/10-technical-vision-document.md) | Writing a long-term technical strategy for your area |
| 11 | [Technology Radar](prompts/architecture/11-technology-radar.md) | Evaluating and categorising technologies for your org |
| 12 | [Database Selection Guide](prompts/architecture/12-database-selection-guide.md) | Choosing the right database for a workload |

### [Hiring Pipelines](prompts/hiring-pipelines/) - 12 prompts
The end-to-end process of finding, evaluating, and closing engineering candidates.

| # | Prompt | When to Use |
|---|--------|-------------|
| 01 | [Hiring Plan](prompts/hiring-pipelines/01-hiring-plan.md) | Planning headcount and roles for a quarter |
| 02 | [Recruiter Kickoff Brief](prompts/hiring-pipelines/02-recruiter-kickoff-brief.md) | Starting a search with a recruiter |
| 03 | [Sourcing Outreach Message](prompts/hiring-pipelines/03-sourcing-outreach-message.md) | Cold outreach to potential candidates |
| 04 | [Phone Screen Script](prompts/hiring-pipelines/04-phone-screen-script.md) | 30-minute initial candidate screen |
| 05 | [Take-Home Exercise Design](prompts/hiring-pipelines/05-take-home-exercise-design.md) | Creating a fair, well-scoped assessment |
| 06 | [Interview Debrief Facilitation](prompts/hiring-pipelines/06-interview-debrief-facilitation.md) | Running a structured hiring decision meeting |
| 07 | [Candidate Evaluation Summary](prompts/hiring-pipelines/07-candidate-evaluation-summary.md) | Synthesising interview feedback into a decision |
| 08 | [Offer Justification](prompts/hiring-pipelines/08-offer-justification.md) | Building the case for a specific comp package |
| 09 | [Candidate Closing Pitch](prompts/hiring-pipelines/09-candidate-closing-pitch.md) | Selling the role to a finalist who's deliberating |
| 10 | [Rejection Email](prompts/hiring-pipelines/10-rejection-email.md) | Delivering a respectful, useful no |
| 11 | [Pipeline Analytics Review](prompts/hiring-pipelines/11-pipeline-analytics-review.md) | Analysing funnel metrics to improve hiring |
| 12 | [Interviewer Calibration Guide](prompts/hiring-pipelines/12-interviewer-calibration-guide.md) | Training interviewers for consistency |

---

## Prompt Structure

Each file follows the same format:

```
## Situation    - When to use it
## The Prompt   - Copy-paste ready, with [PLACEHOLDERS]
## Example Input
## Example Output
## Tuning Notes
```

## Skills

Agent-ready versions of the highest-leverage prompts — for when you want the agent to *do the task*, not just draft text. Each skill lives at `skills/<category>/<name>/SKILL.md` and follows a portable spec (folded trigger description, Inputs to gather, Steps, Output format, Boundaries, Chaining). See [`SKILL_TEMPLATE.md`](SKILL_TEMPLATE.md) to contribute one.

### [Weekly Comms](skills/weekly-comms/) — 8 skills
| Skill | What it produces |
|-------|------------------|
| [exec-status-update](skills/weekly-comms/exec-status-update/SKILL.md) | Synthesise messy team-lead updates into a crisp leadership update an exec reads in two minutes |
| [team-weekly-summary](skills/weekly-comms/team-weekly-summary/SKILL.md) | A Friday wrap-up for your own engineers: what shipped, what's stuck, what's next |
| [stakeholder-project-update](skills/weekly-comms/stakeholder-project-update/SKILL.md) | Update non-engineering stakeholders on a project without jargon or false reassurance |
| [cross-team-dependency-update](skills/weekly-comms/cross-team-dependency-update/SKILL.md) | Surface cross-team blockers and handoffs collaboratively, with clear asks and owners |
| [meeting-recap-action-items](skills/weekly-comms/meeting-recap-action-items/SKILL.md) | Turn messy meeting notes into decisions and owned, dated action items |
| [board-engineering-summary](skills/weekly-comms/board-engineering-summary/SKILL.md) | Translate a quarter of engineering progress into board-level language and outcomes |
| [engineering-newsletter](skills/weekly-comms/engineering-newsletter/SKILL.md) | Turn raw updates into a company-wide newsletter product, design, and sales actually read |
| [engineering-all-hands-agenda](skills/weekly-comms/engineering-all-hands-agenda/SKILL.md) | A tight all-hands agenda that respects people's time and drives real discussion |

### [Planning](skills/planning/) — 14 skills
| Skill | What it produces |
|-------|------------------|
| [quarterly-roadmap](skills/planning/quarterly-roadmap/SKILL.md) | Goals, backlog, and tech debt into a defensible quarterly roadmap with an explicit not-doing list |
| [rfc-outline](skills/planning/rfc-outline/SKILL.md) | A proposed technical change into an RFC thorough enough to decide on |
| [sprint-retro-summary](skills/planning/sprint-retro-summary/SKILL.md) | Raw retro feedback distilled into actionable themes with owners |
| [tech-debt-prioritisation](skills/planning/tech-debt-prioritisation/SKILL.md) | A tech-debt list into a prioritised backlog that quantifies the cost of inaction |
| [build-vs-buy-analysis](skills/planning/build-vs-buy-analysis/SKILL.md) | Building in-house vs buying, weighed on total cost and strategic fit |
| [project-pre-mortem](skills/planning/project-pre-mortem/SKILL.md) | Imagine the project failed, then work backward to the likeliest risks and mitigations |
| [capacity-planning](skills/planning/capacity-planning/SKILL.md) | Team bandwidth mapped against committed work using realistic, not theoretical, capacity |
| [migration-plan](skills/planning/migration-plan/SKILL.md) | A System A → System B move phased for safety, with rollback at every step |
| [okr-drafting](skills/planning/okr-drafting/SKILL.md) | Vague goals into measurable team OKRs with real key results |
| [architecture-decision-record](skills/planning/architecture-decision-record/SKILL.md) | A technical decision captured so future engineers understand the why, not just the what |
| [incident-postmortem](skills/planning/incident-postmortem/SKILL.md) | A blameless postmortem with systemic root cause and prioritised action items |
| [sprint-planning-breakdown](skills/planning/sprint-planning-breakdown/SKILL.md) | An epic broken into independently deliverable, well-scoped sprint tickets |
| [engineering-strategy-one-pager](skills/planning/engineering-strategy-one-pager/SKILL.md) | What engineering is optimising for, and why, on one page |
| [team-offsite-agenda](skills/planning/team-offsite-agenda/SKILL.md) | A substantive offsite that produces real decisions, not forced fun |

### [People Management](skills/people-management/) — 16 skills
| Skill | What it produces |
|-------|------------------|
| [performance-review-draft](skills/people-management/performance-review-draft/SKILL.md) | Scattered observations into a fair, evidence-based review |
| [one-on-one-prep](skills/people-management/one-on-one-prep/SKILL.md) | A personalised 1:1 agenda mixing tactical check-ins with career growth |
| [feedback-synthesis](skills/people-management/feedback-synthesis/SKILL.md) | Multi-reviewer feedback distilled into a coherent, fair narrative |
| [career-ladder-draft](skills/people-management/career-ladder-draft/SKILL.md) | Engineering levels defined with clear, observable expectations |
| [job-description](skills/people-management/job-description/SKILL.md) | A JD that sells the role honestly and filters effectively |
| [interview-rubric](skills/people-management/interview-rubric/SKILL.md) | Consistent, bias-resistant evaluation criteria across an interview loop |
| [pip-documentation](skills/people-management/pip-documentation/SKILL.md) | A fair, evidence-based PIP draft (HR-reviewed) that gives a genuine chance to succeed |
| [promotion-case](skills/people-management/promotion-case/SKILL.md) | A case showing the person is already operating at the next level, with evidence |
| [onboarding-plan](skills/people-management/onboarding-plan/SKILL.md) | A 30/60/90 path to a new hire's first meaningful contribution |
| [skip-level-meeting-prep](skills/people-management/skip-level-meeting-prep/SKILL.md) | A skip-level that surfaces unfiltered signal and builds trust |
| [difficult-conversation-prep](skills/people-management/difficult-conversation-prep/SKILL.md) | Talking points so hard feedback lands clearly and kindly |
| [manager-readme](skills/people-management/manager-readme/SKILL.md) | A head start for reports on your working style and expectations |
| [layoff-communication](skills/people-management/layoff-communication/SKILL.md) | Coordinated, humane layoff communications for the individual and the team (legal-reviewed) |
| [team-values-workshop](skills/people-management/team-values-workshop/SKILL.md) | A workshop that produces real, usable working principles |
| [staff-engineer-scope-doc](skills/people-management/staff-engineer-scope-doc/SKILL.md) | What a staff engineer owns, decides, and is measured on |
| [team-health-survey-analysis](skills/people-management/team-health-survey-analysis/SKILL.md) | Survey themes connected to root causes and concrete actions |

### [Incident Management](skills/incident-management/) — 10 skills
| Skill | What it produces |
|-------|------------------|
| [incident-commander-runbook](skills/incident-management/incident-commander-runbook/SKILL.md) | A coordination playbook so anyone on rotation can run an incident calmly |
| [severity-classification-guide](skills/incident-management/severity-classification-guide/SKILL.md) | An unambiguous P0–P3 guide an engineer can apply at 3am in under a minute |
| [war-room-facilitation-guide](skills/incident-management/war-room-facilitation-guide/SKILL.md) | A script and structure for the IC to run a live war room |
| [on-call-handoff](skills/incident-management/on-call-handoff/SKILL.md) | Exactly what the incoming on-call needs to not be blindsided |
| [runbook-generator](skills/incident-management/runbook-generator/SKILL.md) | Tribal knowledge into a runbook any on-call can follow at 3am |
| [incident-trend-analysis](skills/incident-management/incident-trend-analysis/SKILL.md) | The patterns individual postmortems miss across a quarter |
| [remediation-tracker](skills/incident-management/remediation-tracker/SKILL.md) | Scattered postmortem action items tracked to completion with clear ownership |
| [game-day-plan](skills/incident-management/game-day-plan/SKILL.md) | An incident simulation realistic enough to surface real gaps |
| [escalation-policy-document](skills/incident-management/escalation-policy-document/SKILL.md) | A one-page reference that kills "who do I call next?" ambiguity |
| [incident-readiness-review](skills/incident-management/incident-readiness-review/SKILL.md) | An audit of whether the team can handle incidents before a high-risk event |

### [Architecture](skills/architecture/) — 12 skills
| Skill | What it produces |
|-------|------------------|
| [system-design-document](skills/architecture/system-design-document/SKILL.md) | A blueprint detailed enough that a senior engineer could build from it |
| [api-contract-design](skills/architecture/api-contract-design/SKILL.md) | The API contract right before building, with versioning and errors from day one |
| [scalability-assessment](skills/architecture/scalability-assessment/SKILL.md) | Whether the architecture survives 5–10x load, and where the bottlenecks are |
| [data-model-design](skills/architecture/data-model-design/SKILL.md) | A schema designed for actual query patterns, not theoretical purity |
| [caching-strategy](skills/architecture/caching-strategy/SKILL.md) | What to cache, where, how to invalidate, and what happens when the cache is down |
| [observability-strategy](skills/architecture/observability-strategy/SKILL.md) | The information architecture to go from "it's broken" to "here's the line" fast |
| [slo-definition](skills/architecture/slo-definition/SKILL.md) | Reliability targets that are measurable, meaningful, and have an error-budget policy |
| [architecture-review-prep](skills/architecture/architecture-review-prep/SKILL.md) | The design — and you — prepared for the tough questions reviewers will ask |
| [dependency-mapping](skills/architecture/dependency-mapping/SKILL.md) | Who depends on what, failure behaviour, and blast radius |
| [technical-vision-document](skills/architecture/technical-vision-document/SKILL.md) | An opinionated 12–24 month vision for where the architecture should head |
| [technology-radar](skills/architecture/technology-radar/SKILL.md) | Technologies sorted into Adopt / Trial / Assess / Hold with rationale |
| [database-selection-guide](skills/architecture/database-selection-guide/SKILL.md) | A datastore chosen from the workload, not the marketing |

### [Hiring Pipelines](skills/hiring-pipelines/) — 9 skills
| Skill | What it produces |
|-------|------------------|
| [hiring-plan](skills/hiring-pipelines/hiring-plan/SKILL.md) | Goals, team, and budget into a defensible hiring plan |
| [recruiter-kickoff-brief](skills/hiring-pipelines/recruiter-kickoff-brief/SKILL.md) | The insider context a JD leaves out, handed to a recruiter |
| [phone-screen-script](skills/hiring-pipelines/phone-screen-script/SKILL.md) | A 30-minute screen that assesses fit and sells the role |
| [take-home-exercise-design](skills/hiring-pipelines/take-home-exercise-design/SKILL.md) | A take-home that shows real skill, completable in 2–3 hours, fairly scored |
| [interview-debrief-facilitation](skills/hiring-pipelines/interview-debrief-facilitation/SKILL.md) | A debrief plan that forces an evidence-based, anchoring-resistant decision |
| [candidate-evaluation-summary](skills/hiring-pipelines/candidate-evaluation-summary/SKILL.md) | All interview feedback synthesised into one evidence-based evaluation |
| [offer-justification](skills/hiring-pipelines/offer-justification/SKILL.md) | Interview performance connected to a specific level and comp, defensibly |
| [interviewer-calibration-guide](skills/hiring-pipelines/interviewer-calibration-guide/SKILL.md) | A hands-on session that aligns interviewers and reduces bias |
| [pipeline-analytics-review](skills/hiring-pipelines/pipeline-analytics-review/SKILL.md) | A diagnosis of where candidates are lost and whether to fix speed or quality |

## Installation

Skills are plain markdown with a small YAML header, so any LLM agent can read them. Point your agent at the file and it works.

**Claude Code**
Add to your `CLAUDE.md`:
```
skillsDir: skills/
```

**GitHub Copilot**
Copy the relevant skill folder into `.github/copilot-instructions/`.

**Cursor**
Reference a skill inline via `@skills/<name>/SKILL.md`, or add the path to your `.cursorrules`.

**Any agent**
Point your agent at `skills/<category>/<name>/SKILL.md` — plain markdown with a small YAML header, readable by any LLM.

## Prompts vs Skills

Both cover the same engineering-leadership tasks — they differ in how you use them:

- **[`prompts/`](prompts/)** is the companion resource for **paste-and-fill** workflows: copy the prompt, replace the `[PLACEHOLDERS]`, and run it. Best when you want to drive the output yourself.
- **[`skills/`](skills/)** is for when you want the **agent to act** — gather the inputs (asking for what's missing instead of guessing), apply the structure, and produce the finished artifact, then offer the natural next step.

Not every prompt became a skill. Thin, transactional one-offs (rejection emails, outreach messages, celebration posts, single announcements) stay as prompts — a template beats an agent there. Substantial, multi-part artifacts became skills.

## Roadmap

- [x] V1: 36 prompts across comms, planning, and people management
- [x] V2: Additional categories (incident management, architecture, hiring pipelines)
- [x] V3: Agent-ready skill pack (69 skills, portable across Claude Code / Copilot / Cursor / any LLM)
- [ ] V3: Org-size variants (startup, growth, enterprise)
- [ ] V4: CLI tool to fetch and run skills from the terminal

