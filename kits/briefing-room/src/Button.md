---
category: Actions
---

A deck is presented, not operated, so a button here is rare and always a real
affordance — an appendix link, a live demo, a source. It wears the slide
furniture face: mono, uppercase, tracked, pill radius. `primary` is the accent
fill with `--accent-ink` on it (never white — that is a ban), and the accent is
the one signal on a slide, so a slide with a primary button spends its accent on
that button. `secondary` is the panel-on-hairline form for everything else and
`ghost` the bare one for a footer link. Hover swaps colour instantly and focus
draws a 2px accent ring; nothing transitions, because nothing in this pack does.

```tsx
<Button onClick={openAppendix}>Read the appendix</Button>
<Button variant="secondary" onClick={openModel}>Open the model</Button>
<Button variant="ghost" size="sm" onClick={openSources}>Sources</Button>
```
