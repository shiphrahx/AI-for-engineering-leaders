#!/usr/bin/env python3
import sys

def validate(draft):
    failures = []
    for section in ["what happened","who is affected","current status","next update"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing field: '{section}'")
    # No jargon check
    for term in ["cascading failure","race condition","deadlock","null pointer","stack trace"]:
        if term.lower() in draft.lower():
            failures.append(f"Technical jargon for exec audience: '{term}' — rewrite in plain language")
    # Must have a next-update time
    import re
    if not re.search(r"\b(\d{1,2}:\d{2}|\d{1,2}(am|pm)|within \d+ (hour|minute))\b", draft, re.I):
        failures.append("No next-update time found — always commit to a specific time")
    if len(draft.split()) > 150:
        failures.append(f"Too long ({len(draft.split())} words) — exec comms should be under 150 words")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
