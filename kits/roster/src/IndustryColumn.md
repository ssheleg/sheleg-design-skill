---
category: Signature
---

**The pack's signature element.** A `--radius-pill` label over a column of other
companies' marks, divided from its neighbours by a 1px `--rule` — six across at 1440,
three at 768, two below, and the divider survives every step because the divider is
what makes it a wall rather than a pile.

It sets `container-type: inline-size`, so the marks inside answer to the column's own
width. Below **220px** the two-up grid goes to one, and that number is derived rather
than carried over from a viewport: two tiles at the `--tile` ceiling of 40px plus the
24px gap plus 24px of padding each side is 152px, and a logotype is wider than its
tile, so the pair crowds at roughly 220.

**Do not tidy the roster.** Equalising the logos' optical weights, tinting them to one
colour, or dropping the dividers each turn it into a decoration. Greyscale at rest is
the only normalisation allowed, and `LogoTile` does that.

```tsx
<IndustryColumn label="SaaS & Tech">
  <LogoTile label="ConsentStack"><img src="/consentstack.svg" alt="" /></LogoTile>
  <LogoTile label="Yardstick"><img src="/yardstick.svg" alt="" /></LogoTile>
</IndustryColumn>
```
