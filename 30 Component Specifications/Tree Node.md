---
title: Tree Node
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, tree, density, owner-feedback]
related: ["[[Tree]]", "[[List Item]]", "[[Scrollbar and Scroll Container]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[State Layers]]", "[[Focus Ring]]", "[[Typography]]", "[[Motion]]", "[[Iconography]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]"]
---

# Tree Node

> [!info] Summary
> One row of a [[Tree]]: indentation, an expand chevron box, an optional icon and a one-line label. Material Design 3 has no tree; the row is a one-line [[List Item]] indented by depth, with the WAI-ARIA `treeitem` semantics. Source of truth in code: the last section.

## Purpose

Show one item of a hierarchy at its depth, say whether it can open and whether it is open, and let the pointer and keyboard open, close and choose it. The geometry answers owner feedback F3 (indent gaps too large), F4 (gap between the root chevron and the container edge too large) and F5 (long labels run past the container) in [[Owner Feedback 2026-11-20]].

## When to use and not

- Use when: a row belongs to a [[Tree]] (file lists, structure outlines, settings categories).
- Do not use when: items are flat ([[List Item]]) or the section only reveals content ([[Accordion]]).

## Anatomy

1. Row container: full width of the tree, one density-dependent height, the pointer and selection target.
2. Indent: left padding = row padding + indent x depth.
3. Chevron box: a square holding the chevron glyph; a leaf keeps an empty box of the same size (spacer).
4. Icon (optional): 24 dp at `default`, 20 dp at `compact` and `dense` ([[Iconography]]).
5. Label: one line, left-aligned, flexible width with a minimum width of 0, ellipsis when cut.

Order left to right: indent, chevron box, gap, icon, gap, label, row end padding.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Branch | has children | chevron visible, `aria-expanded` set |
| Leaf | no children | spacer in the chevron box, no `aria-expanded` |
| With icon | folders, files | icon between chevron box and label |
| Selected | chosen item | `secondary_container` background |
| Disabled | unavailable | content at 0.38, container no state layer |

## States

State layers use role `on_surface` at the percentages of [[ADR-0009 State layer percentages]] ([[State Layers]]).

| State | Visual change | Token values |
|---|---|---|
| Rest | transparent container; chevron and icon `on_surface_variant`, label `on_surface` | none |
| Hover | state layer over the row | `on_surface` at 8 percent |
| Focus (keyboard) | state layer plus the focus ring, drawn inset inside the row so that a clipping scroll container does not cut it | 10 percent; ring 3 dp, colour `secondary`; inset ring is #needs-verification (design choice, see [[Focus Ring]]) |
| Pressed | state layer | 10 percent |
| Selected | container `secondary_container`; icon and label `on_secondary_container`; chevron `on_secondary_container` | state layers stack on it |
| Selected and hover | selected container plus 8 percent layer in `on_secondary_container` | |
| Dragged | planned (drag to reorder) | 16 percent |
| Disabled | content `on_surface` at 0.38; no hover, no press, no focus stop | container 0.12 not drawn on a transparent row |
| Loading children | planned: chevron replaced by a 16 dp progress ring | not specified here |

## Tokens used

[[Colour Roles]] (`on_surface`, `on_surface_variant`, `secondary_container`, `on_secondary_container`, `secondary`), [[Typography]], [[Motion]], [[Spacing and Density]].

## Sizing and density

The numbers are the binding density table of [[ADR-0002 Desktop density levels and target sizes]] and [[Spacing and Density]]; they are not redefined here. Tree-specific derived values (icon size, label type) are marked.

| Token | default | compact | dense |
|---|---|---|---|
| Row height, single line | 40 dp | 32 dp | 24 dp |
| Row horizontal padding (`P`) | 12 dp | 8 dp | 4 dp |
| Indent per level (`I`) | 20 dp | 16 dp | 12 dp |
| Chevron box (`C`) | 24 dp | 20 dp | 16 dp |
| Gap between parts (`G`) | 8 dp | 8 dp | 4 dp |
| Icon size | 24 dp | 20 dp | 20 dp |
| Label type | `body_large` 16/24 | `body_medium` 14/20 | `body_medium` 14/20 |

