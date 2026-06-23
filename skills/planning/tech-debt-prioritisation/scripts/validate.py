#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    d = draft.lower()
    if "prioritised backlog" not in d and "prioritized backlog" not in d:
        failures.append("Missing 'Prioritised Backlog' section")
    for col in ["risk if unaddressed", "effort", "business case"]:
        if col not in d:
            failures.append(f"Missing backlog column: '{col}'")
    if "recommended investment" not in d:
        failures.append("Missing 'Recommended Investment' — say what share of capacity to spend")
    if not re.search(r"\bp0\b", d):
        failures.append("No P0 in the backlog — rank items P0–P3")
    if not re.search(r"\|.+\|", draft):
        failures.append("No table found — the prioritised backlog must be a table")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
