# Staff Engineer Scope Document

## Situation

You have a staff engineer (or are writing this as one) whose impact isn't clearly defined. What should they be working on? What decisions do they own? Where do they lead vs. support? A scope document clarifies this — for them, for you, and for the organisation.

## The Prompt

```
You are an engineering manager defining the scope and expectations for a staff engineer role.

Write a staff engineer scope document with these sections:

1. **Role context** (where this person sits in the org, what area they cover)
2. **Primary responsibilities** (what they own end-to-end — not tasks, but ongoing accountabilities)
3. **Decision authority** (what they can decide unilaterally, what they need to consult on, what needs escalation)
4. **How success is measured** (3-4 concrete indicators over a 6-12 month horizon — not velocity metrics)
5. **Working relationships** (who they partner with regularly and in what capacity)
6. **What this role is not** (common scope creep or misunderstandings to head off)

Keep it to 1-2 pages. Avoid generic "technical leadership" language — make it specific to this person, this team, this moment.

Context:
- Engineer: [NAME or "Staff Engineer"]
- Area of ownership: [e.g. data infrastructure, frontend platform, payments]
- Team structure: [who they work with]
- Current biggest challenge in their area: [CHALLENGE]
- Known strengths: [STRENGTHS]
- Known growth areas: [GROWTH_AREAS]
```

## Example Input

```
- Engineer: Ana
- Area: Developer Experience (internal tooling, CI/CD, developer onboarding)
- Team: Works across 6 product teams; no direct reports; works closely with the Platform EM and CTO
- Current challenge: CI pipeline is slow and flaky; new engineers take 3+ weeks to become productive
- Strengths: Deep systems knowledge, trusted by peers, strong written communicator
- Growth areas: Influencing without authority, saying no to requests that don't fit the strategy
```

## Example Output

> **Staff Engineer Scope — Developer Experience**
> *Ana | Updated: [DATE]*
>
> ---
>
> **Role context**
> Ana is the technical lead for Developer Experience at [Company]. She works across all six product teams with a focus on the tools, systems, and practices that determine how fast and safely engineers can ship. She has no direct reports but operates with staff-level autonomy: she sets technical direction in her domain, drives cross-team initiatives, and is a key partner to the Platform EM and CTO.
>
> ---
>
> **Primary responsibilities**
> - Own the health and strategic direction of the CI/CD platform — reliability, speed, and cost
> - Define and maintain the standard for local development environment setup and documentation
> - Drive the engineering onboarding experience for new hires (target: productive in ≤2 weeks)
> - Identify systemic tooling pain points across product teams and build or buy solutions
> - Set the technical bar for internal tooling decisions (build vs. buy, deprecations, migrations)
>
> ---
>
> **Decision authority**
>
> *Can decide unilaterally:*
> - Technical approach for any DX tooling project scoped to her area
> - Deprecation of internal tools with adequate migration path and lead time
> - CI/CD configuration changes that don't affect prod deployment gates
>
> *Consult the Platform EM:*
> - Initiatives requiring significant team time from other squads (>1 sprint)
> - Changes to deployment gating or release processes
> - Vendor evaluations and contracts
>
> *Escalate to CTO:*
> - Architectural changes with company-wide impact
> - Decisions that trade developer velocity against reliability in a material way
>
> ---
>
> **How success is measured**
> By [DATE+12 months], success looks like:
> - CI pipeline p95 build time under 8 minutes (from ~22 minutes today), flakiness below 2%
> - New engineer time-to-first-meaningful-PR under 10 business days
> - Developer satisfaction score on tooling above 4.0/5.0 in the bi-annual survey
> - At least two cross-team initiatives driven and shipped with Ana as technical lead
>
> ---
>
> **Working relationships**
> - **Platform EM:** Weekly 1:1, primary manager relationship; strategy alignment and prioritisation
> - **Product team leads:** Quarterly check-ins to surface tooling pain; ad hoc for urgent issues
> - **CTO:** Monthly; technical direction alignment and escalation path
> - **New hire cohorts:** Ana presents at onboarding and is the point of contact for DX issues in the first 30 days
>
> ---
>
> **What this role is not**
> - Ana is not a general-purpose senior engineer who can be pulled into product feature work. Her leverage comes from depth in DX, not breadth across all engineering problems.
> - She is not responsible for executing every DX improvement — she leads them. Execution is often with or through others.
> - She does not manage people. Influence without authority is the expected working mode.

## Tuning Notes

- **Newly promoted staff engineer:** Add a 30/60/90 day ramp section before the primary responsibilities.
- **Staff engineer without clear ownership area:** Use this document as the starting point for a conversation about what they *should* own — the gaps in the draft reveal the ambiguity.
- **For the engineer to write themselves:** Frame it as a proposal. They draft, you refine together. Creates more buy-in and surfaces their own mental model of the role.
