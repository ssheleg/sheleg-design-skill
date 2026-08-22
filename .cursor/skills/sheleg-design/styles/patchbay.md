# Patchbay — named ports, drawn cords, and signal you can watch move

Origin: <https://nautilustrader.io/>, measured 2026-08-22 with
`getComputedStyle` on the running page. The site declares **no CSS custom
properties at all** — it is Material UI with Emotion — so nothing here was
lifted from a stylesheet; every value was read off a painted element.

A near-black field carrying a faint 40px grid, one mint-cyan doing every
functional job, and boxes that are separated by a 1px line and never by a
shadow. The register is a **live schematic**: named ports in mono uppercase,
cords drawn between them as thin beziers, and small particles travelling those
cords on a 2–3.5s loop so the reader watches data move rather than reading that
it does. Above all of it, four slow light layers drift on an 8.5–11s clock that
never touches the fast one.

Contract: widened — all thirteen headings.

Themes: light only — no second block of any kind ships here.
Rank: unordered — 3 status role(s) and no severity ramp; a rank scale is yours.

> **"light only" is this library's word for "one block", not a claim about the
> register.** This pack is dark — `--bg` is `#1b1b1d` — and ships a single
> `:root`. `instrument-console` carries the same line for the same reason. If
> you need a light twin, you are authoring it, and the reference has none to
> measure.

## Register

Choose this pack for **products whose argument is an architecture**: engines,
message buses, data pipelines, brokers, schedulers, agent frameworks,
infrastructure with named parts and traffic between them. Its whole thesis is
that a reader who watches a packet cross a bus believes the system exists in a
way no paragraph achieves. It is equally the pack for the **open-source project
front door** — the reference is one — where the audience reads code and the
page must not look like it was made for someone who does not.

**Standalone** — it does not ride the SHELEG cinematic motion layer. Its motion
budget is spent on two perpetual loops rather than on scroll choreography.

**Not for:** consumer products, anything selling on warmth, editorial or
long-form reading, and any page whose subject is a person. The pack's ink is a
mono uppercase label; asked to carry a story about human beings it reads as a
monitoring panel. Also not for a product with **no internal structure worth drawing** —
the signature element is a diagram, and a diagram of a single box is an
admission.

**Motion ceiling:** no pack ceiling is pinned here, so `MOTION_INTENSITY` is cut
by §1's frequency table alone — the dial turns up what is left after that table,
and nothing in this pack narrows it further.

## Palette

Ready-made token layer: [`tokens/patchbay.css`](tokens/patchbay.css) — copy it
verbatim instead of transcribing this table.

| Token | Value | Role — every ratio in this column is on `--bg` |
|---|---|---|
| `--bg` | `#1B1B1D` | the field, and the only one |
| `--surface` | `#171718` | one step down |
| `--surface-deep` | `#121214` | the deepest band |
| `--ink` | `#EEEEEE` | every heading — 14.82:1 |
| `--ink-strong` | `#FFFFFF` | body copy inside a card — 17.20:1 |
| `--ink-soft` | `#848895` | the muted tier, and the only one — 4.86:1 |
| `--accent` | `#00CFBE` | THE accent, and it may carry a word — 8.74:1 |
| `--on-accent` | `#05100F` | text on a FILLED accent — 9.81:1 on `--accent` |
| `--accent-far` | `#2FADD7` | one gradient stop, nothing else — 6.62:1 |
| `--ok` / `--warn` / `--danger` | `#86F687` / `#EBA002` / `#E36364` | derived — 12.73:1 / 7.83:1 / 5.11:1 |

- **The accent is text-safe, and that is the unusual part.** Most brand hues in
  this library clear the 3:1 graphical floor and nothing else. `#00CFBE` is
  8.74:1 on the field, so it may set a link, a label or a heading word. What it
  may not do is take white on top: **white on the accent is 1.97:1**, which is
  why a filled accent control takes `--on-accent` and why the reference never
  fills one — its primary button is a 10% teal wash behind a `#EEEEEE` label.
