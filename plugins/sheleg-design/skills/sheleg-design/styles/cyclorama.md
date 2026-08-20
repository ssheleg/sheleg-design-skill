# Style pack — Cyclorama

Origin: <https://www.codos.ai/> (2026), the marketing site of an enterprise
AI-transformation company. Every value below was read off its live computed
styles on 2026-08-08, and every contrast figure was computed by importing this
repository's own palette gate rather than by a second implementation. A pale
field that **breathes through six pastel stops on a 32-second loop**, near-black
ink that never moves with it, one orange used only as a fill, a **monospaced
typewriter serif** over a monospaced sans, and a generative organ that holds a
formation for most of a section and then redeploys.

The identity in one sentence: **a cyclorama** — the seamless theatre backdrop
that changes colour behind a fixed subject. Not a gradient, not a theme switch:
one continuous loop, under type and rules that never shift with it.

Contract: widened — all thirteen headings.

## Register

Choose this pack for **a company selling transformation to an executive buyer**:
founder-led enterprise AI, AI-transformation and applied-AI services, technical
consultancies whose argument is *we install this and your business starts running
differently*. It suits a product with no screenshot worth showing — where the
thing being sold is a change of state, and the page has to make that change
visible without a product tour.

It **rides the SHELEG cinematic layer**, and it is the first pack whose reference
already implements it: GSAP ScrollTrigger with real pinning, two WebGL canvases,
and a formation that holds then redeploys rather than crossfading.

**Not for:** data-dense product UI — a field that recolours under you is a defect
on a screen held for an hour, and that is `workbench`; regulated, clinical or
public-sector pages, where a moving pastel field reads as unserious; decks, which
are `briefing-room` and never animate; and any brand whose identity depends on
one stable background colour, because this pack's background is not a colour, it
is a loop.

**The fork against [`pigeonhole`](./pigeonhole.md), which is the pastel collision.**
Both spend pastel as their signature. Here it is a **field** — full-bleed, cycling
on a 32-second loop behind a fixed subject — and its job is atmosphere. There it is
a **taxonomy**: one hue bound to one named category, appearing only inside a chip
the size of a word, and never moving. Remove this pack's wash and the page loses
its mood; remove that one's tints and the page loses its *information*.

### The forks, in the order people get them wrong

**Against `field-notes`** — the sharp one. Both are warm, light and
monospace-voiced, and both serve technical companies. `field-notes` is a **ruled
document** selling *auditability*: hairlines compose the page, crop marks sit at
the corners, provenance tags qualify each claim, and nothing moves. `cyclorama`
is a **stage** selling *transformation*: the field itself is the motion, the
subject is generative, and there is no hairline composition at all. Route by what
the product's argument rests on — *how do you know?* takes `field-notes`; *watch
this change* takes `cyclorama`.

**Against `instrument-console`.** Both are technical. `instrument-console` is a
dark cockpit whose one electric signal exists to make a **changing value**
readable. This pack is pale and its subject is a **changing organism** — there is
no dial, no telemetry, no live number to read.

**Against `orchard` and `atrium`.** All three are warm and light with a single
warm accent. Those two are **static** fields for consumer health and biotech, and
their buyer is a person spending their own money. This field cycles, and its
buyer is an executive spending a company's.

**Against `briefing-room`.** Both address the boardroom. `briefing-room` is a
fixed 16:9 canvas that never animates; here motion is the identity.

**Against [`prism`](./prism.md).** Both are pale light fields with mono in the
body, and both will be reached for by an AI-infrastructure brief. The difference
is whether the field moves. This pack's field **breathes** — six stops on a 32-
second loop, under a typewriter serif — because its subject is a change of state.
`prism`'s field **holds**: one static iridescent wash with a hard bottom edge and
a heavy grotesque display, because its subject is software that is ready now.
Route by whether the page argues that something *will change* or that something
*is ready*.

## Palette

Ready-made token layer: [`tokens/cyclorama.css`](./tokens/cyclorama.css) — copy
it verbatim instead of transcribing this table.

**The field is not one colour.** `ctaCycle` runs 32 s, `ease-in-out`, infinite,
through six stops. Every ratio below is therefore stated against the **worst**
stop, `--field-2`, not against a representative one.

