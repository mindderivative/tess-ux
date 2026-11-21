---
title: Selection
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, selection, keyboard, list, tree]
related: ["[[40 Patterns]]", "[[Keyboard Navigation]]", "[[Drag and Drop Pattern]]", "[[List]]", "[[List Item]]", "[[Tree]]", "[[Tree Node]]", "[[Checkbox]]", "[[Menu]]", "[[Text Selection]]", "[[Colour Roles]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[11 Interaction]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[List]]", "[[Tree]]", "[[Focus Ring]]", "[[State Layers]]"]
---

# Selection

> [!info] Summary
> How a set of items (list rows, tree nodes, table rows, grid cells) is chosen: single and multiple selection, range, select all, the anchor, the Shift and Ctrl rules for pointer and keyboard, how a selected item looks, and what a screen reader hears. The MD3 counterpart is the selected state of [list items](https://m3.material.io/components/lists/overview); the multi-select model follows the [WAI-ARIA APG listbox](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/) and [tree view](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/) patterns. Text selection is a separate behaviour: [[Text Selection]].

## Problem

Single selection exists in tess-ui `Tree`, the shell `List` and tess-ui `Chip`, `Tabs` and `RadioGroup`; multi-select is absent from `Tree`, `NodeGraph` and `List` ([[Gaps and Contradictions]], "Multi-select: absent from Tree, NodeGraph, List"); the engine has `selected` as an accessibility flag only and `virtual_list` has no key handling. Without a shared model each project would invent its own modifier keys.

## Purpose

One selection model for every collection, so Shift and Ctrl behave the same in a list, a tree, a table and a grid, and a keyboard user can do everything a pointer user can.

## When to use and not

- Use when: the user picks items to act on (delete, move, open, copy) or one item to show.
- Do not use when: the choice is a single value of a form (use a [[Switch]], [[Checkbox]], Radio Button or [[Menu]]); the user edits text ([[Text Selection]]); items only navigate (a navigation rail destination is `current`, not selected).

## Rules

1. Focus and selection are different things. Focus is where the keyboard is (the ring, [[Focus Ring]]); selection is the set of chosen items. Moving focus does not change selection, except in the single-select case of rule 3.
2. Models: single (at most one selected), multiple (any set). The container declares which (`aria-multiselectable`); the item states `selected` or, in a check-style multi list, `checked`, never both ([[14 Accessibility Basics]]).
3. Single select: a click or Enter or Space selects the item and deselects the previous one. Selection does not follow focus by default ([[List]], [[Tree]]); a list that previews on arrow keys (the shell List, a file picker) may let selection follow focus when the preview is cheap, and states it.
4. Anchor: the anchor is the item where a range starts. It is set by a plain click, a Ctrl+click and Space (toggle on). Shift+click and Shift+Arrow never move the anchor; they select the range anchor to target.
5. Pointer rules:

| Input | Result |
|---|---|
| Click | select only this item; it becomes the anchor |
| Ctrl+click | toggle this item; it becomes the anchor |
| Shift+click | select the range anchor to this item, replacing the selection |
| Ctrl+Shift+click | add the range anchor to this item to the selection |
| Click in empty space of the container | clear the selection (multi); the keyboard way is Ctrl+Space on each item or a "Clear selection" control |
| Press and drag over an unselected item | rubber-band selection only where the container declares it (grids, canvases) |
| Press on an already selected item in a multi selection, then release without moving | select only this item (on release); a press that moves starts [[Drag and Drop Pattern|drag]] with the whole selection |

6. Keyboard rules, vertical list or tree (APG, adapted):

| Keys | Result |
|---|---|
| Up, Down | move focus; selection unchanged (single: see rule 3) |
| Ctrl+Up, Ctrl+Down | move focus only, in every case |
| Space | toggle the focused item (multi); choose it (single) |
| Ctrl+Space | toggle the focused item without changing others |
| Enter | activate the item (open); does not change a multi selection |
| Shift+Up, Shift+Down | move focus and select the range anchor to the focused item, replacing the selection |
| Ctrl+Shift+Up, Ctrl+Shift+Down | move focus and add the range anchor to the focused item |
| Shift+Space | select the range from the anchor to the focused item |
| Shift+Home, Shift+End | select from the anchor to the first, last item (APG Ctrl+Shift+Home, End also works) |
| Home, End | move focus to first, last; selection unchanged |
| Ctrl+A | select all items that exist in the container (multi); in a tree, all visible nodes |

7. Escape never clears a selection ([[11 Interaction]], Escape rule order). Select all and clear are also operable by a control when they matter: a toolbar button or menu item "Select all" and "Clear selection" (APG note 4: separate controls improve accessibility). Ctrl+A in a text field selects the field's text, not the list's.
8. In a tree: range and Ctrl+A act on visible nodes only; selecting a closed branch does not select its hidden children unless the tree says "select with children" and then states so in each node's name ("3 items").
9. In a table or grid: row selection by the row header or the first cell; cell selection only in a grid that declares it; Shift+Arrow extends a rectangular range from the anchor cell; Ctrl+Space selects the column and Shift+Space the row (spreadsheet convention, #needs-verification); header cell press sorts, not selects.
10. Virtualised containers: selection is stored by item id, not by built row; Shift+End on 100000 rows selects the range without building every row; the count is exact.
11. A disabled item is skipped by every key and cannot be selected by a range (the range passes it without selecting it).
12. Look: a selected item shows the role `secondary_container` fill with `on_secondary_container` content (the tess-ui Tree row), plus a non-colour cue: a 3 dp start indicator bar in `primary` at default and compact and 2 dp at dense (design choice, #needs-verification-as-design-choice; the shell uses a 2 px `primary` border, also more than colour). The focus ring is separate and drawn over it. An unfocused window or container shows the selection with `surface_container_highest` and `on_surface`. Hover on a selected item adds the 8 percent state layer ([[State Layers]], [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]).
13. Announcements (polite): a single selection change announces the item name and "selected" (the reader does it from the `selected` flag; no extra announce). A multi change announces the count once, debounced 300 ms: "4 selected"; select all announces "all 120 selected"; clear announces "selection cleared". The count is also in the container's description for a status bar to display.

## Decision table

| Collection | Model | Selection follows focus | Range | Select all | Notes |
|---|---|---|---|---|---|
| Navigation tree (config Structure tree) | single | no | no | no | Enter or press chooses; one action per selected node |
| File list, file dialog | multi | no | yes | yes | Open uses Enter |
| Menu, command list | none | not applicable | no | no | items activate, they are not selected |
| Launcher results | single | yes (preview) | no | no | active descendant or announce fallback ([[14 Accessibility Basics]]) |
| Settings choices (radio) | single, one required | focus moves with selection (APG radio) | no | no | [[Radio Button]] |
| Table of records | multi, row | no | yes | yes | sort on header press |
| Chips, filter chips | multi, toggle | no | no | no | each chip is a toggle |
| Canvas, node graph | multi | not applicable | rubber band | yes | selection by pointer area is a pointer alternative only; keys select by Tab and Space |
| Text | not this pattern | not applicable | not applicable | not applicable | [[Text Selection]] |

## Examples (short snippets only)

```text
Items: A B C D E   anchor B (plain click)
Shift+click D      -> B C D selected, anchor B
Ctrl+click E       -> B C D E selected, anchor E
Shift+click C      -> C D E selected (range E..C replaces)
Ctrl+A             -> A B C D E selected; announce "5 selected"
```

```tdl
Tree { Nodes: <| nodes |>, Selected: <| current |> }   # single select, tess-ui
```

## States

| State | Visual change | Token values |
|---|---|---|
| Unselected | no fill | none |
| Hover | 8 percent state layer | [[State Layers]] |
| Selected | `secondary_container` fill, `on_secondary_container` content, 3 dp start indicator in `primary` | [[Colour Roles]] |
| Selected and hover | selected look plus 8 percent layer | [[State Layers]] |
| Focused (keyboard) | ring 3 dp, 2 dp offset, `secondary`; for rows inside a clipped scroll container, an inset ring so it is never cut | [[Focus Ring]] |
| Selected, container unfocused | `surface_container_highest`, `on_surface` | [[Colour Roles]] |
| Disabled | 38 percent content, not selectable | [[State Layers]] |
| Drag source | selected look, 38 percent opacity while dragging | [[Drag and Drop Pattern]] |

## Sizing and density

Rows follow the list and tree heights 40, 32, 24 dp and padding 12, 8, 4 dp ([[Spacing and Density]]); the selection indicator bar is inside the row padding and adds no width. The pointer target of a row is its full width and height (at least 24 dp). A check-style multi list adds a [[Checkbox]] at the row start (18 dp box in a 24 dp target).

## Accessibility

- Container role `list`/`listbox`, `tree`, `grid`, `table` with `aria-multiselectable` true for a multi container; item role `option`, `treeitem`, `row` with `aria-selected` (APG: use `aria-selected` for single, `aria-checked` for check-style multi, one convention per app).
- Virtualised: `aria-setsize` and `aria-posinset` on built rows.
- Selection state is carried by the flag, the fill and the indicator bar, not colour alone (SC 1.4.1).
- Keyboard alone does everything pointer does: range, toggle, select all, clear (SC 2.1.1).
- Pointer targets at least 24 dp ([[ADR-0002 Desktop density levels and target sizes]]).

## Acceptance criteria

- [ ] AC-SLT-1 (scripted input): on items A to E, click B, Shift+click D, Ctrl+click E, Shift+click C yields selected sets {B}, {B,C,D}, {B,C,D,E}, {C,D,E} in that order with anchors B, B, E, E. Pass: sets and anchors equal.
- [ ] AC-SLT-2 (scripted input): focus B (selected), Shift+Down twice selects {B,C,D}, Shift+Up once selects {B,C}; the anchor stays B. Pass: sets equal, anchor B.
- [ ] AC-SLT-3 (scripted input): Ctrl+Down twice moves focus two rows with selection unchanged; Ctrl+Space toggles the focused row only; Space in a multi list toggles and in a single list chooses. Pass: sets equal at each step.
- [ ] AC-SLT-4 (scripted input): Ctrl+A in a multi list selects all enabled items; in a text field inside the same window it selects only the field text; Escape leaves the selection unchanged ([[11 Interaction]]: Escape never clears a selection). Pass: sets equal.
- [ ] AC-SLT-5 (scripted input): a range across a disabled row selects the enabled rows only; Up, Down, Home, End skip the disabled row. Pass: set excludes the disabled row; focus never lands on it.
- [ ] AC-SLT-6 (scripted input): in a virtualised list of 100000 rows, Shift+End from row 0 selects 100000 items with at most (viewport rows + 20) built rows, and the reported count is 100000. Pass: count and built rows equal.
- [ ] AC-SLT-7 (scripted input): in a tree, Ctrl+A selects visible nodes only; collapsing a branch whose children are selected keeps them selected and reports the count. Pass: count equals visible nodes; hidden selection state unchanged.
- [ ] AC-SLT-8 (AT tree assertion): a multi container has `multiselectable` true and each item has `selected` true or false; a single container has `multiselectable` false and at most one selected item. Pass: flags equal.
- [ ] AC-SLT-9 (AT tree assertion): after Shift+click selecting 4 items, exactly one polite announcement "4 selected" occurs after 300 ms; ten selection changes within 300 ms give one announcement. Pass: announcement count and text equal.
- [ ] AC-SLT-10 (pixel check): a selected row differs from an unselected row by fill `secondary_container` and the indicator bar (greyscale render differs), and the focus ring is visible on top of a selected focused row. Pass: pixel regions present.
- [ ] AC-SLT-11 (token test): selected roles `secondary_container` and `on_secondary_container`; unfocused-container selection `surface_container_highest`; state layer 8 percent on hover; no colour literals. Pass: values and roles equal.
- [ ] AC-SLT-12 (contrast script): `on_secondary_container` on `secondary_container` at least 4.5 to 1; the indicator bar against the row at least 3 to 1, in light and dark. Pass: ratios at or above limits.
- [ ] AC-SLT-13 (scripted input): a press on a selected item of a 3 item selection, released without movement, selects only that item; a press that moves 4 dp or more starts a drag carrying all 3. Pass: sets equal.
- [ ] AC-SLT-14 (geometry check): the pointer target of a row is its full width and at least 24 dp high at the three densities; the indicator bar adds no width (row content x unchanged by selection, 0.5 dp). Pass: bounds equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Tree_View.tdl`, `TreeNode_View.tdl`, `tess-ui:docs/components/trees.md`, `tess-ui:docs/guide/lists.md`, `Chip_View.tdl` | partly meets: single select on `Tree` (`Selected`, row `secondary_container`, selection does not follow focus per the Tree note, AC-SLT-8 for single by reading, AC-SLT-11 partly); no multi-select in Tree, NodeGraph or List (AC-SLT-1 to AC-SLT-7, AC-SLT-9, AC-SLT-13 fail, "Not built: selecting several"); no unfocused-container look (AC-SLT-10 partly); no start indicator bar |
| tess-shell | `tess-shell:src/tess_shell/shipped/List/List_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | partly meets: single select, selection follows focus on arrow keys (each move is a choice), Home, End, Page keys, type-ahead, disabled skipped (AC-SLT-5 for single); `:selected` gives raised fill plus 2 px `primary` border (more than colour, AC-SLT-10 partly); no multi, no Shift or Ctrl rules (AC-SLT-1 to AC-SLT-4, AC-SLT-6, AC-SLT-9 fail) |
| tre | `tre:docs/reference/node.md` (`selected`), `tre:docs/guide/nodes-and-layout.md` (virtual list) | not applicable: `selected` is a flag; `virtual_list` has no keys and no selection; the model is framework code |

Request candidates: multi-select in tess-ui `Tree` and `List` (Shift and Ctrl rules as above) and the shell `List`; virtual list keys are [[UXREQ-002 Virtual list keys and scroll to index]]; routed through the Orchestrator.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Shift and Ctrl range and toggle rules, anchor, select all | MD3 gives no multi-select model for lists; desktop file managers and APG define one | none; design choice, [[ADR-0006 MD3 baseline with named Expressive adoptions]] for the MD3 baseline |
| Shift+Arrow extends a range from the anchor (APG recommended model toggles the next item) | desktop convention; Shift+Space and Ctrl+Space give the toggle forms | none; design choice |
| Start indicator bar in addition to the `secondary_container` fill | selection must not rest on colour alone | none; [[14 Accessibility Basics]] |
| Unfocused container selection colour | desktop windows keep a selection while another pane has focus | none |

## Sources

- [WAI-ARIA APG Listbox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/): focus on receive, Up, Down, Home, End, type-ahead, recommended multi selection model (Space, Shift+Up, Shift+Down, Shift+Space, Ctrl+Shift+Home, Ctrl+Shift+End, Ctrl+A), alternative model (Ctrl+Arrow, Ctrl+Space), `aria-multiselectable`, `aria-selected` versus `aria-checked`, `aria-setsize`, separate Select all controls. Verified 2026-11-21.
- [WAI-ARIA APG Tree View pattern](https://www.w3.org/WAI/ARIA/apg/patterns/treeview/): the same multi selection models for trees. Verified 2026-11-21.
- [WCAG 2.2 SC 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color), [SC 2.1.1](https://www.w3.org/TR/WCAG22/#keyboard), [SC 4.1.2](https://www.w3.org/TR/WCAG22/#name-role-value).
- MD3 list selected state: `secondary_container` for a selected item as used in tess-ui `Tree`; m3.material.io list pages are unreadable by tools #needs-verification.
- The Ctrl+Space and Shift+Space column and row rule for grids, the indicator bar width and the 300 ms debounce are design choices #needs-verification-as-design-choice.
- Code: `tess-ui:docs/components/trees.md`; `tess-shell:docs/guide/keyboard.md` (List keys); [[List]], [[Tree]]; [[Gaps and Contradictions]].
