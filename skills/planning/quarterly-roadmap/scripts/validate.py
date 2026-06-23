#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["now","next","later"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing horizon: '{section}' — roadmaps need Now / Next / Later")
    # Every item should have an owner or team tag
    items = re.findall(r"(?m)^[\-\*]\s+.+", draft)
    items_without_owner = [i for i in items if not re.search(r"\(([A-Z][a-z]+|team|squad)\)", i)]
    if len(items_without_owner) > 2:
        failures.append(f"{len(items_without_owner)} items have no owner — add (Name) or (Team) to each")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
