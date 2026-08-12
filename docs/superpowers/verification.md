# Verification ledger — sheleg-design-skill

One row per shipped REQ, written at stage 8 and required at stage 10 in both
directions: no REQ without a row, no row without a REQ.

`Last verified` is a date **and** the thing that was watched — not "tests pass".
`never` is a legitimate value and the one worth counting: it says a requirement
was shipped on the strength of an argument rather than an observation.

Seeded 2026-08-10 by the `2026-08-10-skill-audit` run. **Rows at `never`: 1.**

| REQ | What must stay true | How it is checked | Last verified | Status |
|---|---|---|---|---|
| REQ-01 | Every counted claim (packs, kits, scenarios, headings) is true | `validate_counted_claims()` — whitespace-normalised across line breaks | 2026-08-10 · planted `six locked style packs`, caught | **green** |
| REQ-02 | No cross-cutting doc names a status token the packs it addresses lack | the dataviz table rewritten by role; `validate_core_vocabulary()` for the three role tokens | 2026-08-10 · `--bg`/`--ink`/accent role resolved in all 12, measured | **green** |
| REQ-03 | The `dataviz` handoff is true of the packs it addresses | same; the non-uniform mappings are named in `SKILL.md` | 2026-08-10 · measured 1/12 for `--accent-tint`, 3/12 for `--accent-deep`; table no longer names either | **green** |
| REQ-04 | `MOTION_DOCTRINE.md` reaches every channel that ships the skill | `grep` of README table, `cli.js` help + banner, the slash command, the `.mdc` rule | 2026-08-10 · all five carry it; the rule gained the doctrine in condensed form | **green** |
| REQ-05 | The pack contract has one name and one number everywhere | `validate_contract_terminology()` | 2026-08-10 · a stale spelling planted in CONTRIBUTING.md, caught | **green** |
| REQ-06 | `DESIGN_SYNC_BRIDGE.md` no longer tells an author to ship nine headings | the same check, plus the edit | 2026-08-10 · check covers the file | **green** |
| REQ-07 | The `/sheleg-design` command routes to all twelve packs | `validate_pack_enumerations()` | 2026-08-10 · planted removal of one pack, caught | **green** |
| REQ-08 | Both manifests name the current library | same check | 2026-08-10 · same planted defect | **green** |
| REQ-09 | Every pack declares what it does **not** specify | `validate_contract_declaration()` — declaration checked against the headings actually present, line-anchored | 2026-08-10 · planted removal of `workbench`'s line, caught; and the line-anchoring bug it exposed was watched failing first | **green** |
| REQ-10 | `atrium`, `orchard`, `editorial-luxury` carry the widened four | — | **never** | **carried → board B-004.** Their references are addressable, so this is a measurement pass against live computed styles. Not attempted rather than guessed. The misleading half is closed: each declares `Contract: core` and states what it leaves undecided |
| REQ-11 | Reference-implementation paths cannot be mistaken for real files | all seven `**File:**` headers renamed to `**Reference file:**`, with a callout at the top of the document | 2026-08-10 · `grep -c '^\*\*File:\*\*'` = 0 | **green** |
| REQ-12 | README's "Development" section is backed by code | rewritten claim-by-claim; the one unbackable claim ("both installers' file lists") is now stated as the limit it is | 2026-08-10 · diffed against `validate.py` function by function | **green** |
| REQ-13 | Every new check has been watched failing on a planted defect **and** against a real file | `npm run selftest` (three scripts) + the live catches | 2026-08-10 · 6 + 5 + 5 planted defects caught; `atrium`'s banned transition and 13 wrong ratios caught against real files | **green** |
| REQ-14 | Every gate runnable locally runs in CI | scripts diffed against both workflows | 2026-08-10 · `npm test` and `validate.yml` and `release.yml` all run four gates + three self-tests; release was on one of three | **green** |
| REQ-15 | The audit report exists with `file:line` for every finding | the file | 2026-08-10 · `docs/audit/2026-08-10-skill-audit.md` | **green** |
| REQ-16 | Routing still works after the edits, including the risk the edits introduce | three scenarios in fresh contexts, incl. two core-contract packs that must still be chosen | 2026-08-10 · see the acceptance record | **green** |
| REQ-17 | `v1.10.0` is tagged, released, published; local installs refreshed | `git ls-remote --tags`, `npm view`, the shadow invariant | 2026-08-10 | **green** |
| REQ-18 | Doc map, wiki and graph refreshed — verified by the artifact | `built_at_commit` vs `HEAD`; wiki version string vs the tag | 2026-08-10 · instruction 9 | **green** |
| REQ-19 | Board and verification ledger exist and carry this run's rows | the two files | 2026-08-10 | **green** |
| REQ-20 | `styles/datasheet.md` carries all thirteen headings, `Contract: widened`, and an addressable dated `Origin:` | `validate.py` heading + contract checks; `sloplint.py` origin check | 2026-08-12 · 1647 checks green; the origin check accepts the bare host | **green** |
| REQ-21 | Every value in the pack is measured off the live reference or marked SELECTED at its declaration | the token layer's header defines both words; grep at every declaration | 2026-08-12 · the alarm group was found unmarked by a T24 agent (54 of 118) and is now marked in full | **green** |
| REQ-22 | Every ratio the pack states is recomputed from the token layer | `validate_stated_ratios()` — the table declares its base | 2026-08-12 · palette gate 603 → 716; it caught two of this run's own wrong claims (`--ink-faint` 2.15 vs 3.32, and a 6.24 stated against the wrong base) | **green** |
| REQ-23 | The reference's own accessibility failures are recorded with numbers, never silently applied | the pack's Gotchas, each number recomputed at write time | 2026-08-12 · six corrections recorded: the button label 3.32, the badge ink 2.51, two oranges, reduced motion, the ring on five surfaces, the alarm danger tint 4.44 | **green** |
| REQ-24 | `kits/datasheet` has the identical spine, a doc per component, and a token block copied verbatim | `validate_kits()`; `npm run build` | 2026-08-12 · gate green, and `tsc` emitted 11 components with declarations into `dist/` — verified by listing the directory, not by the exit code | **green** |
| REQ-25 | `datasheet` and every pack a reader could confuse it with name each other | `validate_fork_reciprocity()` | 2026-08-12 · five reciprocal forks: field-notes, instrument-console, showroom, blueprint, scoreboard | **green** |
| REQ-26 | Every count of packs or kits in the library is true, including in the manifests | `validate_counted_claims()`, now reading the three manifests | 2026-08-12 · watched saying no on a planted `eleven` in marketplace.json, plus a permanent self-test plant | **green** |
| REQ-27 | The core-contract paragraph's three numbers match the pack table | `validate_contract_split()` — new | 2026-08-12 · watched saying no on a planted remainder, with its own message; eleven plants caught in the self-test | **green** |
| REQ-28 | T24 is written with both branches **and run** in fresh contexts | the two runs; every finding reproduced before an edit | 2026-08-12 · both green; 22 findings, 11 fixed in the same commit, 1 refuted, 4 filed as B-017…B-020 | **green** |
| REQ-29 | `v1.19.0` is tagged, released and published; the CI verdict read before the tag | `git ls-remote --tags`, `npm view`, the Actions run | — | *pending — stage 7* |
| REQ-30 | Every local channel serves 1.19.0, verified by reading installed files | the shadow invariant plus reading `SKILL.md` in each channel | — | *pending — stage 8* |
| REQ-31 | The code graph's staleness is restated honestly rather than forced past its shrink guard | `built_at_commit` against HEAD; B-009 left open | 2026-08-12 · `9312a85` against a HEAD of `3be7a63`; B-009 holds the two candidate fixes and this run does not choose between them | **green (as restated)** |
