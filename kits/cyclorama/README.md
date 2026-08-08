# @sheleg-design/cyclorama

The React reference kit for the SHELEG **Cyclorama** style pack — a pale field
that breathes through six pastel stops on a 32-second loop under near-black ink
that never moves with it, a monospaced typewriter serif over mono, one orange
used only as a fill, and no shadows anywhere.

It is generated from the pack, not authored beside it: `src/styles.css` opens
with `styles/tokens/cyclorama.css` byte for byte, and the rules the design agent
must obey are in
[`.design-sync/conventions.md`](./.design-sync/conventions.md).

**The cycle is not in this kit, and that is deliberate.** A kit is the static
half of a pack; motion stays behind in the pack. What crosses is `FieldStop` —
the six stops as six surfaces — which is the more useful thing to design against
anyway: a screen proved on stop 2 and stop 5 is proved on every frame between.

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
