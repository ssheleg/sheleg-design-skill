# Style pack — Chorus

Origin: <https://crowdreply.io> (2026), the front page of an AI-search visibility
product. The site is **Framer**, and the authored layer is its 52
`--token-<uuid>` custom properties plus the per-element Framer classes: 274,355
bytes of CSS across 11 stylesheets and 1,106 rules. The token dump and the render
disagree — 15 of the 52 declared tokens are referenced once and reach no painted
surface — so the render decided every value here. Read on 2026-08-30 through CDP
at 1440×900, an emulated 768×1024×2 and an emulated 390×844×2: an area-weighted
census of `background-color` **and** `background-image` over all 2,439 elements of
an 11,750px page. Ratios were computed by importing this repository's own palette
gate.

Warm off-white paper under a **faint construction grid that never switches off** —
two 1px verticals running the full height at `x=162` and `x=1278` of 1440, crossed
by horizontals that carry a small plus at each intersection, 63 rule elements in
the census, drawn across the light field and continued across the dark band. On
that sheet: flat white cards with no border and no shadow, cream wells that hold a
demo, near-black slabs inset into the paper, one hot coral that may fill but never
write, and a periwinkle that only exists inside a gradient or on the dark.

The identity in one sentence: **somebody else's question is the page's set piece**
— a card whose top-right corner is squared off into a speech-bubble tail, holding
a stranger's words in the display face, with the brand's answer placed underneath
it.

Contract: widened — all thirteen headings.

Themes: light only — the dark slab is a SURFACE variant (`[data-surface="slab"]`, with `.chorus-slab` as its class alias), not a theme twin; the page never inverts.
Rank: unordered — 3 status role(s) and no severity ramp; a rank scale is yours.

## Contents

- Register
- Palette
- Type
- Texture & surface
- Components
- Hero
- Responsive
- Motion tokens
- Signature motifs
- Signature element
- Micro-interactions
- Bans
- Gotchas

## Register

Choose Chorus for **products whose proof is other people's conversations** —
AI-search and answer-engine visibility, brand monitoring and share-of-voice,
social listening, community and forum marketing, review and reputation tools,
anything whose pitch is *the buying decision is being made in a thread you are not
in yet*. The proof this pack organizes a page around is **the quoted question**:
the thread title in the display face, the platform mark beside it, the metric that
says how much traffic it carries, and the reply the product would place.

Standalone: it does **not** ride the SHELEG cinematic motion layer. The reference
holds one `@keyframes` (Framer's own loading spinner, which is vendor rather than
design), two timed CSS transitions and no scroll clock at all —
`MOTION_INTENSITY` above **2** has nothing legal to buy here. What it *does* have
is a scripted entrance on almost everything, and that is a hazard rather than a
budget: see Motion tokens.

**Not for:** a product proven by the reading rather than the conversation — a
visibility tracker whose page is portraits of a dashboard and contour texture is
[`surveyor`](./surveyor.md). Not for a product that speaks in its own voice to its
own user — an AI colleague whose transcript is a demo is
[`deskmate`](./deskmate.md). Not for one brand spanning marketing and product UI,
which is `outrank`; not for a white-and-one-accent SEO product sold on long
time-to-value, which is `babylove`. Without a quoted stranger on the page this
pack decays into generic warm-paper marketing, and the grid becomes wallpaper.

### The fork against [`surveyor`](./surveyor.md), which is the AI-visibility collision

Both sell an AI-search visibility product on warm paper, both put a dark dashboard
in the first two screens, and a router reading "track where AI mentions my brand"
cannot separate them on the pitch. The separation is **what the page hands the
reader**. Surveyor hands a *reading*: portraits of the instrument, counted stat
slabs, contour lines that say *mapped*, flat light surfaces with `box-shadow: none`
on every card and no dark band anywhere. Chorus hands a *conversation*: a
cut-corner bubble carrying somebody's actual words, a coral that fills and a
periwinkle that answers, and full-bleed near-black slabs cut into the paper. If
the deliverable is *here is where you stand*, go there. If it is *here is the
thread, go reply*, stay here.

### The fork against [`deskmate`](./deskmate.md), which is the speech-bubble collision

