# Style pack — Surveyor

Origin: <https://visible.seranking.com> (2026), the front page of an AI-visibility
tracker. The site is WordPress behind autoptimize, and the authored layer is SE
Ranking's own `se-uikit` stylesheet — the `--se-btn-*` state ladder, the
`--main-colors-*` palette, the `--spacing-*` tokens and the single `--transition`
clock — plus the front-page CSS: ~68KB across four bundles and fifteen inline blocks.
The WordPress preset `:root` block is vendor noise, and none of it paints. Every value
below was **verified against the render** on 2026-08-29 through CDP at 1440×900, 768
and an emulated 390×844×2 — an area-weighted census of `background-color` and
`background-image` over every element on an 8,176px page. Ratios were computed by
importing this repository's own palette gate.

Warm peach paper, deep navy ink, one working teal whose text-bearing steps are the
reference's own hover ladder, a pink that answers but may not speak, flat white and
tinted cards with no shadow anywhere, fine contour lines as the single texture, and
the product appearing only as portraits — webp screenshots of the dashboard, never an
embed.

The identity in one sentence: **the page maps unseen terrain** — a survey of where a
brand stands in a landscape it cannot see directly, drawn in contour lines and counted
readings, with two voices: teal states the finding, pink marks what is still ahead.

Contract: widened — all thirteen headings.

Themes: light only — no second block of any kind ships here.
Rank: unordered — 3 status role(s) and no severity ramp; a rank scale is yours.

## Register

Choose Surveyor for **products that measure a landscape the buyer cannot see
directly**: visibility and monitoring platforms, SEO and AI-search trackers,
brand-listening and share-of-voice tools, competitive-benchmark dashboards sold to
marketing teams — anything whose pitch is *here is where you stand on a terrain you
cannot walk*. The proof this pack organizes a page around is **the survey**: portraits
of the instrument's readings, counted stat slabs in the working hue, delta chips with
their arrows, and a terrain texture that says *mapped* without saying a word.

Standalone: it does **not** ride the SHELEG cinematic motion layer, and its own
ceiling is lower than the library's default. The corpus holds exactly one
`@keyframes` (a pulse ring), zero scroll clocks and one 0.2s state transition —
`MOTION_INTENSITY` above **2** has nothing legal to buy here, and a page that animates
its terrain has stopped being a survey.

**Not for:** a product proven by handing over the live instrument — an embedded demo
in browser chrome is [`test-drive`](./test-drive.md). Not for developer tools sold on
a call or a document — `manpage`, `onionskin`. Not for the broader SEO-SaaS registers
this one sits beside: a white-and-one-accent SEO product sold on long time-to-value
and disconnected states is `babylove`, and one brand spanning marketing plus product
UI is `outrank` — this pack is narrower than either: its subject is the *survey*, and
without terrain to map it decays into generic warm-paper marketing. Not for
award-bait: the identity is stillness.

### The fork against [`test-drive`](./test-drive.md), which is the analytics-landing collision

Both sell an analytics product on warm paper with a dashboard as the first screen's
centerpiece, and a thumbnail cannot separate them. The separation is **whether the
engine is on**. `test-drive` hands over a running machine — an iframe or a
self-narrating loop inside drawn browser chrome, a founder's handwriting beside it,
demos on double-digit clocks. Surveyor hangs a portrait — the dashboard is a webp
still, the page is flat and nearly motionless, and the voice is a vendor team's, not
a founder's hand. If the visitor is meant to drive it on the page, go there; if the
page presents the readings and asks for a trial, stay here.

### The fork against [`showroom`](./showroom.md), which is the exhibit collision

Both arrange a page around still images of the product. The separation is **what
holds the exhibit up**. `showroom` lights one specimen like a museum piece — a white
gallery, a seven-layer neutral drop shadow, three type families, the application at
real size as the single subject. Surveyor embeds many small portraits flat into
tinted cards — no shadow exists on the page except the scrolled nav's — and the
subject is not the application's surface but the *terrain it measures*, carried by
contour lines, stat slabs and delta chips. One lit exhibit is `showroom`; a field
survey pinned flat to warm paper is this pack.

