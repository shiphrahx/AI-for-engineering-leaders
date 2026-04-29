# Observability Strategy

## Situation

Your system is growing but your ability to understand what's happening inside it isn't keeping pace. You need a coherent observability strategy that covers metrics, logging, and tracing — not just monitoring dashboards, but the ability to answer "why is this broken?" quickly during an incident.

## The Prompt

```
You are a senior engineer designing an observability strategy. Cover the three pillars (metrics, logs, traces) and how they work together. Focus on what questions each signal answers and how to investigate issues efficiently. Don't just list tools — describe the information architecture.

Structure:
1. **Observability goals** — what questions should the team be able to answer?
2. **Metrics strategy** — what to measure, alert thresholds, dashboard design
3. **Logging strategy** — structured logging standards, log levels, retention
4. **Tracing strategy** — what to trace, sampling strategy, trace context propagation
5. **Correlation** — how metrics, logs, and traces connect during investigation
6. **Alerting philosophy** — what to alert on, reducing noise, on-call implications
7. **Tooling** — recommended stack and why

System: [SYSTEM_DESCRIPTION]
Current state: [CURRENT_OBSERVABILITY]
Pain points: [WHAT_IS_HARD_TO_DEBUG]
Scale: [REQUEST_VOLUME_AND_SERVICE_COUNT]
```

## Example Input

```
System: 12 microservices, API gateway, PostgreSQL, Redis, SQS. Mix of Go and Python services.
Current state: Basic CloudWatch metrics, unstructured application logs, no distributed tracing.
Pain points: Debugging cross-service issues takes 2+ hours. "Where is the latency?" is our most common incident question. Log search is painful because formats are inconsistent.
Scale: 5K requests/sec, 12 services, 3 databases.
```

## Example Output

> **Observability Strategy**
>
> **Goals — Questions We Must Be Able to Answer**
> - "Is the system healthy right now?" → Dashboards (< 5 seconds)
> - "Which service is causing the latency?" → Distributed traces (< 2 minutes)
> - "What changed that caused this error spike?" → Correlated logs + deploy markers (< 5 minutes)
> - "How is this customer's experience?" → Per-tenant metrics and trace filtering (< 5 minutes)
>
> **Metrics Strategy**
> Every service emits RED metrics (Rate, Errors, Duration) and USE metrics (Utilisation, Saturation, Errors) for infrastructure.
>
> Standard application metrics per service:
> - `http_requests_total` (counter, by method, path, status)
> - `http_request_duration_seconds` (histogram, by method, path)
> - `errors_total` (counter, by error_type)
> - Business metrics: orders processed, webhooks delivered, etc.
>
> Standard infrastructure metrics: CPU, memory, connection pool utilisation, queue depth.
>
> **Logging Strategy**
> All services emit structured JSON logs with mandatory fields:
> ```json
> {
>   "timestamp": "2025-03-15T14:30:00.123Z",
>   "level": "error",
>   "service": "order-service",
>   "trace_id": "abc123",
>   "span_id": "def456",
>   "message": "Payment processing failed",
>   "error": { "type": "StripeError", "message": "Card declined" },
>   "context": { "order_id": "ord_789", "customer_id": "cust_012" }
> }
> ```
> Log levels: `debug` (dev only), `info` (request lifecycle), `warn` (recoverable issues), `error` (failures requiring attention).
> Retention: 30 days hot (searchable), 90 days cold (archived).
>
> **Tracing Strategy**
> OpenTelemetry SDK in all services. Trace context propagated via W3C `traceparent` header. Sample 100% of error traces, 10% of successful traces. Every service-to-service call, database query, and external API call is a span.
>
> **Correlation**
> The `trace_id` appears in metrics labels, log entries, and traces. Investigation workflow: metric alert fires → click through to traces with high latency → click through to logs for specific spans. One click from "something is slow" to "here's the exact log line."
>
> **Alerting Philosophy**
> - Alert on symptoms (error rate, latency), not causes (CPU usage)
> - Every alert must have a runbook link
> - Three tiers: page (P0/P1 symptoms), notify (P2 trends), inform (dashboards only)
> - Target: < 5 false-positive pages per on-call rotation
>
> **Tooling:** Datadog for metrics + dashboards, OpenTelemetry for instrumentation, Datadog APM for traces, Datadog Logs for log aggregation. Single platform reduces context-switching during incidents.

## Tuning Notes

- **Budget-constrained:** Replace Datadog with Prometheus + Grafana (metrics), Jaeger (traces), and Loki (logs). Open-source stack, more ops overhead.
- **Monolith (not microservices):** Tracing is less critical. Focus on structured logging and application performance monitoring (APM) for slow code paths.
- **Existing messy setup:** Don't migrate everything at once. Start with structured logging standards (highest ROI), then add tracing to the 3 most-debugged services, then expand.
- **Compliance requirements:** Add a section on PII handling in logs and traces. Ensure sensitive fields are redacted before ingestion.
