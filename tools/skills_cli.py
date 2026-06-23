#!/usr/bin/env python3
"""
skills — list, search, and emit prompts/skills from the terminal.

LLM-agnostic by design: this tool only *reads* the library and writes resource
content to stdout. It never calls a model. Pipe `cat` output into whatever agent
you use:

  python tools/skills_cli.py cat promotion-case | your-agent

Commands:
  list   [--category C] [--type skill|prompt] [--with-scripts]
  search <query>
  show   <name>
  cat    <name>

Reads manifest.json if present (run tools/gen_manifest.py to refresh); otherwise
falls back to scanning the filesystem.
"""
import argparse, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(REPO, "manifest.json")


def load_manifest():
    if os.path.isfile(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as f:
            return json.load(f)
    # fallback: regenerate in-memory
    sys.path.insert(0, os.path.join(REPO, "tools"))
    import gen_manifest
    return gen_manifest.build()


def all_items(data):
    return data.get("skills", []) + data.get("prompts", [])


def find(data, name):
    matches = [i for i in all_items(data) if i["name"] == name]
    if not matches:
        matches = [i for i in all_items(data) if name in i["name"]]
    return matches


def cmd_list(data, args):
    rows = all_items(data)
    if args.category:
        rows = [r for r in rows if r["category"] == args.category]
    if args.type:
        rows = [r for r in rows if r["type"] == args.type]
    if args.with_scripts:
        rows = [r for r in rows if r.get("script")]
    for r in sorted(rows, key=lambda r: (r["type"], r["category"], r["name"])):
        tag = r["type"][0].upper()
        extra = f"  [{r['script']}]" if r.get("script") else ""
        print(f"{tag}  {r['category']:<20} {r['name']}{extra}")
    print(f"\n{len(rows)} item(s)")
    return 0


def cmd_search(data, args):
    q = args.query.lower()
    hits = []
    for r in all_items(data):
        blob = " ".join(str(r.get(k, "")) for k in ("name", "description", "title", "category")).lower()
        if q in blob:
            hits.append(r)
    for r in sorted(hits, key=lambda r: r["name"]):
        desc = (r.get("description") or r.get("title") or "")[:90]
        print(f"{r['type'][0].upper()}  {r['name']:<34} {desc}")
    print(f"\n{len(hits)} match(es)")
    return 0 if hits else 1


def cmd_show(data, args):
    matches = find(data, args.name)
    if not matches:
        print(f"no item matching '{args.name}'", file=sys.stderr)
        return 1
    for r in matches:
        print(f"name:        {r['name']}")
        print(f"type:        {r['type']}")
        print(f"category:    {r['category']}")
        print(f"path:        {r['path']}")
        if r.get("script"):
            print(f"script:      {r['script']}")
        if r.get("chains_to"):
            print(f"chains_to:   {', '.join(r['chains_to'])}")
        if r.get("description"):
            print(f"description: {r['description']}")
        print()
    return 0


def cmd_cat(data, args):
    matches = find(data, args.name)
    exact = [m for m in matches if m["name"] == args.name]
    chosen = exact[0] if exact else (matches[0] if len(matches) == 1 else None)
    if chosen is None:
        if not matches:
            print(f"no item matching '{args.name}'", file=sys.stderr)
        else:
            print("ambiguous; matches: " + ", ".join(m["name"] for m in matches), file=sys.stderr)
        return 1
    with open(os.path.join(REPO, chosen["path"]), encoding="utf-8") as f:
        sys.stdout.write(f.read())
    return 0


def main():
    p = argparse.ArgumentParser(prog="skills", description="List, search, and emit prompts/skills.")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list")
    pl.add_argument("--category")
    pl.add_argument("--type", choices=["skill", "prompt"])
    pl.add_argument("--with-scripts", action="store_true")

    ps = sub.add_parser("search")
    ps.add_argument("query")

    psh = sub.add_parser("show")
    psh.add_argument("name")

    pc = sub.add_parser("cat")
    pc.add_argument("name")

    args = p.parse_args()
    data = load_manifest()
    return {"list": cmd_list, "search": cmd_search, "show": cmd_show, "cat": cmd_cat}[args.cmd](data, args)


if __name__ == "__main__":
    sys.exit(main())
