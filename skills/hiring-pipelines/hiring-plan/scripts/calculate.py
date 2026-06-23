#!/usr/bin/env python3
"""
Usage: python calculate.py --current 8 --attrition 0.15 --growth 0.20 --budget 450000 --avg-salary 90000
"""
import argparse, math

p = argparse.ArgumentParser()
p.add_argument("--current",     type=int,   required=True)
p.add_argument("--attrition",   type=float, required=True)
p.add_argument("--growth",      type=float, required=True)
p.add_argument("--budget",      type=int,   required=True)
p.add_argument("--avg-salary",  type=int,   required=True)
args = p.parse_args()

attrition_loss = math.ceil(args.current * args.attrition)
growth_hires   = math.ceil(args.current * args.growth)
total_hires    = attrition_loss + growth_hires
end_headcount  = args.current - attrition_loss + total_hires
total_cost     = total_hires * args.avg_salary
gap            = total_cost - args.budget
affordable     = math.floor(args.budget / args.avg_salary)

print(f"\n=== Headcount Plan ===")
print(f"  Current headcount:   {args.current}")
print(f"  Projected attrition: {attrition_loss}")
print(f"  Growth hires:        {growth_hires}")
print(f"  Total hires needed:  {total_hires}")
print(f"  End headcount:       {end_headcount}")
print(f"  Total cost:          £{total_cost:,}")
print(f"  Budget:              £{args.budget:,}")
print(f"  Budget gap:          £{abs(gap):,} {'OVER — flag for approval' if gap > 0 else 'under'}")
print(f"  Affordable hires:    {affordable}")

if gap > 0:
    print("\nFLAG: over budget — present affordable_hires scenario to stakeholder")
    import sys; sys.exit(1)
else:
    print("\nPASS"); import sys; sys.exit(0)
