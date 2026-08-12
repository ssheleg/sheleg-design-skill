---
category: Surfaces
---

The focal element of the hero, and the only dark surface on the light theme. A
`--r-panel` frame with three window dots, a filename, a language label and a copy
affordance — because the page's argument is the call, not a screenshot of a
dashboard.

Two rules it does not bend. It **scrolls horizontally and never reflows**: a
wrapped code sample is a wrong code sample. And it **never shrinks its type** below
`--t-mono` (12px) on small screens — the sample stops being evidence the moment it
becomes unreadable.

Place it at `--measure-hero` and let the fold crop it. The crop is what signals
there is more.

```tsx
<CodeFrame filename="zernio.ts" language="TypeScript">
  {snippet}
</CodeFrame>
```
