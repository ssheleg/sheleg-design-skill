---
category: Signature
---

Product proof, and in this pack it is **never a screenshot**: a silent looping recording
in a 16:9 box with a 1px hairline, `object-fit: contain`, and no radius.

`label` is required and becomes the `aria-label`, because a silent autoplaying video with
no accessible name is a decorative element pretending to be an argument.

**The component does not start playback.** Gate it from the page with an
IntersectionObserver — the reference uses `rootMargin: 20% 0px` — and pause every frame
under reduced motion rather than hiding it. A kit is the static half of a pack and does
not own the page's motion policy.

```tsx
<FilmFrame src="/media/create-worker.mp4" label="Creating an AI worker" tone="light" />
```
