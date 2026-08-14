---
category: Foundations
---

The display face is **Lora, a serif doing the sans job** — `--font-sans` and
`--font-serif` resolve to the same family in the reference, so there is no sans in this
pack. Every heading is weight 400; the prose ramp never leaves regular.

Level 1 is the display step and takes the fluid clamp; 2 and 3 are fixed. A heading is
never set in mono: mono means a machine reported it.

```tsx
<Heading level={1}>Watch top agents use your site</Heading>
<Heading level={2}>Quick answers</Heading>
```
