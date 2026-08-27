---
category: Surfaces
---

A static `--nav-h` (65px) bar in the field's own `--bg` — not white, not frosted, no
shadow, no scroll-shrink — with one `--hairline` rule beneath. Brand left, links
centered as ghost buttons, one quiet lit control trailing. Below 48rem the consumer
replaces the link row with a toggle at the `--tap-min` floor.

```tsx
<NavBar brand="DataFast" actions={<Button variant="secondary" size="sm">Log in</Button>}>
  <Button variant="ghost" size="sm">Pricing</Button>
</NavBar>
```
