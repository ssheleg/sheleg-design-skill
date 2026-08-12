---
category: Foundations
---

Levels are the spine's contract, identical in every kit, so the prop comment
names the exemplar's sizes rather than this pack's. Here they resolve to
`--t-display` (48px, weight 700, `--tr-display`, set solid) at level 1,
`--t-title` (24px) at level 2 and `--t-body` (14px, weight 600) at level 3.

The display **stops at 48px**. There is no step above it and adding one breaks the
register: a man page does not shout.

Level 1 carries the `fadeInBlur` entrance once, after `--stagger`. Levels 2 and 3
do not animate — in most sections the visible section heading is a `LabelChip`
anyway.

```tsx
<Heading level={1}>The social media and messaging API for developers.</Heading>
```
