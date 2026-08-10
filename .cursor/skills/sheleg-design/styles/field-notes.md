# Style pack — Field Notes

Origin: **graphify.com** (2026), the marketing site of an open-source code
knowledge-graph tool. Every value below was read off its live computed styles
on 2026-08-04. A warm off-white sheet with a green cast, near-black green-cast
ink, one rust accent, a grotesque display face with no italic in it, Geist and
Geist Mono doing the annotation, printer's crop marks at the corners, and a
hero that is not a dark band but a **dawn** — eight stops resolving into the
same paper the rest of the page is printed on.

The identity in one sentence: **an engineer's notes, published.** Not a
cockpit, not a brochure — a document with numbered sections, marked-up sources,
and trim marks showing where it was cut.

Contract: widened — all thirteen headings.

## Register

Choose this pack for **an open-source or developer product sold on
auditability rather than power**: code intelligence, observability with a
lineage story, data provenance, evaluation and benchmarking tools, security
tooling that has to show its work, agent memory. It suits a product whose
argument is *here is where this answer came from* — where a dark console would
make the reader trust the instrument instead of reading the evidence.

It is used **standalone**, like `workbench` and `briefing-room`. The reference
carries no GSAP, Framer, Three or Lenis; its motion is CSS keyframes and one
`.reveal` transition, all of it behind `prefers-reduced-motion`. You may ride
the SHELEG cinematic layer with it — see *Motion flavor* — but nothing here
depends on it.

**The fork against `instrument-console`, which is the one people get wrong.**
Both serve technical products. Ask what the product *is*: if it has a dial, a
stream, a live state that changes while you watch — telemetry, infrastructure,
a control plane — use `instrument-console`, whose dark field and one electric
signal exist to make a changing value readable. If the product has a **source** —
if its output is a claim that has to be traceable — use this one. A cockpit
answers *what is happening now*; field notes answer *how do you know*.

**Against `workbench`.** Both ship an app layer and both use borders rather
than shadows for elevation. `workbench` is neutral grey and is *supposed to
disappear* — internal tooling should have no voice. `field-notes` is warm and
has one. Route by whether the console is part of the brand: a generic admin
panel takes `workbench`; a product whose console must read as the same paper as
its marketing site takes this pack's app layer.

**Against `editorial-luxury`.** Both are warm and light. `editorial-luxury` is
a serif dossier selling prestige; this is a sans-and-mono lab notebook selling
proof.

**Against [`blueprint`](./blueprint.md).** Both draw rules on a light field, both
annotate in mono, both serve readers who scroll to the technical section first.
The difference is the stock and what the marks mean. This pack is **warm paper**:
a green-cast off-white, rust ink, crop marks that say *this was printed and
trimmed* — and its argument is provenance. `blueprint` is **cold stock**: pure
white, electric blue, registration marks that say *this was drawn to tolerance* —
and its argument is precision. *How do you know?* stays here. *How is it built?*
goes there.

The defining constraint is composition: **the page is one continuous sheet with
rules drawn on it.** Ten of the reference's sixteen sections are separated by a
single `1px` hairline and nothing else; three add a wash of `--surface-2` at
40% opacity. Set against the skill's other light packs: `orchard` stacks
discrete slabs with the field showing between them, `atrium` runs a continuous
field and changes layout instead, and this one draws a line.

## Palette

Ready-made token layer: [`tokens/field-notes.css`](./tokens/field-notes.css) —
copy it verbatim instead of transcribing this table.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#F8F7F0` | the paper — warm off-white, green cast | — |
| `--surface` | `#FDFCF6` | card and popover, a lighter sheet | — |
| `--surface-2` / `-3` | `#EDEEE2` / `#E8EBDD` | the section wash (used at 40% / 20%) · the deepest step | — |
| `--line` | `#E0E2D3` | **the hairline that does the composition** | 1.2:1 — a rule, not text |
| `--ink` | `#16211B` | near-black with a green cast, not a true black | **15.4:1** |
| `--ink-soft` | `#626B60` | captions, eyebrows, secondary copy | **5.2:1 — passes AA** |
| `--brand` | `#9A3F28` | rust — the accent, safe as text **on paper** | **6.3:1** |
| `--brand-ink` / `-soft` | `#8F3F1F` / `#E8CBB8` | the text-safe rust / the rust wash | 6.8:1 |
| `--brand-on-dark` | `#CF7A52` | the brand **on any dark surface** — see Gotchas | 4.8:1 on `--dawn-1` |
| `--verify` | `#0E9E76` | provenance: extracted. A **fill**, never text | 3.2:1 |
| `--verify-ink` / `-soft` | `#0A7558` / `#D6F1E7` | the label / the wash | **5.3:1** |
| `--witness` | `#B3402A` | provenance: ambiguous | 5.3:1 |
| `--witness-ink` / `-soft` | `#9A3016` / `#F4DED4` | the label / the wash | **7.0:1** |
| `--danger` | `#C0442E` | destructive — kept distinct from `--witness` | 4.8:1 |
| `--deep` / `-2` / `-3` | `#072820` / `#0B332A` / `#041D17` | one dark family, every member **bounded**: the dawn's darkest step · terminal header · terminal body — see Gotchas | — |

