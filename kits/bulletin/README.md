# @sheleg-design/bulletin

The React reference kit for the SHELEG **Bulletin** style pack — warm cream
paper cut by flat pastel bands, where every card and control is a 1px ink
outline standing on a hard zero-blur ink offset it travels into when pressed.

It is generated from the pack, not authored beside it: `src/styles.css` opens
with `styles/tokens/bulletin.css` byte for byte, and the rules the design agent
must obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit, so switching packs swaps identity rather than API.

## This pack's own

`StatusDot` (the word is required, never the colour alone), `Rail` (the row of
outlined circles that says *many*), `Band` (one flat pastel per act, and the
`ink` tone that flips the whole block to the dark register), `Panel` (one per
page, the widest offset in the ramp) and `Skeleton`.

## The two rules that carry the kit

1. **An outline and an offset always travel together.** A hard shadow under an
   edgeless box reads as a rendering fault rather than as depth.
2. **A control presses into its offset; a surface grows out of it.** One move
   per kind of object. Give a card the button's press and the grid stops reading
   as a set of objects; give a button the card's growth and the click has no
   feedback.

**Motion does not cross into a design tool.** A kit is the static half of a
pack: the press is described here and in the pack, and it is implemented in
`styles.css`, but nothing in this package animates on its own.
