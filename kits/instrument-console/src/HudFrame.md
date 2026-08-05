---
category: Signature
---

The viewport chrome: a thin `--hairline` frame with four corner ticks and an
optional mono label set into the top-left. It is the pack's way of saying "this
region is under observation" — wrap a hero, a diagram or a control panel in it.
The scan and dim of off-band sections belong to the scroll layer and are not in
this kit; the frame here is the static residue of that motif. Corner ticks are
decorative and hidden from assistive tech, so the label is the only thing a
screen reader gets — make it name the region rather than repeat its contents.

```tsx
<HudFrame label="FLIGHT DECK">
  <Heading level={2}>Downlink control</Heading>
  <Telemetry items={channels} />
</HudFrame>
```
