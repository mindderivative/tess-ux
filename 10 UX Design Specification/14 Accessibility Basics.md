---
title: 14 Accessibility Basics
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, accessibility]
related: ["[[01 Principles and Scope]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Colour Roles]]", "[[Focus Ring]]", "[[Motion]]", "[[Spacing and Density]]", "[[Tooltip]]", "[[Popup]]", "[[Text Field]]", "[[Switch]]", "[[Icon Button]]", "[[Button]]", "[[12 Overlays]]", "[[10 Layout Overflow and Scrolling]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[Colour Roles]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[ADR-0004 Tooltip rule]]"]
---

# 14 Accessibility Basics

> [!info] Summary
> Accessibility rules every element of the first slice follows: roles and names, focus, keyboard-only use, contrast, target size, tooltips, announcements, reduced motion and high contrast; the support level each project has today; and the criteria that test them. The checklist form is [[Accessibility Rules]]; the test types are in [[Test Method]].

## Scope

Covers what the first slice (tooltip, popup, menu, dialog, panel, scrollbar, tree, list, accordion, form row, text field, switch, icon button, button) needs from assistive technology (AT) and from keyboard and low-vision users. Full patterns (error recovery, forms flow, notifications) are chapter 13 and later. Standards: [WCAG 2.2](https://www.w3.org/TR/WCAG22/) at level AA where a criterion is named, [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) role names.

## Roles and accessible names

- Every interactive node has a role and an accessible name (WCAG 2.2 SC 4.1.2). Role per element: Button `button`; Icon Button `button`; Switch `switch` with `checked`; Text Field `textbox` or `searchbox`; Tree `tree` with `treeitem` rows and `expanded`, `selected`, level; List `list` with `listitem`; Menu `menu` with `menuitem`, `menuitemcheckbox`; Dialog `dialog` (modal); Tooltip `tooltip`; Scroll container with a name when focusable; separators `separator`.
- Name source: the visible label text; for an icon-only control, the tooltip text (the same string); for a field, the associated label. Name text starts with the visible label text (WCAG 2.2 SC 2.5.3 label in name).
- Decorative icons, images and shapes are hidden from AT; an icon with the only meaning has a name.
- State flags are set by the control, never by the author: `checked`, `selected`, `expanded`, `pressed`, `disabled`, `invalid`, `busy`, `read_only`, `value`.
- `disabled` in tre is announce-only; a Tesserae control suppresses focus and input itself (`tre:docs/guide/accessibility.md`; `tess-ui:src/tess_ui/a11y.py`).
- A description (separate from the name) carries help and error text; a tooltip's text is also the control's description, so the tooltip is not the only source ([[Tooltip]], tess-shell rule 11).

## Focus order and visibility

- Focus order follows the visual and reading order (WCAG 2.2 SC 2.4.3); no positive tab indexes; a control that cannot be focused is not interactive.
- The focus indicator is visible on every focusable control under keyboard focus ([WCAG 2.4.7](https://www.w3.org/TR/WCAG22/#focus-visible)): 3 dp ring, 2 dp offset, role `secondary`, contrast at least 3 to 1 ([[Focus Ring]]); text fields use their 2 dp indicator or outline ([[Text Field]]).
- The focused control is not hidden by another element: a sticky header, a tooltip or a popup does not cover it entirely ([WCAG 2.4.11 Focus Not Obscured (Minimum)](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum)). A tooltip appears beside the trigger, never over it.
- Focus moves into a modal dialog on open and returns to the opener on close; a popup or menu that closes returns focus to its opener ([[12 Overlays]], [[Popup]]).
- Focus in a scroll container scrolls the focused item into view ([[10 Layout Overflow and Scrolling]]).

## Keyboard-only operation

- Everything operable by pointer is operable by keyboard (WCAG 2.2 SC 2.1.1). No keyboard trap (SC 2.1.2): a multi-line text field lets Tab leave unless `tab_navigates` is false, and then documents Escape followed by Tab ([[Text Field]]).
- Keys: Tab and Shift+Tab move focus; Enter and Space activate a button; Space toggles a switch; arrow keys move within a tree, list, menu; Escape closes the topmost transient layer (tooltip, menu, popup, dialog) and does nothing else; Home, End, Page keys move in lists and scroll containers ([[Scrollbar and Scroll Container]]).
- A single-character shortcut is not defined without a modifier unless the user can turn it off (WCAG 2.2 SC 2.1.4).
- Hover-only information has a keyboard path: tooltips appear on keyboard focus ([[ADR-0004 Tooltip rule]]); rich tooltips with actions are reachable by Tab or a documented key.

## Contrast

- Text against its background at least 4.5 to 1 (3 to 1 for large text: 24 dp or 18.66 dp bold) ([WCAG 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum)).
- Non-text parts (icons, switch track and handle, outlines, focus indicator, scrollbar thumb) at least 3 to 1 against the adjacent colour ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)).
- Pairs are checked per colour role pair in light and dark with the contrast script defined in [[Test Method]]; role pairs and their guarantees are in [[Colour Roles]]. Disabled controls are exempt from the ratio but still distinguishable by more than colour.
- Colour is never the only carrier: an error shows an icon or text, a selected switch shows handle position, a checked item shows a mark ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).
- The scrollbar thumb colour rule of [[ADR-0003 Scrollbar rule]] is checked against 3 to 1 in AC-A11Y-6; the proposed rest alpha (38 percent of `on_surface_variant`) may fail it on some surfaces #needs-verification.

