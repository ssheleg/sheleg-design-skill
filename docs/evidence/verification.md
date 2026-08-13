# Verification ledger — sheleg-design-skill

One row per shipped REQ, written at stage 8 and required at stage 10 in both
directions: no REQ without a row, no row without a REQ.

`Last verified` is a date **and** the thing that was watched — not "tests pass".
`never` is a legitimate value and the one worth counting: it says a requirement
was shipped on the strength of an argument rather than an observation.

Seeded 2026-08-10 by the `2026-08-10-skill-audit` run. **Rows at `never`: 1** (REQ-10, carried to board B-004). Extended 2026-08-12 by the `pigeonhole` run with twenty rows, none of them `never`.

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
| REQ-29 | `v1.19.0` is tagged, released and published; the CI verdict read before the tag | `git ls-remote --tags`, `npm view`, the Actions run | 2026-08-12 · validate run 31607435774 green on `f4f25ce` **before** the tag, with 14 of 14 kit jobs including `kits (datasheet)`; release+publish run 31607540101 green; `npm view` 1.19.0; the published tarball unpacked and read — 449 files carrying the pack, its token layer and the kit | **green** |
| REQ-30 | Every local channel serves 1.19.0, verified by reading installed files | the shadow invariant plus reading `SKILL.md` in each channel | 2026-08-12 · plugin cache `1.19.0/skills/sheleg-design/SKILL.md` reads `version: 1.19.0` and carries `styles/datasheet.md` + its token layer; the hub copy reads 1.19.0 and has the pack; the shadow invariant printed nothing. Read from disk, not from the updater's output | **green** |
| REQ-31 | The code graph's staleness is restated honestly rather than forced past its shrink guard | `built_at_commit` against HEAD; B-009 left open | 2026-08-12 · `9312a85` against a HEAD of `3be7a63`; B-009 holds the two candidate fixes and this run does not choose between them | **green (as restated)** |

### `pigeonhole` / v1.21.0 — 2026-08-12

