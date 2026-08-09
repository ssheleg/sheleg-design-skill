---
category: Data
---

`--ink-soft` at 12px/500, a 14px glyph ahead of the label, a `1px --line` bottom
rule; sorted headers go to full `--ink` and gain a caret.

**The icon is load-bearing.** A header row with icons reads as a real
application; the same row without them reads as a styled `<table>` — and since
this pack's entire argument is that the surface in the specimen is the real
product, a table that looks styled defeats the page.

```tsx
<ColumnHeader icon={<GlobeIcon />} sorted="desc" onSort={sort}>Domains</ColumnHeader>
```
