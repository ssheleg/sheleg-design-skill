---
category: Signature
---

A vital-sign's movement: the number first, the arrow second, the hue third — `--good`
up, `--danger` down, and never the colour alone, which is why the arrow ships inside
the component. Sits in a `Stat`'s source slot.

```tsx
<Stat value="83%" label="Bounce rate" source={<Delta direction="up">1%</Delta>} />
```
