#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["summary","impact","timeline","root cause","what went well","remediation"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    # Timeline must be a table
    if not re.search(r"\|.+\|.+\|", draft):
        failures.append("Timeline must be a markdown table (| Time | Event | Source |)")
    # Remediation actions must be specific
    vague_actions = re.findall(r"(?im)^[\-\*]\s+(improve|increase|better|fix|review)\s+\w+$", draft)
    if vague_actions:
        failures.append(f"Vague remediation actions: {vague_actions} — each needs a specific, ownable action")
    # Must not name individuals as causes
    cause_section = re.search(r"root cause(.+?)(\n#|$)", draft, re.I | re.S)
    if cause_section:
        # Simple heuristic: look for "[Name] caused" or "[Name] failed to"
        if re.search(r"[A-Z][a-z]+ (caused|failed|forgot|didn't|missed)", cause_section.group(1)):
            failures.append("Root cause names an individual — reframe to the decision or system condition")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
