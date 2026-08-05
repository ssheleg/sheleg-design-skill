# Editorial Luxury — the contract this design system ships under

**Register.** Choose Editorial Luxury for warm, editorial, print-inspired
products: research and intelligence tools, content products, premium B2B. It
has two registers — **brand** (landing, use-case, legal, shared pages:
cinematic and editorial) and **product** (the authenticated app: quiet, fast,
never cinematic noise) — and the same components serve both. Warm cream field,
espresso ink, hairline rules, eyebrow labels, stamps, mono data.

**Cream and espresso are two surfaces, not two themes.** They coexist on one
page: a cream section, then an espresso one, then cream again. There is no
`[data-theme]` block in this stylesheet and no toggle to build — wrap a section
in `.el-espresso` and every component inside it re-reads its ink, its hairlines
and its accent from that scope. `.el-cream` does the reverse for a cream block
inside an espresso section, and is never needed at the top of a page. Building
a light/dark switch here would ship a control this design never had.

**The accent rule.** There is exactly one functional accent: sage `--accent`
(links, CTAs, the "signal" that runs through the narrative). On espresso
sections the accent switches to `--accent-on-dark` — the same role, brightened
so it survives the dark field. Text sitting **on** the accent is
`--accent-ink`, which clears 6.1:1 over `--accent-deep` and is large-text-only
over `--accent`; that is why the primary button fills with the deep sage.
`--terra` is a rare editorial highlight, not a second accent, and `--red` is
negatives only — the "without" column of a comparison, never a warning badge.
Buttons are tactile (`translateY(-2px)`, no glow); cards lift and their border
warms; focus-visible is a 2px sage outline at 3px offset. Never nest a card
inside a card.

**Bans** (verbatim from the pack):

- No gradient text, no side-stripe accent borders, no glassmorphism, no
  neon/outer-glow shadows, no purple.
- No emojis in product UI; no Inter/system display fonts (Fraunces owns
  display).
- Never flatten the cream identity into generic white; never let motion
  gate content visibility.

Motion is not part of this design system and must not be invented: the film
grain, the magnetic CTAs, the sage cursor ring and the artifact previews that
assemble on scroll all stay behind in the pack. A kit is the static half of a
pack, and that is a contract rather than a gap.
