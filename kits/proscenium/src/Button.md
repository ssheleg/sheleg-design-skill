---
category: Actions
---

Min-height 44, radius **4**, weight 600, label at 16 — and the radius is the
point. The reference's control is nearly square while its cards sit at 16, and
that gap is what keeps a roomy page from reading as soft. Rounding this to match
the card is the single most likely edit to make a page in this pack generic.

`primary` fills with the accent, carries `--shadow-control`, and states its
label colour on the rule rather than inheriting it, because an anchor reset that
says `color: inherit` will otherwise win the label and paint ink on accent.
`secondary` is the 1px `--edge` bordered one with no shadow; `ghost` carries no
fill and takes `--accent-deep` for its label.

**Active flattens the shadow instead of moving the control.** Nothing translates
and nothing scales — a button that pops on click has left this pack.

```tsx
<Button onClick={book}>Book a walkthrough</Button>
<Button variant="secondary" onClick={tour}>See it in action</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Not now</Button>
```
