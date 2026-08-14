# Acceptance — `paperclip`, the twentieth style pack (v1.30.0)

Run `2026-08-14-paperclip-pack`, authored on `feat/paperclip-pack` in its own worktree and
merged into `main` after the concurrent run landed `ora` and `tenor`. The version moved
twice — 1.29.0 while the other run was assumed to hold 1.28.0, then 1.30.0 once it shipped
1.29.0 itself (see the brief).

## The table

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-01 — thirteen headings + a `Contract:` line | ✅ | `validate_contract_declaration()` and `validate_contract_split()` green; `Contract: widened` |
| REQ-02 — `Origin:` is addressable and re-readable | ✅ | `https://paperclip.ing` plus both stylesheet paths and the read date; the provenance gate accepts it |
| REQ-03 — every value measured or marked derived | ✅ | one DERIVED value in the whole token layer (`--info`), marked at the declaration with the 3.83:1 it replaces |
| REQ-04 — every stated ratio recomputed | ✅ | `validate_palette.py` **1156 → 1280** checks after the merge, green in both themes |
| REQ-05 — status separates, or says why it cannot | ✅ | three tight pairs reported and covered: `--good`/`--warn` 6.2 protanopia (dark) and 6.4 (light), `--good`/`--info` 6.7 tritanopia; the pack states *"status is never by colour alone"* and the components carry the word |
| REQ-06 — a kit whose spine matches the exemplar | ✅ | six spine components, props byte-identical to `kits/workbench` once comments are stripped; `tsc -p tsconfig.json` exits 0 |
| REQ-07 — no component sized by the viewport | ✅ | four `container-type: inline-size` roots, four `@container` blocks, zero width `@media` below the components marker |
| REQ-08 — token layer copied, not transcribed | ✅ | `kits/paperclip/src/styles.css` opens with `styles/tokens/paperclip.css` byte for byte; checked by `validate_kits()` |
| REQ-09 — no raw colour literal in kit components | ✅ | `color-mix(in srgb, …)` for every tint below the marker; gate green |
| REQ-10 — the pack is chosen-able everywhere | ✅ | all seven enumeration sites name it; `validate_pack_enumerations()` green |
| REQ-11 — forks are reciprocal | ✅ | `instrument-console`, `workbench`, `orchard` and `ora` each link back; `validate_fork_reciprocity()` green |
| REQ-12 — the routing scenario exists with its negative branch, and has run | ✅ | `T29a` / `T29b` run blind against the bundle, **green on both**; 41 findings, 26 fixed here and 15 filed as B-038 … B-043 |

## The gate, run

Twice, because the branch was measured before the merge and again after it.

| | `validate.py` | `validate_palette.py` | `sloplint.py` |
|---|---|---|---|
| floor at branch point (`cc3b471`, 17 packs) | 2067 | 1001 | 450 |
| this branch alone (`572bb0e`, 18 packs) | 2189 | 1125 | 470 |
| floor on `main` after `ora` + `tenor` (19 packs) | 2294 | 1156 | 478 |
| **merged (20 packs)** | **2422** | **1280** | **498** |

Every one rose at every step; none was lowered. `npm test` exits 0, self-tests green.

`kits/paperclip`: `npm install && npm run build` → exit 0, `dist/` regenerated and ignored.

## The one thing that was not discharged, and now is

**T29 has run.** Both branches green, blind against the bundle directory only. The
scenario's Result line carries the findings rather than a verdict, because a routing
scenario that only says "it chose correctly" tests nothing the pack table could not have
answered: what the pair is for is the twenty-six defects it found in a pack every gate had
already passed.

Two of those are worth carrying forward as a class. The first: **the gates cannot see a
claim about a value, only a value.** `--cream` was prescribed in prose and never declared;
`--terminal-dim` was spent as a clickable label at 2.92:1; all three stagger formulas
hardcoded the literal the token exists to hold. Every one of those passed
`validate.py`, `validate_palette.py` and `sloplint.py` three times. The second: **a
scenario finds defects in whatever it reads, not in what it was written to test.** T29a was
built to separate this pack from `instrument-console`; it rejected `tenor` and `ora`
instead, on clauses that were better than the ones the scenario predicted — and then found
that `SKILL.md` had never marked any of the three newest packs standalone.

## What the merge owed, and what it did

1. **A recount.** ✅ Every site moved from eighteen to twenty — README (×4), `bin/cli.js`,
   the three manifests, `SURFACE_COMPOSITION.md` (×4), `MOBILE_SURFACES.md`,
   `DESIGN_SYNC_BRIDGE.md`, `SKILL.md` (×3) and the `/sheleg-design` fast path. The
   `@role non-text:` tally recomputed to fourteen of twenty and the accent tally to
   eighteen; both were counted from the token layers, not adjusted by one.
2. **A version decision.** ✅ 1.30.0. The other run shipped **1.29.0**, the number this
   branch had already taken — so the collision arrived from the other side despite the
   avoidance. Recorded in the brief as a finding rather than a footnote: a version is not
   reservable by guessing.
3. **The `ora` fork.** ✅ Written in both directions, and it is the one edge in this run
   that **no gate could have requested** — `validate_fork_reciprocity()` only checks links
   that already exist, and neither pack existed in the other's tree while either was being
   authored. Two packs that a screenshot cannot separate would have shipped with nothing
   pointing between them.

## One correction on the record

An earlier draft of this file stated the post-merge gate counts **2529 / 1341 / 508**. They
were written before the gate was run and the measured numbers are **2422 / 1280 / 498** —
restating a number instead of computing it, in the document whose whole job is to hold
computed numbers. Corrected here rather than silently overwritten, because this repository
has shipped exactly this failure before (v0.22.0: notes said 71 fixtures, the acceptance
record said 74, the count was 75).
