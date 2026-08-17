# Motion doctrine

The SHELEG core says motion rides one clock, layers, and degrades to calm. That
tells you how motion is *built*. This file tells you whether to build it at all,
how long it runs, what curve it rides, and which forms are simply wrong.

Every number here is a decision someone else already paid for. Use them.

---

## 1. Should this animate at all?

The first question is not "what animation" — it is "how often will a person see
this". Frequency decides, and it decides before taste gets a vote.

| How often a user sees it | Decision |
|---|---|
| 100+ times a day — command palette, keyboard shortcut, tab switch | **No animation. Ever.** |
| Tens of times a day — hover, list navigation, inline toggles | Remove it, or cut it to the floor |
| Occasional — modals, drawers, toasts, page transitions | Standard animation |
| Rare or first-time — onboarding, empty-to-filled, celebration | Delight is allowed here |

**Never animate a keyboard-initiated action.** Those fire hundreds of times a
day; animation turns them from instant into laggy and disconnects the result
from the keypress. Raycast has no open/close animation, and that is the correct
answer for something opened two hundred times a day — not an oversight.

A pack with a high motion register does not overrule this table. The register
says how motion *feels* where it exists; the table says where it exists.

### What it must be for

Every animation answers "why does this move?" in one sentence. Valid answers:

- **Spatial consistency** — a toast leaves the way it arrived, so swipe-to-dismiss
  feels obvious rather than learned.
- **State indication** — the thing changed and the change is visible.
- **Feedback** — the interface heard the click.
- **Explanation** — the motion shows how the feature works.
- **Preventing a jarring cut** — appearing and vanishing with no transition reads
  as broken.

"It looked cool" is not an answer. If you cannot write the sentence, delete the
animation.

---

## 2. Easing

### The decision tree

```
Is the element entering or leaving?
  yes -> ease-out          (starts fast; the interface feels immediate)
  no  -> is it moving or morphing on screen?
           yes -> ease-in-out
         is it a hover or colour change?
           yes -> ease
         is it constant motion (marquee, progress, scrub)?
           yes -> linear
         otherwise -> ease-out
```

### `ease-in` is banned in UI

It starts slow. The delay lands in the exact moment the user is watching hardest
— just after the click. A dropdown on `ease-in` at 300 ms *feels* slower than
the same dropdown on `ease-out` at 300 ms, with identical duration on the clock.
Keep `ease-in` for something leaving the screen entirely, and even then prefer
`ease-in-out`.

### The curves

The built-in CSS easings are too weak to read as intentional. Use these:

```css
:root {
  /* UI interactions: enters, exits, state changes */
  --ease-out: cubic-bezier(0.23, 1, 0.32, 1);
  /* Movement and morphing on screen */
  --ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);
  /* Drawers and sheets — the iOS feel, from Ionic */
  --ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
}
```

A pack may override these — that is what `## Motion tokens` is for — but it
names its curve explicitly. A pack that ships no curve inherits these three, and
`linear` and `ease-in-out` are never defaults.

---

## 3. Duration

| Element | Duration |
|---|---|
| Button press feedback | 100–160 ms |
| Tooltips, small popovers | 125–200 ms |
| Dropdowns, selects | 150–250 ms |
| Modals, drawers, sheets | 200–500 ms |
| Marketing, explanatory, scrollytelling | longer, deliberately |

**UI motion stays under 300 ms.** A 180 ms select feels responsive; the same
select at 400 ms feels like the app is thinking.

Speed is not only comfort — it is perceived performance. A faster spinner makes
an identical load feel shorter. A tooltip that skips its delay after the first
one makes the whole toolbar feel quicker. Easing amplifies this: `ease-out` at
200 ms reads faster than `ease-in` at 200 ms because movement starts at once.

---

## 4. Springs

Springs have no duration; they settle. Reach for them when motion should feel
physical rather than scheduled:

- drag with momentum,
- gestures a user may reverse mid-flight,
- decorative pointer tracking,
- anything that should feel alive rather than played back.

