#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["context","talking points","asks","what i want from this meeting"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    # Talking points must be concrete
    tp_section = re.search(r"talking points(.+?)(asks|what i want|$)", draft, re.I | re.S)
    if tp_section:
        bullets = re.findall(r"(?m)^[\-\*]\s+.+", tp_section.group(1))
        if len(bullets) < 2:
            failures.append("Fewer than 2 talking points — add specific items you want to raise")
    # Must have a clear ask
    asks_section = re.search(r"\basks?\b(.+?)(what i want|$)", draft, re.I | re.S)
    if asks_section and len(asks_section.group(1).strip()) < 10:
        failures.append("Asks section is empty — every skip-level should have at least one clear ask")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
