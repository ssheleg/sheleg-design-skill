# @sheleg-design/datasheet

The React reference kit for the SHELEG **Datasheet** style pack — an off-white spec
sheet, a live instrument built from hairline cells at radius zero, and a dark alarm
state the instrument enters when it detects the reader is hiding.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/datasheet.css` byte for byte, and the rules the design agent must
obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