| Token | Value | Role | Worst-stop ratio, on `--ink` |
|---|---|---|---|
| `--field-1` | `#F9DEF3` | `0%`/`100%` — the rest stop, pale pink | ink 13.90:1 |
| `--field-2` | `#F3D9B8` | `16.67%` — apricot, **the contrast floor** | ink **12.79:1** |
| `--field-3` | `#F9E0E2` | `33.33%` — blush | ink 13.91:1 |
| `--field-4` | `#EAE3EE` | `50%` — lilac | ink 13.86:1 |
| `--field-5` | `#E6EEE3` | `66.67%` — mint, the lightest | ink 14.67:1 |
| `--field-6` | `#EEEAE3` | `83.33%` — warm cream | ink 14.52:1 |
| `--bg` | `var(--field-1)` | the static render; what a screenshot shows | — |
| `--surface` | `#FFFFFF` | the card — **the only opaque surface** | — |
| `--panel` / `--panel-tab` | `#C8BFCC` / `#B9AFBD` | the mist panel · its selected tab | ink 9.76:1 / 8.23:1 |
| `--ink` | `#1A1A1A` | body and display | **12.79:1** on `--field-2` |
| `--ink-soft` | `#3A3A3A` | eyebrows, captions, secondary copy | **8.36:1** on `--field-2` — a real body colour |
| `--on-ink` | `#EBE1F0` | the label on an ink fill — the **field** colour, not white | 13.73:1 |
| `--line` | `rgba(26,26,26,.22)` | THE hairline: window frames, outline CTA | a rule, not text |
| `--accent` | `#FF8C00` | **fill, dot, chart series — never text on the field** | 1.71:1 as text on `--field-2` ✗ |
| `--on-accent` | `#1A1A1A` | the label on an accent fill | **7.46:1** |
| `--good` / `--warning` | `#2C5A44` / `#9A6A00` | success · warning | — |
| `--danger` / `--info` | `#7A3A1C` / `#1B6EC2` | destructive · informational | — |
| `--signal` | `#00C22D` | the live indicator — **a fill**; ink on it is 7.26:1 | 1.76:1 as text on `--field-2` ✗ |

Three rules carry this palette.

- **The accent is a fill and only a fill.** As text on the field it measures
  **1.71–1.97:1** across the six stops, and the reference paints its section
  eyebrows exactly that way. This pack does not propagate it: eyebrows take
  `--ink-soft` at 8.36:1. Darkening the orange is *not* the fix — see Gotchas,
  where the three rejected candidates are listed with their numbers so the next
  reader does not spend an afternoon rediscovering that there is no text-safe
  orange in this palette.
- **Status is never by colour alone.** `--good` and `--danger` separate by 14.0
  at full colour but **7.2 under protanopia and 5.9 under deuteranopia**;
  `--warning` and `--danger` by 14.8. Every status renders as a mark **plus its
  word** — which is a measurement of the reference, not a licence: its status
  pill reads `● Listening`, and every comparison row pairs its dot with a text
  phrase. A dot alone is a bug in this pack.
- **`--signal` and `--accent` are both dots, and they collide.** 6.8 apart under
  protanopia, 6.7 under deuteranopia. The repository's palette gate does **not**
  check this pair, because `--signal` is not one of the names it treats as
  semantic — so the rule above is the only thing standing between a reader with
  protanopia and two identical dots. Never place an accent dot and a signal dot
  in the same legend without their words.

## Type

**Two faces, both monospaced, two percent apart** — that is the whole thesis.
Measured advance ratios at 100px with one probe: GT Alpina Typewriter **0.590**,
DM Mono **0.600**. Display and body share a rhythm, which is why the page reads
as one voice rather than two.

- **Display — GT Alpina Typewriter at 400.** A monospaced typewriter *serif*.
  Licensed (Grilli Type), so substitutes matter more here than in most packs.
- **Body, UI and data — DM Mono at 400.** Everything that is not the display
  headline: lede, body, buttons, chips, table cells, captions.
- **Urbanist is vestigial.** The reference sets it on `body` and then routes
  almost nothing to it. Do not build with it; if a third family appears in a
  cyclorama page, something has fallen back.

**Substitutes, measured rather than remembered:**

