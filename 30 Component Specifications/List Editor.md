---
title: List Editor
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, input, list, editor, keyboard]
related: ["[[List]]", "[[List Item]]", "[[Text Field]]", "[[Switch]]", "[[Icon Button]]", "[[Button]]", "[[Menu]]", "[[Colour Picker]]", "[[Choice Picker]]", "[[Form Row]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[State Layers]]", "[[Colour Roles]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[List]]", "[[Icon Button]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]"]
---

# List Editor

> [!info] Summary
> An editor for a list of values of one kind (text, number, switch, enum, colour): one row per item with the item's own control and Move up, Move down and Remove buttons, and an Add button under the rows. Material Design 3 has no list editor; the note builds on MD3 [Lists](https://m3.material.io/components/lists/overview), [[Icon Button]] and the matching field controls. Source of truth in code: the last section.

## Purpose

Let a person keep, order, add and remove the values of a list setting (the words of a launcher filter, outputs, palette colours) with the pointer or the keyboard alone.

## When to use and not

- Use when: the value is a list whose items are all of one kind and order may matter.
- Do not use when: the items are hierarchical ([[Tree]]); the items are mixed kinds or lists themselves (not built); the list is read-only ([[List]]); the set is a fixed choice of several ([[Choice Picker]] with multiple selection, not specified).

## Anatomy

1. Group container, named by `Label`.
2. Rows container (role `list`) with rows (role `listitem`, name "Label n").
3. Row: item control (text [[Text Field]], number spin box, [[Switch]], enum button opening a [[Menu]], colour swatch opening a [[Colour Picker]] popup), then Move up, Move down and Remove [[Icon Button]]s.
4. Empty note "No items".
5. Message line (role `alert`): why an edit did nothing (list at its fewest, at its most).
6. Add [[Button]] (text variant, label `Add_Label`).
7. Row drag handle (not built).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Text | words, names | field writes on Enter or on leaving, never per key |
| Number | sizes, levels | spin box with `Least`, `Most`, `Step`; an `int` stays `int` when the step is whole |
| Bool | flags | switch writes on change |
| Enum | a choice per item | button with the label opens a menu of `Choices` |
| Colour | palette | swatch opens the colour popup ([[Colour Picker]]) |
| Bounded | `Min_Items`, `Max_Items` | Remove stops at the least, Add stops at the most (0 means no limit) |

## States

| State | Visual change | Token values |
|---|---|---|
| Row rest | transparent | item control per its own note |
| Row focus-within | the focused control shows the ring; the row has no fill | [[Focus Ring]] |
| Move up disabled | first row | 0.38 on content |
| Move down disabled | last row | 0.38 on content |
| Remove disabled | at `Min_Items` | 0.38, message says why when pressed or on focus |
| Add disabled | at `Max_Items` | 0.38 |
| Row invalid | an item that does not fit the kind shows the kind's nearest value (0, first choice, black) and keeps the stored item until edited; a hint marks the row | `error` outline on the control |
| Empty | note in the rows area | `on_surface_variant` |
| Disabled | nothing edits | 0.38 |

## Tokens used

[[Colour Roles]], [[Typography]] (`body_medium`, `label_large`), [[Spacing and Density]], [[State Layers]], [[Focus Ring]]. The editor adds only the empty note (`on_surface_variant`) and the message (`error`); controls keep their own tokens.

## Sizing and density

| Part | default | compact | dense | Code today |
|---|---|---|---|---|
| Row height | 40 | 32 | 28 | the item control's height |
| Icon button container (Move up, down, Remove) | 40 | 32 | 28 | 40 |
| Icon button icon | 24 | 20 | 20 | 24 |
| Gap between row controls | 8 | 8 | 4 | 8 |
| Gap between rows | 8 | 4 | 4 | 8 |
| Text item field width | fills the row minus the three buttons and gaps | same | same | up to 240 |

Hit areas at least 24 by 24 dp at every density ([[ADR-0002 Desktop density levels and target sizes]]). The three icon buttons keep 4 dp of space between hit areas at dense.