Both make a chat bubble the page's illustration and both sit on warm paper, so a
thumbnail cannot separate them. The separation is **whose bubble it is**.
Deskmate's transcript is the *product's own* — a request the user made and the
work that came back, framed as a demo of the thing being sold, and its geometry is
a pill for everything a hand touches over a 32px slab. Chorus's bubble is a
*stranger's* — a question asked on a forum the brand does not own, and its geometry
is one squared corner on three 24px ones, a tail pointing at a reply that has not
been written yet. Deskmate proves the product talks; Chorus proves the market is
already talking. If the quoted words belong to your product, go there.

## Palette

Every value below is in
[`tokens/chorus.css`](./tokens/chorus.css), which is the single home; this table
documents roles. Provenance is marked per value in the token layer as MEASURED,
DERIVED or PACK DECISION. There is no SELECTED family here — the reference offers
no darker step of its own in any hue that fails, so every correction had to be
derived rather than promoted, which is the opposite of `surveyor`.

| Token | Value | Role and the number that licenses it |
|---|---|---|
| `--bg` | `#fbfaf9` | The field. 16.99M px² of the census, 2.8× the next-largest painted area. |
| `--surface` | `#ffffff` | Every card — 1.04:1 on `--bg`, which is the reference's entire card separation and the pack's first correction (see `--line`). |
| `--paper` | `#faf8f0` | The cream well that holds a demo, and the 1050×682 hero deck. 1.06:1 on `--surface`. |
| `--paper-deep` | `#f5f2e6` | The tinted 67px row. |
| `--parchment` | `#f1ecd9` | The standalone warm panel, and the third stop of the signature sweep. |
| `--slab` | `#1b181c` | The dark band inset into the paper — one 1380×696 instance at 30px inset, radius 16px, plus the announcement strip. |
| `--well` | `#111111` | The product screen inside a white card — 1.07:1 on `--slab`, a step rather than a tier. |
| `--slab-raised` | `#28242a` | A chip on the slab — 1.15:1 on `--slab`. |
| `--ink` | `#111111` | Section heads. 18.11:1 on `--bg`. |
| `--ink-strong` | `#1b181c` | The display, the dark button, the focus ring. 16.87:1 on `--bg`. |
| `--ink-body` | `#46484d` | All body copy. 8.78:1 on `--bg`, 9.15:1 on `--surface`. |
| `--ink-muted` | `#6a6673` | The nav item and the quiet label. 5.36:1 on `--bg`. |
| `--ink-ghost` | `#8a8692` | **Non-text.** The reference's own muted step, and a recorded failure: 3.41:1 on `--bg`. Rules, placeholder bars, tinted icons. |
| `--on-slab` | `#faf8f0` | 16.54:1 on `--slab`, 17.76:1 on `--well`. |
| `--on-slab-quiet` | `#9ca3af` | 6.93:1 on `--slab`. |
| `--coral` | `#f96f4b` | **Non-text.** The primary fill, the flat answer-block, the first gradient stop. It cannot carry a white label at any size; the numbers are in Gotchas. |
| `--coral-hot` | `#ff5d30` | **Non-text.** The reference's hover and current-link token; 2.94:1 on `--bg`. |
| `--coral-ink` | `#cb441f` | DERIVED at hue 35.7°. The coral that may speak: 4.59:1 on `--bg`, 4.79:1 on `--surface`, 4.50:1 on `--paper`. |
| `--on-coral` | `#1b181c` | 6.20:1 on `--coral` — the correction that keeps the brand hue and changes the label. |
| `--periwinkle` | `#82a7f8` | **Non-text on paper.** A gradient stop, a flat block, and a series line at 7.40:1 on `--slab`. |
| `--good` | `#198400` | DERIVED at hue 141.1° from the reference's own green, which cannot carry a word at any size it is set. 4.64:1 on `--bg`. |
| `--danger` | `#d03950` | DERIVED at hue 17.1° from the reference's rose. 4.60:1 on `--bg`. |
| `--info` | `#1167f4` | MEASURED, unmodified. 4.72:1 on `--bg`. |
| `--on-status` | `#ffffff` | 4.84:1 on `--good`, 4.79:1 on `--danger`, 4.92:1 on `--info`. |
| `--good-on-dark` | `#36ff94` | 13.31:1 on `--slab`. The reading's own colour, and it lives **only** on the dark — see below. |
| `--danger-on-dark` | `#fc6373` | 6.01:1 on `--slab`. |
| `--info-on-dark` | `#82a7f8` | 7.40:1 on `--slab`. |
| `--line` | `rgba(70,72,77,.12)` | The grid, and the card's edge. Composited it lands far under the mark floor, which is what a rule wants; the figures are in the token layer. |
| `--line-quiet` | `rgba(70,72,77,.08)` | The inner divider. |
| `--line-on-slab` | `rgba(255,255,255,.12)` | The grid continued across the dark band, at the same weight. |

