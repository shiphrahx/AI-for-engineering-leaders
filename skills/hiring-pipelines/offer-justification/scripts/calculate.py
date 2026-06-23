#!/usr/bin/env python3
"""
Usage: python calculate.py --base 90000 --band-min 80000 --band-max 110000
                           --bonus 0.10 --equity 5000 --start-date 2026-08-01
"""
import argparse, sys
from datetime import datetime

p = argparse.ArgumentParser()
p.add_argument("--base",        type=float, required=True)
p.add_argument("--band-min",    type=float, required=True)
p.add_argument("--band-max",    type=float, required=True)
p.add_argument("--bonus",       type=float, default=0)
p.add_argument("--equity",      type=float, default=0)
p.add_argument("--start-date",  type=str,   required=True)
args = p.parse_args()

midpoint    = (args.band_min + args.band_max) / 2
compa       = args.base / midpoint
total_comp  = args.base + (args.base * args.bonus) + args.equity

print(f"\n=== Offer Check ===")
print(f"  Base:               £{args.base:,.0f}")
print(f"  Band:               £{args.band_min:,.0f} – £{args.band_max:,.0f}")
print(f"  Compa ratio:        {compa:.2f}")
print(f"  Bonus target:       {args.bonus*100:.0f}%  (£{args.base*args.bonus:,.0f})")
print(f"  Equity:             £{args.equity:,.0f}")
print(f"  Total comp:         £{total_comp:,.0f}")
print(f"  Start date:         {args.start_date}")

flags = []
if args.base > args.band_max:
    flags.append(f"Base exceeds band ceiling (£{args.band_max:,.0f}) — needs approval")
if args.base < args.band_min:
    flags.append(f"Base is below band floor (£{args.band_min:,.0f})")
if compa > 1.2:
    flags.append(f"Compa ratio {compa:.2f} is high — check internal equity")
try:
    start = datetime.strptime(args.start_date, "%Y-%m-%d")
    if (start - datetime.today()).days < 14:
        flags.append("Start date is less than 2 weeks away — confirm notice period")
except ValueError:
    flags.append("Start date format invalid — use YYYY-MM-DD")

if flags:
    print("\nFLAGS:"); [print(f"  - {f}") for f in flags]; sys.exit(1)
else:
    print("\nPASS"); sys.exit(0)
