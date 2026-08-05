---
category: Foundations
---

The hairline that does this pack's composition. Ten of the reference's sixteen
sections are separated by a single 1px `--line` and nothing else — no flipped
background, no slab, no full-bleed colour. `hairline` is that line; `strong`
steps to `--line-strong` where two regions genuinely part company. Pass
`className="fn-rule--section"` for the 64px section rhythm instead of the
default 24px.

**The ruled sheet is this component, and there is no `RuledSheet`.** A section
divided by one hairline is a `Rule` with `--section-pad-y` around it, and giving
that arrangement a second name would be the `--accent-dim` mistake in component
form: two names, one thing, and a design agent that has to guess which is meant.

```tsx
<section>
  <NumberedEyebrow index={3} total={9}>How it works</NumberedEyebrow>
  <Heading>Every edge says how it knows</Heading>
</section>
<Rule className="fn-rule--section" />
<section>…</section>
```
