# Acceptance — the thirty-eighth pack (`surveyor`), v1.54.0

Run of 2026-08-29, brief: `2026-08-29-surveyor-pack-brief.md`. Written at stage 10;
release evidence completed after the tag.

## The ladder walk, first

Walked bottom-up per REQ before the table was written. Absences found in-run and
closed before the tag:

- **The ADR entry was promised by the brief and unwritten at staging time** — caught
  by the pre-commit walk, not by a gate: no gate compares a brief's promises against
  the ADR register. Written before the commit.
- **The contour technique's first implementation broke the pack's own ban** — the
  render (CONTRIBUTING step 8) showed the pseudo-element hatch painting over cards
  and body text, full-surface, where the pack says corners-only-off-edge. Fixed as
  finite masked corner boxes under a stacking context; the fade moved into
  `--contour-fade` when the sloplint refused the mask's `#000` literals.
- **T36a's six findings** (see `test/scenarios.md` T36) — the blind reader's, all
  adjudicated pre-tag: the wrong-hex ratio stated twice, the pressed state specced
  past an exhausted ladder, the missing `font-variant-numeric`, the unreachable 1.4
  line-heights, the recycled contour range, the stale disabled-pair claim.

## Coverage table

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-1 register-named, method in Origin | green | pack header; ADR-0001 fifteenth application; `tools/audit_packs.py` → 38 packs, 25 render-read |
| REQ-2 thirteen headings, Themes/Rank derived | green | `validate.py` → OK (5370) |
| REQ-3 token layer, provenance, gate-parseable | green | `validate_palette.py` → OK (3243); the comment-brace parser break found and fixed in-run |
| REQ-4 reference failures recorded, never applied | green | Gotchas: CTA 3.74:1, links 3.54:1, the pink glyph 1.84:1 vs a 3:1 large floor, fill-only focus-visible, 0 reduce rules |
| REQ-5 kit: spine + signature, tokens byte-identical | green | `tsc` strict; `check_kit_vars.py` → OK (38 kits) |
| REQ-6 routing + mirrors + counts 37→38 | green | `validate.py`; the accent tally 35 of 38 recounted, theme split 12/17/9 |
| REQ-7 reciprocal forks | green | `test-drive.md` and `showroom.md` both link back; `validate_fork_reciprocity` green |
| REQ-8 kit rendered, computed vs claimed | green | CDP at 1440/768/390: 37/39 then all-green (two false negatives were mid-transition reads); the terrain overpaint caught and fixed |
| REQ-9 T36 with negative branch, RUN pre-tag | green | both branches PASSED 2026-08-29, blindness held; results and adjudications in `test/scenarios.md` |
| REQ-10 v1.54.0 released and verified | green | PR #8 checks green, squash-merged; tag `v1.54.0`; release run success; `npm view` → 1.54.0 latest; tarball carries the pack |
| REQ-11 launcher + local installs | green | sshlg-skills 1.4.4: pin/submodule/README moved together, annotated tag, npm published; local update run, shadow check clean of family names, no broken symlinks |
| REQ-12 docs/wiki/graph trio | green | this file + CHANGELOG; wiki v1.54.0 section; `built_at_commit` == post-merge HEAD |

## Ledgers

Carry-over: **empty**. One out-of-scope product left with a board id: **B-135**
(five `test-drive` findings from T36b — four reproduced, one refuted with a live
receipt). Board count at close: 31 open.

## Notes for the retro

Two divergences worth an entry: (1) the contour technique shipped its first draft
breaking the pack's own ban and only the render caught it — a pack decision (a
technique invented, not measured) is exactly where the author has no reference to
check against, so the render step is the only witness; (2) T36b produced the
scenario harness's first refutation-with-receipt — a finding disproved against the
live reference rather than the repo — which is instruction 8's "record refuted
claims" clause doing its work one layer out.
