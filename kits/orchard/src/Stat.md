---
category: Data
---

A figure, its plain-language label, and the source it rests on. The value is set
in the **body** face at `--t-price`, not the display face — the same decision the
pack makes about prices, and for the same reason: a rounded display numeral
reads as branding, and a number a buyer is being asked to trust has to read as a
fact.

`source` is optional in the type and effectively mandatory in this pack. A
health page that states a figure without naming the study is making a claim it
has not earned; the citation sits in `--ink-soft` at 12px, which is exactly what
that token is for.

```tsx
<Stat value="87%" label="reported better sleep by week 6" source="n=412 · internal cohort, 2025" />
<Stat value="14 days" label="from swab to results" source="median, last 1,000 kits" />
```
