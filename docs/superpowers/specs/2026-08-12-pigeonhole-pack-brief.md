# Brief — `pigeonhole`, the sixteenth style pack

- **Run:** `feat/pigeonhole-pack-v1.21.0`, opened 2026-08-12 from `main` at `3845aed`
- **Reference:** <https://www.getinboxzero.com/> — the marketing site of an
  open-source AI email assistant
- **Opening request:** *"https://www.getinboxzero.com/ давай этот сайт в
  референсы добавим тоже"* — the site named, and nothing else. That is the third
  time in this repository, and ADR-0001 requires it be answered by pointing at
  the naming rule rather than by complying silently: the pack is named for the
  register it encodes, `pigeonhole`, and the address lives in its `Origin:`.

## What was measured, and with what

Nothing here is repeated from a reference library's description. The most recent
retrospective entry exists because a style card's four checkable claims about
`fingerprint.com` were all wrong, so this run opened the page first.

| Instrument | What it produced |
|---|---|
| `curl` | `/` at 399,558 bytes; two stylesheets at 6,578 + 593,412 = 599,990 bytes; 152 distinct custom properties |
| headless Chrome, CDP `Runtime.evaluate` at 1440×900 | computed styles for 912 rendered elements — type, colour, radius, shadow, border, transition, animation, transform, per-element |
| the same at 390×844 and 768×1024 | the responsive collapse, measured rather than inferred from breakpoint names |
| `test/validate_palette.py`, imported | every ratio this pack states, computed by the repository's own gate rather than by a second implementation |

Screenshots at 1440×1000 and full-page 1440×4200 were read as well. They are
scratch and are **not** committed — B-015 exists because a previous run's
screenshot was swept into history by a `git add -A`.

## The register, in one sentence

A white page for a product whose job is to **sort the reader's incoming mess into
named categories**, which proves it by colour-coding the categories themselves:
an eleven-hue pastel taxonomy where a hue *is* a category, rendered as a
two-layer chip — an outer chip in the deeper tint holding an inner chip in the
paler one — beside a display face that never goes bolder than 400 and one
italic word in the headline.

The identity in one sentence: **the label system is the design system.** Not a
page decorated with pastels — a page whose only bespoke colour is a filing
scheme, borrowed straight out of the product's own inbox and shown at the size a
reader can read it.

## What the measurement refuted, and it changed the pack

Two claims from the first reading of the screenshots did not survive the DOM, and
they are recorded here because a claim disproved and never written down comes
back as folklore (standing instruction 8).

1. **"Tilted, overlapping cards."** Refuted. Zero rotated elements on the page:
   no `transform` matrix carries a rotation term and no element sets the
   individual `rotate` property. The twelve rotations that do exist are inside
   SVG icon internals and carry no text. The pile reads as tilted and is not.
2. **"A before/after diptych built from the product's own rows."** Refuted as a
   CSS technique. The words `Before` and `After` appear **zero** times in the
   server HTML and zero times in the live DOM after a full scroll pass; the
   section's art is a raster at 1152×703 served through `/_next/image`, one of
   several (hero 1150×631, the next section 1152×539). The diptych is an
   **illustration**, so the pack specifies it as art direction with an aspect
   ratio and a role — never as a component an agent can build from tokens.

What survived, and became the pack: the chip taxonomy is real DOM and fully
measurable — nine categories, each ink saturated on a pale wash of its own hue,
outer chip at radius 8px, inner at 7px.

## Why the library has room for it, at sixteen packs

The pairwise question, asked against all fifteen (standing instruction 10):

- **`showroom`** — white gallery, near-black ink, a seven-layer framing shadow,
  chosen when the best argument is the app on screen. Both are white and
  product-led. The fork: `showroom` frames the application **whole** and lets its
  shadow do the lifting; this pack has no framing shadow at all (its dominant
  shadow is `rgba(151,151,151,0.08) 0 3px 12.9px`, measured on 40 elements) and
  its subject is not the app but **one row of it, labelled**.
- **`cyclorama`** — a pastel field on a 32-second loop. Both are pastel. The
  fork, and it is the one a reader will get wrong: there, pastel is a **field**
  that moves; here pastel is a **taxonomy** that means, and it never moves at all.