Three rules carry this palette:

- **`--ink-soft` is a real body colour here, and that is unusual.** At 5.2:1 it
  clears AA, so secondary copy does not have to be promoted to full ink the way
  it does in `orchard`. Use it as intended — the whole page reads quieter for it.
- **`--verify` is a fill and `--brand` is a text colour, and they are not
  interchangeable.** Green at 3.2:1 may hold a dot, a bar, a chart series or a
  40px number; the rust at 6.3:1 may hold a sentence. Swapping them is the most
  common way this palette degrades.
- **The neutrals are green-cast and the ink is not black.** `#16211B` beside a
  cool `#18181B` or a true `#000` reads instantly as a component from another
  kit. So does a pure `#FFF` card on this paper.

Three semantic hues and no fourth: rust is the brand, green is *verified*, red-
orange is *unverified*. A fourth hue means one of them stopped meaning
something.

## Type

Three families, each doing one job:

- **Display — Bricolage Grotesque at 600** (400 for a deliberately quieter
  heading). Variable upstream (`opsz 12..96`, `wdth 75..100`, `wght 200..800`),
  SIL OFL. **It has no italic** — see Bans. Substitutes with the same
  slightly-irregular grotesque voice and a real 600: Archivo, Space Grotesque,
  Darker Grotesque.
- **Body — Geist at 400** (600 for emphasis), variable, SIL OFL.
- **Annotation — Geist Mono at 400.** In this pack mono is **furniture, not
  data**: eyebrows, section numbers, version strings, the terminal, provenance
  tags. That inverts `workbench`, where mono means *this is a number*.

Scale, measured at 1280px:

| Token | px / line-height | Used for |
|---|---|---|
| `--t-hero` | 67.2 / 1.02 | the hero claim |
| `--t-h1` / `-h2` | 44 / 40 · 1.15 | section headings |
| `--t-h3` / `-h4` | 30 · 1.2 / 20 · 1.4 | sub-heads, step titles |
| `--t-h5` | 15 / 1.375 | card titles |
| `--t-lede` / `--t-body` / `--t-sm` | 18 · 1.556 / 16 · 1.5 / 14 | lede · body · UI |
| `--t-eyebrow` | 11 / **1.0** | the numbered eyebrow |
| `--t-tag` / `--t-mono` | 10 / 1.6 · 13 / 1.625 | provenance tag · terminal |

**Tracking is a constant `-0.025em` on every display size** — 67.2, 44, 40, 30,
20 and 15px all resolve to exactly that. One authored decision, not five; keep
it as one. Mono tracks positive instead: `0.16em` on eyebrows (`0.18em` on the
wide variant), `0.08em` on tags, `0.05em` on tab labels.

Measures: `--content-max` 1152px is the default column, `--prose-max` 672px for
long copy, `--lede-max` 448px for the hero paragraph, `--wide-max` 1400px for
figures, `--shell-max` 1920px for the hero and nav shell.

## Texture & surface

- **Elevation is a ring, not a shadow.** The system's dominant "shadow" is
  `0 0 0 1px var(--line)` — a hairline drawn *at* the edge. `--shadow-sm` and
  `--shadow-lg` exist for genuinely floating things, and there is exactly one
  deep shadow, `--shadow-float`, which is **warm** (`rgba(26,22,12,.45)`) rather
  than grey. A grey drop shadow anywhere in this pack reads as a foreign part.
- **Sections are ruled, not flipped.** `border-top: 1px solid var(--line)` plus
  `--section-pad-y` (64px at desktop, 16px below) is the entire section
  vocabulary. A wash of `--surface-2` at 40% marks a change of subject; nothing
  else does.
