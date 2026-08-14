# @sheleg-design/ora

The React reference kit for the SHELEG **Ora** style pack — a warm coal field with cream
ink and no third hue, where the accent is the inverted field, a serif carries every human
sentence and a monospace every machine fact, and the only surface that leaves the page
plane goes down, into a terminal block cut below the field.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/ora.css` byte for byte, and the rules the design agent must obey are in
[`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.

## The spine, and this pack's six

`Button`, `Card`, `Chip`, `Stat`, `Heading` and `Rule` are identical in name, props and
types across every SHELEG kit — switching packs swaps identity, not API.

| Component | What it is |
|---|---|
| `Verdict` | one number in the display serif, in its grade colour, with the letter and the word beneath — the **signature element** |
| `LayerBar` | the weighted score bar, where a layer that does not apply is hatched and reads `N/A` rather than empty |
| `Terminal` | the surface below the page plane: raw machine output, `white-space: pre`, and never a shadow |
| `StepLog` | the loading idiom — one mono line per step, appended as it happens, the caret on the running line |
| `SectionRule` | the band between sections: a squiggle through a hairline strip with a numbered label knocked out over it |
| `StatusDot` | a 6px dot and its word, where the word is a required prop |

## Theme

Dark is the default, because it is the default in the reference. Set
`data-theme="light"` on `:root` for the twin; both are declared in the token block at the
top of `src/styles.css`.

## What is not here

The hero's breathing glows, the drifting agent marks and the scroll-pinned comparison
section are page-level motion. A kit is the static half of a pack, and inventing motion
to fill that silence is the failure this note exists to prevent.
