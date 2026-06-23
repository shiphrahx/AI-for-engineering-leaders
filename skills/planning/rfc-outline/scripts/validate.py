#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    for section in ["problem","proposal","trade-offs","open questions","out of scope"]:
        if section.lower() not in draft.lower():
            failures.append(f"Missing section: '{section}'")
    # Trade-offs must mention both pros and cons
    tradeoffs = re.search(r"trade.off(.+?)(\n#|$)", draft, re.I | re.S)
    if tradeoffs:
        body = tradeoffs.group(1).lower()
        has_pro = any(w in body for w in ["benefit","advantage","pro","upside","strength"])
        has_con = any(w in body for w in ["risk","downside","con","cost","complexity","limitation"])
        if not (has_pro and has_con):
            failures.append("Trade-offs must cover both upsides and downsides")
    # Open questions must not be empty
    oq = re.search(r"open questions(.+?)(\n#|$)", draft, re.I | re.S)
    if oq and len(oq.group(1).strip()) < 10:
        failures.append("Open questions section is empty — every RFC has open questions")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
