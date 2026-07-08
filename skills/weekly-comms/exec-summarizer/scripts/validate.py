#!/usr/bin/env python3
"""Structural checks for an exec-summarizer draft. Stdlib only, no network.

Enforces the skill's discipline: headline-first, tight, no filler.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re

# Preamble openers that bury the conclusion — the bottom line must come first.
PREAMBLE = [
    "this document", "this doc", "this report", "in this", "the purpose of",
    "i wanted to", "i'm writing to", "below is", "here is a summary",
    "here's a summary", "the following", "as requested", "to summarize",
]
# Throat-clearing / hedging / filler the skill explicitly cuts.
FILLER = [
    "as you know", "as previously mentioned", "as discussed", "to reiterate",
    "it's worth noting", "it is worth noting", "needless to say", "in order to",
    "at the end of the day", "basically", "just to be clear",
]
WORD_LIMIT = 250


def validate(draft):
    failures = []
    lower = draft.lower()

    # Required sections.
    if "bottom line" not in lower:
        failures.append("Missing '**Bottom line:**' — the conclusion must lead")
    if "what matters" not in lower:
        failures.append("Missing 'What matters' section")
    if "what's needed" not in lower and "whats needed" not in lower:
        failures.append("Missing \"What's needed\" — state the ask or 'Nothing — FYI only'")

    # Headline-first: first real content line must not be a preamble opener.
    body = re.sub(r"(?m)^\s*\*\*\[?subject.*$", "", draft)  # drop title placeholder line
    lines = [l.strip() for l in body.splitlines() if l.strip()]
    # First line that isn't the title header.
    first = next((l for l in lines if not l.lower().startswith("**[") and "exec summary" not in l.lower()), "")
    fl = first.lower().lstrip("*: -")
    for p in PREAMBLE:
        if fl.startswith(p):
            failures.append(f"Buries the lead — opens with preamble '{p}...'. Lead with the conclusion.")
            break

    # Filler.
    for phrase in FILLER:
        if phrase in lower:
            failures.append(f"Filler phrase: '{phrase}' — cut it")

    # Length.
    n = len(draft.split())
    if n > WORD_LIMIT:
        failures.append(f"Too long ({n} words) — exec summary should be under {WORD_LIMIT} words")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