- **Radii are one root and a proportional ramp.** `--radius: .75rem`, and every
  other radius is a multiple: `×0.25` icon squares, `×0.6` chips and tags,
  `×0.8` inner blocks, `×1.0` cards and buttons, `×1.4` media wells, `×1.8` the
  largest panel, plus a pill for nav and the primary CTA. Change `--radius` and
  the whole page moves together — which is why a hardcoded `12px` is banned.
- **The dawn.** The hero is `--hero-dawn`: eight stops from `#062A22` to the
  paper colour itself, so the dark has no edge. Over it sit `--hero-vignette`
  (a radial pull to the headline's left third), `--grain` at `--grain-opacity`
  `0.06` (an inline `feTurbulence` at `baseFrequency 0.82`), and a field of
  mathematical and logical glyphs at `--sym-op` `0.14`.
- **Crop marks.** `position: absolute; inset: var(--crop-inset)` with eight
  1px linear-gradient arms of `--crop-len` at the four corners, ink at 30%,
  desktop only. Printer's registration marks: they cost nothing and they state
  the thesis.
- Spacing is an 8-based ramp; the two numbers that build the page are the
  **64px section padding** and the **1px rule** between sections.
- **Radius arithmetic when containers nest:** an inner radius is always
  *smaller* than its outer radius, never the same value twice — the same `12px`
  on both reads as two rectangles that happen to touch. This pack sets the step
  **proportionally**, not by subtraction: `tokens/field-notes.css` defines
  `--radius-sm: calc(var(--radius) * 0.6)`, so a tag at `--radius-sm` (7.2px)
  inside a card at `--radius-lg` (12px) is correct.
  *(Corrected 2026-08-10. This read "an inner radius is the outer radius minus
  the padding between them … `12 - 12 ≈ 7.2`". Subtraction gives 0, not 7.2, and
  the token layer never used subtraction — the rule, its worked example and the
  implementation were three different systems, and an agent applying the rule as
  written would have shipped square tags.)*

## Components

Measured off the reference unless a row says otherwise. Where it says
otherwise, the reference has no answer and the pack supplies one — a pack about
provenance does not get to invent a value and stay quiet about it.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Primary CTA** | pill, `--ink` fill · `--on-ink`, `8px 16px`, 14px/500; on the hero a white fill with `--dawn-1` ink | `opacity` shift over `--dur-ui` — the only property it transitions | no separate treatment | **pack decision:** `opacity: .5`, `cursor: not-allowed`; the reference ships a `cursor: default` button at full opacity, which is indistinguishable from enabled |
| **Secondary** | `--radius-lg`, `12px 20px`, 14px/600, `--bg` fill | `transform, background-color` over `--dur-ui` | — | as above |
| **Ghost (on the dawn)** | `--fill-on-deep`, `1px --line-on-deep-strong`, `--radius-lg`, `8px 14px`, 14px/400 | `color, background-color` over `--dur-ui` | — | as above |
| **Chip** | `--surface` on `1px --line`, `--ink-soft`, `--radius-sm`, `6px 14px`, 14px/400 | fill → `--surface-2` | `--brand-soft` fill, `1px --brand`, `--brand-ink` — exactly one selected | as above |
| **Card** | `--surface` fill, `--ring-hairline`, `--radius-lg` | **nothing.** A page built from hairlines has nothing to lift off | — | — |
| **Input** | `--fill-on-deep` on the dawn (`--surface` on paper), `1px --line-on-deep-strong`, `--radius-lg`, `0 12px`, **16px** Geist | border → `--line-strong` | focus-visible: `1.5px` `--focus-ring` at 50% alpha | as above |
| **Nav** | a `--radius-pill` bar, `--fill-on-deep`, `1px --line-on-deep`, `62px` tall, `8px 8px 8px 12px`, **no backdrop blur** | link colour only | — | — |
| **Provenance tag** | transparent, `1px` state-ink at 25% alpha, state-ink text, mono 10px/`--track-tag`, `1px 4px`, `--radius-sm` | none — it is a label, not a control | — | — |
| **Loader** | **pack decision:** a skeleton whose geometry matches the block it replaces — same radius, same hairline, `--surface-2` fill, no shimmer. The reference ships no loader on its marketing surface and leaves `spin`/`pulse` keyframes unused | — | — | — |
| **Empty state** | **pack decision:** one line of `--ink` stating what would be here, one `--ink-soft` line saying how to fill it, and nothing else. No illustration — the register is a document | — | — | — |

The input's `16px` is not a style choice: anything smaller triggers zoom-on-focus
on iOS. Keep it even where 14px would look better.

## Hero

**The dawn is the hero** (`--hero-dawn`, *Texture & surface*), and its
architecture is fixed:

- **Height** `min-height: 100svh` — small-viewport units, so the mobile browser
  chrome collapsing does not reflow the gradient. Never `100vh` here.
- **Shell** `--shell-max` (1920px) with `16px` padding rising to `48px`; the
  content column sits left, not centred.
- **Headline** `--t-hero` (67.2px) at `--lh-hero` (1.02) and
  `--track-display`, **capped at three lines**. The line ceiling is the real
  constraint: at 1.02 leading a four-line headline closes up into a block and
  the dawn no longer reads behind it. Write to the cap.
- **One accent phrase** inside the headline, in `--brand-on-dark` — never the
  paper brand, which measures 2.29:1 there.
- **Lede** `--t-lede` at `--lede-max` (448px), and it **must end above
  `--dawn-5`**: white copy is 15.4:1 at the top of the gradient and 4.06:1 by
  the 85% stop.
- The first viewport carries: eyebrow, headline, lede, up to three buttons, and
  one proof line. It does **not** carry a card, a screenshot, a metric row or a
  second dark surface — those start below the fold, on paper.
- The announcement bar is a real layout participant: the nav sits at
  `top: var(--bar-h)` (`38px` when open, `0` when dismissed) and transitions
  `top` over `300ms`. Do not absolutely position over it.

## Responsive

The rules, not the adjective.

- **Type is fixed px with breakpoint jumps, not fluid.** This is the reference's
  actual behaviour and it is deliberate: the hero drops 67.2 → 44 → 36px at the
  breakpoints rather than sliding. The whole page contains **exactly one**
  `clamp()`: `clamp(0.8125rem, 0.2rem + 2vw, 2.125rem)` (13px → 34px, slope
  2vw), used for the one figure caption that has to survive both ends. Copying
  `atrium`'s fully-fluid approach here would fight the pack, whose sizes are
  chosen against the hairline grid.
- **Breakpoints** are `40rem` / `48rem` / `64rem` / `80rem` / `96rem`, plus one
  `max-width: 639px` branch for the phone-only layout.
- **Full-height sections use `svh`**, with `100dvh` behind
  `@supports (height: 100dvh)`. Figure heights are `24svh` / `34svh` / `36svh`.
  Bare `100vh` is banned — it is why a mobile hero jumps when the URL bar hides.
- **No container queries.** The reference declares no `container-type` and no
  `@container` rule anywhere; components size against the viewport and against
  their own `max-width`. If you add them, add them for the app layer's panels —
  not for the page, whose column widths are the layout.
- **Collapse:** the section rule survives every breakpoint (it is the layout);
  section padding drops `64px → 16px`; the hero shell padding drops `48px →
  16px`; the nav pill keeps its height and sheds links. Crop marks are
  `hidden md:block` — they are a desktop-only flourish and must not become a
  touch target.
- Nothing in this pack overlaps, rotates or uses negative margins, so nothing
  collapses badly. That is a consequence of the ruled-sheet composition, and it
  is a reason to keep it.

## Motion tokens

- **Two eases, two jobs, and they do not borrow from each other.**
  `--ease-ui: cubic-bezier(.4,0,.2,1)` at `--dur-ui: .15s` drives every control
  state; `--ease-reveal: cubic-bezier(.22,1,.36,1)` at `--dur-reveal: .5s`
  drives scroll entry (`opacity` + `transform`). This overrides the SHELEG
  default ease — the pack wins.
- Transitions are **scoped to named properties**. `transition: all` is banned.
- **Only `--verify` ever animates colour.** A glyph in the hero field flips
  from `currentColor` at `--sym-op` to `--verify` at 0.95 for a tenth of its
  cycle; a confirmed claim blooms `text-shadow: 0 0 20px var(--verify)` once
  and returns to none. The rust never moves — the moment the brand animates it
  stops reading as an identity and starts reading as a status.
- The reference's one decorative effect is a chromatic split that uses the two
  hues as its channels (`text-shadow: ±2px 0 var(--verify), ∓2px 0 var(--brand)`).
  Use it on a single word, once per page, or not at all.
- `prefers-reduced-motion` zeroes every duration and resolves `.reveal` to its
  final state. **The reference ships this branch for every animated class** —
  unusually good, and this pack requires the same.

## Signature motifs

- **The dawn hero.** A dark field that resolves into the page instead of ending
  against it. It is the one place the pack spends contrast, and the reason it
  never needs a second dark section: the page has already been dark, at the top,
  and came out of it.
- **The numbered eyebrow.** `〉 HOW IT WORKS [03/09]` — a mono label at 11px and
  `0.16em`, prefixed with a chevron and suffixed with its position in the
  document, both at 55% opacity, built with `::before`/`::after` on a
  `data-n` attribute. The page numbers its own sections; a marketing page
  becomes a document with a table of contents. This is the pack's most
  transferable device and the first thing to keep.
- **The provenance tag.** `[EXTRACTED]` · `[INFERRED]` · `[AMBIGUOUS]` —
  bracketed mono at 10px and `0.08em`, transparent fill, a 1px border of the
  state's own ink at 25% alpha, `--radius-sm`. It sits inline with the claim it
  qualifies, never in a legend. See `AI_PRODUCT_PATTERNS.md` for the
  pack-agnostic version of this pattern.
- **The ruled sheet.** Sections divided by one hairline. No slabs, no alternating
  fills, no full-bleed colour blocks below the hero.
- **Crop marks at the corners.**
- **The claim with its source attached.** Every number on the reference names
  who produced it, in the same block, not in a footnote. On a page whose product
  is provenance this is not decoration — it is the argument.
- **Headings written as claims.** "The answer is a path, not a vibe." "Every
  edge says how it knows." Not "Features" and not "Benefits". (`briefing-room`
  carries the same rule for slides; here it applies to a scrolling page.)

