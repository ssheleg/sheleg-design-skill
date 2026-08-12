# Brief — `datasheet`, the fourteenth style pack

- **Run:** `2026-08-12-datasheet-pack`
- **Branch:** `feat/datasheet-pack-v1.19.0`, built in an isolated worktree at
  `.claude/worktrees/datasheet`
- **Base:** `main` at `0c23558`
- **Target version:** `1.19.0` (a new pack is a feature; minor)

> **[CORRECTION — the version and the base moved mid-run.]** This brief opened
> targeting `1.18.0` from `main` at `13dcd5d`. While the reference was being
> measured, **another agent working in the same checkout committed `0c23558` on
> `main`**, bumped every manifest to `1.18.0`, tagged `v1.18.0` and published it to
> npm. Evidence: `git reflog` puts that commit at `HEAD@{1}`, between this run's
> stage-0 snapshot and its `git checkout -b`; the tag `e3bde7a` is on `origin` and
> `npm view` returns `1.18.0` where stage 0 read `1.17.0`. That commit also swept
> this brief and a scratch screenshot into itself, which is the `git add -A`
> failure the retrospective recorded on 2026-08-04. Two consequences: this run
> moves to `1.19.0`, and it builds in an isolated worktree so a concurrent
> `git add -A` cannot claim its files again. A third is inherited rather than
> caused: **`main` is two commits ahead of `origin/main` while `v1.18.0` is tagged
> and published**, so a fresh clone gets `main` at the `v1.17.0` era while the
> registry serves 1.18.0. Filed as a board row; this run pushes what it merges.
- **Operator request, verbatim in intent:** look at Fingerprint's design through the
  Refero MCP and put it into the library as the recommendation for B2B SaaS.

## The register, in one sentence

**The page is a spec sheet, and the data lives in a dark instrument window cut into
it.** Not a cockpit whose every surface is dark, and not a paper document that refuses
instruments: an off-white datasheet whose focal element is a console panel showing the
product's actual output.

## Why the library has room for it

Ten packs could be mistaken for this one and each fails a different way:

| Pack | Why it is not this | Source |
|---|---|---|
| `instrument-console` | the whole page is the cockpit; here the page is paper and the cockpit is a window in it | `styles/instrument-console.md` Register |
| `field-notes` | explicitly refuses the dark console — "where a dark console would make the reader trust the instrument instead of reading the evidence" | `styles/field-notes.md:32-35` |
| `showroom` | the exhibit is a whole application surface at real size; here it is a payload, a few dozen lines of JSON-shaped data | `styles/showroom.md` Register |
| `blueprint` | white stock, a 32px grid, **no radius**; this reference is off-white with radii of 12/6/4 | `SKILL.md:76` |
| `scoreboard` | the subject is an accumulating number; here it is a live per-visitor record | `styles/scoreboard.md` Register |
| `editorial-luxury` | holds "premium B2B" and is a serif dossier | `README.md:49` |

No pack in the library claims **B2B SaaS sold on an API's output**. That is the slot.

## Source ledger — what the project already knew

| Source | What it gave this run |
|---|---|
| `docs/superpowers/retro.md` | ten standing instructions, all binding. **Twelve run stamps, the last `ada7462`/v1.14.0 — while 1.15.0, 1.16.0, 1.16.1 and 1.17.0 are shipped.** Four releases with no stamp and no prune-log entry |
| `docs/superpowers/backlog.md` | 13 rows, **10 open** (B-001…B-009, B-013); B-010/011/012 resolved |
| `docs/superpowers/verification.md` | **3 rows at `never`** |
| `docs/DOCMAP.md` | the single homes: token values → `tokens/<pack>.css`; a count → derived at check time; a stated ratio → recomputed from the token layer; the version → five-way sync |
| `docs/adr/0001-style-pack-naming.md` | a pack is named for its register, never the source brand → `datasheet`, and `fingerprint.com` goes in `Origin:` |
| `CONTRIBUTING.md:51-58` | the contract is **thirteen**; "do not ship a pack on the nine" |
| `test/floors.json` | ratchet floors 1507 / 603 / 352, measured on `fix/scenario-findings-v1.16.0` |
| `test/scenarios.md` | the harness reaches T23 and every scenario carries a verdict → this run owes **T24** |
| `graphify-out/graph.json` | `built_at_commit` `9312a85` against HEAD `13dcd5d` — stale, and that is open row **B-009** with two candidate fixes; the shrink guard was right and is not to be forced |
| git, per instruction 1 | one worktree, no foreign HEAD move, tree clean; **`main` is one commit ahead of `origin/main`** (`13dcd5d`, unpushed) |
| tags + registry, per instruction 2 | `v1.17.0` local, on `origin` and on npm — all three agree; next is `1.18.0` |
| Refero MCP | style `74adbdf2-822b-4df3-80d1-3c5a1b263a90`, **candidate source only** per `DESIGN_SYNC_BRIDGE.md:133`. Already refuted in one detail: it states the display weight is 600; the live site computes **500** |
| `~/.obsidian-wiki/config` | the projects wiki is present → stage 9 owes it a page update |

