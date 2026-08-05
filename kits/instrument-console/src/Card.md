---
category: Surfaces
---

A machined panel: `--surface-1` inside a 1px `--hairline` at `--r-lg`, with a
title row whose `meta` sits right and mono — a run index, a channel id, a UTC
stamp. Elevation here is the surface step, so a card that needs to read as
raised moves to `--surface-2` rather than growing a shadow; there is no shadow
in this pack except `--accent-glow`. Stack cards on the `--base` field and let
the hairlines do the separating.

```tsx
<Card title="Telemetry downlink" meta="LINK-04 · 14:02:11Z">
  <Telemetry items={channels} />
</Card>
```
