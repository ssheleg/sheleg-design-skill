---
category: Foundations
---

Three steps off the reference's nine-step title ramp. Each carries its **paired**
size and leading — `3.5rem / 3.78rem`, `2.75rem / 2.97rem` — because the system
ships them as one token so they cannot drift apart. Do not substitute a ratio.

Weight is **550**, never 700. Tracking runs negative here and **positive** on
body text, both within the same family; the crossover sits around `1.375rem`.

```tsx
<Heading level={1}>Everything you need to sell</Heading>
<Heading level={3}>Payments</Heading>
```
