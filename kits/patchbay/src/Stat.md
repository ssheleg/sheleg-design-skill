---
category: Data
---

**The component that refuses to lie.** The reference ships `0+` under
`GITHUB STARS`, `DOWNLOADS` and `DISCORD MEMBERS` on a live page, and `0+`
under `TESTING` eight thousand pixels further down: its count-up animates from
zero and has no state for *the fetch did not return*, so the failure renders as
a precise, confident, wrong number.

An empty `value` here renders the pulsing skeleton at the figure's real
geometry and announces itself to a screen reader. It never renders a zero.

```tsx
<Stat value="9,412" label="GitHub stars" source="api.github.com · hourly" />
<Stat value="" label="Downloads" />
```
