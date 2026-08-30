# Style pack — Rimlight

Origin: <https://peppermint.global/services/web-design> (2026), a design studio's
service page selling web design to SaaS and DevTools companies. The site is Webflow:
one shared stylesheet of 230,354 bytes declaring 82 custom properties, and an
interaction engine that ships on the page and drives exactly **one** element. Every
value below was read on 2026-08-24 off **computed styles on the live page** through
CDP at 1440×900 — 487 visible of 562 elements on a 12,410px page — and at a
device-emulated 390×844. Ratios were computed by importing this repository's own
palette gate.

A white field, a cool grey that separates acts, and one near-black act 2,390px tall.
A grotesque for everything a reader reads in sentences and a **monospace for every
piece of chrome** — nav, label, button. The page is square on 84% of its elements,
tracked negative at every size, and its only elevation is **coloured light**: the
primary control wears a sixteen-layer rig, six layers lit and ten pre-declared at
alpha 0, thrown from below and to the left.

The identity in one sentence: **the object is separated from the field by a light
placed behind it, not by a shadow beneath it.**

Contract: widened — all thirteen headings.

Themes: light only — the second block (`[data-surface="dark"]`) is a SURFACE variant, not a theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

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

Choose Rimlight for **a studio's own front door and the pages that sell what it
makes** — design and engineering agencies, product studios, service pages, portfolio
and case-study surfaces, and the kind of B2B page whose argument is craft rather than
a feature list. It suits a page that has to look expensive without a photograph: the
whole budget is type, one blue, and a light.

**Standalone**, and it pins the lowest ceiling in the library beside `bulletin`:
**`MOTION_INTENSITY` above 2 has nothing legal to buy here.** 432 of the 487 visible
elements compute `transition-duration: 0s`, `animation-timeline` appears zero times,
one element is sticky, and the Webflow interaction engine — which is loaded — drives
one element on the whole page. The rig is a *static* light. Animating it is the
single fastest way to turn this pack into a toy.

**Not for:** a product console or anything dense — the reading size here is 20px and
the display is 86px, which is a page that expects to be read once and admired, not
operated. Not for a page whose proof is other people's marks
(`roster`, `nameplate`), and not for a page whose
argument is an accumulating figure (`scoreboard`).

### The fork against [`showroom`](./showroom.md), which is the one a router will get wrong

Both are white, both are product-led, and **both spend a big multi-layer shadow on a
single object** — a router reading "white page, one dramatic elevation" lands on
`showroom` every time. The distinction is what the elevation is made of and what it
is spent on.

`showroom` frames **the application** in a seven-layer *neutral* shadow: the object
lit is a screenshot, and the shadow's job is to make a rectangle sit above a page.
Here the object lit is **a control**, the light is *coloured* — mint, cyan and teal —
and it is thrown from one side rather than dropped from above. `showroom`'s hero puts
the product at real size in the first viewport; this hero has no product in it at
all, only a headline, two controls and an 80px icon tile.

The give-away: delete the shadow from `showroom` and a screenshot floats
unconvincingly. Delete the rig here and the page still reads — it just stops being
this pack, because the light *is* the brand.

## Palette

Copy [`tokens/rimlight.css`](./tokens/rimlight.css) verbatim. Every value there
carries its provenance — MEASURED, SELECTED or DERIVED — and its ratio.

| Role | Token | Value | On `--bg` |
|---|---|---|---|
| Page | `--bg` | `#ffffff` | MEASURED — 23 fills |
| Act separator | `--field` | `#f1f2f3` | MEASURED — 18 |
| Dark act | `--act-dark` | `#1b1b1b` | MEASURED — one 2,390px band |
| Ink | `--ink` | `#1b1b1b` | 17.22:1 — 87 text nodes |
| Secondary | `--ink-soft` | `#6c6e72` | 5.11:1 — DERIVED, see Gotchas |
| Tertiary | `--ink-quiet` | `#6d6d6d` | 5.17:1 — DERIVED |
| Accent | `--accent` | `#5b91ff` | 3.03:1 — **large text only**, ≥ 24px |
| Accent as a word | `--accent-ink` | `#3668d2` | 5.16:1 — DERIVED |
| Bloom | `--glow-mint` | `rgba(31,242,229,.77)` | the layer that does the work |

**The palette is split by field, and that is the pack's central law.** Every one of
the reference's five secondary hues measures 6.5–10.5:1 on the dark act and
1.65–2.65:1 on the white page. They did not fail — **they were designed for the
dark**, and the light field is where they must be held back. So the hues live in
`[data-surface="dark"]`, and on white the page runs on ink, one blue and the light.

