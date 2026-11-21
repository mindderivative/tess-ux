---
title: 03 Typography and Text Rules
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, typography, text, overflow]
related: ["[[Typography]]", "[[10 Layout Overflow and Scrolling]]", "[[07 Spacing and Density Rules]]", "[[02 Colour and Theming]]", "[[01 Principles and Scope]]", "[[14 Accessibility Basics]]", "[[Owner Feedback 2026-11-20]]", "[[Tooltip]]", "[[Text Field]]", "[[Button]]", "[[Menu]]", "[[List Item]]", "[[Tree Node]]", "[[Dialog]]", "[[Colour Roles]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[Deviations from MD3]]"]
depends_on: ["[[Typography]]", "[[10 Layout Overflow and Scrolling]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# 03 Typography and Text Rules

> [!info] Summary
> Chapter-level principles for choosing a type role, centring and truncating text, and tracking and families. The 15 roles and their values live in [[Typography]]; the overflow mechanics (ellipsis, wrap, minimum widths) live in [[10 Layout Overflow and Scrolling]]. This chapter states which role an element class takes and copies no value. Material Design 3 baseline: [type scale](https://m3.material.io/styles/typography/overview).

## Purpose

Text is most of what a Tesserae window shows. Two owner observations (F5, a path label running past its container; F7, single-line text sitting at the top of a field; [[Owner Feedback 2026-11-20]]) show the failures this chapter prevents: text that ignores its box and text that is placed by tuned padding. The chapter makes both a testable property of every component note.

## Scope

- In scope: which type role each class of element uses, the vertical centring rule across components, the truncation rule across components, tracking, families and text colour.
- Out of scope: the role values ([[Typography]]), the mechanics of wrapping and minimum widths ([[10 Layout Overflow and Scrolling]]), text colour roles ([[Colour Roles]]), the text field's own behaviour ([[Text Field]]).

## Principles

1. Roles, not sizes. Text takes size, line height, weight and tracking from a named role of [[Typography]]. A literal size is a defect except for user content ([[ADR-0001 MD3 role names are the specification vocabulary]]).
2. One role per job. The same kind of text takes the same role in every component and every project: all button labels share a role, all menu item labels share a role. A reader who learns one dialog reads every dialog.
3. The line box decides the geometry. Layout uses the line height of the role, not the ink of the glyphs; a control is never shorter than its line box plus the padding that keeps text centred ([[07 Spacing and Density Rules]]).
4. Centre by construction. Single-line text sits at the vertical centre of its control at every density (F7, [[Typography]] rule 4).
5. Text ends, it does not escape. Text that cannot fit ends with an ellipsis or wraps or scrolls; it never paints outside its box (F5, [[10 Layout Overflow and Scrolling]]).
6. Truncated text stays readable. The full text is available by a tooltip on the control that carries the text ([[ADR-0004 Tooltip rule]]) and by selection or accessible name; the tooltip is never the only source ([[14 Accessibility Basics]]).
7. Density does not change the role. A compact or dense level changes heights and padding, not type size; a role is the same size at every level ([[07 Spacing and Density Rules]]). A project that needs smaller text at the dense level states it as a deviation.
8. Text colour comes from an `on_` role and meets contrast ([[Colour Roles]]).

## Which role for which element class

The role is a rule of the chapter; the component note repeats the role name for its own parts and links here ([[Typography]] AC-TYP-9).

| Element class | Role | Basis |
|---|---|---|
| Button, chip, dialog action, snackbar action, rich tooltip action label | `label_large` | verified in the Material Web component tokens `_md-comp-filled-button.scss`, `_md-comp-assist-chip.scss`, `_md-comp-dialog.scss`, `_md-comp-snackbar.scss`, `_md-comp-rich-tooltip.scss` |
| Plain tooltip text | `body_small` | verified in `_md-comp-plain-tooltip.scss` |
| Text field input text and value | `body_large` at the default level | MD3 text field; tracking and size of the compact and dense levels are stated in [[Text Field]] #needs-verification |
| Text field label and supporting text | `body_small` when the label floats, `body_large` at rest; supporting text `body_small` | MD3 text field #needs-verification |
| List item headline, tree row, menu item label | `body_large` at the default level; `body_medium` at compact and dense, so the line box (20 dp) fits the 32 and 28 dp rows | density rule of [[07 Spacing and Density Rules]]; MD3 value for menu and list items not re-read #needs-verification |
| List item supporting text, caption, helper text | `body_small` | MD3 supporting text pattern |
| Section header in a panel, group title in a form | `title_small` | Tesserae choice #needs-verification |
| Dialog title | `headline_small` | MD3 dialog #needs-verification; stated in [[Dialog]] |
| Panel title, card title | `title_medium` | MD3 card pattern #needs-verification |
| Status bar and badge text | `label_small` (the 11 dp minimum) | [[Typography]] rule 2 |
| Page title, display text | `headline_*`, `display_*` | rare in desktop tools; allowed where a note names it |

The shell's five type roles map to these by [[Typography]] (Mapping of the tess-shell type roles).

## Vertical centring across components

- Every control that holds single-line text (button, text field, list row, tree row, menu item, switch row, tab, chip) centres the line box at the centre of its content box, at all three density levels. The geometry is in [[10 Layout Overflow and Scrolling]] (Vertical centring of single-line text).
- The component note states the control height per level and names the role; the test measures the line box centre against the control centre (AC-C03-3).
- A text field is the reference case and has a pixel check on the ink box ([[Typography]] AC-TYP-5).

## Truncation across components

- Single-line text ends with `…` (U+2026) when it does not fit. Every component note that holds text states its overflow behaviour: ellipsis, wrap with a line limit, or scroll ([[10 Layout Overflow and Scrolling]] overflow rule).
- Paths and file names use middle truncation that keeps the last segment visible.
- A truncated label shows its full text in a tooltip on the control that carries the text, not on the row or group ([[ADR-0004 Tooltip rule]]); the tooltip appears only when truncation happens.
- A label never wraps unless its note says it wraps. Button labels, tab labels, menu item labels and chip labels are single-line.
- A flex child that holds text has minimum width 0 so that the ellipsis can work.

## Tracking, families and weight

- Tracking is part of the role. A project whose text node cannot apply tracking renders 0 and records it in the Status table ([[Typography]] AC-TYP-2).
- Roboto is the default family with the fallback chain of [[Typography]] rule 7. Mixed families in one control are not allowed.
- The prominent label weight of [[Typography]] marks a selected or emphasised label; no other control changes weight on state, so state changes never move text (width changes by weight would reflow a row).
- Emphasised Expressive type styles are not baseline ([[Typography]] rule 9).

## Where each rule lives

| Topic | Note |
|---|---|
| Role table, tracking, shell mapping, minimum size | [[Typography]] |
| Ellipsis, wrap, minimum widths, centring geometry | [[10 Layout Overflow and Scrolling]] |
| Text colour roles and contrast | [[Colour Roles]], [[14 Accessibility Basics]] |
| Truncated text tooltip | [[Tooltip]], [[ADR-0004 Tooltip rule]] |
| Text field input rules | [[Text Field]] |

## Acceptance criteria

The 9 criteria AC-TYP-1 to AC-TYP-9 are defined in [[Typography]]. The criteria below test the rules that span components.

- [ ] AC-C03-1 (token test): every component note of `30 Component Specifications` that shows text names the type role of each text part, and every named role is one of the 15 roles of [[Typography]]. Pass: a script over the notes finds zero text parts without a role and zero names outside the 15.
- [ ] AC-C03-2 (token test): the role named for each element class in the table above equals the role named in the component note of that class (button and chip `label_large`, plain tooltip `body_small`). Pass: zero mismatches.
- [ ] AC-C03-3 (geometry check): for each component that holds single-line text, at each of the three density levels, the line box centre is within 1 dp of the control content box centre. Pass: all components and levels pass.
- [ ] AC-C03-4 (geometry check): at each density level, the rendered text size of one role (`body_medium`) is identical in a button row, a list row and a tree row. Pass: the three sizes are equal.
- [ ] AC-C03-5 (geometry check): for every component that holds text, a test sets the text to 3 times the container width. Pass: the text has one line (unless the note allows wrap), ends with `…`, and its right edge is at or inside the container's right edge.
- [ ] AC-C03-6 (scripted input): a truncated label in each of Button, List Item, Tree Node and Menu shows a tooltip with the full text on that control after hover for the hover delay of [[Tooltip]], and a label that fits shows none. Pass: 4 of 4 truncated cases show it, 4 of 4 fitting cases do not.
- [ ] AC-C03-7 (geometry check): selecting a row or tab whose label takes the prominent weight moves no sibling: the x positions of all siblings are equal before and after selection. Pass: zero siblings move by 1 dp or more.
- [ ] AC-C03-8 (token test): a static scan of all stylesheets of a project finds no font size literal below 11 dp. Pass: zero hits.

## Status in code

The per-role and per-criterion facts are in the Status table of [[Typography]]; this table gives the chapter view.

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/tokens.py` (`TYPE_SCALE`); `tess-ui:src/tess_ui/views/*_Stylesheet.tdl`; `tess-ui:src/tess_ui/composed.py` | Partly meets. Roles and sizes exist (AC-TYP-1). Fails AC-C03-3 in part: a single-line config text field is centred by padding, not by the engine. Tooltips use literal sizes (fails AC-TYP-3). AC-C03-8 not run. The role-per-component name is held in each component stylesheet, not checked here (AC-C03-1 not run). |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` (lines 30 to 34) | Partly meets. 5 roles map to nearest MD3 roles; text size per density is not defined; path labels truncate only where the module sets it (F5 recorded in [[Owner Feedback 2026-11-20]]). AC-C03-1 not applicable in full form (no 15 roles). |
| tre | `tre:docs/reference/properties.md` (Text), `tre:crates/engine-py/src/window_events.rs` | Not applicable as roles. The engine has text size, weight and line height on the text node, `letter_spacing` on the text node only; no vertical alignment on `text_input`, so AC-C03-3 depends on the caller computing padding. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| List, tree and menu text uses `body_medium` at compact and dense | the 20 dp line box must fit 32 and 28 dp rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Labels never wrap; single-line truncation with a tooltip on the control | desktop controls with fixed row heights; owner feedback F5 | [[ADR-0004 Tooltip rule]] |
| Vertical centring by construction at all densities | owner feedback F7 | [[ADR-0002 Desktop density levels and target sizes]] |
| Shell type names map to the nearest role | shell keeps its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- Type scale and component typography tokens: https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192 files `_md-comp-filled-button.scss`, `_md-comp-assist-chip.scss`, `_md-comp-dialog.scss`, `_md-comp-snackbar.scss`, `_md-comp-rich-tooltip.scss`, `_md-comp-plain-tooltip.scss` (verified 2026-11-21).
- MD3 typography overview: https://m3.material.io/styles/typography/overview (script-rendered, not readable by tools; values come from the token repository).
- Foundation and layout notes: [[Typography]], [[10 Layout Overflow and Scrolling]]; evidence [[Owner Feedback 2026-11-20]].
