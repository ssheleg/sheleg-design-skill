# Acceptance — `paperclip`, the eighteenth style pack (v1.29.0, provisional)

Run `2026-08-14-paperclip-pack`, on `feat/paperclip-pack` in its own worktree. **Not
merged and not released**: the number is provisional because a concurrent run held
1.28.0 while this one was authored (see the brief).

## The table

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-01 — thirteen headings + a `Contract:` line | ✅ | `validate_contract_declaration()` and `validate_contract_split()` green; `Contract: widened` |
| REQ-02 — `Origin:` is addressable and re-readable | ✅ | `https://paperclip.ing` plus both stylesheet paths and the read date; the provenance gate accepts it |
| REQ-03 — every value measured or marked derived | ✅ | one DERIVED value in the whole token layer (`--info`), marked at the declaration with the 3.83:1 it replaces |
| REQ-04 — every stated ratio recomputed | ✅ | `validate_palette.py` **1001 → 1125** checks, green in both themes |
| REQ-05 — status separates, or says why it cannot | ✅ | three tight pairs reported and covered: `--good`/`--warn` 6.2 protanopia (dark) and 6.4 (light), `--good`/`--info` 6.7 tritanopia; the pack states *"status is never by colour alone"* and the components carry the word |
| REQ-06 — a kit whose spine matches the exemplar | ✅ | six spine components, props byte-identical to `kits/workbench` once comments are stripped; `tsc -p tsconfig.json` exits 0 |
| REQ-07 — no component sized by the viewport | ✅ | four `container-type: inline-size` roots, four `@container` blocks, zero width `@media` below the components marker |
| REQ-08 — token layer copied, not transcribed | ✅ | `kits/paperclip/src/styles.css` opens with `styles/tokens/paperclip.css` byte for byte; checked by `validate_kits()` |
| REQ-09 — no raw colour literal in kit components | ✅ | `color-mix(in srgb, …)` for every tint below the marker; gate green |
| REQ-10 — the pack is chosen-able everywhere | ✅ | all seven enumeration sites name it; `validate_pack_enumerations()` green |
| REQ-11 — forks are reciprocal | ✅ | `instrument-console`, `workbench`, `orchard` each link back; `validate_fork_reciprocity()` green |
| REQ-12 — the routing scenario exists with its negative branch | ⚠️ | `T27a` / `T27b` written; **not run** |

## The gate, run

```
npm test  →  OK (2189 checks) · OK (1125 checks) · OK (470 checks) · self-tests OK · exit 0
```

Floors before this run: `validate.py` 2067, `validate_palette.py` 1001, `sloplint.py` 450.
After: **2189 / 1125 / 470**. Every one rose; none was lowered.

`kits/paperclip`: `npm install && npm run build` → exit 0, `dist/` regenerated and ignored.

## The one thing that is not discharged

**T27 has not been run.** `validate.py` does not read `test/scenarios.md`, so nothing in
`npm test` covers routing behaviour, and the propagation matrix's proof for that row is *a
person running the scenario against a fresh context and stamping the result with a
commit*. The scenario's own Result line says `NOT YET RUN` rather than leaving the reader
to infer it from silence.

Everything else in this pack is either measured off the reference or computed by a gate.

## What the merge owes

1. **A recount.** This branch is off `main` at seventeen packs and writes eighteen
   everywhere. `ora` and `tenor` land the same day from another run; the counted-claims
   gate will name every site that needs moving, and it names them precisely — that is what
   it is for.
2. **A version decision.** 1.29.0 was chosen to avoid the 1.28.0 the other run claimed. If
   that run ships 1.28.0 and 1.29.0 both, this branch moves again.
3. **Two fork clauses that do not exist yet.** `ora` is the closest pack in the library to
   this one — dark by default, no third hue, mono for machine facts — and neither can link
   to the other from a branch where only one of them exists. The reciprocal pair is owed at
   merge, in both directions, and `validate_fork_reciprocity()` will not ask for it
   because neither pack mentions the other yet. This is the one item a gate cannot catch.