Icon sizes follow the icon button rule of the density table; the label types are a Tesserae choice (MD3 list items use `body_large` only). #needs-verification (design choice).

Left padding of a row at depth `d` (`d` starts at 0) = `P` + `I` x `d`. The gap between the chevron box of a depth-0 row and the container edge is `P` and nothing else (no extra margin, F4). Right padding = `P`.

Exact horizontal positions in dp from the left edge of the tree container (the row starts at x = 0). The chevron box spans `[x, x + C]`; the label starts at x + C + G without an icon, and at x + C + G + icon + G with one.

| Density | Depth | Chevron box x | Icon x (if any) | Label x, no icon | Label x, with icon |
|---|---|---|---|---|---|
| default | 0 | 12 to 36 | 44 to 68 | 44 | 76 |
| default | 1 | 32 to 56 | 64 to 88 | 64 | 96 |
| default | 2 | 52 to 76 | 84 to 108 | 84 | 116 |
| compact | 0 | 8 to 28 | 36 to 56 | 36 | 64 |
| compact | 1 | 24 to 44 | 52 to 72 | 52 | 80 |
| compact | 2 | 40 to 60 | 68 to 88 | 68 | 96 |
| dense | 0 | 4 to 20 | 24 to 44 | 24 | 48 |
| dense | 1 | 16 to 32 | 36 to 56 | 36 | 60 |
| dense | 2 | 28 to 44 | 48 to 68 | 48 | 72 |

The label right edge never exceeds the row width minus `P`. A pointer target is the whole row (a click on the chevron box acts as a click on the row); the row height is at least 24 dp at every density, which meets WCAG 2.2 SC 2.5.8 ([[ADR-0002 Desktop density levels and target sizes]]); the 16 dp dense chevron box is not a separate target.

## Dimensions and defaults

These are the binding density values of [[Spacing and Density]] and [[ADR-0002 Desktop density levels and target sizes]]; the icon size and the label type are Tesserae choices #needs-verification-as-design-choice (proposed ADR: tree row label type by density). The icon size follows [[Iconography]] (24, 20, 20). The left padding of a row at depth `d` is the row padding plus the indent times `d`; the indent row gives the per-level step.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| row | height | `density.row_height` | 40 | 32 | 24 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| row | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] (WCAG 2.2 SC 2.5.8) | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| chevron box | height | `density.chevron_box` | 24 | 20 | 16 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| chevron box | min width | `density.chevron_box` | 24 | 20 | 16 | [[Spacing and Density]] | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| row (depth 0) | padding | `density.row_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 4 0 4 | [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| indent (per level) | padding | `density.tree_indent` | 0 0 0 20 | 0 0 0 16 | 0 0 0 12 | [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| row | margin | - | N/A: the row has no margin; the root chevron sits at the row padding from the container edge and nothing else (F4) | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| row | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| row | border width | - | 0 | 0 | 0 | design choice, proposed ADR (tree row appearance); [[Tree Node#States]] (the row has a fill state and a focus ring, no border) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| row | border color | - | N/A: the row draws no border; selection is a fill and focus is the inset ring | N/A: same as default | N/A: same as default | [[Tree Node#States]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| row | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] (the row is a one-line [[List Item]] indented by depth, container shape none) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| label | font | `body_large`, `body_medium`, `body_medium` | 16/24/400/0.5 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]]; design choice, proposed ADR (tree row icon size and label type by density) | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| icon | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Tree Node#Sizing and density]]; design choice, proposed ADR (tree row icon size and label type by density) | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| chevron glyph | icon size | `density.chevron_box` | 24 | 20 | 16 | [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| row | elevation | `elevation.level_0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

## Layout and overflow

- The label has a minimum width of 0, takes the remaining row width, shows one line and ends with an ellipsis when cut (F5). It never wraps and never widens the row, so a tree with long labels has no horizontal overflow from labels.
- Chevron box and icon do not shrink; the label gives way first.
- The text is vertically centred in the row: the line box (label type line height) is centred within the row height, so at `dense` 20 dp of line height sits in 24 dp with 2 dp above and below.
- A leaf keeps its chevron spacer so that sibling leaf and branch labels at the same depth align.

