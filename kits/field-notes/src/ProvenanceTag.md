---
category: Signature
---

`[EXTRACTED]` · `[INFERRED]` · `[AMBIGUOUS]` — bracketed mono at 10px and
`0.08em`, transparent fill, a 1px border of the state's own ink at 25% alpha, at
`--radius-sm`. The three states map to `--verify-ink`, `--brand-ink` and
`--witness-ink`; the border mixes from `currentColor`, so one rule serves all
three and adding a fourth state means adding a fourth semantic hue, which the pack
bans.

**It sits inline with the claim it qualifies, never in a legend.** A legend makes
the reader leave the sentence to find out how the sentence is known, which is the
opposite of what this pack exists to do — the tag has to be readable in the same
glance as the words it marks. For the same reason it has no hover state: it is a
label, not a control.

Never replace it with a confidence percentage. A number pretending to be a
probability is precisely what this tag exists instead of, and the pack bans the
substitution by name.

```tsx
<p>
  Resolved through the re-export chain <ProvenanceTag state="inferred" />
</p>
```
