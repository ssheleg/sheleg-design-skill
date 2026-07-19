# SHELEG Design

A motion-and-particle interface system, reverse-engineered from the Nicegram
Business OS landing page. This document captures *how* the page reaches its
level — the layout discipline, the scroll narrative, the WebGL particle field,
the DOM choreography, and the registration tricks that fuse them — so you can
build new sites on the same principles and understand *why* each piece works.

> SHELEG Design is the **motion + systems** layer. It assumes a **visual**
> system already exists (color, type, elevation, components — the reference
> implementation calls its visual layer "The Instrument Console": a near-black
> aerospace console with one electric-blue signal accent). Build the visual
> system first; layer SHELEG Design on top.

---

## 0. The one-paragraph thesis

A landing page feels "alive" not because it has many animations, but because a
**single source of truth** (scroll position) drives **many cheap, layered
responses** that are individually quiet and collectively cinematic. SHELEG
Design centralizes scroll into one external store, then lets independent layers
(a WebGL particle field, a DOM spotlight, parallax figures, scrubbed
instruments, a progress rail) read that store **per frame** and react in their
own language. Every layer degrades to a calm static state. Nothing crossfades;
things *redeploy*. The result reads as one instrument responding to your hand,
not a pile of effects.

The five principles that make it work:

1. **One clock.** All motion derives from a single measured scroll state. Layers
   never measure scroll independently, so they can never disagree.
2. **Read per frame, notify rarely.** Hot consumers (WebGL, canvas, rail) read
   the store imperatively each frame and never trigger React renders. Only
   coarse, human-visible changes (the current "act") notify React.
3. **Hold, then redeploy.** A formation is held steady for most of a section,
   then morphs in a short, phase-staggered, arc-curved wave — points fly to new
   posts. Crossfades are banned.
4. **Earned motion.** Scrubbed animation belongs to instruments that narrate
   state over time. Hover/entrance motion is sub-500ms and never gates content.
5. **Degrade to calm.** `prefers-reduced-motion` / coarse pointer / no-WebGL all
   collapse to a static, fully-legible page. The effect is an enhancement, never
   a dependency.

---

## 1. Architecture at a glance

```
                         ┌─────────────────────────────┐
   wheel / touch  ─────▶ │  Lenis smooth scroll         │  (SmoothScroll.tsx)
                         │  driven by the GSAP ticker    │
                         └──────────────┬───────────────┘
                                        │ one scroll position / frame
                                        ▼
                         ┌─────────────────────────────┐
                         │  Scroll store (single clock) │  (scroll-progress.ts)
                         │  global · act · form · focusX │
                         │  velocity · finale            │
                         └──────────────┬───────────────┘
            per-frame reads (no React)  │  coarse "act" change → React
        ┌───────────────┬───────────────┼───────────────┬──────────────┐
        ▼               ▼               ▼               ▼              ▼
   SignalField     SignalMesh      FocalSpotlight   ParallaxDrift   ScrollRail
   (WebGL field)   (2D fallback)   (dim off-band)   (figure depth)  (progress)
        │
        │ projects anchor points / reads chart progress
        ▼
   field-sync bridge ──▶ ConstellationOverlay (SVG drawn over clusters)
                    ◀── WhyNowChart scrub (particles assemble with the line)
```

Layers are **independent**. You can delete `ParallaxDrift` or the overlay and
everything else still works. That decoupling is the point: each layer is a small
file with one responsibility, reading the same clock.

---

## 2. Layer 1 — The scroll store (the single clock)

**File:** `src/lib/motion/scroll-progress.ts`

This is the heart of the system. One `requestAnimationFrame` loop (scheduled on
the native `scroll` event) measures the page and writes a plain `state` object.
Everything else reads it.

### The dual-subscription pattern

The store exposes two read paths, which is what keeps it cheap:

- `getScrollState()` — returns the **live, mutable** object. Hot per-frame
  consumers (WebGL `useFrame`, the canvas loop, the rail fill) read this and
  never cause a React render.
- `subscribeAct()` + `useSyncExternalStore` — fires **only when the integer act
  changes** (5 acts on the whole page). React components that show act-derived
  UI (nav badge, rail markers) subscribe here, so they wake up a handful of
  times per full scroll, not 60×/second.

