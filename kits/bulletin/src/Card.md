---
category: Surfaces
---

A card is `--surface` at `--r-lg` with a 1px `--line` outline and
`--shadow-3` — the outline and the offset always travel together, because a hard
shadow under an edgeless box reads as a rendering fault rather than as depth.

A card is for a *group*. A list of statements takes a `Rule`, and a single
figure takes a `Stat` on the bare paper. Hover on a card **grows** the offset to
`--shadow-3-wide` — the opposite of the button's press, and mixing the two moves
is the way this pack breaks.

```tsx
<Card title="Approvals" meta="4 waiting">
  <p>Every post routes through the client before it publishes.</p>
</Card>
```
