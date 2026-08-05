# @sheleg-design/editorial-luxury

The React reference kit for the SHELEG **Editorial Luxury** style pack — a warm
cream field, espresso ink and one sage accent, for research and intelligence
tools, content products and premium B2B.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/editorial-luxury.css` byte for byte, and the rules the design agent
must obey are in [`.design-sync/conventions.md`](./.design-sync/conventions.md) —
starting with the one this pack is most often got wrong, that cream and espresso
are two surfaces on one page and not a light/dark toggle.

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.
