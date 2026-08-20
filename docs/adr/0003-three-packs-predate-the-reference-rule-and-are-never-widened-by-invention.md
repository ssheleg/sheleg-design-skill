# ADR 0003 — three packs predate the reference rule, and none of them is ever widened by invention

**Date** 2026-08-20
**Status** accepted
**Board rows** B-001 (widen the three packs), B-002 (record the grandfather clause)

## The rule they predate

Standing instruction 5 of this repository's retrospective says **no reference, no pack**: a
style pack states values read off something addressable, so a reader can check the pack
against its source. It exists because the alternative is a pack that reads like a
measurement and is a preference.

Three shipped packs predate it, and their `Origin:` lines name a product rather than an
address:

| pack | `Origin:` says |
|---|---|
| `instrument-console` | *Nicegram Business OS landing (the SHELEG reference implementation)* |
| `workbench` | *the Builder Pro AI production design system (light+dark token …)* |
| `briefing-room` | *a production investor-deck site (2026); every value below was read off …* |

Each names a real thing that was really read. None of them names a URL, a commit or a file
a reader can open. **Nothing in the library said so to a reader**, which is the part this
record fixes: an exception nobody wrote down is indistinguishable from a rule nobody
follows.

## The decision

**They stay. They stay on the `core` contract. And they are never widened by invention.**

B-001 asked for the three to be widened to `## Components`, `## Hero`, `## Responsive` and
`## Signature element`. That row offered three ways out, and this is the third: **do not**.
Widening means stating per-component states, an opening viewport and its line ceiling,
collapse rules and a signature element — thirty-odd values that would have to come from
somewhere. With no addressable source they would come from taste, wearing the authority of
a measurement taken off a product. A pack that invents its widened sections is worse than a
pack that declines them, because the reader cannot tell which is which.

So the boundary is drawn where the evidence ends. What each of the three states was read off
its product and is binding. What it declines is **named in the pack's own contract line**,
and since 2026-08-20 a guard requires that: `Contract: core` must enumerate what it leaves
to the implementer. `awning` shipped a bare `Contract: core` and was caught by that guard on
its first run — a narrow pack and an unfinished pack look identical until the declination is
written down.

## What would change this

An addressable reference for any of the three — a public URL, a committed screenshot set,
a token file in a repository — and that pack may be widened **from it**, in one change, with
the `Origin:` line rewritten to the address. Until then the answer to *"why are these three
narrower?"* is this file rather than a guess.

## What this decision costs

A consumer picking `instrument-console` for a product surface gets less than one picking
`datasheet`: they decide the component states themselves. `SKILL.md`'s pack table says so at
the point of choice, which is the only place the cost can be paid honestly.

And it costs the library its symmetry. Seven of twenty-nine packs are `core` and twenty-two
are `widened`, and that split is now a stated fact with a reason rather than an accident of
which pack somebody had time for.
