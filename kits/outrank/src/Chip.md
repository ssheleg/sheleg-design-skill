---
category: Data
---

A pill that labels something already true — `New`, `Beta`, a category, a count.
`tone="accent"` puts it on `--accent-wash` for the one value that is the screen's
subject.

**A chip never carries a status colour as text.** `--info`, `--success`,
`--danger` and `--warning` measure 3.3:1 and below on `--bg`: they are the dot,
the bar or the fill. When the state has to be read, the label takes
`--info-ink` or `--success-ink`, which clear AA.

```tsx
<Chip>Beta</Chip>
<Chip tone="accent">404 keywords</Chip>
```
