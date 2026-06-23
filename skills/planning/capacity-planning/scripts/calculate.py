#!/usr/bin/env python3
"""
Usage: python calculate.py --engineers 6 --sprint-days 10 --leave-days 4 --ceremony-hours 6 --velocity 8
"""
import argparse

p = argparse.ArgumentParser()
p.add_argument("--engineers",       type=int,   required=True)
p.add_argument("--sprint-days",     type=int,   required=True)
p.add_argument("--leave-days",      type=int,   default=0, help="Total leave days across team")
p.add_argument("--ceremony-hours",  type=float, default=6, help="Total ceremony hours per engineer")
p.add_argument("--velocity",        type=float, required=True, help="Points per engineer per day")
args = p.parse_args()

available_days   = (args.engineers * args.sprint_days) - args.leave_days
ceremony_days    = (args.ceremony_hours * args.engineers) / 8
productive_days  = available_days - ceremony_days
capacity_points  = productive_days * args.velocity

print(f"\n=== Sprint Capacity ===")
print(f"  Engineers:           {args.engineers}")
print(f"  Sprint days:         {args.sprint_days}")
print(f"  Leave days (total):  {args.leave_days}")
print(f"  Ceremony days:       {ceremony_days:.1f}")
print(f"  Productive days:     {productive_days:.1f}")
print(f"  Capacity (points):   {capacity_points:.0f}")

if capacity_points < 0:
    print("\nFLAG: capacity is negative — too much leave or ceremony for this sprint length")
    import sys; sys.exit(1)
else:
    print("\nPASS"); import sys; sys.exit(0)