## Behaviour

- Pointer: a press on the row selects it and, for a branch, toggles it open or closed. Hover shows the state layer. The pointer does not scroll the row.
- Keyboard: see [[Tree]] (Left, Right, Enter, Space act on the focused node).
- Touch: the row is the target; touch contexts use 48 dp rows ([[ADR-0002 Desktop density levels and target sizes]]).

## Tooltip and overlay behaviour

Per [[ADR-0004 Tooltip rule]] the tooltip belongs to the smallest element that carries the text: the label. When, and only when, the label is cut by an ellipsis, the label shows a plain tooltip with its full text after a 500 ms hover or immediately on keyboard focus of the row (focus is on the row, whose label tooltip then shows; the label is the trigger for hover). The row, the tree level and the tree carry no tooltip, so hovering the row outside the label shows none. A label that fits shows no tooltip. The tooltip text is never the only way to read the label: the accessible name holds it.

## Motion

- The chevron turns from 0 to 90 degrees in 200 ms (`short4`) with `easing-standard` cubic-bezier(0.2, 0, 0, 1) ([[Motion]]); reduced motion sets 0 ms.
- Background changes (state layer, selection) use 150 ms in tess-ui today; the specification value is `short3` 150 ms.
- Children appear without a height animation (rows are laid out at once, to keep layout cost low).

## Accessibility

- Role `treeitem`; name = label text; `aria-level` = depth + 1; `aria-expanded` true or false on branches only; `aria-selected` on selectable nodes; `aria-setsize` and `aria-posinset` when the tree is virtualised ([[Tree]], WAI-ARIA tree pattern).
- Contrast: `on_surface` on the surface and `on_secondary_container` on `secondary_container` each reach 4.5 to 1; chevron and icon reach 3 to 1 ([[14 Accessibility Basics]]).

## Dark and light

Roles only; the scheme follows the system ([[Theme Following the System]]).

## Defaults

Density `compact` in configuration tools, `default` elsewhere (set by the project, [[ADR-0002 Desktop density levels and target sizes]]); no icon; single select.

## Acceptance criteria

