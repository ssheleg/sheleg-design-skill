# @sheleg-design/almanac

The React reference kit for the SHELEG **Almanac** style pack — an oatmeal-paper grammar (light default, dark twin) with 2px seams and no 1px anywhere, a display set below a line-height of one, and uppercase mono tags notched through the edges of drawn boxes.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/almanac.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit. Switching packs swaps identity, not API.

## This pack's own

`StatusDot` carries the status triplet with a **required** label, because this pack
states that status is never by colour alone. `Skeleton` is static. `TaggedBox` is the
pack's signature element — see [`styles/almanac.md`](../../plugins/sheleg-design/skills/sheleg-design/styles/almanac.md).
