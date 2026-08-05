# Briefing Room — the contract this design system ships under

**Register.** Choose Briefing Room for **presentations rendered as a product**:
investor and board decks, technical briefings, launch memos, architecture
walkthroughs, conference talks published as a page. Single dark register. The
defining constraint is the canvas — a fixed **1280×720 (16:9) frame with
`overflow: hidden`**, not a flowing page — and everything follows from it: if
content will not fit the frame, the answer is a **second slide, never a smaller
type ramp**. A fixed canvas fails silently, so check every slide at exactly
1280×720. Elevation is a surface step plus a hairline, never a glow. Furniture
(section headers, footers, source lines, chip labels) is mono, uppercase and
tracked `+0.14em` to `+0.18em`; the wide tracking is what stops it reading as
code. A slide's headline is a **claim** — a full sentence asserting something —
never a noun like "Market", and every number carries its source in mono directly
beneath it.

**The accent rule.** There is exactly one accent (`--accent`) and it is **the**
signal: one per slide. Text on the accent fill is `--accent-ink`, which is the
near-black field colour — never white. `--accent-soft` is the chip and glow fill,
`--accent-line` the chip border, and at most one radial accent glow appears per
slide. `--good` is the single positive semantic and is state, not decoration.
Every neutral in this pack is the accent hue (254) starved of chroma, at
0.004–0.008 — they are not grays, and swapping in true neutrals makes the deck
read as two designs. The palette is OKLCH so the ramp stays perceptually even;
tints are the same colour at an alpha, never a new swatch. Build against
`var(--…)` only — a value with no token is a gap in the pack, not a literal.
Exactly **one** phrase in the whole deck is highlighted.

**Bans** (verbatim from the pack):

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

Motion is not part of this design system and must not be invented — and in this
pack that is stronger than in any other: **slides do not animate at all.** No
transitions between slides, no build-in sequences, no scroll-linked anything, no
hover state on a static card (a card that lifts under a cursor during a live
presentation is noise). The presenter's voice is the timeline, and motion
competes with it. There is no `transition` anywhere in `styles.css` and none may
be added; `prefers-reduced-motion` is a no-op here by construction, which is the
correct end state rather than a branch that was skipped. The only interactive
affordances left are a genuine link and a focus-visible ring in `--accent`.
