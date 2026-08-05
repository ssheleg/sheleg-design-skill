---
category: Signature
---

A heading that states the reader's suspicion **in the reader's own words**, over
a plain stack of oat cards. Not a benefit rewritten as a question — "Is this
worth £45 a month?" rather than "Why our value is unmatched". The layout device
is deliberately nothing: `44px` between the heading and the stack, `24px`
between the answers. The craft is entirely in the copy, and decorating it is how
an honest section starts to read as marketing again.

The stack is oat `Card`s. The "adjacent slabs never repeat a fill" rule is about
full-bleed `Slab`s; the rows inside one section are cards and are meant to
match.

```tsx
<ObjectionSection objection="Isn't this just an expensive multivitamin?">
  <Card title="It changes when you do">
    <p>Every retest reformulates the blend. A multivitamin cannot.</p>
  </Card>
  <Card title="You can check our working">
    <p>Every dose links to the marker that set it.</p>
  </Card>
</ObjectionSection>
```
