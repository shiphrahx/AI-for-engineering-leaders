# Technology Radar

## Situation

Your engineering team adopts technologies ad hoc — someone tries a new framework in a side project, it ends up in production, and now you're supporting 4 different web frameworks. You need a technology radar that categorises technologies into "adopt, trial, assess, hold" and gives the team clear guidance on what to use and what to avoid.

## The Prompt

```
You are an engineering leader creating a technology radar for your organisation. Categorise technologies that are relevant to your team into four rings: Adopt (use confidently), Trial (use on non-critical projects), Assess (research and evaluate), Hold (stop adopting, migrate away). Every placement must have a rationale. The radar should be opinionated — it's a decision-making tool, not a catalogue.

Structure:
1. **Radar overview** — what this radar covers, who it's for, how to use it
2. **Adopt** — technologies we endorse for production use, with context
3. **Trial** — technologies we're actively experimenting with
4. **Assess** — technologies we're watching and evaluating
5. **Hold** — technologies we're moving away from (with migration guidance)
6. **Recently changed** — technologies that moved rings since the last radar
7. **Review cadence** — how often the radar is updated

Current stack: [YOUR_STACK]
Team skills: [TEAM_SKILLS]
Pain points: [TECHNOLOGY_PAIN_POINTS]
Upcoming needs: [FUTURE_REQUIREMENTS]
```

## Example Input

```
Stack: Python (Django) backend, React frontend, PostgreSQL, Redis, AWS (ECS, SQS, S3), Terraform, GitHub Actions CI/CD. Some services in Flask, one in FastAPI. Mobile app in React Native.
Skills: Strong Python and React. Growing interest in TypeScript and Go. No Rust or Kubernetes experience.
Pain points: Django ORM struggles with complex queries. Flask services lack structure and are hard to maintain. React class components still in use. Terraform state management is painful across teams.
Upcoming needs: Real-time features (WebSocket or SSE), better API documentation, potential move to Kubernetes.
```

## Example Output

> **Engineering Technology Radar — Q2 2025**
>
> **How to use this radar:** "Adopt" means use freely in production. "Trial" means use with tech lead approval on non-critical services. "Assess" means research only — don't build with it yet. "Hold" means stop using it in new projects and plan migration for existing uses.
>
> ---
>
> **Adopt** ✅
> | Technology | Category | Rationale |
> |-----------|----------|-----------|
> | Python 3.12+ | Language | Our primary language. Strong team expertise. |
> | Django 5.x | Framework | Default for new backend services. Well-understood, productive. |
> | FastAPI | Framework | Endorsed for API-only services where Django's ORM isn't needed. Async support and auto-generated OpenAPI docs address two of our pain points. |
> | PostgreSQL 16 | Database | Battle-tested. Team expertise is deep. Default for all relational data. |
> | React 18 + TypeScript | Frontend | TypeScript adoption is complete for new code. Functional components with hooks only. |
> | Terraform | IaC | Default for all AWS infrastructure. Use Terragrunt for multi-environment management. |
> | GitHub Actions | CI/CD | Mature, integrated with our workflow. No reason to change. |
>
> **Trial** 🔬
> | Technology | Category | Rationale |
> |-----------|----------|-----------|
> | Go | Language | Trial for high-performance services where Python's speed is a bottleneck. One team is building a real-time event processor in Go. Evaluate team experience and operational impact before expanding. |
> | Server-Sent Events (SSE) | Protocol | Simpler than WebSockets for our real-time notification use case. Trial on the notification service before committing to a broader real-time strategy. |
> | OpenTelemetry | Observability | Trial for distributed tracing. Instrument 2-3 services this quarter and evaluate the debugging experience before org-wide rollout. |
>
> **Assess** 🔍
> | Technology | Category | Rationale |
> |-----------|----------|-----------|
> | Kubernetes (EKS) | Infrastructure | Our ECS setup works but has limitations for service-to-service communication and scaling policies. Assess EKS in Q3 — the migration cost is high, so the benefits must be clear. |
> | htmx | Frontend | Potential simplification for admin-heavy pages that don't need full React. Assess fit for our internal tools. |
> | SQLAlchemy 2.0 | ORM | Addresses Django ORM pain points for complex queries. Assess whether it's worth the migration cost for services where Django ORM struggles. |
>
> **Hold** ⛔
> | Technology | Category | Rationale | Migration Path |
> |-----------|----------|-----------|----------------|
> | Flask | Framework | Lacks structure for production services. Two existing Flask services should be migrated to FastAPI or Django by Q4. | Rewrite in FastAPI. |
> | React class components | Frontend | Hooks-only going forward. Convert remaining class components as you touch the files (boy-scout rule). | Incremental — convert on touch. |
> | Python 3.9 and below | Language | Security support ending. All services must be on 3.12+ by Q3. | Upgrade in place. |
> | Manual Terraform applies | Process | All Terraform changes must go through CI/CD pipeline. No more `terraform apply` from laptops. | Enforce via CI gating. |
>
> **Review:** This radar is updated quarterly. Any engineer can propose a change via PR to the radar repo. Changes are discussed in the monthly architecture sync.

## Tuning Notes

- **First radar:** Don't try to cover everything. Focus on the decisions that are actively causing confusion or debate ("should I use Flask or FastAPI for this new service?").
- **Getting buy-in:** Make the radar collaborative. Staff engineers and tech leads should contribute placements. A radar imposed by one person gets ignored.
- **Enforcement:** The radar is advisory, not a policy document. "Hold" means "strong recommendation against" — not "prohibited." But if someone repeatedly ignores Hold items, that's a coaching conversation.
- **Visualise it:** The Thoughtworks Radar format (concentric rings with blips) is excellent for visual communication. Use it for presentations, keep the table format for reference.
