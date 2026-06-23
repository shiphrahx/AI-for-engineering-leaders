#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    d = draft.lower()
    for section in ["error budget", "error budget policy", "measurement", "review cadence"]:
        if section not in d:
            failures.append(f"Missing section: '{section}'")
    if not re.search(r"\bsl[io]\b", d):
        failures.append("No SLI/SLO mentioned — define the indicator and the objective")
    if not re.search(r"\|.+\|", draft):
        failures.append("No table found — list SLIs, targets, and windows in a table")
    if not re.search(r"\d+(\.\d+)?\s*%", draft):
        failures.append("No percentage target found — every SLO needs a measurable target (e.g. 99.9%)")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