```ts
// Per-frame, no React (rail fill, WebGL, canvas):
const s = getScrollState();
el.style.transform = `scaleY(${s.global})`;

// Coarse, React-driven (nav badge "02 / CONTROL"):
const act = useSyncExternalStore(subscribeAct, () => getScrollState().act, () => 0);
```

> **Why it works:** the expensive consumers are exactly the ones that must run
> every frame anyway (rendering), so reading a mutable object is free. The cheap
> consumers (text labels) are the only ones in React's render path, and they
> change rarely. You get 60fps motion with almost no React churn.

### What the state carries

| Field | Range | Meaning | Who reads it |
|---|---|---|---|
| `global` | 0..1 | whole-page scroll progress | rail fill, camera dolly |
| `act` | 0..4 | current narrative act (integer) | nav badge, rail markers |
| `actProgress` | 0..1 | progress within the act | act-level copy |
| `field` | 0..4 | continuous act scalar | 2D mesh gain, climax |
| `scene` | 0..13 | current section's scene (integer) | scene lookup |
| `form` | 0..13 | **continuous scene scalar** | particle formation morph |
| `focusX` | -1..1 | camera pan target | WebGL camera, overlay |
| `velocity` | -1..1 | smoothed scroll speed | field breathing, rail |
| `finale` | 0..1 | post-waitlist epilogue progress | N charge → burst |
| `bias` | -0.6..1 | interactive nudge added to `form` | section gestures |

### The "hold then morph" measurement (the calm secret)

A naïve scroll-to-formation mapping changes the backdrop continuously, which
reads as nervous. The fix is a **hold window**. Within a scene's scroll span,
`form` stays pinned to the scene's integer for the first `HOLD` (82%), then
eases through the tail via smoothstep:

```ts
const sp   = spanProgress(y, sceneFrom, sceneTo);   // 0..1 within the scene
const HOLD = 0.82;                                   // formation locked 82% of the span
const tail = clamp01((sp - HOLD) / (1 - HOLD));      // 0..1 only in the last 18%
const eased = tail * tail * (3 - 2 * tail);          // smoothstep
state.form  = scene + eased;                         // integer hold → eased morph at the seam
```

Boundaries are measured when a section crosses **65% of the viewport** (`measure()`),
so a formation "opens" as its section becomes the reading focus. A
`ResizeObserver` on `document.body` re-measures when late layout (fonts, lazy
GSAP pin spacers) shifts the page — without it, every boundary below a pinned
section would be wrong.

### Velocity as a feeling, not a value

`setScrollVelocity()` is written from Lenis on every scroll event and normalized
to roughly -1..1. It **does not notify React** — it is read per frame by the
field (particles breathe faster while you scroll) and the rail (fill brightens
with input speed). This is the cheapest possible "the instrument is responding
to you" signal.

---

## 3. Layer 2 — Smooth scroll (one position per frame)

**File:** `src/components/motion/SmoothScroll.tsx`

Lenis provides inertial scrolling, but the important move is **driving Lenis
from the GSAP ticker** rather than its own rAF:

```ts
const lenis = new Lenis({ lerp: 0.09, wheelMultiplier: 1, touchMultiplier: 1.4 });
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
lenis.on("scroll", (e) => { setScrollVelocity(e.velocity); ScrollTrigger.update(); });
```

> **Why it works:** ScrollTrigger scrubs and the particle field both read scroll
> on the same tick, so a scrubbed chart and the background particles share one
> inertia — they move as a single instrument. A low `lerp` (0.09) means more
> glide between wheel notches, which is what lets formations morph as continuous
> motion instead of discrete jumps.

Reduced-motion / coarse-pointer clients skip Lenis entirely (`shouldReduceScenes()`)
and keep native scroll. The store still runs, so the rail and nav stay in sync.

---

## 4. Layer 3 — The particle field (the scene-formation engine)

**File:** `src/components/webgl/SignalField.tsx`

This is the showpiece: ~936 points (`24 × 13 × 3`) that narrate the page section
by section. It is a single `THREE.Points` cloud whose target positions change
per scene. All motion is CPU positional lerp — cheap, deterministic, tinted only
with the brand accent.

### 4.1 The scene registry

