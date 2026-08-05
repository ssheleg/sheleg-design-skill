---
category: Data
---

The mono token: 11px in the data face, tracked out, 1px hairline, pill radius.
Chips label what is already true — a band, a build, a region, a mode — and never
stand in for a button. `tone="accent"` outlines the one value that is the
screen's subject, and `selected` outlines it and steps the surface up: neither
fills with the accent, because the accent fill belongs to the CTA and a row of
filled chips is the christmas tree the pack warns about.

```tsx
<Chip>BAND S</Chip>
<Chip tone="accent">v2.14.0</Chip>
<Chip selected>FAULTS ONLY</Chip>
```
