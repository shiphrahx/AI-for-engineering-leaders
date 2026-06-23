#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    # Must be a table
    if not re.search(r"\|.+\|.+\|", draft):
        failures.append("Tracker must be a markdown table")
    rows = [r for r in draft.split("\n") if r.startswith("|") and "---" not in r and "Action" not in r]
    for i, row in enumerate(rows, 1):
        cols = [c.strip() for c in row.split("|") if c.strip()]
        if len(cols) < 4:
            failures.append(f"Row {i} missing columns — need: Action | Owner | Due date | Priority")
        else:
            action, owner, due, *_ = cols
            if owner.lower() in ["tbd","unknown",""]:
                failures.append(f"Row {i}: owner is '{owner}' — every action needs a named owner")
            if not re.search(r"\d", due):
                failures.append(f"Row {i}: due date '{due}' has no date — add a specific date or week")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
