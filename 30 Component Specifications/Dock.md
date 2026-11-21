---
title: Dock
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, pattern, dock, docking, keyboard, drag-and-drop]
related: ["[[Dock Panel]]", "[[Splitter]]", "[[Tabs]]", "[[Window]]", "[[Panel and Surface#Variants|Melded Panel]]", "[[Panel and Surface]]", "[[Drag and Drop]]", "[[Navigation Rail]]", "[[Menu]]", "[[Tooltip]]", "[[Scrim]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[Splitter]]"]
---

# Dock

> [!info] Summary
> A Dock arranges panels in zones (left, right, top, bottom, center) around the content of a window; each zone shows its panels as tabs, one at a time, and the user resizes zones with handles and moves panels between zones. MD3 has no dock; its nearest patterns are the [navigation rail](https://m3.material.io/components/navigation-rail/overview) and the canonical pane layouts, and the tab strip follows the MD3 secondary tabs. The word dock also names a different thing in tess-shell (a melded panel with a peek on a screen edge): that realisation is specified in [[Panel and Surface#Variants|Melded Panel]] and its requirements are listed under Behaviour. Source of truth in code: see Status in code.

## Purpose

A tool window (editor, inspector, file tree, console) holds many panels and the user decides where each lives. A dock gives each panel a zone, lets several panels share a zone as tabs, and keeps the arrangement through sessions.

## When to use and not

- Use when: a desktop tool has three or more long-lived panels that the user rearranges (an IDE-like layout).
- Do not use when: two panes only ([[Splitter]]); app destinations that replace each other ([[Navigation Rail]], [[Routed View]]); a panel that floats over content ([[Popup]], [[Dialog]]); fixed layout panes ([[Panel and Surface]]).
- A window has one Dock. Nested docks are not supported.

## Anatomy

1. Zone: left, right, top, bottom or center. A left or right zone has a width, a top or bottom zone a height; the center zone fills what is left.
2. Tab strip: one tab per panel of the zone, over the shown panel ([[Dock Panel]]).
3. Shown panel: the panel of the selected tab, one at a time.
4. Resize handle: between a side or top or bottom zone and the center, 24 dp wide or high, holding a 4 by 48 dp grip; same behaviour as [[Splitter]].
5. Drop highlight: while a panel tab is dragged, the zone under the pointer is highlighted.
6. Splits: a panel may hold halves, each with a strip, handle and own drop bands: [[Dock Panel]].

## Variants

| Variant | Use | Differences |
|---|---|---|
| Panel dock (tess-ui `Dock`) | IDE-like tool windows | Zones, tabs, handles, splits, layout save and restore |
| Edge dock (tess-shell) | A shell panel at a screen edge | A melded Panel with Peek on a Frame; no tabs, no splits ([[Panel and Surface#Variants|Melded Panel]]) |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Zones, strips and handles drawn | zone container `surface`; handle grip `outline` |
| Handle hover, focus, pressed, dragged | State layer over the handle | `on_surface` at 8, 10, 10, 16 percent ([[State Layers]]) |
| Tab dragging | The dragged tab shows the dragged layer; the zone or half under the pointer shows the drop highlight | tab layer 16 percent; highlight `primary` at 16 percent with a 2 dp `primary` outline |
| Empty zone | A zone with no panel takes no room and shows no handle | not applicable |
| Closed panel | Its tab is gone; the panel is kept and can be reopened | not applicable |

## Tokens used

| Part | Role or token |
|---|---|
| Zone and strip container | `surface` |
| Divider under the strip | `surface_variant`, 1 dp ([[Colour Roles]]) |
| Drop highlight | `primary` at 16 percent, outline `primary` 2 dp |
| Handle grip | `outline` |
| Tab tokens | see [[Dock Panel]] |
| Spacing | zone sizes in dp; no padding between a handle and a zone |

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Default zone size, left and right | 240 dp | 240 dp | 240 dp | width when the panel gives none |
| Default zone size, top and bottom | 180 dp | 180 dp | 180 dp | height when the panel gives none |
| Zone minimum | 120 dp | 120 dp | 120 dp | `set_size` clamps |
| Zone maximum | 70 percent of the room | same | same | |
| Handle (hit area) | 24 dp | 24 dp | 24 dp | 48 dp in a touch context |
| Grip | 4 by 48 dp | same | same | |
| Arrow step on a handle | 16 dp | 16 dp | 16 dp | |
| Minimum half of a split | 48 dp | 48 dp | 48 dp | [[Dock Panel]] |
| Drag threshold | 4 dp | 4 dp | 4 dp | a press moving less than this is a click |

Tab and strip heights per density are in [[Dock Panel]].

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| Zone, left or right | min width | - | 120 | 120 | 120 | [[Dock]] Sizing (zone minimum; default width 240) | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Zone, top or bottom | min height | - | 120 | 120 | 120 | [[Dock]] Sizing (zone minimum) | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Zone, top or bottom | height | - | 180 | 180 | 180 | [[Dock]] Sizing and Defaults (default size when the panel gives none) | tess-ui: yes (Dock sizes per side); tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: yes (add_dock_zone size) |
| Half of a split | min width | - | 48 | 48 | 48 | [[Dock]] Sizing, [[Dock Panel]] | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Half of a split | min height | - | 48 | 48 | 48 | [[Dock]] Sizing, [[Dock Panel]] | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Tab strip | height | - | 48 | 40 | 32 | [[Dock Panel]] Sizing (tab height) | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Zone | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Dock]] Tokens used (no padding between a handle and a zone) | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Zone | margin | - | N/A: zones touch each other and the center; the handle is the only space between | N/A: same as default | N/A: same as default | [[Dock]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Zone | gap | `space.0` | 0 | 0 | 0 | [[Dock]] Tokens used (strip and shown panel are stacked directly) | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Handle | min width | - | 24 | 24 | 24 | [[Dock]] Sizing (hit area; 48 in a touch context), [[ADR-0014 Window resize border and splitter alternative]] | tess-ui: no hook; tess-shell: via Peek Size; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Strip divider | border width | - | 1 | 1 | 1 | [[Dock]] Tokens used | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Strip divider | border color | `surface_variant` | `surface_variant` | `surface_variant` | `surface_variant` | [[Dock]] Tokens used, [[Colour Roles]] | tess-ui: via theme role surface_variant; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Drop highlight | border width | - | 2 | 2 | 2 | [[Dock]] Tokens used | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Drop highlight | border color | `primary` | `primary` | `primary` | `primary` | [[Dock]] Tokens used, [[Colour Roles]] | tess-ui: via theme role primary; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Zone | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]]; the note names no rounding | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Grip (4 wide, 48 long) | corner radius | `shape.full` | 2 | 2 | 2 | [[Dock]] AC-DCK-2, [[Shape]] | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |
| Zone | font | - | N/A: the dock draws no text; tab labels belong to the dock panel | N/A: same as default | N/A: same as default | [[Dock Panel]] | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Zone | icon size | - | N/A: the dock draws no icon; the close glyph belongs to the dock panel | N/A: same as default | N/A: same as default | [[Dock Panel]] | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Zone | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: no hook; tess-shell: n/a: the shell dock is a melded Panel with Peek and has no zones or tabs; tre: n/a: tre draws no dock chrome and zones are project nodes |

## Layout and overflow

- Zones lie around the center; a side with no zone is an error; a side zone with no panel is hidden with its handle.
- A zone clips its content (the shown panel); the panel scrolls itself ([[ADR-0003 Scrollbar rule]]).
- The sum of zone sizes never leaves the center zone below its minimum: zone maxima (70 percent of the room each) and the window minimum ([[Window]]) keep the center at its minimum; when the window shrinks, side zones shrink toward 120 dp before the center does #needs-verification (code clamps each zone to 70 percent of the room; the combined case is not documented).
- A layout of the dock (zone of each panel, shown tab per zone, zone sizes, split sizes, halves) is plain data and is saved and restored by the application.

## Behaviour

- Pointer: click a tab to show its panel; drag a tab past 4 dp to move the panel to another zone; the zone under the pointer is highlighted; releasing over no zone leaves the panel where it was. Drag a handle to resize a zone (pointer captured, live, clamped to 120 dp and 70 percent of the room).
- Keyboard: a tab strip is one Tab stop (the shown tab); Left and Right Arrow move to the previous or next tab and show its panel, wrapping at the ends; Home and End go to the first and last tab; Enter shows the focused tab's panel; the Menu key or Shift+F10 on a tab opens its menu with "Move to ..." for each zone and each half, which moves the panel without dragging and keeps focus on the moved tab. A handle is a Tab stop: arrows move it by 16 dp, Home goes to the minimum, End to the maximum (as [[Splitter]]).
- Touch: tabs are 48 dp high, handles 48 dp in a touch context; a long press on a tab opens its menu #needs-verification (design choice).
- Drag cancel: Escape during a tab drag cancels it; the panel returns to where it was and no drop happens.
- Edge dock (tess-shell): the dock rests as a thin tab of `Size` px (default 24) on the screen edge and opens by `Trigger` (HOVER after 150 ms, CLICK or DRAG) and closes after 300 ms away; the keyboard opens it (a focusable handle named "Expand dock"; today only the Frame's shortcut mode) ([[Panel and Surface#Variants|Melded Panel]]).

## Tooltip and overlay behaviour

- A tab shows a tooltip on the tab only, and only when its title is truncated; an icon-only tab always shows its title ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]).
- A close button shows "Close" as its tooltip.
- The tab menu is a [[Menu]] opened by the secondary press, the Menu key or Shift+F10; it closes on Escape or an outside press and returns focus to the tab.
- The drop highlight is drawn by the dock over the zone, not a [[Scrim]], and it is removed when the drag ends in any way.

