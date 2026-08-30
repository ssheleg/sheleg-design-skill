# @sheleg-design/chorus

The React reference kit for the **Chorus** style pack — warm off-white paper under a
construction grid that never switches off, where the set piece is somebody else's
question in a cut-corner bubble.

The pack itself is the authority:
[`styles/chorus.md`](../../plugins/sheleg-design/skills/sheleg-design/styles/chorus.md).
This kit is one built reading of it, not a second source of truth. `src/styles.css`
opens with the pack's token layer copied byte for byte from
`styles/tokens/chorus.css`; everything below the `/* ── components ── */` marker
consumes `var(--…)` and contains no colour literal.

## Build

```bash
npm install
npm run build        # tsc only — no bundler, no runtime dependency but React
```

## What is here

The six-name spine every SHELEG kit shares — `Button`, `Card`, `Chip`, `Stat`,
`Heading`, `Rule` — with identical props everywhere, so switching packs swaps identity
rather than API. Then this pack's own: `Bubble` (the signature element), `GridFrame`,
`Slab`, `Well`, `Delta`, `NavPill`, `Sweep`, `Field`, `Empty`, `Skeleton`, `Capsule`.

Each component carries a `.md` beside it with its category and the numbers that
license its colours.

## The three rules that are easiest to break

1. `--coral` may not be a word, at any size, and its button's label is ink.
2. `--r-bubble`'s cut corner belongs to one object and may not be restyled.
3. The reduced-motion contract has a JavaScript half — see
   `.design-sync/conventions.md`.
