# Tenor — the design contract

The reference is <https://heytenor.com>, read 2026-08-14 from `/assets/home.css?v=45` —
33,822 bytes of hand-authored CSS, not a compiled utility bundle — plus its two scripts
and the served HTML. The full pack is `styles/tenor.md`; this file is what a design agent
must not get wrong.

## The one thing this pack is

**A management thesis, argued in structure rather than colour.** Warm paper, near-black
ink, one hairline weight, and an orange that only exists on hover and on focus — so the
page screenshots with no colour in it at all. Ranking is done by value: a chip is orange,
grey or black; an argument descends four steps from paper to ink.

## Non-negotiable

- **No border radius. Anywhere.** Zero occurrences in the entire stylesheet. Not on a
  button, a cell, a video frame, a chip or an input.
- **No shadows, and no elevation model at all.** Also zero occurrences. Something is
  either filled or it is not. If a block needs to separate, it gets a hairline.
- **One border weight.** `--line` is ink at 16% and there is no strong variant. A divider
  that reads too quietly is answered with space or a fill, never a heavier line.
- **The accent is a hover state.** At rest the only orange on the page is a 25px lockup
  square. A resting orange fill larger than that is out of register.
- **The orange may never carry a word.** It is 3.02:1 on the paper, and contrast is
  symmetric, so a paper label on an orange fill is the same 3.02:1 — below the large-text
  threshold at any mono size this pack uses. Where a control's label is the only
  statement of what it does, the border takes the accent and the fill stays ink.
- **Severity is value, not hue.** Orange = ask, deep paper = limit, ink = never, and the
  **word** carries the meaning in all three. Status is never by colour alone here.
- **The sans is weight 400 and only 400.** Instrument Sans is loaded across two variable
  axes and used at exactly one point. Emphasis comes from size, measure and fill.
- **Tracking runs in opposite directions.** The sans tracks negative and tightens as it
  grows, to `-0.065em` on the hero; the mono tracks positive and opens as it shrinks, to
  `0.12em` on the smallest label. Nothing crosses.
- **Line-height goes below one and the measure is set in `ch`** — 0.91 at 12ch on the
  hero, 0.93 at 8-9.5ch on a section head. That narrow measure is what turns every
  heading into a stack, which is the shape the page is recognised by.
- **The lattice is assembled per cell.** The container draws top and left; each cell draws
  right and bottom. That is what lets a cell go solid on hover with no seam along its own
  border. Never `border-collapse`, never a background grid.
- **Product proof is a silent looping recording**, in a 16:9 box with a 1px hairline —
  not a screenshot, not an illustration, and never inside a browser chrome frame.
- **Reduced motion collapses every duration to zero.** The page keeps every value it was
  showing.

## What this kit is not

It is the **static half** of the pack. The scroll-triggered reveal, the four-step stagger,
the ambient greyscale gradient and the observer that starts and pauses each recording are
page-level motion and do not cross into a component library. `FilmFrame` deliberately does
not start playback: the page owns that policy, not the component.

## The traps the reference itself carries

Six, so a design agent does not reproduce them from a screenshot:

1. `--ink-soft` is **4.16:1** on the paper and carries every lead paragraph at 16px — short
   of AA by a margin no one notices and every audit finds.
2. `--ink-faint` is **2.36:1** and carries the hero's grey clause, below even the 3:1 that
   large text is allowed.
3. Both of the reference's orange-filled elements put a label on the orange below the
   large-text threshold — including every CTA at the moment it is hovered.
4. Instrument Sans is requested across `wdth 75..100, wght 400..600` and used at weight
   400, default width. The rest is downloaded and never touched.
5. The mobile panel is sized with the pre-`dvh` viewport unit and upgraded inside
   `@supports`, so it jumps on every browser without the upgrade.
6. The staircase's two middle rungs are pure neutrals between a warm paper and a warm ink,
   so they read faintly cool against their own field. Kept as measured; warm them
   deliberately or accept the step and say so.
