# @sheleg-design/briefing-room

The React reference kit for the SHELEG **Briefing Room** style pack — a dark,
mono-furnitured deck rendered as a product: a fixed 1280×720 frame, one electric
accent, and every number carrying its source.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/briefing-room.css` byte for byte, and the rules the design agent must
obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
