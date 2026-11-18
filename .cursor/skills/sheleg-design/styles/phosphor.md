# Phosphor: a lit terminal, a schematic drawn in one green, and rain behind the glass

Origin: <https://assessment.passioncode.ai/> (2026-11-18), a story-driven landing
page told as a terminal and a comic. Measured 2026-11-18 with `getComputedStyle`
through CDP at 1440x900, an emulated 768x1024x2 and an emulated 390x844x2, plus
`prefers-reduced-motion: reduce` at 1440. The page loads seven stylesheets; the
palette lives in one authored block (the `html.matrix` rule in `/story/matrix.css`)
that remaps the host design system's roles, and every value here was read off a
painted element and checked against that block. The census counted text nodes by
computed colour (1,618 of them at 1440) and painted backgrounds by computed fill.
The rain was read from the page's own canvas script, `/story/rain.js`, and the
duotone from the SVG filter `/story/cast.js` injects.

A green-black field that is never neutral, one phosphor green `#00ff66` that
fills, writes, rules and glows, and a mono voice for everything the machine says.
Over it: a canvas of falling glyph columns at half opacity, glass windows that let
the rain show through, story panels with a hard comic offset, schematic connectors
drawn in a single stroke, and portraits pushed through a green duotone so no
photograph ever brings its own colour onto the page.

Contract: widened, all thirteen headings.

Themes: light only, no second block of any kind ships here.
Rank: unordered, 3 status role(s) and no severity ramp; a rank scale is yours.

> **"light only" is this library's word for "one block", not a claim about the
> register.** This pack is dark, `--bg` is `#020604`, and it ships a single
> `:root`. `patchbay` and `instrument-console` carry the same line for the same
> reason. There is no light twin to measure: the reference's light look is a
> different register (paper and ink) and is not this pack.

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

Choose this pack for **a page that tells a story about machines doing the work**:
agent products, automation, AI operations, onboarding narratives, a launch that is
read as a sequence of scenes rather than a list of features. Its argument is *you
are inside the system now*: the reader scrolls through a terminal, watches lines
arrive, and the product's actors speak in balloons. The schematic half (connectors,
nodes, an orbit of steps, numbered panels) carries the explanation; the phosphor
half carries the mood.

**Standalone.** It does not ride the SHELEG particle layer: the rain is its
ambient layer, and two ambient layers on one page fight for the same depth.

**Motion ceiling:** no pack ceiling is pinned here, so `MOTION_INTENSITY` is cut
by `MOTION_DOCTRINE.md` §1's frequency table alone. The rain is ambient and continuous by design; the
frequency table already treats a perpetual layer as the expensive one.

**Not for:** a dashboard or any surface a person works in for hours (the glow and
the rain are a show, not a working light); a page that must read as calm, warm or
human first; regulated or financial pages where a novelty register costs trust;
and print or light-mode contexts, because the pack has no paper to fall back to.

### The fork against [`patchbay`](./patchbay.md), which is the near-black diagram collision

Both are near-black, both draw a schematic, both put a single green-cyan to work
and both run a loop that never stops. The test is **what the page asks the reader
to watch**. `patchbay` draws an architecture and moves data along its cords: the
reader watches packets cross a bus and believes the system exists. This pack
narrates: the reader watches a scene play, lines arrive in a terminal, a character
answers, a panel lands. If the page's set piece is a diagram of named ports, it is
`patchbay`. If it is a story with a cast, it is this pack. The colour is the
tell too: `patchbay`'s `#00CFBE` glows only as a faint wash around its primary
button and never lights a word, and this pack's phosphor lights words, figures
and lines.

### The fork against [`instrument-console`](./instrument-console.md)

Both are dark, mono-labelled and built around one luminous accent. A console
reports **a value that changes while you watch**, in electric blue, with no
ornament and no blur. This pack reports nothing live: it stages a sequence, and
its texture (rain, halftone, glass, comic offsets) would be noise on a cockpit.
Telemetry goes to the console; a story goes here.

## Palette

Ready-made token layer: [`tokens/phosphor.css`](./tokens/phosphor.css), copy it
verbatim instead of transcribing this table.

