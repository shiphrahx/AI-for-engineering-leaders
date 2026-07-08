#!/usr/bin/env python3
"""Structural checks for a tech-evaluation-spike draft. Stdlib only, no network.

Enforces: a clear verdict, deal-breaker check, evidence, and an honest scope note.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re


def validate(draft):
    failures = []
    lower = draft.lower()

    # Verdict must be present and one of the three.
    if "verdict" not in lower:
        failures.append("Missing 'Verdict' — lead with Adopt / Avoid / Need more")
    elif not re.search(r"verdict[:\s*]*\s*(adopt|avoid|need)", lower):
        failures.append("Verdict must be Adopt, Avoid, or Need more")

    if "deal-breaker" not in lower and "deal breaker" not in lower:
        failures.append("Missing deal-breaker check — hard requirements decide adoption")
    if "evidence" not in lower and "held up" not in lower and "what was tested" not in lower:
        failures.append("Missing evidence — state what was actually tested and observed")
    if "recommendation" not in lower:
        failures.append("Missing 'Recommendation'")
    if "did not test" not in lower and "did NOT test" not in draft and "left open" not in lower:
        failures.append("Missing 'Did NOT test' — record the risks a short trial leaves open")

    # Guard against reporting docs/marketing as observed evidence.
    if re.search(r"according to (the )?(docs|documentation|website|marketing|vendor)", lower):
        failures.append("Cites docs/marketing as evidence — report only what the spike exercised, or mark Unknown")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
