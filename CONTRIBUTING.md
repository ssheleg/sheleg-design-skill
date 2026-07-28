# Contributing

This repo ships prose an agent reads, not a library — so the review question is
always *"would an agent, with only these files, do the right thing?"* Two rules
follow from that: **no invented values**, and **every promise a file makes must
have a check that fails when it stops being true**.

## Setup

No dependencies. You need Node ≥ 16 (installer) and Python 3 (validator).

```bash
python3 test/validate.py
```

Run it before and after every change. `npm test` runs the same thing plus a
syntax check on the CLI.

## Repo layout

| Path | What it is |
|---|---|
| `plugins/sheleg-design/skills/sheleg-design/` | **The canonical bundle** — SKILL.md, the reference, the packs, the token CSS, the pack template |
| `.cursor/skills/sheleg-design/` | Byte-identical mirror for the Cursor channel; never edit it by hand |
| `plugins/sheleg-design/commands/` | The `/sheleg-design` slash command |
| `cursor/rules/sheleg-design.mdc` | Self-contained condensed rule — **no relative links** (it gets copied into foreign projects alone) |
| `bin/cli.js`, `install.sh` | The two installers; both must ship the whole bundle |
| `test/validate.py` | Structural gate |
| `test/scenarios.md` | Behavioral harness (T1–T7) |
| `templates/style-pack-template.md` | Source of the shipped pack skeleton |

Edit the canonical bundle, then copy the changed file into the `.cursor/`
mirror. The validator compares the whole tree in both directions and fails on
drift.

## Adding a style pack

1. Copy `templates/style-pack-template.md` to
   `plugins/sheleg-design/skills/sheleg-design/styles/<name>.md`.
2. Fill **every** heading — Register / Palette / Type / Texture & surface /
   Motion tokens / Signature motifs / Motion flavor (cinematic packs only) /
   Micro-interactions / Bans / Gotchas. The validator enforces the set.
3. Author `styles/tokens/<name>.css` in the **same change**. Values come from a
   real production system or a reference you can name in the pack's `Origin:`
   line — a pack whose tokens were invented defeats the point of the repo.
4. Route it: add a row to the `SKILL.md` pack table and name the pack in
   `bin/cli.js`. The validator requires both — a pack nobody routes to does not
   exist.
5. Mirror the new files into `.cursor/skills/sheleg-design/`, add them to the
   `install.sh` file list, and re-run the validator.
6. Add or update a scenario in `test/scenarios.md` if the pack changes routing
   behavior.

Token naming is an interface across packs: `--accent-weak` is a tint,
`--accent-dim`/`-deep` is a darker accent. Reusing a name for the opposite
meaning silently inverts anyone who switches packs.

## Changing the skill or the reference

- `SKILL.md`'s front-matter `description` is discovery. It states **trigger
  conditions**, opens with "Use when", carries Russian aliases beside the
  English triggers, and stays under 1024 characters. All three are validated.
- Any behavioral claim in `SKILL.md` or `SHELEG_DESIGN.md` must match the
  packs and the CSS. Contradictions between files are the defect class this
  repo cares about most — see the 0.9.0 entry in the CHANGELOG for a full pass
  of them.
- After editing the skill, a pack or the reference, re-run the affected
  scenarios from `test/scenarios.md` with fresh subagents.

## Releasing

Semver. Bump `.claude-plugin/marketplace.json`, `plugins/sheleg-design/.claude-plugin/plugin.json`,
`package.json` and the `CHANGELOG.md` top entry **together** — the validator
fails on a mismatch. Tag `vX.Y.Z`; the release workflow (armed by the
`RELEASE_ENABLED` repo variable) validates, cuts a GitHub release from the
matching CHANGELOG section and smoke-tests the tag through `npx`. `npm publish`
is deliberately a human step.

## Reporting

Issues and PRs: <https://github.com/ssheleg/sheleg-design-skill/issues>. For a
bug in what an agent *did*, include the prompt and which files it read — that's
the reproduction.
