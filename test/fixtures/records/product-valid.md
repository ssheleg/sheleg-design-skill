---
surface: usage-table
surface_class: product
---

# Director record — usage-table

## Brief

Surface: product UI — the usage table in the billing settings
Job: see which project spent the most this month and open it
Constraint: the workbench pack and the existing DataTable component
Falsifier: the most expensive project is not visible without sorting at 1280×800

## Mode

update — entered at tokens, then visual-qa on the billing screens

## References

none found
Searched: Refero "usage table billing", Lazyweb "usage breakdown" — the sweep returned settings tables with no per-project spend.

## Markers

npx sheleg-design-skill --lint src/billing @ a91c0de — 0 S1, 0 S2, 0 S3, 0 waived

## ADA

n/a — product surface; the product profile's G items run in the pipeline's visual gate.

## Open

Whether the table defaults to this month or the billing period.
