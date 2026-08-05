---
category: Signature
---

The segmented pill: one `--panel-2` trough, the chosen option lifted onto
`--panel` behind a `--border-strong` edge. It is for switching a view between
two to four mutually exclusive states — a time range, an environment, a
grouping — where the options are short enough to read at 12px and stable enough
to memorise. More than four, or options that change per screen, is a select.
Each option is a real button with `aria-pressed`, reachable and operable from
the keyboard.

```tsx
<SegmentedControl
  label="Time range"
  options={[
    { value: '1h', label: '1h' },
    { value: '24h', label: '24h' },
    { value: '7d', label: '7d' },
  ]}
  value={range}
  onChange={setRange}
/>
```
