#!/usr/bin/env python3
"""Structural checks for an ai-coding-guidelines draft. Stdlib only, no network.

Enforces that the policy covers the non-negotiable areas and stays tool-neutral.
Exit 0 = PASS, 1 = FAIL with a plain-text list of what to fix.
Usage: python scripts/validate.py "$(cat draft.md)"   (or pipe on stdin)
"""
import sys, re

# Every AI-coding policy must speak to these areas.
REQUIRED = {
    "stance": ["stance"],
    "when to use / scrutiny": ["when to use", "extra scrutiny", "good fit"],
    "review & verification bar": ["review", "verif"],
    "secrets & data": ["secret", "pii", "data"],
    "security": ["security"],
    "licensing & attribution": ["licens", "attribution", "provenance"],
    "accountability": ["accountab", "owns", "responsible"],
}


def validate(draft):
    failures = []
    lower = draft.lower()

    for area, keys in REQUIRED.items():
        if not any(k in lower for k in keys):
            failures.append(f"Missing area: {area}")

    # Tool-neutral: naming a single assistant as if it's the only one is a smell.
    # Flag only if exactly one vendor is named and it's framed as "our tool".
    vendors = [v for v in ["claude", "copilot", "codex", "cursor", "gemini", "windsurf"]
               if re.search(r"\b" + v + r"\b", lower)]
    if len(vendors) == 1 and re.search(r"(use|only|must use|standard)[^.\n]{0,30}\b" + vendors[0] + r"\b", lower):
        failures.append(
            f"Reads as locked to one tool ('{vendors[0]}') — keep the policy neutral across assistants")

    # Accountability must not let the tool take the blame.
    if re.search(r"the ai wrote it|blame the (ai|tool|model)", lower) and "excuse" not in lower and "never" not in lower:
        failures.append("Accountability unclear — the submitting engineer owns the code, not the tool")

    return failures


draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