| Face | Advance ratio | Monospaced | Verdict |
|---|---|---|---|
| Courier Prime (SIL OFL) | 0.600 | yes | **use this** — typewriter serif, 2% off the original |
| Cutive Mono (SIL OFL) | 0.605 | yes | acceptable, same category |
| Zilla Slab | 0.576 | **no** | banned — proportional |
| Bitter | 0.641 | **no** | banned — proportional |
| Fraunces | proportional | **no** | the reference's own fallback, and wrong — see Gotchas |

Scale, resolved at 1440px:

| Token | Value | Line height |
|---|---|---|
| `--t-display` | `clamp(2.25rem, .5rem + 6.7vw, 8.125rem)` → **104.48px** | **1.0** |
| `--t-h1` / `--t-h2` | `clamp` 2→3.75rem / 1.6→2.5rem | 1.05 / 1.1 |
| `--t-h3` / `--t-h4` | 1.375→1.875rem / 1.125→1.3125rem | 1.15 / 1.3 |
| `--t-intro` | 1.125→1.875rem | 1.35 |
| `--t-body` / `--t-sm` | .9375→1.0625rem / .8125→.875rem | 1.6 / 1.55 |
| `--t-metric` | `clamp(2.75rem, .8rem + 6vw, 6.5rem)` | 0.95 |
| `--t-caption` | .75rem | 1.45 |

**Tracking is `-0.02em` on the display and nothing else** — one authored
decision, measured at exactly −2.0896px on a 104.48px headline. Eyebrows track
positive at `0.12em`, uppercase.

## Texture & surface

- **There are no shadows in this system.** Not one. `box-shadow: none` on every
  surface the reference paints. Elevation is a hairline drawn at the edge, and a
  drop shadow anywhere in a cyclorama page is a foreign part.
- **The app window has no fill.** `1px solid var(--line)`, `--radius-lg`, 12px
  padding, transparent — the field cycle shows *through* it. That is why it
  cannot have a background: give it one and the page's signature stops at its
  border.
- **Radius arithmetic, and the reference gets it right.** A 16px window with 12px
  of padding holds 4px chips, because `16 − 12 = 4`. The ramp is
  `4 / 8 / 16 / 24 / 9999`. Nesting the same radius twice is what makes two
  rectangles that happen to touch instead of one machined object.
- **Cards are the one opaque surface:** `#FFFFFF`, `--radius-lg`, 32px padding,
  no border, no shadow. Used where content must stop competing with the cycle;
  everywhere else the field simply shows.
- **Rhythm:** `--section-gap: 200px` is the number that builds the page.
  `--page-max: 90rem`, `--page-gutter: clamp(1.75rem, 5.6vw, 5.6rem)`, spacing
  ramp `.25 / .5 / .75 / 1 / 1.5 / 2 / 3 / 4 / 6rem`.

## Components

Measured off the reference unless a row says **pack decision** — where it says
that, the reference had no answer at capture time and this pack supplies one
rather than staying quiet about the gap.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Filled CTA** | `--ink` fill, `--on-ink` label, `--radius-md`, `0 24px` (hero) or `0 16px` (nav), DM Mono 20px/14px, tracking `.005em` | `scale(1.02)` **and** fill → `--ink-soft`, over `--dur-base` | `scale(.98)` with `transition-duration: 0s` — the press is instant on purpose | **pack decision:** `opacity: .45`, `cursor: not-allowed`, matching the reference's own `ds-btn` |
| **Outline CTA** | transparent, `1px var(--line)`, `--radius-md`, `0 24px` | border → `--ink`, fill → ink at 6% | as above | as above |
| **Accent CTA** | `--accent` fill, `--on-accent` label, `--radius-md` | fill → `--accent-hover` | as above | as above |
| **Card** | `--surface`, `--radius-lg`, 32px padding, no border, no shadow | `translateY(-2px)` over `--dur-base` | — | — |
| **Chip** | ink at 6%, `--radius-sm`, `4px 8px`, DM Mono 14px | fill → ink at 12% | — | — |
| **Panel tab** | `--panel-tab`, `--radius-sm`, `8px 12px`, DM Mono 17px | fill → `--panel-tab-deep` | the selected tab is the only one filled | — |
| **App window** | transparent, `1px var(--line)`, `--radius-lg`, 12px padding, traffic-light dots and a mono title | none — it is a frame, not a control | — | — |
| **Status pill** | `--surface` fill, a `--signal` dot **and its word** in DM Mono. **Pack decision:** `--radius-pill`, `4px 10px`, `--space-2` gap — the reference mounts this element by scroll progress and it was not in the DOM at capture time | none | — | — |
| **Input** | `--surface`, `1px var(--line-soft)`, `--radius-md`, `12px 16px`, **16px** DM Mono | border → `--ink-soft` | focus: border → `--accent` plus a 3px `--accent-ring` halo | `opacity: .55`, `cursor: not-allowed` |
| **Loader** | **pack decision:** a skeleton whose geometry matches the block it replaces — same radius, same hairline, `--fill-soft` fill, no shimmer. The reference ships no loader on its marketing surface | — | — | — |
| **Empty state** | **pack decision:** one `--ink` line naming what would be here, one `--ink-soft` line saying how to fill it, and nothing else. No illustration — the field is already doing the atmospheric work | — | — | — |

