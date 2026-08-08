---
category: Foundations
---

`hairline` is `--line-soft`, `strong` is `--line`. Both are 1px at different
alphas; this pack has no thicker divider, and no shadow to separate anything
with either.

A rule means something different here than in a ruled pack. In `field-notes` the
hairline *composes* the page — sections are divided by nothing else. Here it is
furniture **inside** a panel or a window: table rows, a footer edge. Do not build
a page out of these; sections in this pack are separated by `--section-gap`
(200px) and by the field itself.

```tsx
<Rule />
<Rule tone="strong" />
```
