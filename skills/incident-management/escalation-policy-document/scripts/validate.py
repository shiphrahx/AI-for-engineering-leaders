#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    d = draft.lower()
    for tier in ["tier 1", "tier 2", "tier 3", "tier 4"]:
        if tier not in d:
            failures.append(f"Missing '{tier}' — define the full escalation chain")
    if "authority" not in d:
        failures.append("Missing 'Authority' — each tier must state what it can approve")
    if "cross-team" not in d and "cross team" not in d:
        failures.append("Missing 'Cross-Team Escalation' section")
    if "after-hours" not in d and "after hours" not in d:
        failures.append("Missing 'After-Hours Policy' section")
    if not re.search(r"\|.+\|", draft):
        failures.append("No table found — cross-team/vendor contacts must be tabulated")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
