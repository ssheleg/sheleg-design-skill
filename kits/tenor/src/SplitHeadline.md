---
category: Signature
---

One sentence, two clauses, two values: the premise in `--ink-faint` and the claim in
`--ink`. The reader parses the emphasis before reading a word, which is why it belongs at
the top of the page and nowhere else. **Use it once.**

Both halves are block spans inside a single heading element, so the sentence remains one
string in the accessibility tree rather than two fragments.

The reference sets its muted half at `#a3a29d` — **2.36:1**, below even the 3:1 that large
text is allowed. This kit's `--ink-faint` keeps the measured value so the pack stays
honest about what it read; if the page must be conformant, override the token to `#8a8985`
(3.24:1) or darker and nothing else changes.

```tsx
<SplitHeadline
  muted="AI workers that attribute"
  claim="the outcome back to the token spend"
/>
```
