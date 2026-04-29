# Sprint Planning Breakdown

## Situation

You have an epic or large feature that needs to be broken into sprint-sized tickets. The goal is well-scoped stories that a single engineer can complete in 1-3 days, with clear acceptance criteria and dependencies mapped.

## The Prompt

```
You are an engineering leader breaking down an epic into sprint-ready tickets. Each ticket should be independently deliverable (or clearly marked as blocked by another ticket), estimated, and have clear acceptance criteria. Optimise for parallel work where possible.

Structure:
1. **Epic summary** — what we're building and the definition of done for the whole epic
2. **Ticket breakdown** — each ticket with: title, description, acceptance criteria, estimate (in days), dependencies, suggested assignee level (senior/mid/junior)
3. **Dependency graph** — which tickets block others (simple list or visual)
4. **Sprint allocation** — how the tickets map across sprints given team capacity
5. **Risks** — what's underestimated or uncertain

Epic: [EPIC_DESCRIPTION]
Definition of done: [EPIC_DOD]
Team: [TEAM_SIZE_AND_COMPOSITION]
Sprint length: [SPRINT_LENGTH]
```

## Example Input

```
Epic: Add CSV export functionality to the admin dashboard. Users should be able to export any data table in the admin panel as a CSV file. Tables include: users, orders, transactions, and audit logs. Some tables have 500K+ rows so we need server-side generation with progress indication. Must respect role-based access — admins see all columns, managers see a subset.

Definition of done: All 4 tables exportable as CSV with role-based column filtering, server-side generation for large exports, progress indicator, and download notification.

Team: 4 engineers (1 senior backend, 1 mid backend, 1 senior frontend, 1 mid frontend)
Sprint length: 2 weeks
```

## Example Output

> **Epic: CSV Export for Admin Dashboard**
>
> **Summary:** Enable CSV export for all 4 admin data tables (users, orders, transactions, audit logs) with role-based column filtering and server-side generation for large datasets.
>
> **Ticket Breakdown**
>
> **Backend**
>
> | # | Title | Description | Acceptance Criteria | Est. | Dep. | Level |
> |---|-------|-------------|-------------------|------|------|-------|
> | B1 | CSV generation service | Create a service that accepts a table name, column list, and filter params, then generates a CSV file server-side | - Service generates valid CSV for all 4 tables | 2d | None | Senior |
> | | | | - Handles 500K+ rows without memory issues (streaming) | | | |
> | | | | - Unit tests for each table's export | | | |
> | B2 | Role-based column filtering | Add column filtering logic based on user role (admin vs manager) | - Admin role exports all columns | 1.5d | B1 | Mid |
> | | | | - Manager role exports permitted subset per table | | | |
> | | | | - Unpermitted column requests return 403 | | | |
> | B3 | Background job + progress tracking | CSV generation runs as a background job with progress stored in Redis | - Job queued and processed asynchronously | 2d | B1 | Senior |
> | | | | - Progress percentage queryable via API endpoint | | | |
> | | | | - Job timeout after 10 minutes with error state | | | |
> | B4 | Download API endpoint | Secure endpoint to download completed CSV files with signed URLs | - Signed URL expires after 1 hour | 1d | B3 | Mid |
> | | | | - Only the requesting user can download their export | | | |
>
> **Frontend**
>
> | # | Title | Description | Acceptance Criteria | Est. | Dep. | Level |
> |---|-------|-------------|-------------------|------|------|-------|
> | F1 | Export button component | Add "Export CSV" button to each data table header | - Button visible on all 4 table pages | 1d | None | Mid |
> | | | | - Button triggers export API call | | | |
> | | | | - Button disabled while export in progress | | | |
> | F2 | Progress indicator | Show export progress in a toast/banner component | - Progress bar updates in real-time (polling every 2s) | 1.5d | B3, F1 | Senior |
> | | | | - Shows "Generating... X%" while in progress | | | |
> | | | | - Error state if job fails or times out | | | |
> | F3 | Download notification | Show download link when export is complete | - Notification with "Download" link appears when ready | 1d | B4, F2 | Mid |
> | | | | - Link triggers file download | | | |
> | | | | - Notification dismissible | | | |
> | F4 | Export column selection (optional) | Allow users to select which columns to include before export | - Checkbox list of available columns (role-filtered) | 1.5d | B2, F1 | Senior |
> | | | | - Default: all permitted columns selected | | | |
>
> **Dependency Graph**
> ```
> B1 ──→ B2
> B1 ──→ B3 ──→ B4
> F1 (parallel with B1-B4)
> B3 + F1 ──→ F2 ──→ F3
> B2 + F1 ──→ F4
> ```
>
> **Sprint Allocation**
>
> *Sprint 1 (all engineers can start on day 1):*
> - Senior Backend: B1 (2d) → B3 (2d) → B4 (1d)
> - Mid Backend: Assist on B1 testing (1d) → B2 (1.5d) → available for F4 backend support
> - Senior Frontend: F1 (1d) → F2 (1.5d, once B3 is done mid-sprint)
> - Mid Frontend: F1 support/testing → F3 (1d, late sprint once F2 is ready)
>
> *Sprint 2 (expected: polish + F4):*
> - F4 (column selection): 1.5d
> - Integration testing across all roles: 1d
> - Bug fixes and polish: 1-2d
> - Sprint 2 has ~60% capacity free for other work
>
> **Risks**
> - Large table export (500K+ rows) performance is hard to estimate precisely. B1 should include a performance test with realistic data volumes early.
> - Role-based column definitions need product input — which columns does each role see? Get this defined before sprint starts.
> - Real-time progress tracking adds complexity. If it proves tricky, fall back to a simpler "Export started, we'll notify you when it's ready" approach.

## Tuning Notes

- **Uncertain scope:** Add a "spike" ticket at the start: "Investigate [unknown] and produce a revised estimate." Timeboxed to 1-2 days.
- **Solo developer:** Remove the parallelism and sequence linearly. Still break into small tickets — it aids focus and gives you clear commit points.
- **Non-technical PM reviewing:** Add a "user story" format to each ticket: "As an admin, I can export the users table as CSV so that I can share user data with the finance team."
- **Tech debt epic:** Same format, but acceptance criteria should include "existing tests still pass" and "no regression in [metric]."
