---
title: Accessibility Rules
type: quality
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [quality, accessibility, checklist]
related: ["[[14 Accessibility Basics]]", "[[Test Method]]", "[[01 Principles and Scope]]", "[[Text Field]]", "[[Switch]]", "[[Icon Button]]", "[[Button]]", "[[Tooltip]]", "[[Popup]]", "[[Menu]]", "[[Dialog]]", "[[Scrollbar and Scroll Container]]", "[[Tree]]", "[[List]]", "[[Colour Roles]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]"]
depends_on: ["[[14 Accessibility Basics]]", "[[Test Method]]"]
---

# Accessibility Rules

> [!info] Summary
> The checklist form of [[14 Accessibility Basics]]: each rule has an id `AR-n`, one statement that passes or fails, the test type from [[Test Method]], the acceptance criterion or note where it is defined, and the standard behind it. Use it for design review and for the accessibility rows of an adoption audit.

How to use: go down the list for every view; mark pass, fail or not run; link failures to a defect. A rule that does not apply (no text field in the view) is marked not applicable with the reason.

## Roles, names and states

| ID | Rule | Test type | Defined in | Standard |
|---|---|---|---|---|
| AR-1 | Every interactive node has a role and a non-empty accessible name. | AT tree assertion | AC-A11Y-1 | WCAG 2.2 SC 4.1.2 |
| AR-2 | The role matches the element: Button `button`, Icon Button `button`, Switch `switch`, Text Field `textbox` or `searchbox`, Tree `tree` with `treeitem`, List `list` with `listitem`, Menu `menu` with `menuitem`, Dialog `dialog`, Tooltip `tooltip`. | AT tree assertion | AC-BTN-7, AC-ICB-5, AC-SWI-6, AC-TXF-9 | WAI-ARIA 1.2 |
| AR-3 | The accessible name begins with the visible label text; an icon-only control's name equals its tooltip text. | AT tree assertion | AC-ICB-5, AC-ICB-6 | WCAG 2.2 SC 2.5.3 |
| AR-4 | State flags (`checked`, `selected`, `expanded`, `pressed`, `disabled`, `invalid`, `busy`, `read_only`) are set by the control from its state and read back correctly. | AT tree assertion | AC-SWI-6, AC-BTN-7, AC-TXF-9 | WCAG 2.2 SC 4.1.2 |
| AR-5 | Decorative icons, images and shapes are hidden from assistive technology unless they carry the only meaning, then they are named. | AT tree assertion | AC-A11Y-1, AC-ICB-5 | WCAG 2.2 SC 1.1.1 |
| AR-6 | Help and error text are the accessible description of their field; the field is `invalid` while an error shows. | AT tree assertion | AC-TXF-9 | WCAG 2.2 SC 3.3.1 |
| AR-7 | A disabled control takes no focus, no pointer and no key; the engine flag alone is not enough. | scripted input | AC-SWI-3, AC-BTN-5, AC-ICB-4, AC-TXF-10 | tre accessibility guide |

## Focus and keyboard

| ID | Rule | Test type | Defined in | Standard |
|---|---|---|---|---|
| AR-8 | Tab and Shift+Tab visit every focusable control once in visual order and return to the start; there is no trap. | scripted input | AC-A11Y-2 | WCAG 2.2 SC 2.1.2, 2.4.3 |
| AR-9 | Every action reachable by pointer is reachable by keyboard only. | scripted input | AC-A11Y-4 | WCAG 2.2 SC 2.1.1 |
| AR-10 | A keyboard-focused control shows a focus indicator: ring 3 dp, offset 2 dp, role `secondary`; text fields use the 2 dp indicator or outline; not shown for mouse-click focus. | pixel check | AC-A11Y-3, AC-BTN-11 | WCAG 2.2 SC 2.4.7 |
| AR-11 | The focus indicator is never hidden by another layer, including a tooltip. | pixel check | AC-A11Y-3 | WCAG 2.2 SC 2.4.11 |
| AR-12 | Enter and Space activate a button; Space toggles a switch; Escape closes only the topmost transient layer. | scripted input | AC-BTN-5, AC-SWI-3, AC-A11Y-15 | WAI-ARIA Authoring Practices |
| AR-13 | Focus moves into a modal dialog on open and returns to the opener on close; a closing popup or menu returns focus to its opener. | scripted input | AC-A11Y-15, [[Dialog]], [[Popup]] | WCAG 2.2 SC 2.4.3 |
| AR-14 | Focus in a scroll container, tree or list scrolls the focused item into view; Home, End, Page keys work. | scripted input | [[Scrollbar and Scroll Container]], [[Tree]], [[List]] | WCAG 2.2 SC 2.1.1 |
| AR-15 | A multi-line text field lets Tab leave it (or documents Escape then Tab). | scripted input | AC-TXF-8 | WCAG 2.2 SC 2.1.2 |

## Contrast, colour and size