### The fork against [`chorus`](./chorus.md), which is the AI-visibility collision

Both sell an AI-search visibility product on warm paper and both put a dark dashboard
early, so the pitch cannot separate them. The separation is **what the page hands the
reader**. Surveyor hands a reading — portraits of the instrument, counted stat slabs,
contour lines, flat light surfaces with `box-shadow: none` and no dark band anywhere.
[`chorus`](./chorus.md) hands a conversation — a cut-corner bubble carrying somebody's
actual words, and full-bleed near-black slabs cut into the paper. If the deliverable
is *here is where you stand*, stay here; if it is *here is the thread, go reply*, go
there.

## Palette

Copy [`tokens/surveyor.css`](./tokens/surveyor.css) verbatim. Every colour there
carries its provenance — MEASURED, SELECTED or DERIVED — and its ratio.

| Role | Token | Value | Notes |
|---|---|---|---|
| Field | `--bg` | `#fff7f3` | MEASURED — the peach paper, 15.7M px² of the census |
| Card | `--surface` | `#ffffff` | MEASURED — every card, and none casts a shadow |
| Present tint | `--mint` | `#ebfbf7` | MEASURED — what the product does today |
| Future tint | `--pink-wash` | `#ffeff8` | MEASURED — the "coming soon" panels |
| Ink | `--ink` | `#101423` | 17.32:1 on `--bg` |
| Body | `--ink-body` | `#252e3d` | 12.92:1 on `--bg` |
| Brand teal | `--accent` | `#0d9488` | non-text and large-only — see below |
| Action | `--action` | `#0a7269` | SELECTED from the reference's own ladder — the only teal that writes |
| Answer pink | `--pink` | `#ff91da` | non-text — glyphs, series, tints |
| Speaking pink | `--pink-deep` | `#a83f88` | DERIVED — the pink that may carry a word |
| Info blue | `--blue` | `#123af8` | 6.65:1 on `--bg` — writes unmodified |

**The teal is a ladder, and the correction climbs it.** The reference fills its CTA
with `#0d9488` and sets a 16px/500 label on it — `#ffffff` on `#0d9488` is 3.74:1 —
and writes its links in the same hue — `#0d9488` on `#fff7f3` is 3.54:1 — both under
AA. The remedy is already in its own `se-uikit` tokens: the hover step becomes the
text-bearing fill here (`#ffffff` on `#0a7269` is 5.79:1, and `#0a7269` on `#fff7f3`
is 5.48:1), the active step becomes the hover, and the brand teal keeps every job
where 3.54:1 clears the large floor — the 40px stat figure, marks, ticks, the Q
glyph. No hue was invented; the roles moved one step down the reference's own ladder.

**The pink answers; it does not speak.** `#ff91da` is the second voice — the FAQ's A
glyph, the future-tense tints, the falling series — and `#ff91da` on `#fff7f3` is
1.92:1, so a word in it is unreadable anywhere (the reference's own glyph step
`#ff98dd` measures 1.84:1 on the same field). Where the pink must carry a
number (the falling delta), `--pink-deep` speaks: `#a83f88` on `#fff7f3` is 5.32:1.

**Three status roles, and no warn — a decision, not a gap.** `--good` is a declared
alias of the action ladder, because the reference paints its rising delta in the same
green family as its button; `--danger` is the deep pink, because the reference's
falling delta is pink, not red — keep that voice, it is half the identity; `--info`
is the measured blue. The authored palette ships no amber, so a warn derived here
would be an invented value; a surface needing four severities is quoting another
library. Status is never by colour alone: every delta ships its arrow and its number,
exactly as the reference's own metric cards do.

**The tints carry tense, not depth.** Mint marks what ships; pink marks what is
coming — measured on the "Powered by" panel against the four "Coming soon" cards.
Swapping them tells the reader a roadmap item is live.

## Type

One face at one loud weight — nothing on the page is bolder than 600.

