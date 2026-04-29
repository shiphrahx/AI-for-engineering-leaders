# Engineering Newsletter

## Situation

You send a monthly or bi-weekly engineering newsletter to the broader company — product, design, sales, ops. You want to share what engineering is building and why it matters, without requiring technical knowledge to follow along.

## The Prompt

```
You are an engineering leader writing an internal newsletter for a non-technical company-wide audience.

Turn the following engineering updates into a readable, engaging newsletter. Structure it as:

1. **What we shipped** (3-5 bullets, plain language, focused on what users or the business can now do)
2. **What we're building next** (2-3 items, framed as outcomes not tasks)
3. **Behind the scenes** (1 short paragraph on something technical made accessible — a pattern, a lesson, a tradeoff we navigated)
4. **Team spotlight** (1-2 sentences recognising a person or team, with a specific accomplishment)

Tone: conversational, no jargon, curious not dry. Avoid "we leveraged," "we utilised," and similar corporate filler.

Context:
- Audience: [AUDIENCE — e.g. the whole company, ~200 people, mostly non-technical]
- Cadence: [FREQUENCY — monthly / bi-weekly]
- Period covered: [DATE_RANGE]

Raw engineering updates to transform:
[PASTE_UPDATES]
```

## Example Input

```
- Audience: Whole company (~180 people), mostly non-technical
- Cadence: Monthly
- Period covered: March 2025

Raw updates:
- Shipped dark mode across web and mobile apps
- Completed migration of search service to Elasticsearch 8.x — p95 latency down 40%
- Deployed new fraud detection model to production, catching 2.3x more fraudulent transactions with 60% fewer false positives
- Started refactoring payment service to improve testability; 30% of the work done
- Backend on-call incident rate down 35% YoY
```

## Example Output

> **Engineering Update — March 2025**
>
> **What we shipped**
> - **Dark mode is here** — flip the switch in Settings on web or mobile. Your eyes will thank you during late-night sessions.
> - **Search got a lot faster** — results now load ~40% quicker across the product. We quietly swapped out the search engine under the hood for a more modern one.
> - **Smarter fraud detection** — our new fraud model is catching more than twice as many bad transactions while flagging genuine customers far less often. Fewer false alarms for your customers.
>
> **What we're building next**
> - Making payments more reliable and easier to test — less risk when we ship changes in that area
> - Continuing to push down on on-call incidents (already down 35% vs last year)
>
> **Behind the scenes**
> Fraud detection is one of those problems where being wrong in either direction is costly — miss a fraudulent transaction and the business loses money; flag a real customer and they have a bad experience. This month we shipped a new model that gets much better at telling them apart. The trick was training on a richer set of signals rather than just transaction amount and location.
>
> **Team spotlight**
> Huge credit to Priya and the Infra team for the search migration — it ran without a single customer-facing outage despite touching one of our highest-traffic services.

## Tuning Notes

- **Technical audience:** Add a "How we did it" section with more implementation detail.
- **Short version:** Cut to shipped items + spotlight only. Works well as a Slack post.
- **Quarterly edition:** Replace "What we shipped" with a themes-based summary (reliability, velocity, new capabilities) and add metrics comparing start vs. end of quarter.
