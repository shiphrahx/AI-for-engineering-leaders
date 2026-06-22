---
name: api-contract-design
description: >
  Produces an API contract before any code is written — overview, design principles, resource model,
  endpoint catalogue, error contract, auth, pagination/filtering, versioning, and rate limiting. Use
  when the user says "design an API", "API contract/spec", "endpoints for [feature]", or describes a
  new internal or external API. Use this for the API surface in isolation; use system-design-document
  for the whole system including the data flows behind the API, and data-model-design for the storage
  schema rather than the request/response shapes.
---

# API Contract Design

Get the contract right before building — intuitive enough to use without docs, with versioning, errors, and pagination designed in from day one because they are painful to retrofit.

## Inputs to gather

Gather these before designing. If any are missing, ask in a single batched question — never invent consumer needs, auth rules, or rate limits. Mark anything genuinely unavailable as **Unknown** in the output.

- **API purpose** — what it does
- **Consumers** — internal, external, or both; human or machine
- **Constraints** — REST/GraphQL, auth methods, pagination style, existing conventions

## Steps

1. Confirm the inputs. If consumer type, auth model, or pagination style is unstated, ask — these shape every endpoint. Mark unresolved items **Unknown**.
2. Write the **Overview** — what the API does, who calls it, the interaction model, and the base path.
3. State **Design principles** — resource-oriented nouns not verbs (`/teams`, not `/createTeam`); consistent casing and pluralisation; ISO 8601 timestamps; one pagination style chosen once; a single error format. Decide pagination and errors before the first endpoint — they touch everything.
4. Define the **Resource model** — core resources and their relationships with cardinality.
5. Build the **Endpoint catalogue** — every endpoint as a table (method, path, description, auth), plus 1-2 full request/response examples with status codes.
6. Specify the **Error contract** — one consistent shape; error `code`s are stable and machine-readable, `message`s are human-readable and may change.
7. Define **Authentication & authorisation** — how each consumer type authenticates, and how identity and permission resolve (e.g. check membership before role; 404 vs 403 to avoid leaking existence). Additive changes ship without a bump; breaking changes need a new version.
8. Define **Pagination & filtering** — style, example, default and max limits; whether unknown filter params 400 or are silently ignored.
9. Define the **Versioning strategy** — how the API evolves without breaking consumers, plus the deprecation policy.
10. Define **Rate limiting** — limits per consumer tier, the headers returned, and 429 behaviour.
11. Adapt to context: for an internal-only API, relax versioning/error rigor (coordinated deploys) but still document it. For GraphQL, replace the endpoint catalogue with schema definitions and resolver descriptions and add query-complexity limits. For an API-first company, add an SDK design section mapping the API to client libraries in 2-3 languages. For a legacy redesign, add a migration guide mapping old endpoints to new ones with a deprecation timeline.
12. Assemble the output in the format below.

## Output format

```
**API Contract: [Name]**

**Overview**
[What it does, consumers, base path]

**Design Principles**
[Bulleted conventions]

**Resource Model**
[Entities and relationships]

**Endpoints**
| Method | Path | Description | Auth |
|--------|------|-------------|------|

[1-2 full request/response examples with status codes]

**Error Contract**
[Standard error shape + example]

**Authentication & Authorisation**
[Methods, how identity resolves, how permission resolves]

**Pagination & Filtering**
[Style, example, default/max limits, unknown-filter behaviour]

**Versioning**
[Strategy and deprecation policy]

**Rate Limiting**
[Limits, headers, 429 behaviour]
```

## Boundaries

- Never fabricate consumer needs, authorization roles, or rate limits — these come from the user. Mark them **Unknown**.
- Never leave error format, pagination, or versioning undesigned — these are the expensive-to-retrofit decisions and the whole point of doing this up front.
- Never use verbs in resource paths or mix casing/pluralisation conventions across endpoints.
- This designs a contract, not an implementation — do not specify storage, indexes, or internal data flow here.

## Chaining

- This commonly follows **system-design-document** (which names the endpoints this skill fleshes out).
- After this, offer **data-model-design** to design the storage behind these resources.
