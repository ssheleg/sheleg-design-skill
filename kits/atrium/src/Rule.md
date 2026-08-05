---
category: Foundations
---

A 1px divider in `--line`, the same hairline that separates the figures in a
stat row and bounds every card. `hairline` is decorative strength — 1.6:1 on the
field, well under the 3:1 WCAG asks of a UI boundary — so it may separate things
but must never be the only thing telling a user a control is there. `strong`
steps up to `--line-strong` where two regions genuinely part company.

Sections are **not** separated with rules or with a change of background: this
pack has one continuous cream field, and `--section-y` rhythm is the separator.

```tsx
<Card title="Biomarker panel" meta="128 markers · updated quarterly">
  <p>Every panel is read by a physician before it reaches you.</p>
  <Rule />
  <p>Results land in the app within five business days.</p>
</Card>
```
