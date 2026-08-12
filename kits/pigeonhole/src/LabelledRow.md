---
category: Signature
---

One row of the product, labelled — the atom this pack is built from, and the
part of the page that is genuinely a component.

The chip sits **above** the row rather than inside it, which is how the reference
stacks them. `date` takes a short absolute date on purpose: "2 days ago" goes
stale the moment a screenshot of it is taken.

The page's set pieces — the chaos-to-order diptych, the composer with its
connector lines — are **raster art** on the reference, at 1152×703 and 1150×631.
Compose them as art direction with an aspect ratio, not out of these rows, and
never rotate anything: the measured page has zero rotated elements at three
viewports.

```tsx
<LabelledRow
  from="Jenny Louve"
  subject="Availability for follow up meeting"
  date="Sep 21"
  category="reply"
  categoryLabel="To Reply"
  unread
/>
```
