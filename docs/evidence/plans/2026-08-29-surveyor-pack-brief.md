# Brief — the thirty-eighth pack, from visible.seranking.com

- **Run opened:** 2026-08-29, on the request *"https://visible.seranking.com/ Давай
  разбор дизайна еще вот этого лендинга сайта и упаковка его в спак"* — an address
  and nothing else. Answered per ADR-0001 before any file was written; the pack is
  named for its register (`surveyor`), with `contour`, `atlas`, `heatmap`/`benchmark`
  and `field-survey` weighed and rejected — the record goes into the ADR with this
  change.
- **Model:** Fable 5. **Baseline:** `main` == `origin/main` == `8236daa`, tree clean;
  registry and tags agree on **v1.53.0 shipped**. Target: **1.54.0**.
- **Companions:** sheleg-design (loaded), task-pipeline (this run order), agent-sync
  (lease before guarded files), graphify (`graphify-out/` at `8236daa`), wiki. The
  same resolutions as the `test-drive` run of 2026-08-27 hold: branch → PR → checks →
  tag; release durably authorized as Definition of Done; text-only design surface.

## Source ledger

Same sources as `2026-08-27-datafast-pack-brief.md`, re-verified this session: the 10
standing instructions (read in full this session, including the new 2026-08-27 entry),
board **30 open** (B-134 newest), verification **1 row at `never`** (REQ-10 → B-004),
CONTRIBUTING's 8-step procedure, the 13-heading template, ADR-0001..0003. New source:
the `test-drive` run's own retro entry — the blind defect-read runs BEFORE the tag.

## Measurement method (the pack's `Origin:` restates this)

Rendered at 1440×900, 768 and an emulated 390×844×2 through CDP; census of
`background-color` and `background-image` over every element, weighted by area, on an
8,176px page. Authored layer separated from vendor: WordPress with autoptimize — the
authored system is SE Ranking's own `se-uikit` stylesheet (the `--se-btn-*` ladder,
`--main-colors-*` palette, `--spacing-*` tokens, `--transition`) plus the front-page
CSS; the WP preset `:root` block is vendor noise and none of it paints. Verified
against the render: the field `#fff7f3`, the flat white/tinted cards, the teal action
and the pink family all paint; the hero's dashboard is a **webp portrait**
(1089×529), not an iframe and not DOM — zero canvases, zero large SVGs, exactly one
`@keyframes` (a pulse ring) and zero `prefers-reduced-motion` rules in ~68KB of CSS.
Ratios computed by importing this repository's own palette gate.

## REQ table (frozen)

| REQ | The requirement | Verified by |
|---|---|---|
| REQ-1 | A 38th pack from `https://visible.seranking.com/`, register-named per ADR-0001, method in `Origin:` | pack header; ADR entry; `tools/audit_packs.py` |
| REQ-2 | Thirteen headings, `Themes:`/`Rank:` derived | `test/validate.py` |
| REQ-3 | Token layer in the same change, provenance marked, gate-parseable | `test/validate_palette.py` |
| REQ-4 | The reference's failures recorded with numbers, never applied: white on `#0d9488` 3.74:1 at 16px/500; teal words 3.54:1 on the field; the pink FAQ marker 1.84:1 at 24px against a 3:1 large floor; `:focus-visible` carried by a fill step alone; 0 reduced-motion rules | pack Gotchas, recomputed by the gate |
| REQ-5 | Kit: six-name spine + signature components, token CSS byte-identical, `.design-sync/` pair | `validate.py`, `check_kit_vars.py` |
| REQ-6 | Routing: SKILL/index/cli/install/commands/mdc + mirrors; every counted claim moves 37→38 | `validate.py` |
| REQ-7 | Reciprocal forks against the confusable neighbours (`test-drive`, `showroom`) | `validate_fork_reciprocity()` |
| REQ-8 | Kit rendered at 1440/768/390, computed vs claimed, pre-tag | render log in acceptance |
| REQ-9 | Scenario T36 with negative branch, RUN blind before the tag | `test/scenarios.md` result line |
| REQ-10 | v1.54.0 released: five homes, PR+checks, tag, GitHub release, npm; verified from registry+tarball | `npm view`, tarball read |
| REQ-11 | Launcher pinned (three sync points) + local installs, shadow check empty | `npx sshlg-skills list`, the checks |
| REQ-12 | Docs/wiki/graph trio, artifacts read | diffs; `built_at_commit` == HEAD |

Carry-over ledger: opened empty.
