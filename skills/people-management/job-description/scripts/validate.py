#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["about the role","responsibilities","requirements","nice to have","what we offer"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    # Requirements must not be a wall of bullets
    req_section = re.search(r"requirements(.+?)(nice to have|what we offer|$)", draft, re.I | re.S)
    if req_section:
        bullets = re.findall(r"(?m)^[\-\*]\s+.+", req_section.group(1))
        if len(bullets) > 10:
            failures.append(f"Requirements has {len(bullets)} bullets — trim to ≤10, move others to 'Nice to have'")
    # Flag gendered or exclusionary language
    for phrase in ["ninja","rockstar","superstar","he or she","manpower","strong cultural fit"]:
        if phrase.lower() in draft.lower():
            failures.append(f"Exclusionary language: '{phrase}' — replace with neutral wording")
    # Must mention salary or band
    if not re.search(r"(salary|£|compensation|band|pay range)", draft, re.I):
        failures.append("No salary or band mentioned — include a range or 'competitive salary' at minimum")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
