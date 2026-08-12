# @sheleg-design/pigeonhole

The React reference kit for the SHELEG **Pigeonhole** style pack — a white wall
ruled by hairlines, a display face that never passes weight 400, one italic word
in the headline, and eleven pastel hues in which a hue *is* a category.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/pigeonhole.css` byte for byte, and the rules the design agent must
obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.

## The spine, and this pack's four

`Button`, `Card`, `Chip`, `Stat`, `Heading` and `Rule` are identical in name, props
and types across every SHELEG kit — switching packs swaps identity, not API.

The four that are this pack's own:

| Component | What it is |
|---|---|
| `CategoryChip` | the two-layer chip — deeper tint outside at 8px, paler inside at 7px — and the **signature element**. Its label word is required by its type |
| `LabelledRow` | one row of the product, labelled: the atom the pack is built from |
| `WashCard` | a feature card in its category's palest pair, its shadow tinted to its own hue |
| `FaqList` | a `<dl>` whose answers are always visible, so a machine can quote them |

## Why the label word is a required prop

Nine category inks were measured on the reference and eight of them fail 4.5:1
against the very tints it paints them on — `#49d1fa` at 1.53:1 is the worst. The
kit ships derived inks that clear the floor, and derivation has a cost: pushing
lightness down compresses the hues in OKLab, so the worst deuteranopic pair
(Marketing against Notification) ends up **1.24 ΔE** apart, well under the palette
gate's hard floor of 10.

Eleven hues cannot be simultaneously AA-compliant and mutually distinguishable to
a dichromatic reader. So the hue is the second channel and the word is the first —
which is why `children` on `CategoryChip` is not optional.

## What this kit deliberately does not contain

The page's set pieces are **raster art** on the reference — the chaos-to-order
diptych at 1152×703, the hero frame at 1150×631 — so they are art direction rather
than components. And nothing here rotates: the measured page has zero rotated
elements at three viewports.
