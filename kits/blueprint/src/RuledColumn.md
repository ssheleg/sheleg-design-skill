---
category: Foundations
---

Two 1px verticals in `--line-strong` at `--column-max` 1280px, running the full
height of the section.

This is the layout made visible. A max-width container with no rules is a
website; the same container with its boundaries drawn is a sheet, and that
difference is most of what separates this pack from a plain white page.

Below 1024px the rules move to the viewport edges; below 768px they are removed
entirely.

```tsx
<RuledColumn><Heading level={1}>Give agents knowledge</Heading></RuledColumn>
```
