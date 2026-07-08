#!/usr/bin/env python3
"""Structural checks for a code-to-exec-translation draft. Stdlib only, no network.

Enforces: so-what leads, jargon translated, honest status, and an explicit ask.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re

# Untranslated engineering jargon an exec can't act on — glossed only, not raw.
JARGON = [
    "refactor", "serialization", "serialisation", "async", "mutex", "kubernetes",
    "kafka", "grpc", "orm", "middleware", "regex", "webhook", "idempotent",
    "race condition", "cron", "polyfill", "transpile", "sharding",
]
FILLER = ["as you know", "it's worth noting", "in order to", "basically", "needless to say"]


def validate(draft):
    failures = []
    lower = draft.lower()

    # Required sections.
    if "so what" not in lower and "so-what" not in lower:
        failures.append("Missing 'So what' — lead with the outcome in the reader's terms")
    if "what changed" not in lower:
        failures.append("Missing 'What changed'")
    if "why it matters" not in lower:
        failures.append("Missing 'Why it matters' — tie it to customer / cost / risk")
    if "needed from you" not in lower and "fyi" not in lower:
        failures.append("Missing 'Needed from you' — state the ask or 'Nothing — FYI'")

    # Untranslated jargon.
    hits = [j for j in JARGON if re.search(r"\b" + re.escape(j) + r"\b", lower)]
    if hits:
        failures.append("Untranslated jargon: " + ", ".join(sorted(set(hits))) + " — translate or cut for an exec reader")

    # Filler.
    for phrase in FILLER:
        if phrase in lower:
            failures.append(f"Filler phrase: '{phrase}' — cut it")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
