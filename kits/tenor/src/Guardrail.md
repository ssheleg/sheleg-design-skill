---
category: Data
---

The pack's status primitive, and the proof of its palette rule: **severity is value, not
hue.** `ask` is the orange, `limit` is the deep paper, `never` is the ink — three levels,
one hue, and the word carries the meaning in all three.

`label` is a required prop for the same reason the palette states it: the orange sits at
3.02:1 on the paper and cannot carry a meaning by itself.

Reach for this before `--good` / `--warn` / `--danger`. Those exist for product surfaces
that genuinely need a success state, and `--good` is the only value in the pack that the
reference does not contain.

```tsx
<Guardrail severity="ask" label="ALWAYS ASK">Before changing forecast assumptions</Guardrail>
<Guardrail severity="limit" label="LIMIT">250 CRM records per run</Guardrail>
<Guardrail severity="never" label="NEVER">Changes pricing or commission rules</Guardrail>
```