| REQ | What must stay true | How it is checked | Last verified | Status |
|---|---|---|---|---|
| P-01 | `styles/pigeonhole.md` carries thirteen headings plus `## Motion flavor`, `Contract: widened`, and a dated addressable `Origin:` | `validate.py` heading + contract checks; `sloplint.py` origin check | 2026-08-12 · green at 1920 checks | **green** |
| P-02 | Every token declaration says which kind of claim it is | grep for the four provenance words at each declaration | 2026-08-12 · watched finding two silent declarations, then 121 of 121 marked | **green** |
| P-03 | The token layer passes the palette gate, with nothing the gate cannot parse | `npm run palette` | 2026-08-12 · OK at 906 | **green** |
| P-04 | Every ratio the pack or the layer states recomputes from the tokens | `validate_stated_ratios()` | 2026-08-12 · watched refusing nine of this run's own lines before it passed | **green** |
| P-05 | The reference's own accessibility failures are recorded with numbers, never applied | `## Gotchas`, each number recomputed at write time | 2026-08-12 · eight inks, the lede, the CTA's two stops, the badge, the missing focus ring | **green** |
| P-06 | The category set's exclusion from the peer set carries the number that justifies it, and the pack states status is never by colour alone | the declaration; the palette gate's secondary-encoding escape | 2026-08-12 · ΔE 4.42 → 1.24 stated; the causal claim corrected after T25a refuted it | **green** |
| P-07 | The type ramps produce the sizes the pack states | arithmetic at each measured viewport | 2026-08-12 · 5.6vw refuted (43.01px at 768); refitted to 7.82vw and 5.21vw, recomputed at 390/768/1440 | **green** |
| P-08 | Reduced motion actually stops the marquee | the component layer, not the duration | 2026-08-12 · `animation-play-state: paused`; a 0.01ms infinite animation strobes and was watched doing so in arithmetic | **green** |
| P-09 | `kits/pigeonhole` has the identical spine, a doc per component, tokens copied byte for byte | `validate_kits()`; `dist/` listed after `tsc` | 2026-08-12 · gate green; 11 modules with declarations, read from the directory | **green** |
| P-10 | `pigeonhole` and every pack a reader could confuse it with name each other | `validate_fork_reciprocity()` | 2026-08-12 · five reciprocal forks | **green** |
| P-11 | Every count of packs or kits is true, in every channel | `validate_counted_claims()`, `validate_contract_split()` | 2026-08-12 · the gate found five sites the sweep missed | **green** |
| P-12 | The nine-versus-eleven distinction is stated the same way everywhere | grep across eleven sites | 2026-08-12 · found by both T25 branches, swept | **green** |
| P-13 | The floors rise with a reason and refuse a drop | the three gates against `floors.json` | 2026-08-12 · watched refusing 1921 with its own message | **green** |
| P-14 | A routing scenario with its negative branch exists **and has run** | T25a / T25b in fresh contexts | 2026-08-12 · both green, before the tag | **green** |
| P-15 | `v1.21.0` is tagged, released, published, and the CI verdict was read before the tag | `gh run view`, `git ls-remote --tags`, `npm view` | 2026-08-12 · run 31642256634 green on `98722cd`, the commit tagged; npm 1.21.0 | **green** |
| P-16 | The published tarball carries the pack, its tokens and the kit | the tarball pulled from the registry and read | 2026-08-12 · 509 files; pack 29,203 bytes; 27 kit files; `7.82vw` present | **green** |
| P-17 | Every local channel serves 1.21.0, verified by reading installed files | the resolved install path, the hub copy, the shadow invariant | 2026-08-12 · plugin resolves to `…/1.21.0` carrying the pack; hub reads 1.21.0; shadow check silent | **green** |
| P-18 | Refuted claims are recorded rather than dropped | the brief, the design record, Gotchas, the CHANGELOG | 2026-08-12 · no rotation anywhere; the diptych is raster art | **green** |
| P-19 | The graph's staleness is restated honestly rather than forced | `built_at_commit` against HEAD | 2026-08-12 · `9312a85` against `149324c`; B-009 untouched | **green (as restated)** |
| P-20 | Every run leaves a stamp, so the retirement trigger stays computable | `retro.md`'s run stamps | 2026-08-12 · this run stamped and the 1.20.0 run backfilled | **green** |

### `color-mix()` and relative colour / v1.22.0 — 2026-08-13

| REQ | What must stay true | How it is checked | Last verified | Status |
|---|---|---|---|---|
| M-01 | The gate computes `color-mix()` in the four spaces it claims, and refuses the rest | four self-test plants + the browser oracle | 2026-08-13 · Chrome 151, eleven cases, worst ΔE **0.004**; an unimplemented space and a `calc()` channel both watched failing with "cannot compute" | **green** |
| M-02 | The new paths are *checked*, not merely tolerated | a mix and a relative colour whose ink misses AA must fail on the ratio | 2026-08-13 · both watched failing with "below WCAG AA", which is only reachable if the value was computed | **green** |
| M-03 | `var()` resolves inside a value, not only as a whole value | `resolve()` → `substitute_vars()`; the showroom ring resolves to `rgb(from #266df0 …)` | 2026-08-13 · read out of the token layer | **green** |
| M-04 | A theme written in a new colour form is still validated | `themes()` asks `COLOR_SHAPED` instead of a `#`/`oklch(` prefix list | 2026-08-13 · the blind spot was closed in the same commit that could have opened it | **green** |
| M-05 | `showroom`'s migrated ring renders exactly what the literal did | ΔE between the derived value and the literal it replaced | 2026-08-13 · **ΔE 0.0000**, alpha 0.35 both sides | **green** |
| M-06 | A browser that cannot parse relative colour still gets a focus ring | the literal declared first, the derived value second | 2026-08-13 · both declarations present in the published tarball | **green** |
| M-07 | The lifted ban reaches the author, in all three copies of the skeleton | `validate.py` mirror + template parity | 2026-08-13 · bundle, `.cursor` mirror and `templates/` all carry rule 5; the gate found the third copy | **green** |
| M-08 | `v1.22.0` is tagged, released, published, CI read before the tag | `gh run view`, `npm view`, the tarball | 2026-08-13 · run 31649056089 green on `4f78dff` (18 jobs) **before** the tag; npm 1.22.0; tarball 509 files carrying rule 5 and both ring declarations | **green** |
| M-09 | Every local channel serves 1.22.0, verified by reading installed files | the resolved install path, the hub copy, the shadow invariant | 2026-08-13 · plugin resolves to `1.22.0` and carries rule 5; hub reads 1.22.0; shadow check clean | **green** |
| M-10 | The measurement behind the audit is reproducible, not asserted | the sweep script's three-way split | 2026-08-13 · 42 EXACT / 13 NEAR / 45 OWN across sixteen token layers | **green** |

