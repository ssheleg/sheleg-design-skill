# Style pack — Briefing Room

Origin: a production investor-deck site (2026); every value below was read off
its live token layer, not eyeballed. The source is **anonymized at the owner's
request** — the values are extracted from a real system, the name simply isn't
public. Near-black field tinted with a single blue hue, one electric accent,
mono slide furniture, 1-bit dithered artwork. It reads like a technical
briefing: the room is dark, one thing is lit.

## Register

Choose this pack for **presentations rendered as a product**: investor and
board decks, technical briefings, launch memos, architecture walkthroughs,
conference talks published as a page. Used **standalone** — the SHELEG
cinematic motion layer does not apply, because a deck is *read at the
presenter's pace*, not scrolled. Single dark register; the accent carries all
emphasis.

The defining constraint is the canvas: a fixed **1280×720 (16:9) frame with
`overflow: hidden`**, not a flowing page. Everything below follows from that —
if content cannot fit the frame, the answer is a second slide, never a smaller
type ramp.

## Palette

Ready-made token layer: [`tokens/briefing-room.css`](./tokens/briefing-room.css)
— copy it verbatim instead of transcribing this table.

| Token | Value | Role |
|---|---|---|
| `--bg` | `oklch(0.045 0.008 254)` | the room (near-black, blue-tinted) |
| `--panel` / `-2` | `oklch(0.145 0.008 254)` / `oklch(0.178 0.008 254)` | card / raised card |
| `--line` / `-2` | `oklch(0.231 0.006 254)` / `oklch(0.269 0.006 254)` | hairline / stronger edge |
| `--ink` | `oklch(0.985 0.004 254)` | display and primary text |
| `--ink-2` / `-3` / `-dim` | `oklch(0.80 …)` / `oklch(0.62 …)` / `oklch(0.56 0.006 254)` | body / muted / furniture |
| `--accent` | `oklch(0.643 0.195 254)` | THE signal — one per slide |
| `--accent-soft` / `-line` | `accent / 0.18` / `accent / 0.45` | chip fill / chip border |
| `--accent-ink` | `= --bg` | text **on** the accent (never white) |
| `--good` (`-soft`) | `oklch(0.824 0.151 148)` (`/0.30`) | the one positive semantic |

Two things make this palette cohere, and both are easy to lose:

- **One hue, top to bottom.** Every neutral carries hue `254` at chroma
  0.004–0.008. They are not gray — they are the accent, starved of chroma. Swap
  in true neutrals and the deck immediately looks like two designs.
- **OKLCH, not hex.** Lightness is perceptual, so a ramp built by moving `L`
  alone stays even; tints are the same color with an alpha, never a new swatch.
  Ship a hex fallback layer only if you must support pre-2023 browsers.

Contrast: `--ink-dim` is for slide furniture (numbers, footers) at ≥10.5px mono
only — never body copy.

## Type

- Display + body: **Inter** — weight 600 for display, 500 for slide titles,
  400 body. Tight optical tracking: `-0.04em` at display, `-0.03em` at title,
  `-0.005em` at body.
- Furniture: **JetBrains Mono** at 10.5–13px, uppercase, tracked **`+0.14em`
  to `+0.18em`** — section headers, footers, source lines, chip labels. The
  wide tracking is doing the work here; mono at normal tracking reads as code,
  not as instrumentation.
- Scale (fixed canvas, so fixed px): `128 / 96 / 64 / 36 / 24 / 17 / 14 / 13 /
  10.5`. Line height `1.02` display, `1.05` head, `1.5` lede, `1.55` body.
- `text-wrap: balance` on every display and title — on a fixed canvas a
  one-word orphan is a visible defect, not a nuance.

## Texture & surface

- Elevation is **surface step + hairline**, never a glow. One card shadow
  exists (`0 28px 70px -28px rgba(0,0,0,0.85)`) and it is for lifted cards on
  the dark field; a second, tighter one for popovers.
- Radii `4 / 6 / 12 / 18 / 24 / 999`. Chips and pills take 999; cards take
  12–18; the frame itself is square.
- 4px spacing grid **with deliberate half-steps** (18, 22, 36) — dense
  information layouts need the in-between values, and inventing them per slide
  is how a deck loses its rhythm.
