---
category: Signature
---

Symptom and topic chips as a rail: `20px` radius, `8px 16px` padding, `11px`
gaps, the selected one filled `--surface-ink` under `--on-ink`. **There is
always exactly one selected** — the rail has no empty state, because "everything"
is itself one of the items rather than the absence of a choice.

It does double duty, and that is the point: it filters, and it reads as a
plain-language list of what the product is for. Write the labels the way a
customer would say them out loud.

Rows key on a real `id`, never an array index. Each chip is a real `<button>`
carrying `aria-pressed`.

```tsx
<ChipRail
  label="What it is for"
  items={[
    { id: 'all', label: 'Everything' },
    { id: 'sleep', label: 'Sleep' },
    { id: 'energy', label: 'Afternoon energy' },
    { id: 'gut', label: 'Digestion' },
  ]}
  selected={topic}
  onSelect={setTopic}
/>
```
