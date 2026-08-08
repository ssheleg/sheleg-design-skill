---
category: Data
---

The mist panel — `--panel` at `--radius-lg` with hairline rows. Ink measures
9.76:1 on it, so it is safe for body copy; it and `--surface` are the only two
surfaces in the pack that are.

It is the one place below the hero where a real fill appears, and it earns that
because a comparison is the one thing that genuinely reads worse over a moving
field: the eye has to hold two columns still to compare them.

Every marked cell carries its **phrase**, not just its mark. A column of bare
accent dots is a legend a reader with protanopia cannot use — the accent and the
signal green sit 6.8 apart there, and see `StatusPill` for the rest of the
numbers. It is also simply worse writing: "Battle-tested, scalable" argues,
a dot does not.

```tsx
<ComparePanel
  headings={['Build it yourself', 'With Codos']}
  rows={[
    { dimension: 'System architecture', without: 'Ad-hoc, experimental', with: 'Battle-tested, scalable' },
    { dimension: 'ROI commitment', without: 'None', with: '10x+' },
  ]}
/>
```
