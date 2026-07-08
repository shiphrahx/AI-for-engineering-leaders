#!/usr/bin/env python3
"""Structural checks for an estimation-sanity-check draft. Stdlib only, no network.

Enforces: original baseline, hidden-work surfaced, a revised RANGE (not a single
number), a confidence level, and a recommendation.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re


def validate(draft):
    failures = []
    lower = draft.lower()

    if "original" not in lower:
        failures.append("Missing 'Original' — restate the estimate being checked")
    if "hidden" not in lower and "omitted" not in lower:
        failures.append("Missing hidden/omitted work — surface what the estimate glosses over")
    if "assumption" not in lower:
        failures.append("Missing assumptions check — challenge what the estimate assumed")

    # Must return a RANGE, not a single number.
    has_range = ("revised range" in lower or
                 (("best" in lower) and ("worst" in lower)))
    if not has_range:
        failures.append("Missing revised range — return best/likely/worst, not a single number")

    # Confidence level required.
    if not re.search(r"confidence[:\s*]*\s*(high|medium|low)", lower):
        failures.append("Missing confidence level — state High / Medium / Low")

    if "recommendation" not in lower:
        failures.append("Missing 'Recommendation' — commit / commit with buffer / de-risk first")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
