# Changelog

All notable changes to this project are documented in this file. The format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions
follow [SemVer](https://semver.org/spec/v2.0.0.html).

## [1.26.0] - 2026-08-13

The palette gate computed one contrast per theme — ink against field — and never once
asked whether a status colour could be read on the surface it sits on. Twenty-eight
findings in eleven of seventeen packs were waiting behind that.

### Added

- **`validate_status_on_field()`** — every semantic colour is checked against the field
  of **its own theme**, in three tiers, which is what the packs already argued and
  nothing enforced:
  - **≥ 4.5:1** — text, no declaration needed.
  - **≥ 3.0:1** — declared `@role non-text:`, a mark that can be understood on its own.
  - **< 3.0:1** — declared **and** the pack states status is never by colour alone,
    because below the non-text floor the colour is reinforcement and the word is the
    message.
- **`@role non-text:`, a second canonical role marker**, beside the `@role accent:` this
  library already had. It is the whole point of the release: eleven packs *did* say their
  status colours were not text — in five different phrasings ("never text on the field",
  "a FILL and large-text colour", "a fill, not a text colour", "No coral word under
  24px", "category marks") — and a class nobody can grep for is a class nobody checks.
  Documented in `SURFACE_COMPOSITION.md` beside the accent marker.
- Two plants, one per tier, and the check's core was split out so a plant can be a token
  layer written as a string rather than an edit to a real file.

### Fixed

- **`scoreboard`'s dark band inherited the paper status set** (board B-034). Its
  `[data-surface="panel"]` block remapped eleven tokens — `--ink-soft` among them, for
  exactly this reason — and left the four statuses pointing at the paper values, so
  `var(--good)` painted **3.69:1** on that band while `--good-on-dark` had **10.21:1**
  waiting three lines away in the same file. The pack has always said to use the on-dark
  set there; now the token layer does it.
- **`showroom`'s status chip painted its label in its own status colour** (board B-021).
  Measured against the fills the kit actually uses: `--good` **2.03:1**, `--warning`
  **1.54:1**, `--danger` **2.65:1**, at the 12px the same row specifies. The label is
  `--ink` now (14.65–14.73:1) and the status colour is the chip's tint plus a 6px dot —
  which is the pack's own "never by colour alone" rule applied to the component that
  exists to serve it. Corrected in the pack, the kit and with the numbers.
- **`validate.py` counted its own worktree.** Both of its ROOT markdown walks read every
  `.md` under the repository, and this project's standing practice for a concurrent run is
  an isolated worktree at `.claude/worktrees/<name>` — a full second copy of the tree. So
  the gate reported **2361 checks** where the same commit measures **2067** clean, and the
  ratchet in `floors.json` was one commit away from enshrining the inflated number. A floor
  measured with a worktree present fails the next clean run for a regression that never
  happened, and the failure names a count, not a cause. Nested checkouts are now excluded
  by what they **are** — a directory carrying its own `.git` — not by name, because the name
  is a convention and the next one will differ. The plant is the only one in this suite
  whose pass condition is silence: a nested checkout must change neither the verdict nor the
  count, and with the guard removed it reports `MISSED`.
- **`blueprint` answered separation and never legibility.** Its four category marks clear
  every separation floor under all three dichromacies, which the pack said — and
  `--good` **2.40:1**, `--warning` **1.72:1** and `--info` **1.21:1** on the stock, which
  it did not. Its own advice, *"label them anyway, because a legend of four coloured
  squares is a legend nobody reads"*, is now the requirement it always was.

### Notes

- **Nothing else changed colour.** The other twenty-four findings are declarations: the
  packs were right about their own colours and unreadable about it to a machine.
- Gates on the merged tree: `validate.py` 2067, palette **1001**, sloplint 450 — palette
  958 base + 8 from 1.25.0's status set + 35 from this check, additive with nothing hidden
  in it. Floors raised with the reason.
- **This release is 1.26.0 because 1.25.0 was taken while it was being built.** Two runs
  worked the repository at once and both bumped to the same number; the other reached
  `origin/main`, its tag and npm first, so it keeps 1.25.0 and its entry above. Nothing was
  discarded and nothing was rewritten — the collision cost this release a version number and
  twenty-two version references in prose, each of which would otherwise have named a release
  it is not in.
- The two remaining `scoreboard` rows (B-033, B-035, B-036) are untouched — a retracted
  permission still live in its token layer, eight numbers that disagree with the values
  beside them, and a pixel-numeral rule with no working mechanism outside WebKit.

## [1.25.0] - 2026-08-13

**`editorial-luxury` gets the status set it told surfaces to ask for.**

The pack shipped one semantic colour, `--red`, and instructed any surface needing
a full set to close the gap *in the pack, deliberately, not at the keyboard*. The
instruction was right and nobody followed it: a production admin console built on
this pack had invented amber-as-warning and cyan-as-info on top of an amber that
was also its entire chrome — so the hue meaning "a provider is backing up" was
the hue of every button on the page. Seven of that surface's colour pairs sat
below AA and three under 1.1:1.

`--status-{ok,warn,info,danger}` and their `-weak` tints close it. Three of the
four are values the pack already owned: `--status-ok` is `--accent-deep`,
`--status-danger` is `--red`. Only `warn` and `info` are new, each the existing
amber and cyan family deepened until it clears the AA floor for normal text on
**all three** cream grounds — `--paper`, `--paper-2` and `--paper-3` — because
two grounds would have been the same enumerated-list hole one level down. Status
is still never carried by colour alone: the tint carries the colour, the word
carries the meaning in `--ink`.

Also: `--dur-hover` and `--dur-state`. The pack said the product register stays
in the fast range and never named the values, so every product surface built on
it typed `0.15s` literals — there was nothing to reference.

## [1.24.0] - 2026-08-13

A seventeenth style pack, whose whole argument is other people's names — and a reference
whose `h1` is one pixel wide.

### Added

- **`roster`** — the seventeenth pack, extracted from `babylovegrowth.ai` off the
  server-rendered HTML of `/en` (1,415,414 bytes), its two shipped stylesheets (466,577
  bytes, 410 custom properties) and then off **computed styles on the live page** at
  1440×900, 768×1168 and 390×790 — **5,936 rendered elements** at the widest. A white
  field in a faint grid of squares, hairlines instead of shadows, the pill as the most
  frequent shape, and one orange that may never carry a word. For products whose argument
  is *who already carries them*: AI-search and GEO visibility, SEO and content platforms,
  agencies, marketplaces. Widened contract, a light-only token layer, a full reference kit,
  and reciprocal forks written into `scoreboard`, `showroom`, `pigeonhole` and `manpage`.
- **The fork against `scoreboard` is the pack's reason to exist.** Both serve growth, ads
  and SEO products, so the category cannot decide it — the **kind of proof** can. One is
  built around a figure that ticks up; the other around a name that appears. Ask what the
  page loses if you delete its proof, and the giveaway is that `roster` sets its largest
  figure (*4,000+*) in the same 16px eyebrow as everything else.
- **`RESOLVED`, a fourth provenance family.** The reference computes its neutrals in
  `lab()`, which the palette gate refuses on purpose, so each was resolved to the sRGB the
  browser actually paints — **34 distinct values**, each painted into a 1×1 canvas and read
  back as bytes. They turn out to be Tailwind v4's defaults: 7,234 borders at
  `lab(91.6229 …)` = `#e5e7eb`. The bespoke layer beside them is four near-blacks and two
  oranges wide, and the pack ships one of each with the criterion written at the
  declaration.
- **`IndustryColumn`, the signature element** — a pill-labelled column of other companies'
  marks, hairline-divided, six across at 1440 — plus `LogoTile`, `Eyebrow` and `StepCard`.
  Both container breakpoints are **derived from the component's own geometry** (220px for
  the column's two-up mark grid, 640px for the step card's split) rather than carried over
  from the viewport, which is what B-032 exists to prevent.

### Fixed

- **The pack refuses the reference's heading structure.** Its `h1` is `.sr-only` — 1×1px,
  white, `clip-path: inset(50%)` — and the visible 68px line is a `<span>`, while all
  sixteen `h2`s are small orange eyebrows. So the document outline says *eyebrow* where the
  page says *section head*, and the largest text on the page is not a heading at all. This
  pack teaches the opposite and `manpage` now carries the fork from the other end.
- **The accent may not carry a word.** `#fa5c12` is 3.18:1 on white; white on `#f25533` at
  the nav pill's 16px/600 is **3.43:1**. The pack ships `--accent-ink` at 4.52:1 for
  anything read, keeps the accent for fills and large text, and makes the primary button
  black — 19.66:1, which is what the reference itself does for its hero.
- **The dominant secondary ink fails on its own band**: `#6a7282` is 4.84:1 on white and
  **4.35:1** on the `#f0f3f8` band it is painted on. `--ink-soft` is the darkened form and
  clears both.
- **No `--warn` is shipped.** The reference paints no amber anywhere, so one here would be
  invented rather than selected. Stated in the Palette instead of filled in.

### Notes

- **Reduced motion covers six of the reference's animations out of roughly twenty.** Its
  branch names classes one by one, leaving `arrow-nudge`, `skeleton-blink`, both spinners,
  `settings-ripple`, `meta-preview-float` and the accordions running — the opposite failure
  to `pigeonhole`'s reference, which collapsed everything with one `*` rule and strobed its
  marquee by doing so. This pack collapses unconditionally and pauses its two floats in the
  component layer.
- **A claim the measurement refused.** The hero sets a third party's wordmark inline after
  the word *from*; it was sampled seven times across 5.4 seconds with no change, so the
  pack specifies **one mark chosen per page** and makes no claim that it rotates.
- Gates: validate 1938 → 2066, palette 906 → 956, sloplint 436 → 450, floors raised with
  the reason.

## [1.23.1] - 2026-08-13

Two of the seven answers 1.23.0 shipped told an implementer to do something the same
release had just described as impossible.

### Fixed

- **`pigeonhole` contradicted the SELF category it shipped beside.** Its new Responsive
  answer said the labelled row and the FAQ "take `container-type: inline-size` on their
  wrapper" — but the row's axis and the list's columns are properties of the row and the
  `<dl>` **themselves**, so neither can query its own width. That is exactly the SELF case
  the skeleton now defines. The corrected answer is the useful one: both live inside a
  list the consumer already owns, so **the consumer's list is the container** — a
  component library may ask for `container-type` on it and may not wrap someone's markup
  to get it. Descendants inside them (the preview's truncation, the date's visibility)
  are ordinary CONTAINER cases and need nothing from the consumer.
- **`showroom` named a wrapper its kit does not ship.** "container-type on the table
  wrapper" became the **specimen frame**, which is the component that actually holds the
  table (`Specimen`), so the data row and the column header query something that exists.

### Notes

Found by checking every component named in the seven new answers against the components
its kit actually ships — a check worth running whenever pack prose starts naming parts.
Five of the seven were already right; `maquette`'s "agent prompt" is named by the pack and
absent from the kit, which is a pre-existing pack/kit gap rather than this release's.

## [1.23.0] - 2026-08-13

A component library that sized itself by the screen, and a contract bullet nobody had
answered since it was written.

### Added

- **`validate_pack_container_answer()`** — a widened pack's `## Responsive` section has
  to say which of its components size against their container. The skeleton has carried
  that bullet since the contract was widened in **1.5.0**, and **seven of the ten
  widened packs left it blank**: the contract asked and nothing checked, which is the
  same dead zone the all-or-nothing heading rule closed. "None, and here is why" is a
  valid answer — `field-notes` and `cyclorama` were already giving it.
- **`validate_kit_breakpoints()`** — every width media query in the sixteen kits must
  either target `:root` alone or carry a declared reason, because a kit ships components
  a consumer drops into an arbitrary box. It found **seven queries across six kits, and
  zero `container-type` anywhere**.
- **Three kinds of breakpoint, in the skeleton**, because only one of them has a
  container answer: **CONTAINER** (a property on a descendant of a component root),
  **PAGE** (a value the page owns — a hero's padding, a root token switch), and **SELF**
  — a property on the element that *establishes* the container, which cannot query
  itself and has no container answer at all. Five of the seven queries turned out to be
  SELF or PAGE, which is why "0 of 16 kits use container queries" was a worse
  description of the problem than it looked.
- **The distinction the library was missing:** the pack documents a page measured off a
  reference, so its breakpoints are viewport-shaped; the kit ships components this
  project authors, so theirs are container-shaped. `field-notes` was right that
  container queries are "not for the page" and incomplete about the component library
  shipped beside it.
- **All seven silent packs now answer**, each from its own component list — the
  instrument's cell grid, the code frame and the endpoint row, the CLI line and the
  agent prompt, the labelled row and the FAQ's columns, the install line and the
  benchmark row, the data row and the column header, the panel and the figure well.

### Fixed

- **`scoreboard`'s ledger now does what its own pack has always specified.** The pack
  says *"Container queries for the report surface and the ledger: `container-type:
  inline-size`, because both appear inside columns of different widths on the same page
  and neither should size against the viewport"* — and the kit was switching on the
  viewport, so a ledger in a 320px sidebar on a 1440px screen kept its wide columns and
  crushed its leader. This was not a missing modern feature; it was a kit ignoring its
  pack.
- **The breakpoint is derived rather than carried over.** 767px was a statement about
  phones. The row's own geometry: label 95 + gap 12 + numeral column 80 + gap 12 = 199px
  of fixed content, plus a minimum leader of `--space-8` so the dotted line still reads
  as a leader — **231px**, with the 32px named as the one decision it contains.

### Notes

- **Two conversions are held, with the reason at the block.** `blueprint`'s tick and
  column rule and `datasheet`'s cell grid are genuine CONTAINER cases marked
  `TODO-CONTAINER B-032`; each needs its breakpoint derived from its own geometry, and
  carrying 768 or 640 into `@container` would be the same mistake in a newer syntax.
- The new check's own first draft looked back a fixed 400 characters for its marker and
  missed a five-line reason whose marker sat at 425 — a check that fails on a longer
  explanation teaches authors to write shorter ones. It reads the whole comment now.

## [1.22.0] - 2026-08-13

The palette gate learns two colour forms it had been refusing, and the refusal turns
out to have been the reason eight token layers restate a token's channels by hand.

### Added

- **`color-mix()` and relative colour are computable, so they are no longer banned.**
  The gate parses `color-mix(in srgb | srgb-linear | oklab | oklch, A p%, B q%)` —
  premultiplied, shorter hue arc — and `rgb(from <colour> r g b / a)`, with `var()`
  now resolved **inside** a value rather than only as a whole value. Verified against
  Chrome 151's own computed values across eleven cases at a **worst ΔE of 0.004**,
  which is the browser's six-digit serialisation rather than a disagreement.
- **Four self-test plants, two of which prove the new paths are checked rather than
  tolerated.** A `color-mix()` and a relative colour whose ink misses AA must fail on
  the *ratio* — only possible if the parser really computed them. The other two prove
  the refusals still refuse: an unimplemented mix space, and a `calc()` inside a
  channel. Half-implemented CSS maths is worse than an honest refusal.
- **Rule 5 in the pack skeleton** replaces the ban with the limits and one migration
  rule: relative colour is Baseline 2024, so where a token feeds an
  accessibility-critical property — a focus ring above all — the literal ships first
  and the derived value second, because a dropped declaration on a focus ring is an
  invisible focus indicator.
- **`docs/audit/2026-08-13-modern-css-audit.md`** — the whole measurement: what the
  library is ahead on (OKLab dichromacy checks, `color-scheme` in 16/16,
  `text-wrap: balance` in 13/16 kits, `tabular-nums` in 10/16), what is a deliberate
  position rather than a gap, and ten findings with counts.

### Fixed

- **`showroom`'s focus ring now tracks its accent.** `rgba(38, 109, 240, 0.35)` was
  the accent's channels written out by hand; it is now
  `rgb(from var(--accent) r g b / 0.35)`, measured **ΔE 0.00** from the literal, with
  the literal kept as the preceding declaration. Re-tinting `--accent` used to leave
  the ring on the old blue silently — the live mechanism behind B-023/B-024.
- **A blind spot closed in the same commit that opened its cause.** `themes()` decided
  whether a block was a theme by testing for a `#` or an `oklch(` prefix, so a dark
  theme written in `color-mix()` would have been read as "overrides no colour" and
  skipped entirely. It asks `COLOR_SHAPED` now.

### Notes

- **The migration itself is not in this release.** 42 declarations across eight token
  layers are ΔE 0.00 from a token in their own file and could migrate with no visible
  change; 13 more sit within ΔE 2 without equalling one, and *near is not drift* — a
  white at 80% beside an off-white field may be deliberately white. The first set is
  B-027 and needs a per-property support decision; the second is B-028 and needs its
  author, not a script.
- Also filed: B-029 (container queries in the kits — 0 of 16, against 7 viewport
  blocks), B-030 (`text-box-trim`, measure in `ch`, metric-matched fallbacks,
  `@property`, fluid spacing), B-031 (a DTCG export for the Figma seam).

## [1.21.0] - 2026-08-12

A sixteenth style pack, whose eleven pastel hues are a filing scheme rather than a
mood — and a taxonomy that fails its own contrast floor eight times out of nine.

### Added

- **`pigeonhole`** — the sixteenth pack, extracted from `getinboxzero.com` off the
  server-rendered HTML of `/` (399,558 bytes), its two shipped stylesheets
  (599,990 bytes, 152 custom properties) and then off **computed styles on the
  live page** at 1440×900, 768×1024 and 390×844 — 912 rendered elements. A white
  field ruled by hairlines, one blue that only ever appears as a two-stop
  gradient, a display face that never passes weight 400, one italic word in the
  headline, and nine categories in which a hue *is* the category, drawn from an
  eleven-ramp pastel system. For products
  whose job is to sort the reader's incoming mess into named categories — email
  triage, ticket routing, digests, organisers, CRM inboxes. Widened contract, a
  light-only token layer, a full reference kit, and reciprocal forks written into
  `cyclorama`, `showroom`, `orchard`, `workbench` and `manpage`.
- **The signature element is a chip with two layers.** The outer carries the
  deeper tint pair at radius 8px, the inner the paler pair at 7px with one pixel
  between them — the one place in the reference where radius-by-subtraction
  happens to hold exactly. `CategoryChip`'s label word is a **required** prop, not
  an optional one, and the reason is measured: see below.
- **Nine category inks, eight of them derived.** The reference paints its chip
  inks on tints of their own hue and eight of nine fail WCAG AA against those very
  tints — `#49d1fa` at 1.53:1, `#d8a40c` at 1.65:1, `#e65707` at 2.71:1, `#17a34a`
  at 2.72:1, `#c942b2` at 2.79:1, `#c94244` at 3.09:1, `#124dff` at 3.89:1,
  `#6410ff` at 4.28:1. Only the neutral `#525252` clears it. Each is re-derived
  along OKLab lightness with hue and chroma held, and each derivation is marked at
  its declaration.
- **The label word is mandatory, and the number says why.** Darkening those inks
  to clear 4.5:1 compresses them: the worst deuteranopic pair (Marketing against
  Notification) falls from ΔE 4.42 to **1.24**, far under the palette gate's hard
  floor of 10. Eleven hues cannot be simultaneously AA-compliant and mutually
  distinguishable to a dichromatic reader, so the hue is declared a *redundant*
  channel and the category tokens sit deliberately outside the gate's semantic
  peer set — with the reason written at the declaration, so a future widening
  reads it rather than assuming an oversight.
- **`LabelledRow`, `WashCard` and `FaqList`** join the six-component spine. A
  wash card's shadow is mixed toward its own hue rather than toward black, which
  is why the page reads coloured while the field stays white.

### Fixed

- **The primary button's ramp is reversed against the reference.** White on its
  upper gradient stop measures 5.04:1 and on its lower stop 3.29:1 — the label
  passes at the top of the button and fails at the bottom of the same button. The
  pack and the kit run the gradient light-to-dark so the worst case is the passing
  colour.
- **The focused CTA gets a ring.** The reference computes `outline-style: none` on
  its focused primary button with no compensating shadow. The kit ships 2px of
  `--accent-strong` at 2px offset.
- **The lede ink.** `#848484` at 3.74:1, painted at 18px regular, replaced by the
  reference's own `#6b7280` at 4.83:1.
- **Two counts that reached no check** are corrected in passing:
  `SURFACE_COMPOSITION.md`'s accent-role tally (thirteen → fourteen, recounted
  from the token layers rather than incremented) and the kit-count claims in
  `README.md`. The class stays open on the board as B-016.
- **B-015 is closed.** `.tmp-fp-hero.png` leaves the tree and `.gitignore` gains
  the `.tmp*` rule that would have stopped it entering.

### Notes

- **Two claims from the screenshots were refuted by the DOM and are recorded
  rather than dropped.** There is no rotation anywhere on the page — zero
  elements carry a rotation term in `transform` or the individual `rotate`
  property, at three viewports — so a scattered, tilted pile is explicitly not
  this pack. And the before/after diptych is not built from DOM rows: the words
  `Before` and `After` appear zero times in the served HTML and zero times in the
  live DOM after a full scroll pass. The section is raster art, and the pack
  specifies it as art direction with an aspect ratio rather than as a component.
- **No dark theme.** The reference's stylesheet carries a `.dark` block, but it
  belongs to the application's stock shadcn slate theme and nothing on the
  marketing page consumes it. Shipping an undocumented dark twin is a defect this
  library already carries once (board B-018), so the pack is light only and says
  so.

## [1.20.0] - 2026-08-12

A fifteenth style pack, whose display typeface costs zero bytes — and three
WCAG failures in the reference, one of them on the very element the design is
remembered by.

### Added

- **`manpage`** — the fifteenth pack, extracted from `zernio.com` off the
  server-rendered HTML of three pages and its two shipped stylesheets, which
  declare 398 custom properties: the Tailwind v4 default ramps plus twelve
  bespoke brand names (coral, cream, ink, charcoal, burgundy, each with a
  `-muted` partner). Cream paper, a 48px display that never grows louder, a
  576px argument column narrower than most prose, coral label chips that are
  real `<h2>`s, `└` tree glyphs in their own grid column, and one dark code
  frame as the focal point. For developer products whose buyer reads code —
  APIs, SDKs, CLIs, MCP servers. Widened contract, a two-theme token layer, a
  full reference kit, and reciprocal forks written into `blueprint`,
  `datasheet`, `field-notes`, `instrument-console`, `scoreboard`, `showroom`
  and `workbench`.
- **The display face is the system monospace, and that is the whole identity.**
  The reference loads exactly one webfont — a single variable Geist Sans — and
  sets its headline, body, chips, code frames and FAQ in
  `Menlo, Consolas, Monaco, "Liberation Mono", "Courier New", monospace`, which
  is already on the reader's machine. No render-blocking request for the face
  that carries the page, and no swap window on the headline. Substituting a
  webfont mono is banned in the pack: it costs a request to look less native.
- **The section heading is a chip and the chip is a real heading.** `LabelChip`
  wraps its span in an `<h2>`, which is why the reference keeps a clean outline
  — one `h1`, one `h2` per section — while reading as a printed specification.
- **`FaqList` is a `<dl>` that never collapses.** The reference ships zero
  `<details>` and zero `<summary>` on its FAQ: every answer is flat text in the
  DOM, paired with its question, extractable without running JavaScript. The
  component has no `collapsed` prop and will not get one.

### Fixed

Four corrections to the reference, every replacement a colour it already ships:

- **The white button label fails AA.** `Start for Free` is white on coral at
  **4.16:1**, on both the hero and the closing CTA. The fill is kept — the coral
  button *is* the identity — and the label darkens to `--on-action` (ink) at
  **4.55:1**. `--action-strong` is the reference's burgundy, carrying white at
  13.34:1.
- **The signature element is the least readable thing on the page.** The section
  chip paints 12px coral on a coral/8 wash: **3.24:1**, worse than coral on bare
  cream because the wash lifts the field. The wash and edge are kept so the chip
  looks identical; the label becomes `--accent-ink` at **10.40:1**.
- **The live-status green fails AA at 2.82:1.** `green-600` carries the credit
  balance, the `online` badge and both weekly counters. Its own ramp cannot be
  stepped into a legal set — `green-700` still misses at 4.35:1 and `green-800`
  clears AA but separates by only 3.9 under dichromacy — so success takes
  emerald-800, a ramp the reference also ships in full.
- **One reduced-motion gate out of eight animations.** The reference gates its
  40s logo marquee behind `motion-safe:` and leaves the hero blur-in, every
  section rise, `fadeInScale`, `slideInRight`, `pulse`, `ping` and a **1.1s
  infinite `waveform`** running for a reader who asked for stillness. The pack
  collapses the whole surface, and infinite motion **stops** rather than
  shortens.

### Changed

- `test/floors.json` raised: `validate.py` 1647 → 1788, `validate_palette.py`
  716 → 791, `sloplint.py` 366 → 422.
- **The stated-ratio checker earned its keep twice on this pack**, catching
  `--ink-strong` claimed at 18.98:1 against a computed 19.44 and
  `--on-action-strong` at 6.71:1 against 7.76 — both authored by hand, both
  wrong, neither visible on inspection.
- `SURFACE_COMPOSITION.md`: three counts corrected by measurement — the accent
  resolves as `--accent` in **thirteen** packs, `--brand` in `field-notes` and
  `--cta` in `orchard`. **B-016 stays open**: none of the three reaches a check,
  because `in thirteen,` is not followed by a counted noun. This is the third
  release in which they were fixed by hand.
- `plugins/sheleg-design/.claude-plugin/plugin.json` said **thirteen** style
  packs while fourteen shipped. `validate_counted_claims()` did not catch it:
  its pattern wants `<number> [pluggable|locked] style packs` and the manifest
  wrote `pluggable visual style packs`, so the intervening adjective hid a stale
  count from the gate that exists to find them. Corrected to fifteen; the
  pattern gap is the same class as B-016.

## [1.19.0] - 2026-08-12

A fourteenth style pack, and the Refero style card it started from was wrong in
four measurable places.

### Added

- **`datasheet`** — the fourteenth pack, extracted from `fingerprint.com` off its
  live computed styles and its shipped stylesheet, which declares 140 custom
  properties including ten-step ramps for nine hues. An off-white spec sheet, one
  vivid orange, Inter over JetBrains Mono, a concentric radius family from 16 down
  to 2 — and a **live instrument ruled out of hairlines at radius 0 which re-skins
  itself dark when it detects the reader is hiding**. For B2B SaaS whose product is
  a verdict about the visitor, the request or the device: fraud and bot detection,
  device intelligence, identity, API products sold on their payload. Widened
  contract, a two-theme token layer, a full reference kit, and reciprocal forks
  written into `field-notes`, `instrument-console`, `showroom`, `blueprint` and
  `scoreboard`.
- **The dark half is a state, not a theme.** `[data-state="alarm"]` — the token
  `--dash-dark` appears in 97 rules on the reference and every one of them is an
  incognito selector; 134 rules in total re-skin the instrument when it detects
  evasion. Wiring that surface to a user preference is banned in the pack, because
  it destroys the only idea the pack has.

### Fixed

- **`validate_counted_claims()` did not read the three manifests, and both carried
  a stale count.** `.claude-plugin/marketplace.json` said *"twelve pluggable style
  packs"* above a list of thirteen for two releases, and `package.json` said
  *"thirteen"* on the day the fourteenth landed. Names in those files were already
  checked; the number beside the names was not, because the source list was
  all-markdown plus two scripts. The list now includes both plugin manifests and
  `package.json`, watched saying no against a planted `eleven` in the real file and
  again as a permanent self-test plant that derives its wrong number from whatever
  the manifest currently claims.
- **Four corrections to the reference, recorded rather than applied silently.** Its
  primary button sets white on `--orange-7` at **3.32:1**, so the pack's resting
  fill moves one ramp step to `--orange-8` (5.34:1) and hovers to `--orange-9`
  (9.02:1) — no colour invented, and the darkening direction kept. Its 8px mono
  badge is set in `--gray-6` at **2.51:1** and the pack refuses that ink. Its `h1`
  is pure black while its `body` is `#141415`, and the pack ships one ink. Its
  `prefers-reduced-motion` block covers one group of hero animations out of roughly
  twenty keyframe sets, and the token layer collapses the whole surface.
- **Eleven defects in the new pack, found by its own routing scenario and fixed
  before the tag.** T24 ran both branches in fresh contexts — the positive branch
  chose `datasheet`, the negative stayed on `field-notes` — and each was asked to
  read its chosen pack and report defects. The sharpest: in the alarm state
  `--danger` on its own tint measured **4.44:1**, in the one cell that state exists
  to render (the tint moves to `--pink-10`, 6.24:1); and the focus ring at
  `--accent` measured **2.85:1** on `--accent-wash`, the surface the pack itself
  mandates for a selected cell (a new `--focus-color` is `--accent-deep` on paper).
  Also fixed: an accent job list that contradicted the pack's own ban, a button
  border rule with no token behind it, 54 of 118 token declarations carrying
  neither MEASURED nor SELECTED, a "hard floor" argument that sat exactly on the
  floor, a duration measured against the wrong ceiling, an empty state using an ink
  the palette table forbids for content, and two type values outside the ramp. Full
  table in `test/scenarios.md` under T24.
- **`SKILL.md` said "Six of the fourteen … The other seven answer all four."** Six
  plus seven is thirteen against a fourteen-row table, and the pack left out of the
  sentence was the one this release adds. It was this release's own count edit that
  did it — **and the identical defect was found by a scenario agent in the previous
  pack release**, fixed then as an instance. `validate_contract_split()` now derives
  all three numbers from the table, watched saying no against a planted remainder
  and shipped with a permanent self-test plant that reads whatever the paragraph
  currently claims.
- **`SURFACE_COMPOSITION.md` said the accent role resolves to `--accent` in ten
  packs.** True at twelve, silently wrong at thirteen, twelve at fourteen. Fixed by
  hand and filed as **B-016**, because the phrase reaches no check: `in ten,` is
  not followed by a counted noun.

### Changed

- Ratchet floors raised to **1647 / 716 / 366** from 1507 / 603 / 352.

## [1.18.0] - 2026-08-12

### Changed

- **The installer now offers the family's routing block** (closing B-06 in the
  umbrella). Until now only `super-ux` delegated: install this skill on its own
  and no router was written at all, so an agent had the skill and no rule saying
  when to reach for it. The bundle installer wrote all eight, which is why
  nothing looked broken — the gap only opened for someone installing one member.

  Delegated to `npx sshlg-skills routers --member sheleg-design` rather than
  reimplemented, for three reasons:

  - The block describes what the machine actually has. A lone member rendering
    the whole thing would print a table for routers nobody installed.
  - `--member` scopes the write to this skill's own section. Verified by damaging
    two sections of a real block and running this installer: its own was
    repaired, the other left exactly as it was.
  - The launcher is the only writer that copies the operator's global instruction
    file before touching it. That file has no version control behind it.

  `--no-install` keeps it from silently downloading a package nobody asked for.
  When the launcher is absent the command is printed instead of failing: ending
  an install in an error over an optional follow-up reads as a failed install.
  Both paths were exercised.

