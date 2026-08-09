---
category: Data
---

A row inside a specimen: 36px tall, a `1px --line-weak` bottom rule, tinting to
`--accent-wash` on hover and taking a 2px `--accent` left edge when selected.

Rows **do not lift**. There is no shadow inside a specimen, and a hovering row
that rises is the clearest tell that the page was built by someone who had not
used the product it is selling.

```tsx
<DataRow selected onSelect={open}>Vercel</DataRow>
```
