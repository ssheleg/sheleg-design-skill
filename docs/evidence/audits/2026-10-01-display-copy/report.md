# DC-02 — visible copy at the visual-review seam

Scope: sheleg-design-skill only, base
`8ed21839252f1f032b44adaf9f85cd9d694f77ff` (1.61.1), branch
`codex/display-copy-guard-2026-10-01`. Companion parser work belongs to super-ux.
The assigned packet is the umbrella's
[DC-02](https://github.com/ssheleg/sshlg-skills/blob/codex/display-copy-guard-2026-10-01/docs/evidence/audits/2026-10-01-display-copy/design.md).

## Before the fix

| Verdict | Finding and evidence |
|---|---|
| PASS | The coordinator's pre-edit house audit accepted all 18 mechanical checks; body 4749/4750 tokens. This did not test instruction usefulness. |
| GAP | At the base commit, `plugins/sheleg-design/skills/sheleg-design/VISUAL_REVIEW.md` checked capture identity but did not name displayed-copy roles or copywriting policy. `SKILL.md`'s visual-review load trigger named screenshots only. |
| GAP | `kits/deskmate/src/Empty.md:14` supplied a title with a terminal period, adjacent to a legitimate sentence in `detail`. Its component receives caller-provided text and must not strip punctuation at runtime. |
| NOT_RUN | Before/after model outcome evaluation was not executed. Contract assertions do not show that a model obeys the review or that visual quality improved. |

## Change

One existing review home now covers eyebrows, headings, line-break fragments,
captions and labels. It names project policy, copywriting/AT-07 ownership,
ordinary prose and meaningful punctuation exceptions. The reviewer records
selector, visible text, role, viewport, revision and source-role coverage.
Source/generated-copy changes must survive regeneration and then be recaptured.
A linter's exit 0 is not evidence for sources or roles it did not inspect.

`SKILL.md` routes to that review before accepting rendered copy; the director
links to the same section. Its body is smaller, not enlarged beyond the budget.
The empty-state example loses its title period and retains sentence punctuation
in the detail. No component runtime, copy parser or unrelated style pack changes.

A bounded source search inspected headings in kit TSX and quoted title/headline/
label examples in kit and bundle Markdown. The confirmed title defect above was
corrected. Caller-supplied headings were not reclassified as fixed copy; this
search does not claim full visual or language coverage for every kit.

## Receipts

- `python3 test/audit_regressions/dc-02.py`: the pre-change bundle failed the
  missing-review, trigger and director probes (2 failures, 1 missing-section
  error). The added empty-state probe separately returned exit 1 before its fix.
  Final run: 5 tests, including 6 missing-boundary mutation subcases, exit 0.
- `python3 .../make-skill/scripts/audit_skill.py plugins/sheleg-design/skills/sheleg-design --house --json`:
  18 PASS, body 349 lines / 4743 tokens, description 960/970 characters.
  Tool path used: `/Users/sshlg/.agents/skills/make-skill/scripts/audit_skill.py`.
- `claude plugin validate . --strict` and
  `claude plugin validate plugins/sheleg-design --strict`: both exit 0.
- `npm pack --json --pack-destination /tmp`: packed skill entry, review,
  director and empty-state example bytes equal the source; the package includes the existing review home.
- `npm run gen-contents`: generated the review's contents and mirror; changed
  entry/director mirror files were copied byte-for-byte and checked by the gate.
- `npm view sheleg-design-skill version` before bump: `1.61.1`; candidate `1.61.2`.

`npm test`: exit 0, including consistency (5776 checks), palette (3409),
slop (818), installer (13 cases), the normal mutation selftests and all audit
regression suites. After the handoff and ledger additions, `python3 test/validate.py`
returned exit 0 / 5778 checks; `git diff --check` returned exit 0. These checks assert
instruction availability, boundaries and package integrity. They do not execute
a user interface or constitute a model behavior evaluation.

## Handoff

The coordinator reviews and owns PR/CI integration, annotated tag, registry
publication, umbrella pin update and machine refresh. None of those is implied
by the patch version in these files. Current source and mirror are the review
inputs; the installed copy is a separate release step.