## [1.17.0] - 2026-08-12

The scenario harness reaches zero unrun, and the last five runs found something
the three gates could not see about themselves.

### Changed

- **Every scenario in `test/scenarios.md` now carries a verdict and a date.** T4,
  T8, T10, T11 and T12 were run **blind** — against the installed bundle, which
  has no `test/` directory, so no agent could reach its own pass condition. Five
  of five green: style-by-name, the Figma border in both directions, the deck
  register, consumer health, and the friendly-half disambiguation.
- **`RATIO_CLAIM` no longer reads `--space-4: 1rem` as a `4:1` claim.** A real
  latent defect that had never fired, because the branch that would have hit it
  skipped every claim whose partner it could not name — the same blind spot, one
  layer down. Floors and bounds (*"must clear"*, *"no better than"*) join the skip
  list, because they are arguments about a measurement rather than one.

### Fixed

- **1.16.0 fixed an instance and called it a class.** It gave
  `instrument-console` a declared ratio base and swept nothing else. Measured now,
  across the library: **121 stated contrast ratios, 71 of them — 59% — reach no
  check.** Six packs declare no table base, and packs that do still leak, because
  a Gotchas paragraph is not a table row.
- **All 71 were recomputed by hand and all 71 are correct**, so nothing shipped
  wrong; what is missing is a guard against the next edit. Two guards were written
  and both discarded, and that is the part worth keeping: pooling every token pair
  **cannot fail** (a planted `9.99:1` passed — thirty tokens are ~435 pairs
  spanning the whole range), and pooling the token named on the line fails on nine
  lines of which eight are correct writing — floors, bounds, gradient positions,
  and candidate colours a pack measures in order to reject them. A guard has to
  tell a measurement from an argument about one. Filed as **B-013**, with the
  honest interim state written into `validate_palette.py` at the point where the
  skip happens, rather than a check that reports coverage it does not have.

