#!/usr/bin/env python3
"""Structural checks for a legacy-code-assessment draft. Stdlib only, no network.

Enforces: an invest/rewrite/leave verdict, all three paths costed, a reassess
trigger, and that rewrite isn't chosen on aesthetics alone.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re


def validate(draft):
    failures = []
    lower = draft.lower()

    # Verdict present and one of three.
    m = re.search(r"verdict[:\s*]*\s*(invest|rewrite|leave)", lower)
    if "verdict" not in lower:
        failures.append("Missing 'Verdict' — lead with Invest / Rewrite / Leave")
    elif not m:
        failures.append("Verdict must be Invest, Rewrite, or Leave")

    # All three paths must be considered.
    for path in ("invest", "rewrite", "leave"):
        if path not in lower:
            failures.append(f"Path not considered: '{path}' — cost all three (invest/rewrite/leave)")

    # Reassess trigger required — legacy calls expire.
    if "trigger" not in lower and "reassess" not in lower:
        failures.append("Missing reassess trigger — state what would change this call")

    # Cost of ownership evidence.
    if "cost of ownership" not in lower and "change frequency" not in lower:
        failures.append("Missing cost-of-ownership evidence — justify spend with real pain, not aesthetics")

    # Guard: rewrite verdict justified only by aesthetics.
    if m and m.group(1) == "rewrite":
        reason_zone = lower[m.start(): m.start() + 400]
        aesthetic = ["ugly", "messy", "hate", "gross", "spaghetti", "don't like", "dont like"]
        has_aesthetic = any(a in reason_zone for a in aesthetic)
        has_substance = any(s in lower for s in ["incident", "time lost", "change frequency", "cost", "risk", "coupling"])
        if has_aesthetic and not has_substance:
            failures.append("Rewrite justified on aesthetics — require evidence of real cost of ownership")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
