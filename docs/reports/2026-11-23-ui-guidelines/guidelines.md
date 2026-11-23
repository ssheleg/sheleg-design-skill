# Modern interface guidelines (2025 to 2026): research for the design-skills family

Prepared 2026-11-23. Scope: the owner's brief (beautiful and simple; no overloaded screens; few actions; everything reachable; elements grouped; each screen has its own clear user scenarios; users may browse variants; the user is inexperienced but not stupid).

## How to read this file

- Every claim carries a source tag like `[A1]`. The full source list (title, author or organisation, date, URL, verification status) is at the end.
- **Verified** means the page (or its official data endpoint, or the PDF) was opened in this session and the claim was read there.
- **UNVERIFIED** means the claim came only from a search-engine abstract, a secondary citation, or my prior knowledge. Do not ship an UNVERIFIED number as fact without opening the source.
- **Foundational** marks an older classic kept because later work builds on it.
- Apple HIG pages were read through Apple's official JSON data endpoint (`developer.apple.com/tutorials/data/design/human-interface-guidelines/<page>.json`), which serves the same text as the rendered HIG page. The m3.material.io site is a client-rendered app that could not be read as text; Material 3 Expressive claims are therefore sourced from Google's own developer.android.com component docs, the design.google research article, the blog.google announcement and the CHI 2026 paper.
- Rules are phrased so a reviewer can check them on one screen. Where a source gives a number, the number is kept.

---

## 1. Simplicity, one primary task per screen, number of primary actions, visual hierarchy

### Rules

1.1 **One primary action per view.** Apple: in a toolbar, use the prominent style for key actions such as Done or Submit, "Only specify one primary action, and put it on the trailing side of the toolbar." [A3] Liquid Glass tinting is reserved for that action: "Tinting should only be used to bring emphasis to primary elements and actions in the UI ... When every element is tinted, nothing stands out." [A10] Material's FAB "promotes a single, focused action that is the most common pathway a user might take." [G6e]

1.2 **Mark the preferred choice with style, not size.** Apple: "Use style, not size, to visually distinguish the preferred choice among multiple options" (HIG wording, punctuation adapted). Buttons of the same size signal a coherent set; a more prominent style marks the likely option. [A2]

1.3 **Never give the primary role to a destructive action**, even if it is the likely choice, "Because of its visual prominence, people sometimes choose a primary button without reading it first." [A2]

1.4 **Order content by importance.** "Place the most important items near the top and leading side of the window or display." [A5]

1.5 **Hierarchy budget (NN/g, Kelley Gordon, 2021, updated 2024).** "Use no more than 3 sizes" (small, medium, large); "Use no more than 3 contrast variations for complex designs. If everything is contrasted, then nothing stands out"; "Make the most important element biggest ... Limit how many elements are big to a maximum of 2." Check with the squint or blur test. [N1]

1.6 **Bars carry navigation and the main tasks only.** Tab bar: "Use a tab bar to support navigation, not to provide actions." [A4] Toolbar: "Provide actions that support the main tasks people perform"; "Choose items deliberately to avoid overcrowding"; "Minimize the number of groups ... In general, aim for a maximum of three." Window title "under 15 characters." [A3] Avoid screen-specific actions in the tab bar: "a checkout button, for example, belongs with the content it supports." [A11]

1.7 **Fewer tabs are easier.** "It's generally easier to navigate among fewer tabs"; avoid the overflow "More" tab; where people customise tabs, "aim for a default list of five or fewer." Use labels, single words where possible. [A4]

