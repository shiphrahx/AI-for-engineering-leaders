#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["concern","expected behaviour","measurable milestones","support provided","review dates","consequence"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    # Milestones must have dates
    if not re.search(r"\b(\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}|week \d|day \d{1,2})\b", draft, re.I):
        failures.append("No dates found in milestones — every milestone needs a target date")
    # Must not use legally risky language
    for phrase in ["fired","dismissed","let go","terminate","get rid of"]:
        if phrase.lower() in draft.lower():
            failures.append(f"Avoid informal language: '{phrase}' — use 'employment may be ended'")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
