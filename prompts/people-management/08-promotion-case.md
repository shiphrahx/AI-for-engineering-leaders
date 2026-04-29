# Promotion Case

## Situation

You have a direct report who's ready for promotion and you need to build a compelling case for the promo committee or your leadership chain. The case needs to show that this person is already operating at the next level, not just doing their current job well.

## The Prompt

```
You are an engineering manager building a promotion case for a direct report. The case should demonstrate that the person is consistently operating at the next level — not aspirationally, but with concrete evidence. Focus on impact, scope, and influence, not just output.

Structure:
1. **Summary recommendation** — one paragraph: who, from what level to what level, and why
2. **Evidence of next-level performance** — 3-5 specific examples mapped to the expectations of the target level
3. **Peer and stakeholder perspective** — what others say about this person's impact
4. **Growth trajectory** — how they've grown during the review period
5. **Readiness signals** — why now, not 6 months from now
6. **Potential concerns and counterarguments** — address the objections the committee might raise

Person: [NAME], current level: [CURRENT], proposed level: [TARGET]
Level expectations at target: [TARGET_LEVEL_EXPECTATIONS]
Evidence: [PASTE_ACCOMPLISHMENTS_AND_EXAMPLES]
Peer perspectives: [PASTE_PEER_FEEDBACK]
```

## Example Input

```
Person: Mei, current L4 (Mid), proposing L5 (Senior)
Target level expectations: Drives complex projects with minimal guidance, mentors others, contributes to technical direction, has influence beyond immediate team.

Evidence:
- Led the search re-indexing project (3 months, involved 2 other engineers). Designed the migration strategy, managed the rollback plan, and delivered on time. Search latency improved 40%.
- Wrote 2 RFCs this year — one for the caching strategy (adopted org-wide) and one for API pagination standards (adopted by 3 teams).
- Mentored Ben (L3) through his first quarter. Ben's review cited Mei as the primary reason for his ramp-up speed.
- Identified and led the fix for a recurring memory leak that had caused 3 P2 incidents. Nobody had prioritised this — Mei did the investigation on her own initiative.
- Regularly consulted by the Platform team on search-related decisions even though she's on the Product team.

Peer feedback:
- "Mei is the person I go to when I'm stuck on a hard problem." (Platform engineer)
- "Her RFC on caching was the clearest technical document I've read here." (Staff engineer)
- "Mei helped me grow more in 3 months than my previous mentor did in a year." (Ben, L3)
```

## Example Output

> **Promotion Recommendation: Mei, L4 → L5 (Senior Engineer)**
>
> **Summary**
> I'm recommending Mei for promotion to Senior Engineer (L5). Over the past two review periods, Mei has consistently demonstrated L5 behaviours: leading complex multi-engineer projects, contributing to org-wide technical direction through adopted RFCs, mentoring junior engineers, and having measurable influence beyond her immediate team. She's not growing into L5 — she's already operating there.
>
> **Evidence of L5 Performance**
>
> *Drives complex projects with minimal guidance:*
> Mei led the search re-indexing project over 3 months, coordinating 2 other engineers, designing the migration strategy, and managing the rollback plan. She identified risks early, adjusted the approach when the initial strategy hit a snag with legacy indices, and delivered on schedule. Result: 40% improvement in search latency, directly measurable in customer-facing performance metrics.
>
> *Contributes to technical direction:*
> Mei authored two RFCs this year. Her caching strategy RFC was adopted org-wide and is now the standard approach for all services. Her API pagination RFC was adopted by 3 teams. A Staff engineer described the caching RFC as "the clearest technical document I've read here." Authoring adopted, org-level technical standards is a clear L5+ signal.
>
> *Mentors others:*
> Mei mentored Ben (L3) during his first quarter. Ben's subsequent performance review specifically cited Mei as the reason for his rapid ramp-up. Ben himself said Mei helped him grow more in 3 months than his previous mentor had in a year. This isn't casual helpfulness — it's deliberate, impactful mentoring.
>
> *Initiative and ownership beyond assigned work:*
> Mei identified a recurring memory leak that had caused 3 P2 incidents. This wasn't on anyone's roadmap — she investigated on her own initiative, diagnosed the root cause, and led the fix. This is the kind of proactive, org-improving behaviour that distinguishes L5 from L4.
>
> *Influence beyond immediate team:*
> The Platform team regularly consults Mei on search-related architectural decisions, despite her being on the Product team. This cross-team influence is organic — people seek her out because her judgment is trusted.
>
> **Peer and Stakeholder Perspective**
> Feedback from peers outside Mei's team consistently describes her as someone they go to for hard problems and whose technical writing sets a quality bar. Notably, recognition comes from a Staff engineer and from engineers on other teams — this isn't just within-team appreciation.
>
> **Growth Trajectory**
> When Mei joined 2 years ago, she was a strong individual contributor focused on her own deliverables. Over the past year, she's shifted from "excellent at execution" to "excellent at leading execution and improving the org's technical foundations." The RFC contributions and the mentoring are new behaviours, not things she's always done.
>
> **Why Now**
> Mei has been operating at L5 for at least two quarters. The evidence above isn't aspirational — every item is a completed, demonstrable contribution. Delaying the promotion risks both recognition debt (she deserves the title she's earning) and retention risk (Mei is aware of her market value).
>
> **Potential Concerns**
> - *"She hasn't led a team-sized project yet":* The search re-indexing project involved 3 engineers over 3 months, which is appropriate L5 scope. L5 doesn't require managing a team — it requires driving complex work across people. She did that.
> - *"Only 2 years of tenure":* Tenure is not a promotion criterion. The ladder specifies behaviours and impact, both of which Mei demonstrates. Holding promotions for time-served sends the wrong signal to high performers.

## Tuning Notes

- **Weak evidence:** If you're struggling to find 3+ concrete examples at the next level, the person may not be ready. It's better to have the "here's what you need to do" conversation than to submit a thin case that gets rejected.
- **Committee is conservative:** Front-load the strongest evidence. Lead with the example that most clearly maps to the target level's expectations. Include direct quotes from respected peers.
- **Skip-level promotion (e.g., L3 → L5):** Extremely rare and requires exceptional evidence. If you're considering this, talk to your skip-level first to gauge feasibility.
- **Your org doesn't have a formal committee:** This format still works as a document you share with your manager to get alignment before telling the engineer.
