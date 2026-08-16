---
category: Data
---

Label above at 14 in `--muted`, figure at `--t-section` weight 700 with
`--track-tight` and tabular numerals, source below in `--font-data` at 12.

The order is the reference's and it is the right way round: the label is what
the reader is looking for, so it comes first and the eye lands on the figure
without hunting. `source` is optional and should almost always be given — a
figure with no provenance is the thing this library's own doctrine bans.

```tsx
<Stat label="Median response" value="2h 14m" source="past 30 days" />
```
