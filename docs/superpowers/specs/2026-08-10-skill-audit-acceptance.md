# Acceptance — 2026-08-10 skill audit (v1.10.0)

Closed at `e92f2c1`, tagged `v1.10.0`, released and published.
Brief: [`2026-08-10-skill-audit-brief.md`](./2026-08-10-skill-audit-brief.md).
Report: [`../../audit/2026-08-10-skill-audit.md`](../../audit/2026-08-10-skill-audit.md).

## Ladder walk

Each REQ walked bottom-up — decision → spec → contract and its failure behaviour
→ task → change → executed test → surface/docs — checking the seam at each step.
Findings are ordered by seam, and **every absence became a REQ row before this
table was written**. Three did:

| Found on the ladder | Seam | Became |
|---|---|---|
| The `Contract: core` note I wrote cited `docs/superpowers/backlog.md`, a repo-only path — the bundle ships no `docs/` | change → surface | fixed in `e92f2c1`; the note is self-contained |
| `tokens/atrium.css` still said "three shadows" after the pack was corrected to four | change → change | fixed; kit prefix regenerated |
| The status sentence left three packs unaccounted for and licensed `var(--warning)` in `atrium` | spec → contract | fixed; the full map is in `SKILL.md` |

## Coverage

Carry-over counts printed beside every verdict, so "green" does not read as
"verified": **1 REQ at `never`** (REQ-10), **6 board rows open** (B-001…B-006).

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-01 counted claims | **green** · 0 carried | `validate_counted_claims()`; planted `six locked style packs` caught |
| REQ-02 status vocabulary | **green** · 0 | full map in `SKILL.md`; `validate_core_vocabulary()` |
| REQ-03 dataviz handoff | **green** · 0 | rewritten by role; T20c verified every token against the CSS and refused to invent |
| REQ-04 doctrine reach | **green** · 0 | README table, CLI help + banner, slash command, `.mdc` rule |
| REQ-05 contract terminology | **green** · 0 | `validate_contract_terminology()`; planted stale spelling caught |
| REQ-06 bridge no longer teaches nine | **green** · 0 | edit + the same check |
| REQ-07 command routes to twelve | **green** · 0 | `validate_pack_enumerations()` |
| REQ-08 manifests current | **green** · 0 | same check |
| REQ-09 contract declared per pack | **green** · 0 | `validate_contract_declaration()`, line-anchored after the substring bug was watched failing |
| REQ-10 backfill three packs | **carried** · → B-004 | not attempted rather than guessed: it needs live computed styles. The misleading half is closed |
| REQ-11 reference paths | **green** · 0 | 7 headers renamed, callout at the top; `grep '^\*\*File:\*\*'` = 0 |
| REQ-12 README Development true | **green** · 0 | rewritten claim-by-claim; the one unbackable claim now states its limit |
| REQ-13 checks watched failing | **green** · 0 | 6 + 5 + 5 planted defects; plus live catches on `atrium` and 13 ratios |
| REQ-14 CI parity | **green** · 0 | `npm test`, `validate.yml`, `release.yml` all run four gates + three self-tests |
| REQ-15 the report | **green** · 0 | `docs/audit/2026-08-10-skill-audit.md` |
| REQ-16 routing survives | **green** · 0 | T20a/b/c, three fresh contexts, all green |
| REQ-17 released | **green** · 0 | npm serves `1.10.0`; tag on origin; release not a draft; **tarball unpacked and checked** (387 files, 12 packs, 12 kits, 13 `Contract:` lines, corrected ratios present) |
| REQ-18 docs/wiki/graph | **green** · 0 | `built_at_commit` `b426ccc` → `e92f2c1` = HEAD, 1335 nodes. The doc half still needs an LLM key — same carry-over as the previous run |
| REQ-19 board + ledger | **green** · 0 | both files, 6 open rows, 1 `never` |

## Gates

| Gate | Before | After |
|---|---|---|
| `validate.py` | 1270 | **1366** |
| `validate_palette.py` | 412 | **469** |
| `sloplint.py` | 224 | **320** |

Floors enforced from `test/floors.json`. All three self-tests green. Both
installers verified against the source with `diff -r`; a kit whose token layer
changed was built.

## What a re-run should look at first

The three defect *classes* this run turned into scripts were each recorded in an
earlier retrospective and still shipped. The pattern to check next time is not a
file — it is whether the last run's findings were swept across siblings, or fixed
only where they surfaced.