- **`orchard`** — warm oat slabs, sage and candy orange, soft-3D pills. Friendly
  and tinted, but the field is warm and the tint is decoration.
- **`workbench`** — the product UI itself. This is the marketing page a user
  lands on before the inbox they log into.
- **`datasheet`** and **`manpage`** — the two most recent, both technical paper
  for a developer buyer. Neither is white, neither is pastel, and both address a
  reader who reads code; this pack addresses a reader drowning in their own mail.

## Source ledger — what the project already knew

| Source | State |
|---|---|
| `docs/DOCMAP.md` | present, 9,563 bytes |
| `docs/superpowers/retro.md` | present, 67,263 bytes — **all ten standing instructions read in full**; the Recent log queried for pack authoring, counts, and origins |
| `docs/superpowers/backlog.md` | present — **14 of 20 rows open**; B-013, B-016, B-017, B-020 touch this work |
| `docs/superpowers/verification.md` | present — 31 rows, **1 at `never`** (REQ-10, carried to B-004) |
| `docs/adr/0001-style-pack-naming.md` | binding — the naming rule; this run is its ninth application |
| `docs/adr/0002-…kits-ship-in-the-package` | binding — the kit ships as source, `dist/` is gitignored |
| `graphify-out/graph.json` | **stale**: `built_at_commit` `9312a85` against a HEAD of `3845aed`; B-009 open, its two candidate fixes untouched by this run |
| the wiki | installed (`~/.obsidian-wiki/config` resolves) |
| project `CLAUDE.md` / `CONTEXT.md` | **absent** — doctrine arrives from `~/.claude/CLAUDE.md`; nothing project-local to contradict |
| release state | `v1.20.0` local **and** on `origin` **and** on npm; three manifests read 1.20.0; `main == origin/main` at `3845aed`. No ghost. Next is **1.21.0** |
| concurrency (instruction 1) | clean: one worktree at stage 0, no foreign HEAD move in `reflog -8`, no file mtime inside 45 minutes. Re-checked before staging |

## Decisions taken in the grill

1. **Scope: the full treatment**, matching `datasheet` (1.19.0) and `manpage`
   (1.20.0) — pack, token layer, kit, reciprocal forks, every enumeration, the
   floors ratchet, the release, and the local channels. Chosen by the operator
   over a pack-without-kit, which would have made this the only one of sixteen
   without a kit while README promises an identical API across all of them.
2. **Name: `pigeonhole`** — a wall of labelled compartments, the object family
   `workbench` and `showroom` already sit in. It carries both halves of the
   register: the compartments are labelled (the taxonomy) and things get sorted
   into them (the transition the page argues). `diptych` was rejected for saying
   nothing about the colour system that is the pack's whole contribution;
   `mailroom` for binding a long-lived artifact to the email domain, where the
   register applies equally to ticket triage, files and CRM.
3. **Scenario runs authorised.** Both branches, in fresh contexts. Standing
   instruction 3 would otherwise force the pack to ship with a stated debt.
4. **Contract: `widened`** — all thirteen headings. The reference is addressable
   and was measured at three viewports, so nothing in the widened four has to be
   invented, and the skeleton's rule 1 forbids shipping on the nine by default.
5. **Design surface: text-only.** No Figma file is recorded for this repository
   and the artifact is a documented visual register rather than a screen to draw.
   Recorded rather than discovered, per the stage-0 UI branch.

## REQ table — frozen; adding is free, removing needs the operator

