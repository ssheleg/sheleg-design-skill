# UI mechanics doctrine (UIM-01 to UIM-34)

Packaged on 2026-11-23 by Claude Fable 5.2 through the Anthropic API (the operator's order for this packaging; two calls, USD 5.45), from the research in [README.md](README.md) and [guidelines.md](guidelines.md) and from a read-only analysis of the three skill packages. Source ids in square brackets resolve in guidelines.md. Two field audits of the operator's own apps fed the amendments; their screens and captures stay in those apps' repositories, so the apps are named here as app D (music creation, dark theme) and app P (learn to play, tools) and their on-screen labels are elided as «…».

Where each rule lives now: UIM-01 to UIM-14, UIM-29 and UIM-31 to UIM-34 in super-ux `scenario-format.md` (the action map, lint U096 to U106) and `templates/test-panel.md` (the novice walk); UIM-15 to UIM-28 in sheleg-design `LAYOUT_CRAFT.md`, `MOBILE_SURFACES.md`, `CREATIVE_DIRECTOR.md` and `ACCESSIBILITY_EVIDENCE.md`; UIM-30 in task-pipeline `design_gate.py` and `agents/design-tester.md`. The sections below are the packaged text as written, with amendments listed after the rules they change; where a shipped file and this text disagree, the shipped file wins and this file gets a correction.


## Read this first: where the shipped text differs (2026-11-23)

The sections below are the packaged drafts. Two blind verification rounds and the first trial run changed the
shipped text; where they differ, the shipped files win:

- **File names.** The draft names its own files (concept.md, rules.md, amendments.md, action-map.md,
  novice-persona.md, ipad-and-controls.md, pipeline-changes.md, trial-protocol.md): each is the section of this
  document with that name.
- **Lint codes.** The shipped linter is super-ux `ux_lint.py` U096 to U106 and its contract table in
  `scenario-format.md`. Differences from the draft table: U099 also fires on an empty `Scenarios:`; U100 also
  fires on a fourth visible exit; U103 reads «More…», its Russian equivalent and «More options» as generic; U104 also fires on a
  visible row with no readable word; U106 spans the screen and lets `hint` and `receipt` rows repeat labels; the
  draft's "an action has two labels" half of U106 is not shipped. Uncounted rows are written as a backticked
  flag or a leading `flag:`.
- **Receipts and tabs.** A receipt is an uncounted row flagged `receipt`, not an exit row as UIM-33 says; tab-bar
  destinations carry the flag `tab`; an icon-only container in a path is named by its glyph.
- **The expert's `slower` check** follows amendment 24 in the shipped test panel: no `every visit` action costs
  more taps, an `often` action at most one more when it moved into a named container, and a `generates`
  preview step is not a slowdown.
- **The metronome example in the action-map section** predates amendments 4 to 6 (one parameter folds up to
  three controls; three chips; depth counts containers only): read the plan in the amendments for the current
  form.
- **Target profiles.** The web value of the standard profile (44 CSS px) is a labelled house level, not FACT;
  WCAG 2.2 SC 2.5.8 is 24 CSS px (sheleg-design `ACCESSIBILITY_EVIDENCE.md`).
- **Line citations** of `MOBILE_SURFACES.md` in the draft predate its new contents list; the numeric-norm rule
  lives in its section *The native state matrix*.
- **Trial findings (first run, app D lyrics-and-beat screen, 2026-11-23).** Linter on the action maps: 18
  findings before, 0 after; counted visible actions 9 before, 5 after. Novice walk (two novices, one expert,
  run blind by the task-pipeline design-tester): find-it 2 of 5 before, 5 of 5 after for both novices; job
  named after only; no expert action got slower. Two rule corrections came out of it: (1) on a rehearse-then-record
  screen both novices tapped Listen first, so test 1.2 passes when the first tap is the scenario's first step,
  not only the primary; (2) on the narrowest phone the two menu buttons lost their chevron and read as tabs, so a
  menu button keeps its menu mark at every width (super-ux contract, *Labels in the map*).

## UI mechanics: the doctrine on two pages

### Stance

1. **Inexperienced, not stupid.** The default user is a capable adult who has not used this app before. They read labels, do not guess hidden gestures, and understand a plain explanation the first time. Plain language is wanted even by experts [N12]. Tutorials do not raise success and make the task feel harder (ease 4.92 with a tutorial against 5.49 without) [N16]. So we make the screen explain itself and never explain the obvious.
2. **Beautiful and simple are one requirement.** Simplification that produces a stock template is a failure, not a safe default. Every screen keeps one signature element (UIM-24).
3. **Keep the exotic that works.** Stressed syllables drawn larger, beat dots that cycle accents and a giant tempo numeral are assets. An unusual element stays when a novice can say what it does from what is visible, and when it has a plain twin for the same action (UIM-25).
4. **Power is tiered, never removed.** There is no "simple mode". Every function stays reachable within two disclosure levels, and gestures remain as accelerators on top of visible controls.

### Backbone: one job, one action map

Every screen has one job (UIM-01) and one action map (see action-map.md). The map lists every action with its label, scenario, frequency, tier, path and target profile. Everything else hangs off it:

- **super-ux** lints the map (U096 to U105).
- **sheleg-design** sizes and groups what the map says is visible.
- **task-pipeline** walks the map as a novice.
- On iPad the menu bar is generated from the map.

A control that is not in the map does not belong on the screen. A scenario step without a row in the map is a missing control.

### The disclosure ladder

| Level | What lives there | Limit |
|---|---|---|
| 0, visible | The primary action and the secondary actions | 5 counted actions per state: 1 primary and up to 4 secondary (UIM-04, HOUSE DEFAULT) |
| 1, one labelled step | A sheet, menu, popover or inspector pane, grouped | Actions used "often" or "rare" |
| 2, a group inside level 1 | Rare actions only | Nothing deeper [N2] |

- "Every visit" actions are always at level 0.
- Nothing on a scenario's main path sits behind a generic "More" [N20].
- Exits (Back, Close, Undo) are always visible and are not counted. Counting them would reward teams for removing Undo.

**Why 5.** No platform source gives a per-screen number, so this is our choice. It is anchored by Apple's three toolbar groups [A3], five default tabs [A4] and Material's two to six actions in a FAB menu [G6c]. The gap analysis proposed 1 plus 3. Both field screens need 4 secondary actions after honest tiering, and a budget that our own best layouts fail would be ignored.

### Control profiles

| Profile | Size (short side of the hit region) | Used for |
|---|---|---|
| Standard | 44 pt (platform fact [A1][A2]) | Everything by default |
| Frequent | 60 pt (HOUSE DEFAULT, about 1 cm [N22]) | The primary action, "every visit" actions, corner targets |
| Performance | 72 pt (HOUSE DEFAULT, about 12 mm [O2]) | Controls used with an instrument in the hands or the device on a stand; at most 3 per screen |

**Small details on a small phone.** Fine detail may be drawn, but it may not be a target. A parameter shows as a compact read-out that opens a large editor. A miniature (a beat strip) is one target that opens the full editor (UIM-21).

### iPad is a first-class layout

- A regular-width frame is owed for every screen of a product that targets iPad.
- It has a second pane (a sidebar or an inspector that shows level 1 already open).
- Controls keep their profile sizes and do not stretch.
- Every function survives any window size [A5][A12].
- The menu bar lists the action map ordered by frequency [A12].

### Browsing variants

For beats, voices, click sounds, versions or another hook:

- One option is marked as recommended or current [N14].
- At most 5 are shown before "Show more".
- A tap previews in place before any commitment [A14].
- Compare 2 at a time on a phone and up to 4 on iPad.
- Going back to the previous choice is one tap and loses no work [N11].

Option count alone does not predict overload [P2]. Complexity and unclear preferences do [P3], and that describes a novice.

### Where the doctrine is checked

| Stage | Who | What |
|---|---|---|
| Screens and flows | super-ux | The action map exists; lint U096 to U105 |
| Design review on frames (pass D) | task-pipeline design-tester | Novice walk: first ten seconds, find it, state. Controls compared with the map |
| Visual craft | sheleg-design | Profiles, spacing, grouping, type budget, materials, signature. iPad frame owed |
| Code audit | super-ux ux-audit | Every map row is wired; no control exists outside the map |
| Design review on the build (pass B) | task-pipeline | The same novice walk over the running build |
| Visual verifier | task-pipeline, reading sheleg-design's sheet | Measured targets; Anchor and Signature recorded on `product` screens |

### What we deliberately do not adopt

- **Forced tutorials and feature tours** [N16][N17]. We use hints next to the control, shown at the moment of use.
- **Glass on content, glass on glass, tint on everything** [A6][A10]. NN/g's legibility critique of Liquid Glass stands [N20].
- **Removing labels for a clean look.** Google's own tests lost usability when labels went [G1]. Label-less controls hide affordances [N20].
- **The thumb-zone chart as a layout law.** Hoober calls it incorrect: people reach the whole screen, and accuracy drops in corners [O2].
- **Miller's seven as a menu cap** [N5], and "fewer options is always better" from the jam study [P1][P2].
- **Confirmation dialogs as a safety habit** [N9]. We build undo.
- **Controls that change size and place while in use** [N20], and motion for its own sake.
- **"Up to" marketing figures for Material 3 Expressive as targets** [G1]. We take the one finding that replicates in the CHI paper [G2]: emphasise the key action.
- **NN/g's three type sizes taken literally** [N1]. We allow three plus one display size, because the signature often is the display size.
- **The density dial's 6 to 8 for consumer screens with novices.** LAYOUT_CRAFT moves these to the trust-first band.

### Where the research is thin

No trusted design research exists for music apps (research section 8). These are house defaults, to be measured in the trial (trial-protocol.md, step 7):

- the performance profile (72 pt);
- the cap of 3 performance controls;
- the lyrics-plus-transport recipe.

The 10 ms latency target is UNVERIFIED [P7] and is not doctrine yet.

## UIM rule catalogue

**Reading the thresholds.** FACT means a platform or research source states the number. HOUSE DEFAULT means it is our choice and revisable after the trial.

**Point-to-millimetre conversions** use roughly 0.16 mm per point on current iPhones. This is house arithmetic that is not in the research set. Verify it before it is written as normative (MOBILE_SURFACES.md (section The native state matrix)).

**What the reviewer holds.** The reviewer has the screen captures (one per state, plus any open sheet or menu), the scenario list and the action map. Captures are read at 1x point scale.

### A. Job and actions (super-ux)

**UIM-01 One job per screen**
- Rule: A screen serves exactly one job, written as one verb phrase with one job id.
- Check: Does `Purpose` name one job id, and can every scenario in the screen's list be read as a way of doing that job?
- Threshold: 1 job. A second job gets its own screen, or its entry moves to the hidden tier. HOUSE DEFAULT, built on the pack's IS-01.
- Owner: super-ux. Sources: [N2][A5]. Applies to: all screens.

**UIM-02 One primary action per state**
- Rule: Each screen state has exactly one primary action. It serves the job, is not destructive and is not a rare action.
- Check: In the map, does each state have exactly one row with tier `primary`, with frequency `every visit` or `often`, and without the `irreversible` flag?
- Threshold: Exactly 1. FACT [A3][A2].
- Owner: super-ux. Sources: [A3][A2][G6e]. Applies to: all screens.

**UIM-03 Every action is mapped, both ways**
- Rule: Every control on the screen has a row with a scenario id (or `exit`). Every action a scenario step needs on this screen has a row.
- Check: Is there a row for each control visible on the capture? Is there a row for each scenario step that happens on this screen?
- Threshold: 0 unmapped controls, 0 missing rows.
- Owner: super-ux. Sources: [N2][N13]. Applies to: all screens.

**UIM-04 Visible action budget**
- Rule: A screen state shows at most 5 counted actions in its main pane: 1 primary and up to 4 secondary. Exits, tab destinations and status banners are not counted (see action-map.md).
- Check: Following the counting rules, is the number of counted visible rows 5 or fewer?
- Threshold: 5. HOUSE DEFAULT. Anchors: 3 toolbar groups [A3], 5 tabs [A4], 2 to 6 FAB menu actions [G6c], cost of every extra option [N13].
- Owner: super-ux. Sources: [A3][A4][G6c][N13]. Applies to: all screens.

**UIM-05 Tier follows frequency, depth at most 2**
- Rule: `every visit` actions are visible. `often` actions are visible or one step away. `rare` actions are one or two steps away. Nothing is deeper.
- Check: For each row, does the number of containers in `Reached by` fit its frequency, and is it never more than 2?
- Threshold: Depth 0 / 0 to 1 / 1 to 2. Maximum 2 is FACT [N2]. The frequency mapping is HOUSE DEFAULT.
- Owner: super-ux. Sources: [N2][A3]. Applies to: all screens.

**UIM-06 Nothing essential in a generic overflow; menus are grouped and stable**
- Rule: No main-path step of a scenario goes through a container labelled only "More" or an ellipsis. A menu or sheet with more than 5 items is split into labelled groups. Inactive items are dimmed in place, not removed.
- Check: Does any main-path row have "More" in its path? In the open-menu capture, is every run of items longer than 5 broken by a group label? Do the active and inactive captures list the same items?
- Threshold: 0 main-path rows behind a generic overflow [N20]. Groups of 5 or fewer are HOUSE DEFAULT. Stable items are FACT [A12].
- Owner: super-ux. Sources: [N20][A3][A12][N3]. Applies to: all screens.

**UIM-07 No gesture-only and no drag-only feature**
- Rule: Every long press, double tap, swipe, pinch or drag has a visible control that does the same thing. Gestures stay as accelerators.
- Check: Does any row list a gesture as its only path? Does every slider, knob, scrub or reorder show a tap alternative (steps, plus and minus, typed value)?
- Threshold: 0 gesture-only rows. FACT for dragging (WCAG 2.2 SC 2.5.7) [W3]. Other gestures are HOUSE DEFAULT, which makes the pack's BP-051 enforceable.
- Owner: super-ux. Sources: [W3][N6]. Applies to: all screens.

### B. Words and state (super-ux)

**UIM-08 A label, or a glyph everyone knows**
- Rule: A control is icon-only only when its glyph is in the allowed set. Every other control carries a visible text label. A badge or dot on a control is explained by words on the same screen.
- Allowed set: back chevron, close X, play, pause, plus (add), minus and plus around a visible value, search, the platform share glyph, trash, gear, ellipsis (More), and the undo and redo arrows as a pair.
- Further limits: A stop square is allowed only next to a state label. A record dot is never alone.
- Check: Is every icon-only control on the capture in the set? Does every dot or badge have a text explanation on the screen?
- Threshold: 0 unlabelled glyphs outside the set. The set is HOUSE DEFAULT; no source lists one.
- Resolving Back and Close: Apple prefers the standard symbols for these [A3], while NN/g asks for text [N11][N20]. We use the system Back and keep the screen title visible.
- Owner: super-ux. Sources: [G1][N11][N20][A3]. Applies to: all screens.

**UIM-09 Running state is unmistakable**
- Rule: While recording or playback runs, the screen shows a text state label with elapsed time or a level meter. The control that started it has become the stop control in the same place. The state stays visible on every screen until it ends.
- Check: On a greyscale copy of the running capture, can the reviewer tell what is running and which control stops it? Is the state label present on captures of other screens taken while it runs?
- Threshold: Text plus a shape change, never colour alone or sound alone. FACT [N24][A8].
- Owner: super-ux. Sources: [N24][A8][A4][A11]. Applies to: all screens with record or play.

**UIM-10 Undo over confirm**
- Rule: Routine edits are undoable and never confirmed. A confirmation appears only for an action flagged `irreversible`. It states the consequence and labels its buttons with the outcome.
- Check: Does a confirmation capture exist for any row without the `irreversible` flag? On a screen with edit actions, is an Undo exit row visible after an edit?
- Threshold: 0 confirmations on reversible actions. FACT [N9]. Undo stays available until the user leaves the screen: HOUSE DEFAULT.
- Owner: super-ux. Sources: [N9][N11]. Applies to: all screens.

**UIM-11 Help in context, no forced tutorial**
- Rule: No tour or overlay blocks the screen on first run. A hint sits next to the control it explains, can be dismissed and can be called up again.
- Check: In the first-run capture, are the screen's own controls uncovered and usable? Is at most one hint visible?
- Threshold: 0 blocking overlays. FACT [N16][N17][A7]. One hint per state is HOUSE DEFAULT. The onboarding budget stays where it is (U082 to U084, ADA R2).
- Owner: super-ux. Sources: [N16][N17][A7][N15]. Applies to: all screens.

**UIM-12 Empty, loading and error states carry status, reason and next step**
- Rule: Each of the three states says what is happening and why, and offers one next action. No blame words. No "empty" message while still loading.
- Check: Does each state capture contain a status line, a reason and exactly one offered action? Does a wait longer than 10 seconds show progress?
- Threshold: 3 parts per state [N7]. Progress after 10 s is FACT [N23]. No "invalid", "illegal" or "incorrect" [N18].
- Owner: super-ux. Sources: [N7][N18][N23]. Applies to: all screens.

### C. Variants (super-ux)

**UIM-13 Variants start from a recommended default and a short set**
- Rule: A choice among alternatives marks one option as recommended or current. It shows at most 5 before "Show more". Every option uses the same layout, with the differences visible.
- Check: Is exactly one option marked? Are 5 or fewer shown before a "Show more" control? Do all options share one layout?
- Threshold: 1 marked option [N14]. 5 is HOUSE DEFAULT, taken from the static comparison limit in [N25].
- Owner: super-ux. Sources: [N14][P3][N25][O4]. Applies to: screens with a `variants` row.

**UIM-14 Preview in place, compare a few, go back for free**
- Rule: Sensory options (sound, voice, look, text version) are previewed with a tap before any commitment. Comparison is 2 at a time on compact width and up to 4 on regular width. The previous choice is restored in one tap with no work lost.
- Check: Does each option show a preview control separate from "Use"? After choosing B, is A still listed and selectable?
- Threshold: Compare 2 (compact) or 4 (regular): HOUSE DEFAULT, under the ceiling of 5 in [N25]. Switch back in 1 tap: HOUSE DEFAULT.
- Owner: super-ux. Sources: [A14][N25][O4][N11]. Applies to: screens with a `variants` row.

### D. Look (sheleg-design)

**UIM-15 The primary is the only dominant control**
- Rule: Exactly one control carries primary emphasis (fill or tint), and it is the map's primary row. Preference is marked by style. No other control is tinted.
- Check: After a 4 px blur, is there one dominant control, and is it the map's primary? Is any other control filled or tinted with the accent?
- Threshold: 1 emphasised control. FACT [A3][A10]. Style over size is FACT [A2].
- Owner: sheleg-design. Sources: [A2][A3][A10][N1][G2]. Applies to: all screens.

**UIM-16 Group by proximity, cap the groups**
- Rule: Related controls sit closer to each other than to anything else. A container is used only where spacing fails.
- Check: Can the reviewer draw at most 5 boxes on the capture that hold every element, with every gap between boxes at least twice the largest gap inside one? Does text keep at least 16 pt from the screen edge?
- Thresholds:
  - Groups per viewport: 5 on compact width, bars included; 7 on regular width. HOUSE DEFAULT.
  - Toolbar groups: 3. FACT [A3].
  - A text button is never grouped with an icon. FACT [A11].
  - Gap ratio 2x: HOUSE DEFAULT.
  - Content inset: 16 pt compact, 24 pt regular. HOUSE DEFAULT.
- Owner: sheleg-design. Sources: [N3][N4][A5][A3][A11]. Applies to: all screens.

**UIM-17 Type and emphasis budget**
- Rule: A screen uses at most 3 text sizes plus 1 display size, 3 emphasis levels and 2 big elements. Text the user must read to act is large enough and has enough contrast.
- Check: Count the distinct text sizes, the emphasis levels and the big elements. Measure the smallest action label and the smallest text. Sample text contrast in light and dark captures.
- Thresholds:
  - 3 emphasis levels and 2 big elements: FACT [N1].
  - 3 sizes plus 1 display size: HOUSE DEFAULT. [N1] says 3; the fourth is reserved for one element.
  - Labels, read-outs and state text at least 13 pt; no text under 11 pt: HOUSE DEFAULT at the default text size.
  - Contrast 4.5:1: FACT [A1].
- The product-wide scale stays under ADA R9.
- Owner: sheleg-design. Sources: [N1][A1][N20]. Applies to: all screens.

**UIM-18 Target profiles**
- Rule: Every target meets its profile, measured on the short side of the hit region. The primary is the largest target on the screen.

| Profile | iOS | Android | Web | Status | Who gets it |
|---|---|---|---|---|---|
| Standard | 44 pt | 48 dp | 44 CSS px for visible tiers; hidden tier may use 24 CSS px with spacing | FACT [A1][A2][G5][W1][W2] | Default |
| Frequent | 60 pt | 64 dp | 60 CSS px | HOUSE DEFAULT, about 1 cm [N22] | Primary, `every visit` rows, corner targets, editor controls |
| Performance | 72 pt | 76 dp | 72 CSS px | HOUSE DEFAULT, about 12 mm [O2] | Controls used while playing or singing; at most 3 per screen |

- Check: Can a square of the profile size be centred on each target without leaving the screen? Is the primary the largest target by area? Are there 3 or fewer performance rows?
- Verdict on app P's 60 and 44:
  - 44 pt for other controls is right. It is the platform figure.
  - 60 pt is not a bonus for playing. It is about 1 cm, which NN/g gives as the general physical floor for any touch target [N22]. It becomes our frequent profile.
  - Controls used with an instrument in the hands move to 72 pt. That is the size Hoober found necessary where accuracy is worst [O2]. We use it as a stand-in for degraded aim, because no source measures instrument-in-hands use. The trial measures 60 against 72.
- Owner: sheleg-design. Sources: [A1][A2][G5][W1][W2][N22][O2]. Applies to: all screens; the performance row applies to performance screens.

**UIM-19 Space between targets**
- Rule: Profile squares of neighbouring targets never overlap. Bezelled neighbours keep a visible gap, and a destructive control keeps its distance from frequent ones.
- Check: Do any two profile squares overlap? Is the visible gap between bezelled neighbours at least 12 pt (16 pt for performance targets)? Is every destructive control at least 24 pt from any frequent or performance target?
- Thresholds:
  - 12 pt around bezelled and 24 pt around unbezelled elements: FACT [A1].
  - 16 pt for performance and 24 pt for destructive: HOUSE DEFAULT.
  - Segments of one connected control are exempt from the gap, not from the size [G6a].
  - Web floor: the 24 px circle test [W1].
- Owner: sheleg-design. Sources: [A1][N22][W1][G6a]. Applies to: all screens.

**UIM-20 Reach: centre and bottom first, corners cost more**
- Rule: On compact width the primary sits in the lower half. No primary or `every visit` action sits in a top corner. A counted action in any corner takes the frequent profile.
- Check: Is the primary's centre below the vertical midpoint? Is the outermost control at either end of the top bar an exit or a non-`every visit` action? Do corner actions pass the 60 pt square?
- Threshold: HOUSE DEFAULT, derived from [O2].
- Note on Hoober: the thumb-zone chart is not a reason to hide or remove top controls. People reach the whole screen; they are simply less accurate at the edges [O2]. The pack's BP-049 wording "thumb zone" is replaced by a link to this rule.
- Owner: sheleg-design. Sources: [O2][N22]. Applies to: all screens, compact width.

**UIM-21 Read-out opens editor; a miniature is one target**
- Rule: A parameter not changed during the screen's main activity is shown as a compact read-out with its current value. Tapping it opens a large editor. Detail finer than a target may be drawn, but the whole miniature is one target.
- Check: Does each read-out show a value in text of 13 pt or more and pass the 44 pt square? In the editor capture, does every control pass the 60 pt square? Is any sub-part of a miniature a separate target under 44 pt?
- Threshold: Read-out 44 pt, editor controls 60 pt: HOUSE DEFAULT on top of [A1]. Reducing the element count is what lets key targets be large [N22].
- Owner: sheleg-design. Sources: [N22][N2][A1][O5]. Applies to: all screens.

**UIM-22 Translucent material stays on the control layer**
- Rule: Glass or any translucent material appears only on bars and floating controls. It never appears on content or on other glass. The clear variant is used only over media with a dimming layer.
- Check: Is any content row, card or text block translucent? Does any translucent element sit on another? Does text on material reach 4.5:1 in the light and dark captures and in the Reduce Transparency capture?
- Threshold: 0 glass on content, 0 glass on glass. FACT [A6][A10]. Contrast 4.5:1 [A1].
- Owner: sheleg-design. Sources: [A6][A10][A11][N20]. Applies to: all screens.

**UIM-23 Expressive emphasis on one thing; controls hold still**
- Rule: Oversize, special shape or spring motion is spent on the primary action and the signature element. Persistent controls keep their frame between states. Money, health and settings screens use the calm variant.
- Check: Overlaying the captures of two states, does every persistent control keep its position and size? Besides the primary and the signature, does any element carry a non-standard shape or scale?
- Threshold: 0 moved controls [N20]. Emphasis limited to 2 elements: HOUSE DEFAULT, matching the 2 big elements of UIM-17. Motion respects Reduce Motion [A10][G7].
- Owner: sheleg-design. Sources: [G1][G2][G3][N20][A10]. Applies to: all screens.

**UIM-24 The signature element survives**
- Rule: Every screen has one element that a stock template for that screen type would not have, tied to the screen's job. No simplification removes it.
- Check: Can the reviewer point to one such element on the capture? In a before and after pair, is it still there?
- Threshold: Exactly 1 per screen. HOUSE DEFAULT. It may be one of the 2 big elements. This brings the idea of ADA R21 to `product` screens.
- Owner: sheleg-design. Sources: [G1][G3][N1]. Applies to: all screens.

**UIM-25 Unusual controls are allowed with proof**
- Rule: A non-standard control stays when the novice walk predicts what it does from visible evidence (its label or one hint line), and a standard control for the same action exists in the map.
- Check: Does the walk record a correct prediction for the control, citing on-screen text? Does the map show a standard path for the same action?
- Threshold: Both conditions. HOUSE DEFAULT. Google's losses came from breaking patterns without such a twin [G1].
- Owner: sheleg-design. Sources: [G1][N6][W3]. Applies to: all screens.

### E. Tablet (sheleg-design, one rule in super-ux)

**UIM-26 Regular width has a second pane**
- Rule: At regular width the screen shows a sidebar, a second column or an inspector. The inspector shows level 1 of the disclosure ladder already open.
- Check: Does the regular-width capture show at least two panes? Does the secondary pane hold only rows that are `hidden` in the compact map, in labelled groups?
- Threshold: 2 or more panes. The layout decision by size class is FACT [A5][A12]. The inspector-equals-level-1 mapping is HOUSE DEFAULT. Pane rows do not count against UIM-04.
- Owner: sheleg-design. Sources: [A5][A12][A14]. Applies to: tablet.

**UIM-27 Controls keep their size and do not stretch**
- Rule: Wider screens get more panes and more visible content, not wider buttons. Profiles stay the same.
- Check: Is any button or stepper wider than 400 pt? Is any text column wider than 680 pt? Does every target still pass its profile square?
- Threshold: 400 pt and 680 pt: HOUSE DEFAULT. Timelines, sliders, waveforms and media may span the pane.
- Owner: sheleg-design. Sources: [A5][A11]. Applies to: tablet.

**UIM-28 Any window size keeps every function**
- Rule: The smallest and the largest window show the same map. A compact-width window uses the phone layout. Resizing back restores the layout.
- Check: Comparing the smallest and largest captures, is every map row reachable in both? After a resize round trip, does the capture match the original?
- Threshold: 0 lost rows. FACT [A5][A12].
- Owner: sheleg-design. Sources: [A5][A12]. Applies to: tablet.

**UIM-29 The menu bar mirrors the action map**
- Rule: On iPadOS every map row appears as a menu command, ordered by frequency. Commands stay in place when inactive.
- Check: In the menu captures, is there a command for each row? Do `every visit` rows come before `rare` ones? Are inactive commands dimmed, not missing?
- Threshold: Full coverage. FACT [A12].
- Owner: super-ux. Sources: [A12]. Applies to: tablet.

### F. Pipeline (task-pipeline)

**UIM-30 The novice walk passes**
- Rule: Every screen in scope is walked by each novice portrait with three tests (first ten seconds, find it, state). Every answer cites visible evidence.
- Check: Does the review hold one row per novice portrait for this screen? In each row, did the novice name the job, pick the primary first, predict every counted visible action, find every secondary action on the first tap and every hidden one with at most one wrong container, and answer the state questions?
- Threshold: All tests pass for both novices. HOUSE DEFAULT. The panel holds at least 2 novices and 1 expert out of 10.
- Owner: task-pipeline. Sources: [N15][N16][N6][N24]. Applies to: all screens.

## Amendments after the two audits

### Corrections to earlier files

| # | Rule or file | Change | Reason |
|---|---|---|---|
| 1 | action-map.md, counting | Add rule 9: placing a cursor or playhead by tapping the content itself is not counted. It still needs a row, visible evidence in words and a full-size alternative. | app D SCR-78: lyric lines and the strip (misfire A-1) |
| 2 | action-map.md, counting | Add rule 10: a transient recovery chip (return to the current position) and a receipt line are not counted. | app D «…»; UIM-33 |
| 3 | action-map.md, counting | Add rule 11: a hint or message is not counted when each of its buttons repeats an existing row or dismisses; at most 2 buttons, none filled. | app D manager message |
| 4 | action-map.md, column "Action" | "Several controls for one parameter are one action" gains a cap: at most 3 controls plus the value itself (HOUSE DEFAULT). | app P tempo (misfire B-1). Without a cap, folding could hide a wall of controls |
| 5 | action-map.md, metronome example | "Set tempo by tapping" folds into "Change tempo". The single read-out becomes three chips; the lamp strip joins the meter chip as one action. Before count: 8 today and 15 after the next build (was 9 and 12). | Consistency with row 4 and with the measured screen |
| 6 | action-map.md, "Reached by" | Depth counts containers that must be opened. A group heading inside an open container is not a container. A segment or "Show more" that hides options is one. The example's "maximum depth 1" stands on this reading. | The example listed group names in paths |
| 7 | action-map.md, flags | Add `generates` (a model creates or replaces content) and `spends` (uses quota, money, a take or a generation). | Needed by UIM-14, UIM-32, UIM-33 |
| 8 | action-map.md, lint | Add U106 (W on format 1, E on format 2): `U106 {SCR}: label "{label}" names two actions, or action "{action}" has two labels.` | app P «…»; app D F4 |
| 9 | UIM-05 | Add the mapping of loose frequency words to the three values, as in trial-protocol-plans.md. | Both audits used five or more frequency words |
| 10 | UIM-08 | Add: (a) a single letter or abbreviation is a glyph, not a label; (b) a portrait needs a visible word; (c) within one screen a word names one action and an action has one label (U106); (d) decorative dots that resemble «⋯» are not allowed. | app D «M» / «S» and the avatar; app P «…» and the three quota dots |
| 11 | UIM-09 | A count-in is a running state. Its text and countdown are never truncated, and it never covers the position display. | app D `(capture)` |
| 12 | UIM-10 | The Undo clause applies to edits of the user's work. A parameter restored by its own control needs no Undo row. Stopping a running job is labelled as stop, never as undo. | Misfire B-2; app D F4 («…» with three meanings) |
| 13 | UIM-12 | Add: a disabled control states its reason in one line or is not shown. | app D F7 |
| 14 | UIM-13 | A choice tile that plays shows a playing state. Add: when the next option is off-screen, part of it is visible. | app D F10; app P carousel peek |
| 15 | UIM-14 | Add: a row flagged `generates` returns 2 or 3 candidates plus the unchanged work marked as current (HOUSE DEFAULT). The work does not change before "Use". | app D F2, F10; the owner's wave-3 order |
| 16 | UIM-15 | Add: a state mark inside content or a display (current line, current beat, selected item) may use an accent. A colour reserved for a state (recording, error) appears on nothing else. | Misfires A-5, B-4; app P red lamp |
| 17 | UIM-16 | Add: no content rests under a pinned control. The scroll area is inset by the pinned height, and when more content exists a cut item or an edge shows it. Check: at the end of scroll, is the last item fully above the pinned bar? | app D F9; app P finding 3 |
| 18 | UIM-17 | Size variation inside the signature element counts as the one display size. | Misfire A-3 |
| 19 | UIM-18 | (a) The cap of 3 counts performance rows; one row may hold up to 3 controls. (b) New class "position target" for lines of text and timeline cells: at least 24 pt high (the web floor [W1], used here as a HOUSE DEFAULT on touch), allowed only when a miss changes nothing in the work and a 44 pt path to the same place exists. | Wording in concept.md said "controls"; misfire A-2 |
| 20 | UIM-21 | Add: a row of more than 6 repeating items on compact width is a miniature (7 by 60 pt exceeds 370 pt). | app P 7/8 and 12/8 lamps |
| 21 | ipad-and-controls.md, recipe 1 | Lamp strip as one target; three two-line chips under it (name over value); state line above Start; nothing scrolls. On iPad the inspector sections replace the chips. | app P plan B |
| 22 | ipad-and-controls.md, recipe 2 | Replace "Ideas" and "More" in the top bar with menus named after the object they change, in the bottom row beside the transport. No generic "More" at all. Add the status slot and the candidate tray. The strip is a seek target with no "Beat" button on it. | The owner's two menus are better than our recipe: the words are shorter, the split is the user's own (text or beat), and both sit in the lower half |
| 23 | trial-protocol.md, S7 and rule 1 | "Must equal the before total" becomes "no fewer than before; moved or dropped functions are listed with the reason". | app D restores two functions and moves one |
| 24 | trial-protocol.md, rule 4; novice-persona.md, finding `slower` | No `every visit` action costs more taps. An `often` action may cost 1 more when it moved into a named container. The preview step of a `generates` row is not a slowdown. | Misfires A-4, B-3. The old rule contradicted UIM-05 and UIM-14 |
| 25 | trial-protocol.md, hands test | Add the iPad arm: 72 against 80 pt on a stand. | app P audit finding 10 |
| 26 | pipeline-changes.md, T4 | `Anchor` and `Signature` are owed when the project has a director record. Without one, the gate warns and asks for screen-level lines. | app D has no record yet (misfire A-6) |
| 27 | pipeline-changes.md, catalogue homes | UIM-31 to UIM-34 live in super-ux (`scenario-format.md` and `component-guidelines.md`). | New rules below |
| 28 | concept.md, "Why 5" | Add: both field screens land on exactly 5 after counting rules 9 to 11 and the parameter cap. The budget held; the counting needed sharpening. | Trial evidence so far |

### New rules

All four are needed: each fails on at least one of the two audited screens today, and none is covered by UIM-01 to UIM-30. Field evidence is cited by audit and section, next to the research ids.

**UIM-31 Words before count**
- Rule: When labelled controls do not fit with their words, fewer controls are shown (the rest go into a named menu). A control never keeps its place by losing its label.
- Check: On the capture at the smallest supported width, and on the capture at the largest standard text size, does every control whose map label is text still show that text in full? If a row wrapped or a menu appeared instead, pass. If a word became an icon or was cut, fail.
- Threshold: 0 labels dropped or truncated on those two captures. Glyphs in the UIM-08 set may drop an accompanying word. At accessibility sizes a row may wrap to two rows. HOUSE DEFAULT.
- Sources: [G1][N20]; field: app D audit F2 and pattern 12.
- Owner: super-ux. Applies to: all screens.

**UIM-32 Consequence line**
- Rule: An option that changes the work or spends something says so in one plain line under its label. A primary whose tap spends something says what, in one line above it. A disabled control shows its reason in the same place.
- Check: In the open-menu or choice capture, does every row flagged `generates`, `spends`, `irreversible` or `variants` show a second line stating what changes or what is kept? If the primary's row is flagged `spends`, is there a line above it naming what the tap uses? Does every dimmed control show a reason?
- Threshold: 1 line, at most 60 characters, 13 pt or more, shown before the tap. HOUSE DEFAULT.
- Sources: [N12][N7][N9]; field: app D patterns 4 and 6, F7; app P section 5 («…»).
- Owner: super-ux. Applies to: all screens with flagged rows.

**UIM-33 One change, one receipt, one undo**
- Rule: After any change made from a menu, a sheet, the agent or a `generates` row, a receipt line says in words what changed and offers Undo in words. One Undo restores the whole change, however many parts it had.
- Check: Does the capture taken right after the change show a line naming the change, with a worded Undo control of at least 44 pt? Does the capture after that Undo equal the capture before the change?
- Threshold: 1 receipt and 1 undo step per change. The receipt stays 8 s or until the next action. Standard Undo keeps working after it fades. HOUSE DEFAULT. The receipt is an exit row and is not counted.
- Sources: [N9][N11][N24]; field: app D pattern 3, F2; the app D audit's 8 s proposal.
- Owner: super-ux. Applies to: screens with edit or `generates` rows.

**UIM-34 Now and Next**
- Rule: On a screen whose content advances in time, exactly one item is marked as current in every state, rest included. The next item is visible. A coming change is counted down in the unit the user performs in.
- Check: On the rest capture, is exactly one item marked as the place where things will start? On the running capture, is the current item marked by more than colour and the next one visible? Before a count-in ends, or a tempo or section changes, is there a countdown in beats, bars or lines? Does the screen show more than one beat display or more than one position display?
- Threshold: Exactly 1 current mark, 1 beat display and 1 position display per screen. Countdown in beats, bars or lines, not seconds. A moving syllable or playhead marker counts as the countdown for continuous text. HOUSE DEFAULT. The look of the mark is sheleg-design's, under UIM-17.
- Sources: [N24][A8]; field: app D F3; app P section 5 («…» / «…», «…») and finding 7 (time shown five ways).
- Owner: super-ux. Applies to: screens with playback, recording, a count-in, a trainer or timed steps.

### Considered and not added

- **"Performance state shows one control alone"** (app D pattern 5). Covered by UIM-04 per state and UIM-18. Re-open it if the trial shows clutter during takes.
- **"Hold to compare with the original"** (app D pattern 2). An allowed accelerator under UIM-14. As the only path it would fail UIM-07, so the tap twin is owed.
- **"One name per concept across the app"** (app D F4, app P finding 4). The single-screen half is now UIM-08 clause (c) with U106. The cross-screen half needs the whole registry, so it stays with the terminology file and super-ux's audit, not with a per-screen rule.

## The action map (owned by super-ux)

The action map replaces the free-text `Elements:` line in a `screens.md` entry. `Elements:` is read as a legacy alias for one release.

### Format

```
#### SCR-07 Metronome
Purpose: Keep time at a chosen tempo (JTBD-03)
Scenarios: SCN-21, SCN-22, SCN-23
Actions:
State: idle            (repeat the table per state only when the visible set differs)
| Action | Label or glyph | What it does | Scenario | Frequency | Tier | Reached by | Profile |
```

| Column | Allowed content |
|---|---|
| Action | A verb phrase, unique on the screen. Several controls for one parameter are one action (minus and plus are "Change tempo"). |
| Label or glyph | The exact on-screen text in quotes, or `glyph:<name>` from the UIM-08 set, or both. |
| What it does | The outcome in one clause. Flags: `irreversible` (cannot be undone), `variants` (opens a choice among alternatives). |
| Scenario | One or more `SCN-` ids, or the literal `exit` for Back, Close, Cancel, Undo and Redo. |
| Frequency | `every visit`, `often` or `rare`, followed by `(data)` or `(assumed)`. Frequency comes from task analysis or usage, not opinion [N2]. |
| Tier | `primary`, `secondary` or `hidden`. |
| Reached by | `visible`, or a path of quoted labels such as `"Rhythm and sound" > "Meter"`. Depth is the number of containers in the path. Accelerators follow `also:` (for example `also: long press`). |
| Profile | `standard`, `frequent` or `performance` (UIM-18). |

### How to count visible actions (UIM-04)

1. Take one state. List the rows with tier `primary` or `secondary`.
2. Remove rows whose scenario is `exit`. At most 3 exit controls may be visible: Back or Close, Undo, Redo.
3. Remove tab bar destinations. They are navigation, capped at 5 by their own rule [A4].
4. A repeating collection counts once per kind of action ("Open song"), not once per item.
5. A status banner with one recovery action is a state (UIM-12) and is not counted.
6. A disclosure entry ("More", or a named read-out that opens a sheet) is one secondary action.
7. A regular-width inspector pane shows `hidden` rows open. They stay `hidden` and are not counted.
8. The result must be 5 or fewer, with exactly one `primary`.

### Lint checks

Severity is W on format 1 and E on format 2.

| Code | Fires when | Message |
|---|---|---|
| U096 | `Purpose` is missing, has no job id, or has more than one | `U096 {SCR}: Purpose must name exactly one job (one verb phrase, one ST- or JTBD- id); found {n}.` |
| U097 | A state has zero or several primary rows, or the primary is `rare` or `irreversible` | `U097 {SCR} state {state}: expected exactly one primary action that is not rare and not irreversible; found {detail}.` |
| U098 | A row has no scenario id and is not `exit` | `U098 {SCR}: action "{action}" serves no scenario; give it a SCN- id, mark it exit, or remove it.` |
| U099 | A scenario's UI element on this screen has no row, or `Scenarios:` is empty | `U099 {SCR}: scenario {SCN} uses "{element}" which is not in the action map.` |
| U100 | Counted visible actions exceed 5 | `U100 {SCR} state {state}: {n} visible actions, budget is 5; move the least frequent to the hidden tier.` |
| U101 | Tier or depth does not fit frequency, or depth is over 2 | `U101 {SCR}: "{action}" is {frequency} but sits at depth {d}; allowed depth is {range}.` |
| U102 | A row is reached only by a gesture, or a hidden row has no quoted label path | `U102 {SCR}: "{action}" is reachable only by {gesture}; add a visible control and keep the gesture after "also:".` |
| U103 | A main-path step is reached through "More" or an ellipsis | `U103 {SCR}: main-path action "{action}" of {SCN} is behind a generic overflow; show it or put it in a named container.` |
| U104 | An icon-only label is outside the allowed glyph set | `U104 {SCR}: "{action}" uses glyph "{glyph}" without a text label; allowed icon-only glyphs are listed in UIM-08.` |
| U105 | `Profile` is missing, the primary is `standard`, or more than 3 rows are `performance` | `U105 {SCR}: profile problem on "{action}": {detail}.` |

### Example: a metronome screen

Scenario ids and frequencies are illustrative and marked `(assumed)` until the team has data.

**Before** (the current screen plus what the next build adds, all on the first layer):

| Action | Label or glyph | Scenario | Frequency | Tier | Reached by |
|---|---|---|---|---|---|
| Start or stop the click | "Start" | SCN-21 | every visit (assumed) | primary | visible |
| Change tempo | glyph:minus, glyph:plus, wheel | SCN-21 | every visit (assumed) | secondary | visible |
| Set tempo by tapping | "Tap tempo" | SCN-22 | often (assumed) | secondary | visible |
| Edit beat pattern | four dots, hint line | SCN-23 | often (assumed) | secondary | visible |
| Choose meter | 7 chips | SCN-23 | often (assumed) | secondary | visible |
| Set clicks per beat | 4 chips | SCN-23 | rare (assumed) | secondary | visible |
| Use a rhythm instead of a click | 5 or more chips | SCN-23 | rare (assumed) | secondary | visible |
| Turn accent on or off | toggle | SCN-23 | rare (assumed) | secondary | visible |
| Turn sound on or off | toggle | SCN-21 | rare (assumed) | secondary | visible |
| Set volume (next build) | slider | SCN-21 | rare (assumed) | secondary | visible |
| Choose click sound (next build) | 3 options | SCN-21 | rare (assumed) | secondary | visible |
| Run the speed trainer (next build) | controls | none yet | rare (assumed) | secondary | visible |

Count: 9 today and 12 after the next build. Expected lint: U100 (12 against 5), U101 (rare actions at depth 0), U098 (the trainer has no scenario).

**After**, State: idle (in State: running the first row's label is "Stop", in the same frame):

| Action | Label or glyph | What it does | Scenario | Frequency | Tier | Reached by | Profile |
|---|---|---|---|---|---|---|---|
| Start or stop the click | "Start" / "Stop" | Starts the click at the shown tempo; the same control stops it | SCN-21, 22, 23 | every visit (assumed) | primary | visible | performance |
| Change tempo | glyph:minus, glyph:plus around the numeral | Steps by 1; tapping the numeral opens the tempo editor (wheel and typed value) | SCN-21 | every visit (assumed) | secondary | visible; also: hold to repeat | performance |
| Set tempo by tapping | "Tap tempo" | Sets the tempo from the taps | SCN-22 | often (assumed) | secondary | visible | performance |
| Edit beat pattern | four dots, hint "Tap a dot: accent, normal, quiet, rest" | Cycles one beat | SCN-23 | often (assumed) | secondary | visible | frequent |
| Open rhythm and sound | read-out "4/4 · 1 click · Wood" | Opens the settings sheet | SCN-23 | often (assumed) | secondary | visible | frequent |
| Choose meter | "Meter", 4/4 marked | variants | SCN-23 | often (assumed) | hidden | "4/4 · 1 click · Wood" > Rhythm | frequent |
| Set clicks per beat | "Clicks per beat" | Subdivides the beat | SCN-23 | rare (assumed) | hidden | same > Rhythm | frequent |
| Use a rhythm instead of a click | "Rhythm pattern" | variants, tap to hear | SCN-23 | rare (assumed) | hidden | same > Rhythm | frequent |
| Choose click sound | "Click sound" | variants, tap to hear | SCN-21 | rare (assumed) | hidden | same > Sound | frequent |
| Set volume | "Volume", glyph:minus, glyph:plus | Changes click volume | SCN-21 | rare (assumed) | hidden | same > Sound | frequent |
| Turn accent on or off | "Accent" | Toggles the accent | SCN-23 | rare (assumed) | hidden | same > Sound | frequent |
| Mute the click | "Sound" | Lamp only | SCN-21 | rare (assumed) | hidden | same > Sound | frequent |
| Run the speed trainer | "Speed trainer" | Raises tempo by steps; its settings appear inline when on | SCN-24 (to be written) | rare (assumed) | hidden | same > Trainer | frequent |
| Go back | glyph:back | Leaves the tool | exit | every visit | secondary | visible | standard |

- Count: 5 counted visible actions, 3 of them performance, maximum depth 1. The lamp row is a display, not an action; the beat dots flash and serve as the lamp.
- If usage shows the trainer is used often, it earns its own screen under UIM-01.
- On iPad the Rhythm, Sound and Trainer groups sit open in the inspector.

## The novice in the test panel

### Who the novice is

A capable adult who is new to this kind of app. The definition for the panel template is one line:

> Has not used an app like this; reads every label; does not guess hidden gestures, long press or icon-only controls; understands a plain explanation the first time.

Experience is about the app category, not the domain. A guitarist of thirty years can be a novice in a metronome app. A first-time songwriter can be an expert phone user. Portraits never describe the novice as slow, confused or careless.

### The field

- The experience level is the first token of the `needs` line: `novice`, `regular` or `expert`. This is the same way `retention` opens with `local` or `tourist`.
- It is a token, not a ninth key, so `FIELDS` in design_gate.py stays as it is and existing panels need a one-word edit per portrait.
- Minimum in a panel of ten: at least 2 `novice` and at least 1 `expert` (HOUSE DEFAULT). The expert guards against hiding power.
- At least one novice should be skilled in the domain. That portrait tests "not stupid".
- When the product targets iPad, at least one portrait's `needs` names a tablet.

### Two portraits

**Music creation (novice in the app and in the domain tools)**
- **basis**: hypothesis
- **situation**: Marta, 24, writes verses in her notes app and hums melodies into voice memos. Evenings, at home, on her phone.
- **goals**: "I want to hear my text over a beat and record myself without learning a studio."
- **features**: lyrics editor, beat picker, recording
- **scenarios**: SCR-02 → SCR-05 → SCR-06
- **activation**: first recorded verse over a beat. Likely to drop when she cannot tell how to change the beat.
- **retention**: tourist: a new verse idea → open the draft → hear it sung → shares it; leaves if a take is lost.
- **needs**: novice: small iPhone, default text size, Bluetooth earbuds, one hand

**Learn to play (novice in the app, skilled in the domain)**
- **basis**: hypothesis
- **situation**: Andrzej, 52, played guitar in his twenties and has picked it up again. He practises with the iPad on a music stand and the guitar in his hands.
- **goals**: "Keep me in time and let me slow a song down."
- **features**: metronome, song player
- **scenarios**: SCR-11 → SCR-07
- **activation**: first song played through with the click. Likely to drop when he must put the guitar down to change the tempo.
- **retention**: local: daily practice slot → open the metronome → plays cleaner than yesterday → comes back tomorrow; leaves if setup takes longer than tuning.
- **needs**: novice: 13 inch iPad in landscape on a stand, larger text, instrument in hands, no headphones

### The walk protocol

The design-tester runs it once per screen in scope for each novice portrait, first on frames (pass D), then on the build (pass B).

**Ground rules**
- The tester writes the novice's answers before opening the action map.
- Every answer quotes the visible text or names the glyph that led to it. An answer without visible evidence is recorded as a guess and counts as a fail. This keeps a model from answering with what it knows instead of what the screen shows.

**Test 1: first ten seconds** (the capture of the initial state only)
1. "What is this screen for?"
2. "What would you tap first?"
3. "For each control you see, what happens when you tap it?"

**Test 2: find it** (once per secondary action and per hidden action in scope)
- The goal is given in the scenario's words, not in the label's words: "You want the click to sound softer. Where do you go?"

**Test 3: state** (the capture of the running state, such as recording or playing)
1. "Is something happening right now? What?"
2. "How do you stop it?"
3. "You made a mistake a moment ago. How do you take it back?"

### Pass or fail

| Test | Pass when | Fails as (existing check, named finding) |
|---|---|---|
| 1.1 Job | The answer matches the verb and object of `Purpose` | `focus`, finding `purpose` |
| 1.2 First tap | The answer is the primary action, or the control of the scenario's first step | `primary_action`, finding `first-tap` |
| 1.3 Predictions | Every counted visible action is predicted correctly with evidence | `focus`, finding `label` (one per missed action) |
| Frame against map | The frame shows no control outside the map and misses none | `controls`, finding `unmapped` or `missing` |
| Over budget | The frame's counted visible actions are 5 or fewer | `focus`, finding `overload` |
| 2 Find it | Visible action: first tap is right. Hidden action: reached with at most one wrong container | `controls`, finding `findability` |
| 3.1, 3.2 State | The state is named from text, and the stop control is identified | `states`, finding `state-unclear` |
| 3.3 Undo | An undo path is identified | `states`, finding `no-undo` |

A fail by either novice is a fail for the screen.

**The expert portrait** runs a short counter-check: no `often` action costs more taps than before the change, and every gesture accelerator still works. A fail is recorded as `controls`, finding `slower`.

**Limit of the method.** The panel is a model playing a person. Before a flagship release, repeat Test 1 and Test 3 with three to five real first-time users.

## iPhone and iPad layout, control profiles (for MOBILE_SURFACES.md)

Every number marked HOUSE DEFAULT is our choice. Every platform number must be re-verified against the current HIG before it is written as normative, and recorded in KNOWLEDGE_PROVENANCE.md (MOBILE_SURFACES.md (section The native state matrix)).

### Decide by size class, not by device

Layout follows the size class, never the device name or the orientation. Functions stay the same in every class; only the amount visible changes [A5].

| Context | Width | Layout |
|---|---|---|
| iPhone portrait | compact | One pane. Bars, content, bottom controls |
| iPhone landscape | compact height | Two columns: read-out and content on the leading side, controls on the trailing side |
| iPad full screen, any orientation | regular | Two or three panes (UIM-26) |
| iPad narrow window | compact | The phone layout; the inspector becomes a sheet |

The row-to-class mapping above is from working knowledge, not from the research set. Verify it against HIG Layout before it is written as normative.

### iPadOS 26 facts [A12]

- Apps are freely resizable windows with a resize handle. Resizing must not permanently change the layout.
- Window controls sit at the leading edge of the toolbar. Wrap the toolbar around them instead of accepting an extra safe area.
- One window per document, each named uniquely by its title.
- Every app has a menu bar. Order commands by frequency, never hide items, and put tabs and the sidebar toggle in the View menu (UIM-29).
- The pointer tracks 1 to 1 and no longer snaps to targets. Design and test hover states.
- Navigation: use a sidebar for many or deep destinations; otherwise start with a tab bar, which can turn into a sidebar.

### Control profiles and spacing

| Profile | Short side of hit region | Gap to neighbour | Used for |
|---|---|---|---|
| Standard | 44 pt [A1][A2] | 12 pt visible gap if bezelled, about 24 pt if unbezelled [A1] | Default |
| Frequent | 60 pt, HOUSE DEFAULT | 12 pt | Primary, `every visit` actions, corner targets, editor controls |
| Performance | 72 pt, HOUSE DEFAULT | 16 pt, HOUSE DEFAULT | Controls used while playing; at most 3 per screen |

- **Profile square test.** A square of the profile size centred on each target does not overlap a neighbour's square or leave the screen.
- **Destructive controls.** At least 24 pt from any frequent or performance target (HOUSE DEFAULT).
- **The primary** is the largest target on the screen and sits in the lower half on compact width (UIM-20).
- **Text.** Labels, read-outs and state text are 13 pt or more; nothing is under 11 pt (HOUSE DEFAULT).
- **Insets.** Content keeps 16 pt from the edge on compact width and 24 pt on regular width (HOUSE DEFAULT).
- **Regular width.** Buttons and steppers are at most 400 pt wide and text columns at most 680 pt (HOUSE DEFAULT). Timelines, sliders, waveforms and media may span the pane.
- **Read-outs and miniatures.** A read-out is a 44 pt target showing the current value; its editor uses 60 pt controls. A miniature is one target (UIM-21).
- **Drags.** Every drag has a tap alternative [W3].
- **Shapes.** Capsule near the phone edge with extra margin; concentric with the window edge on iPad [A11].

### Materials and motion limits

- Translucent material only on bars and floating controls. Never on content, never stacked. The clear variant only over media with dimming [A6][A10].
- Tint only the primary [A10].
- One scroll edge effect per view [A11].
- Persistent controls keep their frame between states [N20].
- Test with Reduce Transparency, Increase Contrast and Reduce Motion [A10].

### Recipe 1: performance tool (metronome-like)

**iPhone portrait, top to bottom**
1. Bar: Back, screen title.
2. Setup read-out row, 60 pt high: current meter, clicks and sound. It opens the "Rhythm and sound" sheet.
3. Beat dots, 60 pt each, with one hint line. They flash on the beat, so no separate lamp row is needed.
4. Tempo numeral in the display size. This is the signature. Tapping it opens the tempo editor.
5. One row: minus, "Tap tempo", plus. 72 pt high, 16 pt gaps.
6. "Start" pill, 72 pt or higher, full width inside 16 pt insets, in the lower third. It becomes "Stop" in the same frame.

**iPhone landscape**
- Numeral and dots on the leading half; tempo row and Start on the trailing half.

**iPad landscape**
- Leading sidebar: the app's tools and songs (collapsible).
- Main pane: a centred block, at most 560 pt wide (HOUSE DEFAULT). Larger numeral, the same control sizes, Start capped at 400 pt.
- Trailing inspector, about 320 to 360 pt (HOUSE DEFAULT): Rhythm, Sound and Trainer groups open, each option at 60 pt, sounds and rhythms previewed with a tap.
- Keyboard (HOUSE DEFAULT): Space starts and stops; arrow keys change the tempo.
- Narrow window: falls back to the phone layout.

### Recipe 2: content plus transport (lyrics-and-beat-like)

**iPhone portrait**
1. Bar: Back, song title, Undo on the leading side. Two labelled actions on the trailing side, for example "Ideas" and "More". No bare badge or dot.
2. Lyrics: the content layer, no glass, 16 to 20 pt inset. Stressed syllables larger and bold: this is the signature.
3. Beat strip: a miniature at least 56 pt high (HOUSE DEFAULT) with a labelled "Beat" button at its leading end. The whole strip is one target that opens the beat editor. Inner text is 11 pt or more, or is dropped.
4. Transport: a floating capsule in the lower part. Play at 60 pt, and the "Record" pill at 60 pt or higher as the largest target. While recording, the label reads "Recording" with elapsed time and a level meter, and the pill becomes "Stop" in place.

**iPad landscape**
- Leading sidebar: sections of the song and its versions.
- Main pane: lyrics column at most 680 pt wide, centred.
- Bottom lane across the main pane: the beat editor open, track rows 44 pt or higher. A timeline benefits from width.
- Trailing inspector: Ideas and Versions as variants, with preview in place and the current one marked.
- Transport: one capsule, bottom centre, the same sizes as on the phone.
- Keyboard: Space plays and pauses (HOUSE DEFAULT). Pencil is used where precision helps [A14].

## Change list by owner

Ship in this order: super-ux, then sheleg-design, then task-pipeline. Each release works alone:
- super-ux adds a format and lint; nothing consumes it yet.
- sheleg-design adds reference text that reads the map when present.
- task-pipeline reads the map and the levels only when the project has them.

Catalogue homes: rules UIM-01 to UIM-14 and UIM-29 live in super-ux files. UIM-15 to UIM-28 live in sheleg-design files. UIM-30 lives in task-pipeline code plus one prompt sentence. Other owners cite the id only.

### 1. super-ux 0.67.1 → 0.68.0 (minor: new format field, new lint codes)

| # | File | Section | Change | Budget |
|---|---|---|---|---|
| S1 | `skills/references/scenario-format.md` | screens.md contract (:511-512, :529) | `Purpose:` becomes one verb phrase plus one job id (UIM-01). `Actions:` table replaces `Elements:`, with the counting rules and tier and depth rules (UIM-02 to UIM-07). `Elements:` stays as a legacy alias for one release. Add the state requirements of UIM-09 and UIM-12 and the flags `irreversible` and `variants`. | Reference file, no skill-body cost |
| S2 | `skills/references/scenario-format.md` | lint table (after :1202) | Add U096 to U105 with the messages from action-map.md | Same |
| S3 | root `templates/screens.md` | entry seed (:51) | Seed the new Purpose line and the empty Actions table | Synced copy |
| S4 | `plugins/super-ux/scripts/ux_lint.py`, `test/ux_lint_test.py` | new rules | Implement U096 to U105; W on format 1, E on format 2 | Code |
| S5 | `skills/references/component-guidelines.md` | rows | Add the allowed glyph set (UIM-08), variant browsing (UIM-13, UIM-14), the iPad menu bar (UIM-29), and one row "iPad regular width: sidebar or split view, see sheleg-design UIM-26". Line :46 links to UIM-02. | Six synced copies |
| S6 | `skills/references/practice-selection.md` | Step 1, Platform | Add the value `mobile-ipados`; it pulls UIM-26 to UIM-29 | Reference |
| S7 | `skills/references/best-practices.md` | BP-049, BP-050, BP-051 | BP-049: replace "thumb zone" with a link to UIM-20. BP-050: link to UIM-18. BP-051: note that U102 enforces it. | Reference |
| S8 | `skills/references/internal-screens.md` | IS-01 | Link to UIM-01; do not restate | Reference |
| S9 | root `templates/test-panel.md` | `needs` line (:23), new section | `needs` opens with `novice`, `regular` or `expert`. Add the one-line novice definition and a "Novice walk" section holding the three tests and the pass or fail table. | Synced copy |
| S10 | `ux-foundation/SKILL.md` | "The test panel" (:224-229) | Add: at least two novices and one expert; a tablet among the needs that change a screen | 1067 tokens free; keep under 60 |
| S11 | `ux-flows/SKILL.md` | :169 | Swap "elements with one primary action" for "the action map (one primary)" | 51 tokens free; token-neutral |
| S12 | `ux-audit/SKILL.md` | :189, :273-277 | The audit checks map rows instead of listed elements. One sentence: PRN-08, PRN-11 and PRN-13 findings on a screen whose map fails U097 to U103 count as scenario findings. | 173 tokens free; keep under 60 |
| S13 | (none) | (none) | Run `python3 test/sync_references.py`, then `test/validate.py` | Drift fails validation |

**Why the walk text lives in the panel template (S9).** The design-tester already reads the project's `docs/ux/test-panel.md`, and task-pipeline prompt files have one word of headroom. super-ux owns the questions; task-pipeline owns running them and the gate.

### 2. sheleg-design 1.67.1 → 1.68.0 (minor: new reference sections and a profile clause)

| # | File | Section | Change | Budget |
|---|---|---|---|---|
| D1 | `MOBILE_SURFACES.md` | new sections; axes (:169-178) | Add "Control profiles and spacing" (UIM-18 to UIM-21), "iPad and regular width" (UIM-26 to UIM-28), "Materials and motion limits" (UIM-22, UIM-23), and the two recipes. Add a third mandatory pair "iPad regular width × default state" when the platform includes iPad. | 245 lines, has Contents; add the entries |
| D2 | `KNOWLEDGE_PROVENANCE.md` | new entries | Record [A1], [A2], [A5], [A6], [A10], [A11], [A12], [N22], [O2], [W1], [W2] with dates. Mark each house default and the point-to-millimetre arithmetic as unverified. | Reference |
| D3 | `LAYOUT_CRAFT.md` | "Proximity before container", "Density is not rhythm" (:23-37) | Add the observable ceilings of UIM-15 to UIM-17, and one line: a panel with novice portraits uses the trust-first density band | 81 lines; stay within 18 added lines or run `scripts/gen_contents.py` |
| D4 | `ACCESSIBILITY_EVIDENCE.md` | :19-21 | One paragraph: visible tiers on the web use 44 CSS px as a labelled house level; profiles are defined in MOBILE_SURFACES.md | 49 lines |
| D5 | `ADA_RUBRIC.md` | R17 (:66), R25 (:74) | R17 gains the clause "by profile, see MOBILE_SURFACES (UIM-18)". R25 gains a pointer: its checkable half is super-ux U098. | One clause each |
| D6 | `CREATIVE_DIRECTOR.md` | record fields (near :342, :369) | Define the one-line `Anchor:` and `Signature:` fields owed on `product` (UIM-15, UIM-24, UIM-25) | Reference |
| D7 | `SKILL.md` | (none) | No change. 10 tokens of headroom; all text goes to files already listed under "Load on demand". | Hard limit |
| D8 | `.cursor/` mirror | (none) | Regenerate; run `test/validate.py` | Checked |

UIM-22 and UIM-23 sit in MOBILE_SURFACES.md because no motion or materials file was named in the gap analysis. If one exists, move them there and leave a link.

### 3. task-pipeline 1.111.0 → 1.112.0 (minor: gate behaviour changes)

| # | File | Section | Change | Budget |
|---|---|---|---|---|
| T1 | `skills/task-pipeline/scripts/design_gate.py`, `test/design_gate_test.py` | `panel_problems` (:104-128) | Parse the first token of `needs`. Require at least 2 `novice` and 1 `expert`. Staged: a panel with no level token on any portrait gets a warning in this release and a failure in the next. | Code, not counted by prompt lint |
| T2 | same | new constant and `--explain` | Add the finding vocabulary: `purpose`, `first-tap`, `label`, `unmapped`, `missing`, `overload`, `findability`, `state-unclear`, `no-undo`, `slower`. Require one row per novice portrait for each screen that has an action map. | Code |
| T3 | `agents/design-tester.md` | questions (:44-48) | Replace the 54-word question block with the 54-word block below | Word-neutral, no bold; `test/prompt_lint.py` is the judge |
| T4 | `skills/task-pipeline/scripts/visual_gate.py` | `RECORD_FIELDS`, product (:61) | The `product` profile owes `Anchor` and `Signature` | Code; the stage-00 table is not edited |
| T5 | `references/design-review.md` | :45-47 | No edit. The check ids and the schema stay `design-review/1`. | Zero words |

**Replacement text for T3** (54 words by whitespace count, the same as the original):

> Is the step's screen there? Is the one primary action visible without hunting? Do controls match the action map, none missing or unmapped? Can a novice name its one job? Are empty, loading and error states designed? Does the text fit? Does the persona's funnel stage or retention trigger land where the scenario says?

### Checks that change meaning

| Check | Before | After |
|---|---|---|
| `controls` | Every control the scenario needs is present | The frame's controls equal the action map (none missing, none unmapped) and each is findable by the novice |
| `focus` | "Does anything compete", undefined in shipped files | One job: the novice names it, predicts every visible action, and the count is within budget |
| `primary_action` | Present and visible | Also the novice's first tap |
| `states` | Empty, loading and error are designed | Also the running state and the undo path are legible to the novice |
| ADA R17 | One floor per platform | The floor plus profiles |
| BP-049 | Thumb zone | Lower half and corners, by UIM-20 |

**New design-review check ids: none now.** Adding a key needs `design-review/2`, because `row_problems` rejects rows without all seven. The named findings carry the detail. If the trial shows findings clustering under `label` or under target size, add `clarity` and `targets` in `design-review/2`.

**Not changed, noted:** `internal` surfaces stay ungated, and the heuristic pass still runs only at `deep`. Both are separate decisions.

## Trial: one screen, before and after

### Inputs

- Captures of the current screen: initial state, running state, every open menu or sheet, and the empty or error state. Phone, and iPad if a build exists.
- The screen's scenario list.
- The project test panel, updated with experience levels (2 novices, 1 expert).
- The current code for the screen (for the audit).

### Steps and artefacts

| Step | Do | Artefact |
|---|---|---|
| 1 | Write the as-is action map honestly from the captures, including gesture-only features | `before-map.md` |
| 2 | Run lint U096 to U105 on it | `before-lint.txt` |
| 3 | Run the novice walk and the expert counter-check on the before captures | `before-walk.md` |
| 4 | Measure on the captures: targets under profile, spacing failures, smallest text, group count, contrast | `before-measures.md` |
| 5 | Re-tier: write the target map until lint is clean | `after-map.md` |
| 6 | Draw the after frames: phone initial, running, disclosure open, one variant choice, empty or error; iPad landscape initial | Frames |
| 7 | Repeat steps 2 to 4 on the after frames. Performance screens also run the hands test below. | `after-*.md` |
| 8 | Fill the scorecard and apply the decision rule | `scorecard.md` |
| 9 | Record every rule that failed a screen everyone judges good | `rule-misfires.md` |

**Hands test (step 7, performance screens only).** Three people with the instrument in their hands make 30 taps each on targets of 60 pt and of 72 pt. Keep 60 pt if nobody misses more than once in 30; otherwise keep 72 pt (HOUSE DEFAULT procedure).

### Scorecard

| Id | Measure | Before | After |
|---|---|---|---|
| S1 | Lint findings (U096 to U105) | | |
| S2 | Counted visible actions (budget 5) | | |
| S3 | Novice test 1: job named, first tap right, predictions k of n | | |
| S4 | Novice test 2: actions found, m of n | | |
| S5 | Novice test 3: state, stop, undo | | |
| S6 | Targets under profile, spacing failures, text under minimum | | |
| S7 | Functions reachable within depth 2 (must equal the before total) | | |
| S8 | Taps for each `often` and `every visit` action (expert) | | |
| S9 | Signature element present; unusual elements kept | | |
| S10 | iPad frame passes UIM-26 to UIM-28 | | |

### Decision rule: "after is better" when all hold

1. **No function lost** (S7).
2. **Fewer failures.** S1 and S6 are strictly lower, and S2 is within budget.
3. **The novice walk passes.** S3 to S5 pass for both novices. If not, every test that failed before has improved and none has worsened.
4. **No slowdown.** No `often` or `every visit` action costs more taps (S8).
5. **The signature is kept** (S9). The owner or creative director, shown before and after side by side without labels, prefers the after or is indifferent.

If 1 to 4 hold and 5 fails, keep the map and redo the look. If a rule blocks a result that everyone prefers, log it in `rule-misfires.md` and revise the house default, not the screen.

### Plans

The two worked plans (app D and app P) live in those apps' own repositories. Amendments 23 to 25 in `amendments.md` change step S7, decision rule 4 and the hands test.
