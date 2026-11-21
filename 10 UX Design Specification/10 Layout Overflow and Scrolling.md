---
title: 10 Layout Overflow and Scrolling
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, layout, overflow, scrolling, text]
related: ["[[Spacing and Density]]", "[[07 Spacing and Density Rules]]", "[[Focus Ring]]", "[[Typography]]", "[[Scrollbar and Scroll Container]]", "[[Text Field]]", "[[Tree]]", "[[Tree Node]]", "[[List]]", "[[List Item]]", "[[Form Row]]", "[[Panel and Surface]]", "[[Tooltip]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[Deviations from MD3]]"]
depends_on: ["[[Spacing and Density]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]"]
---

# 10 Layout Overflow and Scrolling

> [!info] Summary
> Principles for window size classes, panes, overflow, text truncation and wrapping, vertical centring and scrolling. The scrollbar itself (geometry, colours, keys) is in [[Scrollbar and Scroll Container]]; the text field details are in [[Text Field]]. This chapter holds the rules every container obeys.

Evidence: [[Owner Feedback 2026-11-20]] F5 (directory text neither wraps nor has an ellipsis and runs past the container), F6 (no horizontal scroll bars though panels have content past the frame), F7 (text in fields top aligned).

## Window size classes and panes

Classes and boundaries are in [[Spacing and Density]] (width: compact below 600 dp, medium 600 to 839, expanded 840 to 1199, large 1200 to 1599, extra-large 1600 and up; height: below 480, 480 to 899, 900 and up). A boundary value belongs to the larger class.

| Width class | Panes shown | Rule |
|---|---|---|
| compact | 1 | one pane at a time; navigation between panes by an explicit control (back, tabs or a drawer); no side-by-side panes |
| medium | 1 or 2 | two panes when each is at least 320 dp wide, else one |
| expanded | 2 | list and detail side by side; the navigation region may collapse to a rail |
| large | 2 or 3 | navigation, list and detail, each pane at least 320 dp wide |
| extra-large | 3 | extra width goes to the content pane, up to a content maximum of 840 dp for reading text; panes beyond keep their width |

Rules:
- The class is computed from the window width in dp and re-evaluated on each resize; a pane that no longer fits collapses at the class boundary, never by clipping.
- The minimum window size is the smallest size at which every pane that is shown has its minimum width (320 dp) and at which no content is unreachable (AC-LAY-1, AC-LAY-8).
- Panes are separated by a gap of a spacing step or a divider; a pane never overlaps another.
- The named MD3 canonical layouts (list-detail, supporting pane, feed) are the model for the pane counts #needs-verification: m3.material.io is a JavaScript app that tools cannot read. The widths and counts in the table are Tesserae design choices, tested by AC-LAY-9.

## The overflow rule

Content never paints outside its container. Each container takes one of four behaviours for each axis, and states it in its component note:

| Behaviour | Use | Result |
|---|---|---|
| Clip | decoration, image covers, ripples and state layers | content beyond the container's bounds is not painted |
| Wrap | multi-line text | text breaks at word boundaries so no line is wider than the container |
| Ellipsis | single-line text | the end of the text is replaced by `…` |
| Scroll | any content that can exceed the container and must be reached | the container scrolls on the overflowing axis and shows a scrollbar there ([[ADR-0003 Scrollbar rule]]) |

Hard rules:
1. A child's painted bounds lie inside the clipping bounds of its nearest clipping ancestor, or the ancestor is a scroll container and the child lies inside its scrollable extent (AC-LAY-1).
2. Text that can exceed its box wraps, truncates with an ellipsis, or sits in a scroll container. Silent clipping of text without an ellipsis is a defect (F5).
3. Content that is clipped and cannot be scrolled to is a defect (F6): every focusable and every readable element of a scroll container can be reached by scrolling and by keyboard (AC-LAY-8, AC-LAY-14).
4. Overlays (tooltips, popups, menus) are clipped to the window, not to the control or the scroll container that spawned them; they never extend past the window and never draw without an opaque container ([[12 Overlays]], [[ADR-0004 Tooltip rule]]).
5. The focus ring is not clipped by a scroll container ([[Focus Ring]], AC-FOC-5).
6. A parent whose size depends on its content has a maximum size or scrolls; no layout depends on text that is always short.

## Single-line text

- Truncation: the end is replaced by `…` (U+2026) so that the visible text plus the ellipsis fits the available width. The ellipsis follows the last whole glyph, never half a glyph.
- Paths and file names: middle truncation is allowed, the head of the path is shortened and the last path segment (the file or directory name) stays visible: `…/projects/shell/config`. A path never truncates at the end alone when the last segment is cut off.
- The full value is shown on the control that carries the text by a tooltip when the text is truncated, never on the row or group ([[ADR-0004 Tooltip rule]], [[Tooltip]]). The text is also available by selection and copy where the element is selectable. A tooltip is not the only way to read the information ([[14 Accessibility Basics]]).
- A text input shows its value truncated with an ellipsis only while not focused; a focused text input scrolls the caret into view instead ([[Text Field]]).
- A label never wraps unless its component note says it wraps; a label that cannot fit truncates.

