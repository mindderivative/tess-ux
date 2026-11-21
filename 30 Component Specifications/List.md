---
title: List
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, list, keyboard, virtualisation]
related: ["[[List Item]]", "[[Tree]]", "[[Scrollbar and Scroll Container]]", "[[Menu]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[Deviations from MD3]]"]
depends_on: ["[[List Item]]", "[[Scrollbar and Scroll Container]]"]
---

# List

> [!info] Summary
> A column of [[List Item]] rows that scrolls, with one Tab stop, arrow-key navigation and optional single or multiple selection. Counterpart: Material Design 3 lists (https://m3.material.io/components/lists/overview); keyboard behaviour from the WAI-ARIA listbox pattern. Source of truth in code: the last section.

## Purpose

Let the user scan, choose and act on a set of like items, with the keyboard first and with long sets handled by virtualisation.

## When to use and not

- Use when: the set is flat, or has section headers only.
- Do not use when: the set is hierarchical ([[Tree]]); the choice is a command set ([[Menu]]); rows hold editable form controls ([[Form Row]]).

## Anatomy

1. List container: clips, scrolls, carries the role and name.
2. Section header (optional): sticky label row.
3. [[List Item]] rows.
4. Dividers (optional).
5. Empty-state slot.
6. Scrollbar ([[Scrollbar and Scroll Container]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Plain | display, role `list` | rows activate but are not chosen |
| Single select | pick one, role `listbox` | one `aria-selected` row |
| Multi select | pick several, role `listbox` with `aria-multiselectable` | Space toggles, Shift range keys |
| Virtualised | more than about 200 rows | only visible rows are built |
| Grouped | sections with sticky headers | a header sticks at the top while its rows scroll |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | rows at rest | [[List Item]] |
| Focus within | the focused row shows the ring | [[Focus Ring]] |
| Empty | empty-state slot (default text "No items", `body_medium`, `on_surface_variant`, centred) | none |
| Disabled | all rows disabled | 0.38 |
| Loading | planned (progress indicator row) | not specified |

## Tokens used

Row tokens are defined once in [[List Item]]; scrollbar tokens in [[Scrollbar and Scroll Container]]; roles in [[Colour Roles]].

## Sizing and density

Density comes from the container or project ([[ADR-0002 Desktop density levels and target sizes]]); all rows of a list share it. Width 100 percent of the parent (the shell List defaults to 240 by 200 dp when no size is given). Height is set by the parent; a list taller than its parent is wrapped in a scroll container. A sticky section header has the single-line row height of the density and role `title_small` text in `on_surface_variant`.

## Layout and overflow

- Vertical scrolling for rows. Rows truncate their text, so a list does not scroll horizontally; if a trailing control makes the row wider than the list, the list shows a horizontal bar ([[ADR-0003 Scrollbar rule]], F6).
- The container reserves the scrollbar gutter on the end edge when it overflows ([[Scrollbar and Scroll Container]]).
- Empty state: when the row count is 0 the container shows the empty-state slot (a hook: the app supplies text and an optional icon; a loading state is separate).

## Behaviour

- Pointer: click selects (selectable) or activates; wheel scrolls; hover per row.
- Focus: one Tab stop for the whole list (roving). On focus: the selected row if any, otherwise the first row. For a single-select list selection does not follow focus unless the app sets it so; the shell List chooses on arrow keys (a choice per project, stated by the app).
- Keyboard (WAI-ARIA listbox, https://www.w3.org/WAI/ARIA/apg/patterns/listbox/):

| Key | Action |
|---|---|
| Down, Up | focus the next, previous enabled row |
| Home, End | focus the first, last enabled row (recommended for lists of more than 5 rows) |
| Page Down, Page Up | focus the row one viewport (minus 10 percent) away |
| Enter | activate the focused row |
| Space | choose the focused row (single), toggle it (multiple) |
| Printable characters | focus the next row whose text starts with the typed text; the buffer resets after 1 s |
| Shift plus Up, Down, Space | multiple select only: extend the selection, toggle |

- A disabled row is passed over by every key.
- Virtualised: the keys act on the data (row index), not on built rows. Home and End scroll to the first and last row and focus it; the focused row is always built and scrolled into view by the least distance. Rows expose `aria-setsize` and `aria-posinset`. The thumb is draggable ([[Scrollbar and Scroll Container]]).
- Touch: drag scrolls with fling; swipe actions are not applicable on desktop.
- Reorder by drag is planned; Alt plus Up and Alt plus Down will move the focused row; not specified further.

## Tooltip and overlay behaviour

Rows carry no tooltip; truncated text carries one on the text ([[List Item]]). A context menu opens at the focused row from the Menu key or Shift plus F10 ([[Menu]]).

## Motion

None for rows. Scrolling by keys jumps. Reduced motion changes nothing.

## Accessibility

- Role `list` (plain) or `listbox` (selectable) with an accessible name from the visible label or heading; the rows are `listitem` or `option`.
- A virtualised list sets `aria-setsize` and `aria-posinset` on built rows.
- Group headers: rows are inside an element with role `group` named by the header (APG listbox).
- An empty list announces its empty text once when it becomes empty.

## Dark and light

Roles only ([[Theme Following the System]]).

## Defaults

Plain list, vertical scroll, no dividers, `default` density unless the project sets a level, empty text "No items".

## Acceptance criteria

- [ ] AC-LST-01: AT tree assertion. The container has role `list` or `listbox` and an accessible name; a selectable list has rows with role `option` and `aria-selected`; a multi select list has `aria-multiselectable` true.
- [ ] AC-LST-02: Scripted input. The list is one Tab stop; Tab focuses the selected row (or the first); Tab again leaves.
- [ ] AC-LST-03: Scripted input. Down, Up, Home, End move focus by one row or to the ends of 20 rows and never past them; Page Down moves by (viewport minus 10 percent) / row height rows, rounded down.
- [ ] AC-LST-04: Scripted input. Typing "ba" within 1 s focuses the next row whose text starts with "ba"; after 1 s idle the buffer is empty.
- [ ] AC-LST-05: Scripted input. Enter activates the focused row; Space chooses it; in a multi select list Space toggles and Shift plus Down extends the selection.
- [ ] AC-LST-06: Scripted input. A disabled row is skipped by arrows, Home, End and typeahead.
- [ ] AC-LST-07: Scripted input on a virtualised list of 100000 rows. End focuses row 99999 and scrolls it into view; Home focuses row 0; the focused row stays inside the viewport after every key; at most (viewport rows + 20) rows exist; built rows have `aria-setsize` 100000 and `aria-posinset`.
- [ ] AC-LST-08: Geometry check (F6). A list whose rows are wider than the list shows a horizontal bar; a list whose rows exceed the viewport shows a vertical bar; neither shows when content fits.
- [ ] AC-LST-09: Pixel check. A list with 0 rows shows the empty-state text centred and no rows; the list role and name remain.
- [ ] AC-LST-10: Geometry check. Sticky section header stays at the top of the viewport while its rows scroll, and is replaced by the next header when that reaches the top.
- [ ] AC-LST-11: Scripted input. Shift plus F10 and the Menu key on a focused row emit the context-menu request for that row (applies when a context menu exists).

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/ListItem_View.tdl`, `tess-ui:docs/components/lists.md`, `VirtualList` node | partly meets. There is no `List` view: a list is a container of `ListItem` rows (or a `For`, or a `VirtualList`). No roving focus group, no type-ahead, no Home, End on a plain list (fails AC-LST-02 to 06); sticky headers exist (`Sticky: 0`); no empty-state slot (AC-LST-09 fails); virtual list uses the engine node (see tre) |
| tess-shell | `tess-shell:src/tess_shell/shipped/List/List_Module.tdl` | partly meets. One Tab stop; Up, Down, Page Up, Page Down, Home, End, Enter and Space choose when none is chosen, type-ahead with a 1 s end of search, disabled rows skipped, each move is a choice that scrolls the row into view (meets AC-LST-02, 03 in part, 04, 06; the Page distance is not 90 percent of the viewport: not verified); single select only, no multi select (AC-LST-05 partly); role LIST with LISTITEM rows (not listbox and option); no scrollbar (AC-LST-08 fails); no empty state; 240 by 200 default size |
| tre | `tre:crates/engine-core/src/tree/scroll.rs`, `dispatch.rs`, `tre:docs/guide/nodes-and-layout.md` (Virtual lists) | partly meets. `virtual_list` builds only visible rows (`materialize`, `item_extent`, `size_hint`) and has a draggable vertical thumb; no key handling, `scroll_into_view` skips it (fails AC-LST-07 without app code) |

Evidence: F6 in [[Owner Feedback 2026-11-20]] and the shell Launcher list. The engine gap (no key handling in `virtual_list`) is a request candidate for the Orchestrator.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Keyboard model from the WAI-ARIA listbox pattern; MD3 defines no list keyboard behaviour | desktop, keyboard first | [[ADR-0010 Document structure of the specifications]] |
| Densities per [[List Item]] | desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Scrollbar visible, no auto-hide | desktop | [[ADR-0003 Scrollbar rule]] |

## Sources

- MD3 lists: https://m3.material.io/components/lists/overview (page not rendered by the reader; values taken from Material Web tokens, see [[List Item]]). #needs-verification (m3.material.io text on selection, dividers and grouping).
- WAI-ARIA Authoring Practices, Listbox pattern, keyboard interaction and roles: https://www.w3.org/WAI/ARIA/apg/patterns/listbox/ (read 2026-11-21).
- Code: `tess-shell:src/tess_shell/shipped/List/List_Module.tdl`, `tess-ui:docs/components/lists.md`, `tre:docs/guide/nodes-and-layout.md` (Virtual lists, Keyboard scrolling).