**The blue is two tokens because it does two jobs.** `--accent` at 3.03:1 is legal on
a word only at WCAG large text — at this pack's weight 400 that means ≥ 24px, and the
reference spends it at 86px in the headline's first phrase. Anything smaller takes
`--accent-ink`. Using `--accent` for a 16px link is the commonest way to break this
pack while believing you matched it.

**Status is never carried by colour alone**, and it is remapped in the dark act
rather than inherited — the light set measures 1.1–1.5:1 there.

## Type

Two families, and the split is structural rather than decorative: **the monospace is
the chrome.** Archivo carries every sentence a reader reads (102 computed text nodes);
Source Code Pro carries every nav item, every label and every button (43).

| Role | Size | Weight | Line-height | Tracking |
|---|---|---|---|---|
| Hero | 86px → 40px at 390 | 400 | 1.1 | −0.02em → −0.04em |
| Section | 60px | 400 | 1.1 | −0.02em |
| Title | 40px | 400 | 1.1 | −0.02em |
| Card | 32px | 400 | 1.1 | −0.02em |
| Lede | 24px | 300 | 1.4 | −0.02em |
| Body | **20px** | 400 | 1.35 | −0.02em |
| Label (mono) | 16px | 500 | 1.35 | **`normal`** |

**Nothing here is set in bold.** The heaviest weight on the page is 500 and it belongs
to the mono label; the display runs at 400 and the lede at 300. A page that reaches
for 700 to make a headline louder has left the pack — the display is loud because it
is 86px, not because it is heavy.

**The tracking tightens as the display grows, in proportion.** −0.02em at 86px and
−0.04em at the 40px narrow headline: the *smaller* headline is tracked tighter, which
is the opposite of the usual reflex and is measured.

**The mono only looks tracked.** Its `letter-spacing` computes to `normal` on every
label; the openness is the monospace's own advance width. Adding tracking to it is
the trap this pack sets for anyone who matches it from a screenshot — see Gotchas.

## Texture & surface

No texture: no grid, no noise, no pattern. The page is separated by returning to
white, by a `#bcc0c4` hairline, and by entering the dark act.

**Three fields, and the third is an act rather than a theme.** White is the page,
`--field` separates acts, and `[data-surface="dark"]` is one band applied to a
*section* — there is no toggle, the document never inverts, and the light fields above
it are untouched. Apply it to a section and never to `:root`.

**Elevation is light, and there are exactly two exceptions.** `--glow-rig` belongs to
the primary control. `--shadow-tile` and `--shadow-tile-inner` belong to the 80px icon
tile and its 68px inner image. Nothing else on the page carries a shadow at all — 483
of the 487 visible elements compute `box-shadow: none`.

## Components

**Primary control** — `--ink` fill, `--on-ink` label in the mono at 18px/500
uppercase, `--r-glow` (100px), height `--control-h-lg` (60px), and `--glow-rig`. It is
the only object in the pack allowed to wear the rig, and there is **one per
viewport**. Hover raises nothing: the light is static, so hover moves the fill one
step and the rig stays. Disabled drops the rig entirely and takes `--field-2`.

**Secondary control** — transparent, `1px solid --ink-faint`, `--r-pill` (160px),
label in the mono at 16–18px/500 uppercase, height `--control-h` (48px). No fill on
hover; the border goes to `--ink`.

**Icon tile** — `--tile` (80px) at `--r-tile` (20px), `--surface` fill,
`--shadow-tile`, holding a 68px image at `--r-tile-inner` with `--shadow-tile-inner`.
It sits above a hero headline and marks a section; it is never interactive.

**Card** — `--surface` on `--field`, or `--field` on `--bg`, `--r-sm` (12px), no
border and no shadow. In the dark act it is `#242424` on `#1b1b1b` — again separated
by tone, never by a line.

**Input** — `--surface`, `1px solid --ink-faint`, `--r-sm`, 20px body at 400, height
`--tap-min` floor. Focus takes the ring in `--focus-color`. Invalid takes `--danger`
**and** a message.

**Navigation** — transparent over the page at `--nav-h` (88px), mono uppercase at
16px/400 in `--ink-2`, with the two controls right. Not sticky at width; the one
sticky element on the reference is elsewhere.

