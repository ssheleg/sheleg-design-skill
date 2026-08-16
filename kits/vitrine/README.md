# @sheleg-design/vitrine

The React reference kit for the SHELEG **Vitrine** style pack — a white hairline grammar (light default, dark twin) with a serif display over a sans body and an ink primary, built around one framed record per page.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/vitrine.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit. Switching packs swaps identity, not API.

## This pack's own

`StatusDot` carries the status triplet with a **required** label, because this pack
states that status is never by colour alone. `Skeleton` is static. `Frame` is the
pack's signature element — see [`styles/vitrine.md`](../../plugins/sheleg-design/skills/sheleg-design/styles/vitrine.md).