**File:** `src/lib/motion/scenes.ts`

Each section "owns" a scene; a scene is a `{ anchor, formation, focusX, energy }`
record. The registry is the single place that maps DOM sections to particle
behavior:

```ts
export const SCENES = [
  { anchor: "top",       formation: "frame",         focusX: -0.3,  energy: 0.5  },
  { anchor: "telemetry", formation: "curve",         focusX: 0,     energy: 0.45 },
  { anchor: "problem",   formation: "turbulence",    focusX: -0.25, energy: 0.55 },
  // … one per section …
  { anchor: "why-now",   formation: "gapCurve",      focusX: 0,     energy: 0.7  },
  { anchor: "waitlist",  formation: "glyphN",        focusX: 0,     energy: 1    },
] as const;
```

- `formation` — which shape the points fly into (frame, curve, lattice, triad,
  orbit, constellation, ecoMap, gapCurve, glyphN, …).
- `focusX` — where the camera pans (opposite the content column, so the field
  frames the text instead of fighting it).
- `energy` — the brightness budget for the scene (the **One Signal Rule**: the
  glow never out-shouts an on-stage demo). `sceneEnergy(form)` interpolates it
  continuously.

> **Why it works:** adding/reordering a scene is a one-line data edit. The field,
> the 2D fallback, and the overlay all resolve their behavior **from the registry
> by formation name** (`SCENES.findIndex(s => s.formation === "glyphN")`), so
> nothing hard-codes an index. The data is the choreography.

### 4.2 Formation builders (deterministic geometry)

`buildFormations()` produces each formation's target positions once, at mount.
Every builder runs its **own seeded RNG** (`mulberry32(seed)`), so:

- formations are identical across sessions and machines (no hydration drift),
- they are independent of declaration order,
- the same point index can be given a meaningful role in multiple formations
  (e.g. the "tight N" variant reuses the N's per-point stroke assignment so the
  charge densification reads as the letter pulling itself sharp).

Example — the "constellation" formation pulls a relaxed grid toward 8 hubs with
tight jitter so clusters read as deliberate nodes:

```ts
const pull = 0.68;                       // strong pull → hubs read as clusters
out[ix]   = gx + (hub[0] - gx) * pull + (rand() - 0.5) * 1.1;  // small jitter
out[ix+1] = gy + (hub[1] - gy) * pull + (rand() - 0.5) * 1.1;
```

### 4.3 The morph (hold → smoothstep stagger → arc)

Inside `useFrame`, the render-side scalar `s.form` chases the store's `form` with
**clamped critically-damped smoothing**, so flick-scrolls and anchor jumps sweep
through intermediate formations cinematically instead of teleporting:

```ts
const formDelta = (scroll.form + scroll.bias - s.form) * 0.028;
s.form += Math.max(-0.04, Math.min(0.04, formDelta));   // per-frame delta cap
```

Each point then blends between the two active formations with a **per-point
phase-staggered, smoothstepped** progress — points peel off in a wave and ease
in and out of their posts:

```ts
const m   = clamp01((mix - phaseNorm * spread) / (1 - spread));  // spread = 0.5
const eased = m * m * (3 - 2 * m);                                // smoothstep
```

And mid-flight, points swing **perpendicular to their travel line** — half
clockwise, half counter — so the swarm curls between formations instead of
sliding in straight lines:

```ts
if (m > 0.001 && m < 0.999) {
  const arc = Math.sin(m * Math.PI) * arcAmp * (phase > Math.PI ? 1 : -1);
  px += (-dy / dist) * arc;   // perpendicular offset, peaks mid-transition
  py += ( dx / dist) * arc;
}
```

> **Why it works:** crossfades look like one image fading into another (flat,
> digital). A phase-staggered arc-curved redeploy looks like a *swarm of agents*
> flying to new posts (alive, physical). It is the single biggest reason the
> field reads as premium rather than as a screensaver.

### 4.4 Formation profiles (the glow programs)

A `PROFILES` table gives each formation a render character — how lattice-like it
is (drives wire opacity), which glow program lights it, and how much ambient
drift it keeps:

