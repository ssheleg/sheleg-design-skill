---
category: Actions
---

One accent fill per view. In this pack the fill is `--action` — the reference's
own coral, kept because the coral button *is* the identity — but the label is
`--on-action`, which is ink rather than white. White on coral measures 4.16:1 and
does not clear AA at the 16px semibold the reference ships; ink clears at 4.55:1.
Where a white label is non-negotiable, hover onto `--action-strong` (burgundy,
13.34:1).

`secondary` is the white 1px-bordered control the reference pairs with it — on a
developer page that is usually an OAuth continue. `ghost` changes ink and nothing
else.

Transitions `background-color` over `--dur-instant` and nothing more: no lift, no
scale, no shadow bloom.

```tsx
<Button onClick={start}>Start for Free</Button>
<Button variant="secondary" onClick={google}>Continue with Google</Button>
<Button variant="ghost" size="sm" onClick={skip}>I'll do this later</Button>
```
