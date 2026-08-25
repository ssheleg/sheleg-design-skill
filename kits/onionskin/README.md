# @sheleg-design/onionskin

The React reference kit for the SHELEG **Onionskin** style pack — a white technical
sheet at 96.5% zero radius where two bases do all the work and everything quiet is one
of them at an alpha.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/onionskin.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

## The spine

`Button`, `Card`, `Chip`, `Stat`, `Heading`, `Rule` — identical names, props and types
in every SHELEG kit, so switching packs swaps identity rather than API. On this pack
`Card` exists for parity only: reach for `Panel`.

## This pack's own

`Panel` (the signature — a ruled region of the sheet, with a provisional dashed variant
and a lit-edge subject variant), `Micro` (11px uppercase tracked open, the most repeated
object on the page), `Data` (the monospace, which owns every number) and `Grid` (the dot
field, which goes under a section and nowhere else).

## The three rules that carry the kit

1. **There is no grey.** Every quiet value is `--ink` or the navy at an alpha. The
   moment a third base appears, the system reads as an ordinary light UI.
2. **Nothing floats.** Elevation is a 1px rule and, once per section, an inset lit edge.
3. **The three faces do not cross.** Display, sentences, numbers — one family each.

**Motion does not cross into a design tool.** A kit is the static half of a pack, and
this one is nearly all static by measurement: 1,290 of the reference's 1,469 visible
elements do not transition at all.