```ts
const PROFILES = {
  lattice:       { lattice: 1, glow: "wave",  drift: 0.12 },  // engineered grid + wave pulse
  constellation: { lattice: 0, glow: "hubs",  drift: 0.25 },  // hub stars twinkle, no wires
  beam:          { lattice: 0, glow: "beam",  drift: 0.2  },  // focused vertical signal
  glyphN:        { lattice: 0, glow: "glyph", drift: 0.1  },  // the finale "N"
  // …
};
```

Glow programs are blended between the two active formations, so transitions
carry their lighting with them. Profiles are interpolated, never switched hard.

### 4.5 The camera

The camera does three quiet things, all smoothed:

- **Dolly** back as `global` increases (the page pulls away over its length).
- **Pan** toward the active scene's `focusX` (attention follows the content).
- **Tilt** a fraction toward the focus side — applied *after* `lookAt` (which
  resets rotation), from its own smoothed value. This faint instrument tilt is
  what gives the field a sense of being observed through a lens.

### 4.6 The finale (charge → burst), scrub-driven

Past the waitlist, a dedicated `finale` scalar (0..1) drives an epilogue that is
**reversible** because it is pure scrub:

- **Charge** (`finale 0 → 0.55`): the N densifies toward a tight core, scales up,
  and trembles with rising amplitude; brightness and point size climb.
- **Burst** (`finale 0.55 → 0.85`): every point flies out along a precomputed
  radial debris vector with a white-hot flash, then dims into an ember field.
- The DOM **closing line** ("Join Nicegram") fades up from the afterglow.

Because it is gated on the glyph actually holding (`finaleness`) and reads a
scrubbed scalar, scrolling back up rewinds the whole explosion frame-for-frame.

---

## 5. Layer 4 — The 2D fallback (SignalMesh)

**File:** `src/components/atmosphere/SignalMesh.tsx`

Touch and no-WebGL clients get a canvas mesh: two depth layers of grid nodes
with hairline links and traveling pulses, plus **stroke overlays** that fade in
the curve / orbit / N around their scene windows. It reads the **same store**
(`getScrollState().form`, `sceneEnergy`, `finale`), so the escalation and the
finale charge/burst are mirrored — the page tells the same story at lower
fidelity. Only `prefers-reduced-motion` gets a single static frame.

> **Principle:** the fallback is not a stripped logo — it reads the same clock
> and tells the same narrative. That is why switching modes never feels like a
> different website.

---

## 6. Layer 5 — The projection bridge (fusing DOM and WebGL)

**File:** `src/lib/motion/field-sync.ts`

The hardest problem in mixing WebGL particles with DOM labels: the camera moves,
so you cannot hard-code where a cluster appears on screen. The bridge solves it
with a tiny zero-allocation, no-React module that the field writes and the DOM
reads — the same contract as `setScrollVelocity`.

### 6.1 Constellation registration (ecosystem section)

Every frame, `SignalField` projects the constellation's world-space anchors
through its **own camera** and publishes viewport-pixel coordinates + a
visibility alpha:

```ts
// In SignalField useFrame, after all camera moves:
PROJ_SCRATCH.set(anchor.x, anchor.y, -2).project(camera);
setEcoProjection(node,
  (PROJ_SCRATCH.x * 0.5 + 0.5) * size.width,
  (0.5 - PROJ_SCRATCH.y * 0.5) * size.height);
```

`ConstellationOverlay.tsx` (a fixed SVG) reads those points in its own rAF and
positions the constellation lines, the astronomy-chart labels (with leader
ticks), and the rotating "you are here" reticle — perfectly registered over the
particle clusters at any scroll position. CSS `is-live` (toggled at `alpha > 0.5`)
sequences the draw-in: lines stroke themselves, then labels stagger, then the
reticle scales in and spins.

> **Why it works:** the SVG never guesses. It uses the exact projection the GPU
> used that frame, so the "interface drawing the constellation" illusion holds
> through dolly, pan, and tilt. Cost: 4 `Vector3.project` calls per frame ≈ zero.

### 6.2 Chart participation (why-now section)

The reverse direction: the chart's GSAP scrub publishes its draw progress, and
the field assembles its particle copy of the curve left-to-right in lockstep:

```ts
// WhyNowChart timeline:
onUpdate: () => setChartProgress(tl.progress())

// SignalField, per point of the gapCurve formation:
const u = (px + HALF) / (HALF * 2);          // 0..1 along the curve
if (u > chartProg + 0.04) { py -= drop; lum *= 0.5; }   // not yet assembled
else lum += max(0, 1 - |u - chartProg| * 16) * 0.8;     // bright head at the draw front
```

The SVG line and the particles share one scrub and one inertia, so the bright
particle "head" runs exactly where the line tip is being drawn.

---

## 7. Layer 6 — DOM choreography

Three small components, one mechanism each, all reading the same clock.

### FocalSpotlight — `src/components/motion/FocalSpotlight.tsx`
An `IntersectionObserver` with a generous center band (`rootMargin: -22% 0 -22% 0`)
toggles a `data-dim` attribute on sections outside the band. CSS dims them to
62% opacity. The reader's eye is always pulled to the active section. The finale
section is excluded (`:not(#finale)`) because it runs its own fade.

### ParallaxDrift — `src/components/motion/ParallaxDrift.tsx`
Wraps **at most one figure per viewport** in a GSAP `yPercent` scrub for a few
percent of depth drift. Restraint is the rule: parallax on everything is nausea;
parallax on the one hero figure is depth.

### ScrollRail — `src/components/atmosphere/ScrollRail.tsx`
A right-edge hairline whose fill is scaled imperatively (`scaleY(global)`) and
brightened by `velocity` — a live mission timeline, updated per frame with zero
React renders. Act markers deep-link to their anchor sections and use the coarse
`subscribeAct` path for their active state.

---

## 8. Layer 7 — Reveal primitives (act-themed entrances)

**File:** `src/components/design/Reveal.tsx`

Entrances are not generic. Each narrative act has a reveal whose *physics* match
its meaning — this is Disney's "staging" applied to a scroll page:

| Reveal | Physics | Act it serves |
|---|---|---|
| `ScatterReveal` | drifts in off-axis with a blur that resolves | **Problem** — unmanaged things settling into frame |
| `LockReveal` | scales down a hair and snaps into place | **Control** — a part machined into a slot |
| `ClipReveal` | mechanical left-to-right clip wipe | headlines, panels |
| `PulseReveal` | a single soft pulse as it "acquires lock" | **Signal** — the waitlist climax |
| `Stagger` / `StaggerItem` | children cascade with a 0.06s stagger | lists, readouts |

**Every reveal renders its final state plainly under `prefers-reduced-motion`** —
the `useReducedMotion()` branch returns the plain tag. Entrances enhance; they
never gate whether content is visible.

> **Why it works:** when the *kind* of entrance matches the *meaning* of the
> section, motion becomes narration. The page isn't decorated; it's told.

---

## 9. Layer 8 — Scrubbed instruments (GSAP recipe)

Diagrams that narrate state over time (growth chart, comparison table, the
pinned three-step flow, the why-now chart) use one repeatable GSAP recipe.

**Files:** `WhyNowChart.tsx`, `EcosystemDiagram.tsx`, `PinnedSteps.tsx`, `gsap-client.ts`

```ts
useLayoutEffect(() => {
  if (shouldReduceScenes()) return;          // static, fully-drawn fallback
  let teardown;
  loadGsap().then(({ gsap, ScrollTrigger }) => {   // lazy: GSAP never in initial bundle
    const tl = gsap.timeline({
      defaults: { ease: "none" },             // ease: 'none' is mandatory with scrub
      scrollTrigger: { trigger: svg, start: "top 85%", end: "top 25%", scrub: 0.8 },
    });
    tl.fromTo(lines,
      { strokeDasharray: 1, strokeDashoffset: 1 },   // pathLength={1} normalizes every path
      { strokeDashoffset: 0, stagger: 0.08 });        // → one variable draws them all
    teardown = () => { tl.scrollTrigger?.kill(); tl.kill(); };  // ALWAYS kill on cleanup
    ScrollTrigger.refresh();
  });
  return () => teardown?.();
}, []);
```

The non-negotiables (each learned from a real bug here):

- **Lazy-load GSAP** (`loadGsap()`), register the plugin once, keep it out of the
  initial bundle.
- **`ease: 'none'`** on scrubbed tweens — easing fights the scrub.
- **`pathLength={1}`** on SVG paths so a single 0..1 variable can draw any path,
  regardless of its real length.
