---
name: observability-strategy
description: >
  Produces an observability strategy across the three pillars — metrics, logs, traces — plus
  correlation, alerting philosophy, and tooling, framed around the questions the team must answer
  during an incident. Use when the user says "observability strategy", "instrumentation plan",
  "we can't debug X", "set up tracing/structured logging", or describes slow cross-service
  debugging. Use this to design how to SEE the system; use slo-definition to set the reliability
  targets the alerts defend, and incident-postmortem to analyse an incident after the fact.
---

# Observability Strategy

Design the information architecture that lets the team go from "something is broken" to "here's the exact line" fast — not a list of tools, but how metrics, logs, and traces work together.

## Inputs to gather

Gather these before designing. If any are missing, ask in a single batched question — never invent the current tooling, scale, or pain points. Mark anything genuinely unavailable as **Unknown** in the output.

- **System description** — services, languages, data stores
- **Current observability state** — what exists today
- **Pain points** — what's hard to debug now
- **Scale** — request volume and service count

## Steps

1. Confirm inputs. If the current state or top debugging pain is unstated, ask — they anchor the whole strategy. Mark gaps **Unknown**.
2. Define **Observability goals** as the concrete questions the team must answer ("Which service is slow?", "What changed before this spike?"), each with a target time-to-answer and the signal that answers it.
3. Design the **Metrics strategy** — RED (Rate, Errors, Duration) per service, USE (Utilisation, Saturation, Errors) for infra, plus business metrics; alert thresholds and dashboard design.
4. Design the **Logging strategy** — a structured (JSON) log format with mandatory fields including a shared `trace_id`, log levels and their meaning, and retention (hot vs cold).
5. Design the **Tracing strategy** — instrumentation (e.g. OpenTelemetry), context propagation, and sampling: 100% of error traces, a fraction of successful traces to control cost.
6. Define **Correlation** — how the shared `trace_id` links the three pillars and the click-through investigation workflow from alert → trace → log line.
7. Define the **Alerting philosophy** — alert on symptoms (error rate, latency), not causes (CPU); every alert has a runbook link; tier alerts (page / notify / inform); set a false-positive target.
8. Recommend **Tooling** — a coherent stack with rationale, favouring fewer context-switches during incidents.
9. Adapt to context: for budget-constrained teams, use Prometheus + Grafana / Jaeger / Loki (more ops overhead, no license cost). For a monolith, deprioritise tracing and lead with structured logging and APM for slow paths. For an existing messy setup, don't migrate everything — start with logging standards (highest ROI), then trace the 3 most-debugged services, then expand. For compliance, add a PII-handling section ensuring sensitive fields are redacted before ingestion.
10. Assemble the output in the format below.

## Output format

```
**Observability Strategy**

**Goals — Questions We Must Answer**
- "[Question]" → [Signal] (< [time])

**Metrics Strategy**
[Standard metrics per service + infra, alert thresholds, dashboards]

**Logging Strategy**
[Structured format with mandatory fields incl. trace_id, levels, retention]

**Tracing Strategy**
[Instrumentation, propagation, sampling]

**Correlation**
[How trace_id links the three pillars; investigation workflow]

**Alerting Philosophy**
[What to page vs notify vs inform; runbook requirement; false-positive target]

**Tooling:** [Stack and rationale]
```

## Boundaries

- Never fabricate current tooling, scale, or pain points — mark them **Unknown** and ask.
- Never produce a tool shopping list without the information architecture — the questions and correlation workflow are the point.
- Never alert on causes (CPU, memory) where a symptom (error rate, latency) is available, and never propose an alert without a runbook link.
- Sampling rates and alert thresholds are starting points — state that the user must calibrate them against real volume and baseline behaviour.

## Chaining

- Pairs with **slo-definition** — the SLOs define the symptoms this strategy alerts on; do one then the other.
- Often follows **caching-strategy** or **scalability-assessment** (the new components and bottlenecks need monitoring).
