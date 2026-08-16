# @sheleg-design/router

The React reference kit for the SHELEG **Router** style pack — a product console
grammar (light default, dark twin) for dashboards, developer platforms and the
marketing pages that have to look like them.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/router.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit. Switching packs swaps identity, not API.

## This pack's own

- **`StatusDot`** — the triplet as one object: a dot in the mark colour, the state
  named in full in the word colour, on the wash. `label` is required by the type,
  because this pack states that status is never by colour alone.
- **`Skeleton`** — static blocks sized to the element they stand in for. No
  shimmer and no spinner; the reference's skeletons do not animate.

## What the kit will not do for you

The hero's 36px display is not a component here. It belongs to the landing
register, is fluid, and is capped at 17ch — the pack states the ceiling and the
container width that holds it, and a headline that reaches five lines is a broken
hero rather than a long one.
