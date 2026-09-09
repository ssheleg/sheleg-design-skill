# Applying the pack — the order of work, and the mistakes that repeat

Split out of `SKILL.md` on 2026-09-10, when its body measured 5703 tokens against the
house budget of 5000. What stays in `SKILL.md` is what DECIDES — the packs, the
calibration, the craft bar, the component layer. What moved here is the procedure that
follows a decision already made, and the failure list to check a finished surface against.

Read this when starting the build, and again before calling a surface done.

## Contents

- [How to apply](#how-to-apply)
- [Common mistakes](#common-mistakes)

## How to apply


1. Visual system first: pick (or author) a style pack, apply its tokens as
   the site-wide design tokens (color, type, spacing, components). If Lazyweb
   MCP is available, sweep references for the target screen at this point —
   before any layout exists to defend.
2. Build bottom-up in the §11 layer order: scroll clock → smooth scroll →
   particle field → 2D fallback → DOM choreography → reveals → scrubbed
   instruments → optional DOM↔WebGL bridge. One small file per layer.
3. Storyboard in data: a `SCENES` registry (`{ anchor, formation, focusX,
   energy }` per section); iterate on the data before touching render loops.
4. Ship each layer's reduced-motion/fallback branch in the same commit.
5. Verify: typecheck/lint/build; screenshot each scene mid-hold and mid-morph;
   reduced-motion pass; narrow-viewport pass.

## Common mistakes


- Paying the fallback/a11y tax "at the end" → it never ships. Same commit.
- Parallax on everything → nausea. At most one drifting figure per viewport.
- Scrub on hero/entrances → motion feels unearned; reserve scrub for
  instruments.
