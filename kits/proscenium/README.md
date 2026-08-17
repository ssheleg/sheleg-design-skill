# @sheleg-design/proscenium

The React reference kit for the SHELEG **Proscenium** style pack — a white field
carrying two cool acts and one deep indigo act at the middle (light default, dark
twin), an electric violet filling a control that stays nearly square at 4px against
cards at 16, and a framed product panel the fold cuts off.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/proscenium.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit. Switching packs swaps identity, not API.

## This pack's own

`Frame` is the signature element — the proscenium arch, and `cropped` is the prop
that carries it. `Stage` is the one dark act, and the pack allows exactly one per
page. `StatusDot` requires its label, because this pack states status is never by
colour alone. `Skeleton` is static. See
[`styles/proscenium.md`](../../plugins/sheleg-design/skills/sheleg-design/styles/proscenium.md).
