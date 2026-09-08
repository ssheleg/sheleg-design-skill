# Accessibility evidence — standards, heuristics, and what a check can prove

**Read this when** an accessibility claim is about to be made or checked —
contrast, text size, target size, keyboard, assistive technology. The craft
docs say *readability outranks depth*; this file says what counts as proof.

## A criterion is not a heuristic

A **WCAG criterion** carries a number, a version, a level, units and
exceptions. A **design heuristic** carries a community's taste. Both are worth
holding; quoting one as the other is how a design "passes accessibility"
against a bar nobody can name. Every claim states which it is held to.

| claim | class | the exact bar | the trap |
|---|---|---|---|
| body-text contrast | criterion — WCAG 1.4.3, AA, since 2.0 | 4.5:1 for normal text, 3:1 for **large** text | "large" is defined in **pt, not px**: ≥ 18pt (≈ 24px at 96dpi) or ≥ 14pt bold (≈ 18.66px). 18px normal is 13.5pt — NOT large, needs 4.5:1, so 18px at 3:1 **fails**. 24px normal sits exactly on the 18pt boundary and passes at 3:1 |
| enhanced contrast | criterion — WCAG 1.4.6, AAA | 7:1 normal, 4.5:1 large | AAA is a choice, not "extra credit" — name it when the pack claims it |
| UI/graphic contrast | criterion — WCAG 1.4.11, AA, since 2.1 | 3:1 against adjacent colours | applies to component boundaries and meaningful graphics, not decorative ones |
| target size, minimum | criterion — WCAG 2.5.8, AA, added in 2.2 | **24×24 CSS px**, with spacing/inline/equivalent exceptions | the AA criterion is 24, not 44 |
| target size, enhanced | criterion — WCAG 2.5.5, AAA | **44×44 CSS px** | a 24px target satisfies AA and still fails AAA — the two cases are different claims |
| touch target comfort | heuristic — Apple HIG 44pt, Material 48dp | platform guidance | a design held to the house heuristic says so; "WCAG requires 44px" is false at AA |
| contrast exceptions | part of 1.4.3 itself | logotypes, incidental text, inactive controls | an exception invoked is named, not assumed |

Units matter twice: WCAG sizes are **CSS pixels** (zoom-independent), and text
thresholds are **points** (1pt = 4/3 px at 96dpi). A checker that compares px
against pt thresholds without converting manufactures passes and failures.

## What a screenshot proves

A browser screenshot proves **pixels in one state**: the rendered contrast of
this text on this background, the visible presence of a focus ring in the
state captured. It proves **nothing** about the DOM or assistive technology:
name/role/value (4.1.2), focus order (2.4.3), keyboard reachability (2.1.1),
accessible names, live-region announcements. Those live in the accessibility
tree, and only a tool that reads it — the browser's accessibility pane, an
installed scanner, a screen reader — can testify. A render critique that says
"accessible" from a screenshot has claimed the half it cannot see.

## Verdicts: PASS, FAIL, NOT_RUN

A check runs with the tools **available on this machine**. Where the needed
tool is absent — no DOM access, no assistive technology, no scanner — the
verdict is **NOT_RUN, never PASS**: "looked fine" is a screenshot claim wearing
a criterion's name. NOT_RUN names what it would take to run.

**Never auto-install axe** (or any scanner) to convert a NOT_RUN into a
verdict. Installing tools is the operator's decision; a check that installs
things to complete itself has widened its own permissions mid-run. If axe or
an equivalent is already present, use it and name the version in the receipt.
