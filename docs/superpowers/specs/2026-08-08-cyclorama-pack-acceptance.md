# Acceptance — `cyclorama` style pack, v1.8.0

**Run:** 2026-08-08 · `025f866` on `main` · tag `v1.8.0` · npm `1.8.0`
**Carry-over ledger at close: 11 rows — 0 resolved by this run, 5 belong to
stage 9 and were discharged there, 6 are open and owned elsewhere.** That count
is printed beside every verdict below on purpose: a green gate describes what it
checks, not what is left.

## The ladder walk

Each REQ was walked bottom-up — decision → spec section → contract and its
failure behaviour → change → executed check → surface — and the seam inspected
at each step. Two absences were found this way and are recorded as REQ-018 and
REQ-019 below, **before** the coverage table was written.

| ID | Requirement | Evidence | Status |
|---|---|---|---|
| REQ-001 | Pack carries the thirteen widened headings plus `## Motion flavor`, and an addressable `Origin:` | `grep -c '^## '` → **14**; `Origin: <https://www.codos.ai/>` on line 3; `validate.py` pack section and `sloplint.py` `lint_packs` both green | **closed** |
| REQ-002 | Token layer parses entirely — no `color-mix()`, nothing uncomputable | `validate_palette.py` prints a ratio line for `cyclorama`, which it only reaches after every colour-shaped value parses | **closed** |
| REQ-003 | `--ink` on `--bg` clears AA on every stop, and the pack states the worst | gate printed `--ink on --bg = 13.90:1` (rest stop); the Palette table quotes all six and names `--field-2` **12.79:1** as the floor | **closed** |
| REQ-004 | The accent is documented fill-only, with the measured failure and the three rejected repairs | `cyclorama.md:84, 93, 344, 372` (1.71–1.97:1) and `:382–384` (the three candidates with their separations) | **closed** |
| REQ-005 | The pack declares `never by colour alone`; the gate reports the tight pairs as covered | phrase present once; gate prints `--danger/--good tight (14.0 …; 5.9 under deuteranopia) -- covered by secondary encoding` | **closed** |
| REQ-006 | Kit ships the six spine components with `*Props` matching `kits/workbench` | `validate.py` kit section green (it compares comment-stripped prop bodies across every kit) | **closed** |
| REQ-007 | `styles.css` starts with the token layer verbatim; no colour literal after the marker | proved directly: `startswith(tokens)` → `True`, regex scan after `/* ── components ── */` → no hits; and `validate.py` checks 6 and 7 | **closed** |
| REQ-008 | Routed from `SKILL.md`, `README.md`, `bin/cli.js`, `cursor/rules/*.mdc` | four separate `validate.py` checks, all green | **closed** |
| REQ-009 | `.cursor/` mirrors the bundle file-by-file, both directions | `diff -r` → identical; `validate.py` mirror check green | **closed** |
| REQ-010 | Three gates above their ratchet floors; both `--self-test` flags pass | **875** (floor 787) · **305** (269) · **192** (184); both self-tests watched catching every planted defect | **closed** |
| REQ-011 | T15a and T15b, each in a separate fresh context | both GREEN; verdicts and reasoning recorded in `test/scenarios.md`. T15b did **not** drift to the newer warm pack — the over-generalisation branch did not fire | **closed** |
| REQ-012 | `docs/adr/0001-style-pack-naming.md` restored, status line noting the second application | file present; status block records both the restoration and the `cyclorama` application | **closed** |
| REQ-013 | Four-way version sync at 1.8.0 with a CHANGELOG top entry | `validate.py` version-sync check green; `## [1.8.0] - 2026-08-08` is the top entry | **closed** |
| REQ-014 | `package.json` scripts and the CI workflow agree | printed the diff: all three `test/*.py` named in `validate.yml`, all six script step-lists present. Standing instruction 7 | **closed** |
| REQ-015 | `v1.8.0` released; npm serves it | `release.yml` run `31261839050` green (release + publish); `npm view` → **1.8.0**, `latest`; GitHub release published, not draft; the **published tarball unpacked** and carries `styles/cyclorama.md`, `tokens/cyclorama.css` and all of `kits/cyclorama/` | **closed** |
| REQ-016 | Local installs refreshed on this machine | `npx sshlg-skills@latest update` → `sheleg-design` **1.7.0 → 1.8.0**; installed copy lists `cyclorama.md`; shadow check prints nothing; 0 broken symlinks across five channels | **closed** |
| REQ-017 | `DOCMAP.md` floors, the wiki, and the code graph refreshed and checked | floors rewritten to 875/305/192 at `025f866`; wiki overview + `style-packs-architecture` updated and a new `skills/` page added with every link resolving; graph **partially** refreshed — see REQ-019 | **closed, with REQ-019 split out** |
| **REQ-018** | *(found on the ladder)* `DOCMAP.md`'s propagation matrix understated a new pack's obligations — it said "all nine headings" and omitted the `.cursor/` mirror, `install.sh`, the `.mdc` rule and the scenario | corrected in the same stage-9 pass; the row now lists all eleven obligations. Ledger C5 | **closed** |
| **REQ-019** | *(found on the ladder)* The code graph is refreshed on its **code half only** | `graphify . --update` exited 0 while refusing to run; `--code-only` took it 987 → **1042 nodes** with `built_at_commit` now `025f866`, but the 35 changed doc files were not re-extracted. Visible in `god-nodes`, where a hub still reads "T1–T14" | **open** — ledger C11, needs an API key the operator owns |

## Gate verdicts, with the ledger count beside them

| Gate | Verdict | Floor | Carry-over open at this point |
|---|---|---|---|
| `validate.py` | OK, **875 checks** | 787 | 6 |
| `validate_palette.py` | OK, **305 checks** | 269 | 6 |
| `sloplint.py` | OK, **192 checks** | 184 | 6 |
| both `--self-test` | every planted defect caught | — | 6 |
| `claude plugin validate --strict` | passed | — | 6 |
| `validate.yml` on `main` | green, **eight** kit jobs (matrix derived, not typed) | — | 6 |
| `release.yml` on `v1.8.0` | green — release **and** publish | — | 6 |

## What this run did not do

- Did not fix the `field-notes` `--deep` contradiction a subagent surfaced and
  this run reproduced (C9). It is shipped, and the fix is a judgement call.
- Did not chmod `install.sh`, whose own usage line documents an invocation that
  cannot work (C10). Pre-existing; not worth re-cutting a verified release.
- Did not fully refresh the code graph (C11), and did not regenerate
  `GRAPH_REPORT.md`.
- Did not touch `feat/lecture-hall-pack`, the held eighth-pack attempt whose
  chosen name is now spent on a different extraction (C8).
