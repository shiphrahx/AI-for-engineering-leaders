# Pipeline Analytics Review

## Situation

You've been hiring for a while and want to understand how your pipeline is performing. Where are candidates dropping off? How long does the process take? Are you sourcing from the right places? Data-driven hiring improves both quality and speed.

## The Prompt

```
You are an engineering leader reviewing hiring pipeline metrics to identify bottlenecks, improve conversion, and reduce time-to-hire. Analyse the funnel, identify where candidates are lost, and recommend specific improvements.

Structure:
1. **Funnel overview** — conversion rates at each stage
2. **Time analysis** — how long each stage takes and total time-to-hire
3. **Source effectiveness** — which sourcing channels produce the best candidates
4. **Drop-off analysis** — where and why candidates leave the pipeline
5. **Quality indicators** — offer acceptance rate, 90-day retention, performance of recent hires
6. **Recommendations** — top 3 changes to improve the pipeline

Pipeline data: [PASTE_PIPELINE_METRICS]
Roles: [ROLES_COVERED]
Time period: [TIME_PERIOD]
```

## Example Input

```
Period: Q1 2025, Senior Backend Engineers (3 open roles)
Applied: 142
Phone screen: 38 (27% pass rate from application)
Take-home sent: 28 (74% pass from screen)
Take-home returned: 16 (57% completion rate)
On-site: 14 (88% pass from take-home)
Offer: 5 (36% from on-site)
Accepted: 3 (60% acceptance rate)

Time: Average 34 days application to offer. Phone screens take 8 days to schedule on average. Take-home results take 6 days to review.

Sources: 60 from job boards, 45 from LinkedIn outreach, 22 from referrals, 15 from careers page.
Referrals produced 2 of the 3 hires. LinkedIn outreach produced 1.

Drop-off reasons (where known): 8 candidates withdrew citing "process too slow," 4 withdrew after receiving competing offers during take-home stage, 12 take-homes not returned (no reason given).
```

## Example Output

> **Pipeline Analytics: Senior Backend Engineers, Q1 2025**
>
> **Funnel**
> ```
> Applied        142  ████████████████████████████████ 100%
> Phone screen    38  █████████          27%
> Take-home sent  28  ███████            20%
> Returned        16  ████               11%
> On-site         14  ████               10%
> Offer            5  █                   4%
> Accepted         3  █                   2%
> ```
>
> **Key Finding: We're losing candidates to speed, not quality.**
>
> The funnel shape is healthy — conversion rates are reasonable at each stage. But we're bleeding 12 candidates (43% of take-home recipients) who never return the exercise, and 8 candidates explicitly cited slowness. With a 34-day average time-to-hire and competitors moving in 14-21 days, we're losing strong candidates before we can make an offer.
>
> **Bottlenecks**
> 1. **Phone screen scheduling: 8 days average.** This is where we lose momentum. A candidate applies, waits a week to hear back, then waits another week for a screen. By then, they're deep in another process.
> 2. **Take-home completion: 57%.** Almost half of candidates who receive the exercise don't return it. Likely causes: exercise is too long, they got an offer elsewhere first, or they lost interest during the delay.
> 3. **Take-home review: 6 days.** Candidates who complete the exercise wait nearly a week for feedback. Fast competitors close in this window.
>
> **Source Effectiveness**
> | Source | Applied | Hired | Hire Rate |
> |--------|---------|-------|-----------|
> | Referrals | 22 (15%) | 2 (67% of hires) | 9.1% |
> | LinkedIn outreach | 45 (32%) | 1 (33% of hires) | 2.2% |
> | Job boards | 60 (42%) | 0 | 0% |
> | Careers page | 15 (11%) | 0 | 0% |
>
> Referrals convert at 9.1% (2 of 22) — roughly 4x the rate of LinkedIn outreach (2.2%). Job boards produced zero hires from 60 applicants despite being 42% of the pipeline, and the careers page produced none from 15.
>
> **Recommendations**
> 1. **Cut phone screen scheduling to < 3 days.** Block dedicated screening slots on Monday/Wednesday. Offer self-scheduling via Calendly. This alone could recover 4-6 candidates who drop off waiting.
> 2. **Reduce take-home scope or offer alternatives.** Either shorten the exercise to 2 hours (with a clear timer) or offer a 90-minute pair programming session as an alternative. Completion rate should target >80%.
> 3. **Double down on referrals.** Increase the referral bonus, run a referral drive, and ask recent hires to recommend former colleagues. Reduce investment in job boards that aren't converting.
> 4. **Commit to 48-hour review turnaround for take-homes.** Assign reviewers before the exercise is sent. When the submission arrives, the reviewer has 48 hours to evaluate and move the candidate forward.

## Tuning Notes

- **Small sample size:** With fewer than 20 candidates, the percentages are noisy. Focus on qualitative patterns (why did specific candidates drop off?) rather than funnel maths.
- **Multiple roles:** Break the analysis by role. A single funnel for "all engineering roles" masks important differences between junior and senior pipelines.
- **Diversity metrics:** If your ATS tracks demographic data, review whether conversion rates differ by demographic group at each stage. Uneven drop-off rates can indicate bias in a specific interview stage.
- **Share with the team:** Publish pipeline metrics to interviewers. When they see that a 6-day review delay correlates with candidate drop-off, they're more motivated to review quickly.