**Status is never by colour alone.** `--good` and `--danger` sit 32.4 apart at full
colour and **6.2** apart under deuteranopia — green against red is the classic
collision and no re-stepping in this hue pair fixes it — so every delta ships its
arrow and its number, exactly as the reference's own metric cards do.

The reference's own green is `#239806`. Composited against its own field,
#239806 on #fbfaf9 is 3.62:1, which is under AA at every size the reference sets
it, and it is why `--good` is derived rather than measured. The rule inks
composite the same way: #e5e5e4 on #fbfaf9 is 1.21:1, #e9e9ea on #ffffff is
1.21:1, and #363437 on #1b181c is 1.43:1 — all three far under the mark floor,
which is correct for a rule and is why nothing may be written on one.

**The mint is dark-only, and that is a constraint rather than an omission.**
`#36ff94` is the identity of a reading — 36 text instances in the census, every
one of them inside a dark well. Held at its own hue it reaches AA on paper only at
near-black, which is a different colour rather than a step, so the light ladder
above is a separate answer and not a translation. A green figure on paper takes
`--good`; a green figure in a well takes `--good-on-dark`. They are not the same
value and the pack does not pretend otherwise.

**There is no warn.** The authored token set declares an amber (`#ffc300`) that
reaches no painted element at any of the three widths — the census found zero
instances in `background-color`, `color` or `fill`. A fourth severity invented
from an unpainted declaration would be a value with a citation attached. A surface
that needs one is quoting a different library.

## Type

Three faces, and the display face has one job the others cannot take.

| Role | Face | Size · line-height · weight · tracking |
|---|---|---|
| Display | `--font-display` (Outfit) | 56px · 1.1 · 600 · −0.0625em, and 40px · 1.1 · 600 · −0.025em from 768 down |
| Section head | `--font-sans` (Inter) | 44px · 1.2 · 600 · −0.032em, and 34px · 1.2 · 600 · −0.025em from 768 down |
| Sub-head | `--font-sans` | 32px · 1.4 · **500** · −0.047em — the one heading that is not 600 |
| **The quoted question** | `--font-display` | 24px · 1.5 · 600 · −0.02em |
| Card head | `--font-sans` | 18px · 1.7 · 600 |
| Lede | `--font-sans` | 18px · 1.7 · 400 |
| Body | `--font-sans` | 16px · 1.7 · 400, and the same size at 500 for emphasis |
| Label | `--font-sans` | 14px · 1.4 · 400 or 500 |
| Micro | `--font-sans` | 12px · 1.333 · 500 |
| Eyebrow, mono | `--font-mono` (DM Mono) | 13px · 1 · 500 · uppercase — the section label over a heading, and nothing else |

**The display face carries the stranger's words.** Outfit sets exactly two things
in the census: the hero, and the question inside every cut-corner bubble. Inter
sets every section head, all body and all UI. Putting a quoted question in Inter
is the fastest way to lose this pack's identity — it is what makes a bubble read
as *somebody said this* rather than *we wrote this*.

**Tracking relaxes as the type shrinks**, which is the opposite of the usual move
and is measured at both widths: −0.0625em on the 56px display becomes −0.025em on
the 40px one. Do not tighten a small display here.

**Body line-height is 1.7** — 27.2px on 16px and 30.6px on 18px, the loosest in
this library. It is the register's own generosity and the reason a card can hold
four lines of explanation without a scroll.

**Two more families appear in the corpus and are not carried.** Inter Display (9
instances) and Inter Tight (1) are Framer's font-picker drift rather than an
authored system; adding them buys nothing and costs two more font files. All three
faces the pack does carry are open licences. Font loading is the consumer's, by
this library's own rule.

**600 is the heading ceiling and 700 is the line ceiling.** 700 is measured twice,
both times inside a running line, so it is pinned to `--weight-strong` in the
token layer's `strong, b` rule rather than banned. Nothing above 700 appears
anywhere in the corpus. **No italic exists in the corpus at any size** — measured
across every text-bearing element at all three widths — and `em, i` is pinned to
`font-style: normal` in the same layer, because the UA supplies an oblique whether
the pack agrees or not.