**Empty states** — a `--r-sm` panel on `--field`, a mono label in `--ink-soft`, one
sentence at `--t-body`, at most one secondary control. **The rig is never spent on an
empty state** — a glowing button in an empty view promises something the view does not
have.

**Loaders** — a skeleton in `--field-2` at the shape's own radius, no shimmer: the
page's whole motion budget is a 0.3s colour transition and a shimmer would be the
liveliest thing on it. No spinner.

Every interactive element takes `--tap-min` (44px) as a height floor. This is a
correction: at 390 the reference has 26 of 37 visible interactive elements under 44px.

## Hero

Full width, not full height: the reference's hero runs 88px to 754px against a 900px
viewport, so the next act's edge shows at rest.

- Field `--bg`, the nav transparent above it at `--nav-h`.
- Centred column, `--page-max` (1440px) with `--gutter` outside it.
- **The icon tile first**, then the headline, then one paragraph, then the control
  pair. That order is the pack's, and the tile is what tells a reader which service
  page they are on before they read a word.
- Headline at `--t-hero` (86px), **two lines**, with the first phrase in `--accent`
  and the rest in `--ink`. A third line means cutting words.
- Paragraph at `--t-body` (20px) in `--ink-soft`, held to roughly 60 characters.
- The control pair: secondary left, primary right, and **only the primary is lit**.

## Responsive

Three widths, measured: 1440, 768 and 390.

- **Hero 86px → 40px at 390**, tracking going −0.02em → −0.04em. The section head does
  not follow it down.
- **Gutter `--gutter` (12px)** at 390 — tight, and measured; the page relies on the
  centred column rather than on air at the edges.
- **Body stays 20px**; the mono label stays 16px, which is the page's most frequent
  size at every width.
- **The rig does not scale.** Its offsets are absolute px and stay so: a 44px bloom
  behind a 60px control reads correctly at 390 because the control does not shrink.
- No horizontal overflow at 390: `documentElement.scrollWidth` equals 390.
- **Container queries.** Sorted by kind, because only the first three have a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | A card grid stepping 3 → 2 → 1 | CONTAINER | `container-type: inline-size` on the grid, `@container` on the tracks |
  | A card stacking its title above its meta | CONTAINER | container on the card |
  | The control pair wrapping to stacked | CONTAINER | container on the pair |
  | Hero display 86px → 40px | PAGE | the headline answers to the viewport, not to its column |
  | The dark act's vertical padding | PAGE | it is a full-bleed act and the page owns its rhythm |
  | Nav collapsing to a sheet | PAGE | the bar is the page's |
  | The rig's own offsets | SELF | **no container answer exists** — a container cannot query itself, and they do not change |

- **Viewport.** `100dvh` for any full-height section, never `100vh` — though this
  pack's hero is deliberately not one.

## Motion tokens

| Token | Value | Spends on |
|---|---|---|
| `--ease` | `ease` | everything; it is what 465 of the transitions name |
| `--ease-out` | `cubic-bezier(0.23, 1, 0.32, 1)` | an entrance, if the page has one |
| `--dur-press` | 0.16s | the press — DERIVED, see below |
| `--dur-fast` | 0.2s | a border or colour change |
| `--dur-base` | 0.3s | the only duration the reference spends at scale (41 elements) |
| `--dur-reveal` | 0.4s | entrance only, and it never gates content |

`--dur-press` is the one motion value not measured: the reference presses at 0.2s and the
doctrine's press band is 100–160ms, so the pack takes the band's ceiling. Everything else
here is the reference's own.

`ease-in` is banned by the doctrine and does not appear in the reference either.

## Signature motifs

- **The rig.** Sixteen shadow layers, six lit and ten held at alpha 0, thrown from
  below-left. It is the pack's whole idea and it belongs to one control per viewport.
- **Square everything else.** 410 of 487 visible elements at `--r-none` — 84%.
- **The mono as chrome.** Every label, nav item and button in Source Code Pro; every
  sentence in Archivo. A reader can tell a control from a statement without reading
  either.
- **Negative tracking at every size**, tightening as the display shrinks.
- **No bold anywhere.** 500 is the heaviest weight on the page and it is a label.
- **The dark act**, entered once, where the reference's colours finally work.

## Signature element

**The lit control.** A near-black pill at 100px radius on a white field, wearing a
sixteen-layer light rig thrown from below and to the left: a white rim, a teal spill,
a cyan throw, two insets that keep it from reading as a sticker, and a mint bloom at
44px of blur offset −14.78px in x.

