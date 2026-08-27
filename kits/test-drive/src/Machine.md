---
category: Signature
---

The quarantined machine surface: `--machine` body under an optional
`--machine-chrome` title bar, `--r-card`, text in `--on-machine`. It does not flip
with the theme — dark on the light page and dark on the dark one — and its tokens
never reach a card. The terminal is set in the working sans, which is measured, not a
mistake.

`Caret` is the blinking cursor (`--on-machine-accent`, `--dur-caret` step-end) and is
legal inside `Machine` only. Under reduced motion it holds solid.

```tsx
<Machine title="npx datafast init">
  <span>Detecting framework…</span> <Caret />
</Machine>
```
