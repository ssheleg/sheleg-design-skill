---
category: Actions
---

The press is this pack's signature, and it lives here. A button stands `3px`
proud of the paper on a hard zero-blur ink offset; hover translates it `2px` and
shrinks the offset to `1px`; `:active` translates `3px` and removes the offset
entirely — the control has bottomed out. The ink displaced is constant at every
step, which is why it reads as movement rather than as a restyle.

`primary` fills with `--action`, not `--accent`: the measured orange carries
white at 2.89:1 and no type size rescues that. `secondary` is the same outline
and offset over `--surface`. `ghost` keeps neither, for a toolbar row where an
outline would add a line the eye has to parse.

```tsx
<Button onClick={start}>Start free</Button>
<Button variant="secondary" onClick={book}>Book a demo</Button>
<Button variant="ghost" size="sm" onClick={dismiss}>Not now</Button>
```