## Layout and overflow

- Row: horizontal, vertically centred, the item control takes the remaining width with minimum width 0 and the three buttons stay at the end edge; a text item truncates its display with an ellipsis only while unfocused ([[10 Layout Overflow and Scrolling]]).
- The editor grows with its rows. When the app limits its height, the rows container scrolls vertically with a visible [[Scrollbar and Scroll Container]] ([[ADR-0003 Scrollbar rule]]); there is no horizontal scroll.
- Moving or removing a row keeps the other rows' identity, so a field being typed in and an open menu are kept.

## Behaviour

- Writing: a text row writes on Enter or on leaving the field; a spin box, switch, menu and colour picker write on change. An edit writes a new list in which only the edited item differs, and the change handler is called after it. A list the app sets is never rewritten or normalised.
- Pointer: Move up and Move down swap with the neighbour; Remove deletes; Add appends an item of the kind (empty text, the least number or 0, false, the first choice, black).
- Keyboard. Tab goes through each row's item control, Move up, Move down and Remove, on to the next row, and last to Add.

| Key | Action |
|---|---|
| Tab, Shift+Tab | next, previous control |
| Enter, Space on a button | press it |
| Enter in a text item | commit the item |
| Alt+Up, Alt+Down on a focused row control | move the row up or down and keep focus on the same control (not built) |
| Delete on a focused row control | remove the row and focus the next row, or the previous when last (specified, not built) |
| Escape | closes an open menu or colour popup |
| Arrows | the spin box's and the menu's |

- After Remove focus goes to the next row's item control, or the previous when the last row went, or to Add when the list is empty. After Add focus goes to the new row's item control. After a move focus stays on the pressed button of the moved row.
- Touch: 48 dp hit areas in a touch context; drag to reorder is not built.

## Tooltip and overlay behaviour

Tooltips belong to controls only ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]): Move up, Move down and Remove show their labels ("Move up", "Move down", "Remove") after 500 ms of hover and immediately on keyboard focus (the icon button label is its tooltip); the Add button has a text label and no tooltip. The row and the group carry no tooltip. The enum menu is a [[Menu]] and the colour picker a [[Popup]] ([[12 Overlays]]); focus returns to the opening control on close.

## Motion

Rows do not animate when moved or removed by default; an optional 150 ms slide of a moved row is allowed ([[Motion]]); reduced motion removes it.

## Accessibility

- The group is a `group` named by `Label` (default "Items"). The rows container is `list`; each row is `listitem` named "Label n" (for example "Shortcuts 2"); the item control has the same name; the buttons are named "Move up", "Move down", "Remove" and the Add label. The message line is role `alert`, polite.
- Announcements: Add announces "Label n added, n items"; Remove announces "removed, n items"; a move announces "moved to position n of N"; the at-limit message is spoken once when an edit is refused.
- Keys: the table above. Every action reachable by pointer is reachable by Tab and Enter.
- Contrast: empty note and hints `on_surface_variant` at least 4.5:1; controls per their own notes.
- Target size: at least 24 by 24 dp at every density.

## Dark and light

Roles only ([[Theme Following the System]]).

## Defaults

Item kind `text`, `Step` 1, `Min_Items` 0, `Max_Items` 0 (no limit), label "Items", Add label "Add", empty note "No items".

## Acceptance criteria