## Motion

- Switching tabs, moving a panel and resizing have no animation; the active indicator moves in one frame.
- The drop highlight appears in the frame in which the pointer enters a zone and goes in the frame it leaves ([[Motion]]). With reduced motion on nothing changes.

## Accessibility

- Each zone's strip has role `tablist` named "{Side} panels" (Left panels, Right panels); each tab has role `tab`, the panel's title as its name and `selected` true on the shown tab only; each shown panel has role `tabpanel` named by its tab (the APG tabs pattern).
- Keys: as in Behaviour; the dock never traps focus: Tab leaves a strip to the shown panel and on to the next control.
- Drag and drop has a pointer-free alternative: the tab menu "Move to ...", per WCAG 2.2 SC 2.5.7 Dragging Movements (single-pointer alternative) and SC 2.1.1 (keyboard).
- A zone change is announced: moving a panel announces "{title} moved to {side}" through `Window.announce` (polite) #needs-verification (a design choice; the engine announce has not been heard with a screen reader, [[Accessibility Rules]] AR-29).
- Handles: see [[Splitter]]; the role is `separator`. Per [[ADR-0014 Window resize border and splitter alternative]] a zone handle has the splitter's keyboard path (arrow keys, Home, End), which is required and is the dragging alternative for resizing (SC 2.5.7); a zone has a close button for hiding it.
- Contrast: tab text per [[Dock Panel]]; grip at least 3:1; drop highlight outline `primary` at least 3:1 against the zone container.
- Target sizes: tabs and handles at least 24 dp; close buttons at least 24 by 24 dp.