Prefer Apple's parameterisation — it is the one you can reason about:

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }   // preferred
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }   // when you need the control
```

Keep `bounce` between 0.1 and 0.3, and keep it out of most UI. Bounce belongs to
drag-to-dismiss and to play, not to a settings panel.

**Interruptibility is the real reason to use one.** A spring keeps its velocity
when interrupted; CSS keyframes restart from zero. Expand a row, hit Escape
mid-flight, and a spring reverses smoothly from wherever it is while a keyframe
animation snaps and replays.

Tying a value directly to pointer position feels artificial because it has no
inertia. Run it through a spring instead of assigning it — and only when the
effect is decorative. On a functional readout, no motion beats smoothed motion.

---

## 5. Forbidden forms

These are not stylistic preferences. Each one is a defect with a known failure.

- **`window.addEventListener("scroll", …)`** — runs every frame, unbatched,
  janky. Use `useScroll()`, `ScrollTrigger`, `IntersectionObserver`, or CSS
  scroll-driven animation (`animation-timeline: view()`).
- **Scroll progress computed from `window.scrollY` into component state** — same
  defect, now with a re-render on every frame.
- **`requestAnimationFrame` loops that write to component state** — use motion
  values (`useMotionValue` / `useTransform`) so the work stays off the render
  cycle.
- **State for continuous input** — pointer position, scroll progress, magnetic
  hover, physics. Storing these in `useState` re-renders the tree on every
  movement and collapses on mobile.
- **Animating a property that triggers layout** — `top`, `left`, `width`,
  `height`, `padding`, `margin`, `gap`, `font-size`. These re-lay-out the
  document on every frame. Animate `transform` and `opacity`, which the
  compositor handles alone; `filter` and `clip-path` are also safe. Paint-only
  changes (`background-color`, `border-color`, `color`, `box-shadow`) are
  cheaper than layout and are permitted — §2 gives them an ease and §9 treats a
  colour change as the baseline everything else is measured against. The ban is
  on **layout**, not on everything outside a list of four; an earlier wording
  said "anything but `transform`, `opacity`, `filter`, `clip-path`", which
  contradicted both of those sections.
- **`backdrop-filter` on a scrolling container** — continuous GPU repaint. Blur
  belongs on fixed or sticky elements.
- **Grain and noise on a scrolling container** — same reason. Put them on a
  `position: fixed; pointer-events: none` layer.
- **`will-change` left behind** — it is a hint for motion about to happen, not a
  decoration. Remove it when the animation ends.
- **More than one marquee per page.** One can carry content; two read as filler.

---

## 6. Scroll motion

- **Under `scrub`, easing must be `none`.** The scrollbar is already the clock;
  a second easing curve on top of it makes the motion feel detached from the
  hand. This is the most common scroll bug and the least obvious.
- **In React, use `useGSAP` from `@gsap/react`, never a bare `useEffect`.** It
  reverts the context and kills the ScrollTriggers for you. Hand-rolled cleanup
  is where leaked triggers and doubled animations come from.
- **Pin at the top: `start: "top top"`.** A sticky stack or horizontal pan that
  uses `"top center"` or `"top 80%"` begins mid-scroll and shows the user half a
  slide before it catches.
- **`markers: true` is a development tool.** It never ships.
- **Do not mix engines in one component tree.** GSAP, Three.js and Motion each
  want the frame; pick one per subtree and isolate it in a leaf.

---

## 7. Motion that came from a design tool

When animation values arrive from a design file rather than being authored:

1. **Do not invent motion.** A node with no animation data stays still. Never
   borrow a duration or curve from a neighbouring element, and never animate
   something because the rest of the component is animated.
2. **Validate one animation end to end before repeating it.** "Renders without
   errors" is not "renders correctly". One wrong curve is obvious; the same
   wrong curve on twenty nodes is an afternoon.
3. **Factor repeats out.** Elements usually share one animation and differ only
   by delay or offset. Ship one reusable component or one `variants` object
   parameterised by what varies. The same transition literal pasted fifteen
   times is a defect even when it runs.
4. **Layout transforms and animated transforms collide.** A Tailwind utility
   like `-translate-x-1/2` writes the same CSS `transform` that a motion library
   writes inline — so the animation silently erases the centring. Split it: a
   static wrapper carries the layout transform, an inner animated element
   carries rotate/scale/opacity. Or encode the offset in the animation itself
   (`x: "-50%"`) and keep it in every keyframe.

---

## 8. Anti-drift

The failure this whole skill exists to prevent: the tokens are right, the pack
is right, and the built page is generic anyway. Drift happens at application
time, not at specification time.

While implementing against a pack, never:

- simplify a distinctive section into a default template row,
- compress the pack's spacing into a tighter default,
- replace its type hierarchy with a plain one,
- collapse varied sections into one repeated pattern,
- reintroduce nested boxes the pack removed,
- swap a named font for a system stack "for now",
- drop the signature element because it was the hardest part.

The built page must still read as the same design as the pack. If a decision
makes it easier to build and less like the pack, it is drift — name it out loud
or do not make it.

---

## 9. Reduced motion

Not a feature. A contract.

- Anything beyond a colour change honours `prefers-reduced-motion: reduce`.
- Infinite loops, parallax, scroll hijack, magnetic physics and spring chases
  collapse to static or instant — not to "slower".
- In a motion library, gate on the reduced-motion hook and render the resting
  state. In CSS, put motion behind `@media (prefers-reduced-motion: no-preference)`.
- WebGL and canvas scenes degrade to their CSS or SVG still.

**Shipping an animation without a reduced-motion path is a bug, not a polish
item.** It fails review the same way a crash does.

---

## 10. Pre-flight

Before calling motion done:

- [ ] Every animation survives the "why does this move?" sentence.
- [ ] Nothing on the 100+/day path animates at all.
- [ ] No `ease-in` in UI; curves are named, not inherited by accident.
- [ ] UI durations under 300 ms; the table was consulted, not guessed.
- [ ] No banned form from §5 appears anywhere in the diff.
- [ ] Every `scrub` carries `ease: "none"`.
- [ ] Every ScrollTrigger has a cleanup path.
- [ ] `markers` removed.
- [ ] Reduced motion tested by actually turning it on.
- [ ] The page still looks like the pack (§8).

---

## How the calibration dials bind

- **The pack wins on values, the dials win on amount.** A dial never invents a
  colour, a face, or a radius — those come from the pack's token layer. It
  decides how much asymmetry the grid carries, how much of the page moves, and
  how tightly it is packed.
- **`MOTION_INTENSITY` is capped by the frequency table**, not the other way
  round. A 9 on a settings screen still means the keyboard path does not
  animate. Read [`MOTION_DOCTRINE.md`](./MOTION_DOCTRINE.md) §1 first; the dial
  turns up what is left after that table has cut.
- **Motion claimed is motion shown.** Above 4, the page actually moves —
  entrance on the hero, reveal on key sections, response on the primary action.
  A static page announcing 7 is broken. If working motion will not fit the
  scope, drop the dial to 3 and ship a clean still page; never half-build motion
  that stalls, cuts off, or jumps.
- **A standalone pack pins its own ceiling.** `workbench`, `briefing-room` and
  `ledger` are not cinematic; `MOTION_INTENSITY` above 3 on any of the three is a
  misread of the pack, not a bold choice — `ledger` allows exactly three loops,
  all of them state (a typing cursor, thinking dots, a live heartbeat), and stops
  all three under reduced motion. `pigeonhole` is cinematic but at the family's floor: it bans the scroll clock,
scrubbing, parallax and a sticky nav, so `MOTION_INTENSITY` above **4** on it has
nothing legal to buy. **`roster` has the same ceiling of 4** for the same reason —
entrance, hover and two slow floats are its whole budget, and it bans scrubbing,
parallax and `animation-timeline`; it keeps a sticky nav, which is the only difference.
  **Four more standalone packs pin their own, and each states it in its own Register:**
  `ora` at **4**, `tenor` at **4**, `paperclip` at **5** — the last one higher because it
  is the only pack in the family that spends a native scroll-driven parallax —
  and `bulletin` at **3**, the lowest ceiling in the library, because its whole
  measured motion budget is an entrance fade, a 0.12s press and a 0.3s hover.
  Its depth is drawn as a hard ink offset rather than animated, and animating
  that offset is precisely what flattens it.
  `field-notes` is standalone **by default** and may opt into the cinematic layer — it carries a `## Motion flavor` section saying
  how — so it is the one standalone pack without a hard ceiling. Read that
  section before turning the dial up on it.

Moved out of `SKILL.md` on 2026-08-16: the body was 6203 tokens against a
< 5000 budget, and every rule here is about what §1's frequency table has already
cut. The dial turns up what is left after that table — so the table and the dial
belong in one file.

