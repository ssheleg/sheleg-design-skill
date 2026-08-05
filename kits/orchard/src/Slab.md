---
category: Signature
---

The composition unit of this pack. The page is a **stack of rounded slabs, not a
continuous surface**: each section is a `24px`-radius rectangle with its own
fill, `64px 24px` of padding, inset `8px` from the field so the field is always
visible around it, with `55px` of field between one slab and the next.

The fills carry meaning: **oat explains, sage invites, cacao emphasises**.

**Adjacent slabs never repeat a fill.** The field between them is the separator,
and two oat slabs in a row erase it. This component cannot enforce that — the
rule lives in the composition, one level above any single slab — so it is the
one thing to check by eye before shipping a page.

The sage slab sets cacao `--ink`, not `--on-primary`: oat on sage is 2.96:1,
below even the large-text floor. For small copy inside a sage slab, put a `Card`
in it rather than shrinking text onto the sage.

```tsx
<Slab fill="oat">
  <Heading level={1}>What the panel measures</Heading>
</Slab>
<Slab fill="sage">
  <Heading level={1}>Start with a single swab</Heading>
  <Button>Start your kit</Button>
</Slab>
<Slab fill="cacao">
  <Stat value="14 days" label="from swab to results" source="median, last 1,000 kits" />
</Slab>
```