- [ ] AC-LED-1 (geometry check): at default, compact and dense the three icon buttons are 40, 32 and 28 dp square and a text row is 40, 32 and 28 dp high, at scale 1.0 and 2.0; the gap between row controls is 8, 8 and 4 dp.
- [ ] AC-LED-2 (scripted input): Add on `[a, b]` of kind text yields `[a, b, ""]`; kinds number, bool, enum and colour append the least number or 0, false, the first choice and `#000000`; Add is disabled at `Max_Items`.
- [ ] AC-LED-3 (scripted input): Move up on row 2 of `[a, b, c]` gives `[b, a, c]`, Move down on row 2 gives `[a, c, b]`; row 1 has Move up disabled and the last row has Move down disabled; the change handler fires once per move.
- [ ] AC-LED-4 (scripted input): Remove on `[a, b, c]` row 2 gives `[a, c]`; at `Min_Items` it changes nothing and the message line states why.
- [ ] AC-LED-5 (scripted input): in a text row typing does not write; Enter writes once; leaving the field writes once; an edit writes a new list in which only that item differs.
- [ ] AC-LED-6 (token test): a list set by the app with `"x"` among numbers is shown as 0 for that row and stays `"x"` in the value until that row is edited; no write happens on show.
- [ ] AC-LED-7 (scripted input): moving row 2 while row 3 holds typed, uncommitted text keeps that text in the moved row, not in the row at position 3.
- [ ] AC-LED-8 (scripted input): Tab order for 2 rows is row 1 control, Move up, Move down, Remove, row 2 control, Move up, Move down, Remove, Add; Enter and Space press a focused button.
- [ ] AC-LED-9 (AT tree assertion): the group has a name; rows are `listitem` named "Label n"; the buttons are named "Move up", "Move down", "Remove"; the message line has role `alert`.
- [ ] AC-LED-10 (scripted input): after Remove of the last row focus is on the previous row's control; after Remove of the only row focus is on Add; after Add focus is on the new row's control.
- [ ] AC-LED-11 (scripted input): a tooltip appears on Move up after 500 ms hover and at once on focus, none over a row, the group or the Add button; Escape, a press, a scroll and leaving remove it.
- [ ] AC-LED-12 (scripted input): Alt+Down on a focused control of row 1 moves the row to position 2 and focus stays on that control; Delete removes the row and focuses the next. Pass applies once Alt+arrow and Delete exist; the status is recorded below.
- [ ] AC-LED-13 (pixel check): a row wider than the editor shows the three buttons fully at the end edge and the item control shrinks; no ink leaves the editor; a 20-row editor in a 300 dp tall frame shows a vertical scrollbar thumb of at least the minimum thumb length.
- [ ] AC-LED-14 (AT tree assertion): Add, Remove and a move each produce one announcement with the new count or position.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/ListEditor_View.tdl`, `ListEditorRow_View.tdl`, `ListEditor_Stylesheet.tdl`, `tess-ui:src/tess_ui/list_controls.py` (`ListModel`), `tess-ui:docs/components/list-editors.md` | partly meets. Passes AC-LED-2 to 7 and 9 by documented behaviour (not run here). Fails AC-LED-1 (no density), AC-LED-10 (no focus rule), AC-LED-11 (the buttons show their label as tooltip, no run evidence), AC-LED-12, AC-LED-13 (no scroll container in the view), AC-LED-14 |
| tess-ui | Not built (component doc) | dragging a row to move it, Alt+arrow keys to move one (a handler cannot yet choose between three calls by the key), items of mixed kinds, items that are themselves lists |
| tess-shell | `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`ListWidget`) | partly meets: the config app edits list keys through the toolkit editor; turning a TDL list into text and back is the widget's job, not the editor's |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element has no MD3 counterpart | MD3 has no editor for a list of values | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltip on the icon buttons only | owner feedback F2, F8 | [[ADR-0004 Tooltip rule]] |
| Alt+arrow keys to reorder, Delete to remove | keyboard-first desktop use | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- tess-ui: `tess-ui:docs/components/list-editors.md`, `tess-ui:src/tess_ui/views/ListEditorRow_View.tdl`, `tess-ui:src/tess_ui/views/ListEditor_View.tdl`, `tess-ui:src/tess_ui/list_controls.py`.
- WAI-ARIA APG listbox https://www.w3.org/WAI/ARIA/apg/patterns/listbox/ and the APG practice for reorderable lists (Alt plus arrows is a convention, not an APG pattern #needs-verification); WCAG 2.2 SC 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, SC 4.1.3 https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html (links in [[File Dialog]]).
- Material Web icon button and list docs https://github.com/material-components/material-web/tree/main/docs/components (no list editor exists).