| REQ | Requirement | How it is verified |
|---|---|---|
| REQ-01 | `styles/pigeonhole.md` carries all thirteen headings, declares `Contract: widened`, and an `Origin:` naming an addressable reference with the measurement date and what was read | `validate.py` heading + contract checks; `sloplint.py` origin check |
| REQ-02 | Every value is measured off the live reference, or marked `SELECTED` at its declaration against the measured set (`MEASURED`) | the token layer's header defines both words; grep at every declaration |
| REQ-03 | `styles/tokens/pigeonhole.css` passes the palette gate — AA on field, the CVD floors, semantic separation — with no `color-mix()` or `lab()` the gate cannot parse | `npm run palette` |
| REQ-04 | Every ratio the pack states is recomputed from the token layer, because its table declares its base | `validate_stated_ratios()`; the palette gate's count rises |
| REQ-05 | The reference's own accessibility failures are recorded in `## Gotchas` with their numbers, never silently applied: **8 of 9** category inks fail 4.5:1 on their own tint ramp (worst `#49d1fa` at **1.53:1**, then `#d8a40c` at **1.65:1**), the hero lede `#848484` at **3.74:1**, white on the CTA's lower gradient stop at **3.29:1** where the upper stop passes at 5.04:1, the `Coming soon` chip at **2.31:1**, and `outline-style: none` on the focused primary CTA | the section, each number recomputed at write time by the gate |
| REQ-06 | The category set is declared **not** a semantic-by-colour peer set, and the declaration carries the number that justifies it: darkening the inks to clear 4.5:1 drops the worst deuteranopic pair from ΔE 4.42 to **1.24**, so hue cannot be the only channel and the label word is mandatory | the token layer's comment at the declaration; a Ban in the pack; the measurement in the design record |
| REQ-07 | `kits/pigeonhole` exists with the identical spine, a `.md` per component carrying `category:`, and `src/styles.css` derived from the token layer | `validate_kits()`; `dist/` listed after `tsc`, not the exit code |
| REQ-08 | `pigeonhole` names every pack a reader could confuse it with, and each of those names it back | `validate_fork_reciprocity()` |
| REQ-09 | The library's count word moves fifteen → sixteen everywhere it is stated, including the three manifests and the core-contract remainder paragraph | `validate_counted_claims()`, `validate_contract_split()` |
| REQ-10 | Every pack enumeration gains the pack: README table, `bin/cli.js`, the slash command, the `.mdc` rule, both manifests, the `.cursor` mirror | `validate_pack_enumerations()` |
| REQ-11 | `test/floors.json` is raised to the new counts with the reason in the same commit | the three gates against the file |
| REQ-12 | A routing scenario is written **with both branches and run** in fresh contexts; its result line carries a verdict and a date | the two runs; every finding reproduced per instruction 8 |
| REQ-13 | `docs/adr/0001-style-pack-naming.md` records this application — `getinboxzero.com` → `pigeonhole` | the file |
| REQ-14 | Version 1.21.0 is synced five ways: `package.json`, `marketplace.json`, `plugin.json`, CHANGELOG top entry, `SKILL.md` `metadata.version` | `validate.py` version sync |
| REQ-15 | `v1.21.0` is tagged, released and published; the CI verdict is **read before** the tag; every local channel is refreshed and verified by reading installed files | `git ls-remote --tags`, `npm view`, the shadow invariant, instruction 9 |
| REQ-16 | The two refuted claims are recorded rather than quietly dropped — no rotation anywhere, and the diptych is raster art rather than DOM | this brief, the design record, the pack's Gotchas |
| REQ-17 | The code graph is refreshed, or its staleness restated honestly with B-009's two candidate fixes intact | `built_at_commit` against HEAD |
| REQ-18 | B-015 is closed: `.tmp-fp-hero.png` leaves the tree and `.gitignore` gains a rule that would have stopped it — this run generates screenshots of its own | `git ls-files`, the ignore rule |
| REQ-19 | This run is stamped, the ten instructions walked and pruned, an entry written only if the run diverged | `retro.md` |
| REQ-20 | At close-out every repository is clean and pushed, and `origin/main` carries the release commit | `git status`, `git branch -vv` |

## Carry-over ledger

| Item | Why it is not in this run | Home |
|---|---|---|
| B-013 — 59% of stated ratios reach no check | The guard needs to tell a measurement from an argument about one; this pack adds ratios that *are* covered (its table declares a base) but does not solve the class | board, open |
| B-016 — a count whose noun is implied reaches no check | Same class as B-013 and should be solved with it | board, open |
| B-017 — the palette gate's peer set excludes a pack's declared semantic roles | This pack **declares its category set out of the peer set on purpose**, with the number that justifies it, so a future widening does not silently redden it. The widening itself stays B-017's | board, open |
| B-020 — the skeleton teaches radius-by-subtraction, one shipped pack calls that an error | Measured here as evidence rather than resolved: the reference's own nesting is 52px outer / 32px inner at 21px padding, so subtraction (52−21=31) misses by 1px and neither rule is exactly satisfied | board, open |
| B-009 — the code graph is two commits behind | Its two candidate fixes are a decision this run does not own | board, open |
