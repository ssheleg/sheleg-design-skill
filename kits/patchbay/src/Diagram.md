---
category: Signature
---

**The live architecture diagram** — the thing a page in this pack is remembered
by, and the reason the pack is called `patchbay`.

Measured off the reference so it can be rebuilt: **21 cords carrying 32
particles**, distributed 12 cords with one, 7 with two, 2 with three. Every
multi-particle cord divides its own period **evenly** — the seven pairs are
offset by exactly half their duration (1.25s on a 2.5s cord, all seven) and both
triples by a third (0.4 / 1.2333 / 2.0667 and 0.5 / 1.3333 / 2.1667). That is
what `(n * dur) / count` reproduces. Consecutive cords start **0.1s** apart, so
the board has no visible beginning.

Three things that will bite:

- **`<animateMotion>` has no `keyPoints`**, so a particle moves at a constant
  *parametric* rate rather than a constant visual speed — it appears to speed up
  through the curved middle of a bezier. On shallow curves that reads as life; on
  a tight curve it reads as a bug. Keep the control points shallow.
- **CSS cannot pause SMIL.** `animation-duration: .01ms` under
  `prefers-reduced-motion` does not reach these dots, which is exactly what the
  reference ships. The effect above calls `pauseAnimations()` and listens for the
  preference changing.
- **`kind="replay"` is a different EDGE, not a quieter one.** The reference uses
  dashed for its event-replay path while every live edge is solid. Dashing a
  cord to de-emphasise it makes the drawing say something untrue.

The diagram is `role="img"` with a label, and the port names must also exist as
real text in the DOM beside it so a screen reader gets the topology as a list.

```tsx
<Diagram width={943} height={713} title="Engine topology" cords={[
  { d: 'M 60 110 C 60 150, 87 130, 87 170', dur: 2.5, particles: 2 },
  { d: 'M 87 170 C 87 240, 300 260, 470 300', dur: 3.5 },
  { d: 'M 470 300 C 300 380, 120 360, 87 300', dur: 3, kind: 'replay' },
]} />
```
