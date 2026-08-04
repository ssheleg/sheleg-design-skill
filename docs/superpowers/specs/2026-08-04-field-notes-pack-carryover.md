# Carry-over ledger — `field-notes` style pack

> **Append-only.** Any stage may add a row; nobody edits or deletes one. Read in
> full by stage 10. The rule: *deferred out loud is forgotten* — if it isn't
> written here, it wasn't deferred, it was lost.

| # | Stage | What | Why it isn't done | REQ | Where it lives now |
|---|---|---|---|---|---|
| 1 | 0 Grill | Entry documentation audit — `docs/DOCMAP.md`, a decision register, `docs/OPEN_QUESTIONS.md` | Operator declined the one-time offer, 2026-08-04 | — | dropped (operator agreement) |
| 2 | 0 Grill | Code graph for this repo (`/graphify .`) | Recommendation only; never a gate. The CLI is installed, no graph built | — | backlog |
| 3 | 6 Tests | **The brief's `ungated` shared-state assumption is false.** At least three other task-pipeline runs are live in this same working copy (`feat/lecture-hall-pack`, `feat/audit-harvest-v1.5.0`, a design-sync-bridge run), all targeting `1.5.0`; HEAD was moved off `feat/field-notes-pack` at 19:07:50 by another run | discovered at stage 6, not assumable at stage 0 | — | **unresolved — operator decision** |
| 4 | 6 Tests | **`v1.4.0` was never tagged and never published.** Verified directly: latest tag is `v1.3.4` local and on origin; `npm view` returns `1.3.4`; `main` carries a `v1.4.0` commit and CHANGELOG entry for a release that does not exist | pre-existing, found by another run and confirmed by this one | REQ-008, REQ-011 | **unresolved — changes what 1.5.0 means** |
| 5 | 6 Tests | The concurrent `audit-harvest` run intends to grow the pack contract from **9 headings to 13** (`## Components`, `## Hero`, `## Responsive`, …) and is rewriting `STYLE_PACK_TEMPLATE.md` now. `field-notes.md` carries 10 and would fail the new validator | another run owns that contract change | REQ-001 | **unresolved — needs their final heading list** |
| 6 | 0 Grill | The stage-0 decision to skip the entry documentation audit rested on `docs/DOCMAP.md`, `docs/adr/` and a decision register being **absent**. Another run created all three at 19:11–19:12 | the premise expired mid-run | — | re-offer at the next run |

## Counts

```
carry-over: 6 open · unresolved: 3 · dropped with agreement: 1
```
