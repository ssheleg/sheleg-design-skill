# Creative Director — the first act, before any pixel

This is what `/sheleg-design` opens with. Everything else in this bundle is a
craft reference; this is the decision layer that says **which craft, whose tools,
and how you will know it worked**.

It exists because the failure mode of an agent doing design is not ugliness. It
is *plausibility*: a page that looks like a design, answers no stated need, was
built with whatever skill happened to fire first, and cannot be argued with
because nobody wrote down what it was supposed to do. Five acts, in order. Act 1
and Act 5 are the two that are usually skipped, and they are the two that make
the middle three worth doing.

---

## Contents

- Act 1 — The brief, and the sentence that could falsify it
- Act 2 — Cast the tools, by measuring rather than recalling
- Act 3 — Fork, but only when the fork is real — and write the rubric first
- Act 4 — Judge, then graft, then record what the cast produced
- Act 5 — Validate: alignment first, then quality
- Focused visual work
- The output the director owes

## Act 1 — The brief, and the sentence that could falsify it

**Nothing is designed until this exists in writing.** Four lines, and the fourth
is the one that costs something:

| | |
|---|---|
| **Surface** | landing / hero, product UI, mobile screen, agent interface, deck-as-page |
| **Job** | what the person who lands here must be able to do, in their words |
| **Constraint** | the thing that is not negotiable — a brand, a stack, a deadline, an existing system |
| **Falsifier** | **what would prove this design failed**, stated so that it could actually happen |

A falsifier is not "it looks bad". It is *"a first-time visitor cannot say what
this product does after five seconds"*, *"the primary action is below the fold on
a 13-inch laptop"*, *"the dashboard's densest table needs horizontal scrolling at
1280px"*. If you cannot write one, the brief is a mood and the rest of this
document cannot help you.

**Where the brief comes from, in order of preference.** If `super-ux` is
installed and the project keeps a UX scenario base — `/ux` reports whether it
does and where — the Job line is **traced to a scenario id**, not invented, and a
design that answers no scenario is the first finding, before any visual work. No
scenario base: offer `/ux` once, then proceed with the brief written here and say
plainly that it is unvalidated.

**Mode changes where you enter, and it is not cosmetic.**

| Mode | Enters at | Why |
|---|---|---|
| **New design** | `style` | there is nothing to measure yet; the direction is the first commitment |
| **Redesign** | `verify` + `a11y` **first** | you are replacing something that works for somebody. Measure it before you take it away, or you will re-ship its defects and lose its accidents |
| **Update** | the affected visual role | preserve the chosen identity; a targeted component, type or spacing correction does not automatically replace the design direction |
| **Audit** | checks relevant to the stated scope | inspect before proposing changes; distinguish visual evidence, behavior, accessibility and performance, and state unavailable checks |

The redesign row is the one people get wrong. **A redesign starts with a
measurement of the thing being replaced** — contrast, keyboard path, what the
current page actually does on the target viewport — because half of "the old one
was bad" turns out to be "the old one handled a case I have not thought about".

---

## Act 2 — Cast the tools, by measuring rather than recalling

The director does not choose from memory. On a typical machine this pack is a
small fraction of what is installed, and most of it is invisible to a router that
only knows its own roster.

```bash
npx sshlg-skills pack design --lane <style|brand-surface|product-surface|motion|tokens|figma|implement|mobile|verify|a11y|handoff>
```

That prints, for the lane you named: what is **present** here, what is
**missing** with the exact install command, and which of them have been
**measured and declined**. It reports and never installs.

**Absent, nothing is blocked** — the umbrella is an optional sibling like every
other one this skill names. Two of the three things the command gives you have a
substitute and one does not, and the difference is worth knowing before you
proceed: the **lane table below is in this document**, so the question *whose
answer is this* is still answerable, and the agent's harness already puts every
installed skill's name and description in front of you, so *what do I have* is
answerable too — coarsely, by reading rather than by matching. What you lose is
the half no local reading can reconstruct: **what is MISSING and the command that
would install it**, and **what has already been measured and declined**, which is
the part that stops a plausible-looking recommendation from being taken twice.
Cast from the harness's list, and **say in the cast that the roster was not
measured** rather than presenting it as though it had been.

**Then print the cast before starting** — the skills you will use, one line each
saying what for, and the lane each serves. Not for approval; so the operator can
see the choice and correct it. A cast that is never printed cannot be corrected,
and an agent that silently reached for the first skill that fired has made a
decision nobody can audit.

**The three lanes with no owner in this family are the ones to check hardest** —
implementation, verification and **accessibility**. Nothing here asks whether the
interface can be used at all; that lane is delegated, and delegation only works
if somebody actually casts for it.

**Ours versus theirs is not a loyalty question.** Where an outside skill answers
the lane better, cast it. The one rule that does not bend: **this skill decides
the route, and everything cast is a tool inside a lane — never a second entry
point.** Some of them advertise themselves as one; a broad `user-invocable`
design skill will fire on the same prompt you did. That is not a reason to avoid
it. It is a reason to say, out loud, which one is directing.

