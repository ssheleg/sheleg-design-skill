---
category: Signature
---

The canvas, and the pack's defining constraint: a fixed **1280×720** frame with
`overflow: hidden` — not a flowing page. Everything else follows from it. Content
that does not fit becomes a **second slide**, never a smaller type ramp; shrinking
the ramp to fit is a ban, and the frame is where that ban is enforced. A fixed
canvas also fails silently — overflowing content is simply invisible in review and
painfully absent in the room — so check every frame at exactly 1280×720 before
shipping, not at whatever size the browser window happens to be.

The furniture is mono uppercase: the header reads `[04] MARKET · WHY NOW`, and the
footer carries the deck's own line on the left and the slide number on the right.
Numbered sections are what make a 40-minute deck navigable by voice ("go back to
four"). `glow` draws the one radial accent glow the pack permits per slide; it
lives here so it can never quietly become two.

```tsx
<SlideFrame number={4} section="Market · why now" footnote="Series B · March 2027" glow>
  <ClaimTitle>Financial access is already global; the gap is guidance.</ClaimTitle>
  <SourcedNumber value="2.1bn" label="Adults with an account, no advice" source="World Bank Findex 2025" />
</SlideFrame>
```
