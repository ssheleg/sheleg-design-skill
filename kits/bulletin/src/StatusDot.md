---
category: Data
---

Status is **never by colour alone** in this pack, so `label` is required rather
than optional. Under deuteranopia `--danger` and `--warn` separate by 0.7 — the
green/amber/red triple is the classic confusion set and no palette solves it, so
the word carries the meaning and the dot reinforces it.

All four statuses clear AA on the paper, and the `[data-surface="ink"]` block
remaps every one of them — a theme that remaps its ink and leaves its statuses
behind is a defect this library has shipped before.

```tsx
<StatusDot status="good" label="Published" />
<StatusDot status="warn" label="Awaiting approval" />
```