- [ ] AC-TRN-01: Token test. The tree row tokens equal the sizing table for the three densities (height, `P`, `I`, `C`, `G`, icon size).
- [ ] AC-TRN-02: Geometry check. Row height is 40, 32 and 24 dp at `default`, `compact`, `dense` with single-line labels; all rows of one tree have the same height.
- [ ] AC-TRN-03: Geometry check (F4). The left edge of the chevron box of a depth-0 row is 12, 8 and 4 dp from the tree container's left edge; no other element or margin lies between.
- [ ] AC-TRN-04: Geometry check (F3). The left edge of the chevron box at depth n + 1 minus the one at depth n is 20, 16 and 12 dp for n = 0 to 4.
- [ ] AC-TRN-05: Geometry check. The chevron box and label x positions at depths 0, 1 and 2 equal the position table within 0.5 dp, with and without an icon, at all three densities.
- [ ] AC-TRN-06: Geometry check. The chevron box is 24, 20 and 16 dp square and a leaf row has a spacer of identical size, so the labels of a leaf and a branch at the same depth start at the same x.
- [ ] AC-TRN-07: Geometry check (F5). A label of 300 characters in a 240 dp tree: the label right edge is at most the row width minus `P`, the row has no horizontal overflow (container scroll extent equals its viewport), and the last visible glyph is the ellipsis.
- [ ] AC-TRN-08: Scripted input (F8). Hovering the row outside the label for 2 s shows no tooltip; hovering the truncated label for 500 ms shows one tooltip with the full text; a label that fits shows none; the tooltip key is set on no row, tree level or tree node.
- [ ] AC-TRN-09: Geometry check. The vertical centre of the label line box is within 0.5 dp of the row vertical centre at all densities.
- [ ] AC-TRN-10: Pixel check. A hovered row is the rest colour with an 8 percent `on_surface` layer, a pressed one 10 percent, a keyboard-focused one 10 percent plus a 3 dp `secondary` ring inside the row bounds.
- [ ] AC-TRN-11: Contrast script. Label on `secondary_container` and on the surface, light and dark baseline schemes: at least 4.5 to 1; chevron and icon at least 3 to 1.
- [ ] AC-TRN-12: Scripted input. A disabled row shows content at opacity 0.38, ignores click, Enter and Space, and the arrow keys and typeahead skip it.
- [ ] AC-TRN-13: Pixel check. The chevron turns 0 to 90 degrees in 200 ms (sampled at 0, 100 and 200 ms) and in 0 ms under reduced motion.
- [ ] AC-TRN-14: AT tree assertion. The node has role `treeitem`, name equal to the label, `aria-level` depth + 1, `aria-expanded` only on branches, `aria-selected` only on selectable nodes.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TreeNode_View.tdl`, `TreeNode_Stylesheet.tdl` | partly meets. Library default (origin/main after PRs #328 to #330): row 56 px (Compact 40), left 16 plus 24 per level, right 16, gap 8, chevron 24 by 24, leaf spacer 24, label `body_large` with `Max_Lines: 1` and ellipsis. Against `default`: height 56 vs 40, padding 16 vs 12, indent 24 vs 20 (fails AC-TRN-02, 03, 04, 05); chevron and gap meet. Chevron turn 200 ms meets AC-TRN-13; hover, focus and press layers are not part of the tree stylesheet (AC-TRN-10 fails); no label tooltip (AC-TRN-08 fails) |
| tess-ui (config app) | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_Stylesheet.tdl` | partly meets. Override: `Compact: true` rows 40, left 4 plus 16 per level, right 4, gap 4, label `Flex: expand_horizontal` with `Min_Width: 0` and ellipsis; chevron box stays 24. Depth 0, 1, 2 chevron x: 4, 20, 36 (label x 32, 48, 64). Against `compact` (8, 16, 20, 8; row 32): indent 16 meets AC-TRN-04; row 40 vs 32, padding 4 vs 8, gap 4 vs 8, chevron 24 vs 20 fail AC-TRN-02, 03, 05, 06; against `dense` only depth 0 x (4) and gap 4 match. Ellipsis meets AC-TRN-07 as designed (not measured). Folder path label has a tooltip, tree labels have none |
| tess-shell | none | absent (no tree widget; the Config structure tree is planned in the shell vault) |
| tre | `tre:crates/engine-core/src/node.rs` (`role` treeitem only) | not applicable (the engine has roles and text ellipsis, no tree row) |

Evidence: F3, F4, F5, F8 in [[Owner Feedback 2026-11-20]]. The demo ran before PR #329 (dense config trees), which is why the config-app values above are smaller than the ones the owner saw.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A tree row exists although MD3 has no tree | hierarchical data in the config app and shell | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row heights 40, 32, 24 dp instead of the 56 dp one-line list item | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Label type `body_medium` at `compact` and `dense` | fits 32 and 24 dp rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Row padding 12, 8, 4 dp instead of 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- Material Web list item tokens (one-line height 56 dp, leading and trailing space 16 dp, top and bottom space 12 dp, leading icon 24 dp, label `body-large`): https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-list.scss and https://github.com/material-components/material-web/blob/main/list/internal/listitem/_list-item.scss (read 2026-11-21).
- Typography scale values: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss (body large 16/24, body medium 14/20).
- Motion durations and easing: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-motion.scss (short3 150 ms, short4 200 ms, standard cubic-bezier(0.2, 0, 0, 1)).
- WAI-ARIA Authoring Practices, Tree View pattern: https://www.w3.org/WAI/ARIA/apg/patterns/treeview/ (roles, `aria-expanded`, `aria-level`).
- WCAG 2.2 SC 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html.
- Code: `tess-ui:src/tess_ui/views/TreeNode_View.tdl`, `TreeNode_Stylesheet.tdl`, `TreeLevel_View.tdl`, `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_Stylesheet.tdl` (read from origin/main at commit c7117cb).
