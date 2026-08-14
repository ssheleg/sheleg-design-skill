---
category: Signature
---

Mono, 12px, UPPERCASE, tracked `--track-badge`, weight 500, in a `--r-pill` capsule
filled with one of twelve two-stop ramps and dusted with the pack's noise tile at 12%
under `isolation: isolate`.

**Each gradient ships with its own label ink**, hand-picked per ramp rather than computed,
because a 90° gradient has two ends and one label has to clear both: white on the six dark
ramps, and `#2a1530`, `#3d3010`, `#1a2a40`, `#2a2340`, `#1a3a38` on the five light ones.
Do not derive the ink from one end.

**Use them in order, and never repeat one on a page.** The badge is how a reader tells one
section from the next on a long scroll of near-identical dark panels; two sections wearing
the same ramp undo that in a single screenshot.

It is a `<span>`, not a heading and not a link. The heading is the line underneath it.

```tsx
<SectionBadge gradient={4}>Heartbeats</SectionBadge>
<Heading>Heartbeats keep the lights on.</Heading>
```
