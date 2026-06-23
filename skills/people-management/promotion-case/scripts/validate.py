#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["current impact","scope and complexity","evidence","business impact","next level"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    evidence = re.findall(r"(?m)^[\-\*\d][\.\)]?\s+.+", draft)
    if len(evidence) < 3:
        failures.append(f"Thin evidence: {len(evidence)} example(s), need 3+")
    for phrase in ["consistently delivers","strong communicator","great team player","always reliable","works well with"]:
        if phrase.lower() in draft.lower():
            failures.append(f"Vague phrase: '{phrase}' — replace with a specific named example")
    if len(draft.split()) < 200:
        failures.append(f"Too short ({len(draft.split())} words) — reviewers need detail")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
