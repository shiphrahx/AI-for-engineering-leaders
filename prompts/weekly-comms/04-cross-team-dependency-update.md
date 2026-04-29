# Cross-Team Dependency Update

## Situation

Your team depends on other teams (or other teams depend on you), and you need to send a clear, non-confrontational update that surfaces blockers and handoff status without pointing fingers.

## The Prompt

```
You are an engineering leader writing a dependency status update to be shared across multiple teams. The tone must be collaborative and solution-oriented — never blame, always offer a path forward. Focus on what each team needs to know and do.

Structure:
1. **Dependency map summary** — who needs what from whom, one line per dependency
2. **On track** — dependencies that are healthy
3. **Needs attention** — dependencies at risk, with specific impact if delayed and a suggested resolution
4. **Asks** — one clear action per team, with a date

Context:
- My team: [MY_TEAM]
- Dependent teams: [OTHER_TEAMS]
- Project/initiative: [PROJECT_NAME]
- Key dates: [KEY_DATES]

Current dependency status:
[PASTE_DEPENDENCY_NOTES]
```

## Example Input

```
- My team: Mobile Squad
- Dependent teams: API Platform, Design Systems, QA
- Project: Mobile app redesign v2
- Key dates: Beta launch April 1, full launch April 15

Dependency status:
- API Platform: We need the new user profile endpoint (v3). They said "end of March" but no PR yet and it's March 18. We have a workaround using v2 + client-side transform but it's slower and we'd have to rip it out later.
- Design Systems: New component library tokens shipped last week, we've integrated 80%. Remaining 20% is blocked on an icon set update they said is coming "this week."
- QA: We need their regression test suite updated for the new navigation patterns. Haven't heard back on our request from March 10.
```

## Example Output

> **Mobile Redesign v2 — Dependency Check-in (March 18)**
>
> Quick sync on where our cross-team dependencies stand against the April 1 beta deadline.
>
> **Dependency Map**
> - Mobile ← API Platform: user profile endpoint v3
> - Mobile ← Design Systems: icon set update for component library
> - Mobile ← QA: updated regression suite for new navigation
>
> **On Track**
> - ✅ Design Systems component library tokens: 80% integrated, going well
>
> **Needs Attention**
> - 🟡 **API Platform — profile endpoint v3:** We're currently targeting the v3 endpoint for beta. Without it by March 25, we'll ship beta on a v2 workaround that adds ~200ms latency to profile loads and creates rework for the full launch. *Proposed path:* Can we get a quick check-in this week to confirm a commit date? If v3 won't land by March 25, we'll plan for the workaround now rather than scrambling later.
> - 🟡 **Design Systems — icon set update:** Last 20% of component integration is waiting on this. Low risk if it lands this week as planned, but it cascades quickly if it slips since every screen uses the icon set.
> - 🟡 **QA — regression suite update:** We sent the navigation spec on March 10 but haven't heard back. Beta testing needs to start March 28, so we'd need the suite updated by March 26 at the latest.
>
> **Asks**
> | Team | Action | By When |
> |------|--------|---------|
> | API Platform | Confirm v3 endpoint delivery date or flag that we should plan for workaround | March 20 |
> | Design Systems | Ship icon set update | March 22 |
> | QA | Acknowledge regression suite request and share an ETA | March 20 |
>
> Happy to jump on a call with anyone this week to sort things out. No surprises, just trying to keep us all aligned.

## Tuning Notes

- **Escalation needed:** If you've sent this update twice with no movement, add your skip-level and the other team's manager on the next update. Keep the same tone — the CC is the escalation, not the language.
- **Your team is the blocker:** Same format, but lead with your own team's status and be direct about what you're doing to unblock others.
- **Slack-native culture:** Shorten to a table: Dependency | Status | Ask | Date. Post in a shared channel and @ the relevant leads.
- **Large org:** Add a RACI-style column showing who the decision maker is if timelines can't be met.