- **One muted grey, not two — a correction.** The reference paints `#848895` in
  46 text nodes and `#686B75` in 13 more. The second is **3.23:1**, under the
  4.5 text floor and under 3 as well. It is not corrected to a new value because
  there is no room for one: `--ink-soft` is already 4.86:1, and any legible
  "fainter" step lands on top of it. Two greys, one tier.
- **A second correction, and the value comes from the reference's own ladder.**
  The diagram's group labels — `DATA CLIENTS`, `TRADER`, `CACHE` — are set at
  **9px mono uppercase in `rgba(255,255,255,0.30)`**, which composites to
  **2.70:1**. At that size it is the least legible text on the page. The fix is
  `0.50`, which is **5.19:1** and which the reference already uses for its own
  diagram legend eleven hundred pixels further down. Nothing is invented; the
  ladder already had the step.
- **Status is never by colour alone.** The three status tokens are a **pack
  decision** — the reference paints no success, warning or error state anywhere,
  so there was nothing to measure — and they are derived against a constraint
  most packs do not have: the accent is a mint-cyan, so the ordinary dark-UI
  green collides with it under dichromacy. `instrument-console`'s `#46D39A`
  separates from this accent by **3.51** under simulated CVD against a floor of
  8, and was rejected for it. Every candidate that clears the floor is **light**,
  which is why `--ok` sits above `--warn` and `--danger` in luminance instead of
  beside them. Worst pair at full colour is 16.28 and worst under protanopia,
  deuteranopia or tritanopia is 12.06 — but the rule stands anyway: the word
  beside the dot is what carries the state.

## Type

Four faces, four jobs, and the jobs do not overlap.

| Role | Face | Size / weight | Tracking |
|---|---|---|---|
| Display | a custom grotesque, shipped as `newTitleFont` | `2.8rem` → `3.7rem` at 900px, 500, `line-height: 1.1` | see the leak below |
| Body | Inter | 16px / 24px, weights 350 · 400 · 450 · 600 · 650 | −0.1px to −0.3px where designed |
| Controls | IBM Plex Sans | 12.8px, 400 / 450 | +0.3px |
| Data & labels | `SF Mono`, then the system stack | 9–12px, 500 / 600, uppercase | +0.5px to +1px |

- **The display face cannot be named, and the fingerprint says what to
  substitute.** It is a local `woff2` aliased `newTitleFont`; Next.js
  content-hashes the file, so the family's real name is not recoverable from the
  page. Measured against Inter at the same size and weight: **cap height 74.4 vs
  72.8**, **x-height 53.4 vs 54.6** — an x/cap ratio of **0.718** against Inter's
  **0.750** — **descender 19 vs 24**, and a test string **1.1% narrower**. That
  is a taller-capped, shorter-descended, slightly narrower grotesque: substitute
  from the PP Neue Montreal / Aeonik / Söhne class, not from Inter, and never
  from a humanist sans with a large x-height.
- **The scale is a STEP, not a clamp, and the pack keeps it.** `2.8rem` below
  900px and `3.7rem` above — 44.8px and 59.2px, one breakpoint, no interpolation
  anywhere. This is against current fashion and it is deliberate here: at
  `line-height: 1.1` a display line that resizes continuously re-wraps
  continuously, and this hero's argument is a **two-line** headline. See
  `## Hero`.
- **Two tracking systems coexist on the reference and you must pick one.** The
  designed styles track negative in px — 40px/650 at −0.3, 25px/600 at −0.2,
  14px/450 at −0.1. Underneath them MUI's theme default, `letter-spacing:
  0.00938em`, leaks into everything that did not override it, which is where the
  page's odd values come from: 14.5px body at **+0.136px**, the 59.2px hero at
  **+0.555px**. The hero is tracked the wrong way by inheritance. **This pack
  tracks negative above 24px and zero below**, and the leak is documented in
  `## Gotchas` because it is the single most copyable mistake on the page.
- **Measure in `ch`.** Body copy sits at `65ch`; the diagram's mono labels are
  set by their box and have no measure.

## Texture & surface

