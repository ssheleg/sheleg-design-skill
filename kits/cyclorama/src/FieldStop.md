---
category: Foundations
---

The six stops of `ctaCycle`, each as a static surface.

**The cycle itself does not cross into a design system.** A kit is the static
half of a pack and motion stays behind in the pack — so what arrives here is not
an animation but the six extremes, which is the more useful thing to design
against anyway: a screen proved against stop 2 and stop 5 is proved against
every frame between them.

| Stop | Value | Note |
|---|---|---|
| 1 | `--field-1` | `0%`/`100%` — the rest stop; what a screenshot shows |
| 2 | `--field-2` | the **darkest**: the pack's contrast floor, ink at 12.79:1 |
| 3 | `--field-3` | blush |
| 4 | `--field-4` | lilac |
| 5 | `--field-5` | the lightest, ink at 14.67:1 |
| 6 | `--field-6` | warm cream |

Prove contrast against stop 2. Every ratio the pack claims is stated there,
because a claim made against the friendliest stop is not a claim about the page.

```tsx
<FieldStop stop={2}>
  <Heading>Most AI programs never reach the P&L.</Heading>
</FieldStop>
```
