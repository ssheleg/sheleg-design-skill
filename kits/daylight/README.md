# @sheleg-design/daylight

The React reference kit for the SHELEG **Daylight** style pack — a bright client-portal grammar (light default, dark twin) whose whole depth is one very large soft shadow spent on a single object per screen.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/daylight.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit. Switching packs swaps identity, not API.

## This pack's own

`StatusDot` carries the status triplet with a **required** label, because this pack
states that status is never by colour alone. `Skeleton` is static. `LiftPanel` is the
pack's signature element — see [`styles/daylight.md`](../../plugins/sheleg-design/skills/sheleg-design/styles/daylight.md).
