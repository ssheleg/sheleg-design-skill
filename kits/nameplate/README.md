# @sheleg-design/nameplate

The React reference kit for the SHELEG **Nameplate** style pack — a cool
near-white slab under a page that is square on 87% of its elements, where the one
round shape is reserved for a white 1px-bordered pill carrying somebody else's
publication name as type.

It is generated from the pack, not authored beside it: `src/styles.css` opens
with `styles/tokens/nameplate.css` byte for byte, and the rules the design agent
must obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and
types in every SHELEG kit, so switching packs swaps identity rather than API.

## This pack's own

`Plate` (the borrowed name, and the reason the pack exists), `PlateBand` (the
wrapping row of them — it wraps, it never scrolls), `Wave` (the 150px arc that
closes an act, overspilling to 150% width and gone under 768px), `Frame` (the one
object per screen allowed to wear the 70px-blur shadow) and `Eyebrow` (two
uppercase registers, tracked 0.06em and 0.175em, and they are not
interchangeable).

## The three rules that carry the kit

1. **The border is the plate.** A fill takes the meaning away, and a logo takes
   the readability with it. Thirty names set as type read as a list; thirty
   logotypes read as thirty typefaces.
2. **The lift is one gesture.** Travel and shadow-growth share `--dur-base`, so a
   plate rises *and* separates in one motion. Animate one without the other and
   the pack is gone.
3. **The round shape is rationed.** `Chip` is square at `--r-xs` and `Plate` is a
   pill, and reaching for the pill where the content is not a borrowed name spends
   the only shape on the page that means something.

**Motion does not cross into a design tool.** A kit is the static half of a pack:
the lift and the press are described here and in the pack, and implemented in
`styles.css`, but nothing in this package animates on its own.