## Signature element

**The dawn.** Not the crop marks, not the numbered eyebrow — those recur, and
recurrence is what makes them motifs. The dawn happens **once**, at the top,
and it is the only place this pack spends contrast, saturation or spectacle.

It carries the identity because it resolves the pack's central tension in one
gesture. A developer tool is expected to be dark; this one is printed on paper.
The dawn does not argue with the expectation, it *passes through* it: the page
opens where the reader expects a console and arrives, without a seam, at the
document it actually is. A hard-edged dark hero would read as two pages stapled
together; the eight-stop resolve reads as one page that got lighter.

Everything around it stays quiet, which is the price. Below the dawn there is
no second dark surface, no gradient, no photography bleed, no generative layer —
only paper, hairlines and ink. Spend the boldness here or the pack has no
centre.

## Motion flavor (cinematic packs only)

If you ride more of the SHELEG stack with this pack: keep the scroll clock,
use the Reveal set at `--dur-reveal` on `--ease-reveal`, and let the hero's
glyph field be the only ambient layer. It is a **notation** field, not a
particle field — symbols from the product's own domain at `--sym-op`, drifting
slowly, with at most one flipping to `--verify` at a time. Do not add a WebGL
particle system: the register is printed, not atmospheric, and a generative
background is the fastest way to turn a document back into a landing page.
Anything generative stays inside the hero and dies at the dawn's last stop —
nothing generative appears on the paper.

