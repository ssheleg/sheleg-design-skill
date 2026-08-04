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

## Counts

`open: 8 · unresolved: 0 · dropped: 0` — printed beside every gate verdict from here on.