- **Always `tl.kill()` + `scrollTrigger.kill()`** in cleanup — un-killed
  timelines leak and double up on fast-refresh / route changes.
- **Reduced-motion renders the final drawn state** with no trigger attached.

---

## 10. Cross-cutting rules

### Motion tokens — `src/lib/motion/tokens.ts`
No component invents its own curve. Everything uses:

- **`EASE = cubic-bezier(0.16, 1, 0.3, 1)`** (an easeOutExpo-like signature),
  mirrored in CSS as `--motion-ease`.
- **`DUR`** — `fast 0.18` / `base 0.32` / `slow 0.55` / `epic 0.8` seconds.
- **`STAGGER = 0.07`** — the standard interval between sibling reveals.

One ease + a tiny duration set is what makes twelve independent animations feel
like one designed system rather than twelve developers' defaults.

### The fallback policy (single source: `shouldReduceScenes()`)
`gsap-client.ts` centralizes the decision: `prefers-reduced-motion` **or**
`pointer: coarse` ⇒ skip motion-heavy scenes. Consequences everywhere:

- WebGL field → 2D `SignalMesh`.
- Lenis smooth scroll → native scroll.
- Pinned scrub scenes → static fully-drawn diagrams.
- Reveals → final state, instant.
- Constellation overlay → not mounted; section shows the boxed diagram.

### Performance budget
- WebGL is **always** `dynamic(() => import(...), { ssr: false })` — never in the
  first bundle, mounted one frame after hydration paints.
- Hot loops mutate typed arrays / plain objects and **never call `setState`**.
- Animate only `transform` and `opacity` in DOM/CSS; avoid `width`/`height`/
  `box-shadow` transitions.
- Pinned scroll is budgeted at ≈30% of total page height.
- Particle count (936) and DPR cap (`[1, 1.75]`) keep the field on a
  `low-power` GL context.

### Accessibility parity
Tabs follow WAI-ARIA roving-tabindex (`use-tabs.ts`); the mobile nav is a
focus-trapped `role="dialog"`; every canvas/field is `aria-hidden` with a
text-equivalent in the DOM (e.g. the ecosystem stage keeps the diagram's
`aria-label` as `sr-only`). Motion is never the only carrier of meaning.

---

## 11. Recipe — build a new SHELEG site from scratch

A pragmatic order that front-loads the parts everything else depends on.

1. **Lay the visual system first.** Implement `DESIGN.md`: near-black canvas,
   one signal accent, hairline structure, mono telemetry labels, the panel /
   button / status-pill components. Motion on top of a weak visual system just
   amplifies the weakness.

2. **Stand up the clock.** Port `scroll-progress.ts`: the `state` object, the
   dual subscriptions (`getScrollState` for per-frame, `subscribeAct` for
   React), the rAF `update()`, the 65%-viewport `measure()`, and the
   `ResizeObserver` re-measure. Verify with a temporary readout of `global` /
   `act` / `form`.

3. **Add smooth scroll.** `SmoothScroll.tsx` with Lenis on the GSAP ticker,
   feeding `setScrollVelocity`. Gate it behind `shouldReduceScenes()`.

4. **Define scenes.** Write your `scenes.ts` registry — one `{ anchor,
   formation, focusX, energy }` per section. Give each section an `id` matching
   its anchor. This is your storyboard; iterate on it in data before touching
   rendering.

5. **Build the field.** `SignalField.tsx`: a seeded point cloud, one builder per
   formation, the `PROFILES` table, and the `useFrame` morph (clamped smoothing
   + per-point smoothstep stagger + arcs). Get *one* formation looking right,
   then add the rest as data.

6. **Mirror it in 2D.** `SignalMesh.tsx` reading the same store, so touch / no-
   WebGL tells the same story. Wire the `AtmosphereField` capability probe.

7. **Layer the DOM choreography.** `FocalSpotlight`, `ParallaxDrift` (one figure
   per viewport), `ScrollRail`. Each is tiny and independent.

8. **Theme the entrances.** Build the `Reveal` family; assign a reveal physics to
   each act's meaning. Always branch reduced-motion to plain.

