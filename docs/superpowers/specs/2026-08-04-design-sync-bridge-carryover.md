# Carry-over ledger — design-sync bridge + React reference kits

> **Append-only.** Any stage may add a row; nobody edits or deletes one. Read in full
> by stage 10. **Deferred out loud is forgotten** — if it isn't here, it wasn't
> deferred, it was lost.

| # | Stage | What | Why it isn't done | REQ | Where it lives now |
|---|---|---|---|---|---|
| 1 | 0 Grill | `v1.4.0` will never be tagged or released; its CHANGELOG entry describes a version that only ever existed in the manifests | operator's call — everything folds into 1.6.0 | REQ-012 | accepted, D8 |
| 2 | 0 Grill | The five non-workbench kits are not pushed to claude.ai/design this run | only one live proof was authorized; the capability ships regardless | REQ-009 | backlog — run `--kit <pack>` + `/design-sync` any time |
| 3 | 0 Grill | The code graph is not built for this repo | `graphify` is installed but `graphify-out/` does not exist; recommended, never a gate | — | backlog — `/graphify .` |
| 4 | 0 Grill | The documentation entry audit (`references/setup.md`, seven passes) was not run | the minimal doc regime was chosen instead; disproportionate for ~10 docs | — | offer stands for a future run |
| 5 | 0 Grill | Branches `feat/field-notes-pack`, `feat/audit-harvest-v1.5.0`, `feat/lecture-hall-pack` left untouched | not created by this run; another live session owns them | — | owned by the concurrent run |
| 6 | 0 Grill | This run's 71-line first-draft brief is committed inside `d042b41`, a commit about the field-notes pack, on another run's branch | swept up by a `git add -A` in the shared checkout before isolation was in place | — | harmless duplicate — the authoritative brief is on `feat/design-sync-bridge`; flag at merge so the stale copy is not mistaken for the brief |
| 7 | 0 Grill | This repo is `ungated`: no lease mechanism, no id reservation, despite agent-sync v1.4.3 being installed on the machine | out of scope for this run — it is a repo-wide policy change, not part of the design-sync bridge | — | **backlog — recommended**: `/agent-sync` init for this repo, or two agents keep colliding |
| 8 | 0 Grill | ADR numbering across concurrent runs is unarbitrated; this run took 0002 by inspection, not by reservation | same root cause as row 7 | REQ-013 | re-checked at stage 9 (A7) |

| 9 | 1 Docs | D5 ("plain React, no build step, no dependencies") was refuted by the converter's own requirements | the guess was cheap and wrong; corrected as D11 before any code was written, which is where a stage-1 gate is supposed to catch it | REQ-004, REQ-007 | resolved — D11 |
| 10 | 1 Docs | The `/design-sync` flow's own verification needs Playwright + chromium (~200 MB) and the skill asks before installing | not this run's decision to make silently | REQ-009 | asked at stage 6, before the live push |

| 11 | 2 Brainstorm | Five kits (all but `workbench`) ship the converter's floor card instead of authored previews | operator's scope call at the stage-2 gate; upstream supports authoring incrementally on any later re-sync with grades carrying forward. **Not a narrowing of REQ-004** — every kit still ships every component; this scopes verification depth only | REQ-009 | backlog — author `previews/` per pack on a later re-sync |

| 12 | 3 Spec | `test/validate.py`'s link check does not exempt fenced code blocks, so a relative link inside a documentation example is checked against the containing file's directory | found by the check firing on this run's own spec; the spec routes around it with a placeholder. Changing the checker to skip fences is a separate change with its own blast radius — and the strict version has been correct every other time | — | backlog — decide deliberately, don't loosen it in passing |

| 13 | 5 Build | **Three naming conventions for one role across six shipped packs**: `--accent-ink` (`atrium`, `briefing-room`), `--cta-ink` / `--on-primary` / `--on-ink` (`orchard`), and nothing at all (`workbench`, `editorial-luxury`, `instrument-console` — fixed additively this run) | unifying them means **renaming shipped tokens in `orchard`**, which breaks every consumer who copied that layer. The wiki already records how a token remap goes wrong ("sweep hardcoded literals after"). Too big to fold silently into a design-sync run | — | **backlog — worth an ADR**: unify on `--accent-ink` with a deprecation window, or accept per-pack names and document the map |
| 14 | 5 Build | `kits/*/dist/` is untracked and not gitignored — build output would be committed | surfaced by the T2 implementer; the fix belongs beside `package.json` `files[]` | REQ-008 | T8 |
| 15 | 5 Build | `workbench`'s pack text names a destructive button; the locked spine has no room for it | resolved same-stage as a signature component with a real two-click confirm, not deferred | REQ-004 | resolved — spec §6 |

| 16 | 5 Build | No `--danger-ink` / `--ok-ink` / `--warn-ink` — the semantic colours have the same "text on the fill" gap `--accent-ink` just closed | **no active defect**: the destructive button fills `--danger-weak` and keeps its `--danger` label, so nothing is currently unreadable. Adding three tokens × six packs without a forcing case is scope growth, and it is the *same question* as row 13 | — | backlog — decide with row 13, one ADR for the whole ink family |
| 17 | 5 Build | `kits/*/dist/` and `kits/*/package-lock.json` gitignored at T2 rather than T8 as planned | committing 104 KB of build output was a defect I would have created in this commit, not one to schedule | REQ-008 | resolved — `.gitignore` |

| 18 | 5 Build | The scenario is **T13**, not T12 — `T12` is already the orchard pack on `main`. Same collision class as the ADR number (A7): the concurrent run is adding packs and will take scenario numbers too | caught by reading `test/scenarios.md` instead of trusting the plan's number | REQ-010 | re-checked against `main` before the merge, with the ADR number |

## Counts

`open: 15 · unresolved: 0 · dropped: 0` (rows 9, 15 and 17 resolved same-stage) — printed beside every gate verdict from here on.
