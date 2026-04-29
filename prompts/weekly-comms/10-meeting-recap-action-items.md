# Meeting Recap & Action Items

## Situation

You just left a meeting with messy notes — half-sentences, tangents, decisions buried in discussion. You need to turn this into a clear recap that everyone can reference, with unambiguous action items and owners.

## The Prompt

```
You are an engineering leader turning raw meeting notes into a structured recap. Extract the signal from the noise: decisions made, action items with owners and dates, and open questions. Ignore social chat and tangents.

Structure:
1. **Meeting summary** — 2-3 sentences covering the purpose and key outcome
2. **Decisions made** — numbered list of what was decided, with rationale if captured
3. **Action items** — table with: action, owner, due date
4. **Open questions** — unresolved items that need follow-up
5. **Parking lot** — topics raised but deferred

Meeting: [MEETING_NAME]
Date: [DATE]
Attendees: [ATTENDEES]
Purpose: [MEETING_PURPOSE]

Raw notes:
[PASTE_RAW_NOTES]
```

## Example Input

```
Meeting: API Strategy Sync
Date: March 12
Attendees: Me, Carla (PM), Dev (API lead), Suki (security), Fran (DevRel)
Purpose: Decide on API versioning strategy for the public API launch

Raw notes:
- Carla: we need to launch public API by end of Q2, customers are asking
- Dev: three options — URL versioning (/v1/), header versioning, or query param
- long discussion about backward compat
- Suki raised concern about auth tokens — do we need separate tokens for public API?
- decided: URL versioning, it's the most visible and easiest for developers
- Dev will write the RFC by March 20
- Fran wants to start on docs but needs the endpoint spec first
- talked about rate limiting — no decision, need more data on current usage patterns
- Carla mentioned the pricing team wants to tie API access to plan tiers — parking lot for now
- Suki will do a security review of the auth flow by March 25
- someone mentioned webhooks but we ran out of time
```

## Example Output

> **API Strategy Sync — Recap (March 12)**
>
> **Summary:** Met to decide on API versioning strategy ahead of the Q2 public API launch. Agreed on URL-based versioning. Key follow-ups are the versioning RFC and security review of the auth flow. Rate limiting and pricing-tier integration need separate discussions.
>
> **Decisions**
> 1. **URL-based versioning** (e.g., `/v1/users`) — chosen over header and query param versioning for developer visibility and simplicity. This is our approach for the public API launch.
>
> **Action Items**
> | Action | Owner | Due |
> |--------|-------|-----|
> | Write versioning RFC with endpoint structure | Dev | March 20 |
> | Security review of public API auth flow (separate tokens question) | Suki | March 25 |
> | Share endpoint spec with DevRel once RFC is approved | Dev → Fran | After RFC approval |
> | Pull current API usage data to inform rate limiting discussion | Dev | March 22 |
>
> **Open Questions**
> - Do we need separate auth tokens for the public API, or can we extend the current token system? (Suki investigating as part of security review)
> - What rate limits are appropriate? Blocked on usage data analysis.
>
> **Parking Lot**
> - Tying API access to pricing plan tiers (Carla to coordinate with pricing team separately)
> - Webhook support for public API (raised but not discussed — needs its own session)

## Tuning Notes

- **Decision-heavy meeting:** Expand the "Decisions" section with brief rationale for each. This becomes the reference document for "why did we decide X?"
- **Brainstorm/ideation meeting:** Replace "Decisions" with "Key ideas discussed" and "Themes that emerged." Not every meeting produces decisions.
- **Executive meeting:** Shorten to decisions + actions only. Execs don't need the parking lot.
- **Recurring meeting (e.g., weekly sync):** Add a "Status of previous action items" section at the top showing what was completed from last time.
