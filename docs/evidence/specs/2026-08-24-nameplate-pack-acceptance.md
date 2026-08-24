# Acceptance — `nameplate`, the thirtieth style pack (v1.45.0)

Run `2026-08-24-nameplate-pack`, authored on `main` under agent-sync lease `SG-NAMEPLATE`
(run `r-a3532a2fe`). The opening request was an address and a brief to add it to the
references and build a pack from it — the sixth run of that shape, and `ADR-0001` was
pointed at before any file was written.

## The table

| REQ | Verdict | Evidence |
|---|---|---|
| REQ-01 — thirteen headings + a `Contract:` line | ✅ | `validate_contract_declaration()` 65 → 67, green; `Contract: widened` |
| REQ-02 — `Origin:` is addressable and re-readable | ✅ | `https://www.brandpush.co`, the sitemap count (20 URLs, 12 pages), the authored-CSS path and byte count, the three CDP viewports, and the read date |
| REQ-03 — vendor CSS excluded from every count | ✅ | counts are over the 11 files under `/assets/css/` only; Bootstrap 4.6.2, the *ave* theme, the *frest* admin theme and three Font Awesome versions were named and excluded in the pack's Gotchas |
| REQ-04 — values read from the render, not the declaration | ✅ | the reference declares `--primary: #84B761` three times and paints none of it; its real action is a gradient whose element has a transparent `background-color`. Both caught by CDP, both recorded in Gotchas |
| REQ-05 — every value measured, selected or derived, marked at the declaration | ✅ | every token in `tokens/nameplate.css` carries one of the three words and its count or ratio |
| REQ-06 — every stated ratio recomputed | ✅ | `validate_palette.py` 1912 → **1975**, green; it caught two of my own numbers (`--link` phrasing, `--link-hover` stated 6.29 against a computed 6.65) and both were corrected |
| REQ-07 — status separates under all three dichromacies | ✅ | the gate rejected the first set outright (`--accent`/`--info` 7.5 apart against a hard floor of 10.0); the second set clears all **fifteen** pairs at ≥15 full-colour and ≥8 under protanopia, deuteranopia and tritanopia |
| REQ-08 — a kit whose spine matches the exemplar | ✅ | six spine components copied from `kits/workbench` with only the class prefix changed, props byte-identical; `tsc -p tsconfig.json` exits 0 |
| REQ-09 — token layer copied, not transcribed | ✅ | `kits/nameplate/src/styles.css` opens with `styles/tokens/nameplate.css` byte for byte; `validate_kits()` 1717 → 1778 |
| REQ-10 — no raw colour literal below the components marker | ✅ | gate green; every value resolves through a token |
| REQ-11 — no component sized by the viewport without a declared reason | ✅ | two width queries, both marked `PAGE` with the reason at the block (the wave closes a full-bleed act; the hero display answers to the viewport while the section head holds) |
| REQ-12 — the pack is chosen-able everywhere | ✅ | all seven enumeration sites name it; `validate_pack_enumerations()` green |
| REQ-13 — forks are reciprocal | ✅ | `roster` ↔ `nameplate` written from both ends with the measured axis, not the register; `validate_fork_reciprocity()` 92 → 94 |
| REQ-14 — the routing scenario exists with its negative branch | ✅ (written) / ❌ (run) | `T31a` / `T31b` are in `test/scenarios.md`. **Not yet run** — stated as an obligation in the file itself, as `T30` was |
| REQ-15 — the kit renders | ✅ | rendered at 1440×900 and an emulated 390×844, and it **found two defects three green gates could not** — see below |

## What rendering found that the gates could not

This is the second consecutive release where the browser beat the ratchet, and the failure
mode is the same one `bulletin` recorded: **a gate reads structure, not layout.**

1. **The plate rendered 78px against a stated 50px.** The kit declared no `box-sizing`, and
   Chrome's UA stylesheet gives `button` `border-box` while giving an anchor `content-box` —
   so the button beside it rendered the 48px it claimed while the plate, an anchor with
   12.8px of padding and a 1px border against a 50px minimum, silently grew by its own
   padding. Every measured height in this pack is a total height, so the component layer now
   declares `border-box` and says why at the declaration. Re-measured: **50px**, matching the
   reference exactly.
2. **Body copy rendered at weight 400 against the pack's central type claim of 500.**
   `--weight-body: 500` existed and no component consumed it, so the token was decorative
   and the rendered page read as a different product. Fixed in the component layer and at
   `:root` in the token layer. Re-measured: **500**.

Neither is visible to a structural check: the first is arithmetic the browser does, and the
second is an absence.

## The gate, run

| | `validate.py` | `validate_palette.py` | `sloplint.py` |
|---|---|---|---|
| baseline `30bfbc3`, clean tree | 3398 | 1912 | 635 |
| this release | **3510** | **1975** | **649** |
| delta | +112 | +63 | +14 |

Every delta is attributed by measurement in `test/floors.json` rather than assumed — the
eleven `validate_*` functions that moved sum to exactly 112, and the palette gate's +63 was
isolated by copying the tree, deleting the two new files and re-running it, which returned
exactly 1912.

