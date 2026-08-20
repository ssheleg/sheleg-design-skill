# Style pack — Almanac

Origin: [auxia.io](https://www.auxia.io) — measured 2026-08-16 from the token
layer the reference publishes in its own stylesheet.

**Oatmeal paper, not white.** `#f0efe3` is the reference's own `neutral--white`,
and it is the whole first impression. Seams are **2px and 4px — there is no 1px
anywhere**, so structure is read by mass rather than by contrast. The display
runs to 104px at weight 500 with a **line-height below one**, which locks the
lines of a headline into a block. Uppercase mono tags are notched through the
edges of drawn boxes. One object per page floats, on a four-stop shadow whose
deepest stop is 162px of blur.

Contract: widened — all thirteen headings.

Themes: light + dark — a full theme twin.
Rank: unordered — 4 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose Almanac for **pages that assert a category**: a company saying *this is
what this kind of thing is*, a manifesto page, a product whose argument is
editorial rather than functional, and any surface where the headline is the
design. **Standalone.**

**Not for:** dense product UI, dashboards, anything with a table in it, or a
page whose job is to be scanned rather than read. A 104px display and a 2px grid
need room; at 14px in a sidebar this pack has nothing to offer. It is also the
wrong pack for a product sold on precision — oatmeal and 24px radii read as
warmth, not as accuracy.

## Palette

Ready-made token layer: [`tokens/almanac.css`](tokens/almanac.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--bg` | `#f0efe3` | the field — the reference's own oatmeal |
| `--panel` | `#f7f7f0` | a card: a step up, so an object reads as lifted paper |
| `--panel-2` | `#e2e1d3` | the deeper oatmeal that changes subject |
| `--ink` | `#232323` | primary text — the reference's own |
| `--muted` | `#5c5b52` | secondary text |
| `--border` | `#bebdad` | the seam, **at 2px** |
| `--edge` | `#858370` | the visual boundary of a **control** |
| `--accent` | `#1f5fb0` | THE single accent, and it fills the primary |
| `--warn` | `#993f0e` | the reference's orange, darkened until it carries a word |

### Floors, and what each colour may mean

Seam values sit far under a hairline pack's, and that is not a defect: at 2px
they are read by mass. Neither seam carries meaning alone — every panel edge in
this pack has a mono tag notched into it, which is the reference's own device.

**Status is never by colour alone.** Every state is a mono tag or a dot **plus a
word**. Under protanopia `--ok` and `--warn` separate by 5.6 and `--danger` and
`--ok` by 5.7, and under tritanopia `--accent` and `--ok` by 8.0 — the word
carries the meaning and the colour reinforces it.

### Three values that are pack decisions rather than measurements

**The accent is not the reference's `#0b4fff`.** That value measures **4.46 on
the reference's own deeper oatmeal** — under AA on a ground it lands on. This is
the first ported reference that was already blue, so what happens here is a
shift inside one hue rather than a change of hue.

**The orange has exactly one home, and the measurement chose it.**
`#fa6838` is **2.32 on the oatmeal** and **6.65 on the near-black**. So it
carries a word in the dark register and nowhere else; on the light register the
warn role is the same orange darkened until it clears.

**`--danger` is derived, and it is a crimson rather than a red.** The reference
paints no error state. An orange-red beside this pack's burnt-orange warn
measured **6.4 apart at full colour** against the palette gate's hard floor of
10.0 — two semantic states in one colour, which no secondary encoding excuses.
It is moved along the hue until it separates, and the token layer marks it
derived at the declaration.

## Type

Two families, and one of them only ever shouts in capitals.

- **Display and body — Schibsted Grotesk.** The reference sets everything in a
  licensed grotesk that cannot be bought to check a stylesheet against, so it is
  **named as a substitute rather than approximated silently**: a neo-grotesk with
  the same medium-weight display behaviour. Weight **500 is the whole weight
  story** — it appears on 29 of the reference's selectors against 700 on eight.
- **Data — IBM Plex Mono Medium**, the reference's own, at the one weight it
  ships. It appears on 34 selectors and **every one of them is uppercase**,
  which is exactly the count of `text-transform: uppercase` rules. The mono is
  the label voice and it never says a sentence.

Scale: `--t-meta` 12, `--t-body` 16, `--t-card` 24, `--t-title` 32,
`--t-section` 48, `--t-page` 64, `--t-hero` 104. Tracking `-0.03em` on the
display — 17 of the reference's 33 tracking declarations. Line-height **0.95**
on the display, and it is the pack.

Measures: 62ch prose, 52ch lede.

## Texture & surface

**Seams are 2px, and there is no 1px anywhere in the reference.** Structure is
read by mass. Radii cluster at `--r-control` 8, `--r-card` 16 and `--r-lg` 24,
with a `100vw` pill written the way the reference writes it.

**One object floats per page**, on `--shadow-1` — a layered shadow rather than a
single stop, four stops deep, the deepest 162px of blur. It is the pack's only
shadow token and it is re-declared for the dark theme at 30–40% instead of 2–5%,
because a shadow tuned for paper vanishes on a dark field. A second floating
object is the fastest way to lose the effect.

**Radius arithmetic when containers nest:** an inner radius is the outer minus
the padding between them. A control inside a card padded `--space-4` is
`calc(16px - 16px)` = 0 — and the honest reading of zero is *this control should
be square here*, not *give it 8 anyway*. At `--r-lg` 24 with `--space-2` the
inner is 16, which is why the card radius and the panel radius are one step
apart rather than two.

Spacing is a 4px grid; sections run `clamp(64px, 7vw, 112px)`.

## Components

- **Buttons.** Radius 8, 16px label, weight 500, 2px border where bordered.
  *Primary:* `--accent` fill with `--accent-ink`. *Secondary:* no fill, 2px
  `--edge`. *Ghost:* no fill, no border. **Hover** moves the fill away from the
  field; **active** presses nothing; **disabled** is opacity .45.
- **Cards / containers.** A **drawn box**: 2px `--border` at `--r-card`, on
  `--panel`. Every box carries a mono tag notched through its top edge — that is
  the pack's own device and a box without one looks unfinished. Use a box for a
  *thing*; a list of statements takes a 2px rule.
- **Inputs / forms.** Label above at 16/500, a 2px `--edge` field at radius 8,
  hint below in `--muted`. **Focus** is a 3px `--accent-weak` ring plus the
  border at `--accent`. **Error** puts `--danger` on the border and replaces the
  hint.
- **Navigation.** A bar with a 2px bottom rule, no shadow, no fill change on
  scroll. Nav items are uppercase mono.
- **Loaders.** Blocks at `--r-control` filled `--panel-2`, sized to the real
  element. No shimmer.
- **Empty states.** Inside a drawn box with its tag: one line at `--t-card`, one
  sentence at 44ch, and the action. The tag says what is absent.

## Hero

**The display is the page.** At `--t-hero` with a line-height of 0.95 the
headline is a block rather than a sentence, drawn inside a 2px box with an
uppercase mono tag pulled up through its top edge. Below it, one full-bleed
inverted band.

Display capped at **13ch at the top size**, which locks it to **three lines at
1440**. On a phone that cap is wrong and must be released: at 40px in a 346px
column, 13ch is four lines — a measure tuned for one size applied at every size.
The column is the constraint below 620.

The first viewport must contain: the mono tag, the display block, the promise,
its limit, and one primary. It must not contain: a second floating object, a
photograph, or a logo wall.

## Responsive

- **Fluid type.** `--t-hero` ships as `clamp(2.5rem, 7.2vw, 6.5rem)` — 40px at
  390 and 104px at 1444 and above, a slope of 7.2vw, which is the steepest in
  the library and is what a 104px ceiling requires. `--t-section` is
  `clamp(2rem, 4vw, 4rem)`. Body does not scale.
- **Container queries.** Sorted by kind, because only the first has a container
  answer:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | A drawn box's rows going from two columns to one | CONTAINER | `container-type: inline-size` on the box, `@container` on the rows |
  | The tag row wrapping inside a box | CONTAINER | container on the box, `@container` on the tag row |
  | The display's 13ch cap being released | PAGE | viewport `@media (max-width: 620px)` — the cap is tuned to the page's width |
  | The inverted band's full-bleed | PAGE | the page owns it |
  | The floating object's own four-stop shadow at narrow | SELF | **no container answer exists** — the shadow is on the element that establishes the container. Keep the viewport query |

- **Collapse.** The notched tag's inset changes with the box's padding and must
  move with it, or it detaches from the edge it is notched through. Nothing
  rotates and nothing overlaps otherwise.
- **Viewport.** `min-h-[100dvh]`, never `100vh`.

## Motion tokens

One curve, `cubic-bezier(0.16, 1, 0.3, 1)`. `--dur-state` 0.16s, `--dur-hover`
0.12s. An entrance is allowed for the one floating object and for nothing else.

Reduced motion sets both durations to `0s` at the token layer.

## Signature motifs

1. **The oatmeal field.** Not white, and it is the first thing a reader sees.
2. **The 2px seam.** No 1px anywhere; structure is read by mass.
3. **The notched mono tag**, pulled up through the top edge of a drawn box.
4. **Line-height below one.** The display's lines lock together into a block.
5. **The inverted band.** Full-bleed, in the pack's own dark, changing subject
   rather than decorating.
6. **One floating object**, on four stacked shadow stops.

## Signature element

**The display block in its drawn box, with the tag notched through the top
edge.** One headline, set at 104px with a line-height under one so the lines
lock, inside a 2px rectangle, with an uppercase mono label breaking the frame it
sits in.

It carries the pack because it is three of the motifs at once — the mass-read
seam, the notch, and the sub-one line-height — arranged so that the first thing
a reader meets is a *shape*, not a sentence.

## Micro-interactions

- **Hover** moves fill, border and colour. No transform.
- **focus-visible** is a 3px `--accent-weak` ring plus the border at `--accent`,
  identical on every control.
- **Keyboard.** The nav disclosure is a `<details>` and works with script off.
- **Selected** is the mono tag inverting — the tag's ground and ink swap —
  rather than a fill appearing.

## Bans

- **No 1px anywhere.** The reference has none and the pack is read by mass.
- **No second floating object.**
- **No drawn box without its tag.**
- **No sentence in the mono.** It is the label voice.
- **No weight 700 as the default emphasis.** 500 is the pack's weight; 700 is
  rare and deliberate.
- **No status by colour alone.**
- **No white field.** The oatmeal is the identity; a white version of this pack
  is a different pack.

## Gotchas

- **The dark register was the reference's navy and it was wrong.** `#080331` is
  in auxia's own palette and used as a full-bleed band, so borrowing it looked
  principled. A dark theme is dark, and that one was blue. The register is a warm
  near-black now — the oatmeal's opposite rather than a different hue family — so
  the paper identity survives the inversion instead of becoming another company's
  page. **Every ratio was re-measured against the new ground; a number carried
  over from the navy is a number that used to be true.**
- **A band a shade off its own ground is not a band.** The first dark cut made
  the band `#050121`, a step under the canvas, and in the browser it vanished
  while the lighter `washed` sections shouted — the page's hierarchy came out
  backwards. **The band is always the OTHER ground:** the oatmeal on the dark
  register, the near-black on the light one.
- **The 13ch display cap is a desktop measurement and breaks on a phone.** At
  40px in a 346px column it produces four lines. Release it below 620; the
  column is the constraint there, not the character count.
- **`--warn` is two different colours and swapping them is silent.** `#993f0e`
  on the light register and `#fa6838` on the dark are the same orange at two
  steps, because the bright one is 2.32 on oatmeal. Using the bright value on the
  light field ships a warning nobody can read, and nothing on screen looks
  broken.
- **`--danger` is derived and it is a crimson on purpose.** If it is "corrected"
  towards a conventional red it will collide with this pack's burnt-orange warn
  and the palette gate's hard floor will fail the build — which is the check
  working, not a nuisance.
