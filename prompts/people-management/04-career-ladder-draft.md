# Career Ladder Draft

## Situation

You need to create or refine engineering level expectations for your team or org. This could be a new ladder for a growing startup, or revising an existing one that's become disconnected from how people actually work and get promoted.

## The Prompt

```
You are an engineering leader drafting a career ladder for your engineering organisation. Each level should have clear, observable expectations — not vague competencies. Someone should be able to read a level description and know whether they're meeting it. Focus on scope of impact, autonomy, and leadership rather than just technical skill.

Structure per level:
1. **Level title and summary** — one-sentence description of what this level means
2. **Scope** — what's the typical sphere of influence (task, feature, project, team, org, company)
3. **Technical expectations** — what technical work looks like at this level
4. **Collaboration & communication** — how they work with others
5. **Leadership** — how they lead (not manage) at this level
6. **Example behaviours** — 3-4 concrete "you'd see this person doing..." examples

Organisation context:
[ORG_SIZE_AND_STAGE]

Levels to define:
[LEVEL_LIST]

Current pain points with existing ladder (if any):
[PAIN_POINTS]
```

## Example Input

```
Org: 50-engineer startup, growing to 80 this year. Mix of product and platform teams.
Levels: L3 (Junior), L4 (Mid), L5 (Senior), L6 (Staff)
Pain points: Current ladder is too vague ("demonstrates technical excellence" doesn't mean anything). People don't know what they need to do to get promoted. Senior-to-Staff gap is unclear — some L5s are more impactful than some L6s.
```

## Example Output

> **Engineering Career Ladder**
>
> ---
>
> **L3 — Junior Engineer**
> *Builds well-defined features with guidance and is learning the codebase, tools, and practices of the team.*
>
> **Scope:** Individual tasks and well-scoped features within a single service or component.
>
> **Technical:** Writes functional, tested code that follows team conventions. Can debug issues in their area with guidance. Asks questions when stuck rather than spinning. Submits PRs that get progressively smaller in review feedback over time.
>
> **Collaboration:** Participates in code reviews (reviewing and receiving). Communicates progress and blockers in standup. Asks for help within a reasonable timeframe.
>
> **Leadership:** Leads their own learning. Documents what they learn for the next new hire.
>
> **Example behaviours:**
> - Picks up a well-scoped ticket, asks clarifying questions, and delivers it within the sprint
> - Writes a useful PR description that explains the "why" not just the "what"
> - Adds a page to the team wiki after figuring out something that wasn't documented
> - Asks a senior engineer for a pairing session when stuck on an unfamiliar part of the codebase
>
> ---
>
> **L4 — Mid-Level Engineer**
> *Independently delivers features of moderate complexity and is becoming a reliable contributor the team depends on.*
>
> **Scope:** Features and projects within their team. Can own a feature from design through deployment.
>
> **Technical:** Designs and implements features with moderate complexity independently. Considers edge cases, error handling, and performance. Writes code that other engineers can understand and maintain. Reviews PRs with useful, constructive feedback.
>
> **Collaboration:** Communicates technical trade-offs to PMs and designers. Can work with engineers on other teams when projects require coordination. Gives and receives feedback constructively.
>
> **Leadership:** Mentors L3 engineers informally. Identifies small process improvements and implements them.
>
> **Example behaviours:**
> - Takes a product requirement, writes a brief design approach, gets feedback, and delivers the feature across 2-3 PRs
> - Notices a flaky test, investigates the root cause, and fixes it without being asked
> - Runs a sprint demo and explains the feature's value to non-technical stakeholders
> - Gives a code review that teaches the author something new about the codebase
>
> ---
>
> **L5 — Senior Engineer**
> *Drives complex projects with minimal guidance and has a measurable impact on their team's effectiveness.*
>
> **Scope:** Projects that span weeks or months, often involving multiple engineers or teams. Owns technical direction for their area.
>
> **Technical:** Designs systems that are maintainable and scalable. Anticipates future requirements without overengineering. Makes sound trade-off decisions and can articulate the reasoning. Identifies and addresses tech debt that affects team velocity.
>
> **Collaboration:** Can drive alignment across teams on technical decisions. Translates business requirements into technical plans. Communicates risk and complexity to non-technical stakeholders effectively.
>
> **Leadership:** Mentors L3-L4 engineers deliberately. Sets technical standards for their area. Drives improvements to team processes, tools, and practices. Can lead a project involving 2-4 engineers.
>
> **Example behaviours:**
> - Writes an RFC for a system change, solicits feedback, iterates, and drives it to a decision
> - Identifies that the team's deploy pipeline is the bottleneck, proposes a fix, and leads the implementation
> - Mentors a mid-level engineer through their first system design, giving feedback that elevates their thinking
> - Pushes back on a product requirement with a simpler alternative that delivers 80% of the value in 20% of the time
>
> ---
>
> **L6 — Staff Engineer**
> *Defines technical direction across multiple teams and has measurable impact at the organisational level.*
>
> **Scope:** Multiple teams or the full engineering organisation. Solves problems that no single team owns.
>
> **Technical:** Makes architectural decisions that affect the whole platform. Identifies systemic technical risks and creates plans to address them. Balances short-term delivery with long-term technical health. Is the person other senior engineers consult on their hardest problems.
>
> **Collaboration:** Builds consensus across teams with competing priorities. Represents engineering in executive-level discussions. Can explain complex technical trade-offs to the CEO in business terms. Creates alignment where none existed.
>
> **Leadership:** Sets technical standards and practices for the engineering org, not just their team. Grows senior engineers by giving them increasingly complex problems and coaching them through the ambiguity. Identifies organisational problems (not just technical ones) and proposes solutions.
>
> **Example behaviours:**
> - Identifies that three teams are building similar caching layers, proposes a shared solution, and leads the cross-team effort to build it
> - Writes the engineering strategy document that shapes the org's technical direction for the next year
> - Coaches a senior engineer through a failed project in a way that turns it into a career growth moment
> - Notices a gap between how product and engineering think about reliability, and creates an SLO framework that gives both teams a shared language
>
> ---
>
> **The L5→L6 Distinction**
> The difference isn't "bigger projects" — it's *scope of impact and ambiguity*. An L5 drives a complex project within a defined problem space. An L6 identifies the problem space itself, often across team boundaries, and creates clarity where there was confusion. An L5 is excellent within their team's domain. An L6 reshapes how multiple teams work together.

## Tuning Notes

- **Startup (< 30 engineers):** You may only need L3-L5. Adding Staff before you have 50+ engineers can create a title without a role.
- **Adding management track:** Mirror the IC ladder with an EM track that has overlapping scope expectations but diverging "how" — managers lead through people, ICs lead through technical influence.
- **Existing ladder that needs updating:** Keep the level names and add "distinguishing behaviours" — the 2-3 things that most clearly separate one level from the next.
- **Diverse team backgrounds:** Avoid culture-specific expectations (e.g., "speaks up in meetings" disadvantages introverts and non-native speakers). Focus on impact and outcomes, not style.
