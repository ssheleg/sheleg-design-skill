# @sheleg-design/test-drive

The React reference kit for the **Test-drive** style pack — warm paper and white cards
where the set piece is the live product running inside drawn browser chrome, and a
founder's hand annotates the tour.

The pack document is the source of truth for every value here:
`plugins/sheleg-design/skills/sheleg-design/styles/test-drive.md`. This kit is what
those values look like when they are built, and `src/styles.css` opens with the pack's
token layer copied byte for byte — never transcribed.

```bash
npm install && npm run build   # tsc only; there is no bundler in this kit
```

## What ships

**The spine**, identical in name, props and types across every SHELEG kit, so switching
packs swaps identity rather than API: `Button`, `Card`, `Chip`, `Stat`, `Heading`,
`Rule`.

**The signature**, this pack's own: `DemoFrame` (the browser chrome around a running
interior — the signature element), `Annotation` (the hand), `Marker` (the
highlighter), `Delta` (a vital sign's movement), `Machine` + `Caret` (the quarantined
terminal), `ThinkingDots` (the machine's loader), `Field` (and the `td-join` pair),
`NavBar`, `Empty`.

## The three rules a generator loses first

1. The coral splits: `--accent` lights, fills and blinks; `--action` carries every
   body-size word. `#ffffff` on `#e16540` is 3.42:1 — that is why both exist.
2. The lit shadow belongs to controls; a card takes `--ring-card` and nothing else.
3. The `DemoFrame` interior runs. A screenshot inside the chrome is `showroom`'s
   exhibit, not this pack's proof.
