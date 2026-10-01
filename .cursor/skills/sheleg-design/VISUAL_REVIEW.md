# Visual review — what a screenshot has to prove before it counts

A screenshot is evidence only when it is evidence of the RIGHT thing, freshly,
and rendered. A blank frame, a frame of the wrong route, or one captured before
the fonts loaded looks exactly like a pass to anyone reading a filename. This
file is the contract a visual claim clears before it is called a *visual-pass*
— and the line past which "I could not capture it" is stated as **unverified**
rather than dressed up as a reading.

## Contents

- The capture record
- Fitness — what disqualifies a frame
- Capture is tool-agnostic
- Visual evidence is its own class — do not launder others into it
- Rendered copy — the design/copywriting seam

## The capture record

Every visual claim carries the record of what was actually captured. A
screenshot with no record is an image, not evidence:

| Field | What it pins |
|---|---|
| `revision` | the commit/tree the capture ran against — a proof identity, the same discipline the work-graph's `close` applies |
| `route` | the URL/screen actually loaded (not the one intended) |
| `scenario` | which product scenario this frame stands for (the source of truth super-ux owns) |
| `state` | empty / loading / error / populated — the state under test, not whichever happened to render |
| `viewport` | width×height and device-pixel-ratio |
| `locale` | the language the copy rendered in |
| `theme` | light / dark / the token theme applied |
| `motion` | reduced or full — a still of an animated surface says which |
| `captured-at` | ISO-8601 UTC, so staleness is computable |
| `source` | the capability that took it (see below) — never assumed |

## Fitness — what disqualifies a frame

A capture is **not** a visual-pass, and may not be promoted to one, when:

- **it is blank** — an all-one-colour or empty frame is a failed render, not a
  clean screen;
- **it is stale** — its `revision` is not the revision under review, or its
  `captured-at` predates the change it claims to show;
- **it is the wrong route/scenario/state** — a frame of `/` cannot pass a claim
  about `/pricing`, and a populated frame cannot pass an empty-state claim;
- **the wrong viewport** answered a viewport-specific claim;
- **the fonts had not rendered** — a frame captured before webfonts settle shows
  fallback metrics, which is a different layout than the one shipped.

When none of the above can be checked because **no runtime capture is
available**, the claim is recorded as **`unverified`**, not as a pass. Static
work continues — the contract never demands a mandatory tool install — it is
just honest that the visual half was not seen.

## Capture is tool-agnostic

The capability that produces the frame is named in `source`, and **any working
browser capability qualifies** — Playwright MCP, a Chrome DevTools bridge, a
headless run, a screenshot MCP. **Playwright is not required**; a review does
not fail because one specific tool is absent, and it does not install a tool to
manufacture a pass. If no capability is present, that is the `unverified` case
above, stated plainly.

## Visual evidence is its own class — do not launder others into it

Four kinds of evidence answer different questions, and one may not be relabelled
as another:

- **visual evidence** — a fit capture per this contract: what the pixels look
  like;
- **DOM / source reading** — what the markup or code SAYS; it can prove a class
  is applied, never that it rendered;
- **functional trace** — a log, a network call, a test run: what HAPPENED, not
  what it looked like;
- **native device evidence** — a capture from a real iOS/Android device or its
  simulator.

**A native mockup is not a verified native interface.** A web render styled to
look like a phone, or a design comp of an app screen, is a mockup — calling it a
verified native interface claims a device evidence class it does not hold.
Native readiness is claimed only from native device evidence, and its absence is
`unverified`, never inferred from a web capture that resembles the platform.


<a id="rendered-copy"></a>
## Rendered copy — the design/copywriting seam

During visual review, read what the user actually sees: hero eyebrows, headings,
line-break fragments, captions and labels, including text split across inline
markup. Compare each role with the **project policy** in the brand pack.
Copy rules belong to **copywriting** (AT-07 covers terminal full stops in titles
and labels); design catches mismatches between that policy and the rendered
composition. It does not invent a second punctuation linter. A project can
extend the default to hero supporting copy, but ordinary prose keeps its normal
sentence punctuation. Respect a documented intentional exception.

Keep a small review record: **selector**, role, **visible text**, **viewport**,
**revision**, policy reference, finding and disposition. Inspect the supported
narrow and wide layouts: a full sentence may become a misleading fragment when
split for visual emphasis. A corrected headline needs both the source/generated-copy
fix and a new capture. Where templates regenerate the text, fix their source too.

| Review probe | Expected review action |
|---|---|
| `<h1>Your agents.<br>Your tools.</h1>` under a no-title-period policy | Flag both display fragments, including an inline-styled final word. Check the rendered narrow and wide versions after correcting the source. |
| A hero paragraph ends in a period | Apply the project's rule for that role. Do not strip ordinary prose because a title rule exists. |
| `Ready?`, `Dr. Ada`, `v1.2.3`, `https://example.org`, or `Loading…` | Preserve meaningful punctuation in questions, abbreviations, version numbers, URLs and ellipses. Do not use a global replacement. |
| No runtime capture; the text extractor flattened all headings | Mark the visual claim **unverified**. Repair or report source-role coverage; inspect source provisionally and do not claim a rendered pass. |

A linter's **exit 0** proves only the rules and sources it actually checked.
Record its coverage and whether those sources preserve the roles above; a flat
copy export, skipped source glob or token/contrast pass does not demonstrate
that the visible headlines passed copy review. Route textual findings back
through copywriting, compare the resulting composition, and record unresolved
items explicitly. This is a review procedure, not evidence that a model followed it.
