# AI product patterns — designing the surfaces a model drives

Style packs cover how a product looks. This covers the surfaces that did not
exist when most design systems were written: a model streaming an answer, an
agent taking actions on someone's behalf, a result that might be wrong.

Use it with the [`workbench`](./styles/workbench.md) pack — these are patterns
and states, not a palette. Every token named here is workbench's.

> **The one rule everything below follows: honest state.** A model's output is
> uncertain, slow, occasionally refused, and sometimes wrong. An interface that
> hides any of those is not calmer — it is lying, and the user finds out later
> and trusts nothing afterwards.

---

## 1. The five states of a model call

Design all five before building any. Most AI UI ships state 2 and 3 only, then
improvises the rest in production.

| State | What the user sees | Token |
|---|---|---|
| **Idle** | The input, and a plain statement of what this can do (see §6) | — |
| **Working** | First token as fast as possible; a stop control from the first frame | `--info` |
| **Complete** | The answer, plus where it came from (§4) | `--ok` |
| **Refused / needs a human** | Why, and the nearest thing that *is* possible | `--warn` |
| **Failed** | What broke, whether a retry is worth it, and the retry | `--danger` |

**A refusal is not an error and a rate limit is not a failure.** Collapsing
these into one red toast teaches users that every state means "try again",
which is wrong two times out of three.

## 2. Streaming beats spinners

If tokens can stream, a spinner is a bug. The rules:

- **Never a spinner where text can arrive.** Progress is the text itself. A
  spinner is for a call that returns nothing until it returns everything.
- **Reserve the space, do not reflow.** Growing text that pushes the page down
  makes reading impossible. Fix the container, let it fill.
- **Stop is available from the first frame**, not after some threshold. A run
  the user cannot stop is a run they will kill by closing the tab.
- **Structure arrives before prose where you control it.** A table, diff or
  card skeleton that fills is legible while streaming; a paragraph that
  rewrites itself is not.
- **Never fake it.** Typing delays on a cached or instant response are theater;
  they spend the user's time to look busy.

The typing cursor is the single looping element this skill permits — and it
stops the moment the stream does. Everything else in
[SHELEG_DESIGN.md](./SHELEG_DESIGN.md) §10 still applies: no scrubbing, no
scroll-driven motion, transitions in the 0.12–0.18s workbench range.

## 3. Latency has two numbers

Time-to-first-token and time-to-complete are different products. Optimize and
*show* the first: a surface that starts answering in 300ms and finishes in 12s
feels fast; one that shows nothing for 4s and finishes in 5s feels broken.

For anything past a few seconds, say what is happening in the model's own terms
("searching 4 sources", "running the query") — a progress bar with no basis is
the same lie as a fake percentage. When you genuinely cannot know, an
indeterminate indicator plus elapsed time beats an invented estimate.

## 4. Provenance and uncertainty

- **Cite or don't claim.** If the answer rests on retrieved documents, the
  citation is part of the answer, not a footnote — and it links to the exact
  place, not the corpus.
- **Confidence must be actionable or absent.** "94% confident" produced by
  nothing is confidence theater. Either surface a threshold that changes what
  the user should do ("verify this before sending"), or show nothing.
- **Show the input the model actually used.** Most "wrong answer" reports are
  wrong-context reports; the fastest debugging surface is the one that says
  which files, rows or messages were in scope.
- **Label generated content where a person could mistake it for a record** — a
  drafted reply, a synthesized summary of someone's words, a generated image of
  a real place. Not everywhere: labeling every pixel is noise.

## 5. Agent actions: the confirm is the design

The moment a model stops answering and starts *acting*, the interface's job
changes from presentation to consent.

- **Show the action before it runs**, in the shape it will take: the file diff,
  the recipient and subject, the exact query. "I'll update your settings" is
  not a preview.
- **Irreversible, outward-facing, or costly ⇒ explicit confirmation.** Sending,
  publishing, deleting, paying, granting access. Batch approvals must list what
  is in the batch.
- **Reversible and cheap ⇒ let it run and offer undo.** Confirmation dialogs on
  trivia train people to click through the ones that matter.
- **The run log is a first-class surface**, not a debug panel: what it did, in
  order, with what result, and where it stopped. Use the same status vocabulary
  as the rest of the product (`--info` running, `--ok` done, `--warn` needs a
  human, `--danger` failed).
- **A stopped run says where it stopped and what remains done.** Partial work
  that vanishes silently is worse than a failure.

## 6. Empty states carry the capability

The blank input is where users decide what this product is. It states what the
model can do *here*, in this scope, with two or three real examples — not
"Ask me anything", which is both false and useless. Examples are affordances:
clicking one runs it.

## 7. Chat is a shape, not the shape

Reach for chat when the task is genuinely open-ended. When it is structured,
the structured surface wins: a form for parameters, a table for results, a diff
for edits, a canvas for layout. A chat log is a terrible place to keep state
someone will need again tomorrow — anything worth returning to belongs in a
durable object with a URL.

Corollary: if the product's core loop is "user types the same thing every
time", that thing is a button.

## 8. Cost, quota and scope

Where the user pays per token, per run or per seat, spend is state: show it
before an expensive action, not after. Where a quota exists, show what remains
in the same units the user buys. Where the model reads private data, the scope
indicator ("this session can read your calendar") is permanent, not a one-time
consent people forgot in March.

## 9. Bans

- Spinner where tokens could stream; spinner with no stop.
- Fake typing delay, fake progress percentage, invented confidence score.
- A single red state for refusal, rate limit and crash.
- Auto-executing an outward-facing or irreversible action because the model
  suggested it.
- Chat as the storage layer for something the user will need twice.
- "Ask me anything" as an empty state.
- Hiding that a model produced content that a person would read as a record.
- Cinematic motion on a working surface — the model is the spectacle, and it is
  not one. Reserve this skill's motion layer for landings.

---

## Evidence

The gap this file fills is measured, not assumed: in Figma's *State of the
Designer 2026* (NewtonX, 906 digital designers across five regions, surveyed
September–October 2025), **37% of designers name "designing AI-driven products"
a most-in-demand skill** — ahead of motion design and prototyping (29%),
information architecture (19%) and front-end coding (17%), and behind only
visual polish (58%) and using AI in the process (54%).

The same survey is why "honest state" is the organizing rule rather than one
bullet among many: designers report the risk of AI work being *"too perfect and
too generic"*, and craft — "the choices behind user interactions, visual
systems, language, and product quality" — is what the report identifies as the
differentiator once anyone can prompt their way to a prototype.
