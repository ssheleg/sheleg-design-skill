# @sheleg-design/roster

The React reference kit for the SHELEG **Roster** style pack — a white field in a faint
grid of squares whose argument is other people's names: an engine's wordmark inside the
headline, client logotypes in six pill-labelled industry columns, a review score somebody
else computed.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/roster.css` byte for byte, and the rules the design agent must obey are in
[`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.

## The spine, and this pack's five

`Button`, `Card`, `Chip`, `Stat`, `Heading` and `Rule` are identical in name, props and
types across every SHELEG kit — switching packs swaps identity, not API.

| Component | What it is |
|---|---|
| `IndustryColumn` | a pill-labelled column of other companies' marks, hairline-divided — the **signature element** |
| `LogoTile` | one third-party mark, greyscale at rest, full colour on hover, and it never moves |
| `Eyebrow` | the only tracked type in the pack, and a `<p>` rather than an `<h2>` |
| `StepCard` | copy beside a product shot, with a two-digit number in the accent |
| `FaqList` | a `<dl>` whose answers are always visible |

## Why the accent never carries a word

Both of the reference's oranges fail as a text or label colour: `#fa5c12` is 3.18:1 on
white, and white on `#f25533` at the nav pill's 16px/600 is **3.43:1**. The kit ships
`--accent-ink` at 4.52:1 for anything that has to be read, keeps the accent for fills and
large text, and makes the primary button black — which is what the reference itself does
for its hero, at 19.66:1.

## Two breakpoints, both derived

`IndustryColumn` goes two-up to one-up below **220px of its own width**; `StepCard`
collapses its split below **640px of its own**. Neither number is the viewport breakpoint
the reference used, because a column that is 300px wide on a 1440px screen needs the
narrow layout and a viewport query cannot see that.