- **Artwork is 1-bit dithered/halftone, never a photo or a 3D render.** A
  single large dithered form per cover, in the accent, sitting under the text.
- Text over artwork is protected by a **two-part veil**: a directional
  `linear-gradient(95deg, …)` from 0.85 to near-transparent, plus a radial
  darkening in the corner where the text sits. Never lower the artwork's
  opacity to fix legibility — veil the art, keep the art crisp.
- One radial accent glow per slide at most: `radial-gradient(58% 46% at 50%
  26%, var(--accent-soft), transparent 70%)`.

## Motion tokens

- Durations `0.15s` / `0.2s`; ease `cubic-bezier(0.22, 1, 0.36, 1)`. That is
  the whole set — this pack overrides the SHELEG default ease, same as
  `editorial-luxury`.
- **Slides do not animate.** No transitions between slides, no build-in
  sequences, no scroll-linked anything: the presenter's voice is the timeline,
  and motion competes with it. Transitions exist only on interactive
  affordances (links, focus).
- `prefers-reduced-motion` is a no-op here by construction — which is the
  correct end state, not an excuse to skip the branch.

## Signature motifs

- **The slide frame as furniture:** mono uppercase header (`[04] MARKET · WHY
  NOW`), body, mono footer. Numbered sections make a 40-minute deck navigable
  by voice ("go back to four").
- **The title is a claim, not a label.** Every slide's headline is a full
  sentence asserting something ("Financial access is already global; the gap is
  guidance") — never a noun like "Market". The claim is the argument; the
  diagram below is its evidence.
- **One bespoke diagram per slide, never a bullet list.** The recurring set:
  opposing poles with the gap named between them; a staged flow with hairline
  connectors; a positioning map with two labeled axes and dot nodes; lanes or a
  funnel for a money path; a comparison table with one column marked as *us*;
  an allocation bar with a legend.
- **Highlight exactly one phrase per deck** — an accent-filled marker behind
  the single sentence fragment the whole story hangs on, with `--accent-ink`
  text on it. A second highlight halves the first.
- **Every number carries its source** in mono, directly beneath it. An
  unsourced figure on an investor slide is a liability, and the source line is
  also what makes the layout read as instrumentation.
- Chips (`999` radius, panel-2 fill, hairline border) for enumerations that
  would otherwise become bullets.

## Micro-interactions

- The deck is presented, so interaction is deliberately thin: hover only on
  genuine links, focus-visible ring in `--accent`, no hover state on static
  cards (a card that lifts under a cursor during a live presentation is noise).
- Keyboard navigation between slides is the one interaction worth building
  well; the slide number in the footer is the position indicator.

## Bans

- Status carried by hue alone. Success, warning, danger and info always
  ship with an icon or a word beside the fill — **status is never by
  colour alone**. Measured off a production reference, several of these
  pairs sit inside a dichromat's confusion line; re-stepping them would
  invent a colour this pack does not own, so the second signal carries
  the meaning instead.
- Bullet lists as the default slide layout; stock photography; illustrations
  with a mascot; icon grids where a diagram belongs.
- Gradients as decoration (the veil and the one accent glow are the exceptions,
  and they are functional).
- A second accent hue; true-neutral grays alongside the tinted ones; white text
  on the accent fill.
- Animated slide transitions, build-ins, scroll-jacking, particle backgrounds —
  wrong register entirely; that is what `instrument-console` is for.
- Numbers without sources; more than one highlighted phrase per deck; shrinking
  the type ramp to fit content into a frame.

## Gotchas

- **A fixed canvas fails silently.** `overflow: hidden` means overflowing
  content is simply invisible — nobody sees it in review, everybody sees the
  gap in the room. Check every slide at exactly 1280×720 before shipping, not
  at whatever the browser window happens to be.
- **The reference shipped no print or reduced-motion branch.** A deck gets
  exported to PDF and read on a phone; add a print stylesheet (one slide per
  page, veil intact) and a narrow-viewport branch that reflows the frame rather
  than scaling it into illegibility.
- OKLCH renders differently on wide-gamut displays than the sRGB hex you may be
  comparing against — verify on the screen the deck will actually be presented
  on, which is usually a projector with a narrower gamut than your laptop.
- Dithered artwork must be exported at 2× and left unscaled in CSS; resampling
  a 1-bit image destroys the dither pattern and turns it into mud.
