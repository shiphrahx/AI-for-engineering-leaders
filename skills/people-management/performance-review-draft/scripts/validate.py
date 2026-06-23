#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    required = ["what went well","areas for growth","rating","next steps"]
    for s in required:
        if s.lower() not in draft.lower():
            failures.append(f"Missing section: '{s}'")
    # Must have a rating token
    if not re.search(r"\b(exceeds|meets|below|outstanding|developing)\b", draft, re.I):
        failures.append("No rating found — must include: Exceeds / Meets / Below / Outstanding / Developing")
    # Flag empty next steps
    ns_match = re.search(r"next steps(.+?)($|\n#)", draft, re.I | re.S)
    if ns_match and len(ns_match.group(1).strip()) < 20:
        failures.append("Next steps section is empty or too brief")
    for phrase in ["could improve","needs to work on","sometimes struggles"]:
        if phrase.lower() in draft.lower():
            failures.append(f"Non-specific feedback: '{phrase}' — name the situation and the behaviour")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
