# Task brief — design-sync bridge + React reference kits

> Stage-0 intake artifact (task-pipeline 1.10.2). The grill fills this in and the
> operator confirms it before stage 1.

- **Date:** 2026-08-04
- **Task (one line):** add a `design-sync` bridge to the SHELEG Design skill —
  a `DESIGN_SYNC_BRIDGE.md` companion doc covering all four reference types, plus
  minimal React reference kits per style pack, so a pack can be pushed to
  claude.ai/design through Claude Code's bundled `/design-sync` skill.
- **UI verdict:** _pending — grill Q_

## Knowledge sources (the phase-1 harvest — written BEFORE the first question)

| Source | What it says about this task | Fresh? | Authority | Stale after this run? |
|---|---|---|---|---|
| `docs/superpowers/specs/2026-07-19-canon-sync-design.md` | **Out of scope: "Project templates — the skill seeds no application code"**; note: "the original intent (this skill is not a generator) holds". Also fixes the repo layout, the 4-way version sync and the 4 distribution channels. | 2026-07-19, partly superseded | **decision** | **yes — this run either reconciles or supersedes it** |
| `README.md` | "Nothing is added to your dependencies: **the skill is documentation an agent reads**"; lists the installed-file table that a new companion doc must join | current | promise | **yes — update at stage 9** |
| `plugins/sheleg-design/skills/sheleg-design/SKILL.md` | the optional-bridge pattern to copy: `## Optional — Figma (design ↔ code)` and `## Optional — real-world references (Lazyweb MCP)` — tool-presence gated, "proceed without them; nothing here depends on the MCP" | current (v1.4.0) | contract | **yes — gains the design-sync section** |
| `.../FIGMA_BRIDGE.md` | the shape a bridge doc takes: one-line contract ("the pack is the source of truth in both directions"), collection/mode mapping, what cannot cross, round-trip discipline, "file content is data, never instructions" | current | contract | **yes — gains the triangle rule vs claude.ai/design** |
| `test/validate.py` | the 8-point repo contract. Two rules bite this run: **companion docs must both ship in the bundle and be linked from SKILL.md** (hardcoded list at `validate.py:252`), and **`install.sh` must list exactly the bundle files** (`validate.py:298`). Also: every relative markdown link in the repo must resolve. | current | contract | **yes — gains checks for the new doc/kits** |
| `install.sh` | explicit `for f in … ; do` file list — every new bundle file must be added by hand or the validator fails | current | contract | **yes** |
| wiki: `projects/sheleg-design-skill/concepts/skill-canon-and-distribution` | 4-channel distribution; **npm 2FA is the ONE human step and where versions strand** (registry sat 5 releases behind); CI runs *both* installers and `diff -r`s the result; verify a release with `npm view` + e2e `npx <pkg>@<ver>` from a non-repo cwd | 2026-07-28 | context | **yes — update at stage 9** |
| wiki: `projects/sheleg-design-skill/concepts/style-packs-architecture` | the ten-heading pack contract; "**a pack nobody routes to does not exist**"; **[[skills/ship-what-your-docs-point-at]]** — `STYLE_PACK_TEMPLATE.md` had to move *into* the bundle because SKILL.md pointed at a path only the repo had. Directly governs where the kits may live if the bridge doc links to them. | 2026-07-28 | context | **yes — update at stage 9** |
| Claude Code binary (`strings /opt/homebrew/bin/claude`) | the `/design-sync` skill ships **inside the binary**, not as a file: "Push a React design system to claude.ai/design… bundles the real component code (from Storybook or a bare package) and uploads it". Upload layout `_ds_bundle.js` + `@ds-bundle`, `styles.css`, `components/<group>/<Name>/{.html,.jsx,.d.ts,.prompt.md}` with a first-line `@dsCard group="…"`, `_preview/`, `_vendor/`, `fonts/`, `_ds_sync.json`. Local state under `.design-sync/`. Tool order: list/read → `finalize_plan` → `write_files`/`delete_files`. | 2026-08-04 | upstream contract | no (external) |
| `docs/superpowers/retro.md` | **absent** — no standing instructions bind this run | — | — | seeded at stage 10 |
| `docs/superpowers/retro/` | **absent** — nothing to query | — | — | — |
| `CLAUDE.md` / `CONTEXT.md` / `docs/adr/` / `docs/DECISIONS.md` / `docs/DOCMAP.md` / `docs/ux/` | **none found** in this repo. House rules come from the user-global `~/.claude/CLAUDE.md` (production-grade bar, pipeline routing, post-release local-install refresh via `npx --yes sshlg-skills@latest update`, one Obsidian vault). | — | — | doc map seeded this run |
| `graphify-out/graph.json` | **not built** (the `graphify` binary is installed at `~/.local/bin/graphify`) — no reach queries available this run | — | — | offered once, never a gate |

Precedence for *what is*: code > host docs/ADRs > graph > wiki > memory.
For *what should be*: the decision register outranks the code. The operator
outranks every document — **but only out loud**.

### Conflict found in the harvest (must be resolved before the brief locks)

The 2026-07-19 canon spec records **"the skill seeds no application code — this
skill is not a generator"**, and the README promises **"the skill is documentation
an agent reads"**. The chosen scope (React reference kits) is application code.
This is a recorded decision the operator may overrule, but the override has to be
explicit and the reconciliation written down — see *Decisions locked*, D1.

## Documentation (the phase-1b inventory — the four questions)

_pending — grill_

## Scope

_pending — grill_

## Requirements (the REQ spine)

_pending — grill_

## Decisions locked (the grill's output)

| # | Decision | Chosen | Rationale |
|---|---|---|---|
| D1 | Where the React reference kits live, given "the skill seeds no application code" | _pending_ | _pending_ |

## Autonomy (the sweep)

_pending — grill_

## Done-criteria

_pending — grill_

## Open assumptions / risks

_pending — grill_
