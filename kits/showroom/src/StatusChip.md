---
category: Data
---

A tinted chip containing its word. The reference does exactly this in its ICP-fit
and ARR columns, and it is the right call: `--good` and `--danger` sit **4.9
apart under deuteranopia**, the classic pair, so a bare dot carries no meaning
for that reader.

`label` is a required prop. That is deliberate — it makes the rule structural
rather than advisory, and there is no `dotOnly` variant to add later.

There is no confidence percentage here either. A number with nothing behind it is
what a named state exists instead of.

```tsx
<StatusChip status="good" label="Excellent" />
<StatusChip status="warning" label="Low" />
```
