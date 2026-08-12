---
category: Data
---

A `<dl>` / `<dt>` / `<dd>` whose answers are **always visible**. The reference
ships zero `<details>` and zero `<summary>` elements on this section, and that is
the single best decision on its page: every answer is flat text in the DOM,
semantically paired with its question, readable without running a line of
JavaScript.

There is no `collapsed` prop and there will not be one. An accordion trades an
extractable answer for a click, and the answer is the reason the section exists.
Nine questions expanded at 14px cost less vertical space than most people assume,
and nothing here animates because nothing here opens.

Pair it with `FaqSchema` in the host app so the visible text and the `FAQPage`
JSON-LD come from the same array — the reference publishes the section without the
schema, which is the gap this component exists to close.

```tsx
<FaqList entries={[
  { q: 'What happens when a post fails?', a: 'We auto-retry, then fire a webhook with the reason.' },
]} />
```
