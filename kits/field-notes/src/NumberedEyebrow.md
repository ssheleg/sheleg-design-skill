---
category: Signature
---

`〉 HOW IT WORKS [03/09]` — mono at 11px and `0.16em`, prefixed with a chevron and
suffixed with its position in the document, both at 55% opacity, built with
`::before` and `::after` off a `data-n` attribute. The DOM carries only the label;
the furniture is drawn by the stylesheet.

**This is the pack's most transferable device and the first thing to keep.** The
page numbers its own sections, and a marketing page that numbers its sections
stops being a brochure and becomes a document with a table of contents — which is
the entire argument of a pack called Field Notes. Use it on every section, in
order, with the same `total`; a document whose numbering skips is worse than one
that does not number at all.

Set `wide` for the roomier `0.18em` tracking where the label sits alone above a
lot of white. The index pads to at least two digits, so a nine-section page reads
`[03/09]` and a fourteen-section page reads `[03/14]`.

```tsx
<NumberedEyebrow index={3} total={9}>How it works</NumberedEyebrow>
<NumberedEyebrow index={4} total={9} wide>What we extracted</NumberedEyebrow>
```
