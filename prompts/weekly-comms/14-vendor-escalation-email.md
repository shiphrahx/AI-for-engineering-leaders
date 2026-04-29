# Vendor Escalation Email

## Situation

A vendor — cloud provider, SaaS tool, contractor — is blocking your team and normal support channels aren't cutting it. You need to escalate in writing: professional, specific about impact, and clear about what you need and by when.

## The Prompt

```
You are an engineering leader writing a formal escalation email to a vendor.

Draft an escalation email that:
1. States the issue clearly and factually in the first paragraph (no preamble)
2. Quantifies the business impact (time blocked, revenue at risk, engineers idled)
3. Summarises what has already been tried through normal channels (ticket numbers, dates, names if known)
4. States a specific ask with a deadline
5. Signals appropriate urgency without being hostile — professional but firm

Tone: direct, factual, no emotional language. Short paragraphs.

Context:
- Vendor: [VENDOR_NAME]
- Issue: [DESCRIBE_THE_PROBLEM]
- Impact: [HOW_IT'S_AFFECTING_YOUR_TEAM_OR_BUSINESS]
- What's been tried: [PREVIOUS_ATTEMPTS — tickets, calls, account manager contacts]
- What you need: [SPECIFIC_ASK]
- Your deadline: [DATE_OR_TIMEFRAME]
- Who is this going to: [RECIPIENT — e.g. account executive, VP of Customer Success, support director]
```

## Example Input

```
- Vendor: Datastream (data pipeline SaaS)
- Issue: Their API has been returning 503 errors intermittently since March 12, affecting our nightly ETL jobs. The issue is not on our side — confirmed by their own status page (incident #4821, now marked "resolved" but errors continue).
- Impact: Our data warehouse is 5 days stale. Two BI analysts and one data engineer are fully blocked. We have a board report due March 22 that depends on accurate data.
- What's been tried: Support ticket #DS-88234 opened March 12, followed up March 14 and 16. Account manager (James Holt) contacted by phone on March 15, said he'd escalate, no update since.
- What you need: A root cause explanation, a fix timeline, and a dedicated engineer on the call by EOD March 18.
- Deadline: March 18, EOD
- Recipient: VP of Customer Success
```

## Example Output

> **Subject: Urgent escalation — API instability blocking production data pipeline (Ticket #DS-88234)**
>
> Hi [Name],
>
> I'm escalating an unresolved issue that is directly blocking our production operations.
>
> Since March 12, Datastream's API has been returning intermittent 503 errors on our data pipeline. Your status page marked incident #4821 as resolved, but the errors have continued. Our nightly ETL jobs have been failing for five consecutive days, leaving our data warehouse five days stale.
>
> The business impact is significant: two BI analysts and one data engineer are fully blocked. We have a board-level report due March 22 that depends on accurate, current data. Every day this continues increases the risk of us missing that deadline.
>
> We've pursued normal channels without resolution. Support ticket #DS-88234 was opened March 12 and followed up on March 14 and 16. Our account manager James Holt confirmed on March 15 that he would escalate — we have not received an update since.
>
> I need three things by EOD March 18:
> 1. A root cause explanation for the ongoing 503 errors
> 2. A concrete fix timeline
> 3. A dedicated engineer on a call with my team
>
> Please confirm receipt and let me know who will own this from your side. If this isn't resolved by March 18, I'll need to explore alternative options for our board report timeline.
>
> [Your name]

## Tuning Notes

- **Softer tone needed:** Remove the final sentence about alternatives. Add a line acknowledging the vendor relationship.
- **SLA breach:** Reference the specific SLA clause and the remediation or credit you're entitled to.
- **Cloud provider (AWS/GCP/Azure):** Use their enterprise support portal for escalations rather than email; adapt this as a support case description.
- **Contractor or agency:** Adjust to reference the SOW or contract terms and the delivery milestone at risk.
