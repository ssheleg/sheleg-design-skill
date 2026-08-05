---
category: Surfaces
---

A bounded region inside the frame: `--panel` on a 1px `--line` at `--radius-lg`,
with mono furniture on the right of the title row. Elevation is that surface
step plus the hairline — never a glow, never a shadow on the card itself. **It
has no hover state and must not be given one:** a card that lifts under a cursor
during a live presentation is noise, and the room sees the noise rather than the
argument. Cards hold the parts of a diagram; they are not a replacement for one,
and a slide made of six of them is a bullet list wearing borders.

```tsx
<Card title="Guidance layer" meta="2027 · phase 2">
  <SourcedNumber value="41%" label="Advice gap" source="FCA Financial Lives 2024" />
</Card>
```
