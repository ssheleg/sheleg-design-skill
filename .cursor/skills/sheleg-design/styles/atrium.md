# Style pack — Atrium

Origin: **functionhealth.com** (2026), a production consumer-health marketing
site. Every value below was read off its live token layer and computed styles,
not eyeballed. A warm daylight field of cream, one terracotta accent, a
light-weight serif that speaks in italic asides, and photography seen through
**fluted glass**. It reads like the lobby of a very good clinic: bright, calm,
unhurried — a serious clinical claim delivered without a single sterile
surface.

Contract: widened — all thirteen sections. The four that were held back until
1.46.0 are now written from the reference rather than from the token layer,
which is the only way they were ever going to be honest: `## Components` is
`functionhealth.com`'s own single control class and its four skins,
`## Hero` is the numbers of its opening viewport, `## Responsive` is its 184
media queries counted, and `## Signature element` names what Signature motifs
already measured. Read on 2026-08-20 from `/_astro/utilities.*.css` and
`/_astro/PageSections.*.css`; every value carries where it came from.

Themes: light only — no second block of any kind ships here.
Rank: unordered — 3 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose this pack for **consumer health and premium care**: longevity and
diagnostics, wellness and testing subscriptions, clinics and telehealth,
insurance alternatives, high-trust DTC where the buyer must feel both *this is
medically serious* and *this will not frighten me*. It generalizes to any
premium consumer subscription that sells calm authority rather than speed.

It **rides the SHELEG cinematic layer, but at low amplitude**: one continuous
ambient effect in the hero, and below it nothing is scroll-scrubbed at all. The
motion budget is spent entirely above the fold; the rest of the page earns
attention with rhythm and type. If a section below the hero wants a scrubbed
instrument, the answer is usually a Lottie diagram that plays once.

The defining constraint is the field: **one continuous cream page, no dark
bands**. Nearly every section on the reference sits on the same `--bg`. Section
boundaries are made by vertical rhythm and a change of layout — never by
flipping the background dark, which is the reflex that makes generated pages
read as a stack of unrelated slabs.

## Palette

