---
category: Data
---

Label above at `--t-meta` uppercase, tracked `--track-wide`, in `--muted`;
figure at `--t-card` weight 600 in `--ink-strong`; source below in
`--font-data`.

The label comes first so the eye lands on the figure without hunting. `source`
is optional and should almost always be given — a figure with no provenance is
the thing this library's own doctrine bans, and on a page whose whole argument
is a demonstration an unsourced number is the one element that can make the
demonstration read as a mock.

```tsx
<Stat label="Median response" value="2h 14m" source="past 30 days" />
```
