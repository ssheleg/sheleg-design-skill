---
category: Signature
---

The floating nav: a `--surface-2` pill at `50px` radius with
`backdrop-filter: blur(20px)`, sticky at `top: 0`, riding over whatever slab is
passing beneath it. It **never changes size on scroll** — no shrink, no
condense, no border appearing at 40px down. The blur is the only thing
separating it from the slab underneath, and a nav that also resizes turns the
one steady element on the page into another moving one.

`--surface-2` is opaque, so the blur currently has nothing to show through. That
is a gap in the pack's token layer, not something to fix with a literal here: a
translucent oat is a colour this pack does not own, and colour is the one thing
a pack owns exclusively.

```tsx
<GlassNav label="Main">
  <a href="/how">How it works</a>
  <a href="/science">The science</a>
  <Button size="sm">Start your kit</Button>
</GlassNav>
```
