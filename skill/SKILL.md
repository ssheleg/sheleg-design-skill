---
name: sheleg-design
description: Use when building or upgrading a cinematic, scroll-driven landing page, marketing site, or hero experience — especially one with a particle/WebGL background, scroll-linked animation, parallax, pinned/scrubbed sections, or formation-changing motion. SHELEG Design is a motion + systems methodology: one scroll "clock" drives many cheap, layered, independently-degradable responses (a particle field, a 2D fallback, attention dimming, parallax, scrubbed instruments, a progress rail) so the page reads as a single precision instrument. Read this before designing the motion architecture of such a site; it pairs with a visual system, not replaces one.
---

# SHELEG Design

A methodology for landing pages that feel *alive* without feeling busy. Full
reference (architecture, code-level mechanics, build-from-scratch recipe, file
map, and the deeper "why") lives in [`SHELEG_DESIGN.md`](./SHELEG_DESIGN.md) next
to this file — read it before implementing.

## The thesis

A page feels cinematic not from many animations, but from a **single source of
truth** (scroll position) driving **many cheap, layered responses** that are
individually quiet and collectively rich. Centralize scroll into one external
store; let independent layers read it per frame and react in their own language.
Nothing crossfades — things *redeploy*. Every layer degrades to a calm static
state.

## The five principles (apply in order)

1. **One clock.** All motion derives from one measured scroll state. Layers never
   measure scroll independently, so they can never drift out of phase.
2. **Read per frame, notify rarely.** Hot consumers (WebGL/canvas/rail) read the
   store imperatively each frame and cause zero React renders. Only coarse,
   human-visible changes (the current "act"/section) notify the framework.
3. **Hold, then redeploy.** Hold a formation steady for ~80% of a section, then
   morph in a short, phase-staggered, arc-curved wave. Ban crossfades.
4. **Earned motion.** Scrub belongs to instruments that narrate state over time
   (charts, step flows). Hover/entrance motion stays sub-500ms and never gates
   content visibility.
5. **Degrade to calm.** `prefers-reduced-motion` / coarse pointer / no-WebGL all
   collapse to a static, fully-legible page. The effect is a bonus, never a
   dependency.

## How to use this skill

When asked to build or upgrade such a site:

1. **Lay the visual system first** (color, type, spacing, components). Motion on
   top of a weak visual system amplifies the weakness. SHELEG Design is the
   motion layer — it assumes a visual foundation exists.
2. **Build bottom-up following the layer order** in `SHELEG_DESIGN.md` §11:
   the scroll clock → smooth scroll → particle field → 2D fallback → DOM
   choreography → reveal primitives → scrubbed instruments → (optional) DOM↔WebGL
   bridge. Each layer is a small, single-responsibility file reading the one clock.
3. **Storyboard in data.** Express the narrative as a `SCENES` registry (one
   `{ anchor, formation, focusX, energy }` per section). Iterate on the data
   before touching render loops.
4. **Pay the fallback + a11y tax in the same commit** as each layer, never at the
   end. Every animated component ships its reduced-motion branch immediately.
5. **Verify** with typecheck/lint/build, screenshots of each scene mid-hold and
   mid-morph, a reduced-motion pass, and a narrow-viewport pass.

## Non-negotiables (each prevents a real failure mode)

- Centralize scroll in ONE store with two read paths: a live getter for
  per-frame readers and a coarse subscription for framework-rendered UI.
- Hold-then-morph (long hold, short smoothstepped tail) — constant morphing
  reads as nervous; this is the single biggest "calm" lever.
- Redeploy with a per-point phase-staggered, perpendicular-arc migration — this
  is what makes a particle field read as premium rather than a screensaver.
- Drive smooth scroll (e.g. Lenis) from the animation library's ticker so
  scrubbed instruments and the particle field share one inertia.
- Lazy-load heavy libs (GSAP/WebGL) out of the initial bundle; WebGL mounts one
  frame after hydration paints.
- One ease + a tiny duration/stagger token set for the whole site; no component
  invents its own curve.
- For scrubbed SVG: `ease: 'none'`, `pathLength={1}` to normalize paths, and
  always kill timelines + triggers on cleanup.
- Animate only `transform` and `opacity`; reserve scrub for genuine instruments.

## When NOT to use it

Skip for static content sites, docs, dashboards, or anything where motion is not
a goal. Do not bolt the particle field onto a page whose visual system or copy
isn't finished — fix those first.

---

Read [`SHELEG_DESIGN.md`](./SHELEG_DESIGN.md) for the full architecture, code
mechanics, the exact morph math, the DOM↔WebGL projection bridge, the
build-from-scratch recipe, and the file map.