9. **Add scrubbed instruments** with the Section 9 GSAP recipe for any diagram
   that narrates state over time.

10. **Fuse DOM ↔ WebGL where it earns it.** Only when you want labels exactly on
    clusters or particles synced to a chart: add the `field-sync` bridge, project
    anchors in `useFrame`, read them in a fixed SVG overlay.

11. **Pay the fallback + a11y tax as you go**, not at the end. Every layer ships
    with its reduced-motion branch in the same commit.

12. **Verify like the runbook:** `tsc --noEmit`, `eslint`, `build` clean;
    screenshot each scene mid-hold and mid-morph; emulate reduced-motion; check a
    ~390px viewport. Then deploy.

---

## 12. Why it works (the deeper principles)

- **A single clock removes disagreement.** Most "janky" multi-effect pages have
  each effect measuring scroll on its own schedule; they drift apart by a frame
  and the eye reads chaos. One measured state, read by all, makes layers
  *phase-locked* — they look intentional because they literally share a clock.

- **Cheap-but-many beats expensive-but-few.** 936 points doing simple positional
  lerps, plus five DOM layers reading a mutable object, costs less than one
  heavy library effect — and reads richer, because richness comes from *layers
  agreeing*, not from any single layer's complexity.

- **Redeploy, don't crossfade.** Human attention tracks *moving objects*. A
  phase-staggered, arc-curved migration of points gives the eye things to
  follow; a crossfade gives it nothing and reads as flat compositing.

- **Hold creates legibility; morph creates delight.** Long holds let each
  formation be *understood* (it's the why-now curve, it's the constellation);
  the short morph at the seam is the reward. Constant motion would sacrifice
  both — nothing is understood and nothing is special.

- **Earned motion respects the reader.** Scrub is reserved for instruments that
  genuinely encode time/state. Decorative scrub (parallax everything, scrub the
  hero) is the tell of a template; restraint is the tell of a system.

- **Degrade-to-calm is a feature, not a chore.** Because every layer has a
  static state, the page is *correct* on a low-power phone or for a motion-
  sensitive user, and the rich version is a pure bonus. The fallback isn't a
  worse site; it's the same site, quieter.

- **Data-driven choreography scales.** The whole narrative lives in one `SCENES`
  array and a `PROFILES` table. Re-storyboarding the page is editing data, not
  rewriting render loops. That is why this system can keep growing (ecosystem
  constellation, chart particles, the N finale) without collapsing.

---

## 13. File map (where each idea lives)

| Concern | File |
|---|---|
| The clock / scroll state | `src/lib/motion/scroll-progress.ts` |
| Scene storyboard | `src/lib/motion/scenes.ts` |
| Motion tokens (ease/dur/stagger) | `src/lib/motion/tokens.ts` |
| Lazy GSAP + reduced-motion gate | `src/lib/motion/gsap-client.ts` |
| DOM↔WebGL bridge | `src/lib/motion/field-sync.ts` |
| Interactive field gestures | `src/lib/motion/use-section-field.ts` |
| WebGL particle field | `src/components/webgl/SignalField.tsx` |
| 2D fallback field | `src/components/atmosphere/SignalMesh.tsx` |
| Field/fallback mode switch | `src/components/atmosphere/AtmosphereField.tsx` |
| Constellation SVG overlay | `src/components/atmosphere/ConstellationOverlay.tsx` |
| Progress rail | `src/components/atmosphere/ScrollRail.tsx` |
| Smooth scroll | `src/components/motion/SmoothScroll.tsx` |
| Attention dimming | `src/components/motion/FocalSpotlight.tsx` |
| Figure parallax | `src/components/motion/ParallaxDrift.tsx` |
| Reveal primitives | `src/components/design/Reveal.tsx` |
| Epilogue runway | `src/components/sections/FinaleSection.tsx` |
| Scrubbed instruments (examples) | `WhyNowChart.tsx`, `EcosystemDiagram.tsx`, `PinnedSteps.tsx` |
| CSS tokens + motion styles | `src/app/motion.css` |

---

*SHELEG Design is the motion + systems half of this site's identity; pair it
with `DESIGN.md` for the visual half. The north star for both: it should feel
like a precision instrument responding to your hand — authority through
accuracy and restraint, not spectacle.*
