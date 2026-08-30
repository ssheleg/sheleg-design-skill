---
category: Data
---

**Status here is never by colour alone**, and this component is why the rule is
enforceable: it always renders the arrow *and* the number, plus a screen-reader word.

`--good` and `--danger` sit 32.4 apart at full colour and **6.2** apart under
deuteranopia — green against red is the classic collision, and no re-stepping of this
hue pair fixes it. The arrow is the separation.

`surface="dark"` switches to `--good-on-dark` / `--danger-on-dark`. That is a
different ladder rather than a translation: the mint reaches AA on paper only at
near-black, which is a different colour.

```tsx
<Delta value="0.48%" direction="up" />
<Delta value="3 places" direction="down" surface="dark" />
```
