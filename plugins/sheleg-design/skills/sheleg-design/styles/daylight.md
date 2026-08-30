# Style pack — Daylight

Origin: [taskip.net](https://taskip.net) — read off its live computed styles on
2026-08-15, not transcribed from a screenshot.

A cool near-white field, generous radii, and **one very large soft shadow spent
on a single object per screen**. Ink is a deep blue-black, the accent is a
mid-blue that fills the primary, and the type is Inter Tight at 700 over Manrope
at 400 — a display face that tightens as it grows against a body face that does
not. The whole argument of the pack is openness: nothing is boxed that does not
have to be, and the one thing that floats is the thing the page is about.

Contract: widened — all thirteen headings.

Themes: light + dark — a full theme twin.
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

Choose Daylight for **client-facing portals and the pages that sell them**:
onboarding, workspaces a customer logs into, service dashboards, scheduling and
billing surfaces, and marketing pages for products whose promise is *this will
feel simple*. **Standalone** — it does not ride the SHELEG cinematic layer, and
its one shadow is doing the work a motion layer would otherwise be asked for.

**Not for:** dense operator tooling, anything with more than a handful of
controls per view, developer products sold on precision, or a brand that needs
to read as serious rather than as friendly. At 16px body on 16px radii with a
90px shadow, this pack is warm and roomy; asked to hold a table of forty rows it
reads as a toy.

**Motion ceiling:** no pack ceiling is pinned here, so `MOTION_INTENSITY` is cut by §1's frequency table alone — the dial turns up what is left after that table, and nothing in this pack narrows it further.

## Palette

Ready-made token layer: [`tokens/daylight.css`](tokens/daylight.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#f5f7fa` | page field — cool, and never white |
| `--panel` | `#ffffff` | the card, white **on** the cool field |
| `--panel-2` | `#e8f0fc` | the blue band that changes subject |
| `--ink` | `#151a23` | primary text |
| `--muted` | `#4b5565` | secondary text |
| `--border` | `#d5dbe4` | the seam |
| `--edge` | `#7f8997` | the visual boundary of a **control** |
| `--accent` | `#1f5fb0` | THE single functional accent, and it fills the primary |
| `--tile-1…4` | `#e3ecfb` … `#c8daf6` | four steps of one blue, for stacked bands |

### Floors, and what each colour may mean

Body and secondary text clear AA on the field and on the panel in both
registers. The accent fills the primary control and `--accent-ink` is the text
that sits on it.

**Status is never by colour alone.** Every state is a dot or an icon **plus a
word**. Under deuteranopia `--danger` and `--warn` separate by 1.6 and under
protanopia `--ok` and `--warn` by 6.8 — the green/amber/red triple is the
classic confusion set and no palette solves it, so the word carries the meaning
and the colour reinforces it.

**`--danger` is derived, not measured**, and the token layer says so at the
declaration. The reference is a marketing site and paints no error state, so a
red was authored to clear AA on the field, the panel and its own tint (6.09 /
6.54 / 5.75) rather than sampled. Read it as a pack decision.

**`--info` is the accent value.** A second blue would separate from `--ok` by
less than the palette gate's hard floor, and "running" is this product's own
signal rather than a new colour.

## Type

Two families, and the split is the pack.

- **Display — Inter Tight**, weight 700, tracking `-0.019em`, line-height 1.08.
  It is used from `--t-title` up and nowhere below.
- **Body — Manrope**, weight 400, line-height 1.6. Every sentence.

A third family is a defect. The mono in `--font-data` exists for a figure and a
unit, never for a label and never for a sentence.

Scale: `--t-meta` 12, `--t-body` 16, `--t-card` 22, `--t-title` 28,
`--t-section` 36, `--t-page` 44, `--t-hero` 72. Measures: 62ch prose, 56ch lede.

## Texture & surface

**Elevation is one shadow, and it is a budget.** `--shadow-lift` is 90px of blur
at a −30px spread and it belongs to **one object per view** — the thing the page
is about. `--shadow-1` is the quiet card shadow for everything else, and most
things get neither.

Radii: `--r-control` 10, `--r-card` 16, `--r-pill` 999. The card radius is large
on purpose; it is what makes the field read as roomy rather than as a grid.

**Radius arithmetic when containers nest:** an inner radius is the outer minus
the padding between them. A control inside a card padded `--space-2` is
`calc(16px - 8px)` = 8, not 10 — so the button inside a card is **not** the same
radius as the button beside it, and getting that wrong is the tell that a layout
was assembled rather than machined.

Spacing is a 4px grid. Sections run `clamp(72px, 8vw, 120px)` — this pack
breathes more than any other in the library, and compressing it to save a
scroll is how it stops being itself.

## Components

- **Buttons.** Radius 10, 16px label, weight 500. *Primary:* `--accent` fill,
  `--accent-ink` label, stated on the rule rather than inherited. *Secondary:*
  `--panel` fill, 1px `--edge`. *Ghost:* no fill. **Hover** moves background and
  border only; **active** presses nothing; **disabled** is opacity .45 with the
  label colour kept.
- **Cards / containers.** `--panel` at radius 16 with a 1px `--border` and
  `--shadow-1`. A card is for a *group*; a list of statements takes a seam. The
  one card per view that carries `--shadow-lift` is the hero's object and
  nothing else.
- **Inputs / forms.** Label above at 16/500, input at radius 10 with `--edge`,
  hint below in `--muted`. **Focus** is a 3px ring in `--accent-weak` plus the
  border moving to `--accent`. **Error** puts `--danger` on the border and
  replaces the hint.
- **Navigation.** A `--bg` bar with a bottom seam, no shadow at rest. It gains
  `--shadow-1` when the page scrolls — this is the one pack in the library where
  that is right, because the bar sits on a field rather than on a rule.
- **Loaders.** Skeleton blocks at `--r-control`, filled `--panel-2`, sized to
  the real element. No spinner above 400ms of expected wait.
- **Empty states.** Centred in the card that would have held the data: a
  40px ring in `--border-strong`, one line at `--t-card`, one sentence at 44ch
  in `--muted`, and the action that creates the first record.

## Hero

Two columns at 1.1 : 1 — the argument left, the floating object right. The
object is the only element on the page carrying `--shadow-lift`, and that is the
whole composition: everything else sits flat on the field so that one thing can
lift off it.

Display at `--t-hero`, weight 700, tracking `-0.019em`, capped at **18ch**,
which holds it to **three lines at 1440**. The container that keeps it there is
`--page` 1200 with the left column at 1.1fr. A headline that reaches five lines
is a broken hero, not a long one.

The first viewport must contain: the headline, one lede at 56ch, one primary,
and the object. It must not contain: a second shadow, a second filled control,
or a testimonial — the reference puts proof lower and it is right to.

## Responsive

- **Fluid type.** `--t-hero` ships as `clamp(2.75rem, 5.2vw, 4.5rem)` — 44px at
  390 and 72px at 1385 and above, a slope of 5.2vw. `--t-section` is
  `clamp(2rem, 3.2vw, 2.75rem)`. Body does not scale.
- **Container queries.** Sorted by kind, because only the first has a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | Card head stacking its title and its meta | CONTAINER | `container-type: inline-size` on the card, `@container` on the head |
  | Tile band stepping 4 → 2 → 1 | CONTAINER | container on the band, `@container` on the tracks |
  | Hero going from two columns to one | PAGE | viewport `@media (max-width: 1000px)` |
  | The bar collapsing to a disclosure | PAGE | viewport — the bar is the page's |
  | Section rhythm `clamp(72px, 8vw, 120px)` | PAGE | the page owns it |
  | The lifted object's own shadow softening at narrow | SELF | **no container answer exists** — a container cannot query itself. Keep the viewport query |

- **Collapse.** The hero's two columns stack and the object goes **below** the
  argument, never above it: a 90px shadow at the top of a phone screen is a grey
  smear before the reader has read anything. Nothing overlaps and nothing
  rotates, so there is no unwinding to do.
- **Viewport.** `min-h-[100dvh]` for full-height sections, never `100vh`.

## Motion tokens

One curve, `cubic-bezier(0.2, 0, 0, 1)`. `--dur-state` 0.18s for a meaningful
state change, `--dur-hover` 0.12s for background, border and colour.

No stagger and no scroll-driven reveal. The one shadow is this pack's whole
sense of depth and animating it flattens the effect it exists for.

Reduced motion sets both durations to `0s` at the token layer.

## Signature motifs

1. **The single lifted object.** One element per view carries
   `--shadow-lift`; everything else sits flat.
2. **The blue band.** `--panel-2` full-bleed, used to change subject rather than
   to decorate.
3. **The tile ramp.** Four steps of one blue, for a stacked feature grid that
   reads as one family rather than four cards.
4. **The large radius.** 16 on every card, and it is what makes the field read
   as roomy.
5. **Tight display over loose body.** Inter Tight 700 tracked negative against
   Manrope 400 at 1.6 — the contrast is the pack's voice.

## Signature element

**The one floating object in the hero.** Not the shadow as a style — the
*singularity* of it. A page in this pack is remembered as *the one where that
thing lifts off the page*, and the moment a second element carries the same
shadow the memory has nothing to attach to.

Everything around it is deliberately flat: no second lift, no second fill, no
outline competing for the eye.

## Micro-interactions

- **Hover** moves background, border and colour. Nothing translates and nothing
  scales — this pack's depth is spent already.
- **focus-visible** is a 3px `--accent-weak` ring plus the border at `--accent`,
  identical on a button, an input and a link.
- **Keyboard.** The nav disclosure is a `<details>`, so it opens without script.
  The skip link is the first focusable element and clears the bar.
- **Selected** keeps its state after the pointer leaves; hover does not.

## Bans

- **No second lift.** One object per view carries `--shadow-lift`.
- **No shadow on a button or an input.** Controls are flat here.
- **No third family.** Display, body, and a mono for figures.
- **No status by colour alone.** Dot or icon, plus a word.
- **No compressing the section rhythm** to fit more above the fold. The space is
  the argument.
- **No accent on a large surface.** The accent fills a control and marks a link;
  a full-bleed accent band turns the page into a different product.
- **No testimonial in the first viewport.**

## Gotchas

- **The second shadow is the failure mode, and it arrives by accident.** A card
  component that ships `--shadow-lift` as its default gives every card the hero
  object's weight, and the page loses its focal point without any single change
  looking wrong. Default a card to `--shadow-1` and make the lift opt-in.
- **The object above the fold on a phone is a grey smear.** At 390 the hero
  stacks, and a 90px blur at −30px spread rendered before any text has been read
  is noise. Put the object below the argument on the narrow branch.
- **`--danger` is derived and will drift if it is treated as measured.** The
  reference has no error state; if the reference later ships one, this value is
  the first thing to re-check, and the token layer marks it at the declaration
  so the next reader knows which values are which.
- **The tile ramp is not a chart palette.** Four steps of one blue read as one
  family, which is exactly wrong for four independent series — the reader will
  see an order that is not in the data. For a chart, use the status set plus a
  neutral, or authored series tokens.
- **Radius 16 on a small control looks like a mistake, because it is one.**
  `--r-card` is for cards; a 28px-tall chip at radius 16 is a lozenge. Chips take
  `--r-pill`, controls take `--r-control`.
