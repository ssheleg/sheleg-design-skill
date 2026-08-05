---
category: Signature
---

**The signature element, and it happens once per page.** Not the crop marks and
not the numbered eyebrow — those recur, and recurrence is what makes them motifs.
The dawn happens once, at the top, and it is the only place this pack spends
contrast, saturation or spectacle.

It is a dark field that *resolves* into the paper rather than ending against it:
eight stops whose last one is `--bg` itself, so there is no seam. That is why the
pack never needs a second dark surface — the page has already been dark, at the
top, and came out of it. A hard-edged dark hero would read as two pages stapled
together. Below the dawn there is no second dark section, no dark band, no
full-bleed colour block, no photography bleed and no generative layer: only paper,
hairlines and ink. Spend the boldness here or the pack has no centre.

**It is static.** `--hero-dawn` is a gradient, not an animation — nothing fades
in, scrubs, parallaxes or renders to a canvas, and a particle field is the fastest
way to turn a document back into a landing page.

Three constraints the layout enforces and the copy has to respect: the headline is
capped at three lines by `--hero-line-cap` (at 1.02 leading a fourth line closes
into a block and the dawn stops reading behind it); the lede is held to
`--lede-max` so it ends above `--dawn-5`, where white copy has fallen to 4.06:1;
and the one accent phrase takes `--brand-on-dark`, never the paper rust, which
measures 2.29:1 up there. The first viewport carries the eyebrow, the headline,
the lede, up to three buttons and one proof line — no card, no screenshot, no
metric row.

```tsx
<DawnHero
  eyebrow={<NumberedEyebrow index={1} total={9}>Field notes</NumberedEyebrow>}
  headline={
    <>
      The answer is a <span className="fn-hero__accent">path</span>, not a vibe
    </>
  }
  lede="Every edge in the graph carries the pass that produced it."
  actions={
    <>
      <Button onClick={start}>&gt;_ Index your repo</Button>
      <Button variant="ghost" onClick={readDocs}>Read the docs</Button>
    </>
  }
  proof="1 204 883 edges · full index · 2026-08-04"
/>
```
