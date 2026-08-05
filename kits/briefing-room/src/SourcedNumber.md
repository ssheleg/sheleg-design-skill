---
category: Signature
---

Every number carries its source, in mono, directly beneath the figure. That is a
pack rule with two separate reasons: an unsourced figure on an investor slide is
a liability, and the source line is also what makes the layout read as
instrumentation rather than as a poster. `source` is therefore a **required**
prop — the component will not compile without one, which is the only way a rule
like this survives the slide written at 1am before the meeting.

Name the publication, the year and the cut ("World Bank Findex 2025", "Internal
cohort model v7 · UK only"). "Internal data" is not a source; it is a way of
saying there isn't one.

```tsx
<SourcedNumber value="2.1bn" label="Adults with an account, no advice" source="World Bank Findex 2025" />
<SourcedNumber value="41%" source="FCA Financial Lives 2024 · UK adults" />
```
