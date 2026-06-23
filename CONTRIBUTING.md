# Contributing

Contributions are welcome. If you have a prompt or skill that's worked well for you, add it.
Everything here is provider-neutral — plain markdown plus stdlib Python, runnable by any LLM
agent. Keep it that way: no provider SDKs, API keys, or model-specific syntax.

## Contributing a prompt

1. Fork the repo.
2. Copy [`PROMPT_TEMPLATE.md`](PROMPT_TEMPLATE.md) into `prompts/<category>/NN-name.md` and fill
   every section (Situation, The Prompt, Example Input, Example Output, Tuning Notes).
3. Open a PR describing what you added and why it's useful.

## Contributing a skill

1. Copy [`SKILL_TEMPLATE.md`](SKILL_TEMPLATE.md) into `skills/<category>/<name>/SKILL.md`.
2. Keep the portable structure: front-matter (`name` matching the folder, folded `description`),
   then `## Inputs to gather`, `## Steps`, `## Output format`, optional `## Variants`,
   `## Boundaries`, `## Chaining`.
3. Optionally tune for org size with the [variants convention](docs/VARIANTS.md).

## Bundled scripts (optional)

A skill can ship a `scripts/` helper that the agent runs before returning output:

- `scripts/validate.py` — structural checks on the draft (sections present, no banned phrases…).
- `scripts/calculate.py` — arithmetic (compa ratios, capacity, headcount cost…).

Rules:

- Python 3, **standard library only** — no third-party imports, no network, no API keys.
- Exit `0` on pass, `1` on fail. Plain-text output.
- The skill's `## Steps` must reference the script and end with:
  `Run the script. Fix every failure. Do not return output until the script passes.`
- Add golden fixtures under `tests/`: `pass.md`/`fail.md` for validators, or
  `pass.args`/`fail.args` for calculators. `tools/run_script_tests.py` runs them.

## Before you open a PR

Run the local checks (all stdlib, no network):

```
python tools/gen_manifest.py        # refresh the index after adding/renaming
python tools/gen_crossmap.py        # refresh the prompt-skill map
python tools/gen_integrations.py    # refresh the integrations doc
python tools/lint_skills.py         # structure linter
python tools/check_repo.py          # links, counts, generated-doc freshness
python tools/run_script_tests.py    # script fixtures
```

CI runs the same checks on every PR. If they pass locally, they pass in CI.

If the contribution is specific, practical, and follows the format, it's in.
