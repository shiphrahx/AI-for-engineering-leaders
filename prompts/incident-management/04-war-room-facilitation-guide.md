# War Room Facilitation Guide

## Situation

You've called a war room for a live incident. There are 5-15 people on the call, some panicking, some debugging, some just watching. You need to facilitate effectively — keep it focused, prevent chaos, and drive to resolution without micromanaging the debugging.

## The Prompt

```
You are an Incident Commander facilitating a war room during a live incident. Create a facilitation guide that keeps the room productive. The IC's job is to coordinate, not to debug. Structure the room so the right people are working on the right things and information flows clearly.

Structure:
1. **Room setup** — opening the war room, who to invite, how to structure the call
2. **First 5 minutes script** — exactly what to say when the room opens
3. **Running the room** — cadence of check-ins, how to manage parallel workstreams
4. **Decision templates** — pre-built frameworks for common war room decisions
5. **Anti-patterns** — what NOT to do as facilitator
6. **Closing the room** — when and how to stand down

Incident context:
- Severity: [SEVERITY]
- Service affected: [SERVICE]
- People in the room: [ROLES_PRESENT]
- What's known so far: [CURRENT_STATUS]
```

## Example Input

```
- Severity: P0 — full API outage
- Service: API gateway — all customer-facing API calls failing
- People: IC (me), 2 backend engineers, 1 SRE, 1 EM, 1 VP Eng (observing), CS lead
- Known: API gateway returning 502s starting 10 minutes ago. No recent deploys. Traffic looks normal. Health checks failing on 3 of 5 gateway pods.
```

## Example Output

> **War Room Facilitation — API Gateway P0**
>
> ---
>
> **Room Setup**
> - Zoom link posted to #incidents with "P0 WAR ROOM — API Gateway — Join Now"
> - Mute all on entry. IC controls who speaks.
> - Shared screen: Datadog dashboard for API gateway metrics
> - Slack thread: #incident-2025-03-15 for async notes and links (not for discussion — that happens on the call)
>
> ---
>
> **First 5 Minutes — Opening Script**
>
> *Say this verbatim if you're nervous. It sets the tone and structure.*
>
> "Okay, I'm IC for this incident. Here's what we know:
>
> The API gateway has been returning 502s for the last 10 minutes. All customer-facing API calls are affected. Three of five gateway pods are failing health checks. There were no recent deploys and traffic is normal.
>
> Here's how we're going to work:
> - **[SRE name], you're Tech Lead.** Your job is to diagnose and fix. Narrate what you're looking at and what you're trying so we all stay aligned.
> - **[Backend eng names], you're supporting.** [SRE] will direct your investigation. Check with them before running any commands in production.
> - **[CS lead], you're on comms.** I'll give you updates every 10 minutes for Statuspage and CS team. First update goes out in 5 minutes.
> - **[EM and VP], you're observing.** I'll escalate to you if I need decisions outside my authority.
>
> Nobody else should be running commands in production without checking with [SRE] first. Let's go."
>
> ---
>
> **Running the Room**
>
> **Every 10 minutes, IC does a round:**
> 1. "[Tech Lead], status check. What have you tried, what have you learned, what are you trying next?"
> 2. Update the Slack thread with a summary
> 3. Give Comms Lead the customer-facing update
> 4. Ask: "Does anyone have information that the Tech Lead doesn't have?"
>
> **If parallel workstreams develop:**
> - "Okay, [Engineer A], you're investigating the pod health checks. [Engineer B], you're looking at upstream dependencies. Check back in 10 minutes. Don't overlap."
> - Track workstreams on a shared doc or Slack thread: who's investigating what.
>
> **If someone proposes a fix:**
> - "What's the fix? What's the risk? What's the rollback if it makes things worse?"
> - If the risk is low: "Go ahead, let us know when it's applied."
> - If the risk is high: "Let's discuss for 60 seconds, then I'll make the call."
>
> ---
>
> **Decision Templates**
>
> *Should we roll back?*
> - Was there a recent change (deploy, config, infra)? → Yes? Roll back first, debug second.
> - Is rollback safe (no irreversible migrations)? → Yes? Do it now.
> - IC says: "We're rolling back [change]. [Name], execute the rollback. Everyone else, hold."
>
> *Should we escalate?*
> - No progress in 30 minutes → Escalate to the next person in the chain
> - Scope expanding (more services affected) → Escalate immediately
> - Potential data loss or security implications → Escalate immediately and add legal/security
> - IC says: "I'm escalating to [person]. [Name], page them now."
>
> *Should we try a risky fix?*
> - "The fix is [X]. If it works, service is restored. If it fails, [Y happens]. The rollback for the fix is [Z]. I'm approving it. [Name], proceed. Everyone else monitor."
>
> ---
>
> **Anti-Patterns — Do NOT Do These**
>
> - ❌ **Debug alongside the Tech Lead.** Your job is to facilitate, not investigate. If you start debugging, no one is coordinating.
> - ❌ **Let everyone talk at once.** "Hold on — one voice at a time. [Name], finish your thought."
> - ❌ **Ignore the observers.** If the VP asks a question mid-investigation, say: "Good question — I'll address that at the next 10-minute update. Let's keep [Tech Lead] focused."
> - ❌ **Go silent for 15+ minutes.** Even if there's nothing new, post "Still investigating, no change. Next update in 10 minutes." Silence breeds anxiety.
> - ❌ **Let the room grow unchecked.** If people join who aren't needed: "Thanks for joining. We have the right people working on it. I'll post updates in #incidents — you can follow there."
>
> ---
>
> **Closing the Room**
>
> When to close:
> - Metrics have returned to baseline for 15+ minutes
> - Tech Lead confirms the fix is stable
> - No new errors in monitoring
>
> Closing script:
> "Metrics have been stable for 15 minutes. [Tech Lead] confirms the fix is holding. I'm declaring this incident resolved at [time]. Total duration: [X minutes].
>
> Next steps: [Tech Lead name] will write the postmortem. Postmortem review is scheduled for [date]. Thank you all — great response. Go take a break."
>
> Post to #incidents: final summary, duration, root cause (if known), postmortem owner, and a thank-you to everyone involved.

## Tuning Notes

- **You're IC and the only person who knows the system:** You may need to debug AND facilitate. Narrate out loud what you're doing so others can follow. Ask someone else to handle comms updates.
- **Too many people in the room:** "I appreciate everyone's concern. Right now I need [names] active. Everyone else, please follow #incidents for updates and drop off this call to free up bandwidth."
- **Senior leader is trying to take over:** "Thanks for the input. I'm running this incident — I'll incorporate your suggestion. [Tech Lead], what's your assessment?" Maintain authority calmly.
- **Practice this:** Run a tabletop exercise using this guide before a real incident. Muscle memory beats reading a runbook at 3am.
