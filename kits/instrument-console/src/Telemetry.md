---
category: Signature
---

The annotated readout the pack's instruments are drawn around: hairline-separated
rows, every label and value in the mono face with tabular figures, and a `note`
under each value for the unit, the window or the limit that makes the number
mean something. `tone` is a status claim and nothing else — `ok` and `warn` are
the only two colours this pack allows beside the accent, so a green row must be
a verified green. Rows key on `id`. For a single headline figure use `Stat`;
`Telemetry` is for the block of channels read together.

```tsx
<Telemetry
  caption="DOWNLINK LINK-04"
  items={[
    { id: 'rate', label: 'BIT RATE', value: '2.048 Mbps', note: 'nominal 2.0' },
    { id: 'snr', label: 'SNR', value: '14.6 dB', note: 'floor 9.0', tone: 'ok' },
    { id: 'buf', label: 'BUFFER', value: '81%', note: 'spill at 95%', tone: 'warn' },
  ]}
/>
```
