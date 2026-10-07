# Knowledge provenance

Where the reviewed knowledge in this pack came from, and the rules that governed
taking it. This file exists because *"we learned it from an open repository"* is
not a licence, not a citation, and not a substitute for saying exactly which
bytes were read and what was done with them. Every adopted method carries its
receipt here: the commit, the source-relative path, the digest of the file
reviewed, a permalink, whether the result is **derived** (a method re-expressed
in our own words) or **adapted** (text carried over), and the date it was
verified.

**The controlling decision (XD-01).** No external assets are transferred into
this pack. Platform guidance (iOS, Android) is **paraphrased from the primary
platform documentation in our own words**, not copied from a third party, until
that third party's MIT notice has been verified and attached — so the rows below
are *evidence a method exists and works*, never instruction authority. Where a
row is `adapted`, text did come across, and its licence notice travels with it
in this file.

## Contents

- Adopted sources
- Transfer rules (apply the moment a row becomes `adapted`)
- Reconciliation with the installed motion tools
- Third-party notices
- What is NOT in the knowledge package

## Adopted sources

| # | Source (commit-pinned) | Path | SHA256 of reviewed file | Kind | Verified | Permalink |
|---|---|---|---|---|---|---|
| 1 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/SKILL.md` | `104661e9af51d84dd3e2d620b83d4fb319e69fbaa3d4b10db32e02f85283286b` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/SKILL.md |
| 2 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/reference/ios.md` | `40c87038b5f75147a5952a96237acf312a327bf70c1bcd8e0a5f064625ae9668` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/ios.md |
| 3 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/reference/android.md` | `058f81f256134841875fd3183e06b37a023de0c877fd2b9eecd97011640791fe` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/android.md |
| 4 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/reference/adapt.native.md` | `17c583cf8ad41266ea1e787b666b9d91fe13469d3d0f6af57c08e0146f9b17ac` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/adapt.native.md |
| 5 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/reference/audit.native.md` | `fe91fcf28638f95577af481a50edaf339d6c9a3ad3b9fa477bc81c116b8bc392` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/audit.native.md |
| 6 | julianoczkowski/designer-skills @ `c259656c76d9758d7ead46b0d2f125cbe84f8665` | `frontend-design/SKILL.md` | `6a078fa3e5a5cef2656d621a90c8dff8191bd9d8a3724df1b98760262c88ef60` | derived | 2026-10-07 | https://github.com/julianoczkowski/designer-skills/blob/c259656c76d9758d7ead46b0d2f125cbe84f8665/frontend-design/SKILL.md |
| 7 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/reference/typeset.md` | `da98692848aa2e9ea22c681522a082f2226cb5dbfdb704ac38903be1b4cffafd` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/typeset.md |
| 8 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/reference/layout.md` | `1d6d2658482b7e2df0c4d27b1b29c5195f0803b402278b96590598f4d3e57aa7` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/layout.md |
| 9 | pbakaus/impeccable @ `12b25ae25848202ce7a9092442198ada5c4fd984` | `plugin/skills/impeccable/reference/degraded/finish-reviewer.md` | `275dd1b6e63bbd30d2713227c4f79b880a8bc4e01cc48d392068bb86939d3afa` | derived | 2026-10-07 | https://github.com/pbakaus/impeccable/blob/12b25ae25848202ce7a9092442198ada5c4fd984/plugin/skills/impeccable/reference/degraded/finish-reviewer.md |
| 10 | emilkowalski/skills @ `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` | `skills/emil-design-eng/SKILL.md` | `ffbe68e6007fb42cb8149f089b400a1ca007d59ba23e8948e2be4476f3175939` | adapted | 2026-10-07 | https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/emil-design-eng/SKILL.md |
| 11 | emilkowalski/skills @ `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` | `skills/review-animations/STANDARDS.md` | `e7d3605034acda54ca13e43aec9e64d65b53de20f75b11b8d694e373012fbe07` | derived | 2026-10-07 | https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/STANDARDS.md |
| 12 | emilkowalski/skills @ `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` | `skills/review-animations/SKILL.md` | `6ff590d29e436766135aa3d137be1fac2a867165c7257fc315b189361f1873af` | derived | 2026-10-07 | https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/review-animations/SKILL.md |
| 13 | emilkowalski/skills @ `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` | `skills/apple-design/SKILL.md` | `77bb63b7043bb93aca2ff4ab040c249484eef35682bb6ff7163433c31d30adc7` | derived | 2026-10-07 | https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/apple-design/SKILL.md |
| 14 | emilkowalski/skills @ `e8a175de22ae1e49370fc144c1f3bb9aeedf988d` | `skills/mobile-native/SKILL.md` | `888b7651d66d66dbac4e72b7c554638eb19bd971d686d6cbdf030a5ef3788f55` | derived | 2026-10-07 | https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/mobile-native/SKILL.md |
| 15 | Leonxlnx/taste-skill @ `e3c92037548e3e49bea8e6b906c99a8549654e71` | `skills/taste-skill/SKILL.md` | `aa194351b246b8b4799099d4ed7b033d29eab6e6e3d58d8d2172978be7b3ec89` | adapted | 2026-10-07 | https://github.com/Leonxlnx/taste-skill/blob/e3c92037548e3e49bea8e6b906c99a8549654e71/skills/taste-skill/SKILL.md |
| 16 | anthropics/skills @ `2235be7c60b551f5de82ade908fd3816455afcda` | `skills/frontend-design/SKILL.md` | `1608ea77fbb6fc30d13a97d12cfa8ebf31358d40f0dd97beed24829d6b3f45dd` | adapted | 2026-10-07 | https://github.com/anthropics/skills/blob/2235be7c60b551f5de82ade908fd3816455afcda/skills/frontend-design/SKILL.md |

Rows 1–6 were first recorded on 2026-09-07 and re-verified on 2026-10-07: rows
1–5 moved from impeccable `4db7f6b` to `12b25ae` (only `SKILL.md` changed bytes;
the four platform references hash the same at both commits), and row 6 hashes
the same as when it was first read. Rows 7–16 were added on 2026-10-07 for
material that was already in this pack without a receipt.

### What each row informed

A row without its destination cannot be checked against the text it claims to
explain, so each one names where it landed.

- **Row 1** — reading a surface by what it is for, and treating an existing
  visual system as evidence rather than a lock: the brief's Surface and Job
  lines and the mode table in [`CREATIVE_DIRECTOR.md`](./CREATIVE_DIRECTOR.md)
  Act 1.
- **Rows 2–5** — context of use beyond one breakpoint and a native branch that
  is captured separately: [`MOBILE_SURFACES.md`](./MOBILE_SURFACES.md) (platform
  target versus prototype renderer, the native state matrix) and the native
  evidence class in [`VISUAL_REVIEW.md`](./VISUAL_REVIEW.md). Impeccable's own
  `NOTICE.md` records that `ios.md` and `android.md` are distilled from
  `ehmo/platform-design-skills` (MIT). Under XD-01 this pack paraphrases the
  primary platform documentation instead, so no text from either reaches it.
- **Row 6** — named aesthetic directions used only as prompts for the open axes
  in [`VISUAL_EXPLORATION.md`](./VISUAL_EXPLORATION.md). **It is not the source
  of the three default looks** in [`SHELEG_DESIGN.md`](./SHELEG_DESIGN.md): that
  file has no `F4F1EA`, no terracotta and no broadsheet (checked 2026-10-07
  against the row's SHA). The paragraph is credited to row 16.
- **Rows 7–9** — the type, layout and finish-review comparison cited in
  `CREATIVE_DIRECTOR.md`, which now links the same commit as these rows.
- **Row 10** — [`MOTION_DOCTRINE.md`](./MOTION_DOCTRINE.md) §1–4: the frequency
  table and the Raycast example, the purpose list, the easing tree, the three
  named curves with their comments, the duration rows (reorganised into the
  `DUR-*` table), the two spring notations and the interruptibility paragraph.
  Close enough to the source to be `adapted`, so its notice is carried below.
- **Rows 11–14** — the reconciliation below: the `scale(0)` and `transition: all`
  bans (rows 11–12), the critically damped default spring (row 13) and the
  hero-versus-app-shell viewport split (row 14). Restated in this pack's words.
- **Row 15** — the three calibration dials in [`SKILL.md`](./SKILL.md): names,
  1–10 poles, the "reading them off the brief" rows and the "do not ask the user
  to edit a file" rule; and in `MOTION_DOCTRINE.md` "motion claimed is motion
  shown", one marquee per page, `start: "top top"` for a pin, and continuous
  input kept out of component state. This pack changed the baseline (`7 / 5 / 4`
  against the source's `8 / 6 / 4`), added the product-UI, trust-first and deck
  rows, required observable anchors, and softened the scroll-listener ban to a
  measured-defect rule. Table rows and sentences remain close, so `adapted`.
- **Row 16** — "Three looks that are defaults, not decisions" in
  `SHELEG_DESIGN.md`, adapted from the "For calibration" paragraph at `2235be7`,
  the version installed when the section was written. At the source's current
  commit (`41bbe19`, checked 2026-10-07) that paragraph lists five traits; the
  two new ones are not adopted here.

**Kind.** *derived* — the method was read and re-expressed in this pack's own
words; no source text was carried over, so no source licence rides on it beyond
attribution. *adapted* — source text was carried over; a row of that kind
additionally requires the transfer rules below. Rows 10, 15 and 16 are of that
kind, and their notices are in [Third-party notices](#third-party-notices).

## Transfer rules (apply the moment a row becomes `adapted`)

1. **Carry the licence with the text.** Transferred text keeps its upstream
   notice — an Apache-2.0 source keeps its `LICENSE` and `NOTICE`, and each
   modified file is marked as modified per §4 of that licence. Text is not
   "ours" because it sits in our tree.
2. **Platform-derived material is verified before it is attached.** For anything
   traceable to a platform vendor, the original **MIT notice is checked and
   attached** before the text is used; until then the knowledge is paraphrased
   from the primary platform docs, not taken from the intermediary.
3. **A source path, a SHA and a permalink, or it is not adopted.** A method with
   no row here has no provenance and does not ship.

## Reconciliation with the installed motion tools

`emilkowalski/skills` at `e8a175d` is installed beside this skill as a set of
tools (`MOTION_DOCTRINE.md` §11, `MOBILE_SURFACES.md`, `VISUAL_REVIEW.md`). Its
doctrine is not copied in further; where its values and this pack's disagreed,
one value was decided per rule on 2026-10-07, and the doctrine states the reason
in place. A row reading *agree* was checked and needed no change.

| Rule | This pack before | The tool says | Decided | Why |
|---|---|---|---|---|
| RC-01 named curves | `0.23,1,0.32,1` · `0.77,0,0.175,1` · `0.32,0.72,0,1` | the same three (rows 10–11) | agree | one source |
| RC-02 `ease-in` on an exit | kept for an element leaving the screen entirely | never on UI; exits ride `ease-out` (row 11) | no exit exception | the doctrine's own tree already sent exits to `ease-out` |
| RC-03 modal and drawer | DUR-SPATIAL 200–300 ms; 500 only as DUR-SHEET-MOBILE | 200–500 ms (rows 10–11) | this pack's rows | the source's 500 contradicts its own under-300 rule |
| RC-04 UI ceiling | at or under 300 ms | under 300; escalate over 300 without a reason (row 12) | agree, 300 passes | both gates fail 301 |
| RC-05 default spring | `duration 0.5, bounce 0.2` preferred | `duration 0.5, bounce 0.2` (row 10); critically damped by default, bounce after a flick (row 13) | `duration 0.4, bounce 0` by default; `bounce 0.2` after a flick or drag release | a default with bounce contradicted "keep it out of most UI" |
| RC-06 `transition: all` | not addressed | first escalation trigger (row 12) | banned in §5 | it animates whatever changes next, layout included |
| RC-07 `scale(0)` | not addressed | never; start from 0.95, band 0.9–0.97 (rows 10–11) | banned in §5; enter from `scale(0.95)` | nothing real appears from a point |
| RC-08 reduced motion | collapse to static or instant | fewer and gentler, not zero; keep opacity and colour (rows 11, 13) | movement collapses; an opacity or colour change carrying state may stay | both remove movement; neither licenses a slower slide |
| RC-09 pure-fade entrance | allowed under reduced motion and where a pack prescribes it | escalation trigger (row 12) | allowed in those two cases | the fade is the reduced-motion answer, not an omission |
| RC-10 full-height viewport | `svh`, with `dvh` behind `@supports` | `100svh` for a hero, `100dvh` for an app shell (row 14) | the tool's split | `dvh` shifts a hero mid-scroll |
| RC-11 typeface | the pack names it | system font by default (row 13) | the pack's face | identity is the pack's; `MOTION_DOCTRINE.md` §8 names the swap as drift |

The installed tool files hash identically to the rows above (checked
2026-10-07 for `emil-design-eng`, `animate`, `animate-expo`, `review-animations`,
`improve-animations`, `find-animation-opportunities`, `animation-vocabulary`,
`apple-design`, `mobile-native` and `break-ui`). A newer tool commit reopens this
table rather than overriding it.

## Third-party notices

Rows 10, 15 and 16 carry source text, so the source's notice travels with it.
Each adapted passage also names its source where it sits: the opening of
`MOTION_DOCTRINE.md`, the dials in `SKILL.md`, the closing note of the
default-looks section in `SHELEG_DESIGN.md`, and the motion section of the
condensed Cursor rule that ships beside this skill.

### emilkowalski/skills (row 10)

```text
MIT License

