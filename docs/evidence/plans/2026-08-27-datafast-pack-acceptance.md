# Acceptance — the thirty-seventh pack (`test-drive`), v1.53.0

Run of 2026-08-27, brief: `2026-08-27-datafast-pack-brief.md`. This file is written at
stage 10; every row names its evidence. Release evidence completed after the tag.

## The ladder walk, first

Walked bottom-up per REQ — decision → spec → contract → change → executed check —
before the table below was written. Absences found by the walk and closed in-run:

- The **dark twin's coral-word swap** was decided in the token layer and stated
  nowhere in the pack prose — found not by the ladder but by T35a's blind read, which
  is the sharper instrument; the ladder confirms both files now state it
  (`test-drive.md` Palette + Bans, `tokens/test-drive.css` dark block).
- The **`--accent-wash` derivation** claimed 8%-over-white and shipped a hex that did
  not compute; corrected to `#fdf3f0` with the ratio restated (`#c04a28` on `#fdf3f0`
  is 4.53:1).
- The **kit's hover border** consumed `--hairline-strong` where the pack now names
  `--hairline-hover`; aligned, `check_kit_vars` green after.
- No other absence: each REQ resolves to a spec section (the pack's own headings), a
  contract with failure behaviour (the gates), a change (commit on
  `feat/test-drive-pack-v1.53.0`) and an executed check (below).

## Coverage table

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-1 pack measured + register-named | green | `styles/test-drive.md` Origin + method; ADR-0001 fourteenth application; `tools/audit_packs.py` → `test-drive … address` |
| REQ-2 thirteen headings, Themes/Rank derived | green | `python3 test/validate.py` → OK (5219) |
| REQ-3 token layer, provenance, gate-parseable | green | `python3 test/validate_palette.py` → OK (3170); unguarded ratchet at its 27 pin |
| REQ-4 reference failures recorded, never applied | green | Gotchas: CTA 3.42:1, links 3.28:1, statuses 1.66–3.08:1, 53 keyframes vs 2 reduce rules, press 0.25s over the band; each recomputed by the gate |
| REQ-5 kit: spine + signature, tokens byte-identical | green | `tsc` strict build; `validate.py` kit parity; `tools/check_kit_vars.py` → OK (37 kits) |
| REQ-6 routing + mirrors | green | SKILL/index/cli/install/commands/mdc all name the pack; `validate.py` mirror check green |
| REQ-7 pairwise forks reciprocal | green | forks in `datasheet.md`, `showroom.md`, `scoreboard.md`; `validate_fork_reciprocity` inside the green validate run |
| REQ-8 kit rendered, computed vs claimed | green | 1440/768/390 + dark, via CDP on `render.html`; three defects caught and fixed pre-tag (nav 66→65 box-sizing, 428px overflow → link-row collapse, touch floor added); 29/30 then all-green assertion runs |
| REQ-9 scenario with negative branch, run | green | T35a and T35b PASSED 2026-08-27, fresh contexts, blindness held; results in `test/scenarios.md` with the four fixed findings and B-134 |
| REQ-10 v1.53.0 released and verified | green | PR #6 merged with checks green; tag `v1.53.0`; `npm view sheleg-design-skill version` → 1.53.0; tarball read: `styles/test-drive.md`, token layer and kit present (38 files); GitHub release cut by the workflow |
| REQ-11 launcher coordinated + local installs | green | sshlg-skills v1.3.7: pin 1.53.0, submodule at v1.53.0, README row — validator green, tag pushed, `npx sshlg-skills list` shows 1.53.0; local `sshlg-skills update` run, shadow check empty |
| REQ-12 docs / wiki / graph trio | green | this file + CHANGELOG; wiki `sheleg-design-skill.md` v1.53.0 section; `graphify update .` with `built_at_commit` read equal to HEAD after merge |

## Ledgers

Carry-over: **empty** — nothing was deferred in-run; the one out-of-scope product
(nine `datasheet` findings from T35b) left with a board id, **B-134**, priority
medium. Board count at close: 30 open (29 at stage 0 + B-134).

## Notes for the retro

The run diverged in one place worth an entry: the blind scenario's defect-read out-hit
the author's own ladder — four real defects in a pack that had just passed three green
gates and a render pass, one of them (the dark coral-word swap stated only in the CSS)
a contract split across two files that no gate compares for *prose* agreement. That is
the same class as B-122 (nothing checks that a pack's two files agree about what a
token drives), one level up: the files agreed about the tokens and disagreed about the
rule. Recorded in the retro Log by the close-out.
