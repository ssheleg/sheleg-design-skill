---
report:
  id: sheleg-design-skill/2026-11-23-ui-guidelines
  title: "Modern interface guidelines 2025-2026 for simple, grouped, novice-friendly screens"
  kind: research
  project: sheleg-design-skill
  domains: [ux, mobile, accessibility, design-systems]
  as_of: 2026-11-23
  status: active
  valid_until: 2027-05-22
  summary: >-
    What current platform guidance and trusted research say about simple, grouped screens with few
    actions for a user who is new to an app but not stupid: one primary action per view, at most
    two disclosure levels, no essential action in overflow, contextual help instead of tutorials,
    target sizes by platform, Liquid Glass only on the control layer, iPadOS 26 windowing, the
    measured gains and caveats of Material 3 Expressive, choice overload limits for browsing
    variants. Thin evidence for music apps is said plainly. Feeds the UI mechanics doctrine
    shipped in sheleg-design, super-ux and task-pipeline.
  sources:
    - {name: "Apple Human Interface Guidelines (Accessibility, Buttons, Toolbars, Tab bars, Layout, Materials, Onboarding, Playing audio)", url: "https://developer.apple.com/design/human-interface-guidelines/", read_at: 2026-11-23}
    - {name: "WWDC25 sessions 219, 356, 208", url: "https://developer.apple.com/videos/play/wwdc2025/208/", read_at: 2026-11-23}
    - {name: "Nielsen Norman Group articles (authors and dates per row in guidelines.md)", url: "https://www.nngroup.com/articles/", read_at: 2026-11-23}
    - {name: "Mobile Tutorials: Wasted Effort or Efficiency Boost? (Alita Kendrick, 2020-03-08)", url: "https://www.nngroup.com/articles/mobile-tutorials/", read_at: 2026-11-23}
    - {name: "W3C WCAG 2.2 Understanding 2.5.8 and 2.5.5", url: "https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html", read_at: 2026-11-23}
    - {name: "Google Material 3 Expressive research and component docs", url: "https://design.google/library/expressive-material-design-google-research", read_at: 2026-11-23}
  produced_by:
    agent: claude-code
    task: "fabric 4cb64120-754f-417d-9f7d-038f989cc91c (operator order via Fabric CEO request dcc725be)"
  supersedes: []
  consumers: [sheleg-design-skill, super-ux, task-pipeline]
---

# Modern interface guidelines 2025-2026 for simple, grouped, novice-friendly screens

The full research, with 61 numbered sources, the 30-row screen checklist and the verified or
UNVERIFIED mark on each source, is [guidelines.md](guidelines.md). This page holds the findings that
changed the design-skills family.

## Main findings

1. **One primary action per view.** Apple tints only the one primary action and keeps toolbars to at
   most three groups (guidelines.md [A3], [A10]). NN/g caps a screen at three type sizes, three contrast
   levels and two large elements ([N1]).
2. **Grouping.** Proximity groups weakly, a common region groups strongly, and decorative containers add
   clutter ([N3], [N4]). Apple pads bezelled controls by about 12 pt and unbezelled ones by about 24 pt ([A1]).
3. **Progressive disclosure, at most two levels.** What users need often belongs on the first layer.
   Essential actions never live in an overflow menu, and menu items do not disappear when inactive
   ([N2], [N20], [A12]).
4. **Novice, not stupid.** In NN/g's 70-user test, tutorials did not raise task success (91% with,
   94% without, p = 0.443) and made tasks feel harder (ease 4.92 against 5.49, p = 0.047) (Alita
   Kendrick, NN/g, 2020-03-08, re-read 2026-11-23). Help belongs in context, in plain words, and undo
   beats confirmation ([N16], [N17], [N9], [N11]).
5. **Targets.** Apple 44 x 44 pt, Material 48 x 48 dp, WCAG 2.2 SC 2.5.8 24 x 24 CSS px (AA) and
   SC 2.5.5 44 x 44 (AAA). Steven Hoober's measurements: the centre of the screen takes about 7 mm,
   corners need about 12 mm; he calls the popular thumb-zone chart wrong ([A1], [G5], [W1], [W2], [O2]).
6. **Liquid Glass belongs on the control layer only.** Never on content, never glass on glass. Clear
   glass needs a dimming layer, and nested corners are concentric. Raluca Budiu (NN/g, October 2025)
   documents legibility and predictability costs ([A6], [A10], [A11], [N20]).
7. **iPadOS 26.** Windows resize freely, every app has a menu bar (ordered by frequency, items never
   hidden), and functions stay the same at every window size ([A12]).
8. **Material 3 Expressive.** Google reports 46 studies with over 18,000 participants and key elements
   found "up to 4x faster". The peer-reviewed CHI 2026 paper measured 33% faster fixation and 20% faster
   tasks with 48 participants. Google's own caveats: a strong minority prefers calmer designs, and
   dropping labels or breaking standard patterns hurt usability ([G1], [G2], [G3]).
9. **Choice.** The jam study (6 against 24 jams, 30% against 3% bought) does not generalise on its own:
   the 2010 meta-analysis found a mean effect near zero, and the 2015 one found a real effect when options
   are complex, the task is hard and people are unsure, which describes novices. For browsing variants:
   mark a recommended default, highlight differences, preview in place, compare side by side for five or
   fewer, and make switching back free ([P1], [P2], [P3]).
10. **Music apps: thin evidence.** No trusted design case studies were found for the consumer music apps
    named in the brief. Rules for performance screens rest on Apple's audio guidance, Logic Pro for iPad,
    the 2025 Apple Design Awards and latency research (the latency figure is UNVERIFIED), and are marked
    as house defaults where they go beyond them ([A8], [A14], [A15]).

## Method

Primary platform documents (Apple HIG through Apple's own data feed, WWDC session pages, Google's
developer documentation and research articles), W3C Understanding documents, NN/g articles with author
and date, and peer-reviewed papers. Generated listicles, content farms and agency blogs were excluded
by rule. Each source is marked V (opened in the session), U (UNVERIFIED) or F (foundational classic).
m3.material.io could not be read as text, so exact Material shape and motion values are UNVERIFIED.

## What it means for the family

The doctrine built on this research (the action map per screen, the disclosure ladder, the novice
persona walk, the target profiles and the iPad layout rules) is recorded in
[doctrine.md](doctrine.md) and lands in the three skill packages as listed there.

## Corrections

None yet.
