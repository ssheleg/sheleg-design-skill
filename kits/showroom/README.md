# @sheleg-design/showroom

The React reference kit for the SHELEG **Showroom** style pack — a white gallery where one real product surface is the exhibit, under a seven-layer shadow.

It is generated from the pack, not authored beside it: `src/styles.css` opens
with `styles/tokens/showroom.css` byte for byte, and the rules the design agent
must obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
