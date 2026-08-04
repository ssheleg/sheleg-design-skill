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

## Counts

`open: 11 · unresolved: 0 · dropped: 0` (row 9 resolved same-stage) — printed beside every gate verdict from here on.
