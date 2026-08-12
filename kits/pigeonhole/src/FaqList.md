---
category: Data
---

A `<dl>`, always open. There is no `collapsed` prop on purpose: the reference
ships seven `dt`/`dd` pairs in served HTML and no `<details>`, and an answer a
crawler cannot read without running JavaScript is an answer that is not there.

```tsx
<FaqList entries={[{ q: 'Which providers?', a: 'Gmail and Outlook.' }]} />
```