### Container queries in the kits / v1.23.0–1.23.1 — 2026-08-13

| REQ | What must stay true | How it is checked | Last verified | Status |
|---|---|---|---|---|
| C-01 | Every widened pack says which components size against their container | `validate_pack_container_answer()` | 2026-08-13 · watched refusing `scoreboard` with its answer removed; 10 of 10 widened packs answer, six core packs exempt | **green** |
| C-02 | A kit's width query is either a `:root` switch or a declared reason | `validate_kit_breakpoints()` | 2026-08-13 · watched refusing the scoreboard ledger reverted to `@media`; seven blocks found, all now declared | **green** |
| C-03 | The check does not punish a longer explanation | the marker is read from the whole comment, not a fixed window | 2026-08-13 · its first draft looked back 400 characters and missed a marker at 425; both TODO blocks pass now | **green** |
| C-04 | `scoreboard`'s ledger sizes against its own box, which its pack has always required | a browser, at a wide viewport | 2026-08-13 · at **viewport 1440** a 220px ledger takes the narrow columns (75/70) and a 900px one the wide (95/80) — the case the viewport query got wrong | **green** |
| C-05 | `container-type: inline-size` does not collapse the ledger | the same probe | 2026-08-13 · ledger width follows its parent: 900 → 900px, 220 → 220px, 231 → 231px | **green** |
| C-06 | The ledger's breakpoint is derived, not carried over from 767px | arithmetic on the pack's own tokens | 2026-08-13 · 95 + 12 + 80 + 12 = 199px fixed content + a 32px minimum leader = **231px**; at the boundary the leader measures 62px | **green** |
| C-07 | Every breakpoint the kits own is classified truthfully, including the ones with no container answer | the marker at each block | 2026-08-13 · two CONTAINER (held, B-032), three SELF, one PAGE, one `:root` — and the mixed blocks were split so no marker describes half a block | **green** |
| C-08 | Every component named in the seven new answers exists in its kit | each kit's exports against the prose | 2026-08-13 · five right, two wrong and fixed in 1.23.1 (`showroom`'s "table wrapper" → `Specimen`; `pigeonhole`'s wrapper claim → the consumer's list); `maquette`'s "agent prompt" recorded as a pre-existing pack/kit gap | **green** |
| C-09 | A pack does not tell an implementer to do what the skeleton calls impossible | reading the two answers against the SELF definition shipped beside them | 2026-08-13 · `pigeonhole` did exactly that in 1.23.0 and is corrected in 1.23.1 | **green** |
| C-10 | `v1.23.0` and `v1.23.1` are tagged, released, published, CI read before each tag | `gh run view`, `npm view` | 2026-08-13 · run 31652390928 green on `bd3a5b4` before the first tag, 31652643202 green on `c2b271b` before the second | **green** |

### `roster`, the seventeenth pack / v1.24.0 — 2026-08-13

