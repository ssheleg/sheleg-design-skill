# Style pack — Bulletin

Origin: [socialchamp.com](https://www.socialchamp.com) — read on 2026-08-17 by
enumerating all 748 URLs in its page sitemap, fetching every one, and reading
the 58 distinct stylesheets they resolve to plus the shared layer its theme
ships. Every frequency quoted below is a count over that whole set.

Warm paper the colour of cheap cream stock, three flat pastel bands cut into it,
and **every card and control drawn as a 1px ink outline standing on a hard
zero-blur ink offset** — a shadow it travels into when you press it. One ink at
`#464646` does four jobs (text, outline, offset, dark band), one orange fills
the primary and marks nothing else, and a geometric display face at 700 sits
over a plain grotesque at 400 with **no tracking at any size**. The page reads as
drawn rather than as composed: nothing is separated by a tint, everything is
separated by a line.

Contract: widened — all thirteen headings.

Themes: light only — the second block (`[data-surface="ink"]`) is a SURFACE variant, not a theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose Bulletin for **front doors whose argument is breadth** — a tool that does
many things across many channels for many clients, sold cheerfully to a small
team or an agency: social and content platforms, scheduling and inbox products,
all-in-one SMB SaaS, marketplaces of small features. It is the pack for a page
that has to hold twelve sections, a logo wall, a platform rail and a feature
grid without any of them reading as filler.

**Standalone**, and it pins its own ceiling: **`MOTION_INTENSITY` above 3 has
nothing legal to buy here.** The reference's entire motion budget across 748
pages is an entrance fade, a 0.12s press and a 0.3s hover — no scroll clock, no
parallax, no scrub, no pinning. The depth in this pack is drawn, not animated,
and animating it is what flattens it.

**Not for:** anything sold on gravity — enterprise security, financial
infrastructure, clinical or regulated surfaces; dense operator tooling; or a
developer product whose buyer reads code. An outlined card on a hard orange
offset is friendly by construction, and a friendly SOC 2 page is a broken one.

### The two forks, and they are on different axes

**Against [`pigeonhole`](./pigeonhole.md) — the register.** Both are cheerful,
both are pastel, and both are about a person handling many channels at once, so
a brief that says *"one inbox for every network"* reaches either. The pastel is
what separates them. In `pigeonhole` it is a **taxonomy**: a chip the size of a
word, bound to a named category, and the argument points *inward* — your chaos,
filed. Here it is a **band**: a full-bleed act divider carrying no meaning of
its own, and the argument points *outward* — one thing you write reaches twelve
places. The one-line test: **does the colour name a category, or divide an act?**

**Against [`orchard`](./orchard.md) — the surface.** Both are warm and modular
and a thumbnail separates neither. `orchard` is a stack of rounded slabs inset
from the field with a 55px gap and **no outline**; separation there is negative
space. Here every object sits *on* the field behind a drawn 1px edge with a hard
offset under it; separation is a line. The test: **is the object separated by a
gap or by a drawn edge?** If the answer is a gap, this is the wrong pack.

## Palette

Ready-made token layer: [`tokens/bulletin.css`](tokens/bulletin.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role | On `--bg` |
|---|---|---|---|
| `--bg` | `#fcfaf4` | the paper — warm, and never white | — |
| `--surface` | `#ffffff` | the card, white **on** the paper | — |
| `--ink` | `#464646` | text, outline, offset, dark band | 9.04:1 |
| `--ink-strong` | `#333333` | the card head | 12.10:1 |
| `--ink-soft` | `#666666` | meta and secondary copy | 5.50:1 |
| `--ink-faint` | `#7c8697` | icon fill and disabled label **only** | 3.52:1 |
| `--accent` | `#ff6900` | THE single accent — a fill and a mark | 2.77:1 |
| `--action` | derived from `--accent` | the filled control under a label | 4.78:1 |
| `--band-peach` / `--band-sky` / `--band-lilac` | `#feefdd` / `#c4d8f9` / `#cdc5ed` | one flat band per act | — |

### Floors, and what each colour may mean

The ink clears AA on the paper **and on every band** — 5.76:1 on the lilac,
6.53 on the sky, 8.36 on the peach — which is why the bands can be saturated
without a second text colour. That is the strongest thing about this palette
and the reason the pack survives being cheerful.

**The accent is not a word.** At 2.77:1 on the paper it sits below the 3:1
non-text floor, so it fills, tints and marks, and the token layer declares it
`@role non-text`. `--action` is the fill that may carry a label; `--link` is the
only orange that may be a link.

**`--action` and `--link` are derived, and the token layer says so at the
declaration.** The reference sets white on `#ff6900` for every primary CTA on
all 748 pages (2.89:1) and in-content links in `#f16a4b` (2.91:1) — both under
every WCAG floor including large text, so no type size rescues either. The
derivation keeps the measured hue and moves only its lightness. Read them as
pack decisions; the Gotchas carry the numbers.

**Status is never by colour alone.** All four statuses are selected rather than
measured — a marketing site paints no error state — and each is a step of a hue
the reference already carries. Under deuteranopia `--danger` and `--warn`
separate by 0.7 and `--good` and `--info` by 4.8; the green/amber/red triple is
the classic confusion set and no palette solves it. Every state is an icon or a
dot **plus a word**, and the word is the message.

## Type

Two families, and a weight inversion that is the pack's voice.

- **Display — Bricolage Grotesque**, weights 700 and 800, line-height 1.1 at the
  hero and 1.2 at a section head. Written with `"Alexandria"` behind it, because
  that is the face the reference's theme sets on every heading before the page
  overrides it.
- **Body — DM Sans**, 400 for prose, 500 for a strong run, line-height 1.3.

**The control label is heavier than the headline.** Buttons are the display face
at **800** while the hero is 700 — measured, deliberate, and the single cheapest
way to make a page read as this pack rather than as a generic warm landing.

**Tracking is zero at every size.** The reference sets `letter-spacing` seven
times in 58 bundles and never on a heading. A negative track on the display face
is the fastest way to stop this pack looking like itself.

Scale: `--t-2xs` 12, `--t-xs` 13, `--t-sm` 14, `--t-body` 16, `--t-lede` 21,
`--t-card` 20 at weight 600, `--t-title` 32, `--t-section` 42, `--t-page` 48,
`--t-hero` 84. Measures: 60ch prose, 46ch lede.

## Texture & surface

**Elevation is a hard offset and it never blurs.** Across the 58 bundles the
reference draws 185 zero-blur ink offsets against roughly 50 blurred shadows,
and every blurred one is in third-party chrome. The blur is the tell: a 15px
soft shadow anywhere in this pack turns it into a different, tireder page.

The offset grows with the object and the spread is the size dial —
`--shadow-1` 2px for a chip, `--shadow-2` 3px for a control, `--shadow-3` 4px
for a card, `--shadow-4` 4px at 3px spread for the one framed panel per page.
Every one of them is paired with a 1px `--line` outline; an offset with no
outline reads as a rendering bug.

Radii, by frequency: `--r-md` 12 carries the page (87 declarations), then
`--r-pill` 50 and `--r-xs` 5 (58 each), `--r-sm` 8 (46), `--r-lg` 16 and
`--r-2xl` 24. This is a rounded pack; a square corner belongs to nothing here.

**Radius arithmetic when containers nest:** an inner radius is the outer minus
the padding between them, floored at `--r-xs`. A control inside a card at
`--r-2xl` padded `--space-6` computes negative, so it takes `--r-xs` — not the
card's 24, which is the tell that a layout was assembled rather than machined.

Spacing is a **5px grid**, not a 4px one: 10 / 15 / 20 / 30 / 50 / 70 carry
every gap and section pad in the reference. The one exception is 12px, the gap
between a control's label and its icon, and it is a token of its own.

## Components

- **Buttons.** Height 56 (40 small), radius `--r-md`, display face at 800, icon
  gap 12. *Primary:* `--action` fill, `--on-action` label, 1px `--line`,
  `--shadow-2`. *Secondary:* `--surface` fill, `--ink` label, same outline and
  offset. **Hover** moves the fill to `--action-hover` and translates the control
  by `--press-travel` while the offset drops to `--shadow-press`; **active**
  translates by `--press-travel-active` and the offset goes to `none`;
  **disabled** is opacity .45 with the outline kept and the offset removed,
  because a disabled control that still stands proud invites the press.
- **Cards / containers.** `--surface` or one tinted fill at `--r-lg`, 1px
  `--line`, `--shadow-3`, padding `--space-6`. A card is for a *group*; a list
  of statements takes a rule. The tile grid is the exception where hover
  **grows** the offset to `--shadow-3-wide` instead of pressing it — see the
  Gotchas, because mixing the two moves is the way this pack breaks.
- **Inputs / forms.** Label above at 16/500, input height 52 at `--r-md` with a
  1.5px `--line`. **Focus** is `--focus-w` solid `--focus-color` at
  `--focus-offset`, identical on every control. **Error** puts `--danger` on the
  outline and replaces the hint with a sentence; the colour never carries it
  alone.
- **Navigation.** Sticky, `--surface` fill, height `--nav-h` 96, no offset at
  rest and none on scroll — the bar is the one surface in the pack that stays
  flat. An open item takes `--ring-open`, an inset ring, so its box does not
  shift by 1.5px as it opens. The dropdown is a `--surface` sheet with a 1.5px
  bottom `--line` and `--dropdown-min-h` 420.
- **Loaders.** *Pack decision — the reference has none.* Skeleton blocks at the
  real element's radius, filled `--band-lilac-soft`, with the outline kept and
  the offset removed: a skeleton that casts a shadow reads as content that has
  arrived. No spinner under 400ms of expected wait.
- **Empty states.** *Pack decision.* Centred in the card that would have held
  the data: one 60px round outlined chip at `--r-pill` with `--shadow-2-wide`,
  one line at `--t-card`, one sentence at 46ch in `--ink-soft`, and the primary
  that creates the first record. The chip is the pack's own motif doing the work
  an illustration would otherwise be asked for.

## Hero

Centred, single column, over the paper — not over a band. The display sits at
`--t-hero` 84 / weight 700 / line-height 1.1 with **no tracking**, capped at
**22ch**, which holds it to **two lines at 1440**. The container that keeps it
there is `--content-max` 1440 with the headline column at 60% of it. A headline
that reaches four lines is a broken hero, not a long one.

The first viewport must contain: the headline, one lede at 46ch, one primary and
one secondary side by side, and the platform rail — the row of small outlined
round chips at `--r-pill` with `--shadow-2-wide` that says how many channels
this thing touches. That rail is the argument, and putting it below the fold is
the most common way to build this hero wrong.

It must not contain: a band (the first colour change earns its place at section
two), a testimonial, or a second filled control. Two orange fills in one
viewport and neither is the primary.

## Responsive

- **Fluid type.** `--t-hero` ships as `clamp(2.75rem, 6vw, 5.25rem)` — 44px at
  390, 84px at 1400 and above, a slope of 6vw. `--t-page` is
  `clamp(2rem, 3vw, 3rem)`. Body does not scale. The clamp is a **correction**:
  the reference steps 84 → 40 at 767 and back up to 44 at 478, so its tablet
  headline is smaller than its phone headline. See the Gotchas.
- **Container queries.** Sorted by kind, because only the first has a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | Card head stacking its title above its meta | CONTAINER | `container-type: inline-size` on the card, `@container` on the head |
  | Tile grid stepping 4 → 2 → 1 | CONTAINER | container on the grid, `@container` on the tracks |
  | The platform rail wrapping its chips | CONTAINER | container on the rail |
  | Hero going centred-wide to centred-narrow | PAGE | viewport `@media (max-width: 991px)` |
  | Nav collapsing to a sheet | PAGE | the bar is the page's |
  | Section band padding 70 → 30 | PAGE | the page owns its rhythm |
  | A card's own offset shrinking 4px → 2px at narrow | SELF | **no container answer exists** — a container cannot query itself. Keep the viewport query |

- **Collapse.** The breakpoints are 991 / 767 / 478, measured. Below 767 the
  hard offset drops one step everywhere: 4px of ink beside a card on a 390px
  screen is 1% of the viewport spent on a shadow. Nothing in this pack overlaps
  or rotates, so there is no unwinding to do — the bands stay full-bleed and the
  outlines stay on.
- **Viewport.** `min-h-[100dvh]` for full-height sections, never `100vh`.

## Motion tokens

One curve, `ease`, measured off the reference's own press transition, plus the
doctrine's `--ease-out` for an entrance. Durations: `--dur-press` 0.12s,
`--dur-hover` 0.15s, `--dur-base` 0.3s, `--dur-panel` 0.4s for the nav sheet,
`--dur-reveal` 0.5s for an entrance that never gates content.

**The press is a conserved quantity.** The control translates by
`--press-travel` 2px exactly as its offset shrinks from 3px to 1px, so the total
ink displaced stays constant and the control appears to move rather than to
restyle. At `:active` it travels 3px and the offset goes to nothing — the button
has bottomed out. Getting the two halves out of step is what makes a copy of
this pack feel cheap.

Only `transform`, `box-shadow` and `background-color` move. No stagger, no
scroll-driven reveal, no parallax.

Reduced motion sets every duration to `0s` and both travels to `0px` at the
token layer: the control still changes fill and still shows its focus outline,
and nothing moves.

## Signature motifs

1. **The outlined offset.** 1px `--line` plus a hard zero-blur ink offset, on
   every card, control, chip, avatar and media frame.
2. **The band.** One flat pastel, full-bleed, per act — used to change subject,
   never to decorate, and never a gradient.
3. **The round chip.** A 60px outlined circle at `--r-pill` with
   `--shadow-2-wide`, for a platform, an integration or an avatar. The rail of
   them is how this pack says "many".
4. **The framed panel.** One `--surface` block per page at `--r-2xl` with
   `--shadow-4` and 70px of padding, holding the page's densest claim.
5. **The heavy label.** The display face at 800 inside controls, above the
   headline's own 700.

## Signature element

**The press.** Not the offset as a style — the *travel*. A page in this pack is
remembered as *the one where the buttons are physical*: they stand 3px proud of
the paper, sink 2px under the pointer, and bottom out flat when clicked. It is
the only thing in the pack that moves, and that is why it registers.

Everything around it is deliberately still: no entrance beyond a fade, no hover
lift on text, no motion on the nav. The whole motion budget is spent on one
control so that pressing it feels like something.

## Micro-interactions

- **Hover on a control** presses: fill to `--action-hover`, translate
  `--press-travel`, offset to `--shadow-press`. **Hover on a tile** does the
  opposite: the fill saturates and the offset grows to `--shadow-3-wide`. Two
  moves, and each belongs to exactly one kind of object.
- **focus-visible** is `--focus-w` solid `--focus-color` at `--focus-offset` —
  an outline rather than a ring, because the shadow slot is already spent.
  Identical on a button, an input, a link and a chip; the reference does this
  and it is right to.
- **Hover and focus-visible share one rule.** Measured in the reference, and
  worth keeping: a keyboard user sees the press.
- **Keyboard.** The nav disclosure opens without script. The skip link is the
  first focusable element and clears `--nav-h`. Nothing on the keyboard path
  animates.
- **Selected** keeps its state after the pointer leaves — `--accent-wash` fill
  with the outline at full weight; hover does not.

## Bans

- **No blur on any elevation.** The offset is 0-blur ink. One soft shadow and
  the pack is gone.
- **No offset without an outline.** A hard shadow under an edgeless box reads as
  a rendering fault.
- **No second orange fill in one viewport.** The accent fills the primary and
  nothing else on that screen.
- **No accent as a word.** It is a fill and a mark; `--link` carries links.
- **No tracking.** Not on the display face, not on a label, not on a micro-cap.
- **No gradient in a band.** The bands are flat, and a gradient reads as a
  different product.
- **No status by colour alone.** Icon or dot, plus a word.
- **No motion beyond the press and a fade.** No parallax, no scrub, no sticky
  choreography, no marquee.
- **No white page.** White is a card; the field is `--bg`.

## Gotchas

Eight traps, and the first three are corrections to the reference rather than
warnings about it.

1. **White on the orange fails every contrast floor, and it is the site's
   primary CTA.** `#ffffff` on `#ff6900` is 2.89:1 — under AA for body text
   (4.5:1) and under the large-text floor (3:1), so raising the label to 24px
   does not save it. The pack ships `--action`, the same hue darkened in oklab
   until white clears AA at 4.99:1. If you keep the measured orange under a
   label, the label must be `--on-accent` and at least 18.66px at weight 700 —
   and even then you have 3.27:1, which is large-text-legal and nothing more.
2. **The reference's secondary body text is 3.52:1.** `#7c8697` is set as 18px
   DM Sans 400 in 176 declarations across the site, which is body copy below the
   AA floor. In this pack that value is `--ink-faint` and it is an icon fill and
   a disabled label; secondary copy is `--ink-soft` at 5.50:1.
3. **In-content links are 2.91:1.** `#f16a4b` carries links and divider rules in
   the reference. As a rule it is fine; as a word it is not, so `--link` is the
   derived value and the underline is not optional.
4. **The hero type ramp is not monotonic.** The reference steps 84px → 40px at
   `max-width: 767px` → 44px at `max-width: 478px`, so its tablet headline is
   *smaller* than its phone headline. Copy the breakpoints, not the values: the
   pack's `clamp()` is the fix, and it is the reason `## Responsive` states a
   slope.
5. **The reference ships no reduced-motion branch at all** — zero occurrences of
   the query across 58 page bundles and the entire shared layer, while the press
   translates and the nav sheet slides. The token layer's
   `prefers-reduced-motion` block is required, not optional, and it is the one
   part of this pack that has no measurement behind it because there was nothing
   to measure.
6. **The two hover moves cancel each other if you mix them.** A control presses
   *into* its shadow; a tile grows *out of* it. Give a card the button's press
   and the grid stops reading as a set of objects; give a button the tile's
   growth and the click has no feedback. One move per kind of object, decided
   once.
7. **`border-radius: inherit` is load-bearing here and it is easy to lose.** The
   reference uses it 80 times, because a media frame at `--r-md` with
   `overflow: hidden` needs its image to round with it. Drop it and every
   thumbnail grows square corners inside a rounded outline — a defect that looks
   like a browser bug rather than a CSS one.
8. **This field sits in the warm-cream default cluster, and that is a
   measurement.** `#fcfaf4` with an orange accent is close to the first of the
   three looks generated design falls into by itself. It is not that look: there
   is no serif, the accent is a saturated orange rather than terracotta, and the
   elevation is a hard ink offset, which none of the three defaults carry. Say
   which of the two you are shipping — if a page arrives here without reading
   this pack, it is the default talking.