| ID | Rule | Test type | Defined in | Standard |
|---|---|---|---|---|
| AR-16 | Text pairs have contrast at least 4.5 to 1 (3 to 1 for large text) in light, dark and high contrast. | contrast script | AC-A11Y-5, AC-TXF-11, AC-BTN-9 | WCAG 2.2 SC 1.4.3 |
| AR-17 | Non-text parts (icons, switch, outlines, focus indicator, scrollbar thumb) have contrast at least 3 to 1 against the adjacent colour. | contrast script | AC-A11Y-5, AC-A11Y-6, AC-SWI-7, AC-ICB-8 | WCAG 2.2 SC 1.4.11 |
| AR-18 | Colour is never the only carrier of a state: each state differs in a shape, icon, text or position. | pixel check | AC-A11Y-16, AC-ICB-9 | WCAG 2.2 SC 1.4.1 |
| AR-19 | Pointer targets are at least 24 dp by 24 dp or spaced by a 24 dp circle; touch hit areas are 48 dp. | geometry check | AC-A11Y-7, AC-SWI-9, AC-ICB-2, AC-BTN-8 | WCAG 2.2 SC 2.5.8 |
| AR-20 | Every colour comes from a role; no component carries a literal. | token test | AC-PRI-2, AC-TXF-12, AC-BTN-4 | vault principle 3 |

## Tooltips and overlays

| ID | Rule | Test type | Defined in | Standard |
|---|---|---|---|---|
| AR-21 | Information needed to use a control is not only in a tooltip: it is in the visible label, the name or the description. | AT tree assertion | AC-A11Y-9 | WCAG 2.2 SC 1.3.1, [[ADR-0004 Tooltip rule]] |
| AR-22 | A tooltip appears on keyboard focus within one frame as it does on hover after 500 ms, and Escape dismisses it. | scripted input | AC-A11Y-8, AC-ICB-6 | WCAG 2.2 SC 1.4.13 |
| AR-23 | A tooltip has an opaque container and is clipped to the window. | pixel check | AC-SWI-5, AC-TIP-* in [[Tooltip]] | [[ADR-0004 Tooltip rule]] |

## Announcements, motion and contrast preferences

| ID | Rule | Test type | Defined in | Standard |
|---|---|---|---|---|
| AR-24 | A validation error or status message is announced once through a polite live region or polite announce; assertive only for what the user must act on. | AT tree assertion | AC-A11Y-11 | WCAG 2.2 SC 4.1.3 |
| AR-25 | Announce calls are heard in call order and the queue stays at 16 or fewer, the oldest dropped. | scripted input | AC-A11Y-10 | tre 0.6.10 behaviour |
| AR-26 | Loading is exposed as `busy`; the end of a long action is announced. | AT tree assertion | AC-BTN-7 | WCAG 2.2 SC 4.1.3 |
| AR-27 | With the OS reduced-motion preference on, non-essential animation is replaced by an immediate change and the caret is steady. | scripted input | AC-A11Y-12, AC-SWI-10, AC-TXF-15 | WCAG 2.2 SC 2.3.3 |
| AR-28 | With the OS high-contrast preference on, the high-contrast scheme resolves without restart and AR-16 and AR-17 hold. | scripted input | AC-A11Y-13 | WCAG 2.2 SC 1.4.3, 1.4.11 |

## Review items (not automatable)

| ID | Rule | Test type | Defined in | Standard |
|---|---|---|---|---|
| AR-29 | A screen-reader pass on one view per project with Orca, NVDA and VoiceOver; result recorded as pass, fail or not run. | review | AC-A11Y-14 | project audit |
| AR-30 | One filled (primary-emphasis) button per view region; icon-only buttons all named. | review | AC-BTN-12 | MD3 emphasis order |

## Status today

No project has run a real screen reader (Orca, NVDA, VoiceOver); AR-29 is "not run" for tess-ui, tess-shell and tre. The contrast script (AR-16, AR-17, AR-28) does not exist in any project. tess-shell has AR-1, AR-3 and AR-4 tests through module role and state keys; tess-ui asserts roles in `tests/test_a11y*.py`; tre checks `announce` against AT-SPI on a private bus. Details: [[14 Accessibility Basics]], Screen reader support level today.

## Acceptance criteria

- [ ] AC-AR-1: Review. Every `AR-n` row names a test type of [[Test Method]], an id of an acceptance criterion or note, and a standard. Pass: no empty cell in any table.
- [ ] AC-AR-2: Review. Each id `AC-A11Y-n` and each component criterion referenced here exists in its note. Pass: a script resolving the references finds zero broken ids (the `AC-TIP-*` reference resolves to the criteria of [[Tooltip]] once that note is written).

## Sources

- [[14 Accessibility Basics]] and its sources.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.1.1, 1.3.1, 3.3.1 are cited by number only and their anchors were not separately fetched; the other SC anchors were checked in the fetched page.
- [WAI-ARIA 1.2](https://www.w3.org/TR/wai-aria-1.2/) role names.
