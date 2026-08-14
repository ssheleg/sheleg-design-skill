---
category: Actions
---

`primary` is the inverted field: solid `--accent`, label in `--accent-ink`, and the
capsule radius the whole pack is built from. **Its hover is theme-dependent and that is
deliberate** — on paper the fill goes whiter, on coal it goes away and leaves an outline.
Copying one gesture into both themes makes the button vanish in one of them, because on
paper there is nowhere brighter to go and on coal there is nowhere darker.

`secondary` is the pack's single exception to the capsule: `--r-md`, a hairline border,
a `--muted` label. It exists for the path that is not being recommended — the reference
spends it once, on `or install the local version` under the hero.

`ghost` is a text button; the label carries the whole affordance.

Nothing presses. There is no `:active` transform anywhere in this pack — hover is
colour, border and fill only.

```tsx
<Button>Join the waitlist</Button>
<Button variant="secondary">or install the local version</Button>
```
