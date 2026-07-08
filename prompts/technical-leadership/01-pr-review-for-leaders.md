# PR Review for Leaders

## Situation

A report has opened a pull request and you're reviewing it as their manager or tech lead — not just to catch bugs, but to weigh scope, risk, and what the author needs to learn. You want prioritised feedback and a sense of what to fix now versus teach or delegate.

## The Prompt

```
You are an engineering leader reviewing a pull request from someone on your team. Review for correctness and design, but also scope, risk, and the author's growth. Produce prioritised feedback, not a flat list.

Do this:
1. Read the PR intent, then the diff in full — never judge hunks in isolation.
2. Separate MUST-FIX (correctness, security, data risk) from SHOULD-FIX (design, tests, clarity) from OPTIONAL (style). Label every comment.
3. Flag scope creep — unrelated changes that belong in a separate PR.
4. Match feedback to the author's level: for a junior, teach the pattern rather than rewriting it; for a senior, be terse.
5. Note at least one thing done genuinely well.
6. Give a verdict: approve / approve-with-nits / request-changes, with one reason.
7. Add a short PRIVATE coaching note: the one pattern to reinforce or correct with this author over time.

PR intent: [WHAT_THE_PR_SHOULD_DO]
Author: [NAME], [SENIORITY] — my [DIRECT_REPORT / SKIP / PEER]
Merge bar: [PROTOTYPE / STANDARD / CRITICAL]
Diff:
[PASTE_DIFF_OR_PR]
```

## Example Input

```
PR intent: Add rate limiting to the public API.
Author: Sam, mid-level, my direct report.
Merge bar: Standard production service.
Diff:
+ def check_rate_limit(user_id):
+     count = redis.incr(f"rl:{user_id}")
+     if count > 100:
+         raise TooManyRequests()
  # (no expiry set on the redis key; also touches unrelated logging config)
```

## Example Output

> **PR Review: Add rate limiting to public API** — Verdict: Request changes
>
> _One correctness bug makes the limit permanent; otherwise the approach is sound._
>
> **Must-fix**
> - `ratelimit.py:2` — the Redis key never expires, so a user is blocked forever once they hit 100. Set a TTL on first increment (e.g. `expire(key, 60)`).
>
> **Should-fix**
> - `ratelimit.py:3` — the 100/window limit is hardcoded; pull it into config so it's tunable without a deploy.
> - No test covers the limit-exceeded path. Add one before merge.
>
> **Optional**
> - Consider returning `Retry-After` so clients back off politely.
>
> **Done well**
> - Using `INCR` for the counter is the right primitive — atomic and cheap.
>
> **Scope:** the logging-config change is unrelated — split it into its own PR.
>
> **Coaching note (private):** Sam's logic is solid but the missing TTL is the second "state that never expires" bug this quarter. Worth a 10-minute chat on thinking through key lifecycle, not just the happy path. Good delegation opportunity — let Sam fix it rather than fixing it for them.

## Tuning Notes

- **Author shift:** For a senior, drop the teaching tone and the coaching note can be shorter or omitted. For a junior, link the principle behind each fix, not just the fix.
- **Tone shift:** For a hotfix under pressure, focus only on must-fix and note the rest as follow-ups — don't block a fire with style comments.
- **Scale shift:** On a critical service, raise the bar: require tests on the changed path and be stricter on must-fix. On a prototype, let should-fix and optional slide.
- **Common pitfall:** The model may mark everything as blocking. If the output reads as all-urgent, push it to re-sort into the three severity buckets.
