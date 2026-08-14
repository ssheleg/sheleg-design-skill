---
category: Signature
---

The pack's loading idiom, and the reason it needs no spinner on a data path: one mono
line per step, appended as the run reports it, with a status dot, a mark and — on the
running line only — the caret.

**Nothing slides.** A run appends a line every few hundred milliseconds for thirty
seconds; animating the append is motion on a high-repetition path, which the motion
doctrine kills outright. The list grows and the page stays still.

Exactly one caret per page. Under reduced motion it stops blinking and holds visible.

```tsx
<StepLog
  steps={[
    { text: 'Fetching prowl.chat', state: 'done' },
    { text: 'Checking 5 MCP servers', state: 'running' },
  ]}
/>
```
