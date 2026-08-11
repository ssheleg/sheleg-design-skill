# @sheleg-design/scoreboard

The React reference kit for the SHELEG **Scoreboard** style pack — warm paper, an
orange that only ever marks, and a ledger of dotted-leader rows whose numbers are
set in an aliased pixel face.

It is generated from the pack, not authored beside it: `src/styles.css` opens
with `styles/tokens/scoreboard.css` byte for byte, and the rules the design agent
must obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
