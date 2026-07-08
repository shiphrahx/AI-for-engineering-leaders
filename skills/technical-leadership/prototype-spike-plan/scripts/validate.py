#!/usr/bin/env python3
"""Structural checks for a prototype-spike-plan draft. Stdlib only, no network.

Enforces spike discipline: one question, a hard timebox, and kill criteria.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re

TIME_UNITS = ("hour", "day", "hr", "hrs")


def validate(draft):
    failures = []
    lower = draft.lower()

    # Required sections.
    if "question" not in lower:
        failures.append("Missing 'Question' — a spike must name the one thing it answers")
    if "timebox" not in lower:
        failures.append("Missing 'Timebox' — a spike without a hard time limit becomes a project")
    if "disposal" not in lower:
        failures.append("Missing 'Disposal' — state that the code is thrown away / what must be rebuilt")

    # Kill/success criteria must be present.
    if not re.search(r"stop if|kill|❌", lower):
        failures.append("No kill criterion — write what result means 'stop / do not proceed'")
    if not re.search(r"proceed if|success|✅", lower):
        failures.append("No success criterion — write what result means 'proceed'")

    # Timebox must carry an actual number + unit (hours/days), and not be weeks/months.
    tb = re.search(r"timebox[^\n]*", lower)
    tb_line = tb.group(0) if tb else ""
    if tb_line:
        if not re.search(r"\d", tb_line):
            failures.append("Timebox has no number — state how many hours/days")
        elif not any(u in tb_line for u in TIME_UNITS):
            failures.append("Timebox unit unclear — express it in hours or days")
    if re.search(r"\btimebox\b[^\n]*\b(week|weeks|month|months)\b", lower):
        failures.append("Timebox is weeks/months — that's a project, not a spike. Cut it to hours/days.")

    # Single question: flag if the Question line packs multiple '?' (a spike answers one thing).
    q = re.search(r"question:\*{0,2}\s*(.+)", draft, re.I)
    if q and q.group(1).count("?") > 1:
        failures.append("Question section asks more than one thing — a spike answers one question; split it")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
