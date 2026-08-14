# Paperclip — the design contract

The reference is <https://paperclip.ing>, measured 2026-08-14 from the two shipped
stylesheets (`/_next/static/chunks/0sw-z-v7xc9dd.css`, 622 rules, and
`/_next/static/chunks/19xj4kovk13jy.css`, 712 rules), the hero's inline SVG and the
`@font-face` block. Both themes read. The full pack is `styles/paperclip.md`; this file
is what a design agent must not get wrong.

## The one thing this pack is

**No functional colour, and one loud object that does nothing.** A neutral coal field,
every control monochrome, elevation made of hairlines — and the entire chromatic budget
spent on a curtain of gradient capsules behind the headline and a row of gradient section
badges, neither of which can be clicked. Delete every colour from this page and it loses
its poster, not its meaning.

## Non-negotiable

- **The accent is the inverted field.** Solid `--accent`, label in `--accent-ink`, capsule
  radius, one per viewport. A brand hue has nowhere to live here.
- **A coloured thing is never interactive.** No gradient button, no gradient link, no
  hover on a badge. This is the rule the whole composition rests on.
- **Status is never by colour alone.** `--good` and `--warn` separate by 6.2 under
  protanopia and `--good` and `--info` by 6.7 under tritanopia — both below the 8.0
  floor — and in the light theme `--good` (2.28:1) and `--warn` (2.15:1) are below the
  3:1 non-text floor on paper. Every dot, ring, tint and bar carries its word.
- **The capsule is the shape.** `--r-pill` on the button, the badge, the org node and the
  10 × 20 schedule mark alike. A circle is a point; a capsule is a paperclip's end. The
  avatar is the single circle in the system, and the data bar's flat 4px the single
  square-ended form.
- **Elevation is a hairline.** One resting shadow exists in the whole pack and it belongs
  to the modal. No card floats, and the sticky nav gains nothing on scroll.
- **In light there is no surface step.** `--bg` and `--surface` are the same white. A grey
  card fill turns this pack into a generic dashboard in one commit.
- **The tracking closes as the size opens** — −0.01em at 16px through −0.045em at 44px.
  A 60px headline at the default 0em is the fastest way to lose the pack.
- **One noise recipe, on saturated surfaces only.** `fractalNoise`, `baseFrequency 2.95`,
  5 octaves, seed 9, tiled at 256px, `mix-blend-mode: overlay` under `isolation: isolate`
  — 12% on a badge, 86% on the artwork. The field itself stays flat colour.
- **One stagger, 140ms, everywhere.** The org tree, the swimlanes, the goal cascade and
  the card reveals share it. Change it in one place or not at all.
- **Hover is colour, border and fill. Never geometry.** Nothing lifts, scales or shifts.

## What the reference gets wrong, and this kit does not

- `--status-task-in_progress` stays at its light value on the dark field — **3.83:1**,
  set as text. The kit ships `#60a5fa` at 7.79:1 and marks it derived.
- The one text input sets `outline: none` on focus and replaces the ring with a 1px border
  colour change. Keep the ring.
- Two 1.5s infinite loops (`dotPulse`, `statusBlink`) survive `prefers-reduced-motion`.
  Stop them; their meaning is already in the word beside them.
- The budget bar transitions `width` for 1.2s, per bar, six bars in view. Never that —
  `transform: scaleX()` from a left origin.
- There is no `@media (hover: hover)` anywhere, so every hover state fires on first touch.
- `font-weight: 450` is asked for and only 400 and 500 are loaded, as static instances.

## Container, not viewport

Four components size against their own box and carry `container-type: inline-size`:
`HairlineGrid`, `OrgNode`, `LedgerRow`, `ScheduleLane`. The page's own breakpoints — the
nav, the hero padding, the artwork offset, the section rhythm — stay on the viewport,
because the page is not inside anybody's container.
