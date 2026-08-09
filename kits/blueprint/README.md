# @sheleg-design/blueprint

The React reference kit for the SHELEG **Blueprint** style pack — a drawing sheet: grid, ruled columns, registration marks, one electric blue, and zero radius anywhere.

It is generated from the pack, not authored beside it: `src/styles.css` opens
with `styles/tokens/blueprint.css` byte for byte, and the rules the design agent
must obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