1.8 **Functionality beats flourish (Google's own caveat).** "Don't compromise your product's core functionality for visual flourishes. No amount of emotion can compensate for a lack of clarity." [G3]

1.9 **Every extra option has a cost.** Displaying many options "makes the screen appear more crowded and the menus more complex," making errors more likely; in NN/g's soda-machine example, time on task grew "by over 500%." (Hoa Loranger, 2015.) [N13] Total cognitive load affects how easily users find content and complete tasks (Kathryn Whitenton, 2013, updated 2025). [N10]

### Notes for the reviewer
- "One primary task per screen" is not stated as a numeric rule by Apple or Google. What they do state is one primary action per view or toolbar [A3], one FAB per focused action [G6e], and at most 3 toolbar groups [A3]. The per-screen scenario requirement in the brief maps to NN/g's progressive-disclosure advice to put "everything that users frequently need up front" [N2] (section 3).

---

## 2. Grouping (Gestalt proximity, common region), chunking, information density

### Rules

2.1 **Proximity signals relation.** "Design elements near each other are perceived as related, while elements spaced apart are perceived as belonging to separate groups." A 12-field form feels taxing while "a 3-chunk form with 4 fields each seems simple in comparison." Grouping unrelated items camouflages them (an Add button buried among Next, Save as Draft, Cancel). Responsive layouts can destroy groupings when spacing shrinks. (Aurora Harley, 2020, updated 2024.) [N3]

2.2 **Common region: a container groups more strongly than spacing**, "a strong visual cue that can overpower other grouping principles such as proximity or similarity", but "too many borders and colored boxes that exist purely for decoration add clutter." (Aurora Harley, 2020, updated 2023.) [N4] NN/g's hierarchy article agrees: add a container only "if varying whitespace alone is not enough." [N1]

2.3 **Group by function and frequency.** Apple HIG Layout: "Group related items ... you might use negative space, container shapes, or separator lines." [A5] WWDC25 session 356: "Group bar items by function and frequency"; "hierarchy should be expressed through layout and grouping" instead of decoration; do not group a symbol with a text button ("Select" next to a share icon reads as one button). [A11] HIG Toolbars repeats it and adds: keep text-labelled actions separate. [A3]

2.4 **Spacing is as important as size.** Apple: "add about 12 points of padding around elements that include a bezel. For elements without a bezel, about 24 points of padding works well around the element's visible edges." [A1]

2.5 **Chunk content and data.** Short paragraphs, headings, lists; format strings in conventional chunks (card numbers 4x4) and auto-format input so users never type separators. Miller's "magical number seven" is often misused: menus rely on recognition, so a menu can hold more than seven items. (Kate Moran, 2016, updated 2024.) [N5]

2.6 **Density is a per-context choice, not a style.** Apple keeps mini, small and medium rounded-rectangle controls on macOS for "compact, high-density layouts like inspector panels", while large controls become capsules. [A11] Material button groups "should stay on a single line rather than wrapping to a second line" and push extra items into an overflow menu when space is short. [G6a]

---

## 3. Few actions, progressive and staged disclosure, defaults, when to hide versus show

### Rules

3.1 **Progressive disclosure (Jakob Nielsen, 2006, updated 2022; foundational).** "Initially, show users only a few of the most important options. Offer a larger set of specialized options upon request." Get the split right: "disclose everything that users frequently need up front." Make the way to the next level obvious and label it with strong information scent. "Designs that go beyond 2 disclosure levels typically have low usability"; with 3 or more levels, simplify or chunk advanced features into sensible groups. [N2]

3.2 **Staged disclosure (wizards)** suits tasks that split into steps with little interaction between them; it "is problematic when the steps are interdependent." Too many steps bog users down. [N2]

3.3 **Decide what to show from task analysis and usage frequency**, not opinion ("frequency-of-use statistics can help you prioritize"). [N2] Apple toolbars: put less important actions in a More menu and "Try to include all actions in the toolbar if possible, and only add this menu if you really need it." [A3]

3.4 **Hide only what is nonessential.** NN/g on iOS 26: overflow menus should hold only nonessential actions (Raluca Budiu, 2025). [N20] Apple's iPad menu bar: "Hiding menu items is not recommended because people will find this disorienting"; "Menu items should always remain in the same place, even when inactive"; order actions "by frequency of use, and not alphabetically." [A12]

3.5 **Change the amount shown, never the functionality.** "Don't change your app's functionality based on the space it occupies. However, you can change the amount of functionality that's visible onscreen," for example switching a tab bar to a sidebar on larger windows. [A5]

3.6 **Contained secondary actions (Material).** FAB menu: "Opens from a FAB to show two to six related actions," replacing speed dials and stacked small FABs. [G6c] Split button: leading button does the primary action, trailing button opens related options. [G6b] Floating toolbar: "Choose the most essential actions to show on screen by default"; use an overflow menu for the rest. [G6d]

3.7 **Defaults do most of the work.** People "tend to stick to the defaults" and rarely use customisation; in Joachims' study cited by NN/g, 42% clicked the top search hit, and still 34% after the top two were swapped (Jakob Nielsen, 2005, updated 2024; foundational). [N14] Apple: "Provide reasonable default settings so most people can immediately start interacting." [A7]

3.8 **Restore what you hide.** If toolbars hide for a distraction-free view, "offer ways to reliably restore hidden interface elements." [A3]

---

## 4. Novice but not stupid: recognition over recall, learnability, onboarding without tutorials, empty states, plain language, tone, error prevention, undo over confirm

### Evidence that matters most for the brief

- **Tutorials do not help and make apps feel harder.** NN/g ran a between-subjects test with 70 users on 4 apps with deck-of-cards tutorials. Task success: 91% with the tutorial versus 94% without (not significant, p = 0.443). Completion time: 93.49 s versus 85.17 s (not significant). Ease rating (SEQ, 1 to 7): 4.92 with the tutorial versus 5.49 without, a significant difference: people who saw the tutorial rated the task harder. (Alita Kendrick, 2020.) [N16]
- **Push revelations are forgotten; pull revelations work.** Tutorials "interrupt users," "don't tend to be memorable"; the paradox of the active user means people want to start using the product right away. Use contextual help that users can call up when they need it (Page Laubheimer, 2023, updated 2024). [N17]
- **Plain language is not dumbing down.** In NN/g studies with domain experts in science, technology and medicine, "even highly educated online readers crave succinct information that is easy to scan." (Hoa Loranger, 2017.) [N12] This is the evidence behind "inexperienced but not stupid": write simply, never explain the obvious.

### Rules

4.1 **Recognition over recall.** Show options instead of making people remember them; recognition is easier because context helps retrieval (Raluca Budiu, 2024). [N6] NN/g heuristic 6 (Jakob Nielsen, 1994, updated 2026; foundational). [N21]

4.2 **Teach by doing, in context.** Apple: "Teach through interactivity"; "consider providing a collection of context-specific tips instead of a single onboarding flow"; display instructions near the area they refer to; if a tutorial exists, make it optional, never show it again after a skip, and keep it findable later. [A7] NN/g: avoid feature-promotion onboarding at first launch; "for most mobile apps, users should be able to learn the interface by using it." (Alita Kendrick, 2020.) [N15]

4.3 **Postpone setup and permission prompts.** "Postpone nonessential setup flows or customization steps"; ask for a permission when people first use the function that needs it; let people experience the app before asking for ratings or purchases. [A7] If you ask for customisation data at the start, explain why and how it is used. [N15]

4.4 **Design every empty state.** Use it to communicate system status (never show "No records" while still loading), give learning cues, and offer a direct path to the key task. (Kate Kaplan, 2021.) [N7]

4.5 **Errors: human language, no blame, a way forward.** "Avoid technical jargon"; "Don't use phrasing that blames users ... such as invalid, illegal, or incorrect"; protect the user's effort and offer accelerators to fix the problem. (Evan Sunwall, 2023, updated 2024.) [N18]

4.6 **Tone fits the moment.** Tone varies on four dimensions: funny to serious, formal to casual, respectful to irreverent, enthusiastic to matter-of-fact; humour in a message frustrated users see often "might be irritating." Test tone with users. (Kate Moran, 2016, updated 2024.) [N19]

4.7 **Prevent slips before they happen.** Offer suggestions, use constraints, accept flexible input formats. (Page Laubheimer, 2015, updated 2023.) [N8]

4.8 **Undo first, confirm rarely.** Confirm only actions "with serious consequences", especially ones that cannot be undone; "Do not use confirmation dialogs for routine actions"; never ask "Are you sure?", state the consequence; label buttons with the outcome ("Delete file" / "Keep file"); no default Yes; and "go to great lengths to provide undo." (Jakob Nielsen, 2018, updated 2026.) [N9]

4.9 **Always an exit.** Provide a clear Cancel and Undo; "Accompany icons with text labels or substitute icons with plain text. For example, use Back instead of < and Close instead of X." (Maria Rosala, 2020, updated 2024.) [N11] Apple, for its own standard Back and Close, prefers the standard symbols over text labels [A3]; NN/g counters that iOS 26 back buttons that lost their text labels hide affordances [N20]. Resolution for a novice audience: use the system Back control and make the destination title visible on screen.

4.10 **Accessibility criteria that protect novices (WCAG 2.2, new in 2.2):** 3.2.6 Consistent Help (A), 3.3.7 Redundant Entry (A), 3.3.8 Accessible Authentication (Minimum) (AA), 2.5.7 Dragging Movements (AA), 2.4.11 Focus Not Obscured (Minimum) (AA). [W3]

---

## 5. Touch targets and large controls

### Numbers

| Source | Rule | Status |
|---|---|---|
| Apple HIG Accessibility [A1] | Default control size iOS/iPadOS 44x44 pt (minimum 28x28 pt); watchOS 44x44 (28x28); visionOS 60x60 (28x28); tvOS 66x66 (56x56); macOS 28x28 (20x20). | Verified |
| Apple HIG Buttons [A2] | "A button needs a hit region of at least 44x44 pt", 60x60 pt in visionOS. visionOS: button centres at least 60 pt apart. | Verified |
| Apple HIG Accessibility [A1] | Padding about 12 pt around bezelled elements, about 24 pt around elements without a bezel. | Verified |
| Android / Material [G5] | "Touch target size, of at least 48dpx48dp. Larger is even better." Compose Material components enforce this. | Verified |
| WCAG 2.2 SC 2.5.8 Target Size (Minimum), AA [W1] | At least 24x24 CSS px, except: spacing (a 24 px circle centred on each undersized target does not intersect another target or circle), equivalent control, inline, user-agent control, essential. For important controls, aim for 2.5.5. | Verified (Understanding doc updated 02 November 2026) |
| WCAG 2.2 SC 2.5.5 Target Size (Enhanced), AAA [W2] | At least 44x44 CSS px, except equivalent, inline, user-agent control, essential. | Verified |
| NN/g (Aurora Harley, 2019, updated 2023) [N22] | At least 1 cm x 1 cm (0.4 in) physical size, from Parhi, Karlson and Bederson (MobileHCI 2006). Fingertips 1.6 to 2 cm wide, thumb contact about 2.5 cm. Primary calls to action and use while moving deserve larger targets; reducing the number of elements lets key targets be larger. | Verified (NN/g page); the 2006 paper itself UNVERIFIED |
| Steven Hoober, UXmatters, 2017 [O2] | 75% of users touch with one thumb; fewer than 50% hold with one hand; 36% cradle. Accuracy is best at the centre: centre targets can be as small as 7 mm, corners need about 12 mm (sizes that capture 95% of taps). The classic thumb-sweep "thumb zone" chart is called incorrect. | Verified |
| Steven Hoober, UXmatters, 2013 [O1] | 49% one-handed, 36% cradled, observation of about 1,333 people. | UNVERIFIED (search abstract only; foundational) |

### Rules
5.1 Interactive targets meet 44x44 pt (Apple), 48x48 dp (Android), and at least 24x24 CSS px with spacing on the web (WCAG AA), 44x44 for important controls (WCAG AAA). [A1][G5][W1][W2]
5.2 Size is necessary but not enough: "targets must first be big enough, and then also spaced well enough." [N22]
5.3 Make the primary action and any control used while moving or performing physically larger than the minimum. [N22]
5.4 Do not rely on a narrow "thumb zone": people reach the whole screen, but corners need bigger targets (about 12 mm) than the centre (about 7 mm). [O2]
5.5 Every drag-only control (fader, knob, timeline scrub, reorder) also works with a single pointer without dragging (tap steps, plus and minus, numeric entry), per WCAG 2.2 SC 2.5.7. [W3]

---

## 6. Apple HIG 2025 and Liquid Glass (WWDC25, iOS 26 / iPadOS 26)

### What changed
- **A new functional layer.** Liquid Glass is "a distinct functional layer for controls and navigation elements, like tab bars and sidebars, that floats above the content layer" (punctuation adapted). [A6] Newsroom: controls, toolbars and navigation "now fit perfectly concentric with the rounded corners of modern hardware and app windows." [A13] Alan Dye called it "our broadest software design update ever." [A13]
- **Content first.** "Liquid Glass is best reserved for the navigation layer that floats above the content of your app"; making a content table view glass "would make it compete with other elements and muddy the hierarchy." [A10] HIG Materials: "Don't use Liquid Glass in the content layer"; exception: transient controls such as sliders and toggles take on glass while being operated. "Use Liquid Glass effects sparingly." [A6]
- **No glass on glass.** "Stacking Liquid Glass elements on top of each other can quickly make the interface feel cluttered and confusing." [A10]
- **Two variants, never mixed.** Regular works over any content and is used for components with significant text (alerts, sidebars, popovers). Clear only when three conditions hold: over media-rich content, a dimming layer will not hurt the content, and the content on top is bold and bright. Without dimming, "legibility gets noticeably worse." [A10][A6]
- **Concentricity.** Three shape types: fixed (constant radius), capsule (radius half the height), concentric (parent radius minus padding). Phone: capsule with extra margin near the screen edge; iPad and Mac: concentric shape aligned to the window edge; standalone components: concentric with a fallback radius. "If something feels off ... Its shape probably needs to be concentric." [A11]
- **Tab bars.** In iOS 26 "when users scroll, tab bars shrink to bring focus to the content ... The moment users scroll back up, tab bars fluidly expand." [A13] A tab bar can carry an accessory (the Music MiniPlayer) and minimise with the accessory inline on scroll; a dedicated Search tab sits at the trailing end. [A4][A11]
- **Toolbars.** "If you've customized your bars, now's the time to clean them up"; reduce custom backgrounds and tinted controls; prefer system symbols without borders; one prominent primary action. [A11][A3]
- **Scroll edge effects** replace hard dividers; "not decorative"; "Apply one scroll edge effect per view"; soft is the iOS/iPadOS default, hard is mostly macOS. [A11]
- **Sheets.** An interrupting task pairs glass with a dimming layer; a parallel task uses glass without dimming. Action sheets spring from the control that opened them. [A11]
- **Typography.** "Bolder and left-aligned to improve readability in key moments like alerts and onboarding." [A11]
- **Accessibility settings adapt automatically**: Reduce Transparency (frostier), Increase Contrast (black or white with a contrasting border), Reduce Motion (no elastic effects). [A10] HIG Materials also says the look can differ "if people choose a preferred look for Liquid Glass in their device's settings." [A6] Press reports that this preference arrived in iOS 26.1 as a Clear or Tinted choice under Display & Brightness [O6, UNVERIFIED against an Apple primary page].

### iPadOS 26: windowing, menu bar, pointer, layouts (WWDC25 session 208) [A12]
- Every multitasking app shows a resize handle; apps become freely resizable floating windows. Window controls sit on the leading edge of the toolbar: "wrap your toolbar around window controls so they appear in line" instead of accepting the extra safe area.
- "Your app should create a new window for each document"; name each window uniquely (document title).
- Every app gets a menu bar (pointer to the top edge or swipe down). Order by frequency, not alphabet; put tabs and the sidebar toggle in the View menu; never hide menu items or whole menus.
- Pointer tracks input 1 to 1, no longer magnetises to targets; test hover states.
- Navigation: sidebar for many sub-views or deep content; "If you're still not sure ... start with a tab bar"; a tab bar can morph into a sidebar. Resizing must be non-destructive: "Resizing an app should not permanently alter its layout."
- Size classes (HIG Layout [A5]): decide layout by size class, not device or orientation; consider every combination; keep functionality the same as size classes change; test the largest and smallest layouts.

### Legibility concerns (independent critique)
NN/g (Raluca Budiu, 2025-10-10, updated 2026-03-18) [N20]: translucent controls over busy backgrounds lower contrast ("Text on top of images is a bad idea"); floating bars cover content; "Motion for motion's sake is not usability"; spacing between controls shrank; targets that change size and location make the interface "harder to learn and less predictable"; search moved to the bottom; back buttons lost text labels; "Apple is prioritizing spectacle over usability."

### Rules for our designs
6.1 Glass (or any translucent material) only on the navigation and control layer, never on content cards or lists. [A6][A10]
6.2 No translucent control on a busy image without a dimming layer or a regular (frosted) variant; check contrast at 4.5:1 for text in both light and dark appearance. [A1][A10][N20]
6.3 Tint only the single primary action. [A10]
6.4 Nested corners are concentric. [A11]
6.5 Controls keep stable size and position between states; motion has a purpose. [N20]
6.6 Test with Reduce Transparency, Increase Contrast and Reduce Motion on. [A10]

---

## 7. Material 3 Expressive (Google, 2025)

### Research claims, exactly as published
- **design.google research article** [G1] (no named author; acknowledgements list Bradley Patrie, Dallas Barnes, Viviane Herdel, Nico Thornley, Mason Price, Mohammed Khwaja, Brenton Simpson; date not printed, published around Google I/O 2025: date UNVERIFIED): "46 separate research studies with hundreds of designs, and more than 18,000 participants"; "Participants were able to spot key UI elements up to four times faster"; expressive design preferred across ages, "up to 87%" among 18 to 24 year olds; subculture perception +32%, modernity +34%, rebelliousness +30% (baselines not given); time to tap key actions fell "by seconds" (no figure); users 45+ performed on par with younger users in fixation times across 10 apps. Methods: eye tracking, surveys, focus groups, experiments, usability tests.
- **Peer-reviewed version** [G2]: Bentley, Schmidt, Sheehan, Gallardo, Wang, "Usability Hasn't Peaked: Exploring How Expressive Design Overcomes the Usability Plateau," CHI '26, Barcelona, April 2026. 48 participants, 10 apps, M3 Expressive versus previous Material: users fixated on the correct element 33% faster, tasks 20% faster, more positive ratings. The authors also note risks of added design flexibility.
- **Android Developers page** [G3]: preference about +100% and aesthetics up to +170% versus baseline.

### Caveats (from Google's own material)
- "Up to" figures are maxima, not typical results; per-study sample sizes and baselines are not in the article. [G1]
- "A strong minority of users preferred calmer, less intense versions." [G3][G1]
- Breaking standard patterns hurt: a playlist redesign lowered usability scores; removing text labels from email actions reduced usability. [G1]
- Familiarity affected results; banking-style interfaces may not suit expressive design. [G1]
- "Conduct usability research to verify that you haven't gone too far." [G3]
- All research is by Google, about Google's system; the CHI paper is peer reviewed but its authors are Google researchers. I found no independent NN/g evaluation of M3 Expressive (search on 2026-11-23).

### Components (Google developer docs, Compose Material 3) [G6]
- **Button groups**: coordinated shape, motion and width changes; standard (neighbours react when one is pressed) and connected (replaces segmented buttons for selection); sizes XS, S, M, L, XL; single line, overflow menu when space is short. [G6a]
- **Split button**: primary action plus a trailing menu of related options; same five sizes. [G6b]
- **FAB menu**: 2 to 6 related actions from a FAB; replaces speed dials and stacked small FABs; not used with extended FABs. [G6c]
- **Floating toolbar**: contextual actions for the current page; can navigate between related pages; container fully on screen; most essential actions by default, overflow for the rest; can pair with a FAB. [G6d]
- **Loading indicator**: morphing shapes, default or contained; for waits typically under five seconds; replaces most indeterminate circular progress indicators; "never purely decorative." [G6f]
- **Motion physics**: Compose `MotionScheme` with `standard()` and `expressive()` schemes; spatial springs for position, size and shape, effects springs for colour and alpha, each in fast, default, slow. [G7] The announcement describes "a system of more natural, springy animations" (Mindy Brooks, VP Product Management, Android, 2025-05-13). [G4]
- **Shape**: shape morphing on press and selection in button groups and split buttons [G6a][G6b]. The 35-shape library and its tokens live on m3.material.io, which could not be read here: UNVERIFIED.

### Rules for our designs
7.1 Use expressive emphasis (size, colour, shape) on the one key action of a screen, where Google measured the speed gain. [G1][G2]
7.2 Keep text labels on actions and keep standard patterns; Google's own tests show losses when these were removed. [G1]
7.3 Offer or default to a calmer variant for users and contexts that need it (money, health, settings). [G1][G3]
7.4 Springs and morphing respect Reduce Motion (platform setting) and never delay a task.

---

## 8. Music and creative apps on phone and iPad

### Evidence status
Credible, design-specific sources are thin. I found **no** published design case studies by named designers for GarageBand, BandLab, Smule, Yousician or Simply Sing on Apple, Google, NN/g, Baymard or in peer-reviewed venues. A student critique of BandLab (Pratt) and third-party teardowns turned up and were excluded as untrusted. What remains: Apple platform guidance, Apple press releases about Logic Pro for iPad, the Apple Design Awards, latency research, one developer interview (Koala Sampler), and the general rules above applied to this domain. Rules below say which is which.

### Sources and what they support
- **Apple HIG Playing audio** [A8] (updated 2023): pick the audio session category that matches use (recording apps record; record-and-play apps may play simultaneously); recording apps can ask not to be interrupted by an incoming call unless the person accepts it; when headphones disconnect, playback should pause immediately; "Avoid repurposing audio controls"; respond to remote audio controls only in a clear audio context; never communicate important information with sound only (stated for visionOS, "as in every platform").
- **Apple HIG Tab bars and WWDC25 session 356** [A4][A11]: persistent playback controls belong in a tab bar accessory ("media playback controls that stay visible across your app"), which can minimise inline on scroll.
- **Logic Pro for iPad** (Apple Newsroom, 2023-05-09) [A14]: "With Multi-Touch, creators can play instruments using a variety of play surfaces"; a sound browser with dynamic filtering where "users can tap to audition any sound before loading it into a project"; Apple Pencil for precise edits and automation drawing; keyboard shortcuts with an attached keyboard.
- **Apple Design Awards 2025** [A15]: Moises (Music.AI) finalist in Innovation, recognised because it "isolates the instruments in a recorded song" into separate tracks; PBJ: The Musical won Innovation for games (has a karaoke mode).
- **Koala Sampler** (Engadget, 2019, developer Marek Bereza interviewed) [O5]: many samplers are "too fussy, you're focused more on making tiny edits than, well, making music" (punctuation adapted); the app embraces limitation (inspired by the BOSS SP-303). Developer statement, press source, not research.
- **Latency.** Nielsen's limits: 0.1 s feels instantaneous, 1 s keeps flow, 10 s keeps attention (1993, foundational) [N23]. For playing an instrument these are far too slow: the commonly cited target for digital musical instruments is under 10 ms action-to-sound latency with under 1 ms jitter (Wessel and Wright, 2002), discussed by McPherson, Jack and Moro, "Action-Sound Latency: Are Our Tools Fast Enough?", NIME 2016, who found most common microcontroller-to-computer setups miss it [P7, UNVERIFIED: abstract via search only].
- **System status.** Communicating the current state keeps users in control and builds trust (Aurora Harley, 2018, updated 2024) [N24]; percent-done indicators for waits over about 10 s [N23].

### Rules for music and creative screens
8.1 **Record is the one primary action** of a recording screen: largest target on the screen (well above 44 pt / 48 dp; NN/g's examples of in-context primary targets run 2 to 2.3 cm), tinted, nothing else tinted. [A3][A10][N22]
8.2 **Recording state is unmistakable** without colour alone and without sound alone: a persistent state label (for example "Recording" plus elapsed time) and a visual level meter, visible from every screen while recording continues. [N24][A8] (The system microphone indicator exists on iOS, but its HIG wording was not verified in this session: UNVERIFIED.)
8.3 **Transport stays reachable everywhere** through a persistent accessory (mini transport) rather than repeating controls on each screen. [A4][A11]
8.4 **Latency is shown and handled, not hidden**: when monitoring through the device, tell the person when latency is high (for example Bluetooth output) and offer the fix (wired headphones, latency compensation). Anything played live targets under 10 ms. [P7 UNVERIFIED][N23]
8.5 **Destructive edits are undoable** (delete take, overwrite, trim); no confirmation dialog for routine edits. [N9][N11]
8.6 **Every fader, knob and scrub has a non-drag alternative** (tap to step, double-tap to type, plus and minus). [W3]
8.7 **Browsing sounds, presets, takes and covers: preview in place** (tap to audition before committing) and filter dynamically. [A14]
8.8 **Fewer parameters on the first layer**: the musical action first, fine editing behind one disclosure level. [O5][N2]
8.9 **Behave like an audio app**: pause on headphone disconnect; do not hijack system audio controls; pick the right session category; survive interruptions. [A8]
8.10 **iPad landscape**: same functions as on iPhone, more of them visible; sidebar or inspector for secondary controls; non-destructive resizing; one window per project; menu bar with frequency-ordered commands; keyboard shortcuts and Pencil where precision helps. [A5][A12][A14]
8.11 **One-handed phone use**: put frequent controls where the thumb lands near the bottom centre and give corner controls bigger targets; do not assume people never reach the top. [O2]

---

## 9. Browsing variants and choice

### Evidence
- **Hick-Hyman law** (foundational): decision time rises with the number and complexity of choices. Hick, "On the rate of gain of information," Quarterly Journal of Experimental Psychology 4(1), 11 to 26, 1952; Hyman, "Stimulus information as a determinant of reaction time," Journal of Experimental Psychology 45(3), 188 to 196, 1953 [P4][P5 UNVERIFIED: citations from search, papers not opened]. Laws of UX (Jon Yablonski) summarises it and points to these papers [O3, used only as a pointer].
- **The jam study** (Iyengar and Lepper, Journal of Personality and Social Psychology 79(6), 995 to 1006, 2000; foundational) [P1, verified in the PDF]: 6 versus 24 jams. Of 242 passers-by at the 24-jam display 60% stopped; of 260 at the 6-jam display 40% stopped. 30% of the limited-choice group bought jam, against 3% of the extensive-choice group.
- **Meta-analysis 1** (Scheibehenne, Greifeneder and Todd, Journal of Consumer Research 37(3), 409 to 425, 2010) [P2, verified abstract]: 63 conditions from 50 experiments, N = 5,036, "a mean effect size of virtually zero but considerable variance between studies"; "no sufficient conditions could be identified."
- **Meta-analysis 2** (Chernev, Böckenholt and Goodman, Journal of Consumer Psychology 25(2), 333 to 358, 2015) [P3, verified abstract]: 99 observations, N = 7,202. Choice overload is significant once four moderators are accounted for: choice set complexity, decision task difficulty, preference uncertainty, and an effort-minimising decision goal.
- **Takeaway**: the count of options alone does not predict overload. Overload grows when options are complex and hard to compare, when people do not know what they want, and when they want to decide fast. Novices with unclear preferences are exactly that case.
- **Comparison tables** (Kate Moran, NN/g, 2024-02-09, updated 2025) [N25]: use them for decisions over several attributes of a small number of items; static tables for 5 offerings or fewer, dynamic (user-picked) tables when there are more than 5; not needed for items chosen mainly for looks.
- **Baymard** (Edward Scott, 2022-10-19) [O4]: in comparison tools let users hide identical attributes ("Only show differences"), group attributes by category, keep product names, images and prices sticky while scrolling, and use row lines or shading.
- **Previews**: Logic Pro's tap-to-audition before loading [A14]; defaults dominate choice [N14].

### Rules
9.1 **Start with a recommended default** and a short curated set; "show more" reveals the rest (progressive disclosure). [N14][N2][P3]
9.2 **Reduce option complexity, not only count**: same layout per variant, the differences highlighted, identical attributes hidden. [P3][O4]
9.3 **Preview before commit** for anything sensory (sound, voice, look, style): tap plays or shows it in place; no commitment needed to explore. [A14]
9.4 **Compare side by side only when it helps**: up to about 5 items fixed, more items user-selected, sticky headers. [N25][O4]
9.5 **Browsing is safe**: switching a variant is reversible and keeps the user's work. [N11]
9.6 **Show options, do not ask people to remember them** (recognition), and do not cap menus at seven just because of Miller. [N6][N5]

---

## 10. Checklist: pass/fail checks for one screen

Each line is a yes/no check. Fail if the answer is "no."

| # | Check | Source |
|---|---|---|
| 1 | The screen's main user scenario can be stated in one sentence, and the screen's primary action serves it. | [N2][A5] |
| 2 | Exactly one action is visually primary (tinted or filled); no other element shares its emphasis. | [A3][A10][G6e] |
| 3 | The primary action is not destructive. | [A2] |
| 4 | The design uses no more than 3 type sizes, no more than 3 contrast levels, and at most 2 large elements. | [N1] |
| 5 | The most important content sits at the top and leading side. | [A5] |
| 6 | Toolbar items are in at most 3 groups, grouped by function and frequency; no text button shares a group with an icon. | [A3][A11] |
| 7 | Tab bar is navigation only (no actions), has labels, and 5 or fewer default tabs with no overflow "More" tab. | [A4] |
| 8 | Related controls are closer to each other than to unrelated ones; containers appear only where spacing alone fails, never as decoration. | [N3][N4][N1] |
| 9 | Forms are chunked into labelled groups; formatted values are chunked and auto-formatted. | [N3][N5] |
| 10 | Everything users need often is on the first layer; advanced options are one clearly labelled step away; no more than 2 disclosure levels. | [N2] |
| 11 | Nothing essential sits in an overflow menu; menu items do not disappear when inactive. | [N20][A12] |
| 12 | Defaults let a first-time user complete the main task with no setup. | [A7][N14] |
| 13 | No first-launch tutorial or feature tour blocks the screen; help is contextual and can be called up. | [N16][N17][A7] |
| 14 | Permission requests appear at the moment of use, with the reason. | [A7] |
| 15 | Every empty state says what is happening, why it is empty, and offers the next step; no "No results" while still loading. | [N7] |
| 16 | Labels and messages use plain words, no jargon, no blame words ("invalid", "illegal", "incorrect"), no talking down. | [N18][N12][N19] |
| 17 | Routine actions have undo instead of a confirmation; any confirmation states the consequence and labels buttons with the outcome, no default Yes. | [N9][N11] |
| 18 | There is a visible way back or out (Cancel, Back with destination) from every state. | [N11] |
| 19 | Touch targets are at least 44x44 pt (iOS) / 48x48 dp (Android) / 24x24 CSS px with spacing (web, AA); key controls 44x44 CSS px (AAA) or larger. | [A1][G5][W1][W2] |
| 20 | Bezelled controls have about 12 pt padding, unbezelled about 24 pt. | [A1] |
| 21 | Controls in corners are larger than controls near the centre; primary and in-motion controls exceed the minimum. | [O2][N22] |
| 22 | Every drag interaction has a single-pointer alternative. | [W3] |
| 23 | Text contrast is at least 4.5:1 in light and dark appearance, including over translucent materials and images. | [A1][N20] |
| 24 | Translucent (glass) material appears only on the navigation and control layer, never glass on glass, never on content. | [A6][A10] |
| 25 | Nested rounded shapes are concentric with their container. | [A11] |
| 26 | Controls keep the same size and position across states; every animation has a functional reason and respects Reduce Motion. | [N20][A10][G7] |
| 27 | The layout at every size class keeps the same functions; resizing does not permanently change the layout. | [A5][A12] |
| 28 | When the user picks among variants: a recommended default is marked, differences are highlighted, each variant can be previewed in place, and switching back is free. | [N14][P3][O4][A14] |
| 29 | For recording or live-audio screens: record state is shown with text and visuals (not colour or sound alone) and remains visible app-wide; transport is reachable from every screen. | [N24][A8][A4] |
| 30 | Expressive emphasis (shape, colour, motion) is applied only where it speeds up the key task, labels are kept, and a calmer variant exists for sensitive contexts. | [G1][G2][G3] |

---

## Source list

Status legend: **V** verified by opening the page or file in this session; **U** UNVERIFIED; **F** foundational (older classic).

### Apple
- [A1] Accessibility, Human Interface Guidelines. Apple. Latest change-log entry 2025-06-09. https://developer.apple.com/design/human-interface-guidelines/accessibility (read via the official JSON data endpoint). V
- [A2] Buttons, HIG. Apple. Updated 2025-12-16 ("Updated guidance for Liquid Glass"). https://developer.apple.com/design/human-interface-guidelines/buttons. V
- [A3] Toolbars, HIG. Apple. Updated 2025-12-16. https://developer.apple.com/design/human-interface-guidelines/toolbars. V
- [A4] Tab bars, HIG. Apple. Updated 2026-06-08. https://developer.apple.com/design/human-interface-guidelines/tab-bars. V
- [A5] Layout, HIG. Apple. Updated 2026-09-09. https://developer.apple.com/design/human-interface-guidelines/layout. V
- [A6] Materials, HIG. Apple. Updated 2025-09-09 ("Updated guidance for Liquid Glass"). https://developer.apple.com/design/human-interface-guidelines/materials. V
- [A7] Onboarding, HIG. Apple. Updated 2024-06-10. https://developer.apple.com/design/human-interface-guidelines/onboarding. V
- [A8] Playing audio, HIG. Apple. Updated 2023-06-21. https://developer.apple.com/design/human-interface-guidelines/playing-audio. V
- [A10] Meet Liquid Glass, WWDC25 session 219. Apple Human Interface design team (presenters introduced as Chan, Shubham and Bruno; a transcript index lists Chan Karunamuni, Shubham Kedia, Bruno Canales: full names U). June 2025. https://developer.apple.com/videos/play/wwdc2025/219/. V
- [A11] Get to know the new design system, WWDC25 session 356. Apple Design Team (presenter introduced as Maria). June 2025. https://developer.apple.com/videos/play/wwdc2025/356/. V
- [A12] Elevate the design of your iPad app, WWDC25 session 208. Apple. June 2025. https://developer.apple.com/videos/play/wwdc2025/208/. V
- [A13] Apple introduces a delightful and elegant new software design. Apple Newsroom. 2025-06-09. https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/. V
- [A14] Apple brings Final Cut Pro and Logic Pro to iPad. Apple Newsroom. 2023-05-09. https://www.apple.com/newsroom/2023/05/apple-brings-final-cut-pro-and-logic-pro-to-ipad/. V
- [A15] Apple Design Awards 2025, winners and finalists. Apple. June 2025. https://developer.apple.com/design/awards/2025/. V

### Google
- [G1] Expressive Design: Google's UX Research (also titled "Better, Easier, Emotional UX"). Google Design (no named author; acknowledgements name the research contributors listed in section 7). Date not printed, 2025 (U). https://design.google/library/expressive-material-design-google-research. V (content), U (date)
- [G2] Bentley, F., Schmidt, L., Sheehan, A., Gallardo, B., Wang, Y. Usability Hasn't Peaked: Exploring How Expressive Design Overcomes the Usability Plateau. CHI '26, Barcelona, April 2026. https://research.google/pubs/usability-hasnt-peaked-exploring-how-expressive-design-overcomes-the-usability-plateau/. V (abstract page)
- [G3] Benefits of expressive design. Android Developers (Wear OS design guides), Google. Undated. https://developer.android.com/design/ui/wear/guides/get-started/benefits. V
- [G4] Android and Wear OS are getting a big refresh. Mindy Brooks, blog.google. 2025-05-13. https://blog.google/products/android/material-3-expressive-android-wearos-launch/. V
- [G5] Make apps more accessible. Android Developers, Google. Undated. https://developer.android.com/guide/topics/ui/accessibility/apps. V
- [G6] Jetpack Compose Material 3 component guides. Android Developers, Google. Undated. V
  - [G6a] Button groups: https://developer.android.com/develop/ui/compose/components/button-group
  - [G6b] Split button: https://developer.android.com/develop/ui/compose/components/split-button
  - [G6c] FAB menu: https://developer.android.com/develop/ui/compose/components/fab-menu
  - [G6d] Floating toolbar: https://developer.android.com/develop/ui/compose/components/floating-toolbar
  - [G6e] Floating action button: https://developer.android.com/develop/ui/compose/components/fab
  - [G6f] Loading indicators: https://developer.android.com/develop/ui/compose/components/loading-indicator
- [G7] MotionScheme (API reference, material3 1.5.0). Android Developers, Google. https://developer.android.com/reference/kotlin/androidx/compose/material3/MotionScheme. V

### W3C
- [W1] Understanding SC 2.5.8: Target Size (Minimum). W3C WAI. Updated 2026-11-02. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. V
- [W2] Understanding SC 2.5.5: Target Size (Enhanced). W3C WAI. https://www.w3.org/WAI/WCAG22/Understanding/target-size-enhanced.html. V
- [W3] What's New in WCAG 2.2. W3C WAI. https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/. V

### Nielsen Norman Group (author, first published, last updated)
- [N1] Visual Hierarchy in UX: Definition. Kelley Gordon. 2021-01-17, updated 2024-01-30. https://www.nngroup.com/articles/visual-hierarchy-ux-definition/. V
- [N2] Progressive Disclosure. Jakob Nielsen. 2006-12-04, updated 2022-07-15. https://www.nngroup.com/articles/progressive-disclosure/. V, F
- [N3] Proximity Principle in Visual Design. Aurora Harley. 2020-08-02, updated 2024-01-30. https://www.nngroup.com/articles/gestalt-proximity/. V
- [N4] The Principle of Common Region: Containers Create Groupings. Aurora Harley. 2020-07-12, updated 2023-03-06. https://www.nngroup.com/articles/common-region/. V
- [N5] How Chunking Helps Content Processing. Kate Moran. 2016-03-20, updated 2024-02-02. https://www.nngroup.com/articles/chunking/. V
- [N6] Memory Recognition and Recall in User Interfaces. Raluca Budiu. 2024-01-15. https://www.nngroup.com/articles/recognition-and-recall/. V
- [N7] Designing Empty States in Complex Applications: 3 Guidelines. Kate Kaplan. 2021-09-19. https://www.nngroup.com/articles/empty-state-interface-design/. V
- [N8] Preventing User Errors: Avoiding Unconscious Slips. Page Laubheimer. 2015-08-23, updated 2023-07-01. https://www.nngroup.com/articles/slips/. V
- [N9] Confirmation Dialogs Can Prevent User Errors. Jakob Nielsen. 2018-02-18, updated 2026-08-07. https://www.nngroup.com/articles/confirmation-dialog/. V
- [N10] Minimize Cognitive Load to Maximize Usability. Kathryn Whitenton. 2013-12-22, updated 2025-11-25. https://www.nngroup.com/articles/minimize-cognitive-load/. V
- [N11] User Control and Freedom (Usability Heuristic #3). Maria Rosala. 2020-11-29, updated 2024-01-19. https://www.nngroup.com/articles/user-control-and-freedom/. V
- [N12] Plain Language Is for Everyone, Even Experts. Hoa Loranger. 2017-10-08, updated 2019-08-31. https://www.nngroup.com/articles/plain-language-experts/. V
- [N13] Simplicity Wins over Abundance of Choice. Hoa Loranger. 2015-11-22, updated 2022-07-15. https://www.nngroup.com/articles/simplicity-vs-choice/. V
- [N14] The Power of Defaults. Jakob Nielsen. 2005-09-26, updated 2024-11-28. https://www.nngroup.com/articles/the-power-of-defaults/. V, F
- [N15] Mobile-App Onboarding: An Analysis of Components and Techniques. Alita Kendrick. 2020-06-21, updated 2021-01-24. https://www.nngroup.com/articles/mobile-app-onboarding/. V
- [N16] Mobile Tutorials: Wasted Effort or Efficiency Boost? Alita Kendrick. 2020-03-08, updated 2021-01-24. https://www.nngroup.com/articles/mobile-tutorials/. V
- [N17] Onboarding Tutorials vs. Contextual Help. Page Laubheimer. 2023-02-12, updated 2024-02-13. https://www.nngroup.com/articles/onboarding-tutorials/. V
- [N18] Error-Message Guidelines. Evan Sunwall. 2023-05-15, updated 2024-08-02. https://www.nngroup.com/articles/error-message-guidelines/. V
- [N19] The Four Dimensions of Tone of Voice. Kate Moran. 2016-07-17, updated 2024-01-30. https://www.nngroup.com/articles/tone-of-voice-dimensions/. V
- [N20] Liquid Glass Is Cracked, and Usability Suffers in iOS 26. Raluca Budiu. 2025-10-10, updated 2026-03-18. https://www.nngroup.com/articles/liquid-glass/. V
- [N21] 10 Usability Heuristics for User Interface Design. Jakob Nielsen. 1994-04-24, updated 2026-08-20. https://www.nngroup.com/articles/ten-usability-heuristics/. V, F
- [N22] Touch Targets on Touchscreens. Aurora Harley. 2019-05-05, updated 2023-04-11. https://www.nngroup.com/articles/touch-target-size/. V
- [N23] Response Time Limits. Jakob Nielsen. 1993, updated 2024-01-31. https://www.nngroup.com/articles/response-times-3-important-limits/. V, F
- [N24] Visibility of System Status. Aurora Harley. 2018-06-03, updated 2024-01-26. https://www.nngroup.com/articles/visibility-system-status/. V
- [N25] Comparison Tables for Products, Services, and Features. Kate Moran. 2024-02-09, updated 2025-04-12. https://www.nngroup.com/articles/comparison-tables/. V

### Peer-reviewed papers
- [P1] Iyengar, S. S., Lepper, M. R. When choice is demotivating: Can one desire too much of a good thing? Journal of Personality and Social Psychology 79(6), 995 to 1006, 2000. doi:10.1037/0022-3514.79.6.995. PDF: https://faculty.washington.edu/jdb/345/345%20Articles/Iyengar%20&%20Lepper%20(2000).pdf. V (figures read in the PDF), F. Note: replications have been disputed, see P2 and P3.
- [P2] Scheibehenne, B., Greifeneder, R., Todd, P. M. Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload. Journal of Consumer Research 37(3), 409 to 425, 2010. doi:10.1086/651235. https://ideas.repec.org/a/oup/jconrs/v37y2010i3p409-425.html. V (abstract)
- [P3] Chernev, A., Böckenholt, U., Goodman, J. Choice overload: A conceptual review and meta-analysis. Journal of Consumer Psychology 25(2), 333 to 358, 2015. doi:10.1016/j.jcps.2014.08.002. https://www.kellogg.northwestern.edu/academics-research/research/detail/2015/when-product-assortment-leads-to-choice-overload-a-conceptual/. V (abstract)
- [P4] Hick, W. E. On the rate of gain of information. Quarterly Journal of Experimental Psychology 4(1), 11 to 26, 1952. doi:10.1080/17470215208416600. U, F
- [P5] Hyman, R. Stimulus information as a determinant of reaction time. Journal of Experimental Psychology 45(3), 188 to 196, 1953. doi:10.1037/h0056940. U, F
- [P6] Parhi, P., Karlson, A. K., Bederson, B. B. Target size study for one-handed thumb use on small touchscreen devices. MobileHCI 2006. doi:10.1145/1152215.1152260. Cited via [N22]. U
- [P7] McPherson, A. P., Jack, R. H., Moro, G. Action-Sound Latency: Are Our Tools Fast Enough? NIME 2016, pp. 20 to 25. https://nime.org/proc/mcpherson2016 (returned 404 when opened). The 10 ms latency and 1 ms jitter target is attributed to Wessel, D., Wright, M., Problems and prospects for intimate musical control of computers, Computer Music Journal, 2002. U (search abstracts only)

### Other
- [O1] Hoober, S. How Do Users Really Hold Mobile Devices? UXmatters, 2013-02-18. https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php. U (search abstract only), F
- [O2] Hoober, S. Design for Fingers, Touch, and People, Part 1. UXmatters, 2017-03-06. https://www.uxmatters.com/mt/archives/2017/03/design-for-fingers-touch-and-people-part-1.php. V
- [O3] Hick's Law. Jon Yablonski, Laws of UX. Undated. https://lawsofux.com/hicks-law/. V (pointer only, not primary evidence)
- [O4] Scott, E. Comparison tools article. Baymard Institute, 2022-10-19. https://baymard.com/blog/user-friendly-comparison-tools. V. Baymard's full comparison-tool guidelines are paywalled and were not read.
- [O5] J Dilla-inspired sampler makes it easy to create beats on your phone. Engadget, 2019-03-07 (interview with developer Marek Bereza). https://www.engadget.com/2019/03/07/koala-sampler/. V (press source, developer opinion)
- [O6] iOS 26.1 Clear or Tinted Liquid Glass setting. Press reports, e.g. 9to5Mac, 2025-10-21, https://9to5mac.com/2025/10/21/ios-26-1s-new-liquid-glass-setting-is-a-win-for-apple-and-users-alike/. U (not opened; partly corroborated by [A6], which mentions a preferred Liquid Glass look in device settings)

## Gaps and open questions
- No trusted, named-designer case studies found for GarageBand, BandLab, Smule, Yousician, Simply Sing or Moises interfaces; section 8 is platform guidance plus general evidence applied to the domain, not domain research.
- m3.material.io could not be read as text; Material 3 Expressive shape-library specifics and exact spring token values are not verified here.
- The design.google research article carries no date; CHI '26 [G2] is the citable peer-reviewed form of the speed claim (33% faster fixation, 20% faster tasks), with Google authors.
- No independent (non-Google) evaluation of Material 3 Expressive was found; the independent evaluation of Liquid Glass found is NN/g [N20], which conflicts with Apple's own framing.
