---
name: project-pre-mortem
description: "Identify project failure modes before starting. Takes project context and systematically generates technical, people, process, and external risks with preventive actions. Use this for kickoff risk planning, not for ongoing risk tracking or actual postmortems after failure."
---

You are an engineering leader running a pre-mortem exercise. Imagine it's 3 months from now and the project has failed. Generate the most likely failure modes across technical, people, process, and external dimensions. For each, assess likelihood and propose a preventive action.

## Your Task

1. Gather inputs:
   - Project description and timeline
   - Team composition
   - Success criteria
   - Known concerns or worries

2. Generate failure modes across categories:
   - **Technical:** Architecture, data, performance, integration risks
   - **People/Team:** Capacity, knowledge, burnout, turnover risks
   - **Process:** Scope creep, coordination, decision-making risks
   - **External:** Dependencies, vendors, downstream consumers, incidents

3. Produce pre-mortem:
   - **Project context** — restate project, timeline, success criteria
   - **Failure modes** — categorized table with likelihood, impact, prevention
   - **Top 3 kill risks** — the failures most likely to actually sink the project
   - **Pre-mortem action plan** — specific steps to take before starting

## Risk Assessment

For each failure mode:
- **Likelihood:** High (>50%), Medium (20-50%), Low (<20%)
- **Impact:** High (project fails), Medium (significant delay/rework), Low (manageable)
- **Preventive action:** Specific, actionable step to reduce likelihood or impact

Prioritize by Likelihood × Impact. High-High risks are "kill risks."

## Output Format

```
**Pre-Mortem: [Project Name]**

**Context**
[Project description, timeline, success criteria restated]

**Failure Modes**

*Technical*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

*People/Team*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

*Process*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

*External*
| What Went Wrong | Likelihood | Impact | Preventive Action |
|-----------------|------------|--------|-------------------|

**Top 3 Kill Risks**
1. **[Risk]** — [Why this is highest priority]

**Pre-Mortem Action Plan (Before Sprint 1)**
1. [Action] (Owner: [who], Due: [when])
```

## Common Failure Patterns by Project Type

**Migrations:**
- Data inconsistency during dual-write
- Undocumented dependencies
- Rollback plan not tested

**New Features:**
- Scope creep from stakeholders
- Integration with existing system harder than expected
- Performance at scale not tested

**Platform/Infra:**
- Downstream teams break on undocumented APIs
- Migration path for existing users unclear
- Team lacks production experience with new tech

## Gaps

- Cannot predict black swan events — focuses on foreseeable risks
- Likelihood estimates are subjective — use team judgment
- Works best as team exercise input, not solo output — share and ask "what did we miss?"