**There is no shadow on any card in the reference.** Separation is a 1px line
and nothing else, so the hairline ladder is the elevation model rather than a
detail of it: `--hairline` at 8% white does the work, `--hairline-strong` at 10%
marks emphasis, and `--grid-line` at 2% draws a **40px × 40px** grid behind
every diagram — two `linear-gradient`s at 1px, which is the cheapest grid CSS
can draw and the only texture in the pack.

**The card is a light, not a fill.** Measured:
`radial-gradient(circle at 50% 0, #0f2026, #16181a)` with a `1px` border in the
accent at 14%. The centre stop is a **teal-black** — the accent bled into the
ground — so the card reads as lit from its top edge. Nothing is raised; things
are illuminated. Copying this as a flat `background` and a border loses the
whole surface idea.

**Radius arithmetic.** The ramp is measured, not derived: **10px** on 50
elements (diagram nodes), **14px** on 37 (cards, and the dashed group frame),
**12px** on 19 (controls), plus a pill. Two rules, and they are different rules:

- **The ramp defines the set.** `--r-node: 10px`, `--r-control: 12px`,
  `--r-card: 14px`. A 2px ladder, and the tightness is the point — a node, a
  button and a card are three objects two pixels apart, so nothing reads as a
  different material.
- **Subtraction adjusts a nested instance.** A box inset 4px inside a card takes
  `calc(var(--r-card) - 4px)` = **14px − 4px = 10px**, which lands exactly on
  `--r-node`. That the ladder's own step *is* the common inset is why the set is
  2px apart and not 4 or 8.
- **And the case where subtraction gives nothing.** The feature card's padding is
  **24px**, and `14px − 24px` is negative. There is no concentric radius inside
  this card: an element flush against its padding is a **rectangle**, radius 0.
  Reaching for `--r-node` there because 10px "looks about right" is the mistake —
  it produces two curves that are not concentric and the card reads as
  stuck together.

## Components

- **Buttons.** Primary: `linear-gradient(135deg, --accent 10%, --accent-far …)`
  behind a **1.5px** `--accent-rim` border at `--r-control`, padding `9px 19px`,
  label IBM Plex Sans 12.8px/400 at `+0.3px` in `--ink`, plus two 15px teal
  glows as `box-shadow`. Hover: the glow strengthens over `--dur-control`
  `--ease-control`; no lift, no scale. Active: no separate state in the
  reference — this pack adds none, and says so rather than inventing one.
  Disabled: not painted anywhere on the reference; use `--ink-soft` on `--wash`
  with the border dropped to `--hairline`, which is 4.60:1 and legible, never an
  `opacity` multiplier. Secondary: `--wash` fill, `1px --hairline` border, same
  radius and padding, label at 70% white (**8.96:1**).
  **The primary button is a border and a wash, not a fill** — its 1.5px rim is
  3.10:1 and clears the boundary floor by 0.10.
- **Cards.** The lit radial above, `1px --accent-edge`, `--r-card`, `24px`
  padding, **no shadow at any state**, transition `--dur-control --ease-control`.
  A card is used when the thing has a title and a body; a row of facts takes a
  hairline instead.
- **Inputs / forms.** **None, and here is why:** the reference is a marketing
  page with a single external link in place of every form — no field, no
  checkbox, no select anywhere on it. Nothing was measured, so nothing is
  specified. Authoring one: take `--r-control`, a `1px --hairline` resting
  border, `--accent-rim` on focus at 1.5px to match the primary button, and put
  the error message under the field in `--danger` with the word, never the
  colour, carrying the state.
- **Navigation.** A `position: fixed` bar **114px** tall at `z-index: 100` with
  **no background and no backdrop blur** — the page shows straight through it —
  carrying a wordmark, four text items and the two buttons. It **hides on
  scroll-down and returns on scroll-up**. Mobile: not measured; collapse the four
  items and keep the primary button.
  The transparency is a real cost — see `## Gotchas`.
