#!/usr/bin/env python3
import sys, re

def validate(draft):
    failures = []
    d = draft.lower()
    for section in ["funnel", "bottleneck", "source effectiveness", "recommendation", "key finding"]:
        if section not in d:
            failures.append(f"Missing section: '{section}'")
    if not re.search(r"\|.+\|", draft):
        failures.append("No table found — source effectiveness needs a table")
    if not re.search(r"\d+\s*%", draft):
        failures.append("No conversion percentage found — funnel/source analysis needs rates")
    return failures

draft = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
issues = validate(draft)
if not issues:
    print("PASS"); sys.exit(0)
else:
    print("FAIL:\n" + "\n".join(f"  - {i}" for i in issues)); sys.exit(1)