## Texture & surface

**The grid is the texture, and it is the whole texture.** There is no noise, no
gradient mesh, no pattern fill and no illustration behind type. What there is:

- Two 1px verticals in `--line` at the frame edge, running the full height of a
  section, at `x=162` and `x=1278` of 1440 — a 1116px frame that is **wider than
  the 936px content column inside it**.
- Horizontals in the same ink where a section begins and ends.
- A small plus, roughly 12px on each arm, centred on every intersection. This is
  the detail that makes it read as a drawing surface rather than a table.
- The grid **continues across the dark slab** in `--line-on-slab`. It does not
  stop at the band's edge, and that continuity is what makes the slab read as cut
  into the sheet rather than laid on top of it.

**Elevation is four named objects, not a ladder.** `--shadow-bubble` belongs to the
cut-corner card (24 instances, the most-used shadow on the page); `--shadow-card`
is the wide soft halo under a floating panel (3); `--shadow-drift` is the
left-biased warm triple under the stacked hero deck (3), directional because the
deck is offset left; `--shadow-nav` is the single drop under the floating
navigation pill (1). **Any card that is not one of those four objects has
`box-shadow: none` and takes `--line` for its edge.** Borrowing a shadow to
separate a card is a foreign object here.

**Surfaces stack by value, and the steps are tiny by design.**
`--surface` is 1.04:1 on `--bg`.
`--paper` is 1.06:1 on `--surface`.
`--well` is 1.07:1 on `--slab`.
The reference ships that stack with no borders at all, which is its recorded
failure; the pack keeps the value steps and adds `--line` to the card.

## Components

| Component | Ink, and what it measures | Fill | Radius | Metrics |
|---|---|---|---|---|
| Primary button | `--on-coral` at 6.20:1 on `--coral` | `--coral` | `--r-control` | 36px tall, 8px/16px padding, 14px/500 label |
| Secondary button | `--on-slab` at 16.54:1 on `--slab` | `--ink-strong` | `--r-control` | same metrics |
| Tertiary button | `--ink-strong` at 17.59:1 on `--surface` | `--surface` | `--r-control` | 1px `--line`; icon in `--coral` |
| Eyebrow chip | `--ink-body` at 9.15:1 on `--surface` | `--surface` | `--r-chip` | 1px `--line`, 8px/10px padding, 14px/500 in `--font-sans` — it is not the mono eyebrow |
| Nav item | `--ink-muted` at 5.36:1 on `--bg` | transparent | `--r-pill` | 6px/8px padding; hover fills `--line-quiet` |
| Card | `--ink-body` at 9.15:1 on `--surface` | `--surface` | `--r-card` | **32px padding and 32px internal gap, unchanged at 390**; 1px `--line` |
| Quote bubble | `--ink` at 18.88:1 on `--surface` | `--surface` | `--r-bubble` | 24px/600 in `--font-display`; `--shadow-bubble` |
| Dark bubble | `--on-slab` at 16.54:1 on `--slab` | `--slab` | `--r-bubble` | the same object on the dark side of a pair |
| Demo well | `--ink-body` at 8.61:1 on `--paper` | `--paper` | `--r-well` | sits inside a card, inset by the card's padding |
| Product well | `--on-slab` at 17.76:1 on `--well` | `--well` | `--r-well` | the dark screen inside a light card |
| Delta chip | its own solid, at the 4.5:1 body floor | `--good-weak` or `--danger-weak` | `--r-badge` | **arrow glyph and number, always both** |
| Metric chip (on slab) | `--good-on-dark` at 13.31:1 on `--slab` | `--slab-raised` | `--r-chip` | 12px/500 |
| Section slab | `--on-slab` at 16.54:1 on `--slab` | `--slab` | `--r-panel` | 30px inset from the viewport; re-declares `--focus-color` |

**Every state a control needs.** Rest is the table above. Hover steps the fill one
value: the coral button to `--coral-hot`, the dark button to `--slab-raised`, the
white button to `--paper`. Active repeats hover with no transform — nothing on
this page lifts or scales under a press. Disabled is `--disabled-fill` with
`--disabled-ink` and `cursor: not-allowed`. Focus is `--focus-w` at
`--focus-offset` in `--focus-color`, **and the fill step stays** — both, always.
On the slab, `--focus-color` resolves to the paper token instead, because the ink
ring would otherwise vanish — #1b181c on #1b181c is 1.00:1.
`--focus-color-on-dark` is 16.54:1 on `--slab`.