- **Loaders.** A `shimmer` keyframe exists (`background-position: 200% → -200%`)
  and a 2s `opacity: 1 → 0.4 → 1` pulse; neither is a spinner. The pack's loading
  idiom is **the pulse on the thing that is loading**, at the skeleton's real
  geometry, never a spinner over the layout.
- **Empty states.** Not painted on the reference. In this pack an empty diagram
  is the empty state: draw the ports with no cords between them, in
  `--hairline`, and put one sentence under it in `--ink-soft`.

## Hero

Centred, on the field, with the light layers behind it. In order: a full-width
version banner, the fixed nav, the two-line headline, a three-line lede in
`--ink-soft`, a row of mono version chips, and three stat cards.

- **Line ceiling: two.** Measured at 1728px the headline sets 59.2px over
  **1168px** and breaks into exactly two lines.
- **What holds it is the container, not a wrap hint.** The page's measure is
  `max-width: 1200px` and the headline sits inside it; there is no
  `text-wrap: balance` anywhere on the reference. Which means the ceiling holds
  only for a headline of roughly this length — **under about 60 characters** —
  and a longer one takes three lines with nothing to stop it. If your headline is
  longer, `text-wrap: balance` is the addition to make, and say that you made it.
- **What the hero must contain:** the sentence that says what the thing is, and
  at least one **machine-checkable fact** — a version, a package name, a date.
  The reference's `pypi.org v2.0.0rc3 · 1d ago` chip is the pack's tell: the page
  proves it is alive rather than claiming it.
- **What it must not contain:** a product screenshot, a person, or a number the
  page cannot compute. See `## Gotchas` for what happens when it tries.

## Responsive

- **Fluid type — there is none, and that is the measured answer.** The reference
  ships no `clamp()` anywhere. The display steps `2.8rem` → `3.7rem` at a single
  `min-width: 900px`; body sizes do not change at all. The breakpoint set is
  MUI's default — **0 / 600 / 900 / 1200 / 1536** — plus `(hover: none)`. A pack
  that adds `clamp()` here is authoring, not copying, and should say so.
- **Container queries.** Sorting every breakpoint the pack owns:

  | Kind | Subject | Answer |
  |---|---|---|
  | PAGE | the 900px display step, the nav's collapse, the 1200px measure | viewport `@media`, and it stays there |
  | CONTAINER | the diagram's column count, the feature grid's 3 → 2 → 1 | `container-type: inline-size` on the section root, `@container` on the grid |
  | SELF | the 40px grid's `background-size` on the diagram element itself | **no container answer exists** — a container cannot query itself; keep the viewport query |

- **Collapse.** The architecture diagram is the thing that breaks. It is a
  fixed-geometry drawing 943px wide and it **cannot reflow** — below roughly
  760px, stop scaling it and switch to the stacked list of ports with the cords
  dropped, or let it scroll horizontally inside its own frame with the frame's
  edges visible. Squeezing it produces cords that cross their own nodes.
- **Viewport.** `min-h-[100dvh]`, never `100vh`.

## Motion tokens

**Two clocks, and the gap between them is the design.**

| Band | Durations | Ease | What runs on it |
|---|---|---|---|
| Signal | 2s · 2.5s · 3s · 3.5s | `linear` | the particles on the cords |
| Ambient | 8.5s · 9.5s · 10s · 11s | `ease-in-out` | four drifting light layers |
| Control | 0.2s · 0.3s | `ease` | chips, buttons, cards |

Nothing animates on a duration between 3.5s and 8.5s. That gap is what lets a
reader classify the motion without thinking about it: the fast band is data, the
slow band is light, and a 5s loop would be neither.

**Reduced motion.** The reference ships exactly **one** rule —
`*, ::before, ::after { transition-duration: .01ms !important; animation-duration:
.01ms !important; animation-iteration-count: 1 !important }` — and it survives
only because of a property of the loops it kills: **every ambient keyframe's 0%
and 100% are identical**, so collapsing the duration lands the element exactly
where it started rather than at some arbitrary mid pose. Write your loops that way
and the blunt remedy is safe; write a loop that ends somewhere else and this
same rule teleports it there.

