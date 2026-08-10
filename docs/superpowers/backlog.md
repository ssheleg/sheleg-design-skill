# Board — sheleg-design-skill

The work-list between pipeline runs. Stage 0 reads it and quotes the open count;
stage 10 files every ledger row still `open` or `unresolved` as a row here, with
a board id.

Seeded 2026-08-10 by the `2026-08-10-skill-audit` run. Before that date this file
did not exist, which is why five prior runs' deferrals were only ever visible
inside their own carry-over ledgers.

**Priority** is computed, not asserted: `blast radius × age ÷ cost`. A row that
misleads an agent building a page outranks a row that misleads a human reading
the README.

| id | Row | Source | Priority | Status |
|---|---|---|---|---|
| B-001 | Widen `instrument-console`, `workbench`, `briefing-room` to the four sections (`Components`, `Hero`, `Responsive`, `Signature element`). Blocked on an addressable reference: their `Origin:` lines name a product, not an address, so the sections cannot be sourced without inventing them. Resolve by either (a) obtaining a public reference for each, or (b) re-deriving each pack from a live site and re-issuing it. | `2026-08-10-skill-audit` C-1 | high | open |
| B-002 | Retire or replace the three packs whose `Origin:` is not addressable, or record an explicit grandfather clause in an ADR. Standing instruction 5 says "no reference, no pack"; three shipped packs predate it and nothing in the library says so to a reader. | `2026-08-10-skill-audit` | medium | open |
| B-003 | Prose contrast claims and worst-stop tables (`cyclorama`) sit outside `validate_stated_ratios`, which only checks a claim whose base the document declares. Fix by making those tables declare a base, then widening the check. | `2026-08-10-skill-audit` | medium | open |
| B-004 | Widen `atrium`, `orchard`, `editorial-luxury` to the four sections. Authorised by the operator; their references are addressable (functionhealth.com, gutgutgoose.com, prowl.chat), so this is a measurement pass against live computed styles rather than an editing pass. The misleading half is already closed — each declares `Contract: core` and says what it leaves undecided. | `2026-08-10-skill-audit` | high | open |
| B-005 | 13 of 19 scenarios in `test/scenarios.md` carry no recorded result, and 5 of the 6 that do carry a date with no commit. Re-run the unrecorded ones in fresh contexts and stamp each with a commit. | `2026-08-10-skill-audit` | medium | open |
| B-006 | The skill description has 14 characters of headroom and no trigger for presentation decks, the motion doctrine, design-sync, or any pack name. Widening it changes discovery, so it needs the full T1 trigger set re-run in fresh contexts. | `2026-08-10-skill-audit` | high | open |
