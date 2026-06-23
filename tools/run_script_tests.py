#!/usr/bin/env python3
"""
Run golden-fixture tests for every skill that ships a script. No deps, no LLM.

Convention per skill that has scripts/:
  validate.py  ->  tests/pass.md   (expected exit 0)
                   tests/fail.md   (expected exit 1)
  calculate.py ->  tests/pass.args (one line of CLI args, expected exit 0)
                   tests/fail.args (expected exit 1)

Skills with a script but no tests/ directory are reported as SKIP (not a failure),
so fixtures can be added incrementally.

Exit 0 if all present fixtures behave as expected, 1 otherwise.
Usage: python tools/run_script_tests.py
"""
import os, shlex, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO, "skills")


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True).returncode


def check_validator(skill_dir, label, results):
    tests = os.path.join(skill_dir, "tests")
    cases = [("pass.md", 0), ("fail.md", 1)]
    ran = False
    for fname, expected in cases:
        fpath = os.path.join(tests, fname)
        if not os.path.isfile(fpath):
            continue
        ran = True
        with open(fpath, encoding="utf-8") as f:
            draft = f.read()
        code = run([sys.executable, "scripts/validate.py", draft], skill_dir)
        ok = code == expected
        results.append((ok, f"{label} {fname}: exit {code} (expected {expected})"))
    return ran


def check_calculator(skill_dir, label, results):
    tests = os.path.join(skill_dir, "tests")
    cases = [("pass.args", 0), ("fail.args", 1)]
    ran = False
    for fname, expected in cases:
        fpath = os.path.join(tests, fname)
        if not os.path.isfile(fpath):
            continue
        ran = True
        with open(fpath, encoding="utf-8") as f:
            argline = f.read().strip()
        code = run([sys.executable, "scripts/calculate.py"] + shlex.split(argline), skill_dir)
        ok = code == expected
        results.append((ok, f"{label} {fname}: exit {code} (expected {expected})"))
    return ran


def main():
    results = []
    skipped = []
    for category in sorted(os.listdir(SKILLS_DIR)):
        cat_dir = os.path.join(SKILLS_DIR, category)
        if not os.path.isdir(cat_dir):
            continue
        for name in sorted(os.listdir(cat_dir)):
            skill_dir = os.path.join(cat_dir, name)
            scripts = os.path.join(skill_dir, "scripts")
            if not os.path.isdir(scripts):
                continue
            label = f"{category}/{name}"
            ran = False
            if os.path.isfile(os.path.join(scripts, "validate.py")):
                ran = check_validator(skill_dir, label, results) or ran
            if os.path.isfile(os.path.join(scripts, "calculate.py")):
                ran = check_calculator(skill_dir, label, results) or ran
            if not ran:
                skipped.append(label)

    failed = [msg for ok, msg in results if not ok]
    for ok, msg in results:
        print(("PASS " if ok else "FAIL ") + msg)
    for s in skipped:
        print(f"SKIP {s} (no tests/ fixtures)")

    print(f"\n{len(results) - len(failed)}/{len(results)} fixture checks passed, "
          f"{len(skipped)} skill(s) without fixtures")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
