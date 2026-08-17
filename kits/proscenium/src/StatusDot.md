---
category: Signature
---

An 8px dot in the status colour with the state named in full beside it.

`label` is required by the type, and that is deliberate. Green, amber and red
are the classic confusion set and no palette solves it under dichromacy, so the
word carries the meaning and the colour reinforces it. A dot with no word is not
a shorter version of this component, it is a broken one.

Two of the three colours here are pack decisions rather than measurements — the
reference is a marketing site and paints no success and no error state — and the
token layer marks each at its declaration.

```tsx
<StatusDot status="ok" label="Verified" />
<StatusDot status="warn" label="Needs retry" />
<StatusDot status="neutral" label="Held" />
```