## Decisions taken in the grill

1. **Subagent runs for T24 are authorised.** Both branches run in fresh contexts at
   stage 6; every finding they return is reproduced against the artifact before any
   edit (instruction 8). This is the branch that shipped as debt on `scoreboard` and
   the reason instruction 3 exists.
2. **The four missing run stamps are backfilled from evidence** — date and commit from
   git, task and version from the CHANGELOG, `diverged?` from whether the release has a
   `Log` entry. Anything the evidence does not carry is marked *stamped
   retroactively* rather than invented. Without this the prune's five-stamp retirement
   trigger is not computable.
3. **Contract: widened**, all thirteen headings plus `## Motion flavor` if the measured
   reference earns it. Derived from `CONTRIBUTING.md:51-58`, not asked.
4. **Tracks declined, and recorded rather than left silent.** No Figma track: the
   deliverable is a token layer and markdown, not a screen, so there is no frame to
   draw. No `super-ux` track: the pack changes no user-facing product behaviour — its
   reader is an agent choosing a look. `copywriting` is not engaged for the same reason
   (`CHANGELOG` and pack prose are developer-facing).

## REQ table — frozen; adding is free, removing needs the operator

| id | Requirement | How it is verified |
|---|---|---|
| REQ-01 | `styles/datasheet.md` carries all thirteen headings, declares `Contract: widened`, and an `Origin:` naming an addressable reference with the measurement date and the stylesheet read | `validate.py` heading + contract checks; `sloplint.py` origin check |
| REQ-02 | Every value is measured off the live reference, or marked at its declaration as a pack decision (`SELECTED`) against the measured set (`MEASURED`) | the token layer's header defines both words; grep both at every declaration |
| REQ-03 | `styles/tokens/datasheet.css` passes the palette gate: AA 4.5:1 for ink on field, the CVD floors, semantic separation | `npm run palette` |
| REQ-04 | Every contrast ratio the pack states is recomputed from the token layer, because its table declares its base | `validate_stated_ratios()`; the palette gate's check count rises |
| REQ-05 | The reference's own accessibility failures are recorded in `## Gotchas` with their numbers, never silently applied — white on the orange CTA at 3.32:1, tertiary text at 3.23:1, and three chromatic statuses unusable on the canvas | the section, each number recomputed at write time |
| REQ-06 | `kits/datasheet` exists with the identical spine, a `.md` per component carrying `category:`, and `src/styles.css` derived from the token layer | `validate_kits()` |
| REQ-07 | `datasheet` names every pack a reader could confuse it with, and each of those names it back | `validate_fork_reciprocity()` |
| REQ-08 | The library's count word moves thirteen → fourteen in every place that states it | `validate_counted_claims()`, `validate_contract_terminology()` |
| REQ-09 | Every pack enumeration gains the pack: README table, `bin/cli.js`, the slash command, the `.mdc` rule, both manifests, the `.cursor` mirror | `validate_pack_enumerations()` |
| REQ-10 | `test/floors.json` is raised to the new counts with the reason in the same commit | the three gates against the file |
| REQ-11 | **T24 is written with both branches and run** in fresh contexts; its result line carries a verdict and a date | the two runs; findings reproduced per instruction 8 |
| REQ-12 | `docs/adr/0001-style-pack-naming.md` records this application — `fingerprint.com` → `datasheet` | the file |
| REQ-13 | Version 1.18.0 is synced five ways: `package.json`, `marketplace.json`, `plugin.json`, CHANGELOG top entry, `SKILL.md` `metadata.version` | `validate.py` version sync |
| REQ-14 | `v1.18.0` is tagged, released and published; the CI verdict is read **before** the tag; every local channel is refreshed and verified by reading installed files | `git ls-remote --tags`, `npm view`, the shadow invariant, instruction 9 |
| REQ-15 | Four run stamps backfilled, this run stamped, the ten instructions walked and pruned | `retro.md` |
| REQ-16 | The code graph is refreshed, or its staleness is restated honestly with B-009's two candidate fixes intact | `built_at_commit` against HEAD |
| REQ-17 | `13dcd5d` reaches `origin/main`; at close-out every repository is clean and pushed | `git status`, `git branch -vv` |

## Carry-over ledger

| Row | State |
|---|---|
| B-009 (stale code graph, two candidate fixes, do not force the shrink guard) | inherited **open** — this run does not own the choice between a full rebuild and a stated dedup model. REQ-16 covers restating it honestly, not closing it |
| B-013 (59% of stated ratios reach no check) | inherited **open**. This pack must not widen the gap: its table declares a base so its own ratios are covered (REQ-04) |
| B-001, B-002, B-004 (three packs with no addressable origin; widening the core three) | inherited **open**, untouched by this run |