| Role | Family | Size / line | Weight | Tracking |
|---|---|---|---|---|
| Display | TT Fors | 48px/57.6 → 44 → 36 | 600 | −0.02em, relaxing to −0.01em narrow |
| Section head | TT Fors | 36px/43.2 → 32 → 28 | 600 | −0.02em |
| Card head / FAQ q | TT Fors | 24px/28.8 | 600 | −0.01em |
| Stat slab | TT Fors | 40px/56 | 600 | 0 — and it is set in `--accent` |
| Lede | TT Fors | 20px/28 | 400 | 0 |
| Body | TT Fors | 16px | 400 | 0 |
| Label / tab | TT Fors | 14px | 500 | 0 |
| Caps stat label | TT Fors | 16px | 600 | 0, uppercase |

- **TT Fors is the whole voice** — a wide, low-contrast grotesque with tabular,
  lining numerals switched on globally (`font-variant-numeric: lining-nums
  tabular-nums` plus seven stylistic sets, measured on `body`). The numerals matter:
  this pack's pages are full of readings, and readings that jitter in width are
  readings nobody trusts. TT Fors is licensed; Onest is the open substitute, named
  second, as a pack decision.
- **600 is the ceiling.** Display, heads, stats and prices all sit at semibold; an
  800 display here is a different library's voice. Emphasis inside body copy is 500,
  not 700.
- **The tracking relaxes as the page narrows** — −0.96px on the 48px display,
  −0.36px on its 36px narrow step (−0.02em → −0.01em), measured. The opposite of
  tightening into small sizes; copy the direction, not just the values.
- **The stat slab writes in the working hue**: 40px/600 `#0d9488` on the field is
  3.54:1, over the 3:1 large floor — the one place the brand teal may carry
  characters.
- Line-height is 1.2 on every heading, 1.5 on body, and 1.4 on the two reading
  rhythms the table states — the 20px lede (28px measured) and the 40px slab figure
  (56px measured) — shipped as `--lh-reading`; `--measure-lede: 64ch` is a pack
  decision, stated because the reference centers its lede with no max-width.

## Texture & surface

**Elevation is a tint, and the page's one shadow is an event.** Every card and panel
computes `box-shadow: none` — white on peach, mint on peach, pink on peach are the
three depths this pack has. The single drop shadow (`--shadow-nav`) exists only when
the sticky navigation detaches from the field on scroll and fills white. A card
borrowing it is a foreign object.

**The contour is the one texture.** Fine concentric terrain lines: white at 25% on
the teal closer panel, teal at 16% and pink at 22% drifting in the field's corners —
measured as the reference's PNG assets. The pack ships the three line inks as tokens
and the technique as its own: nested `repeating-radial-gradient` rings, 1px line on
10–14px gaps, two origins per surface at most, always bleeding off an edge. A contour
that reads as a mark has stopped being terrain; a third origin is a wallpaper.

