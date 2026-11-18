# @sheleg-design/phosphor

The React reference kit for the **Phosphor** style pack: a green-black terminal with
digital rain falling behind glass windows, one phosphor green that fills, writes and
glows, comic story panels, and portraits pushed through a green duotone.

The pack itself is the authority:
[`styles/phosphor.md`](../../plugins/sheleg-design/skills/sheleg-design/styles/phosphor.md).
This kit is one built reading of it, not a second source of truth. `src/styles.css`
opens with the pack's token layer copied byte for byte from
`styles/tokens/phosphor.css`; everything below the `/* ── components ── */` marker
consumes `var(--…)` and contains no colour literal.

## Build

```bash
npm install
npm run build        # tsc only: no bundler, no runtime dependency but React
```

## What is here

The six-name spine every SHELEG kit shares (`Button`, `Card`, `Chip`, `Stat`,
`Heading`, `Rule`) with identical props everywhere, so switching packs swaps identity
rather than API. Then this pack's own: `Rain` (the signature element), `Glass`,
`ChatLine`, `Balloon`, `Panel` with `Cells`, `Connector`, `Duotone`, `Prompt`,
`Waiting` (the loader) and `Empty`.

Each component carries a `.md` beside it with its category and the numbers that
license its colours.

## The three rules that are easiest to break

1. A white label on the phosphor, at any size.
2. A second ambient layer beside `Rain`, or glass with nothing moving behind it.
3. The reduced-motion contract has a JavaScript half; see
   `.design-sync/conventions.md`.
