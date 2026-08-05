---
category: Signature
---

The static half of the pack's right-edge rail: act markers on a hairline spine,
with the current one lit in `--accent`. It renders position, not progress — there
is no scroll listener, no observer and no transition here, because the scroll
clock is motion and motion does not cross into a kit. Give it the acts and the id
of the one you are on; pin it to the right edge in your layout, which is why the
labels sit left of their ticks. Acts key on `id`, never on the array index.

```tsx
<ProgressRail
  acts={[
    { id: 'problem', label: 'Problem' },
    { id: 'control', label: 'Control' },
    { id: 'downlink', label: 'Downlink' },
    { id: 'proof', label: 'Proof' },
  ]}
  currentId="control"
/>
```
