---
category: Signature
---

**The pack's signature element.** A 16px-high chip in a card's title row saying
how this card's number is known: `verified` in `--info` when it came from a
definition the reader can open, `inferred` in `--accent` when the system derived
it by a step it can name, `unverified` in `--warn` when it cannot. Pass `href`
and it becomes the link to the proof — which is the difference between a seal
and a sticker.

Three rules decide whether it is honest, and they are
`AI_PRODUCT_PATTERNS.md` §4 applied to a card rather than a span:

1. **Every state must be reachable.** If nothing is ever `unverified`, readers
   learn to skip all three.
2. **The label must be derivable from something real** — a metric definition, a
   query, a retrieval hit. A seal assigned by a second model call guessing at
   the first one is confidence theatre with better typography.
3. **It seals a card, not a screen.** One badge over twelve numbers hides
   exactly the number that needed checking.

The word is always rendered, never the glyph alone: in light mode all three
hues sit under 4.5:1 on the field, so the word is what carries the meaning.

```tsx
<Seal state="verified" href="/metrics/mrr" />
<Seal state="inferred" label="Derived" />
<Seal state="unverified" />
```