Copyright (c) 2026 Emil Kowalski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Leonxlnx/taste-skill (row 15)

```text
MIT License

Copyright (c) 2026 Leonxlnx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### anthropics/skills — frontend-design (row 16)

The "three default looks" section of `SHELEG_DESIGN.md` is adapted from
`skills/frontend-design/SKILL.md` in `anthropics/skills` at commit
`2235be7c60b551f5de82ade908fd3816455afcda`, licensed under the Apache License,
Version 2.0. You may obtain a copy of the License at
<http://www.apache.org/licenses/LICENSE-2.0> or read the copy shipped beside the
source at
<https://github.com/anthropics/skills/blob/2235be7c60b551f5de82ade908fd3816455afcda/skills/frontend-design/LICENSE.txt>.
Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. The source carries no
`NOTICE` file. Changes: reworded, restated as a numbered list, and answered with
this pack's rule that values come from a pack.

## What is NOT in the knowledge package

The knowledge package is doctrine and method only. It deliberately excludes:

- **the launcher** — installation machinery is not knowledge;
- **any foreign router or hook** — another pack's control flow is not adopted,
  only observed;
- **any API or font SERVICE** — a runtime dependency is not vendored knowledge;
- **images and fonts** — **no binary asset is vendored.** Cloning a repository
  under its licence does NOT automatically clear the third-party assets inside
  it, and this pack makes no such promise: an asset's own licence is a separate
  question, so assets are referenced by their upstream, never copied in.
