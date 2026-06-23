#!/usr/bin/env python3
"""
Usage: python calculate.py --current 80000 --increase 0.08 --band-min 75000 --band-max 95000
"""
import argparse, sys

p = argparse.ArgumentParser()
p.add_argument("--current",    type=float, required=True)
p.add_argument("--increase",   type=float, required=True, help="e.g. 0.08 for 8%%")
p.add_argument("--band-min",   type=float, required=True)
p.add_argument("--band-max",   type=float, required=True)
args = p.parse_args()

new_salary = args.current * (1 + args.increase)
midpoint   = (args.band_min + args.band_max) / 2
compa      = new_salary / midpoint

print(f"\n=== Compensation Review ===")
print(f"  Current salary:     £{args.current:,.0f}")
print(f"  Increase:           {args.increase*100:.1f}%")
print(f"  New salary:         £{new_salary:,.0f}")
print(f"  Band:               £{args.band_min:,.0f} – £{args.band_max:,.0f}")
print(f"  Compa ratio:        {compa:.2f}")

failures = []
if new_salary > args.band_max:
    failures.append(f"New salary £{new_salary:,.0f} exceeds band ceiling £{args.band_max:,.0f}")
if new_salary < args.band_min:
    failures.append(f"New salary £{new_salary:,.0f} is below band floor £{args.band_min:,.0f}")
if compa > 1.15:
    failures.append(f"Compa ratio {compa:.2f} is above 1.15 — escalate for approval")

if failures:
    print("\nFLAGS:"); [print(f"  - {f}") for f in failures]; sys.exit(1)
else:
    print("\nPASS"); sys.exit(0)
