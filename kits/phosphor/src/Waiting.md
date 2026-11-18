---
category: Data
---

The pack's loader, and a pack decision: the reference ships none. A mono 12px caps line
at 0.1em in `--ink-muted` ending in a block cursor in `--accent` that blinks on
`steps(2)` over `--dur-cursor`. It carries `role="status"`, so the words are announced
and the cursor is decoration.

Never a spinner. Under reduced motion the cursor stops (paused, fully lit) rather than
blinking at a collapsed duration, which would strobe.

```tsx
<Waiting label="Waiting for your choice" />
```
