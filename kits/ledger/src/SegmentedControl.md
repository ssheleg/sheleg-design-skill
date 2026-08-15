---
category: Signature
---

The pack's scope switch, and its worked example of concentric radii: a 15px
track with 4px of padding holding a 10px thumb — outer minus the padding between
them, never the same radius twice. Track is `--inset`, thumb is `--panel-2`,
both 38px and 30px tall as measured.

Use it wherever the options are three or fewer; a fourth option is a select.
Nothing animates: a range switch is a high-frequency control and the motion
doctrine's frequency table cuts before taste gets a vote.

```tsx
<SegmentedControl
  label="Time range"
  options={[{ value: '6m', label: '6 months' }, { value: '12m', label: '12 months' }]}
  value={range}
  onChange={setRange}
/>
```