The input's **16px** is not a style choice: anything smaller triggers
zoom-on-focus on iOS. Keep it even where 14px would look better.

## Hero

- **Height** `--hero-min-h: 100dvh`. Never `100vh` — the field would reflow when
  mobile browser chrome collapses.
- **The headline is split around the subject.** Two display words flank the
  generative organ: one at the left gutter, one at the right. This is the pack's
  opening architecture and the reason the hero needs no card, no screenshot and
  no product shot.
- **The headline is laid out one character at a time**, each glyph its own
  element on a ~59.5px advance at 104.48px — which is what makes the
  per-character entrance possible, and what makes a proportional substitute face
  break the composition rather than merely change it.
- **Line ceiling: two lines per word-block, and two words total.** At
  `line-height: 1` a third line closes the block up and the organ loses the
  space it needs to read as the subject. Write to the cap.
- **The first viewport carries** the split headline, one lede at `--t-intro`, up
  to two buttons, and one proof strip of logos at the foot. It does **not**
  carry a card, a metric row, a screenshot or a second surface.
- **The nav is not sticky.** `position: relative`, 84px tall, no backdrop blur,
  no scrolled shape — it scrolls away with the page and does not come back. If
  you add a sticky nav you have left this pack.

## Responsive

The rules, not the adjective.

- **Type is fluid, and every size is a `clamp()`** with the slope in the token
  layer. This is the opposite of `field-notes`, which steps at breakpoints; do
  not mix the two approaches in one page.
- **Breakpoints** are `480 / 760 / 1080px` as declared, with the layout's own
  branches at `620 / 900 / 1040px`.
- **The landing page carries no media queries of its own.** Its collapse is
  driven in the component layer, not in CSS — measured: the `lp-*` classes have
  no `@media` rule anywhere in the sheet. When porting, that means the collapse
  is *yours* to write, and the rules below are what the reference's own layout
  does, not a stylesheet you can copy.
- **Collapse:** the split headline stacks into a single left-aligned block and
  the organ moves **above** it; the nav sheds its links and keeps only the
  wordmark; buttons stay side by side rather than going full width; eyebrows keep
  their tracking. The `--page-gutter` clamp carries the edges from 28px to 90px
  on its own.
- **Exactly one container query** exists in the reference
  (`container-type: inline-size`, one element). Components otherwise size against
  the viewport and their own `max-width`. If you add more, add them for the app
  window's panels — not for the page, whose column widths are the layout.
- **Full-height sections use `dvh`.** Bare `100vh` is banned.

## Motion tokens

- **One ease, `cubic-bezier(.22, 1, .36, 1)`**, on every state change and every
  reveal. `cubic-bezier(.34, 1.56, .64, 1)` exists for entrances only and must
  not leak onto controls. This overrides the SHELEG default — the pack wins.
- **Durations:** `--dur-fast .15s` for colour and opacity on a control,
  `--dur-base .25s` for transform, `--dur-slow .5s` for a section reveal.
