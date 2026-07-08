# Incident Code Triage

## Situation

Something is failing in production right now and you're reading the code path to figure out why. You want ranked hypotheses, the cheapest way to confirm each, and the safest next move — fast, without thrashing.

## The Prompt

```
You are helping triage a live production incident by reading the failing code path. Optimise for speed and honesty, not completeness. Rank by likelihood, tag confidence, and never propose a risky action as automatic.

Produce:
1. Symptom + blast radius + since-when, in one line. Correlate onset with any recent deploy/change.
2. Ranked hypotheses (most to least likely) with a confidence tag. Include the boring likely cause (bad deploy, config, dependency, resource limit) before the exotic one.
3. For each: the cheapest check that confirms or kills it (log query, metric, one-line test, rollback probe).
4. Safest next action — usually stop-the-bleeding (roll back, disable flag, failover) over root-causing live. Flag anything risky/irreversible and require human confirmation.
5. Data/security exposure — surface prominently if the failure could corrupt or leak.
6. Can't tell yet — the open unknown and the signal that would resolve it.

Work only from what I give you; mark gaps Unknown.

Symptom: [WHAT_S_WRONG_AND_HOW_BIG]
Since / recent change: [WHEN_IT_STARTED_AND_WHAT_DEPLOYED]
Signal: [PASTE_STACK_TRACE_ERROR_LOGS_METRICS]
Suspected code: [PASTE_CODE_PATH_IF_KNOWN]
Constraints: [CAN_WE_ROLL_BACK / DATA_AT_RISK / PEAK_TRAFFIC]
```

## Example Input

```
Symptom: Checkout returning 500s for ~30% of users. Started 14:05.
Since / recent change: Deploy at 14:02 that changed the payments client.
Signal: "KeyError: 'idempotency_key'" in the payments call, ~30% of requests.
Suspected code: payments/client.py builds the request payload.
Constraints: We can roll back. Money is involved. Peak traffic.
```

## Example Output

> **Incident Triage: checkout 500s** — Blast radius: ~30% of checkouts — Since: 14:05
>
> **Recent change:** Deploy at 14:02 changed the payments client — 3-minute gap to onset, prime suspect.
>
> **Ranked hypotheses**
> 1. The 14:02 deploy made `idempotency_key` conditional/optional and some paths now omit it — confidence **High**. Check: diff the deploy; grep for where the payload is built (`payments/client.py`). ~30% matches one of several call sites.
> 2. Upstream payments API changed its required fields — confidence Low. Check: provider status page / recent API changelog.
>
> **Safest next action:** ⚠️ Roll back the 14:02 deploy now — money is involved and it's the clear correlate. Confirm rollback with the on-call lead before executing.
>
> **Data/security exposure:** Missing idempotency key risks **double-charging** on retries — treat as high priority; check for duplicate charges in the affected window after rollback.
>
> **Can't tell yet:** Whether any double-charges already occurred — pull payment logs for 14:05 onward to confirm.

## Tuning Notes

- **Boring first:** Push the model to rule out the recent deploy and config before it reaches for exotic causes. Most incidents follow a change.
- **Stop the bleeding:** Bias the next action toward mitigation (rollback, flag) over live root-causing, especially when data or money is at risk.
- **Common pitfall:** The model may state a guess as the confirmed cause. Require confidence tags and a cheap check for each hypothesis.
- **Keep it short:** Mid-incident is not the time for prose — if the output is long, tell it to cut to hypotheses + next action.
