#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["status","this week","next week","risks","asks"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    if len(draft.split()) > 200:
        failures.append(f"Too long ({len(draft.split())} words) — exec updates should be under 200 words")
    for phrase in ["as previously mentioned","as discussed","to reiterate","as you know"]:
        if phrase.lower() in draft.lower():
            failures.append(f"Filler phrase: '{phrase}' — cut it")
    # Risks section must have at least one item or explicitly say None
    risk_section = re.search(r"risks(.+?)(asks|$)", draft, re.I | re.S)
    if risk_section and len(risk_section.group(1).strip()) < 5:
        failures.append("Risks section is empty — write 'None this week' if no risks, don't leave blank")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
