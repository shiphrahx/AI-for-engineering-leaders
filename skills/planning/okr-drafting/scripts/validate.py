#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    # Count objectives
    objectives = re.findall(r"(?im)^#+\s*objective|^O\d[\.\:]", draft)
    if len(objectives) < 1:
        failures.append("No objectives found — label each as 'Objective N:' or use a heading")
    # Count key results
    krs = re.findall(r"(?im)^[\-\*]\s*KR\d|key result", draft)
    if len(krs) < len(objectives) * 2:
        failures.append(f"Too few key results ({len(krs)}) — aim for 2–5 per objective")
    # Key results must be measurable
    measurable = re.findall(r"\d+\s*(%|pts|points|days|hours|£|\$|users|tickets|nps)", draft, re.I)
    if len(measurable) < len(krs):
        failures.append("Some key results lack a measurable target — every KR needs a number")
    # Flag aspirational waffle
    for phrase in ["be better","improve culture","increase happiness","do more of"]:
        if phrase.lower() in draft.lower():
            failures.append(f"Unmeasurable KR language: '{phrase}' — rewrite with a specific metric")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
