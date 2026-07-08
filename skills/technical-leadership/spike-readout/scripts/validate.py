#!/usr/bin/env python3
"""Structural checks for a spike-readout draft. Stdlib only, no network.

Enforces: the question restated, an explicit answer, a recommendation, and
open risks — so a spike converts to an honest decision.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re


def validate(draft):
    failures = []
    lower = draft.lower()

    if "question" not in lower:
        failures.append("Missing 'Question' — restate what the spike asked")

    # Answer present and explicit (yes/no/inconclusive).
    ans = re.search(r"answer[:\s*]*\s*(yes|no|inconclusive|proceed|don't|dont)", lower)
    if "answer" not in lower:
        failures.append("Missing 'Answer' — lead with yes / no / inconclusive")
    elif not ans:
        failures.append("Answer isn't explicit — state yes, no, or inconclusive")

    if "recommendation" not in lower:
        failures.append("Missing 'Recommendation' — tie it to the decision this feeds")
    if "still open" not in lower and "open" not in lower:
        failures.append("Missing 'Still open' — record the risks the spike did not resolve")
    if "evidence" not in lower and "what we did" not in lower:
        failures.append("Missing evidence / what-we-did — support the answer")
    if "disposal" not in lower and "no code kept" not in lower:
        failures.append("Missing 'Disposal' — state what's thrown away / needs a proper build")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
