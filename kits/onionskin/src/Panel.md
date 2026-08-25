---
category: Signature
---

A zero-radius rectangle with a 1px `--rule` hairline — the navy at 10% — a micro label
along its top in uppercase at `--track-micro`, and rows separated by `--rule-faint`.

**No radius, no shadow, no grey.** It reads as a region of a sheet rather than a card;
elevation here is `emphasis="subject"`, which lights the left and right edge with
`--edge-lit` (the accent at 28%, inset) without lifting anything. One subject per
section.

`boundary="provisional"` draws the hairline **dashed** — the reference's own motif for a
boundary around something that is not there yet: a drop target, a planned step, an empty
slot.

```tsx
<Panel label="Latency">…</Panel>
<Panel label="Retrieval" emphasis="subject">…</Panel>
<Panel label="Not configured" boundary="provisional">…</Panel>
```