**Radii: the ramp defines the token set.** `--r-control` 10px on everything the hand
touches (the reference's own `se-btn` radius), `--r-card` 24px, `--r-panel` 32px on
section panels and the teal closer, `--r-badge` 6px, `--r-pill` 99px. **Subtraction
adjusts a nested instance**: the corpus's 20px is a 24px card's child behind 4px of
breathing room — 24 − 4 = 20 — and its 12px imagery sits in 20px shells the same way,
20 − 8 = 12. Never a second free value on a nested box.

**Hairlines are cool greys on warm paper** — `#dce4f1` on `#ffffff` is 1.28:1,
correct for a rule and far under the mark floor; a rule divides rows, never tints,
and no state change rides on one.

## Components

Read off the reference's authored `se-uikit` classes; states are its own ladder.

- **Buttons.** One height (`--control-h` 48px: 12px × 24px padding on a 16px/500
  label), `--r-control`, `border: 1px solid transparent` so variants swap without
  shifting. *Primary*: `--action` fill, `--on-action` label at 5.79:1 on `#0a7269`,
  hover and press both take `--action-hover` — the reference's three-step ladder
  loses a step to the AA shift the Palette states, so the darker step is the only
  one left past the fill, and hover and active share it deliberately. *Outline*: transparent fill on the field with a 1px `--ink` border and
  `--ink` label — the measured "Book a demo"; hover fills `--surface`. *Ghost* (nav):
  transparent, `--ink`, hover tints with `--mint`. Disabled: the reference's own
  pair, shipped as tokens — `--disabled-ink` `#9a9795` on `--disabled-fill` `#ede8e5`. No lit
  shadows, no scale, no translate — a button here changes only its fill.
- **Cards / containers.** A card is `--surface` at `--r-card` with 24px padding and
  nothing else — no border, no shadow, no hover. A *panel* is the section-scale
  object: `--mint`, `--pink-wash` or `--cool` at `--r-panel` with `--space-14`
  padding, carrying cards or stat slabs inside it. The *closer* is the one dark
  panel: `--accent` fill at `--r-panel`, white heading at 36px (3.74:1 — legal at
  heading sizes only), `--contour-on-dark` rings, and an outline-white CTA; its copy
  never drops to body size, because white on `#0d9488` cannot carry 16px.
- **The portrait.** The product appears as a still image at `--r-card` (12px inside
  panels), flat on its card or bleeding into the fold — never in browser chrome,
  never behind a shadow, never animated. Chrome around a portrait is `test-drive`'s
  seam; a spotlight under it is `showroom`'s.
- **Inputs / forms.** The landing ships no visible form — the contact surface is a
  mint modal at 20px radius (measured) whose field styles live off-page. The pack
  decision, derived from the control geometry: a field is `--control-h` on
  `--surface` with a 1px `--line` border at `--r-control`, label above at 14px/500,
  placeholder in `--ink-faint` (which may hold a placeholder precisely because a
  placeholder is not content); invalid moves the border to `--danger` **and** writes
  the message in `--pink-deep`.
- **Navigation.** Sticky at `--nav-h` (64px, the reference's own token, every
  width), transparent over the field at rest; on detach it fills `--surface` and
  gains `--shadow-nav` — the page's one shadow, measured. Links are ghost buttons at
  14–16px/500; the trailing pair is Sign-in (outline) and the primary CTA.
- **Loaders.** The corpus ships one: the pulse ring — a marker whose halo grows
  100→130% and fades, on `--dur-pulse`. It marks *live*, not *loading*. The loading
  idiom is therefore a pack decision, and the flat page dictates it: a `--cool`
  block at the shape's own radius, no shimmer — the fastest thing on this page is
  0.2s, and a travelling highlight would be the liveliest object on it.
- **Empty states.** A `--surface` card at `--r-card` holding one 16px/500 line in
  `--ink`, one sentence in `--ink-body`, and one outline control. On a page whose
  subject is coverage, an empty state is a reading of zero — write it as a reading
  ("No mentions yet in this engine"), not as an apology.

## Hero

A marketing opening that ends in the survey, not in a promise.

- One centered copy column: the display at `--t-display` (48px/57.6, 600, −0.96px)
  on **exactly two lines — and what holds the ceiling is a word budget**: the
  measured headline is eight words, and the centered column wraps a third line only
  past ~10; past two lines the hero is broken. Under it, two lede lines at 20px/28
  in `--ink-body` naming the engines it surveys; then the control pair — one primary
  (`--action` fill) and one outline — side by side, 48px tall.
- Below, full-content-width (1312px): **the survey portrait** — the dashboard as a
  flat webp still at `--r-card`, metric slabs and delta chips visible in the
  reading, bleeding into the fold. No chrome, no shadow, no motion.
- The field behind the hero carries the terrain: `--contour-teal` rings from one
  corner, `--contour-pink` from the other, both bleeding off-edge, and never behind
  the copy column's text.
- What it must not carry: a second texture, a gradient, an animated number, browser
  chrome around the portrait, or a photograph — the terrain is the only scenery.

## Responsive

Measured at 1440, 768 and an emulated 390×844×2; the reference's ladder is
mobile-first at 768 / 1024 / 1280 / 1536 / 1920.

- **Type steps at the reference's own breakpoints**: display 36 → 44 (768) → 48
  (1024+); section head 28 → 32 → 36; the tracking relaxes to `--track-heading-sm`
  below 768. Line-height holds 1.2 at every step.
- **The spacing ladder is named, and it moves**: v1 48→80, v2 24→32, v3 16→24, v4
  holds 12 — the reference re-declares its own `--spacing-*` tokens upward, and the
  pack keeps that shape: section rhythm 56px at every width, panel padding stepping
  with `--space-14`.
- **The nav holds 64px at every width** — measured at 1440 and 390 — with the link
  row folding into a toggle below 768.
- **The hero pair goes full-column** at the narrow width (358px measured on a 390px
  viewport) and keeps 48px.
- **Container queries.** Sorted by kind; the reference itself ships none, so this
  table is mostly a statement about what belongs to the page:

  | Breakpoint | Kind | Answer |
  |---|---|---|
  | A card grid stepping 3 → 2 → 1 | CONTAINER | `container-type: inline-size` on the grid, `@container` on the tracks |
  | Stat slabs 2-up → 1-up inside a panel | CONTAINER | container on the panel's row |
  | Display 36 → 44 → 48 | PAGE | the headline answers to the viewport |
  | The nav's toggle swap at 768 | PAGE | the nav is the page's |
  | The spacing ladder's steps | PAGE | the rhythm is the page's |
  | The closer panel's own radius and contour origins | SELF | **no container answer exists** — the panel establishes the container, and neither value changes anyway |

- **No horizontal overflow**: `documentElement.scrollWidth` equals the viewport at
  1440, 768 and 390, measured with the census running.
- **Viewport:** `100dvh` for any full-height surface, never `100vh`.

## Motion tokens

| Token | Value | Spends on |
|---|---|---|
| `--ease` | `ease` | the one state clock — MEASURED as the reference's `--transition` |
| `--dur-fast` | 0.2s | every fill and colour step — MEASURED |
| `--dur-pulse` | 2.4s | the live marker's halo — the keyframe is measured, the clock is the pack's |

One clock and one breath. Hover is a fill stepping down the ladder; press is the
active step; nothing moves, lifts, scales or casts. The pulse ring is the only loop,
it marks *live*, and at most one per viewport. Zero scroll clocks — no
`animation-timeline`, no parallax, one sticky element.

**Reduced motion costs this pack almost nothing, which is why shipping it is
non-negotiable**: the token layer collapses both clocks, and the pulse holds at its
resting frame — the marker itself, fully legible. The reference ships zero
`prefers-reduced-motion` rules; the pack does not copy the omission.

## Signature motifs

- **The contour terrain** — fine concentric rings in `--contour-teal` /
  `--contour-pink` on the field, white-at-25% on the teal closer; at most two
  origins per surface, always bleeding off an edge.
- **The counted slab** — a 40px/600 figure in `--accent` over an uppercase 16px/600
  label: "100M+ AI ANSWERS MONTHLY". The survey's headline readings.
- **Two voices** — teal states, pink answers: the Q/A glyph pair, the rising and
  falling delta, the present-mint and future-pink tints.
- **The flat portrait** — product screenshots embedded shadowless at the card
  radius; the page never pretends the picture is a machine.
- **Tense as tint** — mint for what ships, pink for what is coming.

## Signature element

**The closer panel.** A full-width `--accent` slab at `--r-panel`, white contour
rings drifting through it, a white 36px heading ("Need a custom plan?"), one line of
support copy at heading scale, and a single white outline CTA. It is the page's only
dark object and its only saturated surface — the survey ends by inverting once, and
that once is why it lands. Build it as a component with its contour origins fixed;
a page with two closers, or a closer that drops to body-size copy (white on
`#0d9488` is 3.74:1), has spent the device twice and broken it both times.

## Micro-interactions

- **Primary hover:** fill steps `--action` → `--action-hover`, and press holds the
  same step — the shifted ladder has no fourth value and the pack does not invent
  one; the label never moves. 0.2s on `--ease`.
- **Outline hover:** fill goes `--surface`; the border stays `--ink`.
- **Focus-visible:** the fill step **and** a `--focus-w` (2px) outline in
  `--focus-color` at `--focus-offset` — the ring is the pack's correction, because
  the reference's own `:focus-visible` is a fill change alone, and a fill change on
  an already-filled control is a whisper. Both, always.
- **The pulse ring** grows 100→130% and fades over `--dur-pulse`, on the live
  marker only, at most one per viewport.
- **Card hover: nothing. Portrait hover: nothing.** The survey does not fidget.
- `@media (hover: hover)` gates the two hovers above.

## Bans

- **No shadow on anything but the detached nav.** `#ffffff` cards on `#fff7f3`
  paper are the elevation model; a `shadow-md` here is a foreign object.
- **No body-size words in `--accent`** — `#0d9488` on `#fff7f3` is 3.54:1; that is
  `--action`'s job at 5.48:1.
- **No white body copy on the brand teal** — `#ffffff` on `#0d9488` is 3.74:1; the
  closer speaks at heading sizes only.
- **The pink never speaks at `--pink`** — `#ff91da` on `#fff7f3` is 1.92:1; a pink
  word is `--pink-deep` at 5.32:1.
- **No warn role.** Three statuses ship; an amber invented here would come from the
  vendor's WordPress presets, which paint nothing.
- **No weight above 600.** The ceiling is the voice.
- **No third contour origin per surface, and no contour behind body text.**
- **No browser chrome around a portrait** — that seam belongs to `test-drive`.
- **No animated numbers, no scroll clock, no parallax, no `animation-timeline`** —
  zero occurrences, measured.
- **No dark theme.** Light only; the closer panel is the page's one inversion.
- **No `100vh`.**
- **No `ease-in`.**

## Gotchas

**The authored layer hides inside a WordPress site, and the vendor block is bait.**
The page serves a WP preset `:root` with a full palette (vivid cyans, ambers,
magentas) — none of it paints; the census put every painted colour in the
`se-uikit`/front-page layer. A pack extracted from the biggest `:root` block would
have shipped WordPress's colours. Read the render.

**Four corrections travel with this pack, each with its number at the declaration.**

1. *The CTA label misses AA.* The reference sets 16px/500 white on its brand teal —
   `#ffffff` on `#0d9488` is 3.74:1. The fix climbs its own ladder: `--action`
   `#0a7269` carries text-bearing fills at 5.79:1 under white, and the brand teal
   keeps large-only jobs.
2. *Teal words miss AA on the field.* The "Learn more" links measure `#0d9488` on
   `#fff7f3` at 3.54:1. A teal word here is `--action`, because `#0a7269` on
   `#fff7f3` is 5.48:1.
3. *The pink A glyph fails even the large floor.* The FAQ's 24px answer marker
   measures `#ff98dd` on `#fff7f3` at 1.84:1 against a 3:1 large-text floor. The
   glyph keeps the voice as a glyph beside readable text; a pink that must carry a
   word alone is `--pink-deep` at 5.32:1.
4. *Keyboard focus is a fill step alone.* All eleven `:focus-visible` rules in the
   corpus move a fill or a colour and draw nothing — a keyboard user watching a
   teal button darken slightly is the whole affordance. The pack adds the 2px
   `--focus-color` outline and keeps the fill step; both, always.

**Zero reduced-motion rules, and the cheap forgiveness is the trap.** The budget is
one 0.2s clock and one pulse, so the omission costs the reference little — but a
consumer who adds motion on top of this pack inherits the omission at full price.
The token layer's reduce block ships with the pack; keep it when you extend.

**The focus probe lies if you call `.focus()`.** The reference styles
`:focus-visible`, which programmatic focus does not trigger in Chrome — a script
that calls `element.focus()` and reads `getComputedStyle` concludes the page has no
focus styles at all. Probe with keyboard events or read the stylesheet; this pack's
own measurement made that mistake before reading the CSS.

**The tabular numerals are load-bearing, not a nicety.** `font-variant-numeric:
lining-nums tabular-nums` is set on `body` — every reading, delta and price aligns
because of it. A substitute face without tabular figures makes the metric slabs
jitter; Onest ships them, which is half of why it is the named fallback.

**The 20px and 12px radii are not tokens.** They are nested instances of the 24px
card (24 − 4) and the 20px shell (20 − 8). Copying them as free values breaks the
concentricity that makes the nesting read as machined.
