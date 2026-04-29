# Dependency Mapping

## Situation

You need to document which services depend on which, what happens when each dependency fails, and what the blast radius of each service is. This is critical for incident response, migration planning, and understanding your system's true reliability profile.

## The Prompt

```
You are a senior engineer creating a dependency map for your service architecture. Document both direct and transitive dependencies, classify their criticality, and assess the blast radius of each service's failure. This document should answer: "If service X goes down, what breaks?"

Structure:
1. **Service inventory** — all services with one-line descriptions
2. **Dependency matrix** — who calls whom, synchronous vs async, criticality (hard vs soft dependency)
3. **Blast radius analysis** — for each service: what breaks if it goes down, who's affected, and the business impact
4. **Single points of failure** — services that, if down, take everything down
5. **Graceful degradation inventory** — where fallbacks exist and where they don't
6. **Recommendations** — architectural changes to reduce blast radius

Services: [SERVICE_LIST]
Known dependencies: [DEPENDENCY_INFO]
Recent incidents: [INCIDENTS_CAUSED_BY_DEPENDENCIES]
```

## Example Input

```
Services: API gateway, Auth service, User service, Order service, Payment service, Notification service, Search service, Analytics pipeline
Known: Everything goes through the API gateway. Auth is called on every request. Payments depend on Stripe (external). Notifications depend on SendGrid (external) and SQS. Search depends on Elasticsearch. Analytics consumes events from all services via Kafka.
Recent incidents: Auth service outage took down the entire platform (Feb). Stripe blip caused payment failures but orders could still be placed (Jan).
```

## Example Output

> **Dependency Map: Platform Services**
>
> **Dependency Matrix**
>
> | Service | Depends On | Type | Criticality |
> |---------|-----------|------|-------------|
> | API Gateway | Auth service | Sync | Hard — every request fails without auth |
> | API Gateway | All backend services | Sync | Hard — gateway is the entry point |
> | User service | PostgreSQL | Sync | Hard |
> | Order service | User service, Payment service, PostgreSQL | Sync | Hard (user), Soft (payment — can create unpaid orders) |
> | Payment service | Stripe (external), PostgreSQL | Sync | Hard (Stripe for charges), Soft (DB for logging) |
> | Notification service | SQS, SendGrid (external) | Async | Soft — delays are tolerable, failures aren't user-facing |
> | Search service | Elasticsearch | Sync | Hard |
> | Analytics pipeline | Kafka, all services (event producers) | Async | Soft — delays acceptable, no user-facing impact |
>
> **Blast Radius Analysis**
>
> | If This Goes Down | What Breaks | Users Affected | Business Impact |
> |-------------------|-------------|---------------|-----------------|
> | **API Gateway** | Everything | 100% | **Total outage** — this is our #1 SPOF |
> | **Auth service** | Everything (every request needs auth) | 100% | **Total outage** — proven in Feb incident |
> | **PostgreSQL primary** | User, Order, Payment services | 100% | **Total outage** for writes |
> | **Order service** | Order creation and management | 80% (core workflow) | Revenue-critical |
> | **Payment service** | Payment processing | Revenue loss during downtime | High (but orders can queue) |
> | **Search service** | Product search | 30% (users actively searching) | Significant UX degradation |
> | **Notification service** | Email/SMS notifications | 0% of core flows | Low — users unaware until they miss a notification |
> | **Analytics pipeline** | Dashboards, reports | 0% of users | Internal only |
> | **Stripe (external)** | Payment charges | Checkout blocked | Revenue-critical but outside our control |
>
> **Single Points of Failure**
> 1. **API Gateway** — all traffic routes through one gateway. No fallback.
> 2. **Auth service** — hard dependency for every request. February's outage proved this.
> 3. **PostgreSQL primary** — single primary for writes across 3 services.
>
> **Graceful Degradation Inventory**
> | Dependency | Fallback Exists? | Behaviour When Down |
> |-----------|-----------------|-------------------|
> | Auth service | ❌ No | Total failure |
> | Stripe | ✅ Partial | Orders created as "payment pending," retry later |
> | SendGrid | ✅ Yes | Falls back to Mailgun |
> | Elasticsearch | ❌ No | Search returns errors (could fall back to DB query) |
> | Kafka | ✅ Yes | Events buffered locally, flushed on recovery |
>
> **Recommendations**
> 1. **Auth service resilience:** Add a short-lived JWT cache at the gateway (5-minute TTL). If auth service is down, previously authenticated users can continue for 5 minutes.
> 2. **Search fallback:** Add a degraded-mode PostgreSQL search query. Slower but functional.
> 3. **Database write resilience:** Evaluate multi-primary or queued-write pattern for order creation during DB failover.

## Tuning Notes

- **Visual format:** Convert the dependency matrix into an actual diagram (Mermaid, draw.io). Visual dependencies are easier to spot than tables for most people.
- **Automated discovery:** If you have service mesh or APM, generate the dependency map from real traffic data rather than manual documentation. Manual maps drift.
- **Present to non-engineers:** Replace technical service names with business capabilities. "Auth service" → "Login system." "API gateway" → "The front door."
- **Use during incident response:** This document answers "what else might be broken?" when one service fails. Keep it bookmarked.
