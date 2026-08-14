---
category: Data
---

A capsule at `--r-pill` with a **1.5px** border — not 1px. At diagram scale a hairline
disappears, and the reference draws both the node's edge and every connector in the tree
at 1.5px for that reason. Inside: a 28px icon tile at 6px radius, the role name at
`0.8rem` / weight 600, and the runtime beneath at `0.68rem` behind a 6px dot.

**`liveLabel` is a required reading, not a decoration.** A live node gets a `--good`
border and a 1.5px ring at 25% alpha *and* the word knocked out over its top edge. The ring
alone is a colour-only signal, and `--good` against `--warn` separates by 6.2 under
protanopia — below the dichromacy floor. The word is what makes the state legible; drop it
and the component is broken for a reader who cannot see the ring.

The node reveals on a `--stagger` of 140ms times its index — **the same constant the
swimlanes and the goal cascade use**, so three unrelated diagrams on one page share a
metronome and the scroll reads as one document.

Inside a narrow container the icon is dropped and the body centres, which is the
reference's own mobile treatment; it is a `@container` rule here, because a node in a
sidebar needs it at 1440px too.

```tsx
<OrgNode name="CMO" model="OpenClaw" live liveLabel="Active" />
<OrgNode name="Backend Eng" model="Claude" />
```
