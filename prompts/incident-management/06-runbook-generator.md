# Runbook Generator

## Situation

Critical operational knowledge lives in one person's head. You need to extract it into a runbook that any on-call engineer can follow at 3am without prior context. The runbook should be step-by-step, copy-pasteable, and tested.

## The Prompt

```
You are an engineering leader creating an operational runbook from tribal knowledge. The runbook must be usable by any on-call engineer, including someone who has never touched this service before. Every step should be explicit — no "you'll know what to do" or "use your judgment." Include exact commands, expected outputs, and decision trees.

Structure:
1. **Service overview** — what this service does, in 2 sentences, for someone who's never seen it
2. **When to use this runbook** — what alert or symptom triggers it
3. **Prerequisites** — access, tools, permissions needed
4. **Diagnostic steps** — how to assess the situation, with expected outputs at each step
5. **Resolution steps** — step-by-step fix for each common scenario
6. **Verification** — how to confirm the fix worked
7. **Escalation** — when to stop following the runbook and call someone
8. **Appendix** — useful commands, dashboard links, architecture diagram

Service: [SERVICE_NAME]
What it does: [SERVICE_DESCRIPTION]
Common failure modes: [FAILURE_MODES]
Current tribal knowledge holder: [PERSON]
Environment details: [ENVIRONMENT]
```

## Example Input

```
Service: Email delivery pipeline
What it does: Processes outbound emails (transactional and marketing). Reads from an SQS queue, renders templates, sends via SendGrid, logs delivery status to Postgres.
Common failures: Queue backlog (emails delayed), SendGrid rate limiting (429 errors), template rendering failures (malformed variables), database connection exhaustion (delivery status not logged)
Current knowledge holder: Omar (he's been running this for 2 years)
Environment: AWS ECS, SQS queue "email-outbound", SendGrid API, PostgreSQL on RDS, Datadog for monitoring
```

## Example Output

