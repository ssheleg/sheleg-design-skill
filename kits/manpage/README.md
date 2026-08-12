# @sheleg-design/manpage

The React reference kit for the SHELEG **Manpage** style pack — cream paper under
the reader's own system monospace, a 48px display that never grows louder, coral
label chips that are real headings, and one dark code frame as the argument.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/manpage.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.

## The spine, and this pack's five

`Button`, `Card`, `Chip`, `Stat`, `Heading` and `Rule` are identical in name, props
and types across every SHELEG kit — switching packs swaps identity, not API.

The five that are this pack's own:

| Component | What it is |
|---|---|
| `LabelChip` | the coral section tag that **is** an `<h2>` — the signature element |
| `CodeFrame` | the dark panel holding the call; scrolls, never reflows |
| `TreeItem` | a `└` glyph in its own grid column, never a text prefix |
| `FaqList` | a `<dl>` whose answers are always visible, so a machine can quote them |
| `EndpointRow` | a method badge, a path in mono, one line of prose |

## The two things most likely to be broken

**The 4px body frame.** `body { padding: var(--frame) }` is what makes the page
read as a sheet laid on a desk. Deleting it produces no error and no failing test.

**The label chip's ink.** It is `--accent-ink`, not `--accent`. Coral on the chip's
own wash measures 3.24:1; burgundy measures 10.40:1, and the chip looks the same.
