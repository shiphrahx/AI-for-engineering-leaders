# Feedback Synthesis

## Situation

You've collected peer feedback for a direct report — from 4-6 colleagues — and it's a mix of praise, constructive criticism, and vague platitudes. You need to distill this into a coherent narrative that identifies real patterns and is useful in a review or career conversation.

## The Prompt

```
You are an engineering manager synthesising peer feedback for a direct report. Identify patterns across reviewers, separate signal from noise, and produce a narrative that's fair, specific, and actionable. Distinguish between feedback that multiple people echo (strong signal) and one-off comments (weaker signal). Maintain anonymity of reviewers.

Structure:
1. **Overall narrative** — 2-3 sentences capturing the consensus view
2. **Consistent strengths** — themes mentioned by 2+ reviewers, with anonymised evidence
3. **Consistent growth areas** — themes mentioned by 2+ reviewers, with evidence
4. **Outlier feedback** — notable comments from a single reviewer (could be insightful or context-specific)
5. **Actionable takeaways** — 2-3 specific development recommendations

Person: [NAME], [ROLE]
Number of reviewers: [COUNT]

Raw peer feedback:
[PASTE_ALL_FEEDBACK]
```

## Example Input

```
Person: Tomás, Senior Frontend Engineer
Reviewers: 5 (2 engineers on his team, 1 engineer from another team, 1 PM, 1 designer)

Feedback:
Reviewer A (team engineer): "Tomás is incredibly reliable. When he says something will be done, it gets done. His React code is clean and well-tested. I wish he'd share more of his frontend knowledge with the team — he has a lot of expertise that stays in his head."

Reviewer B (team engineer): "Great to work with, very helpful when I'm stuck. Sometimes his PRs are really large which makes them hard to review. He's very knowledgeable about performance optimisation."

Reviewer C (cross-team engineer): "I worked with Tomás on the shared component library. He was responsive and his code quality was high. Communication could be better — I wasn't always sure where things stood until they were done."

Reviewer D (PM): "Tomás delivers consistently. I'd love to see him push back more on specs when he sees technical issues — sometimes he just builds what's asked without flagging that there's a better approach. His estimates are very accurate."

Reviewer E (designer): "Tomás is detail-oriented with the UI implementation — pixel-perfect work. He's quiet in meetings and I sometimes wonder if he disagrees but doesn't say anything."
```

## Example Output

> **Feedback Synthesis: Tomás**
>
> **Overall Narrative**
> Tomás is viewed as a highly reliable, technically excellent engineer whose code quality and delivery consistency are standout strengths. The consistent development theme is communication: multiple reviewers note that Tomás keeps valuable knowledge and opinions to himself, which limits his influence and makes collaboration harder than it needs to be.
>
> **Consistent Strengths (3+ reviewers)**
> - **Reliability and delivery:** Four of five reviewers mention that Tomás delivers consistently and on time. His PM specifically highlights accurate estimates. This is a core strength that builds trust across the team.
> - **Technical quality:** Code quality is praised by every technical reviewer. Specific callouts include clean React code, thorough testing, and performance optimisation expertise.
> - **Helpfulness:** Two teammates note that Tomás is generous with his time when they're stuck.
>
> **Consistent Growth Areas (2+ reviewers)**
> - **Proactive communication:** Three reviewers independently flag that Tomás doesn't share enough — whether it's status updates (cross-team engineer), technical opinions (PM), or disagreements (designer). This isn't about Tomás being a poor communicator; it's about him under-communicating. His knowledge and judgment are valued when shared — the feedback is that people want *more* of it.
> - **Knowledge sharing:** Two reviewers wish Tomás would share his frontend expertise more broadly. His deep knowledge is "staying in his head" rather than levelling up the team.
>
> **Outlier Feedback**
> - Large PRs (Reviewer B): Only one person raised this, but it's a concrete, actionable item. May be project-specific or may indicate a pattern worth watching.
>
> **Actionable Takeaways**
> 1. **Practise speaking up in meetings:** Start with one technical opinion per meeting — even if it's "I think there's a simpler way to do this." The feedback isn't that Tomás is wrong when he speaks, it's that he's silent when his input would be valuable.
> 2. **Run one knowledge-sharing session this quarter:** A lunch-and-learn on React performance or frontend architecture. This directly addresses the "expertise staying in his head" feedback and builds his visibility.
> 3. **Send brief status updates proactively:** For cross-team work, a short end-of-week message ("here's where things stand") would address the communication gap without requiring Tomás to change his working style dramatically.

## Tuning Notes

- **Conflicting feedback:** If two reviewers say opposite things, note the contradiction and add context: "Reviewer A found Tomás communicative while Reviewer C didn't — this may reflect a difference between within-team and cross-team communication patterns."
- **Sparse feedback:** If reviewers give vague praise ("great engineer, good teammate"), don't inflate it. Note that feedback lacked specifics and consider asking for supplementary examples.
- **Negative-heavy feedback:** Check your own bias. If you're synthesising and your gut is "this is harsher than my experience," say so. Feedback synthesis should include your observations, not just aggregate peer input.
- **Using in a review conversation:** Share the themes, not the raw quotes. "Multiple peers noted X" is sufficient — no need to identify which reviewer said what.
