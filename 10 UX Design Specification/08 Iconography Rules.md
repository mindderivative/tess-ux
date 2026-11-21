---
title: 08 Iconography Rules
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, icons, iconography]
related: ["[[Iconography]]", "[[Spacing and Density]]", "[[07 Spacing and Density Rules]]", "[[03 Typography and Text Rules]]", "[[09 State Feedback Rules]]", "[[02 Colour and Theming]]", "[[14 Accessibility Basics]]", "[[01 Principles and Scope]]", "[[Icon Button]]", "[[Button]]", "[[Tree Node]]", "[[List Item]]", "[[Menu]]", "[[Text Field]]", "[[Tooltip]]", "[[Colour Roles]]", "[[ADR-0007 Icon set and Material Symbols deviation]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[Deviations from MD3]]"]
depends_on: ["[[Iconography]]", "[[ADR-0007 Icon set and Material Symbols deviation]]"]
---

# 08 Iconography Rules

> [!info] Summary
> Chapter-level principles for using icons: when an icon carries meaning, how it pairs with a label, its size per density level, colour by role and accessible names. The sizes, the icon set and the fallback glyph live in [[Iconography]]; this chapter links and copies no value. Material Design 3 baseline: [icons](https://m3.material.io/styles/icons/overview).

## Purpose

An icon saves width and speeds scanning if the user knows it. It costs clarity if it stands alone, differs between places, or is the only sign of a state. The chapter sets when to use one, with or without a label, and how to keep it consistent and accessible.

## Scope

- In scope: icon-with-label and icon-only rules, meaning and consistency, size and alignment rules across components, colour and state, accessible names, decorative icons, fallback.
- Out of scope: the set, the view box, size table and fallback glyph ([[Iconography]]), the Material Symbols deviation ([[ADR-0007 Icon set and Material Symbols deviation]]).

## Principles

1. An icon has one meaning in a project. The same icon name means the same action or object everywhere; two actions never share an icon, two icons never name one action.
2. A label first. An icon next to a text label is decoration that supports scanning; an icon alone is allowed only for a small set of familiar actions (close, search, settings, menu, add, delete, back, expand, collapse) and for toolbars where the tooltip names it ([[Icon Button]]).
3. Every icon-only control has an accessible name and a tooltip with the same text on the control ([[ADR-0004 Tooltip rule]], [[14 Accessibility Basics]]).
4. A decorative icon is hidden from assistive technology. An icon that repeats the text beside it adds no node to the accessibility tree.
5. Size follows density. Icon size is a function of the density level and the slot, not of the view ([[Iconography]], [[07 Spacing and Density Rules]]). The painted icon never exceeds its hit area.
6. One size per row. Icons in one row, list, menu or toolbar have one size; icon and label centre on the same horizontal axis.
7. Colour is a role. An icon takes the content colour of its parent through a role, never a literal ([[Colour Roles]]), and takes the state of its control ([[09 State Feedback Rules]]).
8. An icon is never the only carrier of state. Error, warning, selected and disabled have a second cue: text, shape or position ([[14 Accessibility Basics]]).
9. A missing icon is visible. An unresolved name shows the fallback glyph and one warning; a blank slot is a defect ([[Iconography]]).
10. Baseline set only. No project mixes icon sets in one view; Material Design Icons are the set until an ADR changes it ([[ADR-0007 Icon set and Material Symbols deviation]]).

## Icon with label and icon only

| Case | Rule |
|---|---|
| Button with text and icon | the icon leads (left in left-to-right text), 8 dp gap #needs-verification, label role per [[03 Typography and Text Rules]]; the icon size is the button-label icon size of [[Iconography]] |
| Button with icon only | uses [[Icon Button]], not a [[Button]] without a label |
| Menu item | leading icon optional per menu, but all items of one menu either have a leading icon slot or none; a trailing icon marks a submenu or a shortcut state |
| List item and tree row | leading icon optional per list or tree; items without an icon keep the slot width so that labels align; the chevron of a tree row is a separate element ([[Tree Node]]) |
| Text field | leading icon names the field's kind, trailing icon is an action (clear, show); both are inside the field, 24 dp at default ([[Text Field]]) |
| Toolbar | icon buttons only, each with tooltip; a text button joins only for a primary action |
| Status bar and badge row | 16 dp inline icons, always with the text or value that the icon qualifies |
| Dialog and empty state | one standalone 24 dp icon above the title; text always follows |

A control never uses an icon whose meaning depends on colour alone (a red and a green circle with the same shape).

## Size, alignment and hit area

- Size values per use and density level are in [[Iconography]]; a component note names the use row it follows.
- The icon is centred in its slot; the slot is centred in the control; the hit area of an icon-only control is the whole control and at least 24 dp ([[07 Spacing and Density Rules]]).
- At density levels with 20 dp or 16 dp icons the 24-unit glyph scales uniformly; strokes thin by the scale ratio and no optical size exists ([[Iconography]], Deviation from Material Symbols).
- In a touch context the painted icon keeps its size and the hit area grows to 48 dp.

## Colour and state

- Default role: `on_surface` for primary actions, `on_surface_variant` for secondary or decorative icons, `on_primary` on a filled primary button, `on_secondary_container` on a tonal control ([[Iconography]]).
- Disabled: content colour at 38 percent ([[State Layers]]); the state layer sits behind the icon.
- Error and warning: the icon takes the `error` role or the control's error role and is paired with text.
- Selected: a selected control changes its icon colour role or its icon name to the filled variant; no fill animation exists in the set.
- A theme switch changes every icon colour; no icon keeps a colour of the old scheme.
- Multicolour images (application icons, thumbnails) are not tinted ([[Iconography]]).

## Where each rule lives

| Topic | Note |
|---|---|
| Sizes per use and density, set, view box, tint rules, fallback | [[Iconography]] |
| Icon-only action | [[Icon Button]] |
| Accessible names | [[14 Accessibility Basics]] |
| Tooltip on an icon-only control | [[Tooltip]], [[ADR-0004 Tooltip rule]] |
| Disabled and state layers | [[State Layers]], [[09 State Feedback Rules]] |

## Acceptance criteria

The criteria AC-ICO-1 to AC-ICO-8 are defined in [[Iconography]].

- [ ] AC-C08-1 (token test): every component note of `30 Component Specifications` that shows an icon names the use row of [[Iconography]] (icon button, list and tree leading, button label, text field, inline) and the icon size per density level equals that row. Pass: zero icons without a row, zero mismatches.
- [ ] AC-C08-2 (AT tree assertion): in every documented view, every icon-only interactive node has a non-empty accessible name equal to its tooltip text, and every decorative icon is absent from the tree. Pass: zero violations.
- [ ] AC-C08-3 (scripted input): hover or focus on each icon-only control in a documented view shows a tooltip on that control with the accessible name within the delay of [[Tooltip]]. Pass: all controls.
- [ ] AC-C08-4 (geometry check): in a row, list, menu or toolbar, all icons have the same painted size and their centres share one vertical coordinate within 1 px with the label centre (AC-ICO-6). Pass: all rows.
- [ ] AC-C08-5 (geometry check): in a menu or list where some items have an icon, items without one have their label x equal to the labels of those with one. Pass: zero misaligned labels.
- [ ] AC-C08-6 (token test): a static scan of all stylesheets of a project finds no literal colour on an icon, and one icon name does not map to two different meanings in the project's icon-meaning list. Pass: zero hits.
- [ ] AC-C08-7 (pixel check): a state shown by an icon (error, warning, selected) differs in a greyscale render from the neutral state by a non-colour feature: shape, text or position ([[14 Accessibility Basics]] AC-A11Y-16). Pass: differs for every state.
- [ ] AC-C08-8 (geometry check): painted icon bounds are inside the control's hit area at each density level and in a touch context. Pass: zero icons exceeding.

## Status in code

Detail per criterion is in [[Iconography]].

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/icons.py`; `tess-ui:src/tess_ui/views/IconButton_Stylesheet.tdl`; `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl` | Partly meets. Two icon sets with different view boxes; icon button 24 with 20 for size xs and no density levels (AC-C08-1 fails at compact and dense); button size s icon 18 meets; icon colour from roles. |
| tess-shell | `tess-shell:src/tess_shell/shipped/Icons/mdi.json`; `tess-shell:src/tess_shell/model/icons.py` | Partly meets. Fallback with one warning meets; default Icon size 16 and MenuItem icon 16 are literals, which fail AC-C08-1 at the default level (24 for menu and list). |
| tre | `tre:docs/reference/paint.md`; `tess-icons` | Not applicable. The engine draws paths and has no icon size default; accessible names and tooltips are the caller's. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Material Design Icons, no weight, fill, grade or optical size | static path set used by all projects | [[ADR-0007 Icon set and Material Symbols deviation]] |
| 20 and 16 dp icons at compact and dense | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| Every icon-only control has a tooltip | desktop keyboard-first and pointer use, no label to read | [[ADR-0004 Tooltip rule]] |

## Sources

- Icon sizes: https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192 (`_md-comp-icon-button.scss`, `_md-comp-filled-button.scss`, `_md-comp-filled-text-field.scss`), verified in [[Iconography]] on 2026-11-21.
- WCAG 2.2 SC 1.1.1 Non-text Content and SC 1.4.11: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html #needs-verification (page not opened for this chapter); 1.4.11 verified in [[Iconography]].
- MD3 icons overview: https://m3.material.io/styles/icons/overview (script-rendered, not readable by tools).
- The 8 dp gap between a button icon and its label is not read from a token file #needs-verification.
