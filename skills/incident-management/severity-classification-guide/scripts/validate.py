#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    d = draft.lower()
    for level in ["p0", "p1", "p2", "p3"]:
        if not re.search(r"\b" + level + r"\b", d):
            failures.append(f"Missing severity level: '{level.upper()}'")
    for field in ["acknowledge", "target resolution", "communication"]:
        if field not in d:
            failures.append(f"Missing field: '{field}' — each level needs response timings")
    if "customer impact" not in d:
        failures.append("Missing the rule of thumb: classify on 'customer impact', not technical complexity")
    if not re.search(r"\|.+\|", draft):
        failures.append("No table found — each severity level needs a definition table")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
