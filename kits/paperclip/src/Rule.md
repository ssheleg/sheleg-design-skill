---
category: Foundations
---

The whole elevation system. `hairline` is 1px of `--border`; `strong` is
`--border-strong`, one step up, for an edge a reader has to find — an input, a diagram
connector, a table head.

**In dark the border token is alpha, not a colour** (`#ffffff1a`), which is why the same
rule reads correctly over the field, over `--surface` and over the warm terminal block
without being restated three times. Copying it out as an opaque grey breaks on the
terminal immediately.

A diagram's connectors take `strong` at **1.5px**, not 1px: a hairline disappears at
diagram scale, and the reference draws its org tree at 1.5px for exactly that reason.

```tsx
<Rule />
<Rule tone="strong" />
```
