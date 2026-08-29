---
category: Surfaces
---

Sticky at `--nav-h` (64px, every width), transparent over the field at rest. The
consumer toggles `sv-nav--detached` on scroll: the bar fills `--surface` and gains
`--shadow-nav` — the page's one shadow, measured as an event, not a tier. Below
48rem the link row yields to a toggle.

```tsx
<NavBar brand="SE Visible" actions={<Button size="sm">Start free trial</Button>}>
  <Button variant="ghost" size="sm">Pricing</Button>
</NavBar>
```
