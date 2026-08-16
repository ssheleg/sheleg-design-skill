# @sheleg-design/notation

The React reference kit for the SHELEG **Notation** style pack — a restrained near-white grammar (light default, dark twin) drawn entirely in hairlines, with a light serif over a monospace and an ink primary that leaves the accent free to mark what can be read.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/notation.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit. Switching packs swaps identity, not API.

## This pack's own

`StatusDot` carries the status triplet with a **required** label, because this pack
states that status is never by colour alone. `Skeleton` is static. `Eyebrow` is the
pack's signature element — see [`styles/notation.md`](../../plugins/sheleg-design/skills/sheleg-design/styles/notation.md).
