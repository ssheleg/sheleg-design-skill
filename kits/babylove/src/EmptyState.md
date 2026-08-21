---
category: Signature
---

**This pack's signature element.** Where a data source is not connected the card
renders at FULL SIZE — an icon, one sentence naming what connecting buys, and a
button: *"Connect Google Search Console to track your search performance and
rankings."*

It occupies exactly the space the data would, so the dashboard's shape does not
change when a source is added, and a new account reads as unfinished rather than
as broken. That is the difference between an empty state and a hole.

```tsx
<EmptyState title="Not connected yet" action={<Button variant="secondary">Connect site</Button>} />
```
