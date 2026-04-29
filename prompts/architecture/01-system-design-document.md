# System Design Document

## Situation

You're building a new service or system and need to document the design before writing code. This isn't an RFC (which proposes a decision) — it's a detailed technical blueprint that the team will build from. It should be comprehensive enough that a senior engineer can implement the system from this document alone.

## The Prompt

```
You are a senior engineer or engineering leader writing a system design document. The document should cover the full scope: from requirements through to deployment. Be specific about data flows, failure modes, and operational concerns — not just the happy path.

Structure:
1. **Overview** — what this system does and why we're building it (2-3 sentences)
2. **Requirements** — functional requirements (what it does) and non-functional requirements (performance, reliability, security)
3. **Architecture** — high-level system diagram, components, and how they interact
4. **Data model** — key entities, relationships, and storage choices
5. **API design** — key endpoints or interfaces with request/response shapes
6. **Data flow** — step-by-step for the primary use cases (including failure handling)
7. **Failure modes** — what can go wrong and how the system handles each scenario
8. **Operational concerns** — deployment, monitoring, alerting, on-call implications
9. **Security considerations** — auth, data protection, threat model highlights
10. **Open questions** — unresolved design decisions for team discussion

System: [SYSTEM_DESCRIPTION]
Context: [WHY_BUILDING_THIS]
Scale: [EXPECTED_SCALE]
Constraints: [CONSTRAINTS]
Team: [TEAM_CONTEXT]
```

## Example Input

```
System: Webhook delivery service — allows customers to register webhook URLs and receive HTTP callbacks when events occur in our platform (e.g., order.created, payment.completed, user.updated).
Context: Currently, integrating with our platform requires polling our API. Customers (especially enterprise) want push-based notifications for real-time integrations.
Scale: 500 customers initially, 50K events/day, growing to 500K events/day within a year. Target: deliver 99.9% of webhooks within 30 seconds of the event.
Constraints: Must be multi-tenant, must handle unreliable customer endpoints (retries), must log all delivery attempts for debugging. Team has experience with Go and PostgreSQL.
Team: 3 engineers, 8 weeks to MVP.
```

## Example Output

