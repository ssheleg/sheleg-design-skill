# @sheleg-design/paperclip

The React reference kit for the SHELEG **Paperclip** style pack — a neutral coal field
with no functional colour at all, every control monochrome, elevation made of hairlines,
and the whole chromatic budget spent on one curtain of gradient capsules that cannot be
clicked.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/paperclip.css` byte for byte, and the rules the design agent must obey are
in [`.design-sync/conventions.md`](./.design-sync/conventions.md).

```bash
npm install && npm run build
```

Then run `/design-sync` in Claude Code from this directory to push it to
claude.ai/design.

## The spine, and this pack's seven

`Button`, `Card`, `Chip`, `Stat`, `Heading` and `Rule` are identical in name, props and
types across every SHELEG kit — switching packs swaps identity, not API.

| Component | What it is |
|---|---|
| `CapsuleCurtain` | 96 gradient capsules from one hue-rotation rule, under a noise mask — the **signature element** |
| `SectionBadge` | a mono uppercase label on one of twelve ramps, each with its own hand-picked ink |
| `HairlineGrid` | the gap *is* the rule: 1px over a border-coloured background, clipped by the container's radius |
| `OrgNode` | a capsule node at 1.5px, whose live state is a word and not only a ring |
| `LedgerRow` | a spend row in tabular figures whose bar is white and animates `scaleX`, never `width` |
| `ScheduleLane` | a swimlane whose ticks are 10 × 20 capsules and whose active tick says what it is doing |
| `Terminal` | the only warm surface in the pack, with a concentric tab group machined into its bar |

## Container queries, not viewport queries

`HairlineGrid`, `OrgNode`, `LedgerRow` and `ScheduleLane` each take
`container-type: inline-size` and collapse against **their own width**. A three-across
grid dropped into a 320px sidebar on a 1440px screen keeps its columns and overflows
otherwise — which is the bug a kit's viewport query always becomes.

## Two themes, one token layer

Dark is the default; `data-theme="light"` is the twin. The dark border token is *alpha*
(`#ffffff1a`), so the same hairline reads correctly over the field, over `--surface` and
over the warm terminal without being restated. In light there is no surface step at all —
`--bg` and `--surface` are the same white — and that is the theme's whole idea.
