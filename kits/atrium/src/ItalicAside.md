---
category: Signature
---

One phrase inside a serif headline turns *italic and terracotta*: "Life is
short? *We disagree.*"

**This is the pack's entire emphasis vocabulary.** No bold, no highlight fill,
no underline, no second hue, no size jump — those are all drift, and each one
costs the headline the thing that makes it this pack. One aside per heading, and
never two in the same viewport.

It inherits the family, size and 300 weight of the heading it lives in, so it is
the same sentence changing its mind rather than a second style pasted into it.
At heading sizes the accent clears the large-text contrast floor on the field and
on `--surface` alike, which is exactly why the device is safe here and an accent
word at body size is not.

```tsx
<Heading level={1}>
  A hundred years is <ItalicAside>a starting point.</ItalicAside>
</Heading>
```
