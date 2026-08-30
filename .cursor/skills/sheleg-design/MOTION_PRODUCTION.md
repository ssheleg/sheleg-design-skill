# Motion production — when motion leaves the page as a file

[`MOTION_DOCTRINE.md`](./MOTION_DOCTRINE.md) decides whether a thing on a page may
move, and how. This document starts one step later, at the only question it does not
answer: **what happens when the motion has to become a file** — a launch video, a
feature loop, a social cut, an OG card that moves, a changelog clip, a deck that
plays.

That is a different medium with different physics, and treating it as "the same
animation, exported" is the mistake this document exists to prevent.

## The boundary

| The motion is… | It belongs to | Read |
|---|---|---|
| in the page, driven by scroll, hover, focus or state | the page | `MOTION_DOCTRINE.md`, then `SHELEG_DESIGN.md` |
| in the page, but authored as a timeline and played back | the page | `MOTION_DOCTRINE.md` §6 and §9 still bind |
| a file the page embeds, or a file that never touches the page | **this document** | below |
| a Lottie or a Figma export dropped into the page | the page | `MOTION_DOCTRINE.md` §7 |

**Refusal phrase: "no render."** A brief that says *animate the hero* is page motion
and stays page motion. Reaching for a rendered file there is a downgrade, and the
next section prices it.

## Before the tool: what a rendered asset costs

A video in a hero looks like a shortcut and is a trade. Four things are given up, and
a page should only give them up on purpose.

1. **The reduced-motion contract.** A rendered file has no
   `prefers-reduced-motion`. The doctrine's rule does not stop applying because the
   motion moved into an MP4 — it moves to the **embedding page**, which owes a poster
   frame, `autoplay` withheld under the reduce query, and a control. A hero video that
   autoplays regardless is a doctrine violation wearing a different file extension.
2. **The theme.** A pack's token layer answers a dark surface; a rendered frame cannot.
   Every pack in this library declares `Themes:`, and a video baked against one of them
   is wrong on the other. Either the surface behind it is fixed, or the asset is
   rendered per theme, or the motion stays in the page.
3. **The text.** Type in a rendered frame is not selectable, not translatable, not
   readable by a screen reader and not indexable. A headline that matters is DOM.
4. **The weight and the first frame.** The page's opening viewport now depends on a
   decode. `frontend-performance` owns that number; this document only records that
   the cost exists and lands on LCP.

**What a rendered asset is genuinely for:** a surface you do not control (a social
timeline, an app store, an ad slot, an email), a piece longer than an interaction, a
piece with an audio track, and anything that must look identical on every machine.
That last one is the whole reason both tools below exist.

## The two tools, measured

Both turn code into a deterministic MP4 by seeking a headless browser frame by frame
and encoding the result. They differ in the language the composition is written in and
in what using them costs. Read on 2026-08-30; version numbers and prices move, so
re-read before quoting them.

| | **Remotion** | **HyperFrames** |
|---|---|---|
| The composition is | a React component reading `useCurrentFrame()` | an HTML document with `data-start` / `data-duration` timing attributes and a seekable animation runtime |
| Licence | its own two-tier licence, **not** an OSI one | **Apache-2.0** |
| Free for | individuals, for-profit organizations **with up to 3 employees**, non-profits, and evaluation | everyone |
| Paid when | a for-profit organization exceeds that size — Company License, read the current price from the vendor | never for the framework; the vendor's managed cloud render is a separate product |
| First release | 2020 | 2026 |
| Version on npm at the reading | `remotion` 4.0.518 | `hyperframes` 0.8.20 — **pre-1.0** |
| FFmpeg | bundled since v4.0; no separate install | **required separately**, plus Node 22+ |
| In-page playback | `@remotion/player`, a React component that takes props | `@hyperframes/player`, a web component that loads the composition in an **isolated iframe** |
| Distributed rendering | AWS Lambda, Node SSR, Vercel, Cloud Run | AWS Lambda, Google Cloud Run, the vendor's managed cloud |
| Agent surface | a skill set plus a documentation MCP | 20 skills behind one `/hyperframes` router, and a `/remotion-to-hyperframes` porting skill |

Two asymmetries decide most briefs, and they point in opposite directions.

- **Licence.** A studio of four people must pay to use Remotion commercially and may
  use HyperFrames without asking anyone. There is no reading of the Remotion licence
  under which a 4-person for-profit is free; the threshold is written into it.
- **Maturity.** Remotion is on 4.0.518 after six years. HyperFrames has not shipped a
  1.0. Everything below that number is allowed to move, and a composition written
  today may need editing after a minor bump. That risk is real and is not cancelled by
  the licence being friendlier.

## The recommendation, and the three conditions that reverse it

**Default to HyperFrames** for the work this skill is about — a designed page that
occasionally needs a rendered motion asset. Three reasons, in order of weight:

1. **The composition is written in the language the pack already speaks.** A pack's
   `styles/tokens/<pack>.css` is a `:root` block of custom properties. In HyperFrames
   it is `<link>`ed into the composition **unmodified** — the same file the site ships,
   byte for byte, which is exactly the rule the kits already follow. In Remotion the
   composition is React, and the token layer becomes a stylesheet imported into a
   component tree: workable, and one translation step where a value can drift. This
   library's entire position is that a token layer is copied and never transcribed, and
   one of the two tools lets that hold across the render seam.
