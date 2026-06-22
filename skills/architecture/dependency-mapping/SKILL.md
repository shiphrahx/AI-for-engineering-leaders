---
name: dependency-mapping
description: >
  Produces a dependency map for a service architecture — a dependency matrix (who calls whom,
  sync/async, hard/soft), a blast-radius analysis per service, single points of failure, a graceful-
  degradation inventory, and recommendations to reduce blast radius. Use when the user says "map our
  dependencies", "if X goes down what breaks", "find our SPOFs", "blast radius", or lists services
  and their connections. Use this to understand failure propagation across services; use
  scalability-assessment for capacity-under-load rather than failure-propagation.
---

# Dependency Mapping

Document which services depend on which, what happens when each fails, and the blast radius of every service — so the architecture can answer "if service X goes down, what breaks?"

## Inputs to gather

Gather these before mapping. If any are missing, ask in a single batched question — never invent dependencies, criticality, or incident history. Mark anything genuinely unavailable as **Unknown** in the output.

- **Services** — the service list with one-line descriptions
- **Known dependencies** — who calls whom, sync vs async, external dependencies
- **Recent incidents** — outages caused by dependencies (these reveal real blast radius)

## Steps

1. Confirm inputs. If the dependency relationships aren't given, ask — the map is only as good as the dependency facts. Mark unverified edges **Unknown**.
2. Build the **Dependency matrix** — for each service: what it depends on, sync vs async, and criticality (hard = caller fails without it; soft = caller degrades but survives). Include external dependencies (Stripe, SendGrid, etc.).
3. Do the **Blast radius analysis** — for each service: what breaks if it goes down, the share of users affected, and the business impact. Use any cited incidents as ground truth ("proven in the Feb outage").
4. Identify the **Single points of failure** — services that, if down, take everything down. Name them explicitly; these are the priorities.
5. Build the **Graceful degradation inventory** — per dependency: does a fallback exist, and what is the behaviour when it's down? Be honest where no fallback exists.
6. Write **Recommendations** — architectural changes to reduce blast radius, prioritised toward the SPOFs and the dependencies with no fallback (e.g. a short-lived auth-token cache at the gateway, a degraded-mode search fallback).
7. Adapt to context: offer to render the matrix as an actual diagram (Mermaid) — visual dependencies are easier to scan than tables. If the team has a service mesh or APM, recommend generating the map from real traffic rather than manual documentation, which drifts. For a non-engineer audience, relabel services as business capabilities ("Auth service" → "Login system"). Note that this document is most useful kept bookmarked for incident response ("what else might be broken?").
8. Assemble the output in the format below.

## Output format

```
**Dependency Map: [Architecture]**

**Dependency Matrix**
| Service | Depends On | Type | Criticality |
|---------|-----------|------|-------------|

**Blast Radius Analysis**
| If This Goes Down | What Breaks | Users Affected | Business Impact |
|-------------------|-------------|----------------|-----------------|

**Single Points of Failure**
1. [Service] — [why no fallback]

**Graceful Degradation Inventory**
| Dependency | Fallback Exists? | Behaviour When Down |
|-----------|------------------|---------------------|

**Recommendations**
1. [Change → blast radius it reduces]
```

## Boundaries

- Never fabricate dependency edges, criticality, or incident history — mark unverified relationships **Unknown**; a wrong map is worse than an honest gap.
- Never label a dependency "soft" without confirming the fallback actually exists and works — overstating resilience is dangerous in an incident.
- Never omit external dependencies (payment, email, third-party APIs) — they are common blast-radius sources outside your control.
- Manual maps drift — flag that the map should be regenerated from real traffic where tooling allows.

## Chaining

- After this, offer **runbook-generator** (incident-management) to turn each SPOF and degradation gap into an actionable runbook, or **incident-commander-runbook** to prepare response for the highest-blast-radius services.
- The recommendations also feed back into **system-design-document** when re-architecting to remove a SPOF.
