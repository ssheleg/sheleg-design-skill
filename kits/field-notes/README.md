# @sheleg-design/field-notes

The React reference kit for the SHELEG **Field Notes** style pack — an engineer's
notes, published: warm green-cast paper, one rust accent, numbered sections,
marked-up sources, and a dawn at the top that resolves into the page instead of
ending against it.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/field-notes.css` byte for byte, and the rules the design agent must obey
are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