**The nesting rule has one stated exception, and it is measured.** A nested box
normally takes the outer radius minus its inset. A well does not: the reference
draws a 24px well inside a 12px card at 32px of padding, so the inner corner is
*rounder* than the outer one and the subtraction would yield a negative number.
That is the reference's own geometry rather than a slip — the well reads as a
separate object dropped into the card, which is the point of it — so `--r-well` is
a free value by exception, and it is the only one in the pack.

**Inputs.** The reference paints exactly one — a search field inside a demo well:
`--surface` at `--r-control`, 1px `--line`, a 16px/400 value in `--ink-body`, the
placeholder in `--ink-ghost`, a leading search glyph in `--ink-muted`, and a filled
`--coral` action button seated inside the field's right edge with its label in
`--on-coral`. Focus paints the ring and keeps the border. A textarea is the same box
at `--r-card` with the card's 32px padding. There is no other field type on the page,
and inventing a select or a checkbox here means inventing a value — take the
geometry from this one and the colours from the Palette.

**Empty states.** The reference has none, because every surface on it is a canned
demo. The pack's answer is derived from the parts it does have and is stated so it is
not invented twice: a `--paper` well at `--r-well`, a centred 18px/600 line in
`--ink`, a 16px/400 explanation in `--ink-body`, and one `--coral` button. **No
illustration.** The one thing that may sit above the text is an empty quote bubble at
`--r-bubble` in `--line-quiet` with no shadow — the page's own object, drawn hollow.

**Loaders.** The corpus's only `@keyframes` is Framer's vendor spinner, so there is
no authored loader to measure. The pack's answer: a skeleton, never a spinner —
`--line-quiet` bars at `--r-badge` in the shape of the content that is coming, held
static under `prefers-reduced-motion: reduce` rather than pulsed. A shimmer sweep is
banned: it is a gradient in motion, and this pack's gradients do not move.

**The reference's controls are 36px tall and do not clear the 44px tap floor.**
The pack ships 36px as the measured value and requires the hit area to be padded
to `--tap-min` on touch. That is a correction, not a measurement.

## Hero

The opening viewport is centred, and it is built from five bands stacked in the
frame:

1. A full-bleed `--slab` announcement strip at radius 0, 43px tall, 16px/400 in
   `--on-slab`, one `--coral-hot` link at its end.
2. The floating navigation bar — `--surface`, `--r-panel`, `--shadow-nav`, inset
   from the frame rather than pinned to the viewport edge. It is not a pill:
   `--r-pill` belongs to the nav *items* inside it, and to the capsule scatter.
3. The display line, centred, in `--font-display` at 56px/600/−0.0625em, **with
   platform marks set inline as words**: rounded-square logo chips sitting on the
   baseline inside the sentence, at cap height. This is the hero's whole idea —
   the brands doing the mentioning are typeset into the claim.
4. Behind it, pale routing lines in `--parchment` running from logo chips at the
   frame's left and right edges toward the centre — a wiring diagram in
   `--parchment` at 1.14:1 on `--bg`, which is texture rather than a mark.
5. Two CTAs side by side — `--coral` first, `--ink-strong` second — then one
   tertiary button below at `--r-control`, then a **stack of offset cream cards** peeking from behind
   one another under `--shadow-drift`.

The lede is 18px/400 in `--ink-body`, two lines, centred, and never wider than the
936px content column.

## Responsive

One breakpoint does the work, and it sits **above** 768: 390 and 768 take the same
narrow branch — same display size, same section head, same card padding — and 1440
is the only width that differs from them. What separates 390 from 768 is the frame
alone.

| | 390 | 768 | 1440 |
|---|---|---|---|
| Page gutter | 20px | 20px | the 1116px ruled frame |
| Content column | 350px | 728px | 936px |
| Display | 40px · −0.025em | 40px · −0.025em | 56px · −0.0625em |
| Section head | 34px | 34px | 44px |
| Card padding | **32px** | **32px** | **32px** |
| Cards per row | 1 | 1 | 2, and the two are **not equal width** |
| Grid rules | at the viewport edge | `x=11` and `x=756` | `x=162` and `x=1278` |

**The card keeps desktop padding on a 350px sheet.** 32px of padding on a 350px
card leaves a 286px measure, and the reference accepts that rather than tightening
— it is why the narrow page runs 19,291px tall against the desktop 11,750px. Ship
it; halving the padding at 390 makes a different pack.