- **`--dur-cycle: 32s`** — the field's full loop, `ease-in-out`, infinite, six
  stops. **`--dur-breathe: 6s`** — the organ's ambient scale, `0.99 → 1.02`, and
  it runs **on hover only**, never unattended.
- Transitions are **scoped to named properties**. `transition: all` is banned —
  and the reference declares it on its root element, which is the single worst
  line in an otherwise disciplined system.
- **`prefers-reduced-motion` zeroes every duration, including the cycle and
  including hover transforms.** The field settles on `--field-1` and simply is
  not running; nothing crossfades to get there. The reference ships this branch
  for every animated class — unusually good, and this pack requires the same.

## Signature motifs

- **The organ.** A particle cloud that holds a formation for roughly 80% of a
  section and then redeploys into the next — blob, then a diagonal streak, then a
  twelve-cluster grid. It is never a background: it is the subject, and the
  headline is composed around it.
- **The split headline.** Two display words flanking that subject, one per
  gutter. It is the pack's most transferable device and the first thing to keep.
- **The uppercase mono eyebrow** at `--ink-soft`, `0.12em` tracking — `WHO IT'S
  FOR`, `HOW IT WORKS`. Never in the accent; see Palette.
- **The transparent app window.** A hairline frame with traffic-light dots
  through which the field cycle shows. It is how this pack draws product UI
  without breaking the page's one continuous surface.
- **The mist panel.** The single place a real fill appears below the hero, for
  comparison tables — hairline rows, one dot plus one phrase per row.
- **The accent-dot cursor.** A 22px SVG with a 4px `--accent` dot and a white
  ring, hotspot at its centre, on filled and accent buttons only.

## Signature element

**The cycling field.** Not the organ — the organ recurs section by section, and
recurrence is what makes a motif. The field cycle happens **once, continuously,
everywhere**, and it is the only place this pack spends anything.

It carries the identity because it makes the product's claim structural rather
than stated. The company sells a change of state; the page *is* in a state of
change, permanently, under type that never moves. A static pastel page with a
generative blob is a common thing and says nothing. A page that recolours itself
under fixed ink on a 32-second loop is remembered, and it is remembered as the
thing the copy is about.

Everything else is quiet, and that is the price: one accent used only as a fill,
no shadows, no gradients, no second surface colour, ink that never shifts,
borders only ever a hairline. Spend the boldness here or the pack has no centre —
and do not add a second moving thing, because two competing loops read as neither.

## Motion flavor (cinematic packs only)

This is the first pack whose reference already implements the SHELEG stack, so
the mapping is direct rather than interpretive.

- **The clock.** One scroll store; the organ reads it per frame. The reference
  pins with GSAP ScrollTrigger and holds a formation across the pin — that is
  principle 3 (*hold, then redeploy*) in production, and it is why the page never
  reads as a screensaver.
- **The particle field:** warm — `--accent` through amber and pink, on the pale
  field, at low individual opacity so the mass reads as translucent tissue rather
  than confetti. Energy stays low; this organ drifts, it does not sparkle.
- **Formations** come from the page's own argument, one per section, and each
  must be nameable in a word: *blob*, *streak*, *grid*. If a formation needs a
  sentence to describe, it is decoration.
- **The Reveal set** runs at `--dur-slow` on the one ease, translate 10–12px plus
  opacity — nothing larger, because the field is already moving and a big reveal
  on top of it reads as two systems.
- **The cycle is layer 1** in the depth model (ambient), the organ is layer 3
  (the subject), type is layer 4. The cycle must never be put behind a scroller
  or given `pointer-events`.
- **Do not scrub the cycle to scroll.** It is a clock of its own on purpose: tying
  it to scroll position means a reader who stops scrolling freezes the page's one
  living element, which is precisely backwards for a page about change.

## Micro-interactions

- **Buttons** transition `transform` at `--dur-base` and fill at `--dur-fast`,
  scale to `1.02` on hover, and press to `0.98` with **zero** duration so the
  press is instant. Filled and accent variants carry the accent-dot cursor.
- **Cards** lift `2px` and nothing else — no shadow appears on hover, because
  there is no shadow in the system to deepen.
- **Links** shift to `--ink` from `--ink-soft`, and a link with an arrow moves the
  arrow `0.18em`, not the label.
