# Codebase Orientation Brief

## Situation

You've inherited a service, joined a new team, or need to speak credibly about a system you don't own — in a review, incident, or planning meeting. You want a fast, honest map of the code: what it does, its shape, where the risk is, and what to ask the team.

## The Prompt

```
You are helping an engineering leader get oriented in an unfamiliar codebase — enough to ask sharp questions and judge risk, not to override the engineers who own it. Map the territory and mark the unknowns; never assert behaviour you haven't verified.

Produce:
1. What it does — two sentences.
2. Shape — major components and their roles, the primary data flow, external dependencies.
3. Entry points & hot paths — where execution starts and where the real work happens.
4. Risk & load-bearing parts — fragile, complex, or untested areas. Distinguish "I read this and it's risky" from "couldn't tell — ask the team".
5. Conventions & gaps — how it's tested/built/deployed as far as visible, and what you could NOT determine.
6. Questions to ask the team — the specific ones that close the biggest unknowns.

Cite file paths for claims. Mark anything you can't verify as Unknown.

Why I'm orienting: [REASON, e.g. inherited the team / incident tomorrow / planning input]
Depth: [QUICK_SKIM / DEEPER_MAP]
Codebase: [PASTE_STRUCTURE_KEY_FILES_OR_REPO_ACCESS]
What I already know: [ANYTHING_KNOWN]
```

## Example Input

```
Why I'm orienting: I just inherited the notifications team and have a roadmap meeting Thursday.
Depth: Quick skim.
Codebase: notifications-service — Node. Dirs: /api, /workers, /templates, /queue. Entry: api/server.js, workers/dispatch.js. Uses Redis + SendGrid. ~140 files.
What I already know: It sends transactional email and push. Occasional delivery delays reported.
```

## Example Output

> **Orientation: notifications-service** — inherited team, roadmap prep
>
> **What it does:** Sends transactional email and push notifications triggered by events from other services. API accepts send requests; workers pull from a Redis queue and dispatch via SendGrid.
>
> **Shape**
> - API (`api/server.js`) — accepts + validates send requests
> - Dispatch workers (`workers/dispatch.js`) — pull from queue, render, send
> - Templates (`templates/`) — message bodies
> - Primary flow: event → API → Redis queue → worker → SendGrid
> - External deps: Redis (queue), SendGrid (delivery)
>
> **Entry points & hot paths:** `workers/dispatch.js` is the hot path — all delivery flows through it; likely where the reported delays live.
>
> **Risk & load-bearing**
> - ⚠️ `workers/dispatch.js` — single worker loop, no visible retry/backoff on SendGrid failures (couldn't confirm — ask team). Delivery delays plausibly originate here.
> - ⚠️ No tests visible under `/workers` — the riskiest code is the least covered.
>
> **Conventions & gaps:** Tests present for `/api`, absent for workers. Deploy mechanism not determinable from the code.
>
> **Questions to ask the team**
> - What causes the delivery delays — queue backlog, SendGrid throttling, or worker throughput?
> - Is there retry/dead-letter handling for failed sends, and where?
> - Who owns the SendGrid account limits?

## Tuning Notes

- **Depth shift:** For quick meeting-prep, ask for just What-it-does, Shape, and Questions. For a decision, request the full risk map and conventions.
- **Access shift:** If you can only paste snippets, tell the model to scope its claims to what it saw and flag the rest as Unknown — don't let it extrapolate a whole architecture from three files.
- **Common pitfall:** Watch for confident assertions about behaviour it hasn't read. Every risk claim should cite a path or be marked "ask the team".
- **Scale shift:** For a large monorepo, orient on one module at a time rather than asking for the whole thing at once.