| Token | Value | Role, every ratio in this column is on `--bg` |
|---|---|---|
| `--bg` | `#020604` | the field, a green-black, and the only one |
| `--panel` / `--panel-raised` | `#06100a` / `#0a1a10` | instrument cell / a chat line, 1.05:1 and 1.13:1, steps rather than contrast |
| `--face` | `#1d3326` | the initials disc and an idle bar, 1.51:1 |
| `--ink` | `#e6ffee` | body and headings, 19.32:1 |
| `--ink-muted` | `#8fbf9f` | the lede and secondary lines, 9.82:1 |
| `--ink-caption` | `#bfffd6` | mono captions over a scene, 17.95:1 |
| `--ink-bright` | `#d6ffe2` | the rain's leading glyph, a gradient's light end, 18.69:1 |
| `--line` / `--line-strong` | `#14331f` / `#2e6a45` | quiet border / control border, 1.48:1 and 3.17:1, never text |
| `--accent` | `#00ff66` | THE phosphor: fill, word, rule, ring and glow, 15.04:1 |
| `--accent-hover` | `#5cff9a` | the hover step, 15.75:1 |
| `--accent-deep` | `#00a63e` | the dark stop of a radial, 6.33:1 |
| `--accent-soft` | `#063a1a` | a quiet phosphor fill under a word, 1.58:1, never the word |
| `--warn` / `--danger` | `#ffd21a` / `#ff4d6d` | the guarded marker / the falling line, 14.06:1 and 6.34:1 |

- **The phosphor is text-safe, and that is what makes the register possible.** At
  15.04:1 it can set a panel title, a mono headline, a figure and a link. What it
  may not carry is a white label: a filled phosphor takes `--on-accent`, and
  `#001a09` on `#00ff66` is 13.45:1.
- **The keyline is pure black, and it is not ink.** The reference names it
  `--ink: #000` because in comic vocabulary that is what it is. In this library
  `--ink` is the text colour and pure black as text is banned, so the pack ships
  it as `--keyline`: an outline and a hard offset shadow, nothing else. Against
  the field it is invisible, which is correct; it only reads where it borders a
  light object (the balloon) or offsets a lit one (the phosphor button).
- **The balloon is the one light object.** `--balloon` `#e9fff1` with
  `--on-balloon`, and `#06110b` on `#e9fff1` is 18.34:1. The speaker label
  `--balloon-who` measures 6.18:1 on that same fill (`#2a6a44` on `#e9fff1`).
