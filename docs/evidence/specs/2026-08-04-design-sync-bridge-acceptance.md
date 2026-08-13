# Acceptance — design-sync bridge + reference kits (v1.7.0)

Stage-10 close-out for [`…-brief.md`](./2026-08-04-design-sync-bridge-brief.md).
Every REQ accounted for with evidence from a check that has been seen failing.

**Released:** `v1.7.0` · tag pushed · GitHub release created · npm serves `1.7.0`
· local installs refreshed 1.6.0 → 1.7.0.
**Gates:** `validate.py` **786** · `validate_palette.py` **269** ·
`sloplint.py` **184** · CI green on `main` (`75f3748`), including all seven kit
builds from a derived matrix.

## Ladder walk — absences found before the table was written

The REQ table finds what was named and lost; an absence has only one side, so
each REQ was walked bottom-up through its rungs first. Four absences surfaced,
and each became work or a ledger row rather than a silence:

| Absence | Rung it was missing at | Outcome |
|---|---|---|
| `field-notes` had no kit | contract → change | **Found by check 3 at the merge, not by memory.** Built as the seventh kit; spec §6 updated. |
| The CI matrix named six packs by hand | change → executed test | The seventh kit was built, green and **invisible to CI**. Matrix now derived from `kits/`. |
| `SKILL.md` carries no version | surface → docs | Found by the T14 scenario agent against §7's own rule ("the pack's version is the design system's version") — there is nothing to compare against. Ledger row 21. |
| The live push has no executed test | executed test | `/design-sync` is `disable-model-invocation`; a human must run it. Ledger row 19, and REQ-009 closes `partial`, not `verified`. |

## REQ coverage

| ID | Status | Evidence |
|---|---|---|
| REQ-001 | **verified** | `DESIGN_SYNC_BRIDGE.md` ships and is linked; validator companion check, probed by deleting the file (`FAIL: …DESIGN_SYNC_BRIDGE.md: missing`) |
| REQ-002 | **verified** | `SKILL.md` §*Optional — Claude Design*; front-matter untouched, description canon still green in the suite |
| REQ-003 | **verified** | seven required headings enforced; probed by deleting one |
| REQ-004 | **verified** | seven kits, spine + signature; checks 3–5 probed by moving a kit, renaming `Chip`, and changing a prop type in one kit only |
| REQ-005 | **verified** | token block byte-identical per kit; probed by nudging one hex (`FAIL: … token block drifted …`) |
| REQ-006 | **verified** | no colour literal below the marker; probed with `color: #fff` (`FAIL: …:519: raw colour literal '#fff'`) |
| REQ-007 | **verified** | `--kit` materializes; CI diffs it against the source and against `styles/<pack>.md`; **and the materialized kit was built from the published registry** (`dist/index.js` 675 B, `dist/index.d.ts` 1038 B) |
| REQ-008 | **verified** | `files[]` carries `kits/`; no kit file in the bundle; both probed |
| REQ-009 | **partial** | the format is proven structurally and by build, **not by an upload**. `/design-sync` cannot be invoked by an agent. Ledger row 19; the exact human sequence is in the bridge doc and the final report |
| REQ-010 | **verified** | scenario **T14** run by a fresh agent holding only the installed bundle — passed every criterion, and found the version-marker absence above |
| REQ-011 | **verified** | README, CHANGELOG, CONTRIBUTING, cursor rule, `.cursor/` mirror; mirror equality is a suite check |
| REQ-012 | **verified** | `1.7.0` four-way synced; `npm view` returns `1.7.0`; `gh release view v1.7.0` exists; CI green |
| REQ-013 | **verified** | `ADR-0002`, `docs/DOCMAP.md`, and the 2026-07-19 spec annotated as partially superseded |
| REQ-014 | **verified** | the primary checkout received nothing from this run until one fast-forward; the other session's two uncommitted files survived it untouched |
| REQ-015 | **verified** | `conventions.md` per kit wired via `readmeHeader`; check 10 probed by deleting one |
| REQ-016 | **verified** | CI builds every kit and asserts non-empty `dist/index.js` **and** `.d.ts`, because `tsc` exits 0 having compiled nothing |

**15 verified · 1 partial · 0 dropped.** The partial is named, not rounded up.

## Axis rotation

The searching passes were: read the upstream contract (stage 1), verify each
kit against a written checklist (stage 5), plant defects against each new check
(stage 6), and walk the merge (stage 7). Findings came from **different** axes
each time rather than from re-reading the same surface — the merge axis produced
the two findings the earlier axes structurally could not (a pack with no kit, a
matrix with no seventh row). No pass was mostly finding what the previous pass
broke, so the axis was not exhausted and did not need forcing.

## Checks leaned on, and whether they have been watched failing

| Check | Watched saying no? |
|---|---|
| the eleven kit checks | **yes** — twelve planted defects, each with its own FAIL line recorded |
| the bridge-heading check | **yes** — deleted heading |
| the companion-doc check | **yes** — red before the doc existed, green after |
| `validate_palette.py`, `sloplint.py` | inherited from the concurrent run, which has its own self-tests wired (`--self-test` in CI) |
| the kit build | **yes** — a planted type error per kit, seven times |
| the derived CI matrix | **yes, in the useful direction** — it produced seven entries where the hand-written list produced six |