It is what the page is remembered by, and the reason is that **the light is coloured
and the page is not**. On a surface running entirely on ink, one blue and two greys, a
mint-cyan bloom is the only chromatic event — so the single most saturated thing on
the page is also the thing you are meant to click.

Build one. Two lit controls in one viewport and the light stops meaning *this one*.

## Micro-interactions

- **Primary hover:** the fill moves one step; **the rig does not change**. It is a
  static light and animating it reads as a toy.
- **Secondary hover:** border `--ink-faint` → `--ink`, at `--dur-fast`. No fill.
- **Press:** `--dur-press` (160ms), no travel — nothing on this page moves in space.
  The reference presses at 200ms, which is outside the doctrine's 100–160ms band, so
  the pack takes the band's ceiling rather than the nearest measured value.
- **Focus-visible:** `--focus-w` solid `--focus-color` at `--focus-offset`. Opaque.
- **Link hover:** underline appears; the colour does not change, because on the light
  field a link is already `--accent-ink` and there is nowhere legal to go.
- **Section reveal:** opacity only, over `--dur-reveal`. It never gates content.

## Bans

- **No scroll clock, no parallax, no scrub, no `animation-timeline`.** Zero
  occurrences. `MOTION_INTENSITY` above 2 has nothing to buy.
- **No animated rig.** The light is static. Pulsing, rotating or hover-growing it is
  the one change that turns this pack into a novelty.
- **More than one lit control per viewport.**
- **No `--accent` under 24px.** It is 3.03:1 on `--bg`; a 16px link in it is a word
  below the floor. Use `--accent-ink`.
- **No secondary hue as text on a light field.** All five measure 1.65–2.65:1 there.
  They belong to the dark act.
- **No bold.** 500 is the ceiling and it belongs to the mono.
- **No tracking on the mono.** It computes `normal`; the width is the face's own.
- **No shadow on a card.** 483 of 487 elements carry none.
- **No rounding for friendliness** beyond the three radii the pack states.
- **No `ease-in`.**

## Gotchas

**Two things on this page cannot be read off its stylesheet, and they point in
opposite directions.** The uppercase micro-labels *look* generously tracked and are
not — `letter-spacing` computes to `normal` on every one, and the openness is Source
Code Pro's own advance width, so a pack matched from a screenshot ships a tracking
value that does not exist. And the primary control's elevation *looks* like one soft
shadow and is a sixteen-layer rig with ten slots held at alpha 0 — which reads as
noise in a minified stylesheet and only resolves under `getComputedStyle`.

**The ten dark slots are the interesting half.** Every unlit layer already carries its
offset and blur, so a direction can be lit by moving alpha alone, with no relayout and
no reflow. Whether the reference animates them is not the point — it does not — but
the rig is *built* to be relit, and that is why this pack states it as parts rather
than as one 900-character literal.

**Four corrections travel with the pack, each with its number at the declaration.**

1. *Secondary copy is below every floor.* The reference sets it in `#9d9fa3` on 20
   nodes, and `#9d9fa3` is 2.65:1 on `--bg`. `--ink-soft` holds the hue and clears AA
   on both light fields.
2. *The tertiary grey passes the page and fails the band.* Two measurements, one per
   line, because they disagree:
   `#767676` is 4.54:1 on the page `#ffffff`;
   `#767676` is 4.05:1 on the act separator `#f1f2f3`, which is the field it is most
   often used on.
3. *The secondary palette is not a scheme.* Eight of its twenty-one pairs are tight —
   `orange`/`yellow` at 6.74 OKLab units, `purple`/`accent` at 7.99, `red`/`error` at
   6.68 — so the four status roles were **derived** from the reference's own hues
   rather than adopted from its names, and they separate under normal vision and all
   three dichromacies on each field.
4. *Tap targets.* At an emulated 390×844, 26 of 37 visible interactive elements are
   under 44px tall. `--tap-min` is a floor for every control here.

**The dark act is not a dark mode.** There is no toggle on the reference and no second
palette for the document — one section carries `is--dark` and the rest of the page is
light. Shipping `[data-surface="dark"]` on `:root` inverts a page that was never
designed to invert, and the light field's four statuses measure 1.1–1.5:1 if they come
along unremapped.

**`robots.txt` on this host is stale** — it names a different domain and disallows
`/_next/`, which this Webflow site does not have. The stylesheet is on
`cdn.prod.website-files.com` and is not covered by it. Worth stating because the
honest route was checked before anything was fetched.
