# @sheleg-design/ledger

The React reference kit for the **Ledger** style pack — a warm cream console for
a product that answers questions about data, extracted from `basedash.com` on
2026-08-15.

```bash
npm install && npm run build
```

`src/styles.css` opens with `styles/tokens/ledger.css` copied byte for byte, then
the component layer. Consume `var(--…)`; never a literal.

Twelve components: the six-name spine every SHELEG kit shares (`Button`, `Card`,
`Chip`, `Stat`, `Heading`, `Rule`) plus this pack's own — `Seal` (the signature
element), `Kicker`, `DataTable`, `SegmentedControl`, `StatusDot`, `EmptyState`.

The pack itself — palette, measurements, hero, responsive rules, bans and traps —
is `styles/ledger.md` in the sheleg-design skill. `.design-sync/conventions.md`
is the short form that travels with a Claude Design sync.