## Micro-interactions

- **Primary CTA:** a pill, `--ink` fill with `--on-ink` label on paper, or a
  white fill with `--dawn-1` ink on the hero. `8px 16px`, 14px/500, transition
  `opacity` over `--dur-ui`. It carries a `>_` prompt glyph — the one place the
  pack lets a terminal into the marketing surface.
- **Secondary:** `--radius-lg`, `12px 20px`, 14px/600, transition
  `transform, background-color`. **Ghost on the hero:** `--fill-on-deep` with a
  `--line-on-deep-strong` border.
- **Chips:** `--radius-sm`, `6px 14px`, 14px/400. Unselected is `--surface` on
  `--line` in `--ink-soft`; selected is `--brand-soft` on `--brand` in
  `--brand-ink`. Exactly one selected at a time.
- **Focus-visible:** a 2px `--focus-ring` (the brand) at 2px offset, following
  the target's own radius. On the hero it is `--brand-on-dark`, never white.
- Nothing scales on hover and nothing lifts. State is carried by fill, border
  and opacity — a page built out of hairlines has nothing to lift *off*.
- Tabs are mono uppercase at 10px/`0.05em`; the active tab is full ink, the
  rest sit at 60%.

## Bans

- `--verify` as text at body size; white on `--verify`; `--brand` (the light
  value) on any dark surface — use `--brand-on-dark`.
