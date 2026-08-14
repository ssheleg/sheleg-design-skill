---
category: Signature
---

**The pack's signature element.** One number in the display serif, in its grade colour,
with a hairline `/ 100` at roughly half its size and the letter plus the word beneath.

Three rules, all load-bearing:

1. `grade` and `label` are **required props**. Under deuteranopia `--good` and
   `--danger` separate by 6.5 in dark and 7.4 in light — below the 8.0 CVD floor — so
   the letter and the word are what make the verdict legible, not the colour.
2. It is the only place in the pack where a status colour reaches display size, and the
   only place the serif carries a number.
3. Everything around it stays 11px mono and `--muted`. The contrast between the numeral
   and its own chrome is the composition; a second large element cancels it.

```tsx
<Verdict score="61" grade="C" label="Needs Work" />
<Verdict score="7" grade="F" label="Unusable" />
```
