---
category: Foundations
---

The type ramp made visible, in Bricolage Grotesque at 600: `1` is 44px, `2` the
40px section heading, `3` the 30px sub-head. Every display size tracks at the
same `-0.025em` — one authored decision, not three, and changing it on one
heading breaks the only thing holding the ramp together. There is no italic in
this pack and none in the face, so emphasis inside a heading is a colour change
on one phrase, never an `<em>`.

Write the text as a **claim**. "The answer is a path, not a vibe." "Every edge
says how it knows." Not "Features", not "Benefits" — a heading that names a
category turns the document back into a brochure.

```tsx
<Heading level={1}>Every edge says how it knows</Heading>
<Heading level={2}>The answer is a path, not a vibe</Heading>
<Heading level={3} className="fn-heading--quiet">What we extracted</Heading>
```
