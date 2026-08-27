---
category: Actions
---

The pill field: `--control-h` tall, `--surface` fill, a `--rule-w` hairline at the
ink's 12%, and the same geometry as `Button` so a form row reads as one object. Focus
moves the border to `--focus-color` **and** adds `--focus-ring-field` — both, because
the ring alone composites too faint to carry the state.

`error` is what makes the invalid state legal: the border takes `--danger` and the
message appears with it. A red border on its own is a colour carrying meaning alone,
which this pack bans.

```tsx
<Field label="Work email" name="email" type="email" placeholder="you@company.com" />
<Field label="Work email" name="email" type="email" error="Use your work address." />
```