> **Runbook: Email Delivery Pipeline**
>
> ---
>
> **Service Overview**
> The email delivery pipeline processes all outbound emails (password resets, order confirmations, marketing campaigns). It reads messages from an SQS queue, renders email templates, sends them via SendGrid, and logs delivery status to PostgreSQL. If this service stops working, customers don't receive transactional emails.
>
> **When to Use This Runbook**
> - Alert: "Email queue depth > 10,000" (PagerDuty)
> - Alert: "Email delivery error rate > 5%" (PagerDuty)
> - Alert: "Email pipeline ECS task count = 0" (PagerDuty)
> - Symptom: Customer reports not receiving emails (check CS escalation channel first)
>
> **Prerequisites**
> - AWS Console access (Production account)
> - SSH access to ECS tasks via `aws ecs execute-command`
> - Datadog access (dashboard: "Email Pipeline Overview")
> - SendGrid admin panel access (credentials in 1Password vault "Production Services")
>
> ---
>
> **Step 1: Assess the Situation**
>
> Open the Datadog dashboard: [link]
>
> Check these metrics:
> | Metric | Healthy | Investigate |
> |--------|---------|-------------|
> | SQS queue depth | < 1,000 | > 5,000 |
> | Email send success rate | > 99% | < 95% |
> | ECS running task count | 3-5 | < 3 or 0 |
> | SendGrid API response time | < 500ms | > 2000ms |
> | RDS connection count | < 80 | > 90 (max is 100) |
>
> Based on what you see, go to the relevant section below.
>
> ---
>
> **Scenario A: Queue Backlog (queue depth > 10,000, send rate looks normal)**
>
> *Likely cause:* Traffic spike (marketing campaign) or processing slowdown.
>
> 1. Check if a marketing campaign was scheduled:
>    ```
>    aws sqs get-queue-attributes --queue-url https://sqs.eu-west-1.amazonaws.com/ACCOUNT/email-outbound --attribute-names ApproximateNumberOfMessages
>    ```
>    If queue depth is growing but tasks are healthy → likely a campaign. Check with marketing in #marketing-ops.
>
> 2. Scale up ECS tasks temporarily:
>    ```
>    aws ecs update-service --cluster prod-email --service email-pipeline --desired-count 8
>    ```
>    (Normal is 3-5. Max safe is 10 — beyond 10 you'll hit SendGrid rate limits.)
>
> 3. Monitor queue depth. It should start decreasing within 5 minutes.
>
> 4. Once queue depth is below 1,000, scale back to normal:
>    ```
>    aws ecs update-service --cluster prod-email --service email-pipeline --desired-count 4
>    ```
>
> ---
>
> **Scenario B: SendGrid Rate Limiting (429 errors in logs, send success rate dropping)**
>
> 1. Check SendGrid status: https://status.sendgrid.com
>    - If SendGrid is having an outage → nothing to do on our side. Post in #incidents and monitor.
>
> 2. Check our sending rate:
>    ```
>    aws logs filter-log-events --log-group-name /ecs/email-pipeline --filter-pattern "429" --start-time $(date -d '30 minutes ago' +%s000)
>    ```
>    If 429s are frequent → we're exceeding our SendGrid plan limits.
>
> 3. Temporary fix — slow down processing:
>    ```
>    aws ecs update-service --cluster prod-email --service email-pipeline --desired-count 2
>    ```
>    This reduces throughput but stops the 429s. Emails will queue and drain slowly.
>
> 4. If urgent (e.g., password reset emails are blocked): Enable the backup Mailgun provider by setting the environment variable:
>    ```
>    # Update the task definition to set EMAIL_PROVIDER=mailgun
>    # Then force a new deployment
>    aws ecs update-service --cluster prod-email --service email-pipeline --force-new-deployment
>    ```
>    **Note:** Mailgun has lower deliverability for marketing emails. Switch back to SendGrid once rate limits clear.
>
> ---
>
> **Scenario C: ECS Tasks Crashing (task count = 0 or tasks restarting)**
>
> 1. Check recent task failures:
>    ```
>    aws ecs describe-services --cluster prod-email --services email-pipeline --query 'services[0].events[:5]'
>    ```
>
> 2. Check task logs for crash reason:
>    ```
>    aws logs tail /ecs/email-pipeline --since 30m --filter-pattern "ERROR"
>    ```
>
> 3. Common crash causes:
>    - **Out of memory:** Scale to larger task size. Update task definition memory from 512MB to 1024MB.
>    - **Database connection refused:** Go to Scenario D.
>    - **Template rendering error:** A malformed email in the queue is crashing the worker. See Step 4.
>
> 4. If a bad ("poison") message is crashing the worker before it reaches the retry threshold, remove that one message from the main queue so the worker can recover. Receive it to capture its receipt handle, confirm it's the offending message, then delete only that message:
>    ```
>    # Receive one message to inspect its body and get the ReceiptHandle
>    aws sqs receive-message --queue-url https://sqs.eu-west-1.amazonaws.com/ACCOUNT/email-outbound --max-number-of-messages 1
>    # Delete ONLY that message, by its receipt handle
>    aws sqs delete-message --queue-url https://sqs.eu-west-1.amazonaws.com/ACCOUNT/email-outbound --receipt-handle "<RECEIPT_HANDLE>"
>    ```
>    **Warning:** Delete only the confirmed poison message. Never run `purge-queue` here — it discards *every* message in the queue. Once the worker is healthy, redrive any messages parked in the DLQ with `aws sqs start-message-move-task --source-arn <DLQ_ARN>`.
>
> ---
>
> **Scenario D: Database Connection Exhaustion (RDS connections > 90)**
>
> 1. Identify what's consuming connections:
>    ```
>    psql -h prod-email-db.xxxxx.rds.amazonaws.com -U readonly -d emaildb -c "SELECT count(*), state FROM pg_stat_activity GROUP BY state;"
>    ```
>
> 2. If many connections are "idle in transaction": a query is stuck. Kill idle connections:
>    ```
>    psql -h prod-email-db.xxxxx.rds.amazonaws.com -U admin -d emaildb -c "SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state = 'idle in transaction' AND query_start < now() - interval '5 minutes';"
>    ```
>
> 3. Restart ECS tasks to reset connection pools:
>    ```
>    aws ecs update-service --cluster prod-email --service email-pipeline --force-new-deployment
>    ```
>
> ---
>
> **Verification**
> After applying any fix, confirm:
> - [ ] SQS queue depth is decreasing
> - [ ] Email send success rate is recovering (check Datadog)
> - [ ] ECS task count is stable (no restarts in last 10 minutes)
> - [ ] Send a test email to yourself via the admin panel: [link]
>
> ---
>
> **Escalation**
> Stop following this runbook and page someone if:
> - You've tried the relevant scenario and it didn't work
> - You see something not covered here
> - The incident has lasted more than 30 minutes without improvement
> - There's any sign of data loss (emails sent but not logged, duplicate sends)
>
> **Page:** Omar (primary), then Priya (SRE), then your Engineering Manager
>
> ---
>
> **Appendix**
> - Datadog dashboard: [link]
> - SendGrid admin: [link]
> - SQS console: [link]
> - Architecture diagram: [link to wiki]
> - ECS cluster console: [link]

## Tuning Notes

- **Test the runbook:** Have someone who's never touched the service follow it step-by-step. Every place they get confused is a place the runbook needs improvement.
- **Living document:** Runbooks rot fast. Add a "Last verified" date at the top and re-test quarterly. After every incident, update the runbook with what you learned.
- **Multiple services:** Create one runbook per service, not one mega-runbook. Link between them when services interact.
- **Sensitive commands:** Highlight any destructive commands with ⚠️ warnings. Mark anything that could cause data loss or customer impact.
