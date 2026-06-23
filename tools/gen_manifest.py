#!/usr/bin/env python3
"""
Generate manifest.json — a machine-readable index of every prompt and skill.

Scans skills/<category>/<name>/SKILL.md and prompts/<category>/NN-name.md, extracts
metadata, and writes manifest.json at the repo root. No third-party dependencies; any
agent can read the manifest to enumerate and route to resources deterministically.

Usage:
  python tools/gen_manifest.py            # write manifest.json
  python tools/gen_manifest.py --check    # exit 1 if manifest.json is stale
"""
import json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(REPO, "skills")
PROMPTS_DIR = os.path.join(REPO, "prompts")
MANIFEST = os.path.join(REPO, "manifest.json")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_front_matter(text):
    """Return (name, description) from a leading --- ... --- YAML block."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, None
    block = m.group(1)
    name = None
    nm = re.search(r"(?m)^name:\s*(.+?)\s*$", block)
    if nm:
        name = nm.group(1).strip()
    # description may be a folded scalar (> then indented lines) or inline
    desc = None
    dm = re.search(r"(?m)^description:\s*(.*)$", block)
    if dm:
        first = dm.group(1).strip()
        if first in (">", "|", ">-", "|-", ""):
            lines = []
            for line in block[dm.end():].split("\n"):
                if re.match(r"^\S", line):  # next top-level key
                    break
                lines.append(line.strip())
            desc = " ".join(l for l in lines if l).strip()
        else:
            desc = first
    return name, desc


def chains_to(text):
    """Best-effort: skill names bolded under a ## Chaining section."""
    m = re.search(r"(?ms)^##\s*Chaining\s*(.+?)(?=^##\s|\Z)", text)
    if not m:
        return []
    names = re.findall(r"\*\*([a-z0-9][a-z0-9-]+)\*\*", m.group(1))
    seen, out = set(), []
    for n in names:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out


def detect_script(skill_dir):
    sdir = os.path.join(skill_dir, "scripts")
    if os.path.isdir(os.path.join(skill_dir, "scripts")):
        if os.path.isfile(os.path.join(sdir, "calculate.py")):
            return "calculate"
        if os.path.isfile(os.path.join(sdir, "validate.py")):
            return "validate"
    return None


def collect_skills():
    items = []
    for category in sorted(os.listdir(SKILLS_DIR)):
        cat_dir = os.path.join(SKILLS_DIR, category)
        if not os.path.isdir(cat_dir):
            continue
        for name in sorted(os.listdir(cat_dir)):
            skill_dir = os.path.join(cat_dir, name)
            skill_md = os.path.join(skill_dir, "SKILL.md")
            if not os.path.isfile(skill_md):
                continue
            text = read(skill_md)
            fm_name, desc = parse_front_matter(text)
            items.append({
                "type": "skill",
                "category": category,
                "name": fm_name or name,
                "path": os.path.relpath(skill_md, REPO),
                "description": desc,
                "script": detect_script(skill_dir),
                "chains_to": chains_to(text),
            })
    return items


def collect_prompts():
    items = []
    for category in sorted(os.listdir(PROMPTS_DIR)):
        cat_dir = os.path.join(PROMPTS_DIR, category)
        if not os.path.isdir(cat_dir):
            continue
        for fname in sorted(os.listdir(cat_dir)):
            if not fname.endswith(".md"):
                continue
            path = os.path.join(cat_dir, fname)
            text = read(path)
            title = None
            tm = re.search(r"(?m)^#\s+(.+?)\s*$", text)
            if tm:
                title = tm.group(1).strip()
            items.append({
                "type": "prompt",
                "category": category,
                "name": re.sub(r"^\d+-", "", fname[:-3]),
                "title": title,
                "path": os.path.relpath(path, REPO),
            })
    return items


def build():
    skills = collect_skills()
    prompts = collect_prompts()
    categories = sorted({i["category"] for i in skills} | {i["category"] for i in prompts})
    return {
        "schema": "ai-for-engineering-leaders/manifest@1",
        "counts": {
            "skills": len(skills),
            "prompts": len(prompts),
            "categories": len(categories),
            "skills_with_scripts": sum(1 for s in skills if s["script"]),
        },
        "categories": categories,
        "skills": skills,
        "prompts": prompts,
    }


def main():
    data = build()
    rendered = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        current = read(MANIFEST) if os.path.isfile(MANIFEST) else ""
        if current != rendered:
            print("FAIL: manifest.json is stale — run: python tools/gen_manifest.py")
            sys.exit(1)
        print("PASS: manifest.json is up to date")
        sys.exit(0)
    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write(rendered)
    print(f"Wrote {os.path.relpath(MANIFEST, REPO)}: "
          f"{data['counts']['skills']} skills, {data['counts']['prompts']} prompts, "
          f"{data['counts']['categories']} categories")


if __name__ == "__main__":
    main()