Ready-made token layer: [`tokens/atrium.css`](./tokens/atrium.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role — every ratio in this column is on `--bg` |
|---|---|---|
| `--bg` | `#FEF9EF` | the daylight field — this system's "white" |
| `--surface` | `#F5EEE1` | the one step up: cards, wells, footer, CTA band |
| `--surface-ink` | `#2A2B2F` | the ONE inverted surface (media wells, banner) |
| `--line` / `-strong` / `-ink` | `#D1C9BF` / `#737373` / `#2A2B2F` | hairline / input border / ghost-control border |
| `--ink` / `--ink-2` / `--ink-3` | `#2A2B2F` / `#515151` / `#737373` | headings · 13.5:1 / body · 7.6:1 / metadata · 4.5:1 |
| `--accent` | `#B05A36` | THE signal — terracotta, one per page |
| `--accent-tint` / `--accent-ink` | `#F6E9DC` / `#FEF9EF` | 10% wash / text **on** the accent |
| `--good` (`-tint`) | `#79BD8B` (`#F1F3E5`) | fills and icons only — 2.1:1, never a word |
| `--info` | `#488AD5` | 3.4:1 — large text and UI marks only |
| `--danger` | `#DB0000` | 5.0:1 — the one semantic that may be text |

Three contrast facts decide most of the layout, and all three are easy to
violate by accident:

- **The accent changes grade with its ground.** `--accent` on `--bg` is
  **4.6:1** (AA, barely); the same terracotta on `--surface` is **4.2:1** —
  below AA. Accent text is a field-only device. Inside a cream card, accent
  text must go up a size to clear the large-text floor, or become `--ink`.
- **`--good` and `--info` are not text colors.** Green at 2.1:1 exists to fill
  a checkmark and tint a row. A green "Normal" label on cream is unreadable and
  is the single most common way this palette gets broken.
- **`--ink-3` sits exactly on the AA floor** (4.5:1). It is for legal lines,
  captions and form hints — never a paragraph anyone is expected to read.

Text on the accent is `--accent-ink` (`#FEF9EF`), not white. Pure white
*measures* slightly better (4.8:1) — this is a warmth decision, not a contrast
one. The field's beige is the light in this room, and white next to it reads as
a hole cut in the page.

## Type

Three families, and each has exactly one job:

- **Display — Financier Display at weight 300 only** (plus its italic). The
  entire editorial voice of the pack is a *light* serif at large sizes; adding
  a 400 or 500 weight to "make it read better at small sizes" destroys it. If
  it is too small for 300, it should not be the serif.
- **Body/UI — FT Base** at **300** (all running text, including 20px lede) and
  **600** (buttons, labels, stats, inline emphasis, card titles). There is no
  400 and no 500 in the interface. Substitute: any geometric-humanist sans with
  a genuine Light — Söhne, Neue Haas Grotesk Display, or `system-ui` as the
  documented fallback.
- **Furniture — Fragment Mono 400** at **10–11px, uppercase, `+0.07em` to
  `+0.1em`**. It appears in exactly one place: the motion controls. That
  scarcity is what makes it read as an instrument label rather than as code.

Scale (fluid `clamp()`, every one keyed to the same **23.5rem → 90rem**
viewport band, so the whole page resizes as one object):

| Token | 376px → 1440px | Used for |
|---|---|---|
| `--t-display` | 54 → 100px | the hero claim |
| `--t-h1` | 57 → 80px | hero headline, the price numeral |
| `--t-h2` | 48 → 64px | every section heading, every stat |
| `--t-h3` | 34 → 45px | category names inside a grid |
| `--t-quote` | 27 → 40px | pull quotes |
| `--t-xl` / `--t-lg` / `--t-md` | 18→24 / 18→20 / 16→18px | lede, list rows, body |
| `--t-sm` / `--t-xs` | 14 / 12px | captions, legal |

Line height is a two-value system: **`0.9` on the display serif**, **`1.0` on
h2/h3**, and **a flat `1.5` on every sans size without exception**. Tracking is
`normal` everywhere except the big sans stat (`-0.031em`) and the mono
furniture (`+0.07…0.1em`). A pack that never tunes tracking per-heading is
faster to build and impossible to drift.

## Texture & surface

- **Elevation is a hairline plus a cream step, not a shadow.** Cards are
  `--surface` inside a `1px solid --line`; the border is doing the work,
  because `#F5EEE1` on `#FEF9EF` is a 1.05:1 fill difference and invisible on
  its own.
- **Four shadows exist and each has one job**: `--shadow-panel` (the pricing /
  footer panel, `12px 32px 80px rgba(42,43,47,.10)` — offset to the right, which
  is what makes it read as daylight rather than as a drop shadow),
  `--shadow-lift` (the one card pulled out of a table), `--shadow-cta` (a button
  sitting on photography), and `--shadow-float` (`1.6px 1.6px 8px
  rgba(0,0,0,.16)`) — the circular glass media control over photography, and
  the only place it appears. **A fifth shadow means one of these lost its
  meaning.**
  *(Corrected 2026-08-10: this read "three shadows exist … a fourth shadow
  means one of these lost its meaning" while `tokens/atrium.css` has always
  defined four, so copying the token layer as the pack instructs broke the
  pack's own rule on arrival.)*
- **Radii: 12px for containers, `--radius-xl` (24→40px) for full-width panels,
  `999px` for everything you can click or type into** — buttons, chips, inputs,
  carousel dots, the media controls. There is no 4px or 8px button in this
  system.
- **Photography is the only imagery**, and it is always contained: behind glass
  in the hero, or in a `--radius-md` well with a bottom-up `--scrim-card`
  gradient when text sits over it. Diagrammatic motion is Lottie, played once.
  No illustration, no 3D render, no icon set doing decorative work.
- **Glass is a real material here**: `rgba(255,255,255,0.07)` with
  `backdrop-filter: blur(15px)` for chips over photography, plus a directional
  `--glass-sheen` (a 202° highlight ramp) on the circular media buttons. Used
  only where something genuinely sits on top of an image.
- Spacing is a fluid ramp (`--s1…--s13`, 4px → 120px) with a
  **`--section-y` of 48→99px** top and bottom. Vertical rhythm is the only
  section separator this pack has, so it has to be large and consistent.

## Components

Every value below was read off `functionhealth.com`'s own stylesheets on
2026-08-20 — `/_astro/utilities.*.css` for the control system and
`/_astro/PageSections.*.css` for the sections — and mapped onto this pack's
tokens through the reference's own names: `--fill-04` is `--accent`, `--fill-03`
is `--ink`, `--fill-01` is `--bg`, `--stroke-02` is `--line`. Nothing here is
this pack's decision unless it says so.

**The control is a pill and there is only one.** Every button on the reference is
one class with four skins, so the states below are the whole system rather than a
per-component invention.

- **Shape and metrics, shared by all four skins** — `border-radius: 999px` (a
  true pill, not `--radius-lg`), 1px border in the skin's own colour,
  `font-weight: 600`, `line-height: 1.5`, `gap: 0.875rem` between label and icon,
  `width: fit-content`, `white-space: nowrap`. Medium: `min-height: 3rem` (48px),
  padding `0.75rem 1.5625rem` (12px / 25px), 16px. Small: `min-height: 2.5rem`
  (40px), padding `0 1.25rem`, 14px, `line-height: 1`.
- **Primary** — `--accent` fill, `--accent-ink` label at **4.59:1 on `--accent`**,
  border `--accent`. Hover **and** focus-visible: fill and border both go to
  `--ink`, the label stays `--accent-ink` at **13.47:1 on `--ink`**. The press
  does not dim the accent — it *replaces* it with the ink, which is why the label
  gains contrast rather than losing it.
- **Light** — `--bg` fill, `--accent` label at **4.59:1 on `--bg`**, border
  `--bg`. Hover: fill and border to `--accent`, label to `--accent-ink`. This is
  the primary inverted, for use on `--surface-ink`.
- **Outline accent** — `--bg` fill, `--accent` label, border `--accent`. Hover:
  fill and border to `--ink`, label to `--accent-ink`.
- **Outline neutral** — transparent fill, `--ink` label at **13.47:1 on `--bg`**,
  border `--accent`. The one control where the border and the label disagree
  about colour, and it is measured, not an oversight. Hover: as outline accent.
- **Disabled**, all skins — `opacity: .5` and `pointer-events: none`. Nothing
  else changes.
- **Focus ring** — `outline: 2px solid` the accent at **35% alpha**,
  `outline-offset: 2px`. The reference gives hover and focus-visible the same
  fill, so the ring is the only thing that separates a keyboard focus from a
  pointer hover.
- **Transition** — `background-color`, `color` and `border-color`, each `.2s
  ease`. No transform, no shadow change. A control that lifts is not this pack.
- **Two controls side by side** take `--s4` between them (16→18px fluid); on the
  narrow breakpoint the pair becomes a single full-width column.

**A note the pack owes an implementer.** `--accent` measures **4.17:1 on `--surface`**, below AA. An accent label is safe on `--bg` and on `--ink`, and
not on the cream card. The reference never places one there; this pack now says
so.

- **Inputs / forms** — `.form-hero__input` on the reference:
  `width: 100%`, `min-height: 3rem` (48px, the same control height as the
  button), padding `8px 16px`, a **1px `--line-strong` border**,
  `border-radius: 999px` — the pill again, so an input and a button read as one
  family — a white fill rather than `--bg`, `--ink` text at 16px, and a
  placeholder in `--ink-3`. A textarea keeps the border and drops the pill:
  `min-height: 6rem`, `--radius-md`, `resize: vertical`. **Label position and
  error placement are not on the reference's page**, so they are yours to decide
  and to say so — the pack states what it measured.
- **Navigation** — resting: the header sits on `--bg` with no border until
  scrolled. The **mobile shape** is the one the reference specifies in full: the
  panel's fill is `--accent` closed and **`--ink` open**, an `::after` strip
  under it carries the same fill so the panel and the strip never disagree
  mid-transition, and the open state is `transform: translateY(0)` from a
  translated-out rest. Nothing fades; the panel moves.
- **Loaders** — **none, and that is measured, not omitted.** A search of the
  reference's two stylesheets for a skeleton, a shimmer or a spinner returns
  **zero rules**. A page in this pack that needs a loading state should render
  the final layout with `--surface` blocks at rest rather than invent an idiom
  the pack has never had.
- **Empty states** — measured: `--ink-2` text at 16px, weight 300,
  `line-height: 1.5`, centred inside the container it replaces
  (`.testimonials-listing__empty`); the same treatment uncentred where the
  container is already narrow (`.faq-page_empty`). No illustration, no icon, no
  button — the sentence is the empty state.

## Hero

One viewport, and the media is the argument. `height: calc(100svh - <banner>)`
with a full-bleed `object-fit: cover` image or video over an `--ink` field, the
copy lower-left over it. Every number is the reference's.

- **The text column** is `max-width: 33.75rem` (540px) and stacks with `--s4`
  between its parts. It sits at the bottom of the stage, not centred: the media
  above it is the page.
- **Headline** — `--h1`, which is `clamp(3.5625rem, 2.1617vw + 3.0545rem, 5rem)`:
  **57px at 376px of viewport, 80px at 1440px**, and fluid between. Weight
  **300**, `line-height: .9`, colour `--bg` over the media, with a text-shadow
  the pack carries as `--hero-overlay-heading-shadow`.
- **Line ceiling: two, held by the 540px column** — and the ceiling is a word
  budget rather than a rule the CSS enforces. The reference's own headline is
  *"Check your health."*: **three words, 18 characters**, which at 80px in a
  540px measure lands on two lines. A fourth word crosses to three and the stat
  rail below it loses the room that makes it read as a rail rather than a list.
  Below 768px the reference adds `text-wrap: balance` and `letter-spacing:
  -.01em`, which is what keeps the two lines even rather than ragged.
- **The italic phrase** inside the headline is `font-style: italic` and
  `color: inherit` — on the media hero it stays cream. On a light-field hero the
  same class takes `--accent` instead. Signature motifs states the device; this
  states the two colours it takes and when.
- **The eyebrow pill** — `backdrop-filter: blur(15px)` over `#ffffff12` (7%
  white), `--radius-xl`, padding `--s2 --s4`, 14px/600 in `--bg`. It is the only
  place this pack blurs anything.
- **The stat rail** — three stats along the bottom, separated by 1px `--line`
  dividers **58px tall**, `--s7` apart. Number: `--h5` at 600; sublabel:
  16px at 300. Both in `--bg` over the media.
- **The CTA** carries `box-shadow: 0 2px 12px rgba(0,0,0,.1)` — the one shadow in
  the hero, and it exists to lift the control off photography rather than to
  suggest elevation.
- **Below 768px** the stage stops being the viewport: it becomes **666px** tall,
  the stat rail leaves the media entirely and reappears as a `--bg` bar beneath
  it, and the headline takes `line-height: .94`, `letter-spacing: -.01em` and
  `text-wrap: balance`.

## Responsive

The reference's breakpoints, counted from its own media queries — 184 of them
across the two stylesheets:

| Boundary | Queries | What it does |
|---|---|---|
| **768px** | 66 | the layout breakpoint: every two-column shell becomes one, the hero stops being the viewport, the stat rail moves out of the media |
| **1100px** | 74 | the reading breakpoint: grid gaps and section padding step down, the sticky banner reflows |
| 480px | 3 | the narrow tail — stat labels wrap rather than shrink |
| 1200 / 1280px | 7 | minor, and only inside two sections |

**Type does not step at these boundaries — it slides.** The whole scale is
`clamp()` between `--min-viewport: 23.5rem` (376px) and `--max-viewport: 90rem`
(1440px), so a heading has no breakpoint of its own. The layout steps; the type
does not. Mixing the two — a `clamp()` heading *and* a font-size media query — is
how this pack's rhythm breaks.

- **The page margin** is `clamp(1.25rem, 4.1353vw + .2782rem, 4rem)`: 20px at
  376px, 64px at 1440px and above. The content column is `100% - 2 × margin`,
  capped at `--main` = **1440px**.
- **Section padding** is `clamp(3rem, 4.812vw + 1.8692rem, 6.2rem)` top and
  bottom — 48px to 99px — and halves on the small breakpoint.
- **Two-column shells** are `minmax(0,1fr) minmax(0,1.1fr)` with `--s11` between
  them; below 768px they become `1fr` with `--s7`.
- **The one media query that is not width** is `prefers-reduced-motion`, and
  `hover` — the reference guards hover states behind `@media (hover: hover)`
  rather than letting a touch device latch them.

**Which components size against their container: exactly one, and it is a
technique rather than an omission.** The reference declares `container-type:
inline-size` in a single place — the interactive stage in its *tools* section —
and there it does something the rest of the page does not: **every dimension
inside the stage is written in `em`, and the stage's own `font-size` is driven by
the container width**. `width: 66.625em`, `min-height: 39.975em`, `font-size:
min(16px, 1.5009cqw)`; below the layout breakpoint the same stage becomes
`20.9375em × 21.48em` at `clamp(12px, 4.55cqw, 32px)`. One number scales the
whole composition, and nothing inside it needs a breakpoint.

Everything else sizes against the **viewport**, through the `clamp()` scale
above — 152 `vw`-based expressions against 2 container-relative ones. That is the
reference's answer and this pack's: reach for the container only when a
composition must scale as one object, and write its insides in `em` when you do.
A component that merely needs to be narrower belongs in the 768px column change,
not in a container query.

## Motion tokens

- Durations cluster tight: `--dur-quick 0.16s` · `--dur-base 0.2s` ·
  `--dur-soft 0.24s` · `--dur-slow 0.3s`, on `cubic-bezier(0.4, 0, 0.2, 1)`.
  This pack overrides the SHELEG default ease.
- **Transitions are property-scoped, never `all`.** The reference writes
  `background-color .2s, color .2s, border-color .2s` and
  `opacity .24s, transform .24s, box-shadow .24s`. On a page this long, `all`
  animates layout properties you did not mean to animate and costs frames on
  scroll.
- Two continuous motions exist and both are linear and infinite: the logo rail
  at **48s** (`translateX(0 → -50%)` over a duplicated track), and the
  condition marquee as **two rows travelling in opposite directions**.
- The hero runs a **7.2s slide cycle**: hold fluted `750ms` → reveal `2700ms` →
  run clear `2250ms` → cross to the next slide `1500ms`, under a continuous
  `1.08 → 1.10` push. It never rests on a static frame, which is why it needs
  the pause control below.
- **`prefers-reduced-motion` removes the canvas entirely** (`display: none` on
  the shader container) and the still image underneath becomes the hero. Do not
  slow the effect down; a slow refraction is still refraction. The marquees
  stop, and the media control hides because there is no longer motion to pause.

## Signature motifs

- **The fluted-glass hero.** A WebGL fragment shader refracting photography
  through vertical reeded-glass ribs, over a static `<img>` fallback, with the
  canvas `aria-hidden`. The numbers that make it look like *glass* rather than
  like a filter: **82.8 ribs** across the frame (64.8 on mobile), leaning
  **0.36rad ≈ 21°** (mobile `-0.11rad`), amplitude `0.0255`, drift `0.543`,
  feather `0.63`, chromatic aberration `0.04`, bevel `0.0095` at width `0.195`,
  highlight and shadow both `0.02` at focus `10`. Over it: an ink scrim
  (`#2A2B2F` at 70%, scaled `3.05 × 0.91` toward the text side) and a flat
  black `0.12` multiply. The ribs *clear* as the slide plays — the image is
  revealed rather than crossfaded, which is principle 3 arriving as an optical
  effect instead of a transform.
- **The italic aside in the accent.** Inside a serif headline, one phrase turns
  *italic and terracotta*: "Life is short? **We disagree.**" It is the pack's
  entire emphasis vocabulary — no bold, no highlight fill, no underline. One
  per heading, and never two in the same viewport.
- **One continuous field.** Sections are separated by `--section-y` rhythm and a
  change of layout, not by alternating backgrounds. The inverted surface appears
  once or twice on the whole page and always for a reason.
- **The pill triad.** Every control is `999px` at `12px 25px` with a `14px`
  icon gap, in exactly three variants: solid accent (primary), beige-on-photo
  (light), and accent-outline on the field (secondary). A fourth button style
  is drift.
- **The stat row with hairline dividers.** Two to four figures in sans 600 with
  a light sublabel beneath, separated by `1px` `--line` rules. Sans, not serif,
  not mono — the numbers are claims, and the serif is reserved for sentences.
- **Marquees with a visible off switch.** Every autonomous motion ships a mono
  uppercase `PAUSE MOTION` control beside it, with `aria-pressed` and a label
  that swaps to `Play motion`. Treat this as a component of the pack, not as an
  accessibility afterthought — see Bans.
- **The comparison table with one column lifted out.** A wide cream panel of
  `1px`-ruled rows, with the "us" column floated above it as a rounded card
  filled with `--accent-gradient` and `--shadow-lift`. It reads as a physical
  card laid on a printed table.
- **Sourced authority as layout.** Named experts with their institution as a
  second line, a partner-logo rail, and figures that carry their source. On a
  health page an unsourced number is a liability, and the source line is also
  what keeps the layout from looking like marketing.

## Signature element

**The fluted-glass hero.** If a reader remembers one thing from a page in this
pack, it is photography seen through vertical reeded glass — not a filter over an
image, but an image the ribs *clear* as the slide plays. Signature motifs carries
the shader's numbers; what makes it the signature rather than one motif among
several is that it is the first viewport, it is full-bleed, and every other
device on the page is quiet by comparison: one accent, one pill control, hairline
dividers, no second dark band.

Reproduce it or replace it deliberately. A page in this pack with a flat photo
hero is not a cheaper version of it — it is a different pack, because the ribs
are the only place this system spends motion on an image rather than on a
transition.

## Motion flavor (cinematic packs only)

If you ride the full SHELEG layer stack with this pack: the particle field is
**not** the right instrument — the ambient layer here is refractive, not
particulate. Keep the scroll clock and the reveal set, drive the hero shader's
`reveal` uniform from it if you want scroll-linkage, and let every section
below the hero use only short entrance reveals (≤500ms, `--motion-ease`). Tint
anything generative with `--accent` at low chroma against `--surface-ink`;
never introduce a second hue for "energy". The progress rail, if used, is a
`1px` `--line` rule with an `--accent` fill — the same hairline vocabulary as
the stat dividers.

## Micro-interactions

- Buttons transition `background-color, color, border-color` over
  `--dur-base`; the light-on-photo variant also carries `--shadow-cta`. Hover
  swaps fill and ink between the accent pair — nothing scales, nothing lifts.
- Text links use a hover-revealed underline (`--dur-quick`), with an inline
  `--accent` arrow glyph for "go somewhere" links. Focus-visible is a
  `--accent` ring at `2px` with `2px` offset on every interactive element,
  pill-shaped like its target.
- The FAQ accordion is a `--surface` row with a `--radius-sm` square icon well
  that transitions `background-color .18s, color .18s` — the row itself does
  not move, only the icon changes state and the panel heights animate.
- Horizontal rails (experts, stories) use `scroll-snap-type: x` with circular
  `40px` `--line` nav buttons that disable at the ends. Rails are always
  swipeable on touch; the buttons are the desktop affordance, not the mechanism.
- Video story cards autoplay muted on interaction with per-card play, mute, and
  a pill progress scrubber; media swaps are `opacity .22s`. Each card owns its
  own controls — there is no global player.
- The header is a `sticky` layer holding a translucent nav bar that is
  transparent over the hero and **gains its surface on scroll**. Transition the
  surface only — `background-color`, `border-color` and `backdrop-filter` at
  `--dur-slow` — and apply any padding step **without** a transition. Paint
  properties are free; padding is not, and this bar is sticky, so a transitioned
  `padding-top` relays out the whole document on every frame of the scroll that
  triggers it.

## Bans

- Status carried by hue alone. Success, warning, danger and info always
  ship with an icon or a word beside the fill — **status is never by
  colour alone**. Measured off a production reference, several of these
  pairs sit inside a dichromat's confusion line; re-stepping them would
  invent a colour this pack does not own, so the second signal carries
  the meaning instead.
- A dark section used as a rhythm device; alternating light/dark bands; any
  second inverted surface beyond the one the page has earned.
- A second accent hue. Green, blue and red are semantic fills with fixed
  meanings and no decorative use whatsoever.
- White (`#FFF`) as a surface or as text on the accent; true-neutral grays
  beside the warm ones.
- The serif at any weight but 300, the serif in ALL CAPS, or the serif below
  ~27px (`--t-h4`); mono anywhere except the motion controls.
- `transition: all`; scaling or lifting a button on hover; hover states on
  static cards.
- **Autoplaying motion without a visible pause control.** A marquee, a rail, or
  a shader that a user cannot stop is not shippable in this pack —
  `prefers-reduced-motion` alone does not discharge it, because the people who
  most need to stop the motion are frequently not the people who set that flag.
- Icon grids, illustration sets, mascots, stock 3D, gradients as decoration
  (the accent card gradient and the hero scrims are functional and are the only
  ones).
- An unsourced number, a claim without an attributed name, or a testimonial
  without a person attached to it.

## Gotchas

- **This pack prescribed a banned form for two releases, and no gate saw it.**
  Until 1.10.0 the header rule above read `transition: padding-top .2s` — a
  layout property, transitioned, on a `sticky` element, which is exactly what
  `MOTION_DOCTRINE.md` §5 forbids and why. It survived because `sloplint.py`
  only read *fenced* code blocks, and no style pack contains one: every pack
  prescribes its CSS in inline backticks, so all twelve were unlinted. The lint
  now reads inline spans too. If you copied this header before 1.10.0, the fix
  is to move the transition onto `background-color` / `border-color` and let the
  padding step land instantly — nobody perceives a 200ms padding ease, and
  everybody perceives the jank.

- **The hairline is decorative-strength, not affordance-strength.** `--line` on
  `--bg` is only **1.6:1**, well under WCAG 1.4.11's 3:1 for UI boundaries. It
  is fine around a card; it is *not* enough for a control whose only affordance
  is that border. Inputs take `--line-strong`, ghost buttons take `--line-ink`,
  outline buttons take `--accent`.
- **`--line-ink` is the same hex as `--surface-ink` (`#2A2B2F`), so a ghost control
  on the inverted banner has no border at all** — 1.00:1, not a faint one. On the
  banner and inside a media well a ghost control borders in `--on-ink` (13.47:1);
  `--line-ink` is for the light steps, `--bg` and `--surface`, and the token layer
  says so with `@role drawn-on:`. The pack's one inverted surface is also the one
  place its ghost button is most likely to be used, which is why this was worth a
  line rather than a shrug.
- **The accent fails AA on the cream surface** (4.2:1). This bites exactly where
  it is least visible in review: an accent label inside a card looks correct on
  a laptop and fails an audit. Either put accent text on the field, or size it
  as large text, or make it `--ink`.
- **A 300-weight serif at `line-height: 0.9` clips.** Descenders, diacritics and
  parenthesis tails will be cut by any ancestor with `overflow: hidden` or a
  tight fixed height — which is most hero and card containers. Give display
  blocks explicit vertical padding rather than raising the line height, or the
  headline stops being this pack.
- **Fluid `clamp()` everywhere means the browser zoom path is the real test.**
  Because the ramp is `vw`-based, a user at 200% zoom lands mid-band, not at the
  large end — check the page at 200% and at 320px CSS width, not just at the two
  design widths.
- **A WebGL hero needs four lifecycle branches, and shipping one is worse than
  shipping none**: `webglcontextlost`/`restored`, `visibilitychange` (pause when
  the tab is hidden — a shader burning a laptop battery in a background tab is
  the effect's worst review), reduced-motion removal, and the no-WebGL path
  where the `<img>` fallback simply stays. Ship all four in the same commit as
  the effect.
- The canvas must be `aria-hidden` with the still image carrying the real alt
  text, and slide changes announced (if at all) through a discreet live region —
  a slideshow that narrates itself every 7.2s is a screen-reader hazard.
- Substituting the fonts changes the pack more than substituting the colors. The
  light serif's proportions and the sans's Light weight are load-bearing; if
  neither is licensable, prefer a different pack over this one with fallbacks.
