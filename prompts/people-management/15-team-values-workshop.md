# Team Values Workshop

## Situation

You want to define or revisit your team's working values — not a list of platitudes, but a short set of principles that actually guide how the team makes decisions, gives feedback, and resolves disagreements. You need a facilitation plan for a workshop that produces something real.

## The Prompt

```
You are an engineering manager designing a team values workshop.

Create a facilitation plan for a [DURATION] workshop to define (or revisit) team values. Include:

1. **Pre-work** (what participants should do or think about before the session)
2. **Session agenda** with time allocations and facilitation notes for each segment
3. **The core exercise** — the specific activity that generates candidate values, with step-by-step instructions
4. **Synthesis method** — how to go from a wall of ideas to 4-6 usable values
5. **Output template** — the format each value should be captured in (not just a word, but a definition and a "this means we..." statement)
6. **Follow-through** — what to do in the week after the workshop so the values don't die in a doc

Context:
- Team: [TEAM_NAME], [HEADCOUNT] people
- Duration: [e.g. 90 minutes]
- Format: [in-person / remote / hybrid]
- Why now: [new team forming / values feel stale / post-reorg / other]
```

## Example Input

```
- Team: Data Platform, 7 engineers + EM
- Duration: 90 minutes
- Format: Remote (Miro + Zoom)
- Why now: Team doubled in size over 6 months, original norms aren't holding
```

## Example Output

> **Team Values Workshop — Data Platform**
> *90 minutes | Remote | Miro*
>
> ---
>
> **Pre-work (sent 2 days before)**
> Ask each person to come with answers to two questions:
> 1. Describe a moment on this team (or a previous team) where you felt proud of how something was handled. What made it feel right?
> 2. Describe a friction point you've experienced here. What value, if we held it clearly, would have helped?
>
> No need to write essays — bullet points are fine. Tell them this feeds the workshop directly.
>
> ---
>
> **Agenda**
>
> | Time | Segment | Notes |
> |------|---------|-------|
> | 0:00 | Framing (5 min) | Why we're here; what we're making; what we're not making (a poster) |
> | 0:05 | Storytelling round (20 min) | Each person shares 1-2 min from their pre-work. Facilitator captures themes on Miro. No discussion yet. |
> | 0:25 | Candidate generation (15 min) | Silent sticky note round: each person writes values they'd want the team to hold. One per sticky. |
> | 0:40 | Clustering (15 min) | Group silently moves stickies into clusters. Name each cluster. |
> | 0:55 | Prioritisation (10 min) | Dot voting — 3 votes each, pick the clusters that feel most important and most distinctive |
> | 1:05 | Drafting (15 min) | Break into pairs, each pair drafts one value using the output template |
> | 1:20 | Share-back and close (10 min) | Read each draft. Note what needs refinement. Agree on next step. |
>
> ---
>
> **Core exercise: storytelling into themes**
> The pre-work stories are the raw material. As people share, you're listening for patterns — not the specific events, but what they signal. Common themes: trust, speed vs. quality, autonomy, directness, craft. Write these as you hear them. By the end of the round you typically have 8-12 candidate themes. These become the input to the sticky note round.
>
> ---
>
> **Output template for each value**
>
> ```
> Value name (1-3 words)
> Definition (1 sentence — what it means to us specifically)
> This means we... (2-3 concrete behaviours)
> This doesn't mean... (1 common misread to head off)
> ```
>
> Example:
> > **Clarity over comfort**
> > We say the difficult thing rather than avoiding conflict.
> > This means we: give direct feedback in code reviews; name concerns in planning, not after; tell stakeholders bad news early.
> > This doesn't mean: being harsh or skipping empathy. Directness and kindness aren't opposites.
>
> ---
>
> **Follow-through**
> - Polish the 4-6 values into a shared doc within 3 days while the session is fresh
> - Reference them explicitly in the next code review, retro, or decision that tests them
> - Revisit in 3 months: are we actually using them? Which ones need to be retired or sharpened?

## Tuning Notes

- **Existing values that aren't working:** Run the pre-work question as "what value do we claim to hold but don't actually live?" — surfaces the gap more directly.
- **New team with no shared history:** Replace the storytelling round with a "best team you've been on" exercise — what made it good? Works even when there's no shared context yet.
- **In-person:** Replace Miro with physical Post-its. The tactile clustering step is often more energising in person.
- **Short on time (60 min):** Cut the drafting step. Come out of the workshop with candidate clusters, draft the values offline, and review async.
