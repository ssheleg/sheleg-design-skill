---
category: Signature
---

**The colourless chrome.** A full-colour screenshot of the product sits in a
frame that contains no hue at all — the card's radius, the one shadow, and
nothing else. This is the pack's second motif and the reason the accent is
black: every colour a reader sees on the page belongs to the thing being sold.

The frame carries a real `aria-label` describing what the shot shows. A frame
whose label repeats the section heading is a frame that told a screen-reader
user nothing.

```tsx
<ProductFrame label="The orders list, filtered to unfulfilled">
  <img src={shot} alt="" />
</ProductFrame>
```
