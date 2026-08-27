# @sheleg-design/deskmate

The React reference kit for the **Deskmate** style pack — a warm beige working day lit
from one source above the top edge, where the product's own messages are the page's
illustrations.

The pack document is the source of truth for every value here:
`plugins/sheleg-design/skills/sheleg-design/styles/deskmate.md`. This kit is what those
values look like when they are built, and `src/styles.css` opens with the pack's token
layer copied byte for byte — never transcribed.

```bash
npm install && npm run build   # tsc only; there is no bundler in this kit
```

## What ships

**The spine**, identical in name, props and types across every SHELEG kit, so switching
packs swaps identity rather than API: `Button`, `Card`, `Chip`, `Stat`, `Heading`,
`Rule`.

**The signature**, which is this pack's own: `Transcript` (the framed quote, and the
element a page here is remembered by), `Message`, `QuotedCard`, `Eyebrow`, `Field`,
`NavSlab`, `Empty` and `Skeleton`.

## Three rules this kit exists to keep

1. **A control is a pill at 56px; a container is a slab at 32px.** Swap them and the
   pack inverts. Every control also declares `box-sizing: border-box` and a
   `min-height` of `--tap-min`, because an anchor and a button disagree about padding
   otherwise and the taller one silently wins.
2. **Elevation is a field step.** There are two shadow tokens and both are spent — one
   under the frame, one bloom. A third shadow is a defect.
3. **Nothing inside the frame is the brand's.** The quoted client keeps `--quoted-*`:
   its own face, its own ink, its own two status colours. A status dot that reaches for
   them has adopted somebody else's design system.
