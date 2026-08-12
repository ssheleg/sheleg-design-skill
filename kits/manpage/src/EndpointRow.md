---
category: Data
---

The "what you can do" row: a method badge, a path in mono, and one line of prose.
It is how this pack lists capability without a feature grid — each row is a thing
you can call, so the list reads as an index rather than as marketing.

The badge is a status token on its own tint at `--r-chip`: `--info` for writes,
`--success` for reads. The method word is always spelled out, never colour alone —
`GET` and `POST` separate by 29.2 at full colour but only 16.3 under dichromacy,
and a reader who cannot tell them apart still has to be able to read them.

`selected` marks the row the surrounding copy is talking about, using
`--accent-wash`. At most one per list.

```tsx
<EndpointRow method="GET" path="/connect/{platform}">One OAuth flow for every platform.</EndpointRow>
<EndpointRow method="POST" path="/posts" selected>One call, 16 platforms.</EndpointRow>
```
