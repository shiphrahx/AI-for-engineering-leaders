#!/usr/bin/env python3
import sys

def validate(draft):
    failures = []
    for section in ["status","context","decision","consequences","alternatives considered"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    # Status must be a known value
    import re
    if not re.search(r"\b(proposed|accepted|deprecated|superseded)\b", draft, re.I):
        failures.append("Status must be one of: Proposed / Accepted / Deprecated / Superseded")
    # Alternatives must list at least 2
    alt_section = re.search(r"alternatives(.+?)(\n#|$)", draft, re.I | re.S)
    if alt_section:
        bullets = re.findall(r"(?m)^[\-\*]\s+.+", alt_section.group(1))
        if len(bullets) < 2:
            failures.append("Alternatives section has fewer than 2 options — an ADR with one alternative considered is not an ADR")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
