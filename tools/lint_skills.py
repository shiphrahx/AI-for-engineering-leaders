#!/usr/bin/env python3
"""
Lint every SKILL.md against the portable spec. Pure static checks, no LLM, no deps.

Checks per skill:
  - has a --- ... --- front-matter block with a `name:` and `description:`
  - front-matter name matches the folder name
  - contains the required sections: Inputs to gather, Steps, Output format,
    Boundaries, Chaining
  - if a scripts/ dir exists, the Steps section ends with the mandated run line
    and references the script

Exit 0 if all skills pass, 1 otherwise.
Usage: python tools/lint_skills.py
"""
import os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO, "skills")

REQUIRED_SECTIONS = [
    "Inputs to gather",
    "Steps",
    "Output format",
    "Boundaries",
    "Chaining",
]
RUN_LINE = "Run the script. Fix every failure. Do not return output until the script passes."


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def section_body(text, heading):
    m = re.search(r"(?ms)^##\s*" + re.escape(heading) + r"\s*(.+?)(?=^##\s|\Z)", text)
    return m.group(1) if m else None


def lint_skill(skill_dir, folder_name):
    failures = []
    skill_md = os.path.join(skill_dir, "SKILL.md")
    text = read(skill_md)

    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        failures.append("missing front-matter block")
    else:
        block = fm.group(1)
        nm = re.search(r"(?m)^name:\s*(.+?)\s*$", block)
        if not nm:
            failures.append("front-matter missing 'name:'")
        elif nm.group(1).strip() != folder_name:
            failures.append(f"name '{nm.group(1).strip()}' != folder '{folder_name}'")
        if not re.search(r"(?m)^description:", block):
            failures.append("front-matter missing 'description:'")

    for section in REQUIRED_SECTIONS:
        if section_body(text, section) is None:
            failures.append(f"missing section: '## {section}'")

    if os.path.isdir(os.path.join(skill_dir, "scripts")):
        steps = section_body(text, "Steps") or ""
        if "scripts/" not in steps:
            failures.append("has scripts/ but Steps never references it")
        if RUN_LINE not in steps:
            failures.append("has scripts/ but Steps missing the mandated run line")
    return failures


def main():
    total, failed = 0, 0
    for category in sorted(os.listdir(SKILLS_DIR)):
        cat_dir = os.path.join(SKILLS_DIR, category)
        if not os.path.isdir(cat_dir):
            continue
        for name in sorted(os.listdir(cat_dir)):
            skill_dir = os.path.join(cat_dir, name)
            if not os.path.isfile(os.path.join(skill_dir, "SKILL.md")):
                continue
            total += 1
            issues = lint_skill(skill_dir, name)
            if issues:
                failed += 1
                print(f"FAIL {category}/{name}")
                for i in issues:
                    print(f"  - {i}")

    if failed:
        print(f"\n{failed}/{total} skill(s) failed lint")
        sys.exit(1)
    print(f"PASS: all {total} skills conform to the spec")
    sys.exit(0)


if __name__ == "__main__":
    main()
