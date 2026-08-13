# Acceptance — `datasheet`, the fourteenth style pack (v1.19.0)

Run `2026-08-12-datasheet-pack`. Released as `v1.19.0` at `f4f25ce`.

## The ladder walk, first

Each REQ walked bottom-up — decision → spec → contract and its failure behaviour →
task → change → executed test → surface. Three absences were found by the walk itself
and each became work rather than a note:

1. **The token layer stated a ratio no one had computed.** `--ink-faint` on the alarm
   field was written as 2.15:1 from intuition; the palette gate named the two numbers
   it accepts and neither was that. It computes **3.32:1**. Found by the gate, not by
   the walk — recorded here because it is the clearest case in this run of a claim that
   looked measured and was not.
2. **The alarm status inks were checked against the field and never against the tint
   the components pair them with.** Eleven defects came back from T24 and this was the
   root of the worst one. Fixed; the honest limit is written into the retrospective —
   no gate here pairs a colour with a surface a prose rule chooses.
3. **A new check was written and never called.** `validate_contract_split()` was
   defined, and the suite ran without it. Wired, then watched saying no.

## The table

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-01 | ✅ | thirteen headings + `Contract: widened`; `Origin:` names `fingerprint.com`, the date and the stylesheet hash |
| REQ-02 | ✅ | MEASURED / SELECTED at every declaration; the alarm group was found unmarked by a T24 agent (54 of 118) and completed |
| REQ-03 | ✅ | palette gate 603 → **716** checks, green in both themes |
| REQ-04 | ✅ | every stated ratio recomputed from the tokens; the gate caught two of this run's own wrong claims |
| REQ-05 | ✅ | six corrections in Gotchas with numbers: 3.32, 2.51, two oranges, reduced motion, the ring on five surfaces, the alarm tint at 4.44 |
| REQ-06 | ✅ | `validate_kits()` green; `tsc` emitted 11 components with declarations; `kits (datasheet)` green in CI |
| REQ-07 | ✅ | five reciprocal forks, enforced by `validate_fork_reciprocity()` |
| REQ-08 | ✅ | thirteen → fourteen everywhere, and the check now reads the manifests that had gone stale |
| REQ-09 | ✅ | all seven enumeration sites name the pack |
| REQ-10 | ✅ | floors 1507/603/352 → **1647/716/366**, reason in the same commit |
| REQ-11 | ✅ | T24 written **and run**, both branches green, 22 findings, 11 fixed, 1 refuted, 4 filed |
| REQ-12 | ✅ | ADR-0001 records the eighth application, and that the brand name was declined out loud before any file was written |
| REQ-13 | ✅ | five-way version sync at 1.19.0, enforced by the gate |
| REQ-14 | ✅ | CI read before the tag; release + publish green; tarball unpacked and read; both local channels read from disk |
| REQ-15 | ✅ | five stamps backfilled with what evidence supports and *unrecorded* where it does not; this run stamped; all ten instructions walked, instruction 1 widened |
| REQ-16 | ✅ (restated) | graph `built_at_commit` `9312a85` against HEAD; B-009 holds the two candidate rebuilds and this run does not choose between them |
| REQ-17 | ✅ | `origin/main` at `f4f25ce`, 0 ahead; the three inherited commits pushed, which half-closes B-014 |

## Counts beside the verdict, so green does not read as verified

- **Gates:** 1647 / 716 / 366, eleven self-test plants caught, two of them new.
- **Board:** 20 rows, **17 open**. Seven were filed by this run (B-014…B-020); B-014 is
  half-closed by its own push.
- **Verification ledger:** 31 rows, **1 at `never`** (REQ-10, carried to B-004).
- **Scenarios:** 24, every one carrying a verdict and a date.

## What this run did not do

- It did not fix `field-notes`' provenance colours (B-017), though it reproduced both
  collisions — 3.21 and 2.84 against a disclosed hard floor of 10 — and proved the gate
  structurally cannot see either pair. Changing a shipped pack's hexes is a visual
  change to a released design system and is not a quiet edit.
- It did not rebuild the code graph (B-009). The shrink guard was right in 1.11.0 and is
  still right; choosing between a full rebuild and a stated dedup model is the work, and
  it is not this run's.
- It did not run a full `/wiki-update` pass. The project page's false claims were
  corrected against the artifact — version, both counts, and a dated section for this
  release — and the concept pages were left alone.