## Wrapping

- Multi-line text (descriptions, helper text, dialog body) wraps at word boundaries; line height comes from the [[Typography]] role.
- A word longer than the container breaks at a glyph boundary so that it does not exceed the container.
- A multi-line block has a maximum number of lines where its note states one; beyond it the last line ends with `…`; otherwise the block grows and its container scrolls.
- Wrapping text has a minimum container width of 120 dp; below it the container scrolls horizontally or the layout changes class (AC-LAY-10).
- Paragraph measure for reading text: at most 840 dp wide.

## Vertical centring of single-line text

A single-line text in a control (text field, button, switch row, list row, tree row, menu item) is centred vertically on the control's content box. Centring is by construction, not by tuned padding:

- the text line box has the line height of its [[Typography]] role (`body-medium` is 20 dp);
- the line box sits in the control so that the space above and below differs by at most 1 px;
- padding above and below is `(control height - line height) / 2` at each density: 10, 6 and 4 dp for 40, 32 and 28 dp controls with a 20 dp line, and 2 dp for a 24 dp row. These are derived values, not tokens: a project does not store them, it centres.
- a project whose engine has no vertical-alignment property (tre `text_input`) computes the padding from the control height; it does not use top-aligned text with padding of the dense value.

Left alignment of text in fields is correct and stays; only the vertical axis changes (F7). Multi-line fields top-align the first line with the field's vertical padding.

## Minimum widths

- In a flex row or column, a child that holds text has minimum width 0 (`Min_Width 0` in tess-ui and the engine), so the child may shrink below the width of its text and the ellipsis can work. A flex child with an automatic minimum width equal to its content (the default in many layouts) cannot truncate and pushes its sibling out of the container: a defect (F5).
- An icon, a chevron, a switch and a button have a fixed minimum width equal to their hit area ([[Spacing and Density]]); the label next to them shrinks.
- A pane has its minimum width (320 dp for list and detail panes); a window has the minimum size from the pane rule.
- Fixed widths are used for icon-size elements; flexible text takes the rest.

## Scrolling

Details live in [[Scrollbar and Scroll Container]] and [[ADR-0003 Scrollbar rule]]. The layout rules:

- Horizontal scrolling: a container whose content is wider than its viewport and that does not wrap or truncate that content scrolls horizontally and shows a horizontal scrollbar. Trees and file lists in side panels scroll horizontally when a row is wider than the panel, unless the row text truncates with an ellipsis (F6).
- Both axes: a container whose content overflows on both axes scrolls on both and shows two thumbs that do not overlap in the corner (AC-LAY-7). A single-axis scroll container is nested for two axes only where the engine has no two-axis container (tre scroll view is one axis; tess-ui plans a two-way scroll view); the visible result must equal AC-LAY-7.
- A scrollbar is visible when content overflows on that axis and absent when it does not; no auto-hide by default on desktop.
- Keyboard scrolling for any focusable scroll container: arrow keys 40 dp, Page Up and Page Down one viewport minus 10 percent, Home and End; the wheel scrolls 20 dp per notch as the engine default (`tre:crates/engine-py/src/listeners.rs`).
- Scroll chaining: a nested scroll container at its end passes the wheel to its parent only after the wheel stops for 200 ms, a Tesserae design choice #needs-verification as a default.
- A scroll position is restored when a container is rebuilt with the same content.

## Virtualised lists