## Confirmed at 390

Measured on the rendered kit under device emulation, against what the pack claims:

| Claim | Measured |
|---|---|
| hero display steps to 30px | 30px |
| gutter 24px | 24px |
| the wave is hidden | `display: none` |
| plates wrap rather than scroll | 7 rows, every plate 50px |
| cards collapse to one column | 1 |
| no horizontal overflow | `scrollWidth` 390 |
| every control clears 44px | 0 under 44px |

## What is not done

- **`T31` has not been run.** The pack, its tokens and its kit ship with three green gates;
  the behavioural half is an obligation on the record, and the scenario says so in its own
  Result line.
- **The report surface was read indirectly.** `robots.txt` `Disallow`s `/r`, so the report
  pages were not fetched; the surface was read from the showcase the home page embeds and
  the two stylesheets that draw it. The sitemap lists those URLs anyway — a contradiction in
  the source, resolved in favour of `robots.txt`.
- **The radius census is the reference's, not the kit's.** 87% zero-radius is measured on
  `brandpush.co`; the kit's own harness is a smaller page and lands near 70%. The pack states
  the reference's number and attributes it.

---

## Addendum — 1.48.1, the audit that followed

The question *"did we take everything?"* was answered by measurement rather than
memory, and it found three things. Two are closed here; one is named and left.

### The procedure was written down, because it was not

The assembly rule lived in three places — `CONTRIBUTING.md`'s seven authoring steps,
`docs/DOCMAP.md`'s propagation row for a new pack, and the release section — and three
things I did were in none of them. They are now in the home that already owns each,
rather than in a fourth document, which is what `DOCMAP`'s single-homes discipline
forbids:

| What was missing | Where it went |
|---|---|
| Read the render, not the stylesheet; separate authored CSS from vendor CSS | `STYLE_PACK_TEMPLATE.md` rule 7 — it ships, so an author holding only the bundle sees it |
| How to write a ratio claim the gate can compute | `STYLE_PACK_TEMPLATE.md` rule 8, with all four traps this run hit |
| Render the kit and check its computed values against the pack | `CONTRIBUTING.md` step 8 and the `DOCMAP` propagation row |

Step 8 existed only as a sentence in `bulletin`'s CHANGELOG entry, so whether it
happened depended on the next author reading that paragraph. **It earned its place
within the hour of being written:** the `Mark` tile added below rendered 60×60 against
a declared 50, because `.np-mark` was not in the kit's `border-box` list — the same
defect as the plate, in the component added to close a different gap, caught on the
first render.

### The mark set — the omission that mattered

The reference's report surface repeats one object per feature: a 50×50 tile at 16px
radius with a **5px solid ring**, a wash at 9–12% alpha and a glyph in the matching
solid. Six hue pairs drive it, and the pack carried none of them — so an agent
building the reference's own feature row would have invented six colours.

Measuring them changed what the honest carry is. **They are not a taxonomy.** Seven
of the fifteen pairs are tight, and the reference's own indigo `#5b4bd4` and violet
`#6c5ce7` are 5.58 OKLab units apart at full colour — one colour wearing two names. So
the hue is *variety*, it never encodes which feature this is, and the tokens are
**numbered** rather than named so they cannot be misread as semantic. That is the
measured difference from `pigeonhole`, whose hues are a real taxonomy and whose label
word is therefore mandatory — and the fork is now written from both ends.

The sixth hue was dropped for a second measured reason: the reference's red `#d94558`
sits **2.92** units from `--action-to` and 1.12 under the worst dichromacy. A mark in
the action's colour reads as a control, so the coral stays with the action and the
sixth slot takes `--mark-neutral`. All six clear the 3:1 non-text floor on their own
composited tile; none may carry a word, and the Bans say so with each failing ratio on
its own line.

### A claim that was wider than its evidence

The pack said *"the reference has no dark band anywhere"*, and what was checked was
the home page at 1440. The authored stylesheets declare **eight** dark fills. Both
kinds were then checked: `.bg-header-blue` (`#231b66`) is dead CSS no served page uses,
and the one that renders (`#1f2937`) is inside a **mock of another product's
interface** in the hero image. The claim is true in substance and is now stated at the
width it was measured at — in the pack's Bans and in the token layer's own comment.

### Named and not done

- **`T31` is still unrun.** It requires fresh contexts reading blind, which means
  subagents, and that is the operator's call rather than mine.
- **29% of the authored CSS is still unmeasured into the pack** — `order-form-cro.css`
  (66,546 B) plus the report surface (71,302 B), of 500,051 B. The pack describes a
  front door and says nothing about the checkout, which is where the money is. That is
  an extension to a second surface, not a loose end, and it should be scoped as work
  rather than appended quietly.

### Gates

| | `validate.py` | `validate_palette.py` | `sloplint.py` |
|---|---|---|---|
| 1.48.0 | 4617 | 2659 | 692 |
| 1.48.1 | **4626** | **2681** | **692** |

The palette gate's ceilings did not move: all seven new ratio claims are computed,
and the one that landed unpairable was rewritten — a line whose only token was the
partner, which is the trap rule 8 gained in the same commit.