- **Disclosure** (FAQ): the marker rotates 45° over `--dur-base`; the open summary
  and the hovered summary share one state. The reference tints that state with
  `--accent`, which fails on the field — use `--ink` and let the rotation carry
  the state.
- **Focus-visible:** a 2px `--accent` outline at 2px offset, following the
  target's own radius. Inputs additionally take a 3px `--accent-ring` halo. The
  accent is legible *as a ring* at any contrast; this is the one place it is
  allowed near text without being text.
- Nothing in this pack fades between two colours to signal state — state is
  carried by fill, border, transform and opacity.

## Bans

- **`--accent` as text on the field.** 1.71–1.97:1 across the six stops. Also
  banned: a darkened orange invented to get around it — see Gotchas for why there
  isn't one.
- **`--signal` as text**, and any status rendered as a mark without its word.
- A shadow. Anywhere. Elevation is a hairline; there is no `--shadow-*` token in
  this pack because there is nothing for it to describe.
- A fill on the app window; a second opaque surface beside `--surface` and
  `--panel`; a gradient of any kind.
- `transition: all`, which the reference itself declares and this pack refuses.
- A proportional display face — Zilla Slab, Bitter, Fraunces or any serif that is
  not monospaced. The hero is laid out per character; a proportional substitute
  does not restyle it, it breaks it.
- A sticky nav, a scrolled nav shape, or a backdrop blur.
- `100vh`; a scroll listener where the scroll store belongs.
- Scrubbing the field cycle to scroll position, or adding a second continuous
  loop beside it.
- A third font family. Urbanist is vestigial, not an invitation.
- Pure `#000` or pure `#FFF` as ink; white as a label on an ink fill, where the
  field colour belongs.

## Gotchas

The reference is disciplined — no shadows, correct radius arithmetic, a complete
reduced-motion contract — and it has one serious contrast failure plus three
system-level traps. All four are measured, and all four are corrected from inside
the palette rather than around it.

- **The section eyebrows fail WCAG, and they are everywhere.** `--accent`
  `#FF8C00` as text measures **1.71:1** on the apricot stop and no better than
  **1.97:1** on any of the six. The fix costs no design: `--ink-soft` at 8.36:1.
- **There is no text-safe orange in this palette, and this is the trap.** The
  obvious repair — darken the accent until it passes, the way `field-notes`
  derives `--brand-on-dark` — does not work here, because the warm-dark region is
  already occupied by two of this palette's own semantics. Measured, so nobody
  has to repeat it:

  | Candidate | As text on the worst stop | Nearest semantic | Separation |
  |---|---|---|---|
  | `#903A00` | 5.53:1 ✓ | `--danger` | **4.6** — under the hard floor of 10 |
  | `#A14700` | 4.52:1 ✓ | `--danger` | 9.0 normal, 7.4 protanopia |
  | `#C56200` | 3.01:1 (large only) | `--warning` | 8.5 normal, **1.4** protanopia |

  Each one trades a WCAG failure for a colour-blindness failure, and the second
  is worse because it is invisible to the person shipping it. The accent stays a
  fill.
- **The repository's palette gate cannot see the `--accent` / `--signal`
  collision** — 6.8 apart under protanopia — because `--signal` is not one of the
  names it treats as semantic. This is written down rather than renamed around: a
  token renamed to satisfy a checker is worse than an unchecked token that says
  so out loud.
- **The reference's own display fallback is wrong.** Its stack is
  `"GT Alpina Typewriter", "Fraunces", Georgia, serif` — and Fraunces is
  **proportional** (measured advances 22.5 to 89.4 at 100px against the original's
  flat 59.0). Anyone without the licensed face gets a hero that does not merely
  look different, it re-flows, because the headline is one element per character.
  Use Courier Prime.
- **`transition: all` on the root element.** The reference declares it, and it is
  the one line that contradicts the rest of a careful system. Do not port it.
- **The status pill was not in the DOM at capture time** — the app window mounts
  its contents by scroll progress. Its fill, its dot and its word are measured
  from the rendered page; its exact padding and radius are this pack's decision
  and are marked as such in Components. Treat them as a proposal, not a
  measurement.
- **Values are a snapshot** taken 2026-08-08 from a live production site. Treat
  them as extracted, not eternal.
