---
category: Actions
---

`primary` is an `--ink` fill and its label is `--on-ink` — **the field colour,
not white**, measured at 13.73:1. That is the pack's one counter-intuitive
button rule: the reference tints its button labels with the page, and a white
label reads instantly as a component borrowed from another kit.

`secondary` is the hairline outline (`1px var(--line)`), and `ghost` drops the
border for toolbars and table rows. The accent fill is a fourth state carried by
`Chip tone="accent"` and by the CTA class directly — it is deliberately not a
`variant` here, because a `variant` list invites picking one per button and this
pack allows at most one accent fill per view.

**Press is instant.** Hover scales to `1.02` over `--dur-base`; active drops to
`0.98` with `transition-duration: 0s`, so the control answers the finger instead
of easing after it. Filled and accent buttons carry the 22px accent-dot cursor.
Focus-visible is a 2px `--accent` outline at 2px offset — the one place the
accent is allowed beside text, because a ring is not text.

```tsx
<Button onClick={bookDemo}>Book a demo →</Button>
<Button variant="secondary" onClick={emailFounders}>E-mail founders →</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Not now</Button>
```
