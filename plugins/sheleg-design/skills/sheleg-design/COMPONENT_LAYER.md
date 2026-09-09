# The component layer — how a kit composes with a pack

Split out of `SKILL.md` on 2026-09-10, when its body measured 5703 tokens against the
house budget of 5000. The DECISION stays in `SKILL.md` — the default is `shadcn/ui`,
asked once per project, recorded where the pack is recorded, and it does not apply to a
cinematic scroll surface. What moved here is the MECHANICS: why a kit composes with a
token layer rather than competing with it, the two vocabularies that must be mapped, the
six axes of the adapter contract, and who does the work.

Read this when mounting a kit against a pack, or when a mounted kit still looks like its
starter theme.

## Contents

- [Why it composes rather than competes](#why-it-composes-rather-than-competes)
- [The two vocabularies, and the adapter contract](#the-two-vocabularies-and-the-adapter-contract)

## Why it composes rather than competes

`shadcn/ui` is not a theme, but it is
NOT unstyled either — its docs ship "Beautiful Defaults" (styled, opinionated
components you copy INTO your repo and edit), built on HEADLESS primitives
(Radix/Base), themed through CSS custom properties (https://ui.shadcn.com/docs,
checked 2026-09-09). So it arrives with a look and *consumes* a token layer to
change it. That is the seam a pack is: the pack decides the tokens, the kit
decides what a `DropdownMenu` is — and because the components are yours to edit,
a custom component edit is a normal adaptation, NOT automatically a redesign.

## The two vocabularies, and the adapter contract

The packs resolve
`--bg` and `--ink` everywhere and little else by that name; `shadcn/ui` expects
`--background`, `--foreground`, `--primary`, `--muted` and the rest of its own
contract. **Map them explicitly in the pack's token file** — an undefined custom
property does not error, it silently falls back, which is the same failure the
chart rule above exists for. And color is only ONE axis of the adapter contract:
semantic **color + geometry + density + typography + elevation + state/anatomy**.
A kit mounted with only the color vars remapped keeps shadcn's default radius,
padding, shadows and type — so after the token remap **compare the RENDERED
component matrix (Card/Button/Dialog: computed sizes, padding, radius, shadow,
fonts, states) against the chosen direction**, not just the color variables, and
list the defaults you deliberately kept. A kit mounted without any of that
renders in its starter look and looks like nobody chose anything.
