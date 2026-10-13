# FW05 — source-derived design facts, 2026-10-13

Owner: sheleg-design-skill; branch `fix/fw05-derived-design-facts`; canonical
base `f5244f6422c8ed18f72f61eb7afaef44a42276c0`. Entry: [HANDOFF](../../HANDOFF.md).
This is implementation evidence, not a rendered design or native-host acceptance.

## Requirement mapping

| Row | Recovered state and implemented change | Executable proof |
|---|---|---|
| B-055 | Baseline printed 23 unbound traversal hits, not unique figures. Separate pairs in pigeonhole, paperclip, outrank and test-drive token comment; preserve numeric qualifiers. The old maquette example was already paired. | `validate_disclosure_coverage` in `test/validate_palette.py` requires zero unbound; wrong-value and old-shape controls in `test/audit_regressions/fw05_design_facts.py` |
| B-056 | Cyclorama's 14.8 now says full colour; notation's two sentences place each CVD qualifier beside its figure. `_figures` remains strict; unrelated unqualified numbers stay outside. | Same regression file, qualifier-positive and unrelated-number-negative controls; public palette arithmetic |
| B-113 | Current source has 12 full twins; eight now have explicit derived tables: almanac, daylight, notation, outrank, proscenium, router, test-drive, vitrine. Four pre-existing tables (workbench, manpage, ledger, field-notes) retain populated-table checks only. | `dark_palette_table`, `dark_palette_problems`, `validate_dark_palette`; `scripts/sync-dark-palettes.py --check`; missing/stale/removed-marker controls |
| B-126 | `MOTION_DOCTRINE.md` section 9 and `cursor/rules/sheleg-design.mdc` document the existing keep-duration-with-reason contract, with component-level stopping required. | Existing `validate_every_duration_answers_reduce` plus structural and slop gates; doctrine diff. No new animation behavior |
| B-128 | Prism motion guidance now specifies CSS/SVG still, no scheduled frame loop under calm/coarse/no-WebGL, cancellation when preference changes, and visible text/control fallback. | `styles/prism.md` Motion flavor; canonical/mirror consistency. Implementation rendering remains unobserved |
| B-146 | Already linked to the sole token-tier model in super-ux. No second model created. | [super-ux 18d8ebe source](https://github.com/ssheleg/super-ux/blob/18d8ebefca9b9facc9579d65fe8ef4009bd78b82/plugins/super-ux/skills/ux-flows/references/figma-structure.md#components-variants-tokens-bp-094bp-098); same text read from local `v0.59.2` tag |

All style paths above are beneath `plugins/sheleg-design/skills/sheleg-design/`.
The `.cursor/skills/sheleg-design` mirror is copied from canonical source.
The test-drive kit token comment was refreshed with `scripts/sync-kit-tokens.py`;
its component suffix remained byte-identical. No colour token value changed.

## Red and green observations

Baseline `npm test`: exit 0, structural 6641, palette 3409, slop 938 checks;
installer, linter, director-record, render-eval sample, kit lint, self-tests and
audit regressions also passed. The render-eval sample is synthetic evidence.

Before documentation edits, the new palette guard failed on eight absent dark
tables and the zero-unbound condition: nine intended failures, exit 1. After
rewrites, `python3 test/validate_palette.py` exits 0 with 3461 checks and zero
unbound traversal hits. The palette ratchet is raised to that observed count.

Focused checks, all exit 0:

- `python3 test/audit_regressions/fw05_design_facts.py`: 49 controls at this stage.
- `python3 test/validate_palette.py --self-test`: all planted checks caught,
  including missing/stale/broken/removed dark-table markers and unbound pairs.
- `python3 scripts/sync-dark-palettes.py --check`: eight marked tables, zero drift.
- `python3 test/validate.py`: 6641 checks before receipt/board additions.

Actual-file plants were performed serially in this isolated worktree and exact
original bytes restored in `finally`: remove daylight's dark table, replace its
source-derived value, add a third token to pigeonhole's pair, and replace its
stated 5.0 with 99.0. Every public palette run exited 1 and named respectively
`no explicit dark-value table`, `table differs from shipped token graph`,
`unbound token pairs`, and `the disclosure for`. The restored tree then passed
3461 checks. No other worktree or installed skill was mutated.

Final `npm test`: exit 0, structural 6650, palette 3461, slop 938;
all installer/lint/record/render-sample/kit gates, negative self-tests and 31 audit
files passed. After that run, generator controls were made durable in the same
focused regression file; its rerun passed 56 controls. Generator checks cover
idempotence, stale-value repair, malformed/reversed-marker refusal and unknown
arguments. A separate `--write` on the synchronized real tree reported zero
changed tables. Workflow job bodies compare byte-identical to the base.

Independent bounded verdict: PASS at `6a24c2390d66a70eb17c034719d1681bff624ec8`; see the review below. No release/version bump/native install is claimed.

## Guard boundary and maintenance

The new table generator shares the existing token parser with the palette gate;
it resolves CSS aliases/inheritance into source literals. It does not simulate
cascade in a browser, certify all CSS syntax, or prove accessibility. Generated
rows cover core surface/ink/accent/status roles, not every decorative colour.
The four legacy tables are presence-only exceptions by exact pack name. Newly
derived tables cannot drop their markers to enter that exception set.

`python3 scripts/sync-dark-palettes.py --check` is read-only. Explicit `--write`
refreshes marked tables and mirrors after all sources are checked; it refuses
malformed/reversed markers. It does not create missing sections. The palette gate
owns their required presence. Audit regressions run via `npm run test:audit` in
both the owner package and `.github/workflows/validate.yml`.

## Integration policy

The validation workflow keeps the existing jobs unchanged and runs nightly at
23:00 Europe/Warsaw. Deliberate `pull_request: types: [ready_for_review]` promotion
is the explicit frozen-candidate exception; no opened/synchronize/push trigger.
Manual dispatch remains diagnostic and cannot satisfy PR ruleset admission:
[GitHub check eligibility](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks#checks-from-some-workflow-jobs-are-not-evaluated).

Next: independent review, freeze exact head, promote the draft once, observe all
required checks at that head, integrate normally. Separate version selection,
publication, parent pins and installed/native acceptance. Open live observations
such as B-145 remain on the owner board.

## Independent review — 2026-10-13

Reviewer: Codex `/root/fresh_research`, separate from the implementation author.
Reviewed frozen source `6a24c2390d66a70eb17c034719d1681bff624ec8` against
`f5244f6422c8ed18f72f61eb7afaef44a42276c0`. Bounded PASS: no remaining finding in
the changed source-derived table, disclosure, generator or documented motion scope.

Reviewer-executed checks:

- `python3 -B test/audit_regressions/fw05_design_facts.py`: exit 0, 56 controls.
- `python3 -B scripts/sync-dark-palettes.py --check`: exit 0, eight marked tables,
  zero drift.
- Nine separately constructed pure controls passed: valid derived table,
  removed-marker and stale-value refusal, duplicate-marker refusal, generator
  idempotence and stale repair, plus three malformed-marker refusals.
- An independent Git-source comparison removed CSS comments and whitespace and
  compared each changed CSS file with the base: all three retained executable
  CSS text. All 14 changed canonical skill files matched their Cursor mirrors
  byte for byte. Workflow `jobs:` content matched the base byte for byte.

The earlier marker-removal escape is closed by the exact four-name legacy
allowlist; an arbitrary newly generated table cannot become a presence-only
exception by deleting its markers. The generator checks all marked sources before
writing and defaults to read-only operation. This review does not certify browser
cascade, rendered appearance, runtime motion stopping, provider/native discovery,
release or installation. The owner's full-suite observation above is separate
from these independently executed focused checks.