---

## Act 3 — Fork, but only when the fork is real — and write the rubric first

Two variations built by two subagents with **different casts** is the strongest
move in this document and the easiest one to turn into theatre.

### Direction exploration is a separate experiment

Comparing tool casts does not compare artistic directions. When the visual
direction is unsettled, render two meaningfully different treatments even if
only one credible cast is available. Use the same agreed behavior and realistic
content; vary composition, typographic hierarchy, imagery/material and spatial
rhythm, not only accent colour or a chat-versus-services navigation choice.

Record **locked invariants** (brand, accessibility, approved behavior, platform)
and **open axes** before rendering. A locked brand does not freeze every
composition. Sketch with provisional semantic tokens inside those invariants;
after comparison, consolidate the chosen direction into the pack contract.
Do not require a fully authored style pack before the renders needed to choose
it exist. A token-only switch compares compatible skins, not the whole design space.

This exploration may be sequential within one agent; the disjoint-cast fork
below remains a separate, optional experiment. Preserve the operator's chosen
direction when it is already settled. Record the losing direction and why it
lost without adding an unnecessary approval round for a decision already made.

### The rule that makes it honest

**The rubric is written before either variation is made, and it is not touched
afterwards.** If you build two and then decide what you were comparing, you have
not run a comparison — you have picked the one you liked and written the
justification backwards. Three to five criteria, each one *checkable by someone
who did not build either variation*, and each one traceable to the brief's Job or
Falsifier.

A usable rubric line looks like *"the primary action is reachable without
scrolling at 1280×800"* or *"the type scale uses at most five distinct sizes"* —
not *"feels more premium"*.

### When to fork

Fork when **all three** hold:

1. the lane has both a credible family answer and a credible outside one,
2. the brief is genuinely under-determined — two defensible directions exist,
3. the surface is worth it: a landing page, a hero, a product's main screen, a
   visual language being set for the first time.

### When NOT to fork

A token change. A spacing fix. A bug. A surface with a locked design system,
where the answer is *apply the system* and two variations are two ways of
disobeying it. Anything where the brief already determines the answer — forking
there does not explore a space, it manufactures a choice and then spends someone's
attention resolving it.

### How to run it

Two subagents, launched together, each given:

- the **same** brief from Act 1, verbatim,
- the **same** rubric, verbatim,
- **its own cast, declared and disjoint** — variation A on this pack's style pack
  and doctrine; variation B on the outside skills cast in Act 2,
- an instruction to produce a **working surface**, not a description of one,
- **no knowledge of the other variation.** They must not read each other's output,
  or the second one converges on the first and the comparison collapses.

Name the casts in the output. *"A: workbench + MOTION_DOCTRINE. B: impeccable
product mode + vercel-composition-patterns"* is a record that makes the next
casting decision better; *"two options"* is not.

---

## Act 4 — Judge, then graft, then record what the cast produced

Score both against the rubric written in Act 3. Then do the two things a bare
verdict skips:

**Graft.** Name the specific thing the losing variation did better and carry it
into the winner. A fork that discards half its own output wasted half its cost.
If the loser had nothing worth carrying, say so — that is a real finding about
the cast, not a formality.

**Record which tool produced which trait.** *"B's type scale was tighter and came
from its font-pairing data; A's motion degraded correctly and B's did not"* is
the sentence that makes the next run's Act 2 sharper. Without it, every fork
starts from the same ignorance as the first one.

**Where the two variations are equally defensible, say so and stop.** Two
credible directions is a decision for a person, and a director that manufactures
a preference to look decisive is worse than one that hands over a clean choice
with the trade-off named.

---

## Act 5 — Validate: alignment first, then quality

Two different questions, and passing one says nothing about the other.

### Alignment — does this answer the brief?

- Every element on the surface traces to the **Job**, or is deliberate decoration
  and named as such. An element that traces to neither is the first thing to cut.
- The **Falsifier** is checked, out loud. If it is now true, the design failed
  and no amount of craft in the middle acts changes that.
- Where scenarios exist, the surface is checked against them — `/ux-audit` does
  this with `file:line` evidence, and it is the only alignment check here that is
  mechanical.

### Quality — the measurable half

These are checks, not opinions. Each one produces a number or a yes/no that a
second reader can reproduce:

| Check | How it is measured |
|---|---|
| Contrast | every text/background pair against WCAG AA; body text ≥ 4.5:1, large ≥ 3:1 — a **computed ratio**, never a glance |
| Colour is not the only signal | every status, link and error state carries a second cue — shape, icon, weight, text |
| Keyboard path | every interactive element reachable and visibly focused, in DOM order |
| One anchor per viewport | count what competes for first attention; more than one means none |
| Type scale | count the distinct font sizes actually rendered — an ad-hoc scale shows up as a long tail |
| Token discipline | `grep` for raw hex and raw px outside the token layer; a one-off value is a system leaking |
| Motion, and its absence | every duration inside the doctrine's bands, and the surface fully usable under `prefers-reduced-motion: reduce` — checked by turning it on, not by reading the CSS |
| Renders without JS | the content is present in the served HTML — matters for the reader who is a crawler as much as for the one on a slow connection |

