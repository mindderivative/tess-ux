---
title: Owner Feedback 2026-11-20
type: research
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [feedback, evidence, owner-feedback]
related: ["[[01 Principles and Scope]]", "[[02 Colour and Theming]]", "[[07 Spacing and Density Rules]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Tree]]", "[[Tree Node]]", "[[Text Field]]", "[[Switch]]", "[[Form Row]]", "[[Popup]]", "[[Theme Following the System]]", "[[Spacing and Density]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0005 Theme follows the system]]"]
depends_on: []
---

# Owner Feedback 2026-11-20

> [!info] Summary
> The owner's feedback from the live demo of the config app on 2026-11-20 (items F1 to F9) and two shell items (S1, S2), each linked to the rule and acceptance criteria it produced and to the status in each project at the time of writing (2026-11-21). The wording is the owner's, reported verbatim in condensed form by the lead; this note is the evidence the vault guide asks for ("maintainer feedback on real behaviour becomes a rule with the evidence linked").

## How to read this note

- Date: all F items are from the live demo of the config app, 2026-11-20. S1 and S2 come from the shell hand checks and the owner's decisions of 2026-11-06 to 2026-11-19.
- Source: "live demo" means the owner ran the config app (tess-ui `apps/shell_config`) on his desktop and spoke the observations.
- Rule: the note and the acceptance criteria prefix that now cover the observation. Criteria ids are defined in the linked note; a criterion is testable by the method named in [[Test Method]].
- Status per project: what the code did according to the project bots' verified facts of 2026-11-21 (tess-ui main after pull requests 328 to 330, tre 0.6.10, tess-shell origin/main). "Meets", "partly meets", "absent" are used as in the Status in code tables of the component notes.

## Items from the config app demo

| ID | Date | Source | Owner's observation (verbatim) | Rule produced | Status per project at the time |
|---|---|---|---|---|---|
| F1 | 2026-11-20 | live demo of the config app | The system theme was dark, but the app was all white except the tooltips. | The scheme follows the system by default; every surface, not only overlays, uses colour roles; no first-frame flash: [[Theme Following the System]], [[02 Colour and Theming]], [[ADR-0005 Theme follows the system]]; criteria AC-TH-* | tess-ui: `App(dark="system")` is the default and Linux reads the OS appearance at construction (unknown starts dark); an App with no `theme_seed` has no scheme and ignores dark, so surfaces stayed white (the config app now sets a seed); macOS and Windows answer after the window opens, so a flash is possible. tess-shell: the Default stylesheet is dark. tre: delivers `color_scheme` and `dark`; draws no scheme itself |
| F2 | 2026-11-20 | live demo of the config app | Tooltips do not disappear when the pointer leaves the node that spawned them. | Dismiss on pointer leave of the trigger, Escape, scroll of any ancestor, press or activation, trigger removed, window focus loss: [[Tooltip]], [[12 Overlays]], [[ADR-0004 Tooltip rule]]; criteria AC-TIP-* | tess-ui: hidden on pointer leave since pull request 328, on press, focus loss and Escape; not dismissed on scroll or on activation other than press. tre: no tooltip primitive and no timers. tess-shell: not covered by the demo |
| F3 | 2026-11-20 | live demo of the config app | The gaps in the tree indentation are way too large. | Tree indent per level 20, 16, 12 dp at default, compact, dense: [[Tree]], [[Tree Node]], [[07 Spacing and Density Rules]], [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]]; criteria AC-TRE-* | tess-ui: toolkit tree row 56 px (Compact 40), padding left 16 plus 24 per level, right 16, gap 8, chevron box 24 by 24, leaf spacer 24; the config app overrides to left 4 plus 16 per level, right 4, gap 4, Compact trees. Partly meets at compact (16 dp indent), fails at default and in the toolkit default |
| F4 | 2026-11-20 | live demo of the config app | The gap between the root tree chevron and the container edge is way too large. | The gap between the root chevron box and the container edge equals the row horizontal padding (12, 8, 4 dp), with no extra margin: [[Tree]], [[Tree Node]], [[Spacing and Density]]; criteria AC-TRE-* | tess-ui: toolkit left padding 16 px, which equals no density level (12, 8, 4 dp), so the toolkit fails at every level; the config app uses 4 px, which equals the dense value and not the compact value 8 dp it otherwise uses. tre: not applicable |
| F5 | 2026-11-20 | live demo of the config app | The Files directory text neither wraps nor has an ellipsis and runs past the parent container. | Content never overflows its container: single-line text ends in an ellipsis, wrapping text wraps, nothing draws outside its container: [[10 Layout Overflow and Scrolling]], [[Tree Node]], [[Text Field]] (AC-TXF-5, AC-TXF-6); criteria AC-LAY-* | tess-ui: the config app label has `Min_Width` 0 with an ellipsis (fixed in the app); the toolkit tree node label does not guarantee it. tre: `overflow="ellipsis"` exists for text input, `max_lines` and `overflow` for text. Partly meets |
| F6 | 2026-11-20 | live demo of the config app | There are no horizontal scroll bars although every panel has content past the visual frame. | Scrollbars on both axes, visible when content overflows on that axis, no auto-hide by default on desktop: [[Scrollbar and Scroll Container]], [[10 Layout Overflow and Scrolling]], [[ADR-0003 Scrollbar rule]]; criteria AC-SCB-* | tess-ui: `ScrollView` scrolls one axis (its `Orientation`), the two-axis form is planned (`feat/scrollview-two-way`); bar colour `outline`; width and hit area are engine-owned. tre 0.6.10: `scroll_view` is one axis only (nest a horizontal in a vertical); thumb 4 px, 2 px margin, 32 px minimum length, 6 px grab slop, no track, no auto-hide; `virtual_list` has a draggable vertical thumb and no key handling. Absent for horizontal and for two-axis containers |
| F7 | 2026-11-20 | live demo of the config app | Text in text fields is top aligned. Left alignment is right; vertical must be centred for single-line fields. | Vertical centring by construction at every density, horizontal alignment at the start: [[Text Field]] (AC-TXF-1, AC-TXF-2, AC-TXF-4), [[Spacing and Density]]; criteria AC-TXF-* | tess-ui: the config single-line `TextInput` is 32 px high with top and bottom padding and 8 px left and right; the engine `text_input` has no vertical-align property, so centring is by padding. tre: no vertical-align property. tess-shell: `TextInput` module relies on the same engine. Partly meets (padding is hand-tuned) |
| F8 | 2026-11-20 | live demo of the config app | Tooltips appear on the whole row of a feature: hovering the label, the switch or the reset button shows the tooltip of the whole group immediately and the element's own, and they cover the panel and do not go away. The owner guessed the parent container carries the tooltip instead of the text or switch. | The tooltip belongs to the control, the smallest element carrying the label, icon, switch, button or reset, never to a row, group or container; one tooltip visible at a time; 500 ms delay: [[Tooltip]], [[Switch]] (AC-SWI-8), [[Icon Button]] (AC-ICB-6), [[Form Row]], [[ADR-0004 Tooltip rule]]; criteria AC-TIP-* | tess-ui: tooltips are 500 ms (`TIP_DELAY`), one at a time, and the scope is whatever node carries the `Tooltip` key, so the toolkit allows rows; the config form now puts the documentation tooltip on the label box only. tre: no primitive. tess-shell: not applicable to the demo. Partly meets |
| F9 | 2026-11-20 | live demo of the config app | Clicking the switch drew tooltip text over everything with no background. | A tooltip always has an opaque container and is clipped to the window; a press on the trigger dismisses it; a click on a switch draws nothing outside its container: [[Tooltip]], [[Switch]] (AC-SWI-5), [[12 Overlays]], [[ADR-0004 Tooltip rule]]; criteria AC-TIP-* | tess-ui: tooltip hidden on pointer press since pull request 328; the cause of the background-less text is not recorded in the project facts and no test covers it. tre: layers clip to the host window; draws no container. Unmeasured |

