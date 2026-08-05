---
category: Signature
---

Printer's registration marks at the four corners: eight 1px arms of `--crop-len`
inset by `--crop-inset`, drawn in ink at 30%. They cost nothing and they state the
thesis — this page was printed and trimmed, and what you are reading is a document
rather than a screen.

Drop one inside any `position: relative` container; it is `aria-hidden`, has no
pointer events, and is hidden below `48rem`, because a desktop-only flourish that
survives into a phone layout becomes a touch target nobody meant to ship. On the
dawn — the only dark surface in the pack — pass `className="fn-crop--on-deep"`.

They recur, which is exactly why they are a motif and not the signature element:
that is `DawnHero`, and it happens once.

```tsx
<main style={{ position: 'relative' }}>
  <CropMarks />
  <Heading level={1}>Every edge says how it knows</Heading>
</main>
```
