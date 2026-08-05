---
category: Data
---

The compact figure, for a row of two or three inside a `Card` — a mono uppercase
label, a 36px tabular value, and the source line beneath it. `source` is typed
optional because the spine's API is identical in every SHELEG kit, but this pack
bans numbers without sources: **always pass it.** When the figure is the slide's
argument rather than one of several supporting readings, use `SourcedNumber`,
which sets it at 64px and makes the source a required prop instead of a promise.

```tsx
<Stat value="£1.4bn" label="Serviceable market" source="ONS 2025 · UK only" />
<Stat value="18 mo" label="Median payback" source="Cohort model v7" />
```