## [1.16.1] - 2026-08-12

### Changed

- **The body is back inside the token budget** — ~5478 → ~4988 of 5000. Four places
  were restating what a file beside them already carries in full: the style-pack table
  described each pack in a sentence when every pack file opens with its own
  description, so the table is now for *choosing*; the reference-sweep, When-to-Use and
  Overview sections lost their second telling. Nothing was deleted — the core-contract
  asymmetry, the sweep boundary and the pack-wins rule all stay inline, because those
  are traps an agent cannot know to look up.
- The Cursor mirror was updated in the same change; its drift guard is what caught the
  omission.

## [1.16.0] - 2026-08-12

The five findings T5 and T6 left on the board, actioned.

### Fixed

- **`instrument-console`'s palette table declared no base, so none of its ratios
  were checked.** `validate_stated_ratios` reads the comparison base out of a
  table header; with none, the library's default dark infrastructure pack was its
  **least-covered**, and the one automated fact about it was `--ink` on `--bg`. The
  table now declares `| On \`--base\` |` and every number in it is recomputed on
  each run — the palette gate goes 596 → **603 checks**, which is the size of the
  hole.
- **`--accent-ink` was stated at 6.0:1 in two places and computes 6.17.** From the
  unrounded colour rather than the shipped hex, the same way four `scoreboard`
  ratios were wrong in 1.13.0. Conservative in direction, wrong in kind.
- **`workbench`'s reference kit had no selected row.** The pack mandates
  `--accent-weak` plus a 2px accent inset for selected; `Chip` implemented it and
  `DataTable` did not — the one atom on an admin dashboard that most needs
  selection was the one that lacked it. `DataTableRow` gains `selected`, with
  `aria-selected` on the row.
- **`workbench` stated its type scale and its 4px grid in prose and shipped
  neither as tokens**, which made the craft bar's *"no ad-hoc font size anywhere
  in the diff"* unachievable in this pack specifically — and its own kit wrote
  **twenty** raw `font-size` declarations because there was nothing to reference.
  `--t-chip` … `--t-page` and `--space-1` … `--space-6` now ship; every value was
  lifted from the pack's own Type section, none was chosen. The kit is down to
  zero raw sizes.

### Changed

- **`test/scenarios.md` says out loud that it cannot be blind.** Every scenario
  states its pass condition a paragraph from its brief, so an agent with
  repository access can find its own exam — T5's run reported exactly that, after
  selecting the right pack anyway. Runs are now pointed at an **installed** bundle,
  which carries no `test/` directory. A run against the checkout still yields
  findings; its verdict is not blind and must not be recorded as if it were.

## [1.15.0] - 2026-08-12

Two of the eight unrun scenarios were run. Both passed, and between them they
found four things three green gates could not.

### Added

- **A core pack's missing half has an authored answer, and the bundle now says
  where.** `npx sheleg-design-skill --kit <pack>` materializes `src/styles.css`,
  whose component half is real CSS for `:hover`, `:focus-visible`, `:disabled` and
  selected — the exact per-component states a **core** pack declines to specify.
  `SKILL.md` said kits are not installed and stopped there, so an agent reading the
  bundle invented those states from scratch while an authored version sat one
  command away. Neither file pointed at the other.
- **A precedence rule for the dial table.** "A quiet internal admin dashboard"
  fires both *quiet like Linear* (DENSITY 2–3) and *product UI* (6–8) — a factor of
  three, with nothing to break the tie. **The row that names the surface wins over
  the row that names a mood**, and you say which fired.
- **Two cases the reference-sweep pairing assumed away**, both common: only the
  image server present (you are reading structure off screenshots — a weaker read,
  say so) and a sweep that returns nothing (a null result is a result; "I swept"
  with no findings and no statement of emptiness cannot be told apart from not
  sweeping).

### Fixed

- **`workbench`'s accent gotcha named two surfaces of three.** It forbids accent
  text on `--panel-2` and `--accent-weak` at 4.30:1 — but in light mode `--bg` **is**
  `--panel-2` (`#F7F8FA`), so a plain accent link on the app ground fails identically
  and read as covered for four releases. The most ordinary element in an admin panel.

## [1.14.1] - 2026-08-12

### Fixed