| REQ | What must stay true | How it is checked | Last verified | Status |
|---|---|---|---|---|
| R-01 | `styles/roster.md` carries thirteen headings plus Motion flavor, `Contract: widened`, a dated addressable `Origin:` | `validate.py` heading + contract checks; `sloplint.py` origin check | 2026-08-13 · green at 2066 checks | **green** |
| R-02 | Every value is MEASURED, RESOLVED, SELECTED or DERIVED at its declaration | the token layer's header defines all four; grep at each declaration | 2026-08-13 · RESOLVED is new this release, for a `lab()` read off a painted pixel | **green** |
| R-03 | Every `lab()` the reference paints is resolved to the sRGB the browser shows | a 1×1 canvas, painted and read back, with four controls | 2026-08-13 · `#fa5c12`, `rgb(23,23,23)`, `lab(100 0 0)`, `lab(0 0 0)` all round-tripped before the 34 values were trusted | **green** |
| R-04 | Every ratio the pack states recomputes from the shipped hexes, prose included | `validate_stated_ratios()` plus a by-hand sweep of all nineteen | 2026-08-13 · 19 of 19 exact; the gate caught three lines where the reference's FAILING number sat on a derived token's own declaration | **green** |
| R-05 | The four white-field-only colours say so, with the numbers for every surface | the Palette's paragraph and each declaration | 2026-08-13 · **found by T26a**: 4.32 / 4.10 / 4.06 on the three tinted surfaces, where the layer had claimed "BOTH" meaning two of four | **green** |
| R-06 | The reference's failures are recorded with numbers, never applied | the Gotchas | 2026-08-13 · nav label 3.43, accent 3.18, secondary ink 4.35 on its own band, reduced motion covering six animations, 13 bare `100vh` | **green** |
| R-07 | The pack states which heading convention it teaches | the Type section | 2026-08-13 · the reference's `h1` is `.sr-only` at 1×1px and its sixteen `h2`s are eyebrows; the pack refuses both and `manpage` carries the fork | **green** |
| R-08 | The container-query answer the 1.23.0 contract requires is present and specific | `validate_pack_container_answer()` | 2026-08-13 · CONTAINER for the column, the step card and the case card; PAGE for hero, nav and the display steps; SELF for the pattern density | **green** |
| R-09 | Every width query the kit ships is a container query or carries its reason | `validate_kit_breakpoints()` | 2026-08-13 · it caught this pack's own second display step unmarked, on a pack written after the gate | **green** |
| R-10 | Both kit breakpoints are derived from the component's geometry, not the viewport | the arithmetic at each block | 2026-08-13 · 220px for the column's mark grid, 640px for the step split | **green** |
| R-11 | The signature motif is buildable without an asset nobody ships | the token layer | 2026-08-13 · **found by T26a**: the SVG was fetched and measured — 8.367px square, 0.85px radius, `#7f99d1` at 12% = `#f4f6fa`, 0.3px white stroke, 9.667px pitch | **green** |
| R-12 | `roster` and every confusable pack name each other | `validate_fork_reciprocity()` | 2026-08-13 · four reciprocal forks: scoreboard, showroom, pigeonhole, manpage | **green** |
| R-13 | Every count moves sixteen → seventeen, manifests included | `validate_counted_claims()`, `validate_contract_split()` | 2026-08-13 · plus the accent-role tally recounted from the token layers (15), not incremented | **green** |
| R-14 | A routing scenario with its negative branch exists **and has run** | T26a / T26b in fresh contexts | 2026-08-13 · both green before the tag; 37 findings, 15 fixed, 1 refuted, 20 filed | **green** |
| R-15 | A refuted finding is recorded, and anything it disproves is corrected | the scenario result and both packs | 2026-08-13 · `0s` freezes an infinite animation and `0.01ms` strobes it, measured in Chrome 151 — so `pigeonhole` 1.21.0 and `roster` were both over-stating, and both now carry the precise rule | **green** |
| R-16 | A pack and its kit do not disagree | reading one against the other | 2026-08-13 · **a regression this session introduced**: `scoreboard`'s pack still documented the viewport rule its kit replaced in 1.23.0. Fixed | **green** |
| R-17 | `v1.24.0` tagged, released, published; CI read **before** the tag | `gh run view`, `npm view` | 2026-08-13 · run 31657872393 green on `cf06b75`, 19 jobs, the commit tagged | **green** |
| R-18 | The published tarball carries the pack, its tokens and the kit | the tarball pulled from the registry and read | 2026-08-13 · see the close-out | **green** |
| R-19 | Every local channel serves 1.24.0, verified by reading installed files | the resolved install path, the hub copy, the shadow invariant | 2026-08-13 · see the close-out | **green** |
| R-20 | ADR-0001 records the naming, with the rejected alternatives and why | the file | 2026-08-13 · tenth application; `pegboard`, `directory` and `lobby` rejected on the ADR's own criteria | **green** |

