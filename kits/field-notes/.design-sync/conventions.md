# Field Notes — the contract this design system ships under

**Register.** Choose Field Notes for **an open-source or developer product sold on
auditability rather than power**: code intelligence, observability with a lineage
story, data provenance, evaluation and benchmarking tools, security tooling that has
to show its work, agent memory. It suits a product whose argument is *here is where
this answer came from*. The fork people get wrong is against `instrument-console`: a
cockpit answers *what is happening now*, field notes answer *how do you know* — if the
product has a dial or a live state, that pack; if its output is a claim that has to be
traceable, this one. Against `workbench`: that one is neutral grey and is supposed to
disappear, this one is warm and has a voice. The composition is the constraint —
**the page is one continuous sheet of warm paper with hairlines drawn on it.** A
section is `border-top: 1px solid var(--line)` plus 64px of padding, and nothing else;
elevation is a ring (`0 0 0 1px var(--line)`), never a shadow. Build every screen
against `var(--…)` and never a literal.

**The accent rule.** Three semantic hues and no fourth: rust (`--brand`) is the brand,
green (`--verify`) is *verified*, red-orange (`--witness`) is *unverified*. A fourth
hue means one of them stopped meaning something. **`--verify` is a fill and `--brand`
is a text colour, and they are not interchangeable** — green at 3.2:1 may hold a dot, a
bar, a chart series or a 40px number; the rust at 6.3:1 may hold a sentence. On any
dark surface the brand is `--brand-on-dark`, because the paper rust measures 2.29:1 on
the hero's top stop. `--ink-soft` is a real body colour here at 5.2:1, so secondary
copy stays quiet instead of being promoted to full ink. Mono is **furniture, not data**:
eyebrows, section numbers, version strings, provenance tags — which inverts `workbench`,
where mono means *this is a number*.

**Bans** (verbatim from the pack):

- `--verify` as text at body size; white on `--verify`; `--brand` (the light
  value) on any dark surface — use `--brand-on-dark`.
- A true black, a cool grey, a pure `#FFF` card, or any framework default
  neutral (`#18181B`, `#F2F3F4`) beside the green-cast palette.
- A fourth semantic hue; the provenance colours used for anything that is not
  provenance; `--danger` and `--witness` conflated.
- **Italic anywhere.** The display face has none, so `<em>` synthesises a
  slanted fake. Emphasis is a colour change on one phrase, or the mono voice.
- A hardcoded radius in px; a grey drop shadow where the ring belongs;
  `transition: all`; hover states that scale or lift.
- A second dark section below the hero; a dark band with a hard edge; a
  full-bleed colour block. The hero is the only dark surface, and it dissolves.
- Mono for long-form copy; a `tabular-nums` data table styled as annotation, or
  an annotation styled as data.
- A confidence *percentage* where a provenance *tag* belongs.
- A claim with no source in the same block.
- A particle field, a mesh gradient, or any decorative gradient other than
  `--hero-dawn` and `--hero-vignette`.

Motion is not part of this design system and must not be invented: a kit is the
static half of a pack, and anything that moves stays behind in the pack. The dawn is
a gradient, not an animation.
