# API Contract Design

## Situation

You're designing a new API — internal or external — and want to get the contract right before building. A well-designed API contract saves months of integration pain. A bad one haunts you for years.

## The Prompt

```
You are a senior engineer designing an API contract. Prioritise developer experience, consistency, and evolvability. The API should be intuitive to use without reading documentation, but the documentation should be excellent anyway. Think about versioning, error handling, and pagination from day one.

Structure:
1. **API overview** — what this API does, who the consumers are, and the interaction model
2. **Design principles** — conventions this API follows (naming, auth, pagination, errors)
3. **Resource model** — the core resources and their relationships
4. **Endpoint catalogue** — every endpoint with method, path, request/response shapes, and status codes
5. **Error contract** — consistent error format with codes and messages
6. **Authentication & authorisation** — how consumers authenticate and what they can access
7. **Pagination & filtering** — how large collections are handled
8. **Versioning strategy** — how the API evolves without breaking consumers
9. **Rate limiting** — limits and how they're communicated to consumers

API purpose: [WHAT_THE_API_DOES]
Consumers: [WHO_CALLS_THIS_API]
Constraints: [CONSTRAINTS]
```

## Example Input

```
API purpose: Team management API — allows customers to create, manage, and query teams and team memberships within our platform. Used for both our web UI and for customer integrations via the public API.
Consumers: Internal (web frontend, mobile app) and external (customer integrations, Zapier)
Constraints: RESTful, JSON, must support both API key auth (external) and session auth (internal). We use cursor-based pagination everywhere.
```

## Example Output

> **API Contract: Team Management**
>
> **Overview**
> RESTful JSON API for managing teams and memberships. Serves both internal clients (web, mobile) and external integrations (API key consumers). All endpoints are under `/v1/teams`.
>
> **Design Principles**
> - Resource-oriented: nouns, not verbs (`/teams`, not `/createTeam`)
> - Consistent pluralisation: all collection resources are plural
> - `snake_case` for all JSON fields
> - ISO 8601 for all timestamps (`2025-03-15T14:30:00Z`)
> - Cursor-based pagination on all list endpoints
> - Consistent error format on all error responses
>
> **Resource Model**
> ```
> Team (1) ←→ (N) Membership ←→ (1) User
> 
> Team: { id, name, description, created_at, updated_at }
> Membership: { id, team_id, user_id, role (owner|admin|member), joined_at }
> ```
>
> **Endpoints**
>
> | Method | Path | Description | Auth |
> |--------|------|-------------|------|
> | POST | /v1/teams | Create a team | Authenticated user |
> | GET | /v1/teams | List teams the caller belongs to | Authenticated user |
> | GET | /v1/teams/{id} | Get team details | Team member |
> | PATCH | /v1/teams/{id} | Update team name/description | Team admin or owner |
> | DELETE | /v1/teams/{id} | Delete a team | Team owner only |
> | GET | /v1/teams/{id}/members | List team members | Team member |
> | POST | /v1/teams/{id}/members | Add a member | Team admin or owner |
> | PATCH | /v1/teams/{id}/members/{user_id} | Update member role | Team owner |
> | DELETE | /v1/teams/{id}/members/{user_id} | Remove a member | Team admin+ or self |
>
> *Example: Create a team*
> ```
> POST /v1/teams
> { "name": "Backend Engineering", "description": "Core platform team" }
>
> 201 Created
> {
>   "id": "team_abc123",
>   "name": "Backend Engineering",
>   "description": "Core platform team",
>   "created_at": "2025-03-15T14:30:00Z",
>   "updated_at": "2025-03-15T14:30:00Z"
> }
> ```
>
> **Error Contract**
> All errors return:
> ```
> {
>   "error": {
>     "code": "team_not_found",
>     "message": "The team with ID 'team_xyz' does not exist.",
>     "status": 404
>   }
> }
> ```
> Error codes are stable (machine-readable), messages are human-readable and may change.
>
> **Authentication**
> - External: `Authorization: Bearer <api_key>` header
> - Internal: Session cookie (set by auth service)
> - Both methods are accepted on all endpoints. The auth middleware resolves the caller identity regardless of method.
>
> **Pagination**
> All list endpoints use cursor-based pagination:
> ```
> GET /v1/teams?limit=20&cursor=eyJpZCI6InRlYW1fYWJjMTIzIn0=
>
> {
>   "data": [...],
>   "pagination": {
>     "next_cursor": "eyJpZCI6InRlYW1feHl6NDU2In0=",
>     "has_more": true
>   }
> }
> ```
> Default limit: 20. Maximum limit: 100.
>
> **Versioning**
> URL-based: `/v1/teams`. Backward-incompatible changes require a new version (`/v2/`). Additive changes (new fields, new optional parameters) ship without version bumps. Deprecated fields are marked in documentation for 2 major versions before removal.
>
> **Rate Limiting**
> - Default: 100 requests/minute per API key
> - Enterprise: 1,000 requests/minute
> - Rate limit headers included in every response: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`
> - Exceeded: `429 Too Many Requests` with `Retry-After` header

## Tuning Notes

- **Internal-only API:** Relax the versioning and error contract requirements. Internal APIs can be changed with coordinated deploys. Still document them — future you will thank present you.
- **GraphQL instead of REST:** Replace the endpoint catalogue with schema definitions and resolver descriptions. Add a section on query complexity limits.
- **API-first company:** Add an "SDK design" section showing how the API maps to client libraries in 2-3 languages.
- **Legacy API redesign:** Add a "migration guide" section showing how existing endpoints map to new ones, with a deprecation timeline.
