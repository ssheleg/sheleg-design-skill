---
category: Signature
---

The mono kicker that sits above a heading and says what kind of thing follows —
"Field report", "Method", "Chapter 03". Tracked `0.18em` and uppercased, it is
the smallest piece of the editorial voice and the one that appears most often.
`tone="accent"` puts it in sage for the one kicker that is the page's signal;
everything else stays in `--ink-soft`, which is the point — an eyebrow that
shouts is a headline that has lost its nerve. Pair it with `Heading`, never
instead of one: it labels, it does not title.

```tsx
<Eyebrow>Method</Eyebrow>
<Heading level={2}>How the sweep reads a pricing page</Heading>

<Eyebrow tone="accent">The signal</Eyebrow>
```
