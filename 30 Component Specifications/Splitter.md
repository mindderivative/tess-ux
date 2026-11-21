---
title: Splitter
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, containment, splitter, keyboard, accessibility]
related: ["[[Dock]]", "[[Dock Panel]]", "[[Panel and Surface]]", "[[Scrollbar and Scroll Container]]", "[[Tree]]", "[[State Layers]]", "[[Focus Ring]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# Splitter

> [!info] Summary
> A Splitter divides an area into two panes with a draggable, keyboard-operable handle between them. MD3 has no splitter; its nearest patterns are the drag handle of the canonical layouts (Compose Material 3 `VerticalDragHandle` and `HorizontalDragHandle`, sized by `DragHandleSizes`) and the WAI-ARIA Authoring Practices window splitter. This note follows the APG window splitter for roles and keys. Source of truth in code: see Status in code.

## Purpose

A user resizes two adjacent panes (a file tree beside an editor, a list above a detail view) to give one more room, and can fold one away. Resizing works by pointer drag and by keyboard alone.

## When to use and not

- Use when: exactly two panes share one area and the user decides the split (a sidebar, a console under an editor).
- Do not use when: more than two panes (nest splitters); panels the user also rearranges between zones ([[Dock]]); panes whose sizes the layout decides by window size class ([[10 Layout Overflow and Scrolling]]); a fixed divider with no resize (use a divider line, see [[Panel and Surface]]).

## Anatomy

1. First pane (the primary pane).
2. Handle: a focusable strip between the panes, 24 dp wide (horizontal splitter, panes side by side) or 24 dp high (vertical splitter, panes stacked), as long as the splitter on the cross axis.
3. Grip: a 4 by 48 dp rounded bar (radius 2 dp) centred in the handle, role `outline`; the grip's size is the MD3 drag handle size used by tess-ui #needs-verification (the Compose Material 3 `DragHandleSizes` class holds size, pressed size and dragged size; the dp values are not readable from the sources fetched).
4. Second pane.

In this note the terms are "side by side" (panes left and right, handle vertical) and "stacked" (panes top and bottom, handle horizontal). The APG calls the handle of a side-by-side splitter a vertical splitter.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Side by side (`horizontal`) | Default | Handle moves left and right; cursor `col_resize` |
| Stacked (`vertical`) | Console under editor | Handle moves up and down; cursor `row_resize` |
| Collapsible | A pane that can fold away | `Collapsible: true`: Enter toggles collapse; double click on the handle too |
| Fixed | Toggle between two positions | Not built; the APG describes it; omit the arrow keys when built |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Grip drawn | grip `outline` |
| Hover | State layer over the handle; cursor resize | `on_surface` at 8 percent ([[ADR-0009 State layer percentages]]) |
| Focus (keyboard) | State layer plus focus ring | layer 10 percent ([[ADR-0013 Focus and pressed state layer 10 percent]]); ring 3 dp `secondary`, offset 2 dp ([[Focus Ring]]) |
| Pressed | State layer | 10 percent |
| Dragged | State layer; pointer captured | 16 percent ([[State Layers]]) |
| Collapsed | First pane at size 0 and out of the focus order and the accessibility tree; grip stays | `value` equals the minimum |
| Disabled | Not applicable: a splitter that must not resize is not a splitter; use a divider | not applicable |

## Tokens used

| Part | Role or token |
|---|---|
| Grip | `outline` (non-text contrast at least 3:1 against both pane backgrounds, AC-SPL-12) |
| Handle background | transparent |
| State layer | `on_surface` ([[State Layers]]) |
| Focus ring | `secondary`, 3 dp, offset 2 dp ([[Focus Ring]]) |
| Shape | grip radius 2 dp ([[Shape]]) |
| Spacing | none: the handle is the gap between the panes |

## Sizing and density

The splitter has no density-dependent size: a hit area is a target, and targets are the same at every density ([[Spacing and Density]]).

| Measure | default | compact | dense | touch context |
|---|---|---|---|---|
| Handle (hit area) along the split axis | 24 dp | 24 dp | 24 dp | 48 dp |
| Handle along the cross axis | the splitter's full length | same | same | same |
| Grip | 4 by 48 dp | 4 by 48 dp | 4 by 48 dp | 4 by 48 dp |
| Arrow step | 5 percent of the room both panes share | same | same | same |
| Default minimum pane size | 120 dp | 120 dp | 120 dp | 120 dp |

The handle is as large as its hit area, so a 24 dp handle costs 24 dp of layout between the panes. tess-ui uses 16 dp, which fails AC-DEN-7. The 120 dp default minimum equals the `Dock` zone minimum (`MIN_ZONE`) and keeps a pane header and a few characters visible; an author may set 0 on a collapsible pane.

## Layout and overflow

- The room both panes share is the splitter's length along the split axis minus the handle. `Position` (0 to 1) is the first pane's share of that room, two-way.
- A pane is never smaller than its minimum (`Min_First`, `Min_Second`, in dp). When the splitter is shorter than `Min_First` + handle + `Min_Second` the splitter's own minimum applies, which the window minimum or the parent pane enforces ([[Window]]); the panes never overlap and never paint outside their bounds (panes clip their children).
- A window resize keeps the proportion (`Position`) and then clamps to the minimums.
- A pane scrolls its own content by the scrollbar rule ([[ADR-0003 Scrollbar rule]]); the handle has no scrollbar.
- The grip is centred on the cross axis; on a splitter shorter than 48 dp the grip is clipped by the handle, not drawn outside it.

## Behaviour

- Pointer: press on the handle captures the pointer; the first pane's edge follows the pointer so that the handle's middle is under it, clamped to the minimums, updating every frame (live resize, no ghost line). The pointer capture continues outside the handle. Release ends it. Hovering shows the `col_resize` or `row_resize` cursor. Double click toggles collapse when `Collapsible` (closes the first pane, a second double click reopens it at the previous position).
- Keyboard (WAI-ARIA APG window splitter, verified): the handle is a Tab stop.

| Key | Action |
|---|---|
| Left Arrow, Right Arrow | side by side: move the handle left or right by the step |
| Up Arrow, Down Arrow | stacked: move the handle up or down by the step |
| Enter | if the first pane is not collapsed, collapse it; if it is collapsed, restore the previous position (only when `Collapsible`) |
| Home | move to the position that gives the first pane its smallest allowed size (the minimum; 0 on a collapsible splitter) |
| End | move to the position that gives the first pane its largest allowed size (the second pane at its minimum) |
| F6 | cycle focus through window panes (APG optional; owned by [[Window]], not by the splitter) |

- Assistive technology can increment, decrement and set the value.
- Touch: drag the handle; the hit area is 48 dp in a touch context.
- Per [[ADR-0014 Window resize border and splitter alternative]] a splitter offers three ways to resize: drag, double click to collapse and restore, and a keyboard path (arrow keys, Enter to collapse and restore, Home and End). The keyboard path is required (WCAG 2.2 SC 2.1.1) and, with the double-click collapse, is the single-pointer alternative to dragging (WCAG 2.2 SC 2.5.7). A splitter without the keyboard path fails AC-SPL-15.

## Tooltip and overlay behaviour

The handle shows no tooltip by default; the grip is self-describing and the accessible name carries the purpose. A project may add a tooltip on the handle only (never on a pane): [[ADR-0004 Tooltip rule]]. The splitter opens no overlay. While a drag is in progress no tooltip shows (a press removes it).

## Motion

- Dragging and arrow keys move the handle without easing: the position changes in the frame of the input.
- Collapse and restore may animate the first pane's size over `medium2` (300 ms) with `emphasized` easing from [[Motion]] #needs-verification (a design choice; none exists in code, where collapse is instant). With reduced motion on the change is instant.

## Accessibility

- Role: `separator` (a focusable separator is a widget in ARIA 1.1; the APG window splitter uses it). The engine has the role `separator` since 0.5.6, exposed as a splitter that AT-SPI and UIA read as a separator (`tre:docs/reference/node.md`). tess-ui uses the role `slider` instead (see Status in code).
- Name: `Label`, default "Resize panes"; a project gives a name that says what resizes (for example "Resize the sidebar"). If the first pane has a visible label, the label names the handle.
- Value: `value` is the first pane's share (0 to 1), `value_min` 0 (the first pane at its minimum), `value_max` 1 (the first pane at its maximum), `value_step` 0.05; the APG states aria-valuenow, aria-valuemin and aria-valuemax and `aria-controls` referring to the first pane; the engine has no controls relation #needs-verification.
- Keys: as in Behaviour; no key is captured while the handle is not focused.
- Announcements: a change of value is announced as the new value by the AT from the value update; no live region. A collapse announces the new value.
- Contrast: grip at least 3:1 (WCAG 2.2 SC 1.4.11) against `surface` and the pane backgrounds; focus ring `secondary` at least 3:1.
- Target size: 24 by 24 dp at least (WCAG 2.2 SC 2.5.8), 48 in a touch context.

## Dark and light

All colours are roles and follow the scheme. The grip `outline` is a mid-tone role: its contrast with the pane backgrounds is checked in both schemes (AC-SPL-12).

## Defaults

| Setting | Default |
|---|---|
| Orientation | side by side |
| Position | 0.5 |
| Handle | 24 dp, grip 4 by 48 dp |
| Minimum pane size | 120 dp |
| Collapsible | false |
| Label | Resize panes |
| Arrow step | 5 percent |

## Acceptance criteria

- [ ] AC-SPL-1 (geometry check): the handle's hit area, read from the engine hit test, is at least 24 dp along the split axis (48 dp in a touch context) and spans the whole splitter on the cross axis; the grip is 4 by 48 dp, radius 2 dp, centred on the handle within 0.5 dp. Pass at default, compact and dense, scale 1.0 and 2.0.
- [ ] AC-SPL-2 (scripted input): Tab focuses the handle; in a side-by-side splitter Right Arrow increases `Position` by 0.05 and Left Arrow decreases it by 0.05, Up and Down do nothing; in a stacked splitter Down and Up do, Left and Right do not. Pass: `Position` after each key equals the expected value to 6 decimals, clamped to the minimums.
- [ ] AC-SPL-3 (scripted input): Home sets the first pane to its minimum size (0 when collapsible), End sets it to the largest allowed size (the second pane at its minimum); the value is `value_min` and `value_max` respectively. Pass: pane sizes in dp equal the minimums.
- [ ] AC-SPL-4 (scripted input): on a `Collapsible` splitter Enter on the focused handle collapses the first pane (size 0), a second Enter restores the position held before the collapse (to 6 decimals), including when `Min_First` is greater than 0. Pass: positions before, after the first and after the second Enter.
- [ ] AC-SPL-5 (scripted input): a double click on the handle of a `Collapsible` splitter toggles collapse as Enter does; two clicks 500 ms apart do not. A non-collapsible splitter ignores Enter and double click. Pass: positions and pane sizes.
- [ ] AC-SPL-6 (geometry check): after dragging, Home, End and a window resize, the first pane is at least `Min_First` and the second at least `Min_Second` (default 120 dp each, 0 for a collapsed pane); panes do not overlap; no pane content paints outside the pane. Pass: pane rectangles in dp, over the three actions.
- [ ] AC-SPL-7 (scripted input): a press on the handle then moves outside the handle (to 300 dp beyond it) keep resizing (pointer captured); the handle's middle is under the pointer, clamped; release ends the drag; a `pointer_cancel` ends it and leaves the position as it was. Pass: `Position` after each of three runs.
- [ ] AC-SPL-8 (pixel check): handle state layers read `on_surface` at 8 percent hover, 10 percent focus, 10 percent pressed and 16 percent dragged (within 2 channel values of the blend); a keyboard-focused handle draws the 3 dp ring in `secondary` at 2 dp offset; a pointer press draws no ring. Pass in light and dark.
- [ ] AC-SPL-9 (token test): the pointer cursor over the handle is `col_resize` (side by side) or `row_resize` (stacked); the grip fill is role `outline`; no colour literal in the splitter builder. Pass: property equality and zero literals.
- [ ] AC-SPL-10 (AT tree assertion): the handle node has role `separator` and a name equal to `Label` (default "Resize panes"); `value` equals `Position`, `value_min` 0, `value_max` 1, `value_step` 0.05; `value` updates in the frame of each change. Increment, decrement and set_value actions change `Position` by 0.05, minus 0.05 and to the set value, clamped. Pass: property equality and action results.
- [ ] AC-SPL-11 (scripted input): `Position`, bound to a signal, is written by user moves (drag, keys, AT actions) and not by layout or window resizes; `on_change` hears each user move once and no programmatic set. Pass: write counts over a 5-step run.
- [ ] AC-SPL-12 (contrast script): grip `outline` against `surface`, `surface_container` and every pane background role used in the project is at least 3:1 in light and dark; focus ring `secondary` against the handle's background is at least 3:1. Pass: all pairs.
- [ ] AC-SPL-13 (scripted input): while the first pane is collapsed its descendants are not focusable (Tab skips them) and are absent from the accessibility tree; after restore they are again. Pass: Tab order and tree contents.
- [ ] AC-SPL-14 (review): every drag-only function of the splitter has a single-pointer alternative without dragging (collapse by double click, the keyboard path), and every pointer function has a keyboard path; the reviewer records both ([[ADR-0014 Window resize border and splitter alternative]]). Pass: reviewer sign-off.
- [ ] AC-SPL-15 (scripted input): the keyboard path is present and complete on every splitter ([[ADR-0014 Window resize border and splitter alternative]]): the handle is a Tab stop; arrow keys on the split axis, Home and End move it; on a `Collapsible` splitter Enter collapses and restores (as AC-SPL-2 to AC-SPL-4 check). Pass: each of the four key groups changes the position as specified; a splitter where any group has no effect fails.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/widgets/containment.py` (`splitter()`, `HANDLE_SPAN` 16, `HANDLE_SIZE` (4, 48), `SPLIT_STEP` 0.05), `tess-ui:src/tess_ui/spec/lower.py` (`_split`), `tess-ui:src/tess_ui/composed.py` (`_wire_splitters`), `tess-ui:src/tess_ui/spec/builtin_widgets.py` (`Splitter`), `tess-ui:docs/components/splitter.md`, tests `tess-ui:tests/test_splitter.py`, `tess-ui:tests/test_carousel_splitter.py` | Partly meets. Meets: arrow keys by 5 percent on the split axis, Home and End, pointer capture and live drag, resize cursors, a Tab stop, `Min_First` and `Min_Second` in the view version (AC-SPL-2, AC-SPL-3 for the view version, AC-SPL-7, AC-SPL-9), the 4 by 48 grip, screen-reader increment, decrement and set (as `slider`). Fails AC-SPL-1: the handle is 16 dp, not 24. Fails AC-SPL-4 and AC-SPL-15: Enter does nothing; collapse is a double click only (APG requires Enter, and [[ADR-0014 Window resize border and splitter alternative]] makes the keyboard path required, so this is a finding). AC-SPL-10 fails: the role is `slider`, not `separator`. AC-SPL-6 and AC-SPL-3 fail in the Python function `splitter()`, which has no minimums, so Home sets the first pane to 0 and End to 1 and a pane can vanish; the default minimum is 0 in the view version too. AC-SPL-4 also fails on a reading of `_wire_splitters`: with `Min_First` greater than 0 the collapse call clamps to the minimum, the position stays above 0, and the second double click collapses again instead of restoring [INFERENCE from code, not run]. AC-SPL-8 (layer values and ring), AC-SPL-12 (contrast), AC-SPL-13 (collapsed pane focus) are not run and not found in the tests. Not built: a fixed (two-position) splitter, `aria-controls` |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` | Not applicable: no splitter block or module in the shell; panes in shell modules are fixed by their layout |
| tre | `tre:docs/reference/node.md` (`separator` role, `capture_pointer`, cursor), `tre:docs/guide/events-and-input.md` | Primitives exist: pointer capture, cursors, roles `slider` and `separator` (0.5.6), value ranges and the a11y actions. The engine has no splitter node |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has drag handles in canonical layouts, no splitter) | desktop panes are resized by the user | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Handle hit area 24 dp (touch 48 dp) | desktop pointer minimum per WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard operation per the APG window splitter (arrows, Enter, Home, End), required not optional | MD3 describes pointer and touch dragging only; the keyboard path is the dragging alternative | [[ADR-0014 Window resize border and splitter alternative]] |
| Focus and pressed layers 10 percent, dragged 16 percent on the handle | Material Web latest state tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |

## Sources

- WAI-ARIA Authoring Practices window splitter pattern (verified 2026-11-21: role `separator`, aria-valuenow, aria-valuemin, aria-valuemax, aria-controls on the primary pane, label by aria-labelledby or aria-label; keys Left, Right, Up, Down, Enter to collapse and restore, optional Home, End, F6): https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/
- Compose Material 3 `DragHandleSizes` (size, pressedSize, draggedSize exist; the dp values were not readable from the fetched page): https://developer.android.com/reference/kotlin/androidx/compose/material3/DragHandleSizes
- WCAG 2.2 SC 2.5.7 Dragging Movements (verified): https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- State layer values: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-state.scss
- Engine roles and capture: `tre:docs/reference/node.md`, `tre:docs/guide/accessibility.md`, `tre:docs/guide/events-and-input.md`.
- tess-ui: `tess-ui:docs/components/splitter.md`.
- Not verified: the MD3 drag handle dp values (4 by 48 dp is the value tess-ui states as MD3's) #needs-verification; the 120 dp default minimum is a Tesserae choice; the collapse animation is a design choice #needs-verification.
