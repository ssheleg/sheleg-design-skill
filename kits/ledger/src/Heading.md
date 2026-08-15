---
category: Foundations
---

Three levels and no more: 1 is the page title at `--t-title` (34px, weight 400,
`--track-title`), 2 is a section at `--t-card` (18px, weight 500), 3 is a card
title at `--t-prose` (15px, weight 500). The prop comment is the spine's, shared
byte for byte across every kit in this library; the sizes it names are
`workbench`'s and the ones this pack renders are the three above.

The 48px display face is **not** reachable from here on purpose. It is one line
per page, on a signed-out or marketing surface, and giving it a `level` is how it
ends up three times on a dashboard.

```tsx
<Heading level={1}>Revenue overview</Heading>
<Heading>New signups by channel</Heading>
```