2. **The licence removes a question that has nothing to do with design.** Apache-2.0
   over a seat count.
3. **The determinism rules are the doctrine's rules.** No wall clock, no unseeded
   randomness, no fetch mid-frame, a locked output size, a finite length — the same
   discipline `MOTION_DOCTRINE.md` §8 already demands of a page, restated for a
   renderer. An author who has followed the doctrine has already followed this.

**Reach for Remotion instead when any one of these is true.**

- **The motion must be driven by application state in the page.** `@remotion/player` is
  a React component: props go in, the composition re-renders, the page owns it. The
  HyperFrames player is an iframe by design, which is excellent isolation and a wall
  between your state and the timeline. A configurator, a live preview of a
  user's edit, a chart the visitor drives — Remotion.
- **The product is a video pipeline, not a page.** Prompt-to-video, per-customer
  renders, template farms at volume. Remotion has six years of Lambda operations behind
  it and a price per render, which is a business model rather than an obstacle.
- **The team cannot carry a pre-1.0 dependency.** If a broken minor bump is a real cost
  — a long-lived pipeline, a regulated client, a repository nobody will revisit for a
  year — take the mature one and pay for it.

**A brief that hits none of those and the licence threshold is not close** — one
person, one landing page, one launch clip — can use either, and the tie-break is which
one the operator already knows. Say so rather than manufacturing a reason.

## The token seam

Whatever the tool, the rule is the library's existing one and it does not relax:
**a pack's token layer is copied, never transcribed**, and no colour literal appears
outside it. The seam differs only in mechanism.

**HyperFrames.** The composition is a document, so the token layer is a stylesheet:

```html
<head>
  <link rel="stylesheet" href="./tokens/<pack>.css" />
</head>
<div data-composition-id="launch" data-width="1920" data-height="1080">
  <h1 class="clip" data-start="0.4" data-duration="4">…</h1>
</div>
```

Everything after that consumes `var(--…)`, exactly as a kit does.

**Remotion.** Import the same file once at the composition root and consume the same
custom properties from `style` objects or CSS modules. Do **not** rebuild the palette
as a TypeScript object: two homes for one colour is the defect the DOCMAP's
single-home rule exists to prevent, and it is invisible until the site and the video
disagree in a screenshot.

Three token families need a decision the page never forced:

- **Durations.** A pack's `--dur-*` are page clocks in seconds. A renderer thinks in
  frames. Convert at the edge — `frames = seconds × fps` — and keep the token as the
  source. A duration typed twice is a duration that will drift.
- **The reduced-motion branch.** Every token layer in this library carries one. It
  **does not fire in a render**, because a renderer has no user preference. See below.
- **Type.** A rendered frame has no font fallback worth the name: if the face has not
  loaded before frame 0, the frame is wrong and stays wrong. Both tools require every
  asset resolved before the first frame; a webfont is an asset.

## Reduced motion, on the other side of the render

This is the part neither tool does for you, and it is the doctrine's clause that most
often gets dropped at this seam.

- A rendered file **has no reduced-motion state**. The `@media (prefers-reduced-motion:
  reduce)` block in the pack's token layer collapses nothing during a render, and that
  is correct — there is no user there.
- Therefore the obligation moves **to the page that embeds the file**, and it is
  concrete: no `autoplay` under the reduce query, a poster frame that is a real frame
  of the piece rather than a title card, a visible control, and no `loop` on anything a
  reader has to read past.
- If the asset exists *only* in a surface you do not control, say so in the pack's or
  the project's notes. An unstated exemption reads as an oversight to the next reader,
  which is how the clause quietly stops being followed.
- **A JavaScript-driven reveal has the same shape and is easier to miss.** A media
  query cannot stop a transform a script sets. Where a composition's motion is scripted,
  the script reads the preference itself. `styles/chorus.md` carries the worked case —
  a reference with zero reduced-motion rules and 383 script-set transforms.

## Pre-flight for a rendered asset

Run this before the render, not after. It is the doctrine's §10 with the four items a
file adds.

- [ ] The brief actually wants a file. Page motion was considered and rejected for a
      stated reason.
- [ ] The pack is chosen and its token layer is linked, not retyped.
- [ ] Output size, fps and duration are fixed and written down. Nothing reads a clock.
- [ ] Every asset — fonts, images, audio, video — resolves before frame 0.
- [ ] No `Date.now()`, no `requestAnimationFrame`, no unseeded `Math.random()` anywhere
      in the composition.
- [ ] Durations came from the pack's tokens and were converted once.
- [ ] The theme the asset is baked against is stated, and the surface behind it matches.
- [ ] Any text that carries meaning is either also in the DOM, or its absence is a
      deliberate, recorded choice.
- [ ] The embedding page withholds autoplay under `prefers-reduced-motion: reduce`,
      ships a poster and a control.
- [ ] A byte-identical re-render was produced from the same input. If two runs differ,
      something in the composition is reading the machine — pin the environment
      (a container) before blaming the tool.
