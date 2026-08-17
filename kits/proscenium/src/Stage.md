---
category: Signature
---

**The one dark act.** A full-bleed `--stage` gradient block — measured stops,
`#07061d` to `#2a0b78` at 86.41% — placed once at the middle of the page.

**Once.** A second `--stage` block makes the page read as a section list rather
than as a design with a middle, and it is this pack's most likely drift because
the block is the easiest thing on the page to like. The measured reference has
exactly one.

Inside it, cards separate by `--stage-panel` and a seam rather than by
elevation; the stylesheet does that swap for any `.ps-card` inside `.ps-stage`,
so a card does not have to know where it is standing.

```tsx
<Stage>
  <Heading>One operating layer for every team working in Telegram</Heading>
  <UseCaseCards />
</Stage>
```
