# Technical Vision Document

## Situation

You've been asked to write a 12-24 month technical strategy for your domain. This isn't a roadmap (that's quarterly) — it's a vision for where the architecture should be heading and why. It guides decisions, aligns teams, and helps leadership understand the "why" behind engineering investment.

## The Prompt

```
You are a senior engineering leader writing a technical vision document for your domain. This should be opinionated — take a position on where the architecture should go. Support it with evidence (current pain points, industry trends, business needs) but don't be afraid to make bold calls. The audience is engineering leadership and your peers.

Structure:
1. **Current state** — where we are today, in honest terms (strengths and weaknesses)
2. **Business context** — what the business needs from the platform in the next 1-2 years
3. **Vision** — where we should be in 18-24 months, described concretely
4. **Principles** — 3-5 architectural principles that guide decisions toward the vision
5. **Key initiatives** — the 4-6 major efforts that get us from here to there
6. **What we stop doing** — patterns, technologies, or approaches we should phase out
7. **Success metrics** — how we know the vision is being realised
8. **Risks** — what could prevent us from getting there

Domain: [YOUR_DOMAIN]
Current architecture: [CURRENT_STATE]
Business direction: [WHERE_THE_BUSINESS_IS_HEADING]
Team: [TEAM_SIZE_AND_SKILLS]
Time horizon: [MONTHS]
```

## Example Input

```
Domain: Backend Platform (API layer, data storage, service infrastructure)
Current: Rails monolith serving 80% of traffic. 3 microservices extracted last year (auth, search, notifications). PostgreSQL primary + 2 read replicas. Manual deployments take 45 minutes. Test suite takes 25 minutes. No feature flags. Basic monitoring via Datadog.
Business direction: Expanding to 3 EU markets (data residency requirements), launching mobile app (need faster APIs), targeting 10x customer growth from enterprise sales pipeline.
Team: 12 backend engineers, 3 SREs. Strong Ruby skills, growing Go expertise.
Time horizon: 18 months
```

## Example Output

> **Backend Platform Technical Vision — 2025-2026**
>
> **Current State**
> Our Rails monolith remains the core of the platform, handling 80% of traffic. It's well-understood and productive for feature development, but it's becoming a constraint: deploy times are long, the test suite is slow, and it's difficult to scale components independently. The three microservices we extracted (auth, search, notifications) have proven the pattern works for us, but they were extracted reactively, not strategically.
>
> Our biggest strengths: strong domain knowledge in the monolith, excellent PostgreSQL expertise, and a pragmatic team that ships reliably. Our biggest weaknesses: no feature flags, no multi-region capability, and deployments that are slow and risky.
>
> **Business Context**
> Three forces shape our technical direction: EU expansion requires data residency (we must run in eu-west-1). The mobile app requires faster, more granular APIs than our current endpoints provide. Enterprise sales targets 10x customer growth, which our single-region monolith cannot support without architectural investment.
>
> **Vision: 18 Months From Now**
> A platform that runs in two regions, deploys in under 5 minutes, and allows teams to ship features independently. Not a full microservices rewrite — a strategically decomposed system where the monolith handles the stable core and extracted services handle the high-growth, high-change boundaries.
>
> Concretely: multi-region deployment (EU + US), 6-8 services (up from 4), sub-5-minute deploys with feature flags, comprehensive observability, and a developer experience that lets engineers go from idea to production in a day.
>
> **Principles**
> 1. **Extract at the boundary, not in the core.** Decompose services where the business is growing fastest or where independent scaling is needed. Don't break apart stable domain logic for architectural purity.
> 2. **Boring technology by default.** PostgreSQL, Redis, Go, Rails. New technology requires an ADR and a strong justification. We're solving business problems, not collecting technologies.
> 3. **Every deploy is safe by default.** Feature flags, canary rollouts, and automated rollback. No human should need to make a judgment call about whether a deploy is safe at 2am.
> 4. **Observe everything, alert on symptoms.** Full distributed tracing across all services. Alerting on customer-facing symptoms, not internal metrics.
> 5. **Multi-region is not optional.** Every new service must be designed for multi-region from day one. Data residency is a business requirement, not a nice-to-have.
>
> **Key Initiatives**
> 1. **Multi-region deployment** (Q1-Q2): Deploy the application stack to eu-west-1. Data residency routing at the API gateway. PostgreSQL cross-region replication for read replicas.
> 2. **Feature flag infrastructure** (Q1): Adopt LaunchDarkly. Integrate into deploy pipeline. Mandate feature flags for all customer-facing changes.
> 3. **Deploy pipeline overhaul** (Q1-Q2): CI/CD pipeline target: commit to production in < 10 minutes. Automated canary analysis. Rollback on error rate spike.
> 4. **Strategic service extraction** (Q2-Q4): Extract billing/payments and order management from the monolith. These are the highest-growth domains with the most scaling pressure.
> 5. **API layer for mobile** (Q2-Q3): GraphQL or BFF layer optimised for mobile access patterns. Sits in front of the monolith and services.
> 6. **Observability upgrade** (Q1-Q2): OpenTelemetry instrumentation, distributed tracing, structured logging standards, SLO dashboards.
>
> **What We Stop Doing**
> - Stop adding new features to the monolith's order management module (extract first)
> - Stop deploying without feature flags for customer-facing changes
> - Stop using unstructured logging
> - Stop treating the monolith as a monolith — treat it as one service among several
>
> **Success Metrics (18 months)**
> - Median deploy time < 5 minutes (from 45)
> - EU region live and serving EU customer traffic with data residency compliance
> - Zero P0 incidents caused by deploy issues (currently ~2/quarter)
> - 3+ services independently deployable by separate teams
> - Mobile API latency p99 < 200ms
>
> **Risks**
> - Team capacity: 6 initiatives is ambitious for 12 engineers + 3 SREs. Sequencing is critical — we can't do everything in Q1.
> - Multi-region complexity: we've never run multi-region. Expect unknowns.
> - Monolith extraction is deceptively hard. The billing domain has 4 years of implicit coupling.

## Tuning Notes

- **Presenting to the board:** Extract a one-page executive summary: current pain, vision in one sentence, 3 key investments, and the business outcome each enables.
- **Getting buy-in:** Circulate as a draft RFC and invite feedback from staff engineers and other EMs. A vision document that's co-created gets adopted; one that's dictated gets ignored.
- **Review cadence:** Revisit every 6 months. The vision should be stable but the priorities may shift based on what you learn.
- **Small team (< 10 engineers):** Focus on 2-3 initiatives maximum. A vision document for a small team that lists 8 initiatives is a wishlist, not a strategy.