**Run them where the thing runs.** A screenshot in a browser at the target
viewport beats reading the diff, every time; `webapp-testing` and the Chrome
DevTools tooling exist for this, and the `verify` lane in Act 2 casts them. A
quality claim made from source is a claim about source.

### The limit, stated rather than implied

For a new direction or substantive redesign, also run a visual critique loop:
compare rendered states at the same viewports and with the same content against
the brief and selected reference traits; name the specific weak hierarchy,
composition, typography, imagery or platform treatment; change it and render
again. This loop applies even when no cast fork ran. Keep the before/after
evidence and distinguish visual judgment from functional and mechanical checks.
Change a render only for an actionable finding. If the rubric yields none, stop.
Set a bounded iteration/time budget before the loop; at its end record unresolved
findings. Surface a material unresolved direction choice to the operator without
inventing another approval gate for an already selected direction.

Use anchored examples and a stated rubric for visual judgment; record the
reviewer, rationale and uncertainty. Passing contrast, token discipline or a
font-size count cannot be the acceptance criterion for visual craft by itself.
A flow mockup approves transitions; it does not automatically approve the art
direction. If browser/image inspection is unavailable, state that limitation
rather than claiming the rendered result was reviewed.

**Taste is not on that table, and this document will not pretend otherwise.**
These checks catch defects and enforce a system. They cannot tell you whether the
result is *good* — and a director that reports "all gates green" as if it meant
"this is good design" has substituted the measurable half for the whole. Say
which half you checked. Where two directions both pass, that is the moment a
person decides, and the honest output is the pair plus the trade-off, not a
manufactured winner.

---

## Focused visual work

For a bounded request, reuse the existing brief and select the relevant lens
below. These are modes inside this skill, not new global routers or an external
command dependency. Do not repeat direction selection for an already chosen
direction, or run every lens for a single local correction.

| Lens | Question and concrete work | Evidence to keep |
|---|---|---|
| **Type** | List the text roles and the faces/weights actually in use. Improve distinctions between those roles through size, weight, spacing and contrast. Keep a single family when it does the job. Check long labels, the target languages, zoom and fallback fonts. | Representative rendered roles; loaded/fallback font status; the specific reading or hierarchy defect fixed. A font name or a universal line-length target is not a quality verdict. |
| **Composition** | Establish the leading element, supporting elements and meaningful groups. Adjust proximity, rhythm and density to the task. Inspect the relevant supported sizes and content extremes; preserve a sensible reading and focus order. | Before/after of the same state and content; evidence of wrapping, overflow and order. Optical adjustments follow inspection rather than guessed pixel offsets. |
| **State adaptation** | Walk empty, long-content, error, pending, keyboard and recovery states relevant to the scenario. Separate browser prototype behavior from native platform expectations. | State/viewport identifiers, declared versus walked coverage and explicit simulations. No invented latency or claim that a browser preview proves native behavior. |
| **Finish** | Revisit the already identified defects and check what the changes introduced. Keep useful details that were already working. Stop when no actionable finding remains or the agreed budget is reached. | Each previous finding is resolved, partial or unresolved, with current captures and any regressions. The number of edits is not a success metric. |

Before visual review, check that each capture belongs to the expected build,
screen, state, viewport and content. A stale screenshot or one taken before an
overlay opened cannot prove that overlay correct. If the capture cannot be
verified, mark the visual claim unverified and continue only the checks the
available evidence supports.

Judge the render against the brief before reading an explanation of how hard it
was to build. Separate observed defects from preferences and hypotheses. A fresh
reviewer is useful when available and authorized; an explicit separate review
pass by one agent is a valid fallback. Neither requires an external detector,
binary, service, API key, font download or new framework. Reuse local assets and
existing inspection tools; missing inspection remains NOT_RUN.

These local procedures were informed by a comparison of Impeccable's
[type](https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/reference/typeset.md),
[layout](https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/reference/layout.md)
and [finish-review methods](https://github.com/pbakaus/impeccable/blob/4db7f6ba4b6ef661bc8a721261b691b40648c08a/plugin/skills/impeccable/reference/degraded/finish-reviewer.md) (Apache-2.0). They use this family's contracts; no
upstream runtime, assets, fixed style bans or automatic workflow are included.
The links record provenance, not instructions to fetch during every run.

## The output the director owes

One short record, every time, whether the work took ten minutes or a day:

```
Brief      surface / job / constraint / falsifier      (+ scenario id where one exists)
Mode       new | redesign | update | audit             → entered at <lane>
Cast       <skill> — <what for>, per lane              (measured with `pack design`)
Fork       yes → rubric (written first), A: <cast>, B: <cast>, winner + what was grafted
           no  → why not
Alignment  falsifier checked: <result>
Quality    the table above, with numbers
Open       what a person still has to decide
```

**`Open` is not an admission of failure.** It is the line that separates a
director from a generator: the generator returns something finished-looking with
nothing left to decide, and every real design job has something left to decide.