- **1.14.0 said Refero was "alone among the three" in returning flows. Mobbin
  returns them too.** `mcp__mobbin__search_flows` has always existed; it was
  invisible because Mobbin was registered and unauthenticated, so the sentence
  shipped as a claim nobody in that session could check — in a file whose own
  rule, two paragraphs away, is **gate on the tools present in the session, not
  on the config**. The rule was right and was not applied to its own author.
  Corrected the hour Mobbin was signed in, against its live tool surface.
- **The distinction that replaces it is the useful one: they answer in different
  media.** Mobbin returns each step as an evenly-spaced *preview image* — its own
  tool description says to look at those rather than trust the metadata — and
  also searches web **sections** (hero, pricing, footer). Refero returns each step
  as *structure*: a goal, an action, a system response. Drawing a diagram with
  decision points and recovery paths reads Refero; judging whether a step works on
  a phone looks at Mobbin.

## [1.14.0] - 2026-08-12

### Added

- **Refero joins the reference-sweep slot** (`mcp__refero__*`), beside Lazyweb
  and Mobbin. It searches real UI screens, returns visually and functionally
  *similar* screens for one you already have, and — alone among the three —
  returns **flows**: connected steps carrying a goal, an action and a system
  response each. `DESIGN_SYNC_BRIDGE.md` §4 now says what each of the three is
  for, since they are not interchangeable, and the section heading names all
  three: a heading is a discovery surface, which is the lesson 1.12.1 shipped.

### Changed

- **The sweep boundary is now stated against a tool that argues with it.**
  Refero ships a *style* search whose own description offers "typography,
  palette, layout/composition, spacing, elevation… the overall design language"
  — by that description a source of identity, which is the half a pack owns. The
  rule is unchanged and now explicit: a style found there is a **candidate
  source**, not a decision. One that should set identity goes through §5
  live-site extraction into a pack, with measured values and an addressable
  `Origin:`; applied straight to a page it is a second identity source and the
  page ends up in two design systems. The one-line test: **a sweep may change
  what is on the screen and where; only a pack may change what it looks like.**
- The gate pins the full §4 heading, so a fourth server is a check failure
  rather than a silent omission.

## [1.13.1] - 2026-08-12

`scoreboard`'s routing scenario was run the day it shipped, and it found nine
things three green gates had not.

### Fixed

- **The focus ring was invisible.** 1.13.0 promoted the reference's decorative
  `focus-within` glow — a 20% accent halo with a 40% border — to the pack's focus
  treatment without measuring it. Composited the way a browser does it, the halo
  is **1.29:1** against the paper and the border **1.67:1**, against a WCAG floor
  of 3:1 for a non-text indicator. `--ring-focus` is a solid 2px accent ring now,
  and `--ring-focus-sand` carries `--surface-sand`, the one field where the accent
  falls under the floor at 2.97:1.
- **No orange in the pack can carry a link, and 1.13.0 said one could.**
  `--accent-hover` was called "the one orange that may carry a link" at 4.12:1 —
  below the same AA threshold the pack cites two paragraphs earlier to ban the
  accent from text. A link is `--ink` with an `--accent` underline.
- **Four status ratios were stated 0.02–0.08 optimistic**, computed from the
  OKLCH the colours were selected from rather than from the 8-bit hex the token
  layer ships: `--good` 5.09, `--warn` 4.78, `--danger` 7.93, `--info` 6.49. They
  passed the repository's own gate only because its tolerance is 0.1, which is
  how a wrong number survives a green check.
- **The status chip carried a 10% tint that put an 11px `--warn` label at
  4.38:1.** The chip has no fill now — the word carries the colour. This also
  removes a disagreement between the pack doc and the kit, which had never
  rendered a tint.
- **`--bp-md` and `--bp-lg` were referenced in three token comments and defined
  nowhere.** Replaced with the pixel values they meant.
- **`SKILL.md` miscounted its own library**: "Six of the thirteen are on the core
  contract … the other **six** answer all four." Six plus seven. Introduced by
  1.13.0's own count edit and found independently by both scenario branches.
- **`SURFACE_COMPOSITION.md` said only `field-notes` ships a validated
  `--chart-1…N` set.** `scoreboard` ships one too.
- **The numeral column is a glyph budget, and the pack only warned about it.**
  Press Start 2P advances a full em per glyph, so at 15px the 80px column holds
  five glyphs and the 70px mobile column four: `3.4x` fits, `$9,840` does not.
  Stated as a ceiling with the only two legal answers — shorten the figure, or
  widen the column for the whole ledger.

### Changed

- **T23 has a result.** Both branches run in fresh contexts: `scoreboard` chosen
  for the tally brief with the fork quoted from both sides, `field-notes` held for
  the provenance brief. Recorded with every finding's disposition — including one
  **refuted** (`--on-accent` is not a dead token; its consumer is the selected chip
  at 4.92:1), because a refuted claim nobody writes down comes back as folklore.
- `validate_palette.py`'s floor drops 597 → 596, with the reason in
  `test/floors.json`: a token was deleted rather than a check weakened.

## [1.13.0] - 2026-08-12

A thirteenth style pack, and it is the first one in the library whose accent is
forbidden from carrying a word.

### Added

- **`scoreboard`** — the thirteenth pack, extracted from
  <https://www.get-ryze.ai/> on 2026-08-12 off its shipped stylesheet and the
  markup of three pages. Warm paper (`#FAF9F5`), a warm near-black ink
  (`#221D16`, 15.88:1), radii of two and three pixels, an **ink** primary button,
  one hot orange (`#FF4801`) used only as a mark, and a dark ledger of
  dotted-leader rows whose numbers are set in an aliased pixel face. Widened
  contract — all thirteen headings — with `styles/tokens/scoreboard.css` and a
  full reference kit in `kits/scoreboard/`.
- **The accent measures 3.23:1 and the pack says so at the top.** Above the 3:1
  floor for a non-text mark, below the one for a word. The reference obeys this
  without ever stating it: across three pages its orange is a 3×18px tick, a
  `::marker`, a focus ring, a selection colour, a link underline and one
  oversized chevron — and its primary button is ink. The pack turns that
  observation into a ban, which is the only reason a page in it can carry a
  colour that loud.
- **Two status sets rather than one filtered set.** The reference paints status
  only on its dark panels; those values measure 1.6–2.6:1 against warm paper. The
  paper set is selected from deeper steps of the Tailwind ramp the reference's own
  stylesheet ships, and the measured on-dark set is kept beside it under
  `--*-on-dark`. Every declaration says which of the two kinds of claim it is.
- **`TickHeading`, `Ledger`, `LedgerRow` and `StatusChip`** in the kit, on the
  same six-component spine as every other kit. `StatusChip` takes `label` as a
  **required** prop: the paper statuses cluster (the accent and `--warn` separate
  by 6.3 under protanopia), so status in this pack is a chip with its word in it.

### Fixed

- **Three corrections to the reference, recorded rather than silently applied.**
  Its positive-delta colour `#00D492` is set at 11px on white — 1.84:1, an
  invisible success state — and is confined here to the dark panel where it
  measures 10.21:1. Its primary button transitions over 500ms, past the 300ms
  ceiling in `MOTION_DOCTRINE.md` §3, and the pack pins `--dur-fast` at .16s. Its
  scan line animates `top`; the pack rebuilds it on `transform`.
- **`validate.py --self-test` printed FAILED and exited 0.** `main()` returned
  the self-test's status and `__main__` called it bare, so the code was dropped
  on the floor and `npm run selftest` stayed green through a self-test that had
  failed — found because this release's count change broke a plant fixture and
  the suite passed anyway. The argv handling directly above it exists to close
  this exact class one layer up and never reached the exit code. Verified by
  breaking a fixture in a copy of the tree: 0 before, 1 after.
- **A plant fixture pinned to a literal that changes every release.** The
  stale-count plant searched for `**twelve locked style packs**`; the first time
  the library grew it mutated nothing and stopped testing the check it exists
  for. It now reads whatever number the README claims and makes that wrong.
- **Reciprocal forks with `field-notes` and `workbench`.** From a distance
  `field-notes` *is* this pack — warm paper, one orange-red accent, hairline
  rules — and the distinction is what the small type does: mono numerals make
  evidence auditable, pixel numerals make results countable. Both neighbours now
  carry the fork back, so an agent arriving at either one first still learns it
  exists.

## [1.12.1] - 2026-08-11

- **The reference-sweep heading named one server for a section about two.** It
  read `Optional — real-world references (Lazyweb MCP)` after Mobbin joined it,
  so an agent skimming headings would conclude Mobbin was not there. Headings are
  a discovery surface, not decoration.

## [1.12.0] - 2026-08-11

Mobile becomes a register the skill can name, and a second reference sweep joins
the one slot that already existed rather than opening a competing one.

### Added

- **`MOBILE_SURFACES.md`** — loaded when the brief is a native app screen or a
  mobile-web view. It collects the five mobile rules the packs each state on
  their own (`svh` over a banned bare `100vh`, the 16px input floor that exists
  to stop iOS zoom-on-focus, a desktop flourish that must not survive into a
  touch target, the `pointer: coarse` depth collapse, and why reduced motion and
  a coarse pointer are two signals rather than one). Until now a reader looking
  for *mobile* had to find them inside `field-notes`, `cyclorama` and the
  template.
- **The half a pack does not decide on a phone: platform convention.** Where
  primary navigation lives, sheet versus push, gesture affordances, the notch and
  the home indicator — no pack in the library states any of it and none should.
  Said out loud, in the same shape as a `Contract: core` declaration, so the
  silence is not read as permission to invent.
- **Mobbin joins the reference-sweep slot** (`mcp__mobbin__*`) beside Lazyweb.
  Strongest on native iOS and Android, and it carries web products too, so it is
  swept on a website as well — **use whichever server is present, on web and
  mobile alike; with both, sweep both.** `DESIGN_SYNC_BRIDGE.md` §4 is
  unchanged and now governs two sources: **a sweep informs structure, hierarchy,
  content order and platform convention; identity stays the pack's.** Stylistic
  observations are allowed *as observations* — "three of five finance apps use a
  full-bleed dark sheet for the confirm step" is a structural fact worth telling
  a designer; "use their blue" is a second identity source, and a reference that
  genuinely should set identity goes through §5 live-site extraction into a pack
  instead.

- **A sixth mobile rule that no pack answers.** Every pack's type scale is a
  `vw`-keyed `clamp()`, which responds to viewport width and **not** to iOS
  Dynamic Type or Android's font scale — a user at the largest text size gets
  the same type as a user at the smallest. Zero mentions of it existed anywhere
  in the bundle. Two independent test agents raised it as the largest
  unaddressed gap for a native surface, and it is now stated as a gap with the
  decision handed to the reader rather than answered with an invented value.

### Changed

- **The sweep gate reads the tools, not the config.** A registered MCP server
  nobody has signed into exposes nothing, and Mobbin needs both a browser
  sign-in and a paid plan — so "is it configured" was never the right question.
  Its tool surface is unpublished, so the skill says to discover what the session
  exposes rather than naming a tool it cannot verify.
- **The description carries a mobile trigger** (`"mobile screen" / "мобильный
  экран"`) and `mobile app screens` in the product-UI clause. It was restructured
  rather than extended to make room: the two overlapping Figma triggers merged
  into one pair and `"particle landing"` came out, since the prose already
  carries `particle/WebGL background`. Net 964 → **961**, under the 970 working
  limit the house rule reserves for a future "not for" clause — the first draft
  reached 1017 and the gate refused it.
- **One trigger removal was a regression, caught by running T1 rather than by
  reasoning about it.** Dropping `scrubbed sections` from the prose cost the
  scroll-narrative storyboard task: a fresh agent answered `none` where the old
  description loaded the skill. A control run against the previous description
  proved the edit caused it rather than the task being borderline. The phrase is
  back, paid for by shortening `marketing site, or hero experience`, and the
  re-run is **14/14 — 0 misses, 0 false loads** across the full set including
  both new mobile tasks. A description edit obliges the whole trigger set for
  exactly this reason.

## [1.11.0] - 2026-08-10

The bundle now stands on its own. A repeat audit ran the skill the way an agent
actually uses it — six application scenarios in fresh contexts, not routing
questions — and found the same defect class three times: **a rule inside the
shipped bundle instructing the reader to use something only the repository has.**
1.10.0 had fixed one instance of this and swept the literal form (a repo path in
backticks, now zero) without sweeping the class.

### Fixed — the class, in its three shipped shapes

