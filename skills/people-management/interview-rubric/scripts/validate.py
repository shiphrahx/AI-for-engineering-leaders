#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    d = draft.lower()
    if "loop overview" not in d:
        failures.append("Missing 'Loop Overview' — list the stages, who runs them, and what each assesses")
    if "debrief" not in d:
        failures.append("Missing 'Debrief Guide' — state how ratings combine into a decision")
    for rating in ["strong hire", "strong no hire"]:
        if rating not in d:
            failures.append(f"Missing rating anchor: '{rating}' — rubrics need the full scale")
    if not re.search(r"\|.+\|", draft):
        failures.append("No table found — per-stage rubrics must tabulate ratings vs behaviours")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