> **System Design: Webhook Delivery Service**
>
> **Overview**
> A service that delivers HTTP webhook callbacks to customer-registered endpoints when events occur in our platform. Replaces the need for customers to poll our API, enabling real-time integrations. Designed for reliability — every webhook is delivered at least once, with full delivery logging.
>
> **Requirements**
>
> *Functional:*
> - Customers register webhook URLs via API, specifying which event types to receive
> - When an event occurs, the system delivers an HTTP POST to all matching registered webhooks
> - Failed deliveries are retried with exponential backoff (up to 5 retries over 24 hours)
> - Customers can view delivery history and manually re-trigger failed deliveries
> - Webhook payloads are signed (HMAC-SHA256) so customers can verify authenticity
>
> *Non-functional:*
> - Delivery latency: 95th percentile < 30 seconds from event creation
> - Throughput: 500K events/day (peak: ~20 events/second)
> - Reliability: 99.9% of webhooks successfully delivered (excluding customer endpoint failures)
> - Delivery logs retained for 30 days
> - Multi-tenant: strict isolation between customers' webhook data
>
> **Architecture**
> ```
> [Platform Services] → Event Bus (SQS) → [Webhook Router] → Delivery Queue (SQS)
>                                              ↓
>                                     [Webhook Config DB]
>                                              
> Delivery Queue → [Delivery Workers (N)] → Customer Endpoint
>                        ↓                       ↓
>                   [Delivery Log DB]      [Retry Queue (SQS DLQ)]
> ```
>
> Components:
> - **Event Bus:** SQS queue receiving events from platform services
> - **Webhook Router:** Reads events, looks up matching webhook registrations, fans out to delivery queue
> - **Delivery Workers:** Pool of workers that execute HTTP requests to customer endpoints
> - **Webhook Config DB:** PostgreSQL — stores webhook registrations, event type subscriptions
> - **Delivery Log DB:** PostgreSQL — stores every delivery attempt (request, response, timing)
> - **Retry Queue:** SQS dead-letter queue for failed deliveries
>
> **Data Model**
> ```
> webhooks
>   id (uuid, PK)
>   customer_id (uuid, FK, indexed)
>   url (text)
>   secret (text, encrypted — for HMAC signing)
>   event_types (text[]) — e.g., ["order.created", "payment.completed"]
>   is_active (boolean)
>   created_at, updated_at
>
> delivery_attempts
>   id (uuid, PK)
>   webhook_id (uuid, FK, indexed)
>   event_id (uuid, indexed)
>   event_type (text)
>   request_url (text)
>   request_body (jsonb)
>   response_status (int)
>   response_body (text, truncated to 1KB)
>   response_time_ms (int)
>   attempt_number (int)
>   status (enum: pending, success, failed, retrying)
>   next_retry_at (timestamp, nullable)
>   created_at
> ```
>
> **API Design**
>
> *Register webhook:*
> ```
> POST /v1/webhooks
> { "url": "https://customer.com/webhook", "event_types": ["order.created"] }
> → 201 { "id": "...", "url": "...", "secret": "whsec_...", "event_types": [...] }
> ```
>
> *List delivery attempts:*
> ```
> GET /v1/webhooks/{id}/deliveries?status=failed&limit=20
> → 200 { "data": [...], "pagination": {...} }
> ```
>
> *Retry a delivery:*
> ```
> POST /v1/webhooks/{id}/deliveries/{delivery_id}/retry
> → 202 { "status": "queued" }
> ```
>
> **Data Flow: Successful Delivery**
> 1. Platform service publishes event to Event Bus (SQS)
> 2. Webhook Router consumes event, queries Config DB for matching webhooks
> 3. For each match, Router enqueues a delivery job to Delivery Queue with webhook ID, URL, payload, and signing secret
> 4. Delivery Worker picks up job, signs payload with HMAC-SHA256, sends HTTP POST to customer URL with 10-second timeout
> 5. Customer responds 2xx → Worker logs success in Delivery Log DB → done
>
> **Data Flow: Failed Delivery**
> 5b. Customer responds non-2xx or times out → Worker logs failure in Delivery Log DB
> 6. Worker calculates next retry time (exponential backoff: 1min, 5min, 30min, 2hr, 12hr)
> 7. Worker enqueues to Retry Queue with visibility delay matching the backoff
> 8. Repeat steps 4-7 up to 5 times
> 9. After 5 failures → mark as permanently failed, log final status
>
> **Failure Modes**
> | Failure | Impact | Handling |
> |---------|--------|----------|
> | Customer endpoint down | Deliveries fail for that customer | Retry with exponential backoff. Other customers unaffected. |
> | Customer endpoint slow (> 10s) | Worker thread tied up | 10-second timeout per request. Workers are pooled — one slow endpoint doesn't block others. |
> | Event Bus backlog | Delivery latency increases | Auto-scale Webhook Router. Alert at queue depth > 1000. |
> | Config DB down | Can't look up webhook registrations | Router retries with backoff. Events stay in Event Bus queue (SQS retention: 4 days). |
> | Delivery Log DB down | Can't log delivery attempts | Buffer logs locally, flush when DB recovers. Deliveries continue — logging is async. |
> | Duplicate events in bus | Duplicate webhook deliveries | Idempotency key (event_id + webhook_id) in delivery_attempts table. Workers check before sending. |
>
> **Operational Concerns**
> - Deploy: standard CI/CD pipeline, blue-green deployment
> - Monitoring: delivery success rate, p99 delivery latency, queue depth, retry rate per customer
> - Alerting: delivery success rate < 99%, queue depth > 5000, any single customer with > 50 consecutive failures (suggests disabled endpoint)
> - On-call: this service adds 1 new on-call responsibility. Runbook covers: queue backlog (scale workers), high retry rate (investigate specific customers), DB connection issues
>
> **Security Considerations**
> - Webhook secrets stored encrypted at rest (AES-256)
> - HMAC-SHA256 signature in `X-Webhook-Signature` header for payload verification
> - Customer URLs validated on registration (must be HTTPS, valid domain, responsive to a HEAD request)
> - Rate limit webhook registrations per customer (max 20 webhooks)
> - Delivery log payloads may contain PII — respect data retention policy (30-day purge)
>
> **Open Questions**
> 1. Should we support webhook URL verification (send a challenge, customer must respond) before activating?
> 2. Do we need to support custom headers on webhook requests for customers who need auth tokens?
> 3. What's the right SQS retention for the event bus — 4 days default or longer?

## Tuning Notes

- **Simpler system:** Cut the API design and data flow sections if the system has no external API. Focus on architecture, data model, and failure modes.
- **Distributed team reviewing:** Add a "glossary" section defining any terms that aren't universally understood. What your team calls an "event bus" might be another team's "message broker."
- **Presenting to non-engineers:** Extract the architecture diagram and requirements into a one-page summary. Everything else is for the engineering team.
- **Living document:** Update this doc as the system is built. Add a "deviations from design" section to capture where implementation diverged from the plan and why.
