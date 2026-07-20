---
name: sheleg-design
description: Use when building or upgrading a cinematic scroll-driven landing page, marketing site, or hero experience — a particle/WebGL background, scroll-linked animation, parallax, pinned or scrubbed sections, formation-morphing scenes — or when such a page feels busy or janky, or its motion layers drift out of sync. RU triggers - кинематографичный лендинг, скролл-анимация, лендинг с частицами. Pairs with an existing visual system, does not replace one.
---

# SHELEG Design

## Overview

A page feels cinematic not from many animations, but from a **single source of
truth** (measured scroll position) driving **many cheap, layered,
independently-degradable responses**. Centralize scroll into one store; layers
read it per frame and react in their own language. Nothing crossfades — things
*redeploy*. Every layer degrades to a calm static state.

**REQUIRED REFERENCE:** read [`SHELEG_DESIGN.md`](./SHELEG_DESIGN.md) (same
directory) before implementing — it holds the architecture, exact morph math,
the DOM↔WebGL bridge, the build recipe (§11), and the file map.

## When to Use

- Landing/marketing/hero pages where motion is a stated goal
- Particle or WebGL backgrounds tied to scroll; scenes that morph per section
- Scroll-linked charts, step flows, progress rails, parallax
- Existing scroll site that feels nervous, janky, or out of phase

**Not for (the motion layer):** docs, dashboards, static content sites — or
any page whose visual system or copy isn't finished yet. For dashboards,
tools, and product UI, use the [`workbench`](./styles/workbench.md) style
pack standalone: its tokens and atoms apply without the cinematic motion
layer.

## Core Pattern — five principles, in order

1. **One clock.** All motion derives from one measured scroll state; no layer
   measures scroll itself, so layers can never drift out of phase.
2. **Read per frame, notify rarely.** Hot consumers (WebGL/canvas/rail) read
   the store imperatively, zero framework renders; only coarse act/section
   changes notify the framework.
3. **Hold, then redeploy.** Hold a formation ~80% of a section, then morph in a
   short, phase-staggered, arc-curved wave. Crossfades are banned.
4. **Earned motion.** Scrub only for instruments that narrate state over time;
   hover/entrance motion stays sub-500ms and never gates content.
5. **Degrade to calm.** Reduced-motion / coarse pointer / no-WebGL collapse to
   a static, fully-legible page. The effect is a bonus, never a dependency.

## Style packs

The motion methodology is style-agnostic; the visual identity comes from a
style pack in [`styles/`](./styles/):

| Pack | Look | Choose for |
|---|---|---|
| [`instrument-console`](./styles/instrument-console.md) | near-black aerospace console, one electric-blue signal, mono telemetry | technical / systems / infra products |
| [`editorial-luxury`](./styles/editorial-luxury.md) | warm cream + espresso ink, sage accent, Fraunces/Newsreader, dossier motifs | editorial / research / premium B2B |
| [`workbench`](./styles/workbench.md) | quiet light/dark product UI: neutral grays, borders as elevation, one blue accent, mono data | dashboards / admin / internal & dev tools (standalone — no cinematic motion) |

Read the chosen pack in full before styling anything — it supplies the
palette, type, texture, motion-token values, signature motifs, and bans.
For a new style, author a new pack file with the same headings (Register /
Palette / Type / Texture & surface / Motion tokens / Signature motifs /
Micro-interactions / Bans); never invent token values ad hoc.

## How to Apply

1. Visual system first: pick (or author) a style pack, apply its tokens as
   the site-wide design tokens (color, type, spacing, components).
2. Build bottom-up in the §11 layer order: scroll clock → smooth scroll →
   particle field → 2D fallback → DOM choreography → reveals → scrubbed
   instruments → optional DOM↔WebGL bridge. One small file per layer.
3. Storyboard in data: a `SCENES` registry (`{ anchor, formation, focusX,
   energy }` per section); iterate on the data before touching render loops.
4. Ship each layer's reduced-motion/fallback branch in the same commit.
5. Verify: typecheck/lint/build; screenshot each scene mid-hold and mid-morph;
   reduced-motion pass; narrow-viewport pass.

## Quick Reference

| Rule | Prevents |
|---|---|
| One scroll store, two read paths (live getter + coarse subscription) | layers drifting out of phase; render storms |
| Long hold, short smoothstepped morph tail | nervous, constantly-moving page |
| Per-point phase-staggered, perpendicular-arc migration | "screensaver" particle look |
| Smooth scroll driven from the animation library's ticker | scrub and field on different inertia |
| Lazy-load GSAP/WebGL; mount WebGL one frame after hydration | heavy initial bundle, hydration jank |
| One ease + tiny duration/stagger token set site-wide | motion reading as many systems, not one |
| Scrubbed SVG: `ease: 'none'`, `pathLength={1}`, kill timelines on cleanup | easing fighting scrub; leaked triggers |
| Animate only `transform`/`opacity` | layout thrash |

## Common Mistakes

- Paying the fallback/a11y tax "at the end" → it never ships. Same commit.
- Parallax on everything → nausea. At most one drifting figure per viewport.
- Scrub on hero/entrances → motion feels unearned; reserve scrub for
  instruments.
