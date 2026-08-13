# Plan — ship the `field-notes` style pack (v1.5.0)

Design: [`2026-08-04-field-notes-pack-design.md`](../specs/2026-08-04-field-notes-pack-design.md).
Brief: [`2026-08-04-field-notes-pack-brief.md`](../specs/2026-08-04-field-notes-pack-brief.md).
Branch: `feat/field-notes-pack`. Base: `main` at `5e59263`.

**The shape of this change.** Adding a pack is a *registration* problem, not an
authoring problem: the two new files are the easy half, and the eleven places
that must learn about them are where every previous pack release nearly broke.
`test/validate.py` covers four of those places; the other four are checked by
hand here and by T13.

Ownership is strictly non-overlapping, so tasks 1–2 could run in parallel and
3–8 are a sequential registration sweep over distinct files.

---

## Task 1 — the token layer (owner: `styles/tokens/field-notes.css`)

**New file.** Light `:root` + `.dark`, every value from the design doc §2, with
the four corrections from §7 applied:

- reconcile the dark surfaces to the **forest** family (drop the navy terminal
  and the warm-brown `.dark` background in favour of one ramp);
- `--brand-on-dark: #cf7a52` as its own token, because the light brand fails on
  the hero (§8);
- app layer inherits the page neutrals; `--sidebar-ring` becomes the brand;
- `--chart-5` leaves the unrelated blue.

Also carries: the proportional radius ramp keyed to `--radius`, the two eases
with their two durations, the hero gradient's eight stops, the grain and
vignette values, the crop-mark geometry, and `color-scheme` set **per theme**
(the reference sets none — design doc §7).

**DoD:** file parses as CSS; every hex in it appears in the design doc or is
derived by a rule stated in a comment; both themes set `color-scheme`; a
`prefers-reduced-motion` block zeroes the durations.

## Task 2 — the pack (owner: `styles/field-notes.md`)

**New file.** All nine contract headings plus `## Motion flavor`, in the
template's order. Content from the design doc:

- **Register** — the dev-tool-on-paper claim, standalone posture, and the
  three-way disambiguation against `instrument-console` (the "does the product
  have a *dial* or a *source*?" test), `workbench` (app-chrome that disappears
  vs. a console with a voice), and `editorial-luxury`.
- **Palette** — link `tokens/field-notes.css`, the table with **measured
  ratios**, the provenance triad, the two fill-only colours named as such.
- **Type** — three families, the no-italic fact and what replaces it, the
  constant −0.025em tracking, the measured scale, the `.eyebrow` component.
- **Texture & surface** — ruled sections, the dawn hero, ring-as-elevation, the
  proportional radius ramp, containers, crop marks.
- **Motion tokens** — two eases/two jobs, the keyframe set, the rule that only
  `--verify` ever animates colour, reduced-motion.
- **Signature motifs** — the dawn, the numbered eyebrow, the provenance tag,
  the ruled sheet, crop marks, the glyph field.
- **Motion flavor** — how it rides the cinematic layer if asked to.
- **Micro-interactions** — the five button/chip variants, focus ring, tabs.
- **Bans** — from design §7 + §8.
- **Gotchas** — the five measured defects.

**DoD:** `python3 test/validate.py` finds all nine sections; every colour claim
carries a ratio; no value appears that is not in the design doc.

## Task 3 — route it (owner: `SKILL.md`)

Add the table row linking `styles/field-notes.md`; extend the "Style packs"
prose if it counts packs. Add the pointer from the AI-surfaces paragraph to the
new provenance section.

**DoD:** validator's "linked from the pack table" check passes.

## Task 4 — the AI pattern (owner: `AI_PRODUCT_PATTERNS.md`)

New section: **show provenance, not confidence.** Pack-agnostic — states the
three-state vocabulary, the tag component's shape, the rule that the label is
text a reader can act on rather than a number, and the token names any pack
must supply to implement it.

**DoD:** section exists, is linked from `SKILL.md`, names no `field-notes`-only
token as required.

## Task 5 — ship it (owners: `install.sh`, `bin/cli.js`)

`install.sh`: add `styles/field-notes.md` and `styles/tokens/field-notes.css`
to the `for f in …` list. `bin/cli.js`: add the pack to both help strings and
change **six → seven**.

**DoD:** validator's installer-sync and CLI-naming checks pass;
`node --check bin/cli.js`; `sh -n install.sh`.

## Task 6 — the human surfaces (owners: `README.md`, `cursor/rules/sheleg-design.mdc`)

README: pack table row, "six style packs" → seven wherever it appears. Cursor
rule: one clause describing the pack, no relative links (the .mdc travels
alone).

**DoD:** `grep -c field-notes` ≥ 1 in each; no "six style packs" string
survives; validator's .mdc link ban passes.

## Task 7 — the mirror + the version (owners: `.cursor/skills/`, the four manifests, `CHANGELOG.md`)

Copy the whole bundle to `.cursor/skills/sheleg-design/` (the validator diffs
it **both ways**). Bump `marketplace.json`, `plugin.json`, `package.json` to
`1.5.0` and write the CHANGELOG entry in the repo's prose-first voice.

**DoD:** validator's mirror and four-way version checks pass.

## Task 8 — the scenario (owner: `test/scenarios.md`)

**T13 — the dev-tool register, and the fork against `instrument-console`.**
Two prompts: one that should select `field-notes` (a product sold on
auditability), one that should still select `instrument-console` (a product
sold on live telemetry). Records the expected verdict and the values a correct
answer quotes.

**DoD:** scenario present with both branches and an explicit expected outcome.

---

## Gate order

1. `python3 test/validate.py` → `OK (n)`, **n > 272**
2. `node --check bin/cli.js`
3. `sh -n install.sh`
4. npx bundle diff — the CLI's file walk equals the bundle
5. POSIX bundle diff — `install.sh`'s list equals the bundle
6. the validator **probed with a planted defect** so its green means something

Then: merge to `main`, push, tag `v1.5.0`, watch CI, verify npm, refresh local
installs, sync the wiki, write the retro.
