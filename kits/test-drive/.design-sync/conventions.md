# Test-drive — conventions for a design agent

This kit is the built form of the Test-drive style pack. Read these before generating
anything with it; they are the pack's bans, stated where a design tool will see them.

## Colour

- **One coral, two tokens.** `--accent` (#e16540) lights controls, fills bars and
  blinks carets; it carries text only at display sizes. Every body-size coral word is
  `--action` (#c04a28). Swapping them ships the reference's own AA failure.
- **The declared teal is dead.** The reference's theme names an accent it never
  paints; nothing here may resurrect it.
- **Money is coral, traffic is blue** (`--chart-money`, `--chart-traffic`), and the
  blue never carries a word.
- **Status is never colour alone** — a state takes the word or the glyph beside it;
  `Delta` ships the arrow for exactly this reason.

## Geometry

- A control is 8px (`--r-control`), a card 16px (`--r-card`), the frame 20.8px
  (`--r-frame`), the badge a pill. The frame's window is concentric:
  `calc(var(--r-frame) - var(--frame-inset))`.
- The nav is 65px, static, unfrosted, in the field's own colour.

## Elevation

- A card is ringed (`--ring-card`); a control is lit (`--lit-action` /
  `--lit-quiet`); the frame gets the one big drop (`--shadow-frame`). There is no
  fourth shadow.

## The machine

- Terminal, CLI and agent surfaces take `--machine-*` and ignore the theme. Their
  tokens never reach a card, and the caret never leaves them.

## Motion

- 0.2s for anything a pointer caused; press scales to 0.95 over 0.15s; demos narrate
  themselves on double-digit clocks. Nothing is scroll-driven. Under reduced motion a
  demo shows its final frame, not its hidden first one.
