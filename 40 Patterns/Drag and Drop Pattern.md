---
title: Drag and Drop Pattern
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, drag, drop, accessibility]
aliases: ["Drag and Drop pattern", "DnD"]
related: ["[[40 Patterns]]", "[[Drag and Drop]]", "[[Selection]]", "[[Keyboard Navigation]]", "[[Dock]]", "[[Dock Panel]]", "[[List Editor]]", "[[Tree]]", "[[List]]", "[[Menu]]", "[[File Dialog]]", "[[Scrollbar and Scroll Container]]", "[[Focus Ring]]", "[[Elevation]]", "[[Motion]]", "[[Notifications]]", "[[14 Accessibility Basics]]", "[[11 Interaction]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Selection]]", "[[Keyboard Navigation]]"]
---

# Drag and Drop Pattern

> [!info] Summary
> How the user moves or copies content by dragging it: start, feedback, drop targets, cancel with Escape, and the required non-drag alternatives for pointer and keyboard (WCAG 2.2 SC 2.5.7 and SC 2.1.1), within the limits of the engine (no OS file drop on Wayland). The engine and shell capability is the note [[Drag and Drop]]; this note is the interaction rule. MD3 gives only [gesture](https://m3.material.io/foundations/interaction/gestures) guidance and a dragged state; the rest follows WCAG and the WAI-ARIA practices.

## Problem

Dragging content exists only in pieces: tess-ui docks panels by dragging a tab (with a menu alternative), the shell moves a `Panel` with `Movable` and has a `DRAG` peek trigger, the config app moves blocks with Alt+Up and Alt+Down and a menu; list reorder, tree reorder, card drag and node graph connecting are "Not built". The engine reports `dock_target` and `dock_drop` and draws no handle or highlight, in-app drag is manual `capture_pointer`, and OS file drop does not exist on Wayland ([[Gaps and Contradictions]], tre evidence "Drag and drop"; summary item 8).

## Purpose

Let the pointer user move things by direct manipulation without making dragging the only way, with feedback that shows where the item will land and a cheap way to abort.

## When to use and not

- Use when: moving or copying items between containers or positions is a core task (reorder rows, dock panels, move blocks, drop files to open).
- Do not use when: the action is rare or destructive (use a command with a confirmation); the target is a value (use a field); the only benefit is novelty. Dragging never starts an action that has no undo.

## Rules

1. Every drag has a non-drag equivalent, both of them (WCAG 2.2 SC 2.5.7 for a single pointer without dragging; SC 2.1.1 for the keyboard): (a) a single-pointer alternative: a menu "Move to" or "Move up, Move down" buttons, or click to pick up and click to drop; (b) a keyboard alternative: Alt+Up, Alt+Down move the focused item among its siblings, and a menu (Menu key or Shift+F10) offers "Move to" with a list of targets. The tess-ui dock and the config app already have both.
2. Start: a press on the item (or its grip) followed by movement of at least 4 dp starts the drag; a press without movement is a click (threshold shared with [[11 Interaction]]); a drag never starts on a press in a text field's text or on a scrollbar. Touch: long press 500 ms starts it (design choice, #needs-verification-as-design-choice).
3. What moves: the whole selection when the pressed item is selected ([[Selection]], rule on press of a selected item), else only the pressed item. The count shows on the drag image when more than one item.
4. Drag feedback has four parts, all required:
   - the source shows the dragged state layer, 16 percent ([[State Layers]], MD3 `md.sys.state.dragged.state-layer-opacity`; tess-ui `DRAGGED` 0.16);
   - the drag image follows the pointer at an offset of 8 dp, `surface_container_high` container, level 2, the item's text at `body_medium`, at most 2 lines;
   - the pointer shape changes: grabbing while dragging, not-allowed over an invalid target (where the platform allows it; the engine sets the cursor per node);
   - the valid target shows a drop indicator (below), the invalid ones show nothing.
5. Drop indicator: between items a 2 dp line in `primary` with a 6 dp end dot, spanning the row; onto an item (move into a container, a tree branch) a 2 dp `primary` outline on the target and an 8 percent `primary` fill; onto a zone (dock) a `primary` fill at 12 percent with a 2 dp outline. The indicator is never colour alone: the line or outline is a shape. A target holds focus ring and drop indicator without overlap.
6. Targets declare what they accept; a target that cannot accept the item shows no indicator and the drop does nothing. A drop onto itself or a descendant is refused with a polite message.
7. Hover to open: holding a dragged item over a closed tree branch or collapsed group for 700 ms opens it; moving away within the time cancels it (design choice).
8. Autoscroll: within 24 dp of a scroll container edge the container scrolls at 8 dp per frame at 60 Hz, up to 32 dp per frame at the edge itself; it stops when the pointer leaves the band or the drag ends ([[Scrollbar and Scroll Container]]).
9. Cancel: Escape during a drag aborts it with no change: the drag image disappears, the source returns to normal, no drop event is raised. Releasing over no target also aborts. Losing pointer capture or window focus aborts. Escape takes effect before any other key action (it closes no overlay during a drag).
10. Drop result: the move shows at once (a 100 ms settle, none under reduced motion) and the result is announced politely ("Moved Alpha to position 3 of 7", "Docked Terminal at the bottom"); an undo is offered through the app's undo, and for a destructive result a [[Snackbar]] with Undo ([[Notifications]]).
11. Keyboard alternative detail: Alt+Up and Alt+Down move the focused item one step among its siblings and keep focus on the moved item; Alt+Home and Alt+End move it to the first and last place (design choice); the move is announced as in rule 10; at the first or last place the key does nothing and says so politely. "Move to" opens a [[Menu]] of valid targets with the current place marked.
12. Files from the OS (engine): `file_hover`, `file_drop` and `file_hover_cancel` reach the node under the pointer (tre 0.5.4) but there is no drop from the OS on Wayland (winit 0.30), no drag source, and on X11 the position can be missing. A drop zone for files therefore: (a) never is the only way, an Open button and a File dialog exist ([[File Dialog]]); (b) shows its hover highlight on `file_hover` and removes it on `file_hover_cancel`; (c) states its accepted types before the drop.
13. Drag between windows and from the app to the OS is not supported; no pattern offers it.
14. Reduced motion: no settle animation, no fade of the drag image, indicators appear at once; autoscroll speed stays.

## Decision table

| What is moved | Drag start | Drop target | Non-drag pointer alternative | Keyboard alternative |
|---|---|---|---|---|
| A row in a [[List Editor]] or [[List]] | row grip or row | between rows | Move up and Move down buttons | Alt+Up, Alt+Down |
| A tree node or block | node | between or onto a node | menu "Move into..." and Move up, Move down | Alt+Up, Alt+Down; Ctrl+Shift+M "Move into" list |
| A dock panel | its tab | a zone of the [[Dock]] | tab menu "Move to ..." (right click) | Menu key or Shift+F10, "Move to ..." |
| A shell Panel (`Movable`) | panel | screen position | config key or menu entry | shell shortcut mode ([[Keyboard Navigation]]) |
| Files from the OS | file manager | file drop zone (X11, Windows, macOS) | Open button, [[File Dialog]] | the same button by keyboard |
| A slider thumb, a splitter, a resize handle | thumb or handle | the track | click on the track moves it (SC 2.5.7 slider example) | arrow keys, Page keys, Home, End |
| A node graph edge | port | another port | pick source then pick target | Tab to the port, Enter, Tab to target, Enter (planned) |

## Examples (short snippets only)

```python
handle.on("pointer_down", lambda: window.start_panel_drag(panel))   # engine
window.on("dock_target", show_target)       # app draws the highlight
window.on("dock_drop", lambda: highlight.remove())
```

The config app moves a block with Alt+Up, Alt+Down, Ctrl+Shift+M and a menu; every one of them is one undo step (`tess-ui:apps/shell_config/README.md`, keys table).

## States

| State | Visual change | Token values |
|---|---|---|
| Draggable, rest | optional grip icon 18 dp at default and compact, 16 dp at dense, `on_surface_variant` | [[Iconography]] |
| Pressed, not yet dragging | pressed state layer 10 percent | [[State Layers]] |
| Dragging, source | dragged state layer 16 percent | [[State Layers]] |
| Drag image | `surface_container_high`, level 2, radius 8 dp | [[Elevation]], [[Shape]] |
| Valid target | drop indicator (rule 5) | [[Colour Roles]] |
| Invalid target | no indicator, not-allowed cursor | none |
| Dropped | 100 ms settle | [[Motion]] |
| Cancelled | back to rest at once | none |

## Sizing and density

The 4 dp start threshold and the 24 dp autoscroll band are density independent. The grip is the row height (40, 32, 24 dp) by 24 dp wide at least, so its hit area meets 24 dp ([[Spacing and Density]]). The drop line is 2 dp at all densities; the tree "onto" outline is 2 dp inside the row. The drag image max width is 240 dp.

## Accessibility

- The draggable item exposes the alternatives: its context menu has "Move to ..." and its description says "Alt+Up and Alt+Down move this item" (also in the help line or tooltip, never only there).
- `aria-grabbed` and `aria-dropeffect` are deprecated in WAI-ARIA 1.2 and are not used. The app announces the start of a keyboard move and each new position ("Moved to position 3 of 7").
- No keyboard trap in a keyboard move: Escape cancels, Enter or the key release commits.
- Drop targets are not additional Tab stops.

## Acceptance criteria

- [ ] AC-DNP-1 (scripted input): every action that can be done by dragging in a view (reorder, dock, move block, slider thumb) can also be done by a single click or tap sequence (a menu entry, buttons, a click on the track). The script performs each action with pointer press-release only. Pass: effect equals the drag result for every action.
- [ ] AC-DNP-2 (scripted input): the same actions are performed by key events only: Alt+Up, Alt+Down, Menu key then "Move to", arrow keys on a slider. Pass: effect equals the drag result; focus stays on the moved item.
- [ ] AC-DNP-3 (scripted input): a pointer press followed by 3 dp of movement and release is a click (activation count 1, no drag event); 4 dp starts a drag. Pass: counts equal.
- [ ] AC-DNP-4 (scripted input): Escape during a drag leaves the data unchanged, raises no drop event, removes the drag image and indicator within one frame and removes the dragged state layer; releasing over no target behaves the same. Pass: data equal, event count 0.
- [ ] AC-DNP-5 (pixel check): while dragging, the source shows the 16 percent dragged state layer, a drag image of `surface_container_high` follows the pointer at 8 dp offset, and over a valid target a drop indicator (2 dp `primary` line, outline or zone fill) is present; over an invalid target none. Pass: pixel regions present or absent.
- [ ] AC-DNP-6 (pixel check): the drop indicator differs from its absence in shape pixels in a greyscale render (not colour alone). Pass: shape pixels present.
- [ ] AC-DNP-7 (scripted input): dragging 3 selected items by one of them carries all three and shows the count 3; dragging an unselected item while others are selected moves only it. Pass: moved sets equal.
- [ ] AC-DNP-8 (scripted input): holding a dragged item 700 ms over a closed branch opens it; leaving at 600 ms does not. Pass: expanded flag equals.
- [ ] AC-DNP-9 (geometry check): within 24 dp of a scroll container edge the container scrolls during a drag at 8 to 32 dp per frame and stops 1 frame after the pointer leaves the band or the drag ends. Pass: scroll deltas in range.
- [ ] AC-DNP-10 (AT tree assertion): a completed move produces exactly one polite announcement with item name and new position; a refused drop (onto itself) produces one polite refusal. Pass: announcement count and text equal.
- [ ] AC-DNP-11 (scripted input): a drop of a file onto a drop zone raises `file_hover` then `file_drop` with the paths; `file_hover_cancel` removes the highlight; an Open button in the same view performs the same action. Pass: events and effect equal; on Wayland the test asserts only the button path and records "OS drop unavailable".
- [ ] AC-DNP-12 (scripted input): with `reduced_motion` true, the drop settle and fades take at most 1 frame. Pass: frame count at most 1.
- [ ] AC-DNP-13 (geometry check): the pointer hit area of a drag grip is at least 24 by 24 dp at each density. Pass: bounds at or above 24.
- [ ] AC-DNP-14 (review): no feature in a view requires dragging with no alternative and no destructive result lacks undo. Pass: reviewer checklist per view.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/docking.py`, `tess-ui:docs/guide/docking.md`, `tess-ui:apps/shell_config/README.md`, `tess-ui:docs/guide/gestures.md` (`On_File_Drop`) | partly meets: dock tab drag with zone highlight and the "Move to ..." menu by right click, Menu key and Shift+F10 (AC-DNP-1, AC-DNP-2 meet for docks by reading); config app block move with Alt+Up, Alt+Down, Ctrl+Shift+M and menu, one undo step each (AC-DNP-1, AC-DNP-2); Escape cancel not documented (AC-DNP-4 unmeasured); no drag image, no list or tree reorder ("Not built: drag reorder"), no multi drag, no hover to open, no autoscroll (AC-DNP-5, AC-DNP-7 to AC-DNP-9 fail); `List Editor` has no Alt+arrow move ("Not built") |
| tess-shell | `tess-shell:src/tess_shell/surfaces/manager.py`, `tess-shell:docs/guide/surfaces.md#panel` | partly meets: `Movable` Panel and `DRAG` Peek trigger exist with a saved position; no content drag and drop; no keyboard or menu alternative for `Movable` (AC-DNP-1, AC-DNP-2 fail for Panel move); slider drag has arrow keys, Page keys, Home, End (AC-DNP-2 meets for sliders by reading) |
| tre | `tre:docs/guide/events-and-input.md` (Pointer capture, Files dragged from the OS), `tre:docs/guide/docking.md` | partly meets as engine: `capture_pointer`, `release_pointer`, `dock_target`, `dock_drop`, `file_hover`, `file_drop`, `file_hover_cancel`; no handle, highlight or drag image; no OS file drop on Wayland (winit 0.30), no drag source, X11 position can be missing |

Request candidates: a drag session helper (threshold, Escape cancel, autoscroll, drag image) in tess-ui; Alt+Up and Alt+Down in `ListEditor`; routed through the Orchestrator. Engine limits are recorded, not requested.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A required non-drag alternative for every drag | WCAG 2.2 SC 2.5.7 and SC 2.1.1 | none; accessibility rule, [[14 Accessibility Basics]] |
| 4 dp start threshold, Escape cancel, 700 ms hover open, autoscroll values | MD3 gives no desktop drag rules | none; design choice |
| Drag image, drop indicator shapes and hover-to-open | MD3 gives the dragged state layer only | none; design choice |

## Sources

- [WCAG 2.2 Understanding SC 2.5.7 Dragging Movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html): all drag functionality has a single pointer alternative without dragging; examples: sortable list with up and down controls, kanban with menu or arrow buttons, slider with click on the track; keyboard equivalence alone does not meet it; scrolling by the user agent is exempt. Verified 2026-11-21.
- [WCAG 2.2 SC 2.1.1 Keyboard](https://www.w3.org/TR/WCAG22/#keyboard); [WAI-ARIA 1.2: `aria-grabbed` and `aria-dropeffect` deprecated](https://www.w3.org/TR/wai-aria-1.2/#aria-grabbed).
- [WAI-ARIA APG Listbox rearrangeable example](https://www.w3.org/WAI/ARIA/apg/patterns/listbox/examples/listbox-rearrangeable/): toolbar buttons that move options.
- MD3 gesture and dragged-state guidance at m3.material.io is not readable by tools #needs-verification.
- The thresholds 4 dp, 500 ms, 700 ms, autoscroll band and speeds, drop indicator sizes are design choices #needs-verification-as-design-choice.
- Code and engine: `tre:docs/guide/events-and-input.md`, `tre:docs/guide/docking.md`; `tess-ui:docs/guide/docking.md`, `tess-ui:docs/components/dock-panel.md`; `tess-ui:apps/shell_config/README.md`; `tess-shell:docs/guide/surfaces.md`; [[Gaps and Contradictions]] (tre evidence "Drag and drop").
