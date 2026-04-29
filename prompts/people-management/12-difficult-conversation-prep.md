# Difficult Conversation Prep

## Situation

You need to have a hard conversation with a direct report — delivering tough feedback, addressing a conflict, discussing a missed promotion, or raising a behavioural concern. You want to be direct but not harsh, clear but not cold. Preparation is the difference between a productive conversation and a damaging one.

## The Prompt

```
You are an engineering manager preparing for a difficult conversation with a direct report. Help me structure my talking points so I'm clear, kind, and specific. The conversation should leave the person understanding exactly what the issue is, why it matters, and what "better" looks like — without feeling attacked.

Structure:
1. **Opening frame** — how to start the conversation (set the tone, state the purpose)
2. **Core message** — the specific issue, stated directly with evidence (no sandwich method)
3. **Impact statement** — why this matters (to the team, the project, or their career)
4. **Listen** — create space for their perspective
5. **Path forward** — what you want to see change, with specific expectations
6. **Support offer** — how you'll help
7. **Close** — reaffirm the relationship and check how they're feeling

Person: [NAME], [ROLE]
What the conversation is about: [DESCRIBE_THE_ISSUE]
Specific examples: [EVIDENCE]
Desired outcome: [WHAT_YOU_WANT_TO_CHANGE]
Relationship context: [YOUR_RELATIONSHIP_WITH_THIS_PERSON]
```

## Example Input

```
Person: Ryan, Senior Engineer (L5)
Issue: Ryan has been dismissive and curt in code reviews, to the point where two mid-level engineers (separately) have told me they dread getting reviews from him. His technical feedback is correct, but his tone is discouraging and is affecting team dynamics.

Examples:
- Commented "This is wrong. Just use the pattern from X service." on a PR from Jun (L3), with no explanation of why or how. Jun spent 2 hours trying to figure out what Ryan meant.
- Left "Why?" on 4 separate lines of a PR from Ana (L4) with no further context.
- In a design review meeting, interrupted Ana mid-explanation to say "That won't scale" and then went back to his laptop.

Desired outcome: Ryan maintains his technical standards (which are valuable) but communicates with respect and patience. Reviews should teach, not discourage.

Relationship: Good working relationship, 8 months as his manager. Ryan respects directness and doesn't respond well to vague or indirect feedback.
```

## Example Output

> **Conversation Prep: Ryan — Code Review Communication**
>
> **Opening Frame**
> "Ryan, I want to talk about something that's important to me and to the team. It's about how your feedback lands in code reviews and discussions. I'm raising this because I value your technical judgment and I want to make sure it's having the positive impact it should."
>
> *(Direct, no small talk lead-in. Ryan respects directness. Frame it as "your impact isn't matching your intent" — not "you're doing something wrong.")*
>
> **Core Message**
> "Your technical instincts in reviews are consistently right — that's not the issue. The issue is how the feedback is communicated. I have specific examples:
>
> In Jun's PR last week, you wrote 'This is wrong. Just use the pattern from X service' — with no explanation. Jun is an L3; he spent 2 hours trying to figure out what you meant. The correct answer was probably a 3-sentence explanation.
>
> On Ana's PR, you left 'Why?' on 4 separate lines with no context. That's not a review — it's a quiz.
>
> In the design review on Wednesday, you interrupted Ana mid-explanation to say 'That won't scale' and then went back to your laptop. She didn't get to finish her thought."
>
> *(Specific, dated, observable. No interpretations like "you're rude" — just what happened and the impact.)*
>
> **Impact Statement**
> "Here's why this matters: two engineers on the team have separately told me they dread getting reviews from you. That means your feedback — which is technically valuable — is having the opposite of its intended effect. Instead of raising the bar, it's making people afraid to submit code. That's bad for them, bad for the team, and honestly, it's bad for you — because you end up carrying more of the technical load when people avoid sending you PRs."
>
> **Listen**
> "I'd like to hear your perspective. Are you aware of how this is landing? Is there something going on that's contributing to it?"
>
> *(Pause here. Really listen. Ryan might have context you don't — frustration with code quality, being overloaded, personal stress. Hear him out before moving to solutions.)*
>
> **Path Forward**
> "What I need from you going forward:
> - Code review comments should include the *why*, not just the correction. 'This won't scale because X — consider Y instead' takes 30 seconds longer but is actually useful.
> - When reviewing junior engineers' code, assume they don't have your context. Explain the pattern, link to an example, or offer to pair.
> - In meetings, let people finish their point before critiquing. If something won't work, say 'I have a concern about scale — can I share it when you're done?'
>
> This isn't about lowering your standards. It's about delivering your standards in a way that makes people better, not smaller."
>
> **Support Offer**
> "I'm happy to help with this. If you want, I can review a few of your code reviews with you next week and we can calibrate together on tone. I also think watching how [respected peer] gives review feedback might be useful — their reviews are thorough but people come away energised."
>
> **Close**
> "I'm raising this because I think you're one of the strongest engineers on the team, and I want your influence to match your ability. This is a fixable thing — it's communication, not character. How are you feeling about this?"
>
> *(End by checking in emotionally. Even direct people can feel stung. Reaffirm that this comes from respect.)*

## Tuning Notes

- **The person gets defensive:** Don't argue. Restate the facts: "I understand you see it differently. What I can tell you is that two teammates independently raised this concern, and the examples I shared are things I observed. I'm not asking you to agree with their interpretation — I'm asking you to adjust the approach."
- **Missed promotion conversation:** Lead with empathy, be specific about what was missing, and immediately pivot to "here's the path forward." Don't let the conversation end without a clear plan.
- **Conflict between two reports:** Don't mediate in a joint meeting first. Talk to each person individually, understand their perspective, then bring them together only if needed.
- **Your own nervousness:** Rehearse the opening sentence out loud before the meeting. The first 15 seconds set the tone for the entire conversation. Write it down and say it exactly as planned.
- **Follow up:** Always follow up in writing within 24 hours: "Thanks for the conversation. Here's what we agreed to." This creates accountability and prevents "I thought you meant..." later.
