---
category: Actions
---

The primary button is filled in `--ink`, not in the accent — this pack forbids
the accent from filling any control, which is what leaves the orange free to
mean "look here" wherever it does appear. One primary per view; `secondary` is
the hairline ghost every other action wears, `ghost` is the bare one for
toolbars and table rows where a border would add a line the eye has to parse.

Hover moves fill, border and colour only. Active presses to `scale(0.97)`, the
reference's own feedback, and reduced motion zeroes it through
`--press-scale`. `disabled` is this pack's decision rather than a measurement:
the reference has no disabled control anywhere on the page.

```tsx
<Button onClick={run}>Run query</Button>
<Button variant="secondary" onClick={openSql}>Show SQL</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Dismiss</Button>
```