## Shell items

| ID | Date | Source | Observation | Rule produced | Status per project at the time |
|---|---|---|---|---|---|
| S1 | 2026-11 (date of shell ADR-0022) | shell hand checks, shell ADR-0022 (default stylesheet accepted) | The shell Launcher is unreadable with no stylesheet. | A surface with no project stylesheet still shows a readable look: the app falls back to the baseline scheme and a default stylesheet, and still follows light and dark: [[02 Colour and Theming]], [[Theme Following the System]], [[Popup]] (AC-POP-*), [[ADR-0005 Theme follows the system]]; criteria AC-TH-* | tess-shell: `src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` exists and ADR-0022 of the shell accepts a default stylesheet; whether every shipped module is readable with it has no recorded contrast script result. tess-ui: an App with no seed has no scheme. tre: not applicable |
| S2 | 2026-11-06 | shell hand checks on KWin | A click-away layer sits under the Launcher, and the popup grab steals the keyboard on KWin. | A popup or launcher dismisses on outside click and Escape without a full-screen input layer that takes the keyboard, focus returns to the opener on close: [[Popup]] (AC-POP-*), [[12 Overlays]], [[14 Accessibility Basics]]; criteria AC-POP-* | tess-shell: closes a focused Popup on Escape itself (`tess-shell:src/tess_shell/surfaces/popup.py`, `_key`); not verified on real KWin and no test found. Shadow click-through fixed by tre 0.6.5 `input_region`. tre: layers clip to the host window. Partly meets, unverified |

## What these items produced

- Principles: the content-never-overflows rule, the keyboard-first rule, density by choice and testable rules in [[01 Principles and Scope]].
- Foundations: [[Theme Following the System]], [[Spacing and Density]].
- Chapters: [[02 Colour and Theming]], [[07 Spacing and Density Rules]], [[10 Layout Overflow and Scrolling]], [[12 Overlays]], [[14 Accessibility Basics]].
- Components: [[Tooltip]], [[Scrollbar and Scroll Container]], [[Tree]], [[Tree Node]], [[Text Field]], [[Switch]], [[Icon Button]], [[Button]], [[Form Row]], [[Popup]].

## Sources

- Owner feedback, config app live demo, 2026-11-20 (reported by the lead; this note reproduces it).
- Project facts verified in code on 2026-11-21: `tess-ui:src/tess_ui/views/TreeNode_Stylesheet.tdl`, `tess-ui:src/tess_ui/composed.py`, `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_Stylesheet.tdl`, `tre:crates/engine-core/src/tree/scroll.rs`, `tess-shell:src/tess_shell/surfaces/popup.py`.
- [[Gaps and Contradictions]] items on popup faults found on KWin (2026-11-06) and on the missing contrast script.
