#!/usr/bin/env python3
"""
Repo consistency checker. No deps, no LLM.

  - every relative markdown link in README.md resolves to a real file
  - README badge + headline counts match the actual filesystem counts
  - manifest.json is up to date (delegates to gen_manifest --check)

Exit 0 if consistent, 1 otherwise.
Usage: python tools/check_repo.py
"""
import os, re, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO, "README.md")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def actual_counts():
    skills = prompts = 0
    skills_dir = os.path.join(REPO, "skills")
    prompts_dir = os.path.join(REPO, "prompts")
    cats = set()
    for cat in os.listdir(skills_dir):
        cdir = os.path.join(skills_dir, cat)
        if not os.path.isdir(cdir):
            continue
        cats.add(cat)
        for name in os.listdir(cdir):
            if os.path.isfile(os.path.join(cdir, name, "SKILL.md")):
                skills += 1
    for cat in os.listdir(prompts_dir):
        cdir = os.path.join(prompts_dir, cat)
        if not os.path.isdir(cdir):
            continue
        cats.add(cat)
        prompts += sum(1 for f in os.listdir(cdir) if f.endswith(".md"))
    return {"skills": skills, "prompts": prompts, "categories": len(cats)}


def check_links():
    failures = []
    text = read(README)
    for target in re.findall(r"\]\(([^)]+)\)", text):
        t = target.split("#")[0].strip()
        if not t or t.startswith(("http://", "https://", "mailto:")):
            continue
        if not os.path.exists(os.path.join(REPO, t)):
            failures.append(f"broken link in README.md: {target}")
    return failures


def check_counts():
    failures = []
    text = read(README)
    actual = actual_counts()
    patterns = {
        "prompts": [r"prompts-(\d+)", r"(\d+)\s+(?:situation-specific\s+)?\*\*prompts\*\*"],
        "skills": [r"skills-(\d+)", r"(\d+)\s+agent-ready\s+\*\*skills\*\*"],
        "categories": [r"categories-(\d+)"],
    }
    for key, pats in patterns.items():
        for pat in pats:
            for found in re.findall(pat, text):
                if int(found) != actual[key]:
                    failures.append(
                        f"README {key} count {found} != actual {actual[key]} (pattern: {pat})")
    return failures


def check_generated():
    """Every generated artifact must be in sync with its source."""
    failures = []
    generators = ["gen_manifest.py", "gen_crossmap.py", "gen_integrations.py"]
    for gen in generators:
        r = subprocess.run([sys.executable, os.path.join(REPO, "tools", gen), "--check"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            failures.append(r.stdout.strip() or f"{gen} output is stale")
    return failures


def main():
    failures = check_links() + check_counts() + check_generated()
    if failures:
        print("FAIL:")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print("PASS: links resolve, counts match, manifest fresh")
    sys.exit(0)


if __name__ == "__main__":
    main()
