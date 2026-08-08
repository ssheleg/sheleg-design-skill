---
category: Data
---

A mark **and its word** — `● Listening`, never a bare dot. `label` is a required
prop, and that is the entire design of this component.

This is where the pack's colour rule stops being advice and becomes API. The
measurements behind it:

| Pair | Full colour | Protanopia | Deuteranopia |
|---|---|---|---|
| `--good` / `--danger` | 14.0 | **7.2** | **5.9** |
| `--signal` / `--accent` | 28.3 | **6.8** | **6.7** |

The floor is 8. Both pairs are under it, and the second one is invisible to the
repository's palette gate, because `--signal` is not among the names it treats
as semantic. So for a reader with protanopia the word is not a helpful extra —
it is the only thing carrying the meaning.

An API that let you omit the label would be an API that lets you ship that bug,
which is why `label` is not optional and why there is no `dotOnly` prop to add
later.

There is no confidence percentage here either. A number with nothing behind it
is what a named state exists instead of.

```tsx
<StatusPill status="live" label="Listening" />
<StatusPill status="danger" label="Needs review" />
```
