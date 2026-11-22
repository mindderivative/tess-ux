---
title: Tree
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, tree, keyboard, owner-feedback]
related: ["[[Tree Node]]", "[[List]]", "[[Scrollbar and Scroll Container]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[Deviations from MD3]]"]
depends_on: ["[[Tree Node]]", "[[Scrollbar and Scroll Container]]", "[[ADR-0003 Scrollbar rule]]"]
---

# Tree

> [!info] Summary
> A vertical hierarchy of [[Tree Node]] rows that open and close, one Tab stop, one chosen row. Material Design 3 has no tree, so this is a Tesserae element built from the list item and navigation drawer patterns of MD3 and the WAI-ARIA tree view pattern (verified at https://www.w3.org/WAI/ARIA/apg/patterns/treeview/). Source of truth in code: the last section.

## Purpose

Navigate and choose in hierarchical data (files by type, configuration structure, settings categories) with the keyboard as the first input.

## When to use and not

- Use when: items have parents and children and the user moves between levels.
- Do not use when: items are flat or have one grouping level ([[List]] with section headers); content only reveals more content ([[Accordion]]); the data is a table.

## Anatomy

1. Tree container: role `tree`, vertical roving focus, lays rows in a column.
2. Tree rows: the visible rows are direct children of the tree, each with its level; the children of an open branch follow it in tree order, with no group wrapper ([[ADR-0028 Tree rows are flat in the accessibility tree]], accepted).
3. [[Tree Node]] rows.
4. Scroll container around the tree ([[Scrollbar and Scroll Container]]).
5. Empty-state slot, shown when there are no nodes.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Single select | the default | one `aria-selected` node, selection chosen explicitly |
| Multi select | planned | `aria-multiselectable`, Space toggles, Shift range keys |
| Virtualised | thousands of rows | only visible rows are built; `aria-setsize`, `aria-posinset` on every node (as in every tree, [[ADR-0028 Tree rows are flat in the accessibility tree]]) |
| Dense, compact, default | density per container | row tokens of [[Tree Node]] |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | rows at rest | see [[Tree Node]] |
| Focus within | the focused row shows the focus ring; the tree itself draws no ring | [[Focus Ring]] |
| Empty | the empty-state slot (default text "No items", `body_medium`, `on_surface_variant`) is shown | none |
| Disabled tree | all rows disabled | 0.38 content |
| Loading | planned; rows show a progress ring | not specified |

## Tokens used

Row tokens are defined once in [[Tree Node]]; colour roles in [[Colour Roles]]; density in [[Spacing and Density]].

## Sizing and density

The tree takes the density level of its container or project ([[ADR-0002 Desktop density levels and target sizes]]); every row has the same height. The tree is as wide as its parent and as tall as its rows; the scroll container around it sets the viewport. The default level for configuration tools is `compact` (set by the project, not here).

## Dimensions and defaults

The tree is a container: it has no fill, border or text of its own, and every row size lives in [[Tree Node#Dimensions and defaults]]. Container defaults are the ones that make the rows line up. Alignment: rows span the full tree width, stack top to bottom with no gap, and each row's content is start-aligned and vertically centred in the row height. The container values are Tesserae choices #needs-verification-as-design-choice (proposed ADR: tree container defaults).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | N/A: as tall as its rows (row count times the row height of [[Tree Node]]); the surrounding scroll container sets the viewport | N/A: same as default | N/A: same as default | [[Tree#Sizing and density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | min width | - | N/A: the tree is 100 percent of the parent width; below depth times indent plus chevron box plus 16 dp of label the surrounding container scrolls | N/A: same as default | N/A: same as default | [[Tree#Layout and overflow]] | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| container | min height | - | N/A: the height is the row count times the row height, so the 24 dp target minimum is a row property | N/A: same as default | N/A: same as default | [[Tree Node#Dimensions and defaults]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| container | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | design choice, proposed ADR (tree container defaults); the row horizontal padding sits in [[Tree Node]] so that the root chevron has no extra margin (F4) | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container | margin | - | N/A: the parent or the scroll container sets the outer space | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| rows | gap | `space.0` | 0 | 0 | 0 | design choice, proposed ADR (tree container defaults); [[Tree Node]] (rows touch and each has the single-line height) | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| container | border width | - | N/A: the tree draws no border; the surrounding panel or scroll container owns it | N/A: same as default | N/A: same as default | [[Tree#Anatomy]] | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| container | border color | - | N/A: the tree draws no border, so it has no border colour | N/A: same as default | N/A: same as default | [[Tree#Anatomy]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container | corner radius | - | N/A: the tree has no fill or outline, so it has no corner; rows are rectangular ([[Tree Node]]) | N/A: same as default | N/A: same as default | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| empty-state text | font | `body_medium` | 14/20/400/0.25 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| container | icon size | - | N/A: the tree draws no icon of its own; the chevron and the node icon belong to [[Tree Node]] | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| container | elevation | `elevation.level_0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

## Layout and overflow

- Width: 100 percent of the parent. Labels truncate with an ellipsis; the tree does not create horizontal overflow from labels ([[Tree Node]]).
- When rows still exceed the viewport (many rows, or the container narrower than depth x indent + chevron box + 16 dp of label), the surrounding container shows a vertical bar for height overflow and a horizontal bar for width overflow ([[ADR-0003 Scrollbar rule]], F6).
- Virtualised trees build only the visible rows plus 10 rows of overscan on each side; the scroll extent is rows x row height.

## Behaviour

- Pointer: a press chooses the row; on a branch it also opens or closes it. A second press on a chosen leaf does nothing. Wheel scrolls the container.
- Focus: the tree is one Tab stop (roving focus). When it receives focus: the chosen node if there is one, otherwise the first node. Selection does not follow focus; arrow keys move focus only.
- Keyboard, from the WAI-ARIA tree pattern (vertical tree):

| Key | Action |
|---|---|
| Down | focus the next node that is visible, without opening or closing |
| Up | focus the previous visible node |
| Right | closed branch: open it, focus stays; open branch: focus its first child; leaf: nothing |
| Left | open branch: close it; leaf or closed branch that is not a root: focus its parent; closed root: nothing |
| Home | focus the first node |
| End | focus the last visible node |
| Enter | activate: choose the node and, for a branch, toggle it (the same as a press) |
| Space | choose the node without toggling (single select); toggle its selection (multi select) |
| A printable character | focus the next visible node whose label starts with the typed text; characters typed within 1 s extend the text; the search wraps |
| `*` | open all siblings at the level of the focused node |
| Shift plus Up, Down, Space; Ctrl plus Shift plus Home, End | multi select only: extend or toggle selection (APG recommended model) |
| Page Up, Page Down | focus the row one viewport (minus 10 percent) up or down |

- Closing a branch that contains the focused node moves focus to that branch. Opening or closing keeps the chosen node, the scroll offset of rows above, and the focus.
- Scrolling: moving focus scrolls the row into view by the least distance ([[Scrollbar and Scroll Container]]), also in a virtualised tree.
- Touch: the row is the target; 48 dp rows in touch contexts ([[ADR-0002 Desktop density levels and target sizes]]).

## Tooltip and overlay behaviour

Only truncated labels show tooltips, on the label ([[Tree Node]], [[ADR-0004 Tooltip rule]]). A context menu on a node is planned and opens from the Menu key or Shift plus F10 at the focused row ([[Menu]]); it is not specified further here.

## Motion

Chevron rotation 200 ms; no height animation of the children ([[Tree Node]], [[Motion]]).

## Accessibility

- Role `tree` with an accessible name taken from the pane or heading label ("Files", "Structure"), never a generic word.
- Each row: role `treeitem`, `aria-level` (depth + 1), `aria-setsize` and `aria-posinset` (the number of siblings under the same parent and the position among them), `aria-expanded` on branches only, `aria-selected` on selectable rows; the rows are direct children of the tree and no group wrapper is required (the APG flat form, [[ADR-0028 Tree rows are flat in the accessibility tree]], accepted; the claim that screen readers announce this well is unverified until a real pass).
- Multi select: `aria-multiselectable` true.
- Keys per the table; the focus indicator is visible and keyboard only ([[Focus Ring]], [[14 Accessibility Basics]]).
- Collapsing, expanding and selecting changes are exposed as property changes of the node; no extra announcement is made.

## Dark and light

Roles only ([[Theme Following the System]]).

## Defaults

Single select, nothing selected, all branches closed, `default` density unless the project sets one, no tooltip, no multi select.

## Acceptance criteria

- [ ] AC-TRE-01: AT tree assertion. The container has role `tree` and an accessible name equal to the pane label supplied by the app (not the literal word "Tree").
- [ ] AC-TRE-02: Scripted input. The tree is exactly one Tab stop: Tab from the previous control focuses the chosen node (or the first); Tab again leaves the tree; Shift plus Tab returns to the same node.
- [ ] AC-TRE-03: Scripted input. On a tree of 10 visible rows: Down x3 focuses row 4; Up x1 row 3; End row 10; Home row 1; Down at the last row and Up at the first do nothing; no node opens or closes.
- [ ] AC-TRE-04: Scripted input. Right on a closed branch opens it and keeps focus; Right on an open branch focuses its first child; Right on a leaf does nothing.
- [ ] AC-TRE-05: Scripted input. Left on an open branch closes it; Left on a leaf at depth 2 focuses its parent; Left on a closed branch at depth 1 focuses its parent; Left on a closed root does nothing.
- [ ] AC-TRE-06: Scripted input. Typing "pa" within 1 s focuses the next visible node whose label starts with "pa" (case-insensitive); after 1 s pause the buffer resets; typing past the last match wraps to the first.
- [ ] AC-TRE-07: Scripted input. Enter on a branch chooses it and toggles it; Space on a branch chooses it and does not toggle; arrow keys alone never change the chosen node.
- [ ] AC-TRE-08: Scripted input. `*` on a depth-1 node opens every closed sibling at depth 1 and no others.
- [ ] AC-TRE-09: AT tree assertion. Exactly one node has `aria-selected` true in a single-select tree; every selectable node has `aria-selected` true or false; non-selectable nodes have none.
- [ ] AC-TRE-10: AT tree assertion ([[ADR-0028 Tree rows are flat in the accessibility tree]]). Every visible row is a direct child of the tree with role `treeitem`; each branch has `aria-expanded`, each leaf has none; `aria-level` is 1 for roots and increases by 1 per depth; `aria-setsize` equals the number of siblings under the same parent and `aria-posinset` the position among them (not the count of all visible rows); the children of a closed branch are not in the tree. Pass: values equal on a tree with two open levels.
- [ ] AC-TRE-11: Scripted input and AT tree assertion (applies when multi select exists). Space toggles selection, Shift plus Down extends it, the tree has `aria-multiselectable` true.
- [ ] AC-TRE-12: Geometry check. In a virtualised tree of 100000 rows with row height 32 dp and a 400 dp viewport, at most 33 rows (13 visible plus 10 overscan rows on each side) exist at any moment; every built row has `aria-setsize`, `aria-posinset` and `aria-level` (as in every tree, AC-TRE-10); End focuses and shows the last row; the focused row is fully inside the viewport after every key.
- [ ] AC-TRE-13: Geometry check (F6). A tree wider than its container (container 120 dp, depth 6 at `default`) shows a horizontal bar in the surrounding container, and the vertical bar appears when rows exceed the viewport.
- [ ] AC-TRE-14: Scripted input. Closing a branch that contains the focused node moves focus to the branch; opening or closing does not change the chosen node.
- [ ] AC-TRE-15: Geometry check. All rows in one tree have equal height and take the container density; changing the density re-flows the rows with the values of [[Tree Node]].
- [ ] AC-TRE-16: Pixel check. A tree with zero nodes shows the empty-state slot text and no rows.
- [ ] AC-TRE-17: Scripted input. A disabled node is skipped by Up, Down, Home, End and typeahead.
- [ ] AC-TRE-18: Scripted input. Page Down moves focus by (viewport minus 10 percent) / row height rows, rounded down.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Tree_View.tdl`, `TreeLevel_View.tdl`, `TreeNode_View.tdl`, `tess-ui:src/tess_ui/composed.py` (roving focus group, `_typeahead`) | partly meets. Meets: one Tab stop via `Focus_Group: vertical`; Up, Down, Home, End and typeahead with a 1 s reset (AC-TRE-02, 03, 06); Right opens and Left closes a branch; roles tree and treeitem with level and expanded; two-way `Expanded` and `Selected`. Fails: Left does not move to the parent and Right does not move to the first child of an open branch (AC-TRE-04, 05); `*` absent (08); tree label is the literal "Tree" (01); children are not in a `group` element (10); no virtualisation (12); no multi select (11); no empty-state slot (16); no Page keys (18); no scroll-into-view check for rows (inside a vertical `ScrollView`, focus scrolls it, not verified for rows) |
| tess-ui (config app) | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (`files_tree`, `structure_tree` in vertical `ScrollView`s, `Compact: true`) | partly meets: same as above; the `ScrollView` is vertical only, so AC-TRE-13 fails if the tree is wider than the pane |
| tess-shell | none | absent (tree is planned for the configuration application in the shell vault) |
| tre | `tre:crates/engine-core/src/tree/scroll.rs` | not applicable for the tree; the `virtual_list` the tree would use has no key handling and no `scroll_into_view`, so a virtualised tree needs app code for AC-TRE-12 |

Evidence: F3, F4, F5, F6 in [[Owner Feedback 2026-11-20]]; row geometry and the config-app overrides against the spec are in [[Tree Node]].

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | hierarchical navigation | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Selection does not follow focus | APG: authors choose; avoids accidental action in file trees | none; design choice |
| Rows are flat in the accessibility tree, no `group` wrappers | the engine container selection ranges over the direct children of one container; APG allows the flat form | [[ADR-0028 Tree rows are flat in the accessibility tree]] |

## Sources

- WAI-ARIA Authoring Practices, Tree View pattern, keyboard interaction and roles, states and properties: https://www.w3.org/WAI/ARIA/apg/patterns/treeview/ (read 2026-11-21).
- MD3 list item tokens as in [[Tree Node]]; MD3 has no tree (checked in the Material Web repository tree listing, https://github.com/material-components/material-web, 2026-11-21; m3.material.io not read, #needs-verification).
- Code: `tess-ui:src/tess_ui/views/Tree_View.tdl`, `TreeLevel_View.tdl`, `tess-ui:src/tess_ui/composed.py` (`TYPEAHEAD_RESET`, focus group keys), `tess-ui:docs/components/trees.md` (origin/main c7117cb).
