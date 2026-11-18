# Phosphor: conventions for a design agent

This kit is the built form of the Phosphor style pack. Read these before generating
anything with it; they are the pack's bans, stated where a design tool will see them.

## Colour

- **One phosphor green does every job.** `--accent` (#00ff66) fills the action, sets a
  mono headline, draws a connector, rings the focus and glows. It is 15.04:1 on the
  field, so it may be a word. A filled phosphor takes `--on-accent` (#001a09, 13.45:1);
  **a white label on the phosphor is banned**.
- **The field is a green-black, never neutral.** `--bg` #020604, steps `--panel` and
  `--panel-raised`. There is no light theme and no light section.
- **The balloon is the one light object.** `--balloon` with `--on-balloon` (18.34:1).
  Pin its text colour with a selector a surrounding panel cannot outrank.
- **`--keyline` is pure black and is never text**: an outline and a hard offset only.
- **Status is never by colour alone.** `--ok` is the phosphor itself, `--warn` the
  gold, `--danger` the red; the phosphor and the gold sit inside a dichromat's
  confusion range, so every status carries a word or an arrow. There is no info role.
- No second interface hue: no blue, no purple, no cyan.

## Light, surface and edge

- Elevation is light, not shadow: a raised thing has a brighter edge and a glow. The
  only downward shadows are the comic offsets, hard and unblurred, down and right.
- Glass (`Glass`) only over the rain, where it lets the rain stay visible behind a
  window that must be read. Glass over a still field is banned.
- Glow only on the lit things: a control, a live figure, a mono headline, a connector.
  Never on body copy, never on every card.
- No scanlines, no CRT curvature, no chromatic aberration. The terminal feel comes
  from the mono voice, the stepped timing and the prompt glyphs.

## Type

- Inter is the human voice (the hero headline at 800, body, balloons, buttons). The
  system mono is the machine voice (panel titles, captions, chips, tags, figures).
- No gradient text anywhere. The emphasis is `--accent` with `--glow-text`.
- Mono measures in `ch`, never px: the mono is the platform's own and varies.

## Motion

- Terminal timing is stepped: a typed headline on `steps(24)`, the cursor on
  `steps(2)`. Interface motion is one curve, `--ease-ui`, at 120 and 180ms.
- No overshoot easing and nothing entering from `scale(0)`.
- `Rain` is the signature element and the page's only ambient layer: mount it once.
- The reduced-motion contract has a JavaScript half: `Rain` never starts its loop under
  `prefers-reduced-motion: reduce`, and the stylesheet hides the canvas. A reveal
  observer must also read the query and mount at the final state.
