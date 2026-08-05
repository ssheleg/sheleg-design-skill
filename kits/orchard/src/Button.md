---
category: Actions
---

`primary` **is** the candy pill — this pack has no separate `CandyPill`
component, and building one would give the design agent two buttons and no way
to pick. A flat `--cta` fill under its radial sheen, wearing both inset white
hairlines plus the ambient orange glow, at pill radius with `16px 24px 14px`
padding: the extra top pad is what makes the label sit optically centred.
Exactly one per view. It is the only orange object on the page, which is what
makes it unmissable without being loud. Its label is `--cta-ink`, never white —
white on candy orange is 2.8:1 and fails AA.

`secondary` is the sage pill: `--primary` under cacao ink at rest, deepening to
`--primary-deep` under `--on-primary` on hover. The label swaps because the
contrast does: oat on plain sage is 2.96:1, below even the large-text floor.
`ghost` is the bare one, washing `--primary-tint` on hover. Nothing scales and
nothing lifts — a soft-3D pill that also grows reads as a toy. Focus-visible is
a `2px --ink` ring at `2px` offset, pill-shaped like its target, on the orange
CTA as well.

```tsx
<Button onClick={startKit}>Start your kit</Button>
<Button variant="secondary" onClick={seeHow}>See how it works</Button>
<Button variant="ghost" size="sm" onClick={skip}>Not right now</Button>
```
