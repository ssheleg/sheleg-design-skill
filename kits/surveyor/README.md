# @sheleg-design/surveyor

The React reference kit for the **Surveyor** style pack — warm peach paper where an
unseen terrain is mapped: contour lines for texture, flat portraits for proof, a teal
that states and a pink that answers.

The pack document is the source of truth for every value here:
`plugins/sheleg-design/skills/sheleg-design/styles/surveyor.md`. This kit is what
those values look like when they are built, and `src/styles.css` opens with the
pack's token layer copied byte for byte — never transcribed.

```bash
npm install && npm run build   # tsc only; there is no bundler in this kit
```

## What ships

**The spine**, identical in name, props and types across every SHELEG kit: `Button`,
`Card`, `Chip`, `Stat`, `Heading`, `Rule`.

**The signature**: `StatSlab` (the counted reading in the working hue), `Delta` (a
reading's movement, arrow included), `Portrait` (the flat still), `TintPanel` (tense
as tint), `Closer` (the one dark slab — the signature element), `Dialogue` (the
teal-Q/pink-A pair), `Pulse` (the one loop), `Field`, `NavBar`, `Empty`.

## The three rules a generator loses first

1. The page is flat: no shadow on anything but the detached nav, and elevation is a
   tint. A `shadow-md` is a foreign object.
2. The teal ladder is shifted for AA: `--action` `#0a7269` writes and fills;
   `--accent` `#0d9488` is large-only (`#ffffff` on it is 3.74:1).
3. The pink answers, it does not speak: `--pink` for glyphs and tints beside
   readable ink, `--pink-deep` when pink must carry a word.
