---
category: Signature
---

The card the page is made of, in two halves. The top is the agent speaking, set on
`--gradient-dusk` in `--on-accent`, with the artefact it produced underneath the
sentence. The bottom is `--surface`, a heading in `--ink` and a paragraph in
`--ink-soft`.

No border and no shadow on either half — the two fills are the separation, which is
this pack's whole elevation model. `--r-card` rounds the outside; the seam between the
halves is square.

```tsx
<QuotedCard
  quote="Shipped. The deck is in the channel and the portal is live."
  title="Real output, not just text"
  artefact={<Chip>Weekly-Performance.pdf</Chip>}
>
  Finished decks, dashboards and deployed apps — at a link, not described.
</QuotedCard>
```