**What the blanket rule cannot reach, and this pack does not copy it.** The
reveal that fades each section in is **not** CSS — it is JavaScript writing
`opacity` and `transform` inline per scroll frame. A media query that zeroes
durations does not stop a script from writing `opacity: 0`, so under
`prefers-reduced-motion: reduce` the reference's sections are still hidden until
scrolled. This pack's rule: **anything that can hide content must be able to see
the media query.** Gate the reveal in JS on
`matchMedia('(prefers-reduced-motion: reduce)').matches` and render it revealed.

## Signature motifs

1. **The cord and its particle.** A thin cubic bezier at 8% white, 1.5px, with
   2px dots at 35% white travelling it — the pack's atom.
2. **The dashed group frame.** `1px dashed` at 8% white, `--r-card`, no fill,
   with a mono uppercase label sitting on it. Groups without boxing.
3. **The 40px grid at 2% white** behind every diagram — present, and never
   consciously seen.
4. **The mono uppercase port label** at 11px/600 with `+0.5px`, and a mono
   subtitle under it listing what the port carries — `pub/sub · req/res · data`.
5. **The tint that says "ours".** Every node is the same box; the ones belonging
   to the system are tinted `linear-gradient(145deg, --accent 12%, …)` with a
   35% accent border, and everything else is the same gradient in white at
   4%/2% with an 8% border. **Only the tint changes** — not the radius, not the
   type, not the size.
6. **The version chip.** A pill at `--accent-wash` behind a 25% accent border,
   mono 12px/500 in the accent, carrying a package name, a version and an age.

## Signature element

**The live architecture diagram.** Not the light, not the grid — the drawing of
the system with signal moving through it, and the pack is named for it.

Measured, so it can be rebuilt: **21 cords, 32 particles**, distributed
**12 cords carrying one, 7 carrying two, 2 carrying three**. Every multi-particle
cord divides its own period **evenly** — the seven pairs are offset by exactly
half their duration (1.25s on a 2.5s cord, all seven), and both triples by a
third (0.4 / 1.2333 / 2.0667 and 0.5 / 1.3333 / 2.1667 on 2.5s). Consecutive
cords start **0.1s** apart, so the board has no visible beginning. Each cord is
its own inline `<svg>` carrying: the visible path, a duplicate transparent path,
a static `r="3"` endpoint dot in `--accent`, an arrowhead `<marker>`, and one
`<circle r="2">` per particle driven by **`<animateMotion>`** along the same `d`.

Three consequences of that construction, all of them load-bearing:

- **`<animateMotion>` needs no JavaScript and no library.** The whole diagram is
  declarative SVG; nothing schedules it, nothing can drop a frame on the main
  thread, and it costs one element per particle.
- **It has no `keyPoints`, so the particle moves at a constant *parametric*
  rate, not a constant visual speed** — it appears to accelerate through the
  curved middle of a bezier. On these gentle curves that reads as life. On a
  tight curve it reads as a bug, so keep the control points shallow.
- **A particle cannot be paused by CSS.** `animation-duration` does not apply to
  SMIL, which means the blanket reduced-motion rule above **does not stop these
  dots**. If you ship this, stop them yourself: `svg.pauseAnimations()` behind
  the same media query.

Build it a second time and the vocabulary holds — the reference uses it twice,
for a message-bus topology and for an event-replay loop, and the second adds one
rule to the first: **a dashed cord is a different kind of edge** (there, the
replay path), where every live edge is solid.

## Motion flavor

Standalone — this pack does not ride the SHELEG cinematic layers, and its
particle field is a **diagram**, not a background. If you do put it under the
cinematic layer, tint particles `--accent` at 35% and keep their energy at the
bottom of the range: the pack's own signal band is already perpetual, and a
second moving field competes with the one carrying the meaning.

## Micro-interactions

- Buttons and cards transition on `--dur-control` `--ease-control`; chips on
  `--dur-chip`. Nothing scales, nothing lifts, nothing shadows.
- Hover on a card: the border moves from `--accent-edge` toward
  `--accent-edge-strong`. The fill does not change — the light stays where it is.