## Dark and light

All colours are roles; the dock follows the application's scheme and retints when the scheme changes (a Dock made with no `theme=` follows the app theme). The highlight is `primary` in both schemes.

## Defaults

| Setting | Default |
|---|---|
| Zones | those named by the panels; center fills |
| Left and right size | 240 dp; top and bottom 180 dp |
| Zone minimum, maximum | 120 dp, 70 percent of the room |
| Handle, grip | 24 dp, 4 by 48 dp |
| Drag threshold | 4 dp |
| Closed panels | none |
| Layout save | by the application |

## Acceptance criteria

- [ ] AC-DCK-1 (geometry check): a dock with panels in left, right, top, bottom and center zones gives left and right zones 240 dp wide and top and bottom zones 180 dp high when the panels give no size; `set_size` clamps to 120 dp and to 70 percent of the room (a request for 50 or for 99 percent returns 120 or 70 percent). Pass: sizes in dp at scale 1.0 and 2.0.
- [ ] AC-DCK-2 (geometry check): each zone handle's hit area is at least 24 dp across (48 dp in a touch context) and spans the whole zone edge; the grip is 4 by 48 dp, radius 2 dp, centred within 0.5 dp. Pass at default, compact and dense.
- [ ] AC-DCK-3 (scripted input): Tab focuses a zone handle; for a left zone Right Arrow grows it by 16 dp and Left Arrow shrinks it; for a right zone Left Arrow grows it; for a top zone Down grows it; for a bottom zone Up grows it; Home sets the minimum (120 dp), End the maximum (70 percent of the room); the handle's `value`, `value_min` and `value_max` follow. Pass: zone sizes after each key.
- [ ] AC-DCK-4 (scripted input): a press on a handle and a move of 40 dp changes the zone by 40 dp in the growing direction, clamped; the drag continues outside the handle (captured); release ends it. Pass: zone size after each of three runs.
- [ ] AC-DCK-5 (scripted input): a press on a tab and a move of 3 dp is a click (shows the panel, no drag); a move of 4 dp or more starts a drag and does not select the panel on release over the same tab; with the pointer over zone Z the zone shows the drop highlight (pixel: `primary` at 16 percent blend inside, 2 dp `primary` outline at the edge); releasing over Z moves the panel to Z and shows it; releasing over no zone leaves it. Pass: panel side and highlight pixels in each case.
- [ ] AC-DCK-6 (scripted input): Escape during a tab drag cancels it: the panel stays in its zone, no `on_move` call, the highlight is removed within one frame. Pass: side, call count and layer pixels.
- [ ] AC-DCK-7 (scripted input): the Menu key and Shift+F10 on a focused tab open the tab menu with one "Move to {side}" entry per zone other than the current one, and one per half; choosing one moves the panel, shows it and leaves keyboard focus on the moved tab. Pass: menu entries, panel side and focused node.
- [ ] AC-DCK-8 (scripted input): a strip is one Tab stop: only the selected tab is focusable; Left and Right Arrow move to the previous and next tab and select it, wrapping; Home and End select the first and last tab; Enter or Space selects the focused tab. Pass: focused and selected tab ids after each key.
- [ ] AC-DCK-9 (scripted input): `layout()` then `restore()` round-trips: panel zones, shown tab per zone, zone sizes (clamped), split sizes and halves are equal; a title, zone or half the dock does not have is skipped without error; an edit of the view while the app runs keeps the user's arrangement. Pass: `layout()` before equals `layout()` after for the restored dock.
- [ ] AC-DCK-10 (AT tree assertion): each zone strip has role `tablist` named "{Side} panels"; each tab role `tab` with its title as name and `selected` true on the shown tab only; each shown panel role `tabpanel` named by its title; a hidden panel is not in the tree; handles have role `separator` and a name that says "Resize the {side} panels". Pass: property equality for a dock with 5 zones.
- [ ] AC-DCK-11 (token test): zone, strip and tab colours are role references (`surface`, `on_surface`, `on_surface_variant`, `primary`, `surface_variant`, `outline`); a scheme change retints the dock in place within one frame. Pass: zero colour literals; resolved values equal the scheme before and after `set_dark`.
- [ ] AC-DCK-12 (scripted input): a zone with no panel is hidden together with its handle; removing the last panel of a split half collapses the half and its neighbour takes the room back (one frame); re-adding a panel to the empty side brings the zone back at its last size. Pass: zone visibility and sizes.
- [ ] AC-DCK-13 (scripted input): a window shrinks from 1100 to 480 dp wide with left and right zones at 240 dp: the center zone stays at least its minimum (120 dp) and no zone overlaps another or paints outside the window. Pass: zone rectangles at each of five widths #needs-verification (the combined-zone rule is a Tesserae choice).
- [ ] AC-DCK-14 (scripted input): the edge dock of tess-shell opens by the keyboard: a key route reaches the peek handle (focusable, named "Expand dock") and Enter opens it; HOVER opens after 150 ms and closes after 300 ms away; the resting tab is at least 24 dp on its short side. Pass: open state after each input. Hand check on KWin (not automated) for the focusable handle.
- [ ] AC-DCK-15 (review): the application offers no layout feature that only drag can do: every move has the tab menu, every size has the handle keys, every close has the close button; reviewer records each ([[ADR-0014 Window resize border and splitter alternative]]). Pass: sign-off.
- [ ] AC-DCK-16 (scripted input): every zone handle meets the keyboard path of [[Splitter]] (AC-SPL-15): Tab focuses it, and the arrow keys on its axis, Home and End resize it as AC-DCK-3 states, with no resize function reachable by drag alone ([[ADR-0014 Window resize border and splitter alternative]]). Pass: zone size after each key; a handle without the path fails.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/docking.py` (`Dock`, `TAB_HEIGHT` 48, `DRAG_THRESHOLD` 4, `HALF_EDGE` 0.25), `tess-ui:src/tess_ui/dockhost.py` (`DockHost`, `HANDLE_SPAN` 16, `MIN_ZONE` 120, `MAX_SHARE` 0.7, `STEP` 16, `DEFAULT_SIZE`), `tess-ui:src/tess_ui/spec/dock.py`, `tess-ui:docs/components/dock.md`, `tess-ui:docs/guide/docking.md`, tests `test_docking.py`, `test_dock_view.py`, `test_dock_halves.py`, `test_dock_close.py`, `test_window_dock_example.py` | Partly meets. Meets (per code and docs, not all run): zone defaults and clamps (AC-DCK-1), drag threshold and drop highlight (AC-DCK-5), the "Move to ..." menu from the Menu key and Shift+F10 (AC-DCK-7), one Tab stop strip with arrows and wrap (`tab.node.set(selected=on, focusable=entry.node == stop)`), layout and restore (AC-DCK-9), tablist, tab and tabpanel roles (AC-DCK-10), arrow, Home and End on handles, close, reopen, halves with collapse. Fails AC-DCK-2: handle 16 dp, not 24. Fails AC-DCK-6: no Escape handling in a drag. Fails AC-DCK-8 in part: Home and End on the tab strip do nothing. Fails AC-DCK-5 in the highlight value: `HIGHLIGHT_ALPHA` 0x1F is 12 percent, quoted as the MD3 pressed or dragged overlay, which is 16 percent dragged and 10 percent pressed in the current tokens. Fails AC-DCK-10 in the handle role (`slider`, not `separator`). Not run: AC-DCK-11, AC-DCK-12 (empty zone), AC-DCK-13. Drag and drop of panels is built for tabs moving between zones and onto halves; not built: floating panels, tearing a panel off into a window, maximising a panel, reordering tabs, layouts saved by name, dragging or closing a half's own content, panel identity (panels are found by title) |
| tess-ui (dimensions) | `tess-ui:src/tess_ui/dockhost.py` | Differences in [[#Dimensions and defaults]]: zone handle 16 (`HANDLE_SPAN`), spec 24 (AC-DCK-2, AC-DEN-7). Zone minimum 120 and zone defaults 240 and 180 meet the table. Not settable from the project layer (no hook): `MIN_ZONE` 120, `MIN_SPLIT` 48, `HANDLE_SPAN` 16, `GRIP` 4 by 48, `TAB_HEIGHT` 48, the 1 dp divider and `HIGHLIGHT_OUTLINE` 2 in `dockhost.py` and `docking.py`; only the zone sizes (`sizes`) and theme roles reach the project |
| tess-ui (ADR-0014) | `tess-ui:src/tess_ui/dockhost.py` | AC-DCK-16: arrow, Home and End on zone handles are built (row above), so the required keyboard path is met for resizing; not run [INFERENCE from the row above]. The handle role (`slider`, not `separator`) stays under AC-DCK-10 |
| tess-shell | `tess-shell:src/tess_shell/surfaces/join.py`, `frame.py`, `tess-shell:docs/guide/surfaces.md` (Melded Panels, Peek), `shell-vault:40 Specifications/Surfaces/Frame.md` | Partly meets as the edge dock: a melded Panel with Peek (`Size` 24 default, `Enter_Delay` 150, `Exit_Delay` 300, `Trigger` HOVER, CLICK, DRAG). AC-DCK-14: the handle is part of the painter, not a focusable control named "Expand dock"; the keyboard route is the Frame's shortcut mode (decided 2026-11-10); real KWin behaviour is a hand check, not run. No tabs, no splits and no drag of panels in the shell. Dock is not a surface kind in code |
| tre | `tre:docs/guide/docking.md`, `tre:crates/engine-core/src/dock.rs` | Exists as the mechanism: `add_dock_zone`, `dock_panel`, `set_active_panel`, `start_panel_drag`, `undock_panel`, the `dock_target` and `dock_drop` events, moving without a drag by calling `dock_panel` again. The engine draws no handle and no highlight; those are tess-ui's |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has no dock; nearest are the navigation rail and canonical layouts) | desktop tool windows hold many rearrangeable panels | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tab strip follows the MD3 secondary tab (48 dp) but adds drag, a menu and a roving Tab stop | MD3 tabs are not draggable; desktop users move panels | [[ADR-0002 Desktop density levels and target sizes]] |
| Handle hit area 24 dp, grip 4 by 48 dp | desktop pointer minimum | [[ADR-0002 Desktop density levels and target sizes]] |
| Drop highlight `primary` at 16 percent | dragged state layer value | [[ADR-0009 State layer percentages]] |

## Sources

- WAI-ARIA Authoring Practices tabs pattern (verified 2026-11-21: tablist, tab with aria-selected, tabpanel; Left and Right Arrow with wrap; Home and End optional; Space or Enter activates; Shift+F10 opens a tab's popup menu; Delete optional): https://www.w3.org/WAI/ARIA/apg/patterns/tabs/
- WAI-ARIA Authoring Practices window splitter (handles): https://www.w3.org/WAI/ARIA/apg/patterns/windowsplitter/
- Secondary navigation tab tokens (container height 48, indicator 2, divider 1, container `surface`, divider `surface-variant`, indicator `primary`): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-secondary-navigation-tab.scss
- WCAG 2.2 SC 2.5.7 Dragging Movements: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- State layer values: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-state.scss
- Engine docking: `tre:docs/guide/docking.md`; tess-ui: `tess-ui:docs/guide/docking.md`, `tess-ui:docs/components/dock.md`; shell: `tess-shell:docs/guide/surfaces.md` (Melded Panels, Peek).
- Not verified: Home and End on the dock strip and the drop highlight at 16 percent follow the APG and the state tokens; the combined zone shrinking rule, the long press menu on touch and the move announcement are Tesserae design choices #needs-verification.