### A status colour on its own field / v1.26.0 — 2026-08-13

| REQ | What must stay true | How it is checked | Last verified | Status |
|---|---|---|---|---|
| S-01 | Every semantic colour is measured against the field of **its own theme**, not the pack's first one | `validate_status_on_field()` | 2026-08-13 · first run found 28 findings in 11 of 17 packs; `scoreboard`'s panel band was the mechanical one | **green** |
| S-02 | The three tiers are enforced, not described: ≥4.5 text, ≥3.0 declared, <3.0 declared **and** the pack says status is never by colour alone | two plants, one per tier | 2026-08-13 · both watched failing; the check's core was split out so a plant can be a token layer as a string | **green** |
| S-03 | `@role non-text:` is a canonical marker, documented beside `@role accent:` | `SURFACE_COMPOSITION.md`; the regex in the gate | 2026-08-13 · 11 packs declare it; five prose phrasings replaced by one greppable form | **green** |
| S-04 | `scoreboard`'s dark band uses the on-dark status set its own Bans require | the token layer, measured | 2026-08-13 · 10.21 / 11.49 / 6.92 / 7.51 on the panel, where they had been 3.69 / 3.94 / 2.37 / 2.90 (B-034 closed) | **green** |
| S-05 | `showroom`'s status chip does not paint its label in its own status colour | the pack and the kit read against each other | 2026-08-13 · label is `--ink` at 14.65–14.73:1, the colour is the tint plus a 6px dot; was 2.03 / 1.54 / 2.65 (B-021 closed) | **green** |
| S-06 | `blueprint` states legibility, not only separation | the pack | 2026-08-13 · `--good` 2.40, `--warning` 1.72, `--info` 1.21 on the stock named in the pack, with the colour-alone rule | **green** |
| S-07 | No colour changed that did not have to | the diff | 2026-08-13 · 3 packs changed values, 24 findings were declarations only | **green** |
| S-08 | The `.cursor` mirror and the kits carry every token edit | `validate.py` mirror parity | 2026-08-13 · green; propagated in the same change | **green** |
| S-09 | A gate's check count does not move with whether a worktree exists | the nested-checkout plant, whose pass condition is silence | 2026-08-13 · **found by the merge disagreeing with itself**: 2361 with a worktree present, 2067 clean on one commit; watched reporting `MISSED` with the guard removed | **green** |
| S-10 | The class is swept, not just the site that showed it | reading the sibling gates | 2026-08-13 · `sloplint.py` walks `SKILL_DIR.rglob`, `validate_palette.py` does not recurse; only `validate.py`'s two ROOT walks were exposed | **green** |
| S-11 | Floors are the counts of the merged tree, and the raise carries its reason | `test/floors.json`, re-measured | 2026-08-13 · 2067 / 1001 / 450; palette additive as 958 base + 8 concurrent + 35 this check | **green** |
| S-12 | A version taken by a concurrent run costs nothing but a number | the tag, the registry, the prose | 2026-08-13 · 1.25.0 left exactly as published, its entry reseated under the preamble; 22 version references in prose moved with the release | **green** |
| S-13 | `v1.26.0` tagged, released, published; CI read **before** the tag | `gh run view`, `npm view` | 2026-08-13 · run 31661837515 green on `a9c497e`, 19 jobs, tree `279af78` identical to `main^{tree}` | **green** |
| S-14 | The published tarball carries the check, the marker and no stale version | the tarball pulled from the registry and read | 2026-08-13 · 1.26.0 in both manifests, `@role non-text` present, **0** stale `1.25.0` references outside the CHANGELOG, 17 packs | **green** |
| S-15 | Every local channel serves 1.26.0, verified by reading installed files | the resolved install path, the hub copy, the shadow invariant | 2026-08-13 · plugin cache `.../1.26.0/skills/sheleg-design/SKILL.md` and `~/.agents/skills/sheleg-design/SKILL.md` both `version: 1.26.0`; no plain copy in `~/.claude/skills`; 17 packs + template installed | **green** |