**The two-column row is deliberately unequal** — the census measures 410px beside
a wider sibling inside the same 936px column. An equal-column grid reads as a
different, tidier page.

**What sizes against its container, and what answers to the page.**

| Thing | Answers to | How |
|---|---|---|
| The card grid stepping 2 → 1 | CONTAINER | `container-type: inline-size` on the grid, `@container` on the tracks |
| A well inside a card (demo or product) | CONTAINER | container on the card; the well is always the card's width minus its padding |
| A quote bubble in a stack | CONTAINER | the bubble wraps its own question; nothing about it reads the viewport |
| The display and section-head steps | PAGE | the headline answers to the viewport |
| The grid rules and the frame | PAGE | the frame is the page's, and it is the only thing that knows about 1116px |
| The dark slab's 30px inset | PAGE | measured against the viewport, not against a parent |
| Card padding | SELF | **no container answer exists** — it is 32px at every width by construction |

**No horizontal overflow**: `documentElement.scrollWidth` equals the viewport at
1440, 768 and 390, measured with the census running. **Viewport:** `100dvh` for any
full-height surface, never `100vh`.

## Motion tokens

**Read this section before animating anything, because the stylesheet lies.** The
CSS corpus holds one `@keyframes` (Framer's loading spinner — vendor), two
transitions with a duration, and **zero** `prefers-reduced-motion` rules. The real
choreography is JavaScript: **383 elements carry a script-set inline `transform`,
1,057 a script-set inline `opacity`, and 43 compute a `will-change` other than
`auto`.**

| Token | Value | Rule it answers to |
|---|---|---|
| `--dur-state` | 0.2s | UI motion, inside the doctrine's 150–250ms band |
| `--dur-reveal` | 0.4s | MEASURED entrance — exempt from the 300ms UI ceiling |
| `--ease-state` | `cubic-bezier(0.44, 0, 0.56, 1)` | MEASURED |
| `--ease-reveal` | `ease-out` | MEASURED |

**The reduced-motion contract has two halves and CSS is only one of them.** The
token layer collapses both clocks to `0s` under
`@media (prefers-reduced-motion: reduce)`. That does nothing to a transform a
script sets. **The reveal observer must read
`matchMedia('(prefers-reduced-motion: reduce)')` and mount its elements at their
final transform and full opacity**, never animate to them. A pack that ships the
media query alone and calls the contract met has shipped 383 unstoppable
animations.

**The 0.5s colour crossfade is measured and not shipped.** At 500ms it is UI
motion over the doctrine's ceiling; `--dur-state` carries hover instead, on the
measured curve.

Nothing lifts or scales **under interaction** — no hover lift, no press scale, no
parallax. The one lift in the pack is the entrance above, which is a mount and
fires once. There is no scroll clock: no `animation-timeline`, no scroll-linked
transform, and one sticky element.

## Signature motifs

1. **The cut corner.** `--r-bubble` — 24px on three corners, 0 on the top right.
   Measured on all 24 instances of one object. It is a speech-bubble tail drawn by
   subtraction, and it is the pack's whole geometry.
2. **The persistent grid with crosshairs.** Two verticals, horizontals at section
   seams, a plus at every intersection, continuing across the dark band.
3. **The frame that is wider than the content.** 1116px of rule around 936px of
   column. The margin between them is never filled.
4. **Marks typeset inline.** Rounded-square platform chips sitting on the baseline
   inside a heading, at cap height, as if they were words.
5. **The three-stop sweep.** `--coral` → `--periwinkle` → `--parchment` at 90deg,
   measured on the signature gradient; hot to cool to paper, never reversed.
6. **The dark slab cut into the paper.** Inset 30px, `--r-panel`, full width
   otherwise, with the grid running through it.
7. **The capsule scatter.** In the closing band, stadium-radius pills — some
   outlined in `--line-on-slab`, some filled `--coral`, `--periwinkle` or
   `--parchment` — jumbled at angles between logo chips. Many voices, one page.

## Signature element

**The quoted question.** A `--surface` card at `--r-bubble` under
`--shadow-bubble`, holding a stranger's question at 24px/600 in `--font-display`
with the source platform's mark to its left, and — where the page is making the
commercial argument — a `--good-on-dark` traffic figure beside it. It is the one
element the page is remembered by, and it is the one element that may not be
restyled: change its corner, its face or its shadow and the pack is gone. If a
page has no stranger's words to put in it, the page does not want this pack.

## Micro-interactions

- **Hover on a control** steps the fill one value on `--dur-state` with
  `--ease-state`. No lift, no scale, no shadow change.
- **Hover on a quote bubble** raises nothing; it reveals the reply affordance
  inside the card — a `--coral-ink` label that was at `--ink-muted`.
- **Hover on a nav item** fills `--line-quiet` behind it at `--r-pill`.
- **Link hover** moves colour to `--coral-ink`, never to `--coral`, and keeps its
  underline where it had one.
- **The entrance** fades and lifts a band on `--dur-reveal` with `--ease-reveal`,
  staggered by band and never by character. Content is legible before it runs and
  is never gated on it.
- **Focus** paints the ring and steps the fill, together, on every control, on
  both surfaces.
- **A delta appearing** changes its number and its arrow together. Neither alone.

## Bans

- **No word in `--coral`, at any size.** Both directions land under the large-text
  floor of 3:1, so size is not an escape.
  #ffffff on #f96f4b is 2.84:1, and #f96f4b on #fbfaf9 is 2.72:1.
  `--coral-ink` exists for this.
- **No white label on `--coral`.** The label is `--on-coral`.
- **No mint on paper.** `--good-on-dark` is a dark-surface token; a green figure on
  a card takes `--good`.
- **No status by colour alone.** Arrow and number, always both.
- **No shadow on a card that is not one of the four named objects.** Take `--line`.
- **No border-radius outside the measured ladder**, and no second cut-corner
  variant beyond `--r-bubble` and its mirror.
- **No italic anywhere** — the corpus has none, and `em, i` is pinned in the token
  layer.
- **Nothing above weight 700**, and 700 only inside a running line.
- **No lift, scale or parallax under interaction**, and no scroll clock. The
  entrance's single lift is the stated exception, and it fires once on mount.
- **No second accent hue.** The periwinkle is a gradient stop and a dark-surface
  series line; promoting it to a second button colour makes a different pack.
- **No tightening of display tracking at narrow widths.** It relaxes; that is
  measured.
- **No card padding below 32px**, at any width.

## Gotchas

Six corrections. Each is a number the reference produces and the pack refuses.

1. **The primary CTA fails AA and no size saves it.** `#ffffff` on `#f96f4b` is
   **2.84:1** at the 14px/500 the reference ships — under AA and under the 3:1
   large floor. The pack's fix keeps the brand hue exactly and changes the label:
   `#1b181c` on `#f96f4b` is **6.20:1**. Darkening the coral was rejected; a brand
   colour read off a reference is not the pack's to re-step.
2. **The coral cannot be a word.** `#f96f4b` on `#fbfaf9` is **2.72:1** and the
   link token `#ff5d30` on `#fbfaf9` is **2.94:1**, and the reference sets both at
   16px/600 and 14px/500. `--coral-ink` at 4.59:1 on `--bg` is the derived answer.
3. **A card is separated from the field by 1.04:1 and nothing else.** `#ffffff` on
   `#fbfaf9`, with no border and no shadow on any card in the census over
   250×150px. That is not an edge. The pack gives every card a 1px `--line`.
4. **There is no focus indicator at all.** Zero `:focus` rules and zero
   `:focus-visible` rules across 274,355 bytes, plus two `outline: none`
   declarations. The entire mechanism in the token layer is the pack's, including
   the dark-surface re-declaration: the ink ring measures #1b181c on #1b181c at
   **1.00:1** and would have vanished on the band that carries the closing CTA.
5. **The muted step does not read.** `#8a8692` on `#fbfaf9` is **3.41:1** at the
   14px/400 the reference sets it at, 38 instances.
   `--ink-muted` is 5.36:1 on `--bg` and is the step for a word; `--ink-ghost`
   keeps the measured value for bars and rules.
6. **Zero reduced-motion rules against 383 script-set transforms.** The media
   query the pack adds cannot reach them. The JS half of the contract is stated in
   Motion tokens and is not optional.

Two more facts that are not failures but will surprise an implementer: the
controls are **36px** tall and miss the 44px tap floor, so the hit area is padded
rather than the button resized; and the declared amber `#ffc300` **paints
nothing** at any of the three widths, which is why this pack has three status
roles rather than four.