- A true black, a cool grey, a pure `#FFF` card, or any framework default
  neutral (`#18181B`, `#F2F3F4`) beside the green-cast palette.
- A fourth semantic hue; the provenance colours used for anything that is not
  provenance; `--danger` and `--witness` conflated.
- **Italic anywhere.** The display face has none, so `<em>` synthesises a
  slanted fake. Emphasis is a colour change on one phrase, or the mono voice.
- A hardcoded radius in px; a grey drop shadow where the ring belongs;
  `transition: all`; hover states that scale or lift.
- A second dark section below the hero; a dark band with a hard edge; a
  full-bleed colour block. The hero is the only dark surface, and it dissolves.
- Mono for long-form copy; a `tabular-nums` data table styled as annotation, or
  an annotation styled as data.
- A confidence *percentage* where a provenance *tag* belongs.
- A claim with no source in the same block.
- A particle field, a mesh gradient, or any decorative gradient other than
  `--hero-dawn` and `--hero-vignette`.

## Gotchas

The reference is strong on composition and on reduced motion, and it has one
serious contrast failure plus three system-level inconsistencies. All four are
measured and all four are fixed from inside the palette — treat them as the
first thing to correct when porting this look:

- **The hero's accent phrase fails badly, and it is the most prominent text on
  the site.** `--brand` `#9A3F28` measures **2.29:1** against the gradient's top
  stop and **1.41:1** against its middle. The fix costs one token and no design:
  `--brand-on-dark` `#CF7A52` measures **4.82:1** there. Darkening the paper
  brand instead would break its 6.3:1 on the page, so the two values must both
  exist.
- **White body copy dies before the gradient does.** White is 15.4:1 on
  `--dawn-1` and **4.06:1** by `--dawn-5` at 85%. Content must end above that
  stop; a lede that runs into the dawn becomes unreadable exactly where the page
  looks prettiest.
- **`--verify` is not a text colour.** 3.2:1 on the paper, and white on it is
  3.4:1 — so the reference's own `--verify-foreground: #fff` fails. Labels take
  `--verify-ink` (5.3:1). The reference gets this right in its tags and wrong in
  its token names.
- **The reference sets `color-scheme` nowhere** despite shipping a complete dark
  theme, so UA form controls and scrollbars follow the OS while the page follows
  the class. This token layer sets it **per theme** — the same trap that bit
  `workbench`; never `light dark`.
- **The reference runs three unrelated dark palettes**: a warm-brown `.dark`
  theme (`#14110E`), forest bands on the page (`#072820`), and a navy terminal
  (`#0B101D`). This pack keeps the forest family, because it is the hero's own
  gradient and the only one the page argues for; the terminal takes a darker
  step of the same family. If you port the reference verbatim you inherit three
  systems and no rule for choosing between them.
- **Its app layer drifts from its page layer.** The reference's `--sidebar-*`
  neutrals are browner than the page's green-cast ones and its sidebar ring is a
  violet that appears nowhere else. Reconciled here; do not re-import it.
- **The display face has no italic and one substitution trap.** Bricolage
  Grotesque's slight irregularity is the whole personality; a clean neutral
  grotesque in its place turns the page corporate, and the loss is bigger than
  any colour substitution. Its `opsz 12..96` axis is available and unused by the
  reference — set `font-optical-sizing: auto` at hero sizes.
- **`--deep` was annotated as a "full-bleed dark band" — the exact thing this
  pack bans.** Corrected 2026-08-08. Surfaced by a routing-scenario subagent
  reading the pack cold, then reproduced: the token layer called `--deep` a
  full-bleed band, the Palette table called it "band", and Bans forbids "a
  second dark section below the hero; a dark band with a hard edge". Checking
  the consumers settled it — **nothing consumes `--deep`, `--deep-2` or
  `--deep-3` anywhere in the kit or the bundle.** What *is* consumed is the
  `-on-deep` family (`--on-deep`, `--fill-on-deep`, `--line-on-deep`), and only
  inside `.fn-hero`, which is the dawn — the pack's one legitimate dark surface.
  So the family is real and the annotation was wrong: these are **bounded** dark
  surfaces, and the terminal is the intended one. If you reach for `--deep` as a
  section background you have left the pack.
- **Values are a snapshot** taken 2026-08-04 from a live production site. Treat
  them as extracted, not eternal.