A virtualised list or tree realises only the rows in view plus a buffer of one viewport at each end.
- The scrollbar thumb length and position reflect the total extent, not the realised rows; a thumb is draggable.
- Arrow Up and Down move focus by one row and scroll it into view; Page Up and Page Down move by one viewport minus 10 percent; Home and End move to the first and last row; the focused row stays inside the viewport with its ring ([[Focus Ring]]).
- Row height is uniform at a density level ([[Spacing and Density]]); variable rows are measured before they are placed.
- Screen readers get the row count and position (set size and position in set) for rows not realised ([[14 Accessibility Basics]]).
- The tre `virtual_list` has a draggable vertical thumb but handles no Home, End, Page or arrow keys, and `scroll_into_view` skips it (`tre:crates/engine-core/src/tree/scroll.rs`, `dispatch.rs`); this fails AC-LAY-11.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/composed.py`, `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_Stylesheet.tdl` | partly meets: the config app gives tree labels `Min_Width 0` with ellipsis (meets AC-LAY-6 for trees); ScrollView scrolls one axis, two-axis is planned (`feat/scrollview-two-way`), so AC-LAY-7 fails; text input shows an ellipsis only while unfocused; the single-line TextInput centres by 7 px padding in 32 px (meets AC-LAY-2 at compact by padding, not by construction); no AC-LAY-1 layout test is known |
| tess-shell | `tess-shell:src/tess_shell/shipped/` | partly meets: wheel scrolling only; no scrollbar and no scroll affordance on long lists (fails AC-LAY-7, AC-LAY-8 for long lists) |
| tre | `tre:crates/engine-core/src/tree/scroll.rs` | partly meets: `scroll_view` one axis (nest for two), clips children, thumb 4 px, 32 px minimum, no auto-hide; `virtual_list` without keys (fails AC-LAY-11); text input has no vertical-align property |

Facts are from [[Existing Tokens]] and [[Gaps and Contradictions]].

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Scrollbars always visible on desktop when content overflows, both axes | MD3 treats scrollbars as a platform concern; the owner reported unreachable content | [[ADR-0003 Scrollbar rule]] |
| Middle ellipsis allowed for paths | the end of a path is the part that identifies it | [[ADR-0004 Tooltip rule]] |
| Tooltip with full value on truncated text | desktop pointer affordance | [[ADR-0004 Tooltip rule]] |
| Single-line field height 40, 32, 28 dp with vertical centring (MD3 56 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Acceptance criteria

- [ ] AC-LAY-1 (geometry check): for every node of a rendered tree at widths 320, 480, 600, 840 and 1200 dp and at 200 percent text scale, the painted bounds lie inside the bounds of the nearest clipping ancestor (or inside the scrollable extent of a scroll container); overlays are excluded and checked against the window. Pass: zero violating nodes.
- [ ] AC-LAY-2 (geometry check): for a single-line Text Field, Button, Switch row, List row and Tree row at each density level, the text line box top margin and bottom margin inside the control differ by at most 1 px. Pass for control heights 40, 32, 28 and rows 40, 32, 24.
- [ ] AC-LAY-3 (pixel check): a label whose text is 300 dp wide in a 100 dp wide container shows no ink right of the container's inner right edge, and its last visible glyph is `…`; the ellipsis occupies the end, not the start.
- [ ] AC-LAY-4 (pixel check): a path of 12 segments in a container too narrow for it shows `…` inside the path (not at the end) and the last segment fully, in a control that allows middle truncation.
- [ ] AC-LAY-5 (scripted input): hovering for 500 ms the truncated label shows a tooltip carrying the full text, whose trigger is the label node (not its row or the group); the tooltip is absent when the text fits.
- [ ] AC-LAY-6 (geometry check): in a flex row of 200 dp width with a text child of 600 dp natural width, an icon of 24 dp and a button of 40 dp, the text child's width is at most 200 minus 24 minus 40 minus gaps; the icon and the button stay at full size.
- [ ] AC-LAY-7 (geometry check): a container with content 2 times its viewport on both axes shows a vertical and a horizontal thumb; the two thumb rectangles do not intersect; neither thumb extends into the corner square (thumb thickness plus margin) where the two bars meet.
- [ ] AC-LAY-8 (scripted input): in a container whose content is 1000 dp wide in a 400 dp viewport, the horizontal scroll offset can reach 600 dp (content minus viewport) by wheel, drag and End key; the last pixel of the content becomes visible.
- [ ] AC-LAY-9 (geometry check): at widths 599, 600, 839, 840, 1199, 1200, 1599 and 1600 dp the window reports the class compact, medium, medium, expanded, expanded, large, large, extra-large, the number of panes shown lies in the range the pane table gives for that class (1; 1 to 2; 2; 2 to 3; 3), and no shown pane is narrower than 320 dp.
- [ ] AC-LAY-10 (geometry check): wrapping text in a container wider than 120 dp has no line wider than the container; a 400 dp unbroken word in a 200 dp container breaks at a glyph boundary.
- [ ] AC-LAY-11 (scripted input): in a virtualised list of 10000 rows, End moves focus to the last row and scrolls it into view with its ring visible, Home to the first, Page Down moves by the viewport height minus 10 percent, and the thumb position matches the focused row index within 1 percent of the extent.
- [ ] AC-LAY-12 (pixel check): at 150, 200 and 250 dp container widths, an editable text field with a 600 dp value shows its value truncated with `…` when unfocused, and scrolls the caret into view when focused; no text ink lies outside the field's content box.
- [ ] AC-LAY-13 (AT tree assertion): rows of a virtualised list expose set size and position; a truncated label's accessible name is the full text.
- [ ] AC-LAY-14 (scripted input): Tab to a control outside the viewport of a scroll container scrolls it so that the control and its ring (5 dp beyond the border box) are fully visible.
- [ ] AC-LAY-15 (review): every component note states its overflow behaviour per axis (clip, wrap, ellipsis, scroll). Pass: a reviewer finds no component note without it.

## Sources

- Window size classes (verified): https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes.
- Engine facts: `tre:crates/engine-core/src/tree/scroll.rs` (KEY_SCROLL_LINE 40), `tre:crates/engine-py/src/listeners.rs` (WHEEL_LINE_PX 20), [[Existing Tokens]].
- MD3 canonical layouts: https://m3.material.io/foundations/layout/canonical-layouts/overview (not readable by tools #needs-verification).
- Not verified: scroll chaining delay of 200 ms (Tesserae design choice) #needs-verification; 840 dp reading width and 320 dp pane minimum (Tesserae design choices).