- **The bundle carries its own version.** `SKILL.md` front-matter gains
  `metadata.version`, making version sync ×5. `DESIGN_SYNC_BRIDGE.md` §7 has told
  readers since 1.6.0 to record the pack version in the synced project; there was
  no version anywhere in the bundle to read, only historical mentions in two packs
  ("until 1.10.0 the header rule read…"). A rule whose input does not ship is not
  a rule.
- **The spine is named.** §1 built its "names are the interface" argument on "the
  same six component names" and named none of them. They are now stated —
  `Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — so a delivered kit can be
  checked against the claim. A test agent refused to guess them and said asserting
  them would be "inventing a value and believing I read it".
- **Pack-authoring rules ship with the template.** *Never ship on the nine*, *no
  addressable reference, no pack*, *a derived value is marked derived where it is
  declared*, and *the three gates are what done means* lived in `CONTRIBUTING.md`,
  which no install contains. They are now in `styles/STYLE_PACK_TEMPLATE.md`,
  which does.
- **`validate_bundle_self_sufficiency()`** gates all three shapes, each watched
  failing on a planted defect *and* discriminated by its own message. It checks
  the three forms that have actually shipped and says so — it is not a general
  proof, so a fourth instance has to be a new shape.

### Fixed — two files that disagreed, and two constants with no value

- **The scrub recipe now obeys the doctrine it contradicted.** `SHELEG_DESIGN.md`
  §9 shipped `useLayoutEffect` with hand-rolled teardown; `MOTION_DOCTRINE.md` §6
  names that exact pattern as where leaked triggers and doubled animations come
  from. Neither file acknowledged the other, and an agent reading only the
  reference copied the banned shape into a junior-ready plan.
- **`arcAmp` and `drop` are declared tuning constants.** Both appeared inside
  formulas with no value anywhere in the skill, which reads as an omission rather
  than a decision. Neither is invented here; the rule is to tune, then record the
  value beside the formation rather than inline.

### Changed

- **The entry point is back under its disclosure budget** — 6157 → 4856 tokens.
  Scene depth and the `dataviz` handoff moved to `SURFACE_COMPOSITION.md` with
  stated load triggers; the quick-reference table moved next to the mechanisms it
  summarises in `SHELEG_DESIGN.md`. No doctrine was deleted.
- **The front-matter budget was measuring the wrong thing, and fixing it raises
  the total ceiling from 1024 to 1280.** That is a loosening, named as one. The
  single 1024 cap over the whole block conflated the spec's limit on
  `description` with the bookkeeping keys beside it, leaving the check stricter
  than the standard it claimed to implement — so a 24-character version key
  consumed the description's headroom and would have blocked the widening board
  row B-006 asks for. Now two budgets: `description` ≤ 1024 (the spec),
  everything else ≤ 256, against 74 characters used today.
- **Six scenario results recorded** with their commit, closing most of board row
  B-005. The harness had 20 scenarios and 7 recorded results, so the repository
  could not answer "do the usage scenarios work" from its own records.

## [1.10.0] - 2026-08-10

A fresh-eyes audit of the whole skill, and the finding is the green: at 1.9.0 all
three gates passed — 1270 / 412 / 224 — while the skill told a reading agent
there were six style packs, handed the chart layer a token ramp no pack defines,
and stated thirteen contrast ratios that are wrong.

Full report with every `file:line`, and the reproductions:
[`docs/audit/2026-08-10-skill-audit.md`](./docs/audit/2026-08-10-skill-audit.md).

### Fixed — what an agent was told that was not true

- **The `dataviz` handoff named tokens no pack defines.** `SKILL.md` promised a
  ramp `--accent-tint … --accent-deep`: `--accent-tint` exists in **one** pack of
  twelve, `--accent-deep` in three, and **no pack has both**. It promised a
  status set of `--good` / `--warning` / `--danger` that seven packs lack and
  two have no version of at all. An undefined custom property does not error —
  the declaration goes invalid at computed-value time and the property silently
  inherits — so the agent follows the instruction exactly and the page is wrong.
  The table is now written by role, and the non-uniform mappings are named.
- **Thirteen stated contrast ratios, recomputed and corrected.** `blueprint`'s
  ratio column is headed ``On `--bg` `` and every number in it was computed
  against pure white (`--ink` 17.74 → **17.15**, `--accent` 7.53 → **7.28**,
  pure black 21 → **20.31**). `prism` claimed ink "≥18:1 over all four stops"
  three times; it is **15.85–16.82** — 18.95 is ink on plain white, carried onto
  the wash. Also `showroom` 15.9 → **15.35** and 7.7 → **7.08**, `maquette` 5.0 →
  **5.62** and 13.9 → **13.57**, `editorial-luxury` 6.1 → **6.93**, `workbench`
  5.0 → **4.57**. None crossed a floor; all were presented as measured.
- **Two packs justified one accent by a "symmetry" that is a mathematical
  identity.** WCAG contrast is symmetric for every pair by definition. In
  `showroom`, whose field is white, the sentence stated one measurement twice; in
  `blueprint`, whose field is not, the two directions genuinely differ and the
  pack asserted one number for both.
- **`atrium` prescribed `transition: padding-top .2s` on a sticky header** — a
  layout property, transitioned, on scroll: the exact form `MOTION_DOCTRINE.md`
  forbids, shipped inside the bundle that ships the ban.
- **`field-notes`' radius rule, its worked example and its token layer were three
  different systems.** "Subtract the padding … `12 - 12 ≈ 7.2`" — subtraction
  gives 0; the token layer uses `calc(var(--radius) * 0.6)`.
- **`blueprint`'s Components and Hero instructed the violation its own Signature
  element section names** (registration marks on both CTAs). `test/scenarios.md`
  recorded this as "fixed in the same run"; only half of it had landed.
- **`atrium` said three shadows exist**; its token layer defines four.
- **The colour-blindness ban was copy-pasted into six packs**, asserting a
  measurement across "several pairs" in packs owning one status colour or none —
  and naming four states as if the pack supplied them, which is an invitation to
  invent a hue. Rewritten for `orchard`, `editorial-luxury` and `briefing-room`.
- **`MOTION_DOCTRINE.md` §5 over-banned**, forbidding everything outside four
  properties while §2 prescribes an ease for colour changes. The ban is on
  layout, which is what its own rationale says.
- **ADR-0001 named a pack that never existed** (`lecture-hall`; the pack that
  shipped from graphify.com is `field-notes`). The decision stands; the example
  was written on a branch that never merged.

### Added — the half-library nobody declared

Six of twelve packs carry `## Components`, `## Hero`, `## Responsive` and
`## Signature element`; six do not, and nothing said which. Every pack now
declares **`Contract: core` or `Contract: widened`** above its Register, a core
pack states what it leaves the reader to decide, the `SKILL.md` routing table
marks it, and a check enforces the declaration against the headings present.

### Added — six checks, each watched failing on a planted defect

Counted claims (whitespace-normalised: the README's "six locked style packs" was
split across a line break) · exhaustive pack enumerations in both manifests, the
slash command, the CLI, the README and the Cursor rule · one name for the pack
contract · the `Contract:` declaration · the core role vocabulary (`--bg`,
`--ink`, and an accent role every pack resolves) · and **every stated contrast
ratio, recomputed from the token layer**.

The ratio check is scoped to claims whose base the document declares — a column
headed ``On `--bg` ``, an `on/over --token` phrase, or an `--on-X` name. A first
draft that inferred the partner produced 22 false positives out of 40.

### Fixed — three gates that could not fail

- **Deleting requirements made two gates quieter, and green.** Stripping a pack's
  four widened headings took `validate.py` 1270 → 1269 and `sloplint.py` 224 →
  223, both exit 0. **Ratchet floors** now live in `test/floors.json` and are
  enforced by all three.
- **One decoy comment disabled a slop-lint ban for a whole file, permanently.**
  The check took the first match only and `continue`d past a nearby negation
  word, so the counter fell and later occurrences went unexamined. Suppression is
  now per occurrence, and ban-quoting sections are exempted by heading.
- **`validate.py --self-test` printed OK for a self-test that did not exist** —
  the same defect the 2026-08-05 retrospective recorded in `validate_palette.py`.
  All three scripts now exit 2 on an unknown argument, and `validate.py` has a
  real self-test: six planted defects, run against a copy of the tree.
- **The slop lint read only fenced code blocks**, and no style pack contains one —
  so all twelve packs, `SKILL.md`, both bridges and the AI patterns were never
  linted. It now reads the inline CSS the packs prescribe in prose.
- **`npm test` and both workflows now run every gate and every self-test.** The
  release path was gated on one of three.

### Fixed — stale counts and reach

"six locked style packs" and "all six kits" (twelve), "T1–T7" (T1–T19), "Three
packs extracted" (eight), the pack contract called nine / ten / thirteen in five
places at once — one of which told an author to ship nine headings, which the
gate then passed. `plugin.json`, `marketplace.json` and the `/sheleg-design`
command named three packs of twelve, so nine could not be asked for by name.
`MOTION_DOCTRINE.md`, marked REQUIRED, appeared on no install surface: it is now
in the README table, the CLI help and banner, the slash command, and the Cursor
rule — which gains the whole doctrine in condensed form.

Gates: **1364 / 469 / 320**, from 1270 / 412 / 224.

## [1.9.0] - 2026-08-09

Four style packs, taking the library from eight to twelve — and a fix to the
thing that would have made twelve worse than eight.

Extracted from four live references on 2026-08-09. Three of them sell vector
databases and none of them collapse into each other; two are the same company's
project page and product page, and they share a type stack and nothing else.

### Added

