# Acceptance — four style packs, v1.9.0

**Run:** 2026-08-09 · `b426ccc` on `main` · tag `v1.9.0` · npm `1.9.0`
**Carry-over ledger at close: 8 rows — 7 resolved, 1 open** (the code graph's doc
half, carried in from the v1.8.0 run and still blocked on a key the operator
owns). That count sits beside every verdict below on purpose: a green gate
describes what it checks, not what is left.

## The ladder walk

Each REQ walked bottom-up — decision → spec section → contract and its failure
behaviour → change → executed check → surface. Two absences were found this way
and became REQ-018 and REQ-019 **before** the coverage table was written.

| ID | Requirement | Evidence | Status |
|---|---|---|---|
| REQ-001 | Four pack documents on the widened contract with addressable origins | `grep -c '^## '` → **14** each; four `https://` origins on line 3; `validate.py` + `sloplint.py` green | **closed** |
| REQ-002 | Four token layers, hex/rgb/oklch only — no `lab()`, no `color-mix()` | `validate_palette.py` prints a ratio line for all four, which it only reaches after every colour-shaped value parses | **closed** |
| REQ-003 | Each pack's ink clears AA on its own field; each states the figure it holds | 16.87 / 17.74 / 18.95 / 17.49 :1, all in the Palette tables | **closed** |
| REQ-004 | The four corrections documented in the owning pack's Gotchas, with measurements | `blueprint` 21.2 OKLab · `showroom` 2.27:1 · `prism` 2.36:1 · both missing reduced-motion branches | **closed** |
| REQ-005 | `showroom`, `prism` **and `maquette`** declare `never by colour alone` | gate prints `covered by secondary encoding` for all three. `maquette` was added to this list mid-run — see REQ-018 | **closed** |
| REQ-006 | Four kits with the six-component spine matching `kits/workbench` | `validate.py` kit section green | **closed** |
| REQ-007 | Each kit's `styles.css` starts with its token layer verbatim, no colour literal after the marker | proved directly per kit; the gate caught one raw `rgb(` in `maquette` and it was replaced with a token | **closed** |
| REQ-008 | All four routed from `SKILL.md`, `README.md`, `bin/cli.js`, a `.mdc`, and `install.sh` | five `validate.py` checks per pack | **closed** |
| REQ-009 | `.cursor/` mirrors the bundle both directions | `diff -r` identical; gate green | **closed** |
| REQ-010 | Gates above the floors 876 / 305 / 192; both self-tests pass | **1270** / **412** / **224**; both self-tests watched catching planted defects | **closed** |
| REQ-011 | Four scenario pairs, each with a negative branch, each in a separate fresh context | **8 of 8 GREEN**; verdicts and reasoning recorded in `test/scenarios.md` | **closed** |
| REQ-012 | Reciprocal forks, enforced | `validate_fork_reciprocity()` added; watched failing on a planted one-way edge and going quiet on restore | **closed** |
| REQ-013 | Four-way version sync at 1.9.0 with a CHANGELOG top entry | gate's version-sync check; `## [1.9.0] - 2026-08-09` on top | **closed** |
| REQ-014 | `package.json` scripts and `validate.yml` still agree | printed: all three `test/*.py` named in the workflow | **closed** |
| REQ-015 | Released; npm serves 1.9.0; the tarball carries all four | `release.yml` green (release **and** publish); `npm view` → 1.9.0 `latest`; **tarball unpacked** — 29 files per new pack | **closed** |
| REQ-016 | Local installs refreshed; shadow check silent | plugin **1.9.0**, 12 packs installed, shadow check prints nothing | **closed** |
| REQ-017 | DOCMAP floors, wiki, code graph | floors → 1270/412/224 at `b426ccc`; wiki overview + concept updated, new `skills/` page, every link resolves; graph 1042 → **1313** nodes, stamp current | **closed, with REQ-019 split out** |
| **REQ-018** | *(found on the ladder)* **`maquette`'s status palette was invented, not measured** — and the brief said the pack needed no correction | The gate caught it: 7.9 under deuteranopia, 7.8 under protanopia. The set was re-derived inside the pack's own world, the token layer now marks it as a pack decision, and **the brief and design record were corrected** — they had carried a false claim | **closed** |
| **REQ-019** | *(found on the ladder)* The code graph is refreshed on its **code half only** | No backend key on this machine — six env vars and `~/.graphify` checked again this run, all absent. `--code-only` took it to 1313 nodes with the stamp current; the doc nodes are one release behind | **open** — ledger C6, operator |

## Gate verdicts, with the ledger count beside them

| Gate | Verdict | Floor | Carry-over open |
|---|---|---|---|
| `validate.py` | OK, **1270 checks** | 876 | 1 |
| `validate_palette.py` | OK, **412 checks** | 305 | 1 |
| `sloplint.py` | OK, **224 checks** | 192 | 1 |
| both `--self-test` | every planted defect caught | — | 1 |
| `validate_fork_reciprocity()` | watched failing on a planted one-way edge | new | 1 |
| `claude plugin validate --strict` | passed | — | 1 |
| `validate.yml` on `main` | green, **15 jobs** (12 kits, matrix derived) | — | 1 |
| `release.yml` on `v1.9.0` | green — release **and** publish | — | 1 |

## What the scenario agents caught that the gates could not

Three findings, each reported by a subagent, each **reproduced against the
artifact before anything was edited** — standing instruction 8:

1. **`blueprint` contradicted itself about registration marks.** Signature
   element said one thing per viewport; Components and Hero gave them to both
   CTAs. Fixed: the primary only, and the Signature element now says so.
2. **The three vector-database packs did not fork against each other.** Reported
   independently by two agents; one said it had to *derive* the distinction
   because it was not written down. The reciprocity work had drawn every
   new-to-old edge and missed every new-to-new one.
3. **The fork clauses are being read from both sides.** Two negative-branch
   agents quoted *both* halves of a fork by file and line, and one said it used
   the test "as written rather than inventing one" — which is the reciprocity fix
   doing exactly the job it was added for.

## Still open

- **C6 / REQ-019 — the code graph's doc half.** No graphify backend key exists on
  this machine. Set one, then one full `graphify . --update`. `GRAPH_REPORT.md`
  is unregenerated for the same reason.