## Target size

- Pointer targets at least 24 dp by 24 dp or spaced so a 24 dp circle around each does not meet another target ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)); the density floors 28 (dense), 32 (compact), 40 (default) dp meet it ([[ADR-0002 Desktop density levels and target sizes]]).
- Touch contexts: 48 dp hit area ([[Icon Button]], [[Button]], [[Switch]]).

## Tooltips are not the only source

- A tooltip only repeats or adds to what a visible label, the accessible name or the accessible description gives; information needed to use the control is never only in a tooltip ([[Tooltip]], [[ADR-0004 Tooltip rule]]).
- Tooltip text is exposed as description or, for an icon-only control, as the name.
- WCAG 2.2 SC [1.4.13 Content on Hover or Focus](https://www.w3.org/TR/WCAG22/#content-on-hover-or-focus) asks that hover content is dismissible, hoverable and persistent. All tooltips, plain and rich, meet it ([[ADR-0011 Tooltip hover grace for all tooltips]]): Escape dismisses without moving the pointer, the pointer can move from the trigger onto the tooltip within a 150 ms grace and the tooltip then stays open, and the tooltip stays until the pointer leaves both, focus leaves, or Escape.

## Announcements and live regions

- A live region (`live="polite"` or `"assertive"`) announces changes to its name or text; the announcement happens when the name changes or when the node enters the tree (`tre:docs/guide/accessibility.md`). Polite waits for the reader to finish; assertive interrupts and is reserved for what the user must act on (critical battery, data loss).
- Announcing without a node: `window.announce(text, politeness)` (tre 0.6.9) raises one announcement per call; a repeated text is announced again, so removing duplicates is the caller's job. Calls are heard in call order within one window (tre 0.6.10); six messages take about six frames (about 100 ms at 60 Hz); the queue holds 16 and the newest are kept; empty text or any politeness other than `polite` or `assertive` raises `ValueError`. The shell sends announcements through one window (Frame, else Bar) by the owner's decision of 2026-11-19. Order across windows is not guaranteed.
- Rules for the specification: validation errors and status messages use a polite live region or polite announce (WCAG 2.2 SC 4.1.3 status messages); an error is announced once when it appears, not on each keystroke; the result of a long action is announced when it ends; loading uses `busy`; no more than one announcement per user action unless the action has several independent results; selection moves in a list that owns a text field are announced with polite messages until `active_descendant` is released (tre TRE-REQ-023).
- Window-wide announcements that are not tied to a focused control are checked by scripted input against the tre announce queue, not by a screen reader, today.

## Reduced motion

- The OS preference is read at start and tracked: tre `window.get("reduced_motion")` and the `reduced_motion` event (0.5.4); `True` when the user asked for less motion, unknown on platforms that cannot say.
- With the preference on, animation that is not essential is replaced by an immediate state change (WCAG 2.2 SC 2.3.3 Animation from Interactions, AAA; Tesserae adopts it as a MUST): handle slides, label glides, ripple, slide-in surfaces, expand and collapse, caret glide and blink, typing effects flash and fade; the caret is steady; spinners and progress that convey activity may keep moving at no more than 3 flashes per second ([[Motion]]).
- tess-ui reads the preference for typing effects and caret (`tess-ui:docs/components/text-fields.md`); tess-shell lists the animations that honour it (Toggle, Expander, Marquee, ProgressBar, peek) in `tess-shell:docs/design/60 Quality/Accessibility.md`, tested headless only.

## High contrast

- The OS preference is read at start and tracked: tre `window.get("high_contrast")` and the `high_contrast` event (0.5.4).
- With the preference on, the scheme resolves to the high-contrast scheme of [[Colour Roles]] (text at least 7 to 1 and non-text at least 4.5 to 1 #needs-verification-as-design-choice), outlines are drawn on controls that rest on a similar surface, and elevation shadows are replaced by outlines; no information is lost.
- tess-shell tests it headless only (the owner's desktop has no such setting); the portal path reports it where the desktop does.

## Screen reader support level today

| Project | Level | Evidence |
|---|---|---|
| tre | Accessibility tree built (roles, names, states, live regions, announce, text selection and links) and checked against AccessKit's own consumer and, for `announce`, against AT-SPI's `Announcement` signal on a private bus; not tried with Orca, NVDA or VoiceOver | `tre:docs/guide/accessibility.md` |
| tess-ui | Roles, names and states set by controls and views (a11y keys `Label`, `Description`, `Role`); tests assert them on the tree (`tess-ui:tests/test_a11y*.py`); no real screen reader run | `tess-ui:src/tess_ui/a11y.py` |
| tess-shell | Roles, names, states, live regions and one-window announcements built; Orca is not installed on the owner's machine so Launcher and announcements are untested; `active_descendant` for the Launcher list waits for tre; high contrast and reduced motion headless only; no contrast script exists | `tess-shell:docs/design/60 Quality/Accessibility.md`, Hand Checks |

What the specification requires regardless: roles, names, states and descriptions exactly as in [[Accessibility Rules]]; the tests of [[Test Method]] (AT tree assertion) run on the tree; a screen-reader pass with Orca (Linux), NVDA (Windows) and VoiceOver (macOS) is a review item of the adoption audit, recorded as "not run" until done, never as "passes".

## Acceptance criteria

- [ ] AC-A11Y-1: AT tree assertion. Every interactive node in a view has a role and a non-empty name; nodes with only an icon are hidden unless named. Pass: zero interactive nodes without name or role in the tree walk of each documented view.
- [ ] AC-A11Y-2: Scripted input. Tab from the first control visits every focusable control once in visual order and returns to the start; no key sequence of Tab, Shift+Tab, arrows, Escape leaves the focus stuck (no trap). Pass: visited sequence equals the expected order list.
- [ ] AC-A11Y-3: Pixel check. Every focusable control shows a focus indicator under keyboard focus with a ring 3 dp wide at 2 dp offset (text field: 2 dp indicator or outline), and the indicator is not covered by any other layer. Pass: indicator pixels present, none occluded.
- [ ] AC-A11Y-4: Scripted input. Every action in a documented view is performed by keyboard only; the script drives the view with key events only (the tess-ui test pattern from `docs/guide/shell-config.md`) and reaches each action. Pass: every action's effect observed.
- [ ] AC-A11Y-5: Contrast script. For every role pair listed in [[Colour Roles]] and every shipped scheme (light, dark, high contrast), text pairs at least 4.5 to 1 (3 to 1 large) and non-text pairs at least 3 to 1. Pass: no pair below the limit.
- [ ] AC-A11Y-6: Contrast script. The scrollbar thumb at rest, hover and drag (rest alpha per [[ADR-0003 Scrollbar rule]]) against the container surface in light and dark at least 3 to 1. Pass: ratios at or above 3 to 1 or a recorded exception.
- [ ] AC-A11Y-7: Geometry check. Every interactive node's pointer hit area is at least 24 dp by 24 dp at each density, or a 24 dp circle around its centre meets no other target. Pass: all nodes pass.
- [ ] AC-A11Y-8: Scripted input. Every tooltip shown by hover is also shown by keyboard focus within one frame, and its text is present as description or name on the same node. Pass: tooltip visible and description equal.
- [ ] AC-A11Y-9: AT tree assertion. Any information shown only in a tooltip is also in the node's description or visible text. Pass: set of tooltip-only strings is empty in the review of each view.
- [ ] AC-A11Y-10: Scripted input. `announce` sequence: call announce with three texts in one loop turn and read the tre announce queue: order equals call order and the queue length stays at most 16, dropping the oldest when exceeded. Pass: order and length equal.
- [ ] AC-A11Y-11: AT tree assertion. An error message appears in a polite live region, once; the field is `invalid`; typing further characters does not raise another announcement while the message is unchanged. Pass: announcement count 1.
- [ ] AC-A11Y-12: Scripted input. With `reduced_motion` simulated true, a switch toggle, a label glide and a caret finish within one frame and the caret does not blink; with it false they animate at the documented durations. Pass: frame counts equal.
- [ ] AC-A11Y-13: Scripted input. With `high_contrast` simulated true, the app resolves the high-contrast scheme without restart and AC-A11Y-5 holds for it. Pass: scheme name equals and ratios pass.
- [ ] AC-A11Y-14: Review. A screen reader pass (Orca, NVDA, VoiceOver) on one view per project: roles, names, states and announcements as in [[Accessibility Rules]]. Pass: the audit records each reader as passed, failed with defects, or "not run".
- [ ] AC-A11Y-15: Scripted input. Focus moves into a modal dialog on open, returns to the opener on close, and Escape closes the topmost transient layer only. Pass: focus owner equals at each step.
- [ ] AC-A11Y-16: Pixel check. In a view with a state shown by colour (error, selected, checked, disabled) the same state differs in at least one non-colour feature (icon, shape, text, position). Pass: the greyscale render differs between states.

## Sources

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.1, 1.4.3, 1.4.11, 1.4.13, 2.1.1, 2.1.2, 2.1.4, 2.3.3, 2.4.3, 2.4.7, 2.4.11, 2.5.3, 2.5.8, 4.1.2, 4.1.3 (section anchors present in the page, checked).
- [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) for role names; [WAI-ARIA Authoring Practices, Switch pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch/).
- tre accessibility guide: `tre:docs/guide/accessibility.md` (live regions, `announce`, active descendant, testing); `tre:docs/reference/events.md` (`reduced_motion`, `high_contrast`).
- tess-shell accessibility note: `tess-shell:docs/design/60 Quality/Accessibility.md` (rules 1 to 12); Hand Checks kit M7g.
- Shell and engine facts of 2026-11-17 to 2026-11-19 as recorded in [[Gaps and Contradictions]].
- WCAG anchors for SC 1.4.1, 1.4.3, 1.4.11, 1.4.13, 2.1.1, 2.1.4, 2.3.3, 2.4.3, 2.4.7, 2.4.11, 2.5.3, 2.5.8, 4.1.2, 4.1.3 were found in the fetched page; the 7 to 1 and 4.5 to 1 high-contrast figures are Tesserae design choices, marked #needs-verification-as-design-choice.
