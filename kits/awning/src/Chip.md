---
category: Data
---

A chip is a **pill**, like the button — this system has two shapes and a chip
takes the round one.

`accent` is the **ink** fill, not a hue: this pack has no colour to tint a chip
with, so a selected or emphasised chip inverts exactly as the primary button
does. That constraint is the register rather than a limitation — it is what
keeps every colour on the page belonging to the product screenshot.

Where a chip must carry a *state*, put the word in it and take the colour from
`--good` / `--warn` / `--danger` in your own rule. Those three are derived, and
the red and the green collapse toward each other under deuteranopia at a
measured 5.2 against a floor of 8.0 — so the word is the primary encoding and
the colour is the second. A status chip with no word is a bug here.

```tsx
<Chip>Draft</Chip>
<Chip tone="accent" selected>Monthly</Chip>
```