- **Status is never by colour alone.** `--ok` is an alias of the phosphor (the
  reference remaps its host's positive role onto it), `--danger` is measured, and
  `--warn` is a measured gold the pack assigns to the warn role because it is the
  only third hue the page owns. In OKLab distance (×100) the phosphor and the gold
  separate by 5.5 under deuteranopia and 7.9 under protanopia, against the
  library's floor of 8 for a simulated dichromacy, so every status
  carries a word or an arrow beside its colour. There is no info role: a fourth
  would be a second phosphor or an invented hue.
- **The two capsule colours are not palette.** The reference's choice moment
  shows a red and a blue capsule (`#ff2d55`, `#2d7bff`); they are a narrative
  prop on one screen and the pack does not carry them as tokens.

## Type

Two families, and the split is the voice.

- **Inter** (the reference's own stack, `Inter, ui-sans-serif, -apple-system`)
  for the human voice: the hero headline, body, balloons, buttons.
- **The system mono** (`ui-monospace, "SF Mono", Menlo, Consolas, monospace`)
  for everything the machine says: panel titles, captions, chat headers, chips,
  tags, figures, the waiting line, the rain.

| Role | Face | Size / line-height | Weight | Tracking |
|---|---|---|---|---|
| Hero headline | Inter | `clamp(38px, 4.4vw, 68px)` / 1 | 800 | −0.03em |
| Lede | Inter | `clamp(17px, 1.5vw, 20px)` / 1.5 | 400 | 0 |
| Body | Inter | 16px / 1.5 | 400 | 0 |
| Chat line | Inter | 19px / 1.4, 16px in a window under 560px | 400 | 0 |
| Balloon line | Inter | 18px / 1.35, 16px in a panel under 560px | 400 | 0 |
| Panel title | mono | `clamp(20px, 2.2vw, 28px)` / 1.15 | 700 | 0 |
| Closing headline | mono | `clamp(28px, 4vw, 52px)` / 1.1 | 800 | 0 |
| Figure | mono | 40px / 1 | 800 | 0 |
| Eyebrow, chip, tag | mono | 11 to 12px, caps | 600 to 700 | 0.08 to 0.14em |

Measured at 1440: the headline computes `63.36px/63.36px`, weight 800, tracking
`-1.9008px`; at 768 and 390 it sits at its 38px floor. Below 860px every mono
caption steps down to 12px.

**The mono is not a substitute you pick; it is the platform's own.** The
reference names no web mono and loads none, so the terminal reads in SF Mono on a
Mac and Consolas on Windows. That is a decision about honesty (the machine speaks
in the machine's face), and it means a mono line's width varies by platform: set
mono measures in `ch`, never in px.

## Texture & surface

- **Darkness lit from inside.** Elevation is light, not shadow: a raised object is
  brighter at its edge (`--accent-rim` border) and glows (`--glow-window`), it
  does not cast down. The only downward shadows are the comic offsets, and they
  are hard and unblurred.
- **Three textures and no fourth.** The rain (a canvas behind everything, at
  `--rain-opacity`), the halftone screen (`--halftone`, 1.1px phosphor dots on a
  7px pitch, only behind a scene), and glass (`--glass` with an 8px backdrop
  blur, only on a window that floats over the rain). No grain, no noise image.
- **Glass is functional here.** It exists so the rain stays visible behind a
  window that must still be read; `--ink` on the composited glass stays far above
  AA (see Gotchas). A glass surface with nothing moving behind it is decoration
  and is banned.
- **The comic offset.** `--offset-keyline` (4px 4px, pure black) under a light or
  lit object, `--offset-panel` (8px 8px, the phosphor at 13%) under a story panel,
  `--offset-cell` (4px 4px at 25%) under an instrument cell. Always down and to
  the right, never blurred.
- **Radius ramp, one per object.** `--r-tag` 3px, `--r-glass` 4px, `--r-panel`
  6px, `--r-cell` 8px, `--r-window` 14px, `--r-balloon` 18px, `--r-pill` 999px.
  It is not a proportional ramp: a story panel is nearly square on purpose, a
  window is soft, every control is a pill. Two glass radii because there are two
  glass objects: `--r-glass` for a panel docked over a full-screen scene (an
  overlay that belongs to the screen's edge), `--r-window` for a chat window that
  floats free.
- **Nesting.** Neither nested object in this pack is flush, so neither takes the
  subtraction rule. A chat line sits 20px inside the window and keeps its own
  `4px 14px 14px 14px`, the sharp corner pointing at its speaker; an instrument
  cell sits in the flow of a panel, 28px in from its edge, and keeps `--r-cell`.
  The rule would apply only to a child drawn flush against a panel's inner edge:
  with `p` of padding its concentric radius is `--r-panel` minus `p`, and for the
  measured 6px panel that is zero once `p` reaches 6px, so a flush child in a
  padded panel is square-cornered. Do the arithmetic before you round it.

## Components

Measured off the reference unless a row says **pack decision**.

| Component | Resting | Hover | Active / selected | Disabled |
|---|---|---|---|---|
| **Primary button** | `--accent` fill, `--on-accent` label, 14px/700, `8px 14px`, `--r-pill`, a 2px `--keyline` ring plus `--offset-keyline` plus `--glow-action` | fill → `--accent-hover` over `--dur-hover` | **pack decision:** the offset collapses to 0 and the button sits into its own shadow over `--dur-hover`, inside the doctrine's press band | **pack decision:** `--panel-raised` fill, `--ink-muted` label, no offset, no glow |
| **Large button** | as above at 18px, `14px 22px`, 55px tall | as above | as above | as above |
| **Ghost button** | no fill, a 1px `--line-strong` border, `--ink` label, `--r-pill` | border and label → `--accent` | `aria-pressed`: border → `--accent`, label → `--accent`, `--glow` | border `--line`, label `--ink-muted` |
| **Chip** | mono 12px/600 caps at 0.08em, `--ink-muted`, a 1px `--accent-rim` border, `--r-pill`, `6px 12px` | none | none | none |
| **Story panel** (the card) | `--glass-panel`, a 2px `--accent-rim` border, `--r-panel`, `--offset-panel`, padding `26px 28px`, at most 760px | none | none (its entrance, from 60px below and turned 0.6°, is motion: see Motion tokens) | none |
| **Instrument cell** | `--panel`, a 1px `--accent` border, `--r-cell`, `8px 12px`, 14px/600 | none | none | none |
| **Chat window** | `--glass` with an 8px blur, a 1px `--accent-rim` border, `--r-window`, `--glow-window`, 640px wide | none | none | none |
| **Chat line** | `--panel-raised`, a 1px `--line` border, radius `4px 14px 14px 14px`, `10px 14px` | none | an agent's line: border → `--accent`, `0 0 18px --accent-trace` | none |
| **Balloon** | `--balloon` fill, `--on-balloon` text, a 2px `--keyline` border, `--r-balloon`, `--offset-keyline`, a tail drawn in `--keyline` | none | none | none |
| **Select** (the input) | `--bg` fill, a 1px `--line-strong` border, `--r-pill`, 12px/600, `4px 8px` | border → `--accent` | focus: the ring below | label `--ink-muted` |
| **Navigation bar** | fixed, 56px, `--glass-bar` with a 10px blur, a 2px `--accent-trace` bottom rule; a progress line under it in a phosphor gradient with `--glow` | none | none | none |
| **Loader** | **pack decision:** the reference ships none. A mono caps line in `--ink-muted` ending in a block cursor that blinks on two steps over `--dur-cursor`; static and fully visible under reduced motion. Never a spinner | | | |
| **Empty state** | **pack decision:** a dashed 1px `--accent-edge` cell holding one mono line in `--ink-muted` that starts with a `>` prompt and one sentence of `--ink`. No illustration | | | |

**Inputs and forms are thin in the reference, and the pack says so rather than
inventing a form system.** The page's only field is a language select. A form
built in this pack takes the select's border and radius for every field and the
focus ring below; a label sits above its field in mono caps.

## Hero

- **Two columns, the story on the right.** `grid-template-columns: minmax(0,1.2fr)
  minmax(0,.8fr)`, a 40px gap, padding `96px max(24px, 6vw) 72px`, full height at
  `100dvh` (the reference uses `100vh`; see Gotchas).
- **Left:** a mono chip, the headline in Inter 800, a lede in `--ink-muted` held
  at **52ch**, then the primary button and a ghost link, then a row of proof
  chips whose figure is mono `--accent` with `--glow`.
- **Right:** the first scene, not a screenshot: a chat window or a character's
  portrait in duotone, already on the glass layer over the rain.
- **Line ceiling: four lines** at the 68px cap, held by `max-width: 16ch` and
  `text-wrap: balance`. The reference's headline is two short sentences and lands
  in four lines at 1440; a fifth line pushes the first scene below the fold.
- **The headline's emphasis may glow** with `--glow-text`, and the reference also
  lays a faint `0 0 30px --accent-trace` across the whole headline, which is the
  one glow allowed on Inter. The emphasis may **not** be gradient text. See Bans.

## Responsive

- **One breakpoint, 860px, and it is a PAGE breakpoint.** Below it the hero goes
  to one column, the bar's primary button hides, panels take `18px 16px` padding
  and centre themselves, and the choice buttons stack full width. The reference
  also drops chat lines from 19 to 16px and balloons from 18 to 16px at 860px;
  the pack moves those two to container queries (below), because a window and a
  panel are components and do not know the screen.
- **Fluid type** is the two clamps in Type: `clamp(38px, 4.4vw, 68px)` reaches its
  cap at 1545px and its floor at 864px, so the hero headline is a fixed 38px for
  every phone and tablet, which is what the 768 and 390 readings show.
- **The rain re-pitches**, not scales: glyphs drop from 16 to 13px below a 700px
  window, so the column count stays high and the fall reads as rain, not as type.
- **Container queries.** The instrument grids inside a story panel (four
  department cells, three cubes, the two-up comparison) size against the panel,
  not the viewport: the panel takes `container-type: inline-size`, and the cell
  grids step from four to two columns and from two to one at their container's
  width. A panel dropped into a 400px column on a wide screen still stacks. The
  chat window is a container too: its lines step from 19 to 16px when the window
  is under 560px wide, whatever the screen, and a balloon steps from 18 to 16px
  when its panel is under 560px. The hero and the bar are PAGE
  breakpoints and stay viewport queries.
- **Collapse.** The alternating panel offset (left, right, left) and the 0.6°
  entry turn go away below 860px: panels centre and enter straight. Absolutely
  placed sound-effect lettering is hidden below 860px rather than squeezed.
- **Viewport.** Full-height sections are `100dvh`; the sticky opening stage is
  `100dvh` tall.

## Motion tokens

- **Two clocks.** The interface clock is the host's: `--ease-ui`
  `cubic-bezier(0.2, 0, 0, 1)`, `--dur-hover` 120ms, `--dur-state` 180ms. The story
  clock is longer: `--dur-line` 0.35s for a chat line, `--dur-enter` 0.7s for a
  panel on `--ease-settle` `cubic-bezier(0.2, 1, 0.3, 1)`, `--dur-draw` 1s for a
  connector drawing itself, `--stagger` 160ms between instruments in a panel.
- **Terminal timing is stepped.** A mono headline types on with `steps(24)` over
  `--dur-type`; a message arrives with `steps(6)`; the waiting cursor blinks on
  `steps(2)` over `--dur-cursor`. A stepped animation is a terminal; an eased one
  on the same line is a slideshow.
- **The rain runs on its own clock**: columns fall at 40 to 130 px a second, the
  head glyph changes every `--dur-glyph` 140ms, and scrolling multiplies the fall
  speed by up to seven. It is drawn by `requestAnimationFrame`, not by CSS.
- **Reduced motion.** Every duration collapses to 0.01ms and the stagger to 0.
  The rain is not started and its canvas is hidden; panels, lines and instruments
  render in place and fully visible; the cursor stops blinking (the kit pauses it,
  because a 0.01ms infinite blink strobes). The reference does all of this for
  the rain and the panels.

## Signature motifs

- **The rain**: falling glyph columns (katakana, digits, a few Latin capitals and
  operators) behind the page at half opacity, the head glyph bright, the tail
  fading.
- **The mono prompt**: `> ` before a typed headline, `[ CH 03 ]` brackets around a
  chapter number, uppercase tracked labels.
- **AR corner brackets**: two 18px L-shaped corners in `--accent` on a glass
  window, top-left and bottom-right only. (The reference also declares a 67%
  phosphor for them that nothing paints; the painted brackets are full `--accent`.)
- **The comic offset and keyline**: hard 4px or 8px offsets, black outlines on the
  balloon, a numbered tag on each panel.
- **The drawn connector**: a single 3px stroke with round caps, drawn on with a
  dash offset, a soft phosphor drop-shadow, and a mono label for what it carries.
- **Duotone portraits**: every photograph is desaturated and mapped through
  three stops (near-black, the phosphor, the pale ink), so a face is made of the
  page's own light.

## Signature element

**The rain behind the glass.** Not the glow (that is a property of every lit
thing) and not the panels (they recur). The rain is the one element that says
*this is a terminal you are inside*: it sits behind every window, it speeds up when
the reader scrolls, and the glass windows exist so that it stays visible while the
story is read. Spend the page's motion budget there and keep everything above it
still between beats. A second ambient layer (particles, a gradient mesh, a moving
grid) breaks it.

## Micro-interactions

- **Buttons** change fill on hover over `--dur-hover`; nothing lifts or scales. On a
  coarse pointer every button grows to the 44px tap floor (**pack decision**: the
  reference's bar button measures 37px).
  The press sits the button into its offset over `--dur-hover` (120ms, inside the
  doctrine's 100 to 160ms press band); the longer state step is never a press.
- **Focus-visible** is a 2px solid `--accent` outline at a 2px offset, on every
  focusable element. **Pack decision:** the reference declares no focus-visible
  outline at all (only a transform on its choice buttons), so the browser default
  ring was the only focus signal.
- **A toggle** (`aria-pressed`) lights: border and label to `--accent` and
  `--glow`; a small three-bar meter in the button animates only while it is on.
- **A panel enters once** as it crosses into view and stays; it does not leave
  and re-enter on scroll back.
- **Keyboard**: the choice buttons and the closing actions are real links; the
  story never traps focus inside its sticky stage.

## Bans

- **Gradient text.** The reference clips a phosphor-to-pale gradient into its hero
  emphasis and the closing headline; the pack refuses it (it fails the library's
  slop rule and drops the words' contrast where the gradient is darkest). The
  emphasis is `--accent` with `--glow-text`.
- **Overshoot easing.** The reference's slam-in and pop curves (`cubic-bezier(.2,
  1.6, .4, 1)` and kin) overshoot past 1; the pack settles with `--ease-settle`
  instead.
- **Scale from zero.** The reference stamps sound-effect lettering in from
  `scale(0)`; the pack enters it from 0.6 and opacity, or not at all.
- **A second hue for the interface.** No blue, no purple, no cyan accent; the gold
  and the red are status and nothing else.
- **White text on the phosphor**, and the phosphor as a large background field.
- **Pure black as a text colour or a field.** `--keyline` is an outline.
- **Glass with nothing behind it**, blur as decoration, and blur on anything that
  is not a floating window.
- **Glow on more than the lit things**: a control, a live figure, a mono headline,
  the hero's emphasis, a connector. Glow on body copy or on every card turns the page into a sign.
- **Scanlines, CRT curvature and chromatic aberration.** The reference draws none;
  its terminal feel comes from the mono voice, the stepped timing and the prompt
  glyphs. Adding the clichés turns a register into a costume.
- `100vh`; `transition: all`; a scroll listener that does layout.

## Gotchas

- **The balloon's text paints at 1.01:1 on the live reference.** Its stylesheet
  declares the balloon text `#06110b`, and a later rule (`.panel p`, same
  specificity, later in the file) repaints every paragraph in a panel `#e6ffee`.
  All 16 balloons read `#e6ffee` on `#e9fff1` at every width. The pack's
  `--on-balloon` is the declared value; a kit must give the balloon's text a
  selector that outranks the panel's, and the pack's reference kit does.
- **The reference has no focus-visible ring.** Zero focus-visible outline rules
  across its seven stylesheets; the pack's ring is a decision, not a measurement.
- **`100vh` on the hero and the sticky stage.** On a phone the browser chrome
  makes `100vh` taller than the visible screen, so the stage's bottom hides under
  the toolbar. Use `100dvh`.
- **Glass over rain, the arithmetic.** `--glass` is the field at 85% opacity, so
  whatever the rain paints behind it reaches the reader at 15% of its 50%: the
  brightest glyph (`--ink-bright` drawn at 0.9 on a 0.5 canvas) lifts the glass
  by under 7%, and `--ink` on that composite keeps a contrast ratio of 17.26
  (computed with the library's own palette gate; no token pair carries it, which
  is why it is not written as a pair). The margin is wide, so the glass's opacity is
  not a contrast question; it is a legibility one, because lowering it lets the
  rain's moving shapes compete with the words long before the ratio fails.
- **The duotone needs an SVG filter, and a custom property cannot feed it.** The
  three stops are `feFuncR/G/B` table values (0.01, 0, 0.84 / 0.02, 1, 1 / 0.02,
  0.4, 0.89), which are the field, `--accent` and `--ink-bright` written as
  fractions. Move a token and the filter does not follow; change both together.
- **The rain must not run when it cannot be seen**: under reduced motion, in a
  background tab, and when the canvas has scrolled away under a solid section. A
  canvas loop that keeps drawing costs battery for no reader.
- **Values are a snapshot** of a page that was being iterated daily when it was
  measured (its layout is on its fourth version). Treat the numbers as extracted
  on 2026-11-18, not eternal.
