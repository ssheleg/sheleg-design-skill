---
category: Data
---

A cell whose whole background takes the matching `--*-weak` tint while its text
takes the status token — the reference's own measured pattern (`--green-9` on
`--green-2`). The verdict is **always written out**, because the four statuses do
not separate under dichromacy: success and warning sit 3.7 apart under
deuteranopia against a floor of 8. The tint is emphasis; the word is the meaning.

Never a bare dot, and never a hue swap to indicate disabled — a disabled cell that
changes colour reads as a different verdict.

```tsx
<StatusCell label="VPN" reading="success">Not detected</StatusCell>
<StatusCell label="Bot" reading="danger">Detected — automation</StatusCell>
```
