# Style pack — Proscenium

Origin: [mailmodo.com](https://www.mailmodo.com/) — read off its live computed
styles in a headless Chrome at 1440×1000 on 2026-08-17, not transcribed from a
screenshot or a stylesheet.

A white field carrying two cool acts and **one deep indigo act at the middle**,
ink that is an indigo rather than a grey, and a single electric violet that
fills a control which is nearly square at 4px while every card around it sits at
16. The page opens on a framed product panel the fold cuts off, and then repeats
a fixed cadence: two acts, then the same call to action, again. The whole
argument of the pack is *demonstration* — the product is on screen before a
single claim is made, and every act after that is another view of it.

Contract: widened — all thirteen headings.

Themes: light + dark — a full theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose Proscenium for **product-led marketing front doors whose argument is a
demonstration**: SaaS home pages, launch and tour pages, pages that have to
carry six or more distinct acts without the reader losing the thread, and any
surface whose best evidence is the interface itself rather than a logo wall.
**Standalone** — it does not ride the SHELEG cinematic layer. Its motion ceiling
is **4**: entrance reveals, a disclosure that opens a stored state, and hover.
It bans scrubbing, parallax and a scroll clock, so a dial above 4 has nothing
legal to buy here.

**Not for:** dense operator tooling, documentation homes, or anything sold on
restraint — a 62px display over a violet fill is the opposite of quiet, and
`notation` is the fork for that. Not for a page whose argument is an inventory
rather than a promise: that is `router`. Not for a single hero object floating
alone on a cool field, which is `daylight` — this pack frames its object rather
than lifting it, and repeats the frame down the page.

**The fork against [`showroom`](./showroom.md).** Both are white, both are
product-led, and both put a real interface on the page. The split is **tempo**:
showroom is a gallery that gives the app a white room and lets the reader dwell,
while Proscenium is a sequence of staged acts on a fixed beat — two acts, then
the same call to action, again — with one dark act at the middle. Choose
showroom when the product is the whole argument and the page can be quiet around
it; choose this one when the page has six or more acts to get through and the
reader needs a beat to hold on to.

## Palette

Ready-made token layer: [`tokens/proscenium.css`](tokens/proscenium.css) — copy
it verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#ffffff` | page field — white, and the acts sit on it |
| `--panel-2` | `#f4f6fa` | the cool act that changes subject |
| `--ink` | `#101043` | body text — an indigo, not a grey |
| `--ink-strong` | `#05041c` | headings — measured as `#000`, shipped one step into the pack's indigo |
| `--muted` | `#475467` | secondary text |
| `--border` | `#e5ecf3` | the seam |
| `--edge` | `#767f99` | the visual boundary of a **control** |
| `--accent` | `#5a45fe` | THE single functional accent, and it fills the primary |
| `--accent-deep` | `#4c3bea` | link ink, one step deeper than the fill |
| `--stage-from` / `--stage-to` | `#07061d` / `#2a0b78` | the one dark act, gradient stops measured |
| `--stage-panel` | `#18143a` | the dark card that stands inside that act |
| `--bloom-1` / `--bloom-2` | `#72d0f2` / `#82bdff` | two soft discs behind the field — decoration, never meaning |

### Floors, and what each colour may mean

Every ratio below is computed from the token layer, not asserted.
`--ink` is 17.84:1 on `--bg` and 16.49:1 on `--panel-2`, the cool act.
`--muted` is 7.69:1 on `--bg` and 7.10:1 on `--panel-2`.
`--accent` is 5.65:1 on `--bg` and carries white text at the same 5.65:1
when it fills a control.

**Status is never by colour alone.** Every state is a dot or an icon **plus a
word**. Green, amber and red are the classic confusion set and no palette solves
it under dichromacy, so the word carries the meaning and the colour reinforces
it. This is a ban, not a preference — see `## Bans`.

**`--ok` and `--danger` are derived, not measured**, and the token layer says so
at the declaration. The reference is a marketing site and paints neither state,
so both were authored to clear AA on the field, the cool act and their own tint
(6.45 / 5.96 / 5.69 and 6.54 / 6.04 / 5.70) rather than sampled.

**`--warn` is a measured hue at an authored lightness.** The reference paints
its amber at `#9e7613`, which is 4.15:1 on white and under AA for body text. The
hue is the reference's; the step down to `#8a6510` (5.32 / 4.91 / 4.68) is this
pack's, and the token layer marks it at the declaration.

**`--info` IS the accent.** The reference has exactly one functional colour and
this pack keeps that: "running" is the product's own violet, never a second
blue.

**The blooms are not a palette.** `--bloom-1` and `--bloom-2` are two soft discs
laid behind the field at low opacity. They never carry state, never sit under
text that has to be read, and never appear in a chart.

## Type

**One family, and that is the pack.** The reference loads Inter at nine weights
and no second face anywhere on the page — the hierarchy is bought entirely with
size, weight and tracking.

- **Display — Inter 600**, tracking `-0.016em` (measured as −1px at 62px),
  line-height 1.048 at the hero and 1.161 at an act heading.
- **Feature heading — Inter 700**, tracking `-0.006em`, line-height 1.231.
- **Body — Inter 400**, line-height 1.54. Every sentence.
- **Quote — Inter 400 at 44px**, tracking `-0.045em`. A large heading at *body
  weight* is the reference's one type surprise and it is worth keeping.

A second family is a defect. The mono in `--font-data` is derived — the
reference ships none — and exists for a figure and a unit inside a product
demonstration, never for a label and never for a sentence.

Scale: `--t-meta` 13, `--t-body` 16, `--t-lead` 18, `--t-card` 26,
`--t-feature` 28→39, `--t-quote` 26→44, `--t-act` 28→62, `--t-hero` 27→62.
Measures: 62ch prose, 46ch lede under a centred hero.

## Texture & surface

**Elevation is four shadows and they do different jobs.** `--shadow-frame` is the
fourth and the quietest: `0 0 34px` of ambient with an inset white bloom, for the
framed media a scene is built around — never for a card and never for a control.
`--shadow-card` is
94px of blur at 4px of offset in a violet-tinted black — the argument-carrying
card, and it is the pack's signature texture. `--shadow-hair` is a hard
`1px 2px 0` in the seam colour with no blur at all, for the quiet card that is
merely a container. `--shadow-control` is the primary button's own two-stop
shadow. A control never takes the card shadow and a card never takes the
control's.

Radii: `--r-control` 4, `--r-inner` 10, `--r-card` 16, `--r-pill` 999. **The gap
between 4 and 16 is measured and it is load-bearing** — a nearly square button
against a generous card is what keeps a roomy page from reading as soft. Closing
it is the single fastest way to stop this pack working.

**Radius arithmetic when containers nest:** an inner radius is the outer minus
the padding between them. A panel inside a card padded `--space-3` is
`calc(16px - 12px)` = 4, which lands exactly on `--r-control` — so an inner
panel and a button read as the same curve, and that coincidence is the pack's,
not an accident to be "fixed".

Spacing is a 4px grid. Acts run `--act-rhythm`, measured at 25px on a phone and
120px at 1440 — the reference spends a fifth of its page on air and compressing
it to save a scroll is how this pack stops being itself.

## Components

- **Buttons.** Radius 4, 16px label, weight 600. *Primary:* `--accent` fill,
  `--accent-ink` label, `--shadow-control`. *Secondary:* `--panel` fill, 1px
  `--edge`, no shadow. *Ghost:* no fill, `--accent-deep` label. **Hover** moves
  background and border only. **Active** presses nothing — the shadow flattens
  to `0 1px 2px` instead. **Disabled** is opacity .45 with the label colour
  kept, never a grey fill that reads as a second variant.
- **Cards / containers.** `--panel` at radius 16. Two kinds and they are not
  interchangeable: the *argument card* carries `--shadow-card` and no border;
  the *container card* carries a 1px `--border` and `--shadow-hair`. A list of
  statements takes neither — it takes a seam.
- **Inputs / forms.** Label above at 16/500, input at radius 4 with `--edge`,
  hint below in `--muted`. **Focus** is a 3px `--accent-weak` ring plus the
  border at `--accent`. **Error** puts `--danger` on the border and replaces the
  hint with the message; the field keeps what the person typed.
- **Navigation.** Sticky and **transparent at rest** — measured: the reference's
  bar has no background until the page scrolls, at which point it takes `--panel`
  and a bottom seam. Height 60 on a phone, 78 at 1440. Mobile shape is a
  `<details>` disclosure, not an overlay.
- **Loaders.** Skeleton blocks at `--r-inner` filled `--panel-2`, sized to the
  real element. No spinner under 400ms of expected wait, and never a spinner
  inside a card that already has its frame drawn.
- **Empty states.** Centred inside the card that would have held the data: one
  line at `--t-card`, one sentence at 44ch in `--muted`, and the action that
  creates the first record. No illustration — this pack's decoration budget is
  spent on the blooms.

## Hero

**Centred, and the product panel is already in the first viewport.** The
composition is: eyebrow at `--t-meta` in `--muted` with `0.04em` tracking,
display at `--t-hero`, one lede at 46ch, one primary control, one line of
reassurance under it — then the framed product panel, cropped by the fold.

Display capped at **32ch**, which holds it to **two lines at 1440** and four at
390. The container that keeps it there is `--page` 1271 with the headline itself
limited to 890px — measured: the reference's own h1 box. A headline reaching
five lines is a broken hero, not a long one.

The first viewport must contain the panel's top edge. It must not contain: a
second filled control, a logo wall, or a testimonial — the reference puts proof
below and is right to, and a page that has no real logos to show (most of them)
must not leave a hole where one would go.

## Responsive

- **Fluid type.** `--t-hero` is `clamp(27px, 0.34rem + 5.52vw, 62px)` — 27px at
  390 and 62px at 1024 and above, both endpoints measured, a slope of 5.52vw.
  `--t-act` is `clamp(28px, 0.44rem + 5.36vw, 62px)`. Body does not scale.

  **The reference's own answer is different and this pack declines it.**
  Mailmodo steps the root font size by viewport — 10px at 390 and 768, 11px at
  1024, 13px at 1440 — and lets every rem follow. It is measurable, it is
  coherent, and it overrides the reader's own text-size preference, so what this
  pack takes from it is the *endpoints*, expressed as a slope with a rem term
  that keeps user text size in the sum.
- **Container queries.** Sorted by kind, because only the first has a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | Feature card going from text-beside-interface to text-above | CONTAINER | `container-type: inline-size` on the card, `@container` on its grid |
  | The proof rail stepping 4 → 2 → 1 | CONTAINER | container on the rail, `@container` on the tracks |
  | A demonstration table dropping its third and fourth columns | CONTAINER | container on the table wrapper |
  | Hero going from centred-wide to centred-narrow | PAGE | viewport `@media (max-width: 900px)` |
  | The sticky bar collapsing to a disclosure | PAGE | viewport — the bar is the page's |
  | Act rhythm `--act-rhythm` | PAGE | the page owns it |
  | The framed panel's own tilt unwinding | SELF | **no container answer exists** — a container cannot query itself. Keep the viewport query |

- **Collapse.** The hero's panel loses its tilt below 900 and its crop below 640
  — a rotated element that survives to a phone is a touch-target conflict and a
  horizontal scrollbar. The blooms drop to a single disc. The floating CTA panel
  becomes a static block in the flow rather than a fixed bar, because a fixed bar
  on a phone eats the one viewport the reader has.
- **Viewport.** `min-h-[100dvh]` for full-height sections, never `100vh`.

## Motion tokens

One curve, `cubic-bezier(0.23, 1, 0.32, 1)` — the doctrine's enter curve,
derived rather than measured, because the reference reveals through AOS and
publishes no timing of its own.

`--dur-hover` 0.12s for background, border and colour. `--dur-state` 0.2s for a
disclosure or a state change. `--dur-reveal` 0.42s for an entrance, with
`--stagger` 0.06s between siblings and **no more than four in a run** — a fifth
sibling arrives after the reader has already started reading.

Reduced motion sets all four to `0s` at the token layer, so an entrance becomes
a presence and nothing else in the page has to know.

## Signature motifs

1. **The framed panel.** A translucent grey fill, a 1px white border and an
   inset white glow around a product view — repeated down the page at every act
   that shows an interface.
2. **The fixed cadence.** Two acts, then the same call to action, again. The
   reader is never more than two acts from the next one.
3. **The one dark act.** A single `--stage` gradient block at the middle of the
   page, and exactly one — a second turns the page into a different design.
4. **The nearly square control.** Radius 4 against cards at 16.
5. **The blooms.** Two soft discs behind the white field, low opacity, no
   meaning.
6. **One family, nine weights.** Hierarchy from size, weight and tracking alone.

## Signature element

**The proscenium arch — the framed product panel the fold cuts off.** Not the
frame as a border style: the *cropping*. The page opens with the product already
on screen and deliberately unfinished at the bottom edge, so the first scroll is
motivated by the object rather than by a promise about it. A page in this pack
is remembered as *the one where the product was already there*.

Everything else in the first viewport stays quiet so the arch can carry it: one
control, no second fill, no logo wall.

## Micro-interactions

- **Hover** moves background, border and colour, and on a card lifts nothing —
  the shadow is the card's identity, not its response.
- **focus-visible** is a 3px `--accent-weak` ring plus the border at `--accent`,
  identical on a button, an input and a link. The ring ships as a literal before
  any derived value, so a browser without relative colour keeps it.
- **Keyboard.** The nav disclosure and the FAQ are `<details>`, so both open
  without script and both are in the server HTML. No keyboard-initiated path
  animates.
- **Selected** keeps its state after the pointer leaves; hover does not.

## Bans

- **No second dark act.** One `--stage` block per page.
- **No scroll clock, no scrub, no parallax.** The ceiling is 4 and this is what
  it means.
- **No status by colour alone.** Dot or icon, plus a word.
- **No card shadow on a control**, and no control shadow on a card.
- **No closing the 4/16 radius gap.** Rounding the button to match the card is
  drift, and it is the most likely single edit to make this page generic.
- **No second family**, and no swapping Inter for a system stack "for now".
- **No logo wall and no invented counter.** The reference has real logos; a page
  that does not must build its proof rail from product facts and leave no hole.
- **No bloom under running text.**
- **No fixed CTA bar on a phone.**

## Gotchas

- **The reference's rem-base step will re-enter through a "fix".** Someone
  reading mailmodo directly will see `html { font-size: 13px }` and copy it, and
  every clamp in this pack will then be computed against a 13px rem while the
  reader's own setting is discarded. If a page in this pack suddenly reads small
  on a phone, check the root font size before touching a single token.
- **The 94px shadow disappears on a coloured act.** `--shadow-card` is a
  violet-tinted black at 9% and it is invisible on `--panel-2` and worse than
  invisible on `--stage`. Inside the dark act, a card is separated by
  `--stage-panel` and a seam, not by elevation.
- **A second dark act reads as a template, not a design.** Two `--stage` blocks
  make the page look like a section list. The measured page has exactly one, at
  the middle, and it is the pack's tempo rather than its decoration.
- **The blooms tint text that sits over them.** They are `#72d0f2` and `#82bdff`
  at low opacity on white; body ink over one still clears AA, but `--muted` at
  14px does not reliably. Keep them behind cards and headings, never behind a
  paragraph.
- **`--warn` looks wrong beside the measured screenshot, because it is not the
  measured value.** The reference's `#9e7613` fails AA for body text; this pack
  ships `#8a6510`. If someone re-measures the reference and "corrects" the
  token, the palette gate fails and it is right to.
- **The heading ink is not the measured value, and re-measuring will "find" that.**
  The reference sets headings to pure black; this pack ships `#05041c`, because a
  pure black field or ink is banned library-wide as an unfinished default and the
  slop lint fails on it. What was worth keeping is the *move* — headings a step
  darker than an indigo body ink — not the literal.
- **Radius 16 on a chip looks like a mistake, because it is one.** `--r-card` is
  for cards; a 28px-tall chip at 16 is a lozenge. Chips take `--r-pill`,
  controls take `--r-control`.
