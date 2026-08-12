---
category: Signature
---

The pack's signature element: a 12px uppercase mono tag in a coral wash that **is
the section heading**, not an eyebrow sitting above one. The reference wraps the
span in a real `<h2>`, which is why its page keeps a clean outline — one `h1`, one
`h2` per section — while reading as a printed document rather than a marketing
page.

The label ink is `--accent-ink`, not `--accent`. Coral on its own wash measures
3.24:1; burgundy on the same wash measures 10.40:1. The chip looks identical
either way, so this is the one correction in the kit that is invisible and
mandatory.

Never interactive, never a pill: `--r-chip` is 2px, which is what keeps it reading
as a tag.

```tsx
<LabelChip>How It Works</LabelChip>
<LabelChip level={3}>WhatsApp Numbers</LabelChip>
<LabelChip level={null}>What's new</LabelChip>
```