- **`showroom`** — from [attio.com](https://attio.com/). A white gallery where
  one real product surface is the exhibit, under a **seven-layer shadow**. The
  reference declares its palette in **CIE Lab**, which this repo's palette gate
  cannot parse; every value was converted by painting it into a canvas and
  reading the sRGB bytes back — the browser's conversion, not ours.
- **`blueprint`** — from [pinecone.io](https://www.pinecone.io/). A drawing
  sheet: a 32px grid, ruled column boundaries, corner registration marks, one
  electric blue that works as ink *and* as fill at 7.53:1 both ways, and **no
  radius anywhere**.
- **`prism`** — from [milvus.io](https://milvus.io/). One static iridescent wash
  with a hard bottom edge, a heavy grotesque display over **mono body copy** —
  the inversion that makes a page read as a project rather than a company.
- **`maquette`** — from [zilliz.com](https://zilliz.com/). A near-black table
  with a cream axonometric model on it, mono block labels, and the only accent in
  this library's four new packs that works as text (15.49:1).
- Four reference kits, each with the six-component spine plus four signature
  parts, and four routing scenario pairs (**T16–T19**), every one with its
  negative branch.

### Fixed — the routing table, which was a list

**Five of the eight shipped packs named no other pack at all.** Forks existed
only in `field-notes`, `cyclorama` and `atrium`, and every one pointed backwards
at packs that never pointed back — so an agent entering at `instrument-console`,
which is where any infrastructure brief lands first, never learned that a
distinction existed. Four more one-way forks would have made twelve packs with
eight dead ends.

- `instrument-console`, `workbench`, `field-notes` and `cyclorama` each gain the
  mirror clause for the new pack that forks against them.
- **A new `validate.py` check enforces it:** a markdown link from one pack to
  another must be reciprocated. Watched failing against a planted defect before
  it landed.

### Fixed — in the packs, not in the references

- **`blueprint`'s reference sets pure black as body ink**, on 316 elements, which
  the doctrine bans. The pack ships the reference's *own* second ink `#111827`
  (136 elements) and does not pretend it is the same colour: the two sit **21.2
  apart** in OKLab.
- **`showroom`'s reference names `#A4ADBA` "caption-foreground"** and it measures
  **2.27:1** on its own white field. Kept, renamed `--disabled`, and captions
  routed to an ink that passes.
- **`prism`'s reference sets 72px display type in `#00B3FF`** — **2.36:1**, which
  fails even the relaxed large-text floor. The cyan is a fill in this pack.
- **Neither `blueprint` nor `prism` ships a `prefers-reduced-motion` branch** —
  zero blocks each, against live marquee, ping, pulse and scroll. Both packs
  require the branch their references omit.
- **`maquette`'s status palette is derived, not extracted**, and the token layer
  says so at the declaration. The reference exposes none; the first set this run
  reached for was a framework default, and the palette gate caught it colliding.

## [1.8.0] - 2026-08-08

An eighth style pack, and the first one whose reference already implements this
skill's own core pattern.

`cyclorama` is extracted from [codos.ai](https://www.codos.ai/): a pale field
that breathes through **six pastel stops on a 32-second loop** under near-black
ink that never moves with it, a **monospaced typewriter serif** over a
monospaced sans, one orange used only as a fill, and no shadows anywhere. Its
reference ships GSAP ScrollTrigger with real pinning and two WebGL canvases
whose formation holds and then redeploys — principle 3 in production rather than
in a doc.

### Added

- **`styles/cyclorama.md`** on the thirteen-heading widened contract plus
  `## Motion flavor`, with an addressable origin and every ratio computed by
  importing `test/validate_palette.py` rather than by a second implementation.
- **`styles/tokens/cyclorama.css`** — the six cycle stops as named tokens, one
  ease, three durations plus the 32s loop, a five-step radius ramp whose nesting
  is arithmetic, and an inline accent-dot cursor.
- **`kits/cyclorama/`** — the six-component spine plus four signature parts:
  `FieldStop` (the six stops as six static surfaces — the cycle itself does not
  cross the border), `AppWindow` (a hairline frame with **no fill**, so the
  field shows through it), `StatusPill` and `ComparePanel`.
- **`docs/adr/0001-style-pack-naming.md`** — restored to `main`. It was written
  on a branch that held at its stage-0 gate and never merged, so the decision
  register began at `0002` for four days while the rule it records was already
  binding. It is why this pack is `cyclorama` and not `codos`.
- **T15** in `test/scenarios.md` — a routing pair with its negative branch, so
  "is `cyclorama` distinguishable from `field-notes`?" can fail in the
  interesting direction.

### Fixed — in the pack, not in the reference

- The reference paints its section eyebrows in the accent on the field, which
  measures **1.71–1.97:1** across the six stops. This pack does not propagate
  it: the accent is a fill, eyebrows take `--ink-soft` at 8.36:1. The three
  darkened-orange candidates are recorded in `## Gotchas` **with their numbers**,
  because each one trades a WCAG failure for a colour-blindness collision with
  `--danger` or `--warning` — there is no text-safe orange in this palette, and
  the next reader should not have to rediscover that.
- The pack states that `--accent` and `--signal` sit 6.8 apart under protanopia
  and that **the palette gate cannot see it**, because `--signal` is not one of
  the names it treats as semantic. Written down rather than renamed around: a
  token renamed to satisfy a checker is worse than an unchecked token that says
  so out loud.
- The reference's own display fallback is `Fraunces`, which is **proportional**,
  while the face it replaces is monospaced — so a reader without the licensed
  font gets a hero that reflows rather than merely restyles. The pack ships
  measured substitutes instead (Courier Prime 0.600, Cutive Mono 0.605 against
  the original's 0.590).

## [1.7.0] - 2026-08-05

The Claude Design border, and the first code this skill has ever shipped.

`DESIGN_SYNC_BRIDGE.md` is the contract for pushing a pack to claude.ai/design
through Claude Code's bundled `/design-sync`, so the design agent builds screens
out of a pack's real components instead of generic ones. Like the Figma bridge,
it spends as much space on what does **not** cross: motion stays in code, and a
kit is the static half of a pack.

### Added

- `DESIGN_SYNC_BRIDGE.md` — seven sections, each a reference type or a border:
  what crosses and in what shape, style packs as the source of truth, the
  Figma/pack/Claude Design triangle taken one direction at a time, Lazyweb
  sweeps (layout crosses, identity does not), live-site extraction (the pack
  first, the sync second), what cannot cross, and round-trip discipline.
- A tool-presence-gated `## Optional — Claude Design (design-sync)` section in
  `SKILL.md`, gated exactly like the Lazyweb one. Cursor is unaffected.
- **Seven React reference kits** under `kits/<pack>/` — a six-component spine
  with identical names, props and types in every kit, plus each pack's signature
  components, built by `tsc` to `dist/` with a `.d.ts` tree, because the
  converter reads the built entry and the design agent codes against those types.
- `npx sheleg-design-skill --kit <pack> --out <dir>` materializes one kit and
  drops the pack document into `guidelines/` on the way.
- `--accent-ink` in `workbench`, `editorial-luxury` and `instrument-console`,
  additively. Text on the accent had no token in those three; `atrium` and
  `briefing-room` already had exactly this name. In `workbench` it flips with
  the theme, because white on the dark-mode accent is 3.2:1 and fails AA.
- `docs/DOCMAP.md` and `docs/adr/` — the repo's doc map and its decision home.
- Scenario `T14`, run green by a fresh agent holding only the installed bundle.

### Changed

- The validator gained eleven kit checks, including a prop-parity diff of the
  spine across every kit package. Each was watched failing against a planted
  defect before it landed.
- CI builds every kit in a matrix and asserts the build emitted something —
  `tsc` exits 0 when it compiles nothing.
- README's dependency-free promise gains its one honest caveat: the kits are
  code, they are not installed, and they appear only when asked for by name.

### Notes

- **The kits are not installed with the skill.** They ship in the npm package
  and are copied out on demand (`ADR-0002`), which is how the installed skill
  stays documentation while still having real components to hand.
- The live `/design-sync` push is a human step: the skill carries
  `disable-model-invocation`, so only a person typing the command can start it.
  Structure, build and materialization are proven; the upload is not yet proven
  in anger.

## [1.6.0] - 2026-08-05

The harvest of a 41-skill audit of the design skills installed on this machine.
The finding was narrow and repeated everywhere: the skill specified *what a
thing looks like* with real rigour and left *how much, how fast, and whether at
all* to whoever happened to be typing. Three of those four are now numeric, and
two of them are checked by a script.

Landed on top of 1.5.0, which shipped the `field-notes` pack from a concurrent
run in the same working copy. That pack was already written against the widened
contract below, so the two runs converged rather than collided — it is the first
and so far only pack on the thirteen-heading contract.

### Added

- **`MOTION_DOCTRINE.md`** — the missing half of the motion story.
  `SHELEG_DESIGN.md` says how motion is built; this says whether to build it.
  Frequency decides first, and it overrules taste: anything a user meets a
  hundred times a day does not animate, ever. Then the easing tree with
  `ease-in` banned in UI and the reason stated, three named curves, a duration
  table with a 300 ms ceiling, springs in Apple's notation, and interruptibility
  as the actual argument for reaching for one. Then the forms that are defects
  rather than preferences — scroll listeners, continuous input held in component
  state, blur and grain on scrolling containers, easing under `scrub`,
  `useEffect` where `useGSAP` belongs, and layout transforms silently erased by
  animated ones. Closes on anti-drift: the tokens are right and the built page is
  generic anyway, which happens at application time and so is named there.

- **Three calibration dials** — `DESIGN_VARIANCE`, `MOTION_INTENSITY`,
  `VISUAL_DENSITY`, baseline `7 / 5 / 4`, read off the brief from a table. A
  pack answers *which register*; it never answered *how far*, which is how a
  regulated insurer and a design studio came out of one pack looking alike. The
  dials are deliberately weak where the pack is strong: no dial invents a
  colour, a face or a radius, and `MOTION_INTENSITY` sits **under** the
  frequency table rather than over it.

- **A widened pack contract — nine headings to thirteen.** `Components`,
  `Hero`, `Responsive` and `Signature element`. The packs were precise about
  colour and motion and then went quiet exactly where implementations drift:
  per-component states, the opening viewport, collapse behaviour, and the one
  element a page is remembered by. The skeleton also now teaches concentric
  radius arithmetic, a `Not for` line in `Register`, and that an origin nobody
  can re-read is decorative.

- **`test/validate_palette.py`** — the colour part is computable, so it is
  computed. Claimed contrast ratios are re-derived from the hex and compared,
  WCAG floors are enforced, and semantic colours are checked for separation in
  OKLab under protanopia, deuteranopia and tritanopia. A pack may sit under the
  floor only if it states out loud that colour is never the only carrier.

- **`test/sloplint.py`** — the skill is held to its own bans. The token layers
  and every fenced example are read for `100vh`, scroll listeners, bare
  `ease-in`, transitions on layout properties and pure black fields; and the
  tables the docs promise are asserted by string, so a rule cannot be deleted
  without failing the build. Both scripts ship a `--self-test` that watches every
  check fail against a planted defect — a green from a check nobody has seen say
  no is not evidence.

- **A six-layer scene depth model**, a **parameter handoff to the built-in
  `dataviz` skill** instead of duplicating it, and a **`?variant=` procedure**
  for choosing between packs by mounting them on a populated page rather than
  arguing about them.

- **The three generated looks that are defaults rather than decisions** —
  recorded so a page that lands on one has to say whether that was a measurement
  or the default talking.

### Changed

- **The pack section gate is all-or-nothing.** The nine original headings stay
  required; adopt one of the widened four and all four are owed. The six packs
  that shipped before the widening stay valid on nine — backfilling them
  honestly needs re-reading each live reference, and three record a product name
  where an address belongs, so they cannot be re-read at all. Filling those
  sections from the token layer instead would be inventing values with a
  citation attached, which is the failure the pack layer exists to prevent. The
  rule closes the gap either way: no pack can be half-widened, so a new pack
  cannot copy the thirteen-heading skeleton, keep the cheap nine and pass.
- `npm test` now runs three gates, not one. `npm run selftest` runs the planted
  defects.
- `package.json` described "three locked style packs" while six shipped.

### Not shipped, deliberately

- **An eighth `industrial-brutalist` pack.** The register is real and the set
  lacks it, but the only description available carries a synthesised palette,
  not one measured off a production site. Held rather than authored.
- **A backfill of the six existing packs onto the widened contract.** Same
  reason, from the other direction: three of them cannot be re-read.

## [1.5.0] - 2026-08-04

The register the skill was missing for its own audience: a developer tool that
does not live on a dark console. Six packs could dress a landing page, a
dashboard, a deck and two kinds of consumer health, and none of them had an
answer for open-source software sold on *being checkable* — which is most of
the software the people using this skill actually build.

### Added

- **Seventh style pack: `field-notes`** — extracted from **graphify.com**
  (2026) by reading its live computed styles: 92 declared custom properties,
  the served `@font-face` set, every authored rule pulled out of the CSSOM, and
  a contrast pass over all 38 colour pairs in the system. Warm off-white paper
  with a green cast (`#F8F7F0`), near-black green-cast ink (`#16211B`, 15.4:1),
  one rust accent (`#9A3F28`), and a complete dark twin.

  Its defining composition is what separates it from every warm pack already
  here: **the page is one continuous sheet ruled by a `1px` hairline.** Ten of
  the reference's sixteen sections are divided by nothing but that line; three
  add a 40% wash. Where `orchard` stacks discrete slabs and `atrium` runs a
  continuous field that changes layout, this one draws a rule and keeps going.

  The hero is the other half of the idea: not a dark band but a **dawn** —
  eight stops from `#062A22` to the exact paper colour, so the dark has no
  edge. Over it, an inline `feTurbulence` grain at `baseFrequency 0.82`, a
  radial vignette, and an ambient layer that is **notation rather than
  particles**: mathematical glyphs at 14% opacity, one at a time flipping to
  the verified hue.

  It also carries the two devices most worth stealing. **The numbered eyebrow**
  — `〉 HOW IT WORKS [03/09]`, built from `::before`/`::after` on a `data-n`
  attribute — makes a marketing page into a document with a table of contents.
  And **printer's crop marks** at the four corners: eight 1px gradient arms,
  `inset: 14px`, ink at 30%, desktop only. Both cost nothing and both state the
  thesis that the page is a printed record.

  Elevation is a **ring** (`0 0 0 1px var(--line)`), not a shadow; radii are a
  proportional ramp off one `--radius`, so a hardcoded `12px` is banned; and
  motion is two eases doing two jobs — `.15s` `cubic-bezier(.4,0,.2,1)` for
  control state, `.5s` `cubic-bezier(.22,1,.36,1)` for scroll entry — with one
  rule on top: **only the verified hue ever animates colour.** The rust never
  moves, because a brand that animates stops reading as an identity and starts
  reading as a status.

  Four corrections to the reference ship with it, each measured. Its hero
  accent phrase — the single most prominent piece of text on the site — runs
  the light brand over the gradient at **2.29:1** at the top and **1.41:1** in
  the middle; the pack adds `--brand-on-dark` `#CF7A52` (**4.82:1**) and bans
  the other. Its `--verify` green is 3.2:1 on paper and its own
  `--verify-foreground: #fff` is 3.4:1 on the green, so both are fills and the
  labels take `-ink`. It sets `color-scheme` nowhere despite a complete dark
  theme — the same trap that bit `workbench`. And it paints three unrelated
  dark palettes (warm-brown theme, forest bands, navy terminal) plus an app
  layer whose neutrals drift browner than its page layer and whose ring is a
  violet used nowhere else; the pack reconciles all of it to the forest family
  and the page's own neutrals.

  The pack ships that app layer deliberately, with a routing rule rather than a
  turf war: `workbench` stays the default for neutral product UI, which should
  disappear; `field-notes` is for a product whose console must read as the same
  paper as its site.

- **`AI_PRODUCT_PATTERNS.md` gains the provenance pattern** (§4), promoted out
  of the pack because it is the reference's one genuinely transferable
  invention and a direct extension of the file's existing *honest state* rule:
  **label the part, not the whole.** A single confidence number on a mixed
  answer hides exactly the clause the reader needed to check, so the pattern
  attaches a small set of named states — `[EXTRACTED]` · `[INFERRED]` ·
  `[AMBIGUOUS]` — inline to the span each one qualifies, with three tests for
  whether it is honest: every state must be reachable, every label must derive
  from something real, and if you cannot say which words a state covers you do
  not know it well enough to show it. Any pack can implement it on three hues.

- **Test scenario T13** — the developer register **and** the fork against
  `instrument-console`, run as two prompts in separate contexts. The pack is
  only worth its row if an agent can tell "this product has a source" from
  "this product has a dial", so a pass requires both branches: one that must
  select `field-notes`, one that must stay on the dark console.

### Changed

- `SKILL.md`, `README.md`, `bin/cli.js`, `install.sh` and the Cursor rule all
  learn the seventh pack; the CLI's help and the README's file table stop
  saying "six".

## [1.4.0] - 2026-08-03

Two packs for the warm consumer register, extracted from two production sites
that solve the same brief in opposite ways — one premium and editorial, one
friendly and modular. Between them they replace the reflex a generated wellness
page falls into (a gradient, three cards, a stock photo of someone stretching).

### Added

- **Fifth style pack: `atrium`** — the warm consumer register, extracted from
  **functionhealth.com** (2026) by reading its live token layer and computed
  styles. The skill could already do dark-technical, editorial, product UI and
  decks; it had no answer for *premium consumer health* — the page that has to
  land a serious clinical claim without a sterile surface anywhere on it.

  What it encodes: **one continuous cream field with no dark bands** (sections
  are separated by a 48→99px rhythm and a change of layout, never by flipping
  the background — the reflex that makes generated pages read as a stack of
  slabs); a single terracotta accent `#B05A36`; a serif that ships **one
  weight, 300**, set at `line-height: 0.9`, whose entire emphasis vocabulary is
  *one italic accent phrase* per heading; a sans with only 300 and 600 in it;
  mono reserved for exactly one component; a fully fluid `clamp()` scale keyed
  to a single 23.5rem→90rem band, so the page resizes as one object; hairline
  and cream-on-cream steps instead of shadows, with three shadows that each
  have one job; and `999px` on everything clickable.

  Its signature motif is the **fluted-glass hero**: a WebGL shader refracting
  photography through reeded-glass ribs, shipped with the real numbers (82.8
  ribs at `0.36rad`, amplitude `0.0255`, feather `0.63`, a 7.2s reveal cycle,
  the ink scrim at 70%) over a still-image fallback. Its lifecycle is the pack's
  most useful lesson: context-lost, tab-hidden, reduced-motion and no-WebGL are
  four branches that ship in the same commit as the effect.

  It also promotes something the reference does that most sites do not: **every
  autonomous motion carries a visible `PAUSE MOTION` control**, and the pack
  bans shipping one without it — `prefers-reduced-motion` alone does not
  discharge the obligation.

  Three measured contrast traps are carried as Gotchas rather than left for an
  audit: the accent is AA on the field (4.6:1) but **fails on the cream surface**
  (4.2:1); `--good`/`--info` are fills at 2.1:1 and 3.4:1 and may never be text;
  and the hairline is 1.6:1 — decorative strength, not affordance strength, so
  controls need `--line-strong`, `--line-ink` or `--accent` instead.
- **Sixth style pack: `orchard`** — the same buyer, the opposite voice,
  extracted from **gutgutgoose.com** (2026). Where `atrium` is one continuous
  field, `orchard` is **a stack of rounded slabs**: every section is a card with
  its own fill (oat, sage, cacao), no two adjacent slabs repeat, and the field
  shows around all of them. Its whole layout rhythm is four numbers — `64px 24px`
  slab padding, `44px` between blocks, `55px` between slabs, `36px` card padding.

  Three colours with fixed jobs — oat is the paper, sage is the brand, candy
  orange is the verb — and the pack's most useful rule is that **two of them are
  not text colours**. A rounded geometric display at Medium carries all
  hierarchy, so body weight never goes above 500; the price is deliberately set
  in the body face, because a rounded display numeral reads as branding and a
  price has to read as a fact.

  Its signature material is **light, not shadow**: the "candy pill" is a flat
  fill wearing two inset white hairlines (`.8` top, `.35` bottom) plus an
  ambient glow **in the button's own hue** — the only real drop shadow in the
  system. Its one cinematic move is a **word-by-word scrubbed headline** (opacity
  only, ~12% of hero scroll per word) beside a sticky visual column, and that is
  the entire motion budget.

  The reference is strong on composition and weak on contrast, so the pack
  carries the three measured failures with fixes from inside its own palette:
  the CTA label is **2.8:1** (white on orange) and must use the cacao ink for
  **5.6:1**; body copy on the sage slab is **3.4:1** — and oat on sage is
  **2.96:1**, under even the large-text floor — so small text moves to
  `--primary-deep` at **4.9:1**; and the 60% ink is **4.1:1** on oat, a caption
  colour only. It also ships the `prefers-reduced-motion` branch the reference
  has nowhere on the site.
- `scenarios.md` gains T11 and T12 for the two consumer registers.

### Changed

- README, `SKILL.md`, `bin/cli.js`, `install.sh` and the standalone Cursor rule
  route and ship both new packs; the stale "three style packs" counts in the
  README are corrected to six, and the Cursor rule — which had listed only three
  packs and never gained `briefing-room` — now names all six.

## [1.3.4] - 2026-07-30

### Added

- **`displayName`** ("SHELEG Design") in both manifests — the `/plugin` picker
  falls back to `name`, which is kebab-case for namespacing reasons.

## [1.3.3] - 2026-07-30

### Fixed
- **`argument-hint` in the slash command was unquoted.** In YAML a bare
  `[a | b]` is a flow sequence, not a string, so the hint parsed as a *list*.
  Found by `claude plugin validate --strict`, the upstream schema checker, which
  now runs in CI on both this plugin and its marketplace manifest.
- **`homepage` and `repository` sat at the top level of `marketplace.json`,
  where Claude Code does not recognize them.** They are plugin-entry fields;
  moved there, so the values reach the plugin listing instead of being ignored.

## [1.3.2] - 2026-07-30

### Changed

- **The licence is declared in both manifests** — SPDX `license: MIT` in the
  `marketplace.json` plugin entry and in the skill's front matter (mirrored into
  the `.cursor` copy, which the validator holds byte-identical). The `LICENSE`
  file was always present and visible on neither surface a user actually reads.

## [1.3.1] - 2026-07-30

### Changed

- **README** — the family list gained `agent-sync`, and the install block now
  carries all three family commands (`install`, `update`, `list`) with the
  restart note; skills and hooks load at session start, so the session that
  updates is not the session that gets the new ones. The registry copy of the
  README is what most people read, and it only moves on a release.
- `CONTRIBUTING.md` — how to run `test/validate.py` and what a PR is checked
  against.

## [1.3.0] - 2026-07-29

### Added

- **Fourth style pack: `briefing-room`** — a register the skill had no answer
  for. Decks are among the most-requested things people ask an agent to build,
  and the default output is bullet lists on a gradient. Extracted from a
  production investor-deck site (2026) by reading its live token layer; the
  source is **anonymized at the owner's request**, so the `Origin:` line says
  what it is without naming it — the values are still extracted rather than
  invented, which is the point of the rule.

  What it encodes: a fixed **1280×720 canvas with `overflow: hidden`** (content
  that does not fit becomes a second slide — never a smaller type ramp); the
  first **OKLCH** token layer in the skill, where every neutral is the accent
  hue `254` starved of chroma, so the palette cannot drift into two designs;
  Inter at tight optical tracking against JetBrains Mono furniture at `+0.14em`
  to `+0.18em`; a two-part veil that protects text over artwork **without**
  fading the artwork; 1-bit dithered art as the only imagery; mono numbered
  section headers; **the slide title is a claim, not a label**; one bespoke
  diagram per slide instead of bullets; exactly one highlighted phrase per
  deck; and every number carrying its source.

  Its motion position is a deliberate inversion of the rest of the skill:
  **slides never animate**, because the presenter's voice is the timeline.
  `prefers-reduced-motion` is a no-op by construction rather than by neglect.

  Two honest notes carried as Gotchas: a fixed canvas fails *silently* (clipped
  content is invisible in review and obvious in the room), and the reference
  shipped no print or reduced-motion branch — the pack requires both.
- `scenarios.md` gains T10 for the deck register. Gate: 194 → 220 checks.

## [1.2.0] - 2026-07-29

Worked through Figma's *State of the Designer 2026* (NewtonX, 906 digital
designers across five regions, surveyed September–October 2025). It is a survey
of the profession — AI adoption, what designers mean by craft, satisfaction,
regional outlook — **not** a visual-trends report, so nothing here is a "trend"
invented from it. Two findings were actionable, and one was a gap in this skill.

### Added

- **`AI_PRODUCT_PATTERNS.md`** — the surfaces a model drives, which the skill
  had nothing to say about while the survey ranks *designing AI-driven
  products* the **third most in-demand skill (37%)**, ahead of motion design
  (29%) and information architecture (19%). Organizing rule: **honest state**.

  Contents: the five states of a model call (idle · working · complete ·
  refused/needs-a-human · failed — a refusal is not an error and a rate limit
  is not a crash); streaming instead of spinners, with a stop control from the
  first frame, a reserved container and no fake typing delay; latency as two
  numbers (time-to-first-token is the one users feel); provenance and
  uncertainty (cite or don't claim, no confidence theater, show the context the
  model actually used); agent actions where the confirmation *is* the design —
  the diff/recipient/query shown before it runs, explicit consent for anything
  irreversible or outward-facing, undo for what's cheap; empty states that
  carry the capability; chat as a shape rather than the shape; cost and scope
  as visible state; and a ban list. Pairs with `workbench` and reuses its
  status tokens.
- **The craft bar** in `SKILL.md` — a definition of done ordered by what
  designers actually mean by craft in that survey: visual polish (58%),
  thoughtful problem solving (47%), clear intuitive UX (36%), emotion and
  delight (35%), consistency (15%). Item 3 is explicitly *not* this skill's
  half — if flows and states aren't decided, the honest move is to stop.
- Discovery, the Cursor rule, the README and both installers cover the AI-UI
  direction; `scenarios.md` gains T9.

### Fixed

- **The validator enforced five of the nine required pack headings** while the
  0.9.0 entry, `CONTRIBUTING.md`, the README and the wiki all claimed the full
  contract was gated. Exactly the promise-without-a-check defect this repo
  keeps hunting, living inside the checker itself. All nine are now enforced
  (`Motion flavor` stays conditional — `workbench` is standalone and has no
  motion layer to flavor), which is also why the check count jumps to 194.

## [1.1.1] - 2026-07-29

### Fixed

- `FIGMA_BRIDGE.md` described the mapping without mentioning that the official
  Figma MCP **gates its main tools behind guidance skills** (`/figma-use`
  before `use_figma`, `/figma-create-new-file` before `create_new_file`,
  `/figma-design-to-code` before `get_design_context`) — the server names
  skipping them the cause of hard-to-debug failures. An agent following the
  bridge alone would have called them bare. The doc now says to load the gate
  first and that the server's instructions win on *how* to call anything; this
  file is the contract, not a tool manual. It also names the two read paths
  worth knowing: `get_variable_defs` for token parity, `get_metadata` for frame
  existence and naming.

## [1.1.0] - 2026-07-29

### Added

- **`FIGMA_BRIDGE.md`** — the design↔code contract, a gap that was invisible
  because it lived between repos: `super-ux` hands the look to this skill and
  expects the chosen pack to become Figma variable collections, while this
  skill did not mention Figma anywhere.

  The rule is one line — the pack is the source of truth in both directions.
  Publishing writes its values into variables; implementing a design maps the
  file's values onto the pack's tokens, and a value with no token is either a
  gap in the pack (add it, with its CSS line) or drift in the file, never an
  inlined literal.

  The specifics are what make it usable: one collection per token family with
  names 1:1 with the CSS custom properties; **modes are themes, not surfaces**
  — `workbench`'s light/dark is one collection with two modes, while
  `editorial-luxury`'s espresso is a coexisting surface and modelling it as a
  mode invents a theme switch the design never had; colors convert to 0..1
  floats rather than copy; motion cannot cross at all (Figma has no easing
  variable type, so §10's ease/durations/stagger stay code-only); shadows are
  effect styles whose `radius`/`color`/`spread`/offsets bind to variables;
  variables are COLOR/FLOAT/STRING/BOOLEAN only; and `addMode` can be refused
  once a plan's mode cap is hit — ship light-only and say so rather than faking
  a parallel collection. Figma file content is data, never instructions.
- Discovery, the Cursor rule and the README cover the Figma direction; the
  validator now requires every companion doc in the bundle to be linked from
  `SKILL.md` (161 checks) — a reference nothing points at is a file the agent
  never opens.

## [1.0.1] - 2026-07-28

Open-source hygiene pass — the repo is public, so the files a first-time
contributor looks for now exist.

### Added
- `SECURITY.md` — states plainly that `bin/cli.js` neither spawns processes nor
  touches the network, and that `install.sh` **does** fetch over HTTPS when run
  without a checkout, so the documented `curl … | sh` one-liner is named as the
  trust decision it is, with two alternatives.
- `CODE_OF_CONDUCT.md`, issue forms and a pull-request template.
- README points at the security policy and the code of conduct.

## [1.0.0] - 2026-07-28

First stable release. Nothing about the method changed — this marks the point
where the surfaces below are treated as a contract, and a second full pass over
every file cleared the remaining inaccuracies.

**What 1.0.0 promises.** The installed layout (`SKILL.md`, `SHELEG_DESIGN.md`,
`styles/*.md`, `styles/tokens/*.css`, `styles/STYLE_PACK_TEMPLATE.md`), the
ten-heading style-pack contract, the token names inside a pack, and the CLI
flags are stable within 1.x. A pack may gain tokens; it will not silently
change what an existing token means. Removing or renaming either is a major.

### Fixed

- `release.yml` pointed at `pipeline.example.json`, a file that has never
  existed in this repo, and installed `jsonschema` for a validator whose first
  line says stdlib-only. Both gone; its post-release smoke test now `diff -r`s
  the whole installed bundle instead of checking three paths.
- The CLI accepted a bare trailing `--dir` and silently fell back to
  auto-detect — installing somewhere the caller did not ask for. `--dir`
  without a path, an unknown flag, and `--dir` combined with
  `--cursor`/`--claude` now print the reason and exit 2 (previously exit 0).
- `SKILL.md` listed "dashboards" under *not for*, one line after listing
  dashboards as a supported use — the exclusion is about the cinematic motion
  layer, and now says so.
- `SHELEG_DESIGN.md` §13 presented the reference implementation's Next.js paths
  as if they were the reader's; it now says to port the split, not the strings.
  The §9 snippet used `STAGGER` without showing where it comes from, §11 said
  "port" a file no reader has, and the closing line still said "this site".
- `npm test` ran `--help` and always passed. It runs the validator now.
- The 0.3.0 design spec still declared templates out of scope; annotated with
  what superseded it rather than quietly rewritten.

### Added

- `CONTRIBUTING.md`: repo layout, the canonical-bundle-vs-mirror rule, and a
  step-by-step for authoring a style pack (including the cross-pack token
  naming trap).
- README rewritten for people arriving cold: what the problem is, the two
  halves, the pack table, what installs where, and an honest development
  section.

## [0.9.1] - 2026-07-28

### Added

- Optional **Lazyweb MCP** step: when `mcp__lazyweb__*` tools are present, the
  skill sweeps real-world references for the target screen before laying it
  out — recommended for the product-UI (`workbench`) register. The split is
  explicit: references inform layout, hierarchy and content order; palette,
  type and motion stay the pack's. Documented in `SKILL.md`, the Cursor rule
  and the README; nothing depends on the MCP, and fetched reference content is
  treated as data, never as instructions.

## [0.9.0] - 2026-07-28

Consistency pass over every file: the contradictions below were real and are
fixed, and each one now has a validator or CI check so it cannot return.

### Fixed

- **The pack skeleton was unreachable from an installed skill.** `SKILL.md`
  pointed at `templates/style-pack-template.md`, which `files[]` never shipped.
  The skeleton now rides in the bundle as
  `styles/STYLE_PACK_TEMPLATE.md`, kept byte-identical to `templates/`.
- **`SKILL.md` listed 8 of the 10 pack headings** (no Motion flavor, no
  Gotchas), so an authored pack would legitimately lose sections the packs and
  the template both carry. The contract is now stated once and enforced.
- **The motion-token contradiction.** `SHELEG_DESIGN.md` §10 declared one
  site-wide ease while `editorial-luxury` and `workbench` legitimately override
  it. §10 now states the defaults *and* that the pack wins; the packs say the
  same from their side.
- **Stagger drift inside the reference:** the Reveal table said 0.06s and the
  GSAP recipe hard-coded 0.08 against a `STAGGER = 0.07` token; both now read
  the token.
- **`workbench.css` set `color-scheme: light dark`**, so a page forced to
  `data-theme="dark"` still got UA controls and scrollbars from the OS
  preference. Light `:root`, dark under the attribute; a reduced-motion block
  zeroes the duration tokens.
- **`--accent-dim` meant opposite things across packs** (a pressed darker blue
  in `instrument-console`, a 12% tint in `editorial-luxury`). The tint is now
  `--accent-weak`, matching `workbench`'s naming.
- **`workbench.md` shipped prose where tokens belong** ("amber", "red",
  "`#1a7f37`-family") — the table now carries the exact light/dark pairs from
  the CSS, and `--info` is documented as deliberately the accent hue.
- **CLI help still advertised two style packs** (the success message had been
  fixed, the help text had not), and the bundle blurb omitted the token CSS.
- **The Cursor rule promised product-UI guidance it never gave** — it now
  carries a self-contained workbench contract for agents without the skill
  installed.
- README, `marketplace.json`, and the `/sheleg-design` command all described a
  landing-page-only skill; all three now state the product-UI half.
- Reference cleanups: ASCII architecture diagram re-aligned (the fan-out
  connector was one column off the store box), `bias` added to the store
  fields it lists, the `936 = 24 × 13 × 3` factorization disambiguated from
  scene indices, and a product-specific closing-line example genericized.

### Added

- Validator (146 checks, was 101): the **whole** `.cursor/` mirror is compared
  against the plugin bundle file-by-file in both directions (previously only
  `SKILL.md`), the full ten-heading pack contract is enforced on every pack and
  on the template, the shipped template must match `templates/`, and every pack
  must be routed from the `SKILL.md` table and named in the CLI output.
- CI installs through both channels and `diff -r`s the result against the
  bundle, so a file that reaches one installer and not the other fails the run.
- `test/scenarios.md` gains T7 (authoring a new pack against the contract).

## [0.8.0] - 2026-07-28

### Fixed
- The Cursor channel copy of `SKILL.md` could drift from the plugin copy without
  anything noticing. The validator now compares them and fails on drift.

### Changed
- `RU triggers - …` replaced with English-first pairs
  (`"design tokens" / "дизайн-токены"`), so the description reads as English
  with localized aliases.
- README is English-only, with a plain statement of what the skill gives you and
  an author/links block.

### Added
- Validator enforces the description canon: `Use when` opening, Russian trigger
  aliases present, front-matter under 1024 characters.

## [0.7.0] - 2026-07-25

Review pass.

- **FIX: `SHELEG_DESIGN.md` pointed at a non-existent `DESIGN.md`** and hard-coded
  the instrument-console palette in the build recipe, contradicting the
  style-agnostic method — §11 now says to implement the chosen style pack's tokens.
- **Toggleable release automation** (`.github/workflows/release.yml`, off unless
  `RELEASE_ENABLED` is set): the repo shipped 0.2.0–0.6.0 with no tags and no
  GitHub releases.
- README gains a Russian section; `package.json` `files[]` ships `CHANGELOG.md`;
  a stray untracked `.claude/skills/sheleg-design` plain copy was removed and
  `.claude/` gitignored (it shadowed the plugin).

## [0.6.0] - 2026-07-20

### Added

- Ready-made token layers `styles/tokens/<pack>.css` for all three packs
  (copy verbatim instead of transcribing tables; workbench ships light +
  `data-theme="dark"` twins). Validator requires a tokens file per pack.
- Motion-flavor sections in the cinematic packs (particle tint/energy,
  Reveal set, instrument styling per style).
- Versioned release test scenarios (`test/scenarios.md`, T1–T6) encoding
  the RED/GREEN history.
- Validator installer-sync check (every bundle file shipped by install.sh;
  npx CLI now walks the bundle at runtime — adding a pack no longer
  touches installers) and a CI negative self-test (validator must FAIL on
  a corrupted version).
- Style-pack authoring skeleton `templates/style-pack-template.md`;
  `/sheleg-design` accepts a pack name argument.

### Fixed

- Discovery gap: skill description (and Cursor rule) now trigger on
  product-UI tasks — dashboards, admin tools, design tokens, light/dark
  themes (EN + RU) — previously such tasks never loaded the skill.
- Stale manifests: package.json / marketplace / plugin descriptions and
  the Cursor rule now mention style packs incl. workbench.

## [0.5.0] - 2026-07-20

### Added

- **`workbench` style pack** — quiet light+dark utilitarian product UI for
  dashboards, admin panels, and internal/dev tools: neutral grays, borders
  as elevation, one functional blue accent, system + mono type, canonical
  atoms (status dot, chip, stat tile, sparkline), honest-state and
  glanceability rules. Blended from the Builder Pro AI production design
  system and GitHub-style border discipline. Usable standalone — SKILL.md
  now routes dashboard/tool requests to this pack instead of excluding
  them outright.

## [0.4.0] - 2026-07-19

### Added

- **Style packs** (`styles/`): the motion methodology is now style-agnostic
  and pairs with a chosen visual identity pack. Two packs ship:
  `instrument-console` (near-black aerospace console, electric-blue signal
  — the original reference style) and `editorial-luxury` (warm cream +
  espresso + sage, Fraunces/Newsreader/JetBrains Mono, dossier motifs —
  extracted from the prowl.chat production design system). Each pack locks
  palette/type/texture/motion tokens, signature motifs, and bans; SKILL.md
  documents the pack contract for authoring new styles.
- Installers (npx CLI, install.sh) ship the `styles/` directory; validator
  enforces >=2 packs with required sections.

## [0.3.0] - 2026-07-19

### Added

- Claude Code marketplace layout: `.claude-plugin/marketplace.json` +
  `plugins/sheleg-design/` (plugin.json, `/sheleg-design` command, skill).
  Installable via `/plugin marketplace add ssheleg/sheleg-design-skill` and
  discoverable by the vercel-labs `skills` CLI.
- Cursor rule `cursor/rules/sheleg-design.mdc` (self-contained, no relative
  links).
- Repo consistency validator `test/validate.py` + GitHub Actions CI
  (`validate.yml`: validator, `node --check`, CLI smoke test).
- POSIX fallback installer `install.sh` (local checkout / curl / wget).
- Russian trigger phrases in the skill description.

### Changed

- Skill bundle moved from `skill/` to
  `plugins/sheleg-design/skills/sheleg-design/`; the npx installer copies
  from the new location (installed layout unchanged).

## [0.2.0] - 2026-07-19

### Changed

- SKILL.md reworked to skill-authoring canon: trigger-only description
  (no workflow summary), canonical sections (Overview / When to Use / Core
  Pattern / How to Apply / Quick Reference / Common Mistakes), ~590 words,
  explicit REQUIRED REFERENCE pointer to SHELEG_DESIGN.md.
- Reference doc genericized (removed source-repo-specific `v2` paths).
- Verified with subagent scenarios (trigger, application, retrieval) before
  and after the rewrite.

## [0.1.0] - 2026-06-11

### Added

- Initial release: SKILL.md + SHELEG_DESIGN.md bundle and the zero-dependency
  `npx sheleg-design-skill` installer (auto-detect `.cursor`/`.claude`,
  `--cursor`, `--claude`, `--dir`, `--force`).
