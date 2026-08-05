---
category: Actions
---

Three variants with three measured geometries, and each one transitions exactly
the properties the pack names for it. `primary` is a pill — `--ink` fill,
`--on-ink` label, 8×16, 14px/500 — and `opacity` is the **only** property it
moves; it carries a `>_` prompt glyph when it wants to, the one place the pack
lets a terminal onto the marketing surface. `secondary` is the hairline block at
12×20 and 14px/600. `ghost` is the pack's hero button: on paper it is a bare
hairline, and inside `DawnHero` it picks up `--fill-on-deep` on a
`--line-on-deep-strong` border without any prop of its own.

Nothing scales and nothing lifts on hover — state is carried by fill, border and
opacity alone. Disabled is `opacity: .5` and `cursor: not-allowed`; that is a
**pack decision**, correcting a reference that ships a `cursor: default` button
at full opacity, which is indistinguishable from an enabled one. Focus-visible is
2px of the brand at 2px offset, and `--brand-on-dark` on the hero, never white.

`size` steps the variant's own padding rather than replacing it, so `md` is
always the number the pack measured.

```tsx
<Button onClick={start}>&gt;_ Index your repo</Button>
<Button variant="secondary" onClick={readDocs}>Read the docs</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Not now</Button>
```
