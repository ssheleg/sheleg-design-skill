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