- `:focus-visible` takes the **primary button's own rim**: `1.5px --accent-rim`
  at `--r-control` with a 2px offset. One shape for focus across the pack, and it
  is a shape the reader has already seen.
- Keyboard: the diagram is decorative and takes no focus, but its **content is
  not** — every port label must exist as text in the DOM, which it does on the
  reference, so a screen reader gets the topology as a list.
- A `borderGlow` keyframe (`background-position: 0% → 200%`, 3s linear) sweeps a
  gradient along a border. Spend it on **one** element per page.

## Bans

- **No shadow.** Not on cards, not on buttons, not on the nav. Elevation is the
  hairline ladder; a shadow here reads as a different design system.
- **No white on the accent.** 1.97:1. A filled accent control takes
  `--on-accent`.
- **No second accent.** `--accent-far` is one gradient stop on one button. A
  second functional hue breaks the diagram, where colour means *belongs to the
  system*.
- **No `opacity` as a disabled state.** It composites against whatever is behind
  it and the ratio is then unknowable. Name the pair.
- **No text under 4.5:1**, and specifically not the reference's 30% white group
  labels at 9px.
- **No `clamp()` presented as measured.** The reference has none. Add it if you
  need it and mark it a pack decision.
- **No diagram whose motion cannot be stopped.** SMIL ignores the media query;
  `pauseAnimations()` is the answer.
- **No number the page cannot compute.** See `## Gotchas`.

## Gotchas

- **The stat counters read `0+` on a live page, in two separate sections.**
  `GITHUB STARS 0+`, `DOWNLOADS 0+`, `DISCORD MEMBERS 0+`, and further down
  `TESTING 0+ automated tests`. The component animates a count-up from zero and
  has no state for *the fetch did not return*, so the failure renders as a
  confident, precise, wrong number — worse than an empty slot, because a reader
  believes it. **Ship the skeleton until the number arrives, and ship nothing if
  it never does.** A hero that proves the project is alive with a fact is the
  pack's whole opening move; the same slot proves the opposite when it lies.
- **The reveal is scroll-progress-linked with a long runway, and a programmatic
  jump freezes it.** 48 wrappers carry a JS-written inline `opacity` and
  `translateY`. Scrolling normally, a section is at ~9% opacity when its top
  crosses the viewport bottom and reaches full about 500–600px later. Jumping
  there instead — an in-page anchor, a deep link, `scrollTo`, a print stylesheet,
  a screenshot service — leaves it stuck: measured at eight positions from 700px
  to 1700px, the target stayed `opacity: 0` at every one and the section never
  appeared. **Anything that hides content must have a path that shows it without
  a scroll event.**
- **MUI's `letter-spacing: 0.00938em` leaks into everything not overridden**,
  including the hero. That is the source of the page's `+0.555px` on a 59.2px
  headline and `+0.136px` on 14.5px body — positive tracking on a display line,
  which is the opposite of what the designed styles do two selectors away. If you
  build on MUI, set `letterSpacing` in the theme's typography variants or inherit
  a mistake.
- **Fourteen text nodes render in `Roboto`, not Inter.** MUI's default stack
  shows through where a variant was not overridden, and Roboto is not among the
  three fonts the page loads — so those nodes fall back again, to whatever the
  reader has. The page ships three families and paints four.
- **The isometric hero illustration is a single static `nautilus.svg`** — 1000 ×
  749, no live DOM, no animation. Only the architecture diagram is live. Do not
  spend a week rebuilding the isometric scene in CSS 3D: the reference did not,
  and the two idioms sit beside each other because one of them is an asset.
- **The fixed nav has no background and no blur.** Content scrolls under it and
  through it — measured overlapping the venue logo row. On a light section this
  would be unreadable; the pack survives because every band is near-black. If you
  add a light band, the nav needs a ground.
- **`--accent-rim` clears the 3:1 boundary floor by 0.10.** It is the primary
  button's only visible edge. Do not thin it, do not drop its alpha, and if you
  darken `--bg` re-compute it.
