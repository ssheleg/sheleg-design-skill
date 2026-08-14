# @sheleg-design/tenor

The React reference kit for the SHELEG **Tenor** style pack — warm paper with zero radius
and zero shadow, a single hairline weight assembling every lattice, and one orange that
exists only on hover and on focus, so the page screenshots with no colour in it at all.

It is generated from the pack, not authored beside it: `src/styles.css` opens with
`styles/tokens/tenor.css` byte for byte, and the rules the design agent must obey are in
[`.design-sync/conventions.md`](./.design-sync/conventions.md).

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
| `Staircase` | four rows descending to the right, each 3% narrower and a step darker — the **signature element**, and its prop type is a four-tuple so the ramp cannot grow a fifth rung |
| `SplitHeadline` | one sentence in two clauses and two values: the premise muted, the claim in ink |
| `Lattice` + `LatticeCell` | the hairline grid, assembled per cell so a cell can go solid on hover with no seam |
| `FilmFrame` | product proof as a silent looping recording in a 1px rectangle, with a required accessible name |
| `Guardrail` | the status primitive, and the proof that severity here is value rather than hue |
| `Eyebrow` | the mono micro-label, a `<p>` on purpose so it does not become a second heading |

## Surface

There is no dark theme. `[data-surface="dark"]` inverts a **section** inside a paper
page — the reference uses it for one grid and the footer — and both blocks are declared in
the token layer at the top of `src/styles.css`.

## What is not here

The scroll-triggered reveal, the four-step stagger, the ambient greyscale gradient and the
observer that starts and pauses each recording. A kit is the static half of a pack, and
inventing motion to fill that silence is the failure this note exists to prevent —
`FilmFrame` does not call `play()` for exactly that reason.
