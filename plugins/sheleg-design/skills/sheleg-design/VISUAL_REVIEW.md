# Visual review — what a screenshot has to prove before it counts

A screenshot is evidence only when it is evidence of the RIGHT thing, freshly,
and rendered. A blank frame, a frame of the wrong route, or one captured before
the fonts loaded looks exactly like a pass to anyone reading a filename. This
file is the contract a visual claim clears before it is called a *visual-pass*
— and the line past which "I could not capture it" is stated as **unverified**
rather than dressed up as a reading.

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
