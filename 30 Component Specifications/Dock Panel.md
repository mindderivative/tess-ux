---
title: Dock Panel
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, dock, tabs, drag-and-drop, keyboard]
related: ["[[Dock]]", "[[Splitter]]", "[[Tabs]]", "[[Menu]]", "[[Icon Button]]", "[[Tooltip]]", "[[Drag and Drop]]", "[[Melded Panel]]", "[[Panel and Surface]]", "[[State Layers]]", "[[Focus Ring]]", "[[Typography]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Dock]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# Dock Panel

> [!info] Summary
> A Dock Panel is one panel of a [[Dock]]: a titled tab in a zone, with optional close button, that the user shows, moves to another zone, drops onto the half of a split, or closes. A panel may also hold halves (other panels side by side or stacked) with a handle between them. MD3 has no dock panel; the tab follows the MD3 secondary tab ([secondary navigation tab tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-secondary-navigation-tab.scss)). Source of truth in code: see Status in code.

## Purpose

A dock panel names a piece of content (Files, Outline, Console) so the user can find, show, rearrange and dismiss it.

## When to use and not

- Use when: content lives in a [[Dock]] zone or half and the user manages it as a unit.
- Do not use when: a panel is page content that never moves ([[Panel and Surface]]); tabs choose between views of the same data ([[Tabs]]); the surface is a shell edge panel ([[Melded Panel]]).
- A panel has either halves or content, not both. A half has no zone.

## Anatomy

1. Tab: container, label, optional close button, active indicator.
2. Label: the panel's title (else its name), one line.
3. Close button (optional, `Closable`): 24 by 24 dp hit area, 14 dp glyph.
4. Active indicator: 2 dp line at the bottom edge of the selected tab, full tab width, `primary`.
5. Strip: the row of tabs of a zone or half; a 1 dp divider under it.
6. Content: the panel's node, shown under the strip.
7. Half (when split): a column of its own strip over its body; between two halves a 24 dp handle ([[Splitter]]).
8. Drop bands (half): four edge bands, each the outer 25 percent of the half on one side, and the middle (the rest, strip included).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Plain tab | Panel the user cannot close | label only |
| Closable tab | Panel the user may dismiss and reopen | `Closable: true`; close button after the label |
| Split panel | A panel of halves | `DockPanel` inside a `DockPanel`; handle between halves; each half is a small zone |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest, inactive | Label `on_surface_variant`; no indicator | `on_surface_variant` |
| Active (selected) | Label `on_surface`; indicator under the tab | label `on_surface`; indicator `primary` 2 dp |
| Hover | State layer over the tab | `on_surface` at 8 percent |
| Focus (keyboard) | State layer plus ring | layer 10 percent; ring 3 dp `secondary`, inward, because the tab touches the strip edge ([[Focus Ring]]) |
| Pressed | State layer | 10 percent |
| Dragging | The tab shows the dragged layer | 16 percent ([[State Layers]]) |
| Drop target (half) | Band highlighted | `primary` 16 percent, outline 2 dp `primary` |
| Disabled | Not applicable: a panel that cannot be used is not docked | not applicable |

Layers: [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]. Token names for the MD3 secondary tab: active label `on_surface`, inactive label `on_surface_variant`, indicator `primary`, divider `surface_variant`, focus indicator `secondary` (verified in Sources).

## Tokens used

| Part | Role or token |
|---|---|
| Strip and tab container | `surface` |
| Label active, inactive | `on_surface`, `on_surface_variant` |
| Label type | `title_small` (14/20, weight 500) ([[Typography]]) |
| Indicator | `primary`, 2 dp |
| Divider | `surface_variant`, 1 dp |
| Close glyph | `on_surface_variant` |
| Layers | `on_surface` ([[State Layers]]) |
| Highlight | `primary` |

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Tab height | 48 | 40 | 32 | default equals the MD3 secondary tab container height 48; compact and dense are Tesserae steps of 8 dp; [[Tabs]] should use the same values #needs-verification |
| Tab horizontal padding | 16 | 12 | 8 | tess-ui `TAB_PADDING` 16 at all levels |
| Close button hit area | 24 by 24 | 24 by 24 | 24 by 24 | glyph 14 dp centred; 8 dp before it |
| Close button hit area, touch context | 48 by 48 | 48 by 48 | 48 by 48 | the tab height already holds it |
| Indicator | 2 | 2 | 2 | |
| Divider | 1 | 1 | 1 | |
| Tab width | label width + 2 x padding (+ 32 with close) | | | label width measured with `title_small` |
| Minimum half of a split | 48 | 48 | 48 | `MIN_SPLIT` |
| Handle between halves | 24 | 24 | 24 | hit area; grip 4 by 48 dp |

## Layout and overflow

- A tab label is one line; it never wraps. A title longer than the tab maximum of 240 dp is cut with an ellipsis and the tab shows the full title as its tooltip #needs-verification (240 dp is a Tesserae choice).
- Tabs are laid out in a row at their own width and never shrink. When the tabs of a zone are wider than the zone, the strip scrolls horizontally (scrollbar rule: [[ADR-0003 Scrollbar rule]]) and the selected tab is scrolled into view on selection and on focus; tabs do not wrap to a second row #needs-verification (design choice; tess-ui tabs do not shrink and no overflow handling is documented).
- The label is vertically centred in the tab by construction (AC-DEN-9).
- The shown panel fills the zone below the strip and scrolls its own content.

## Behaviour

- Pointer: click or press a tab to show its panel; drag a tab past 4 dp to move the panel (to a zone, to the middle of a half to join it as a tab, to an edge band of a half to split it); the highlight shows what a drop will do. Releasing outside any target leaves the panel where it was. A drag on the close button closes nothing; pressing the close button closes the panel and shows the next panel of the zone (else the previous).
- Keyboard: the strip is one Tab stop. In a horizontal strip Left and Right Arrow move to the previous and next tab and show its panel (wrapping), Home and End go to the first and last tab, Enter or Space shows the focused tab, Shift+F10 or the Menu key opens the tab menu ("Move to ..." for every zone and half), Escape closes the menu and cancels a drag. The close button of a tab is a separate Tab stop after the strip's selected tab #needs-verification (tess-ui makes the close button `focusable` but only the selected tab keeps `focusable`; the order is not run).
- Touch: tab height 48 dp meets the touch minimum; a long press opens the tab menu #needs-verification.
- Split drop: dropping on an edge band splits the half (the panel takes a new half on that side with a handle); dropping on the middle or the strip adds the panel to the half as a tab; a panel cannot be dropped on the halves inside it. A half made by a drop collapses when its last panel leaves, and its neighbour takes the room back.
- Closing: `Closable` panels are undocked, kept and reported through the dock's close handler; `Closed` holds the names of closed panels (two-way); removing a name from `Closed` reopens the panel as the last tab of its zone.
- Retitling: changing a panel's title updates its tab and its accessible name in the same frame.

## Tooltip and overlay behaviour

- The tab shows a tooltip on the tab only when its label is truncated; the close button shows "Close" ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]).
- The tab menu is a [[Menu]]; it opens at the tab, closes on Escape or an outside press and returns focus to the tab.
- No tooltip shows during a drag.

## Motion

- No animation: the indicator moves in one frame; a panel appears in the frame of the selection; drop highlights appear and go in the frame of the pointer's move. With reduced motion on nothing changes ([[Motion]]).

## Accessibility

- Role and name: the tab has role `tab`, its title as the name and `selected` true on the shown tab; the content has role `tabpanel` named by its title; the strip has role `tablist` named "<Side> panels" for a zone or "<title> panels" for a half; the close button has role `button` named "Close <title>" (APG tabs pattern: aria-selected, aria-controls on tab, aria-labelledby on tabpanel).
- Keys: as in Behaviour. Per the APG tabs pattern Left and Right Arrow move focus with wrap, Home and End optionally go to the ends, Space or Enter activate when activation does not follow focus, Shift+F10 opens a tab's menu and Delete optionally closes the tab; Tesserae adopts Home and End and not Delete.
- Announcements: a changed title is announced by the name change; a panel moved to another zone or half is announced as "<title> moved to <side>" #needs-verification.
- Target sizes: tab 48 dp high and at least 24 dp wide; close button 24 by 24 dp (WCAG 2.2 SC 2.5.8).
- Contrast: label `on_surface` and `on_surface_variant` on `surface` at least 4.5:1; indicator `primary` on `surface` at least 3:1; focus ring `secondary` at least 3:1.
- Drag has a non-drag alternative: the tab menu (WCAG 2.2 SC 2.5.7).

## Dark and light

All colours are role references; the tab, strip and highlight retint when the scheme changes. The indicator `primary` and the highlight `primary` meet 3:1 against `surface` in both schemes (AC-DKP-9).

## Defaults

| Setting | Default |
|---|---|
| Title | the panel's name |
| Closable | false |
| Zone | none in a plain Dock: the author gives `Zone` on the panel |
| Panel size | left and right 240 dp wide; top and bottom 180 dp high |
| Tab height | 48 dp at `default` |
| Edge band | 25 percent of the half on each side |
| Drag threshold | 4 dp |

## Acceptance criteria

- [ ] AC-DKP-1 (geometry check): tab height is 48, 40 and 32 dp at default, compact and dense; horizontal padding 16, 12 and 8; indicator 2 dp high and as wide as the tab; divider 1 dp; the tab width equals label width plus twice the padding (plus 32 dp with a close button). Pass: equal to the dp at scale 1.0 and 2.0.
- [ ] AC-DKP-2 (geometry check): the close button's hit area is at least 24 by 24 dp (48 dp in a touch context), the glyph is 14 dp and centred within 0.5 dp, the gap before it is 8 dp, and the hit area does not overlap the tab body's hit area. Pass: hit test extents at default, compact and dense.
- [ ] AC-DKP-3 (token test): label fill `on_surface` when selected and `on_surface_variant` otherwise, indicator `primary`, divider `surface_variant`, container `surface`; type `title_small`; no colour literal in the tab builder. Pass: resolved values equal the roles in light and dark.
- [ ] AC-DKP-4 (pixel check): tab state layers are `on_surface` at 8 percent (hover), 10 percent (focus) and 10 percent (pressed), 16 percent while dragged (within 2 channel values); a keyboard-focused tab draws a 3 dp inward ring in `secondary`; a pointer click draws no ring. Pass in light and dark.
- [ ] AC-DKP-5 (scripted input): in a zone of three tabs, Tab focuses the selected tab and a second Tab leaves the strip for the panel; Right Arrow selects the next tab and moves focus to it, wrapping from the last to the first; Left Arrow likewise; Home selects the first and End the last; Enter and Space select the focused tab. Pass: focused and selected tab ids after each key.
- [ ] AC-DKP-6 (scripted input): a drop on each band of a half: a point in the outer 25 percent of the left, right, top and bottom edge splits the half on that side (a new half with a handle between); a point in the middle or on the strip adds the panel as a tab of the half and shows it; a drop on a half inside the dragged panel is refused. Pass: the half tree and tab lists after seven drops (four edges, middle, strip, inside).
- [ ] AC-DKP-7 (scripted input): when the last panel leaves a half created by a drop, the half collapses and its neighbour regains the room within one frame; a half the view defined (not created by a drop) stays and shows its own content. Pass: half list and neighbour sizes.
- [ ] AC-DKP-8 (scripted input): the close button of a `Closable` tab closes its panel: the tab is gone, the zone shows the next panel (else the previous), the close handler is called once with the panel, the panel's name is in `Closed`; removing the name from `Closed` reopens the panel as the last tab of its zone; a drag started on the close button moves nothing. Pass: tab list, shown panel, handler count and `Closed` after each step.
- [ ] AC-DKP-9 (contrast script): `on_surface` and `on_surface_variant` on `surface` at least 4.5:1; `primary` indicator and highlight outline on `surface` at least 3:1; focus ring `secondary` on `surface` at least 3:1; in light and dark. Pass: all pairs.
- [ ] AC-DKP-10 (AT tree assertion): tab role `tab` named by the title, `selected` true on the shown tab only; panel role `tabpanel` named by the title; strip role `tablist` named "<Side> panels" (zone) or "<title> panels" (half); close button role `button` named "Close <title>"; after retitling the tab, the tab name and the panel name equal the new title in the same frame. Pass: property equality.
- [ ] AC-DKP-11 (scripted input): two panels with the same title in one dock are told apart: each has its own id, `layout()` records both, `restore()` puts each back, and moving or closing one by id affects only that one. Pass: panel list and `layout()` content for a dock with two panels titled "Console".
- [ ] AC-DKP-12 (geometry check): a zone narrower than its tabs scrolls the strip horizontally with a scrollbar per [[Scrollbar and Scroll Container]]; the selected tab and the focused tab lie fully inside the strip viewport after selection or focus; the tabs do not wrap and do not shrink below their label width plus padding. Pass: scroll offset and tab rectangles for a strip with 12 tabs in a 240 dp zone #needs-verification.
- [ ] AC-DKP-13 (scripted input): the tab menu opened with Shift+F10 or the Menu key lists "Move to ..." for each zone except the panel's own and each half, choosing an entry moves the panel and keeps focus on its tab, Escape closes the menu and returns focus to the tab. Pass: entries, panel side, focus node after each action.
- [ ] AC-DKP-14 (scripted input): a title longer than the tab maximum of 240 dp is cut with an ellipsis, the tab is 240 dp wide at most, and the full title is shown as the tab's tooltip after 500 ms; a title that fits shows no tooltip. Pass: tab width and tooltip layer counts #needs-verification.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/docking.py` (`_tab`, `_rebuild`, `_key`, `TAB_HEIGHT` 48, `TAB_PADDING` 16, `INDICATOR` 2, `CLOSE_SIZE` 18, `HALF_EDGE` 0.25, `_band`), `tess-ui:src/tess_ui/dockhost.py`, `tess-ui:src/tess_ui/spec/dock.py`, `tess-ui:docs/components/dock-panel.md`, tests `tess-ui:tests/test_dock_halves.py`, `test_dock_close.py`, `test_docking.py` | Partly meets. Meets (per code and docs, not all run): tab 48 dp, padding 16, 2 dp indicator, `title_small` label, roving selected tab with arrow keys and wrap, `selected` state and roles `tab`, `tablist`, `tabpanel`, tab menu on the Menu key and Shift+F10, drop bands with a 25 percent edge, middle and strip, no drop on the panel's own halves, collapse of an emptied half, `Closable` with `Closed` two-way, retitle, layout and restore with halves (AC-DKP-1 at default, AC-DKP-3, AC-DKP-5 in part, AC-DKP-6, AC-DKP-7, AC-DKP-8, AC-DKP-10 in part, AC-DKP-13 in part). Fails AC-DKP-2: the close button is 18 by 18 dp. Fails AC-DKP-1 at compact and dense: tab height is fixed at 48 and padding at 16. Fails AC-DKP-5 in part: Home and End are not handled. Fails AC-DKP-4 in the drop highlight value only (12 percent, `HIGHLIGHT_ALPHA` 0x1F, not 16). Fails AC-DKP-11: panels are found by title and two panels with the same title clash (`tess-ui:docs/guide/docking.md`, Not yet covered). AC-DKP-12 (strip overflow) and AC-DKP-14 (long title) are not run and no handling was found in `_tab` (tabs are `flex_shrink` 0 at the label width): they probably fail [INFERENCE from code]. Not built: reordering tabs, floating panels, tearing a panel into a window, maximising a panel, dragging or closing a half's own content, layouts saved by name |
| tess-shell | not applicable | Not applicable: a shell dock panel is a melded Panel ([[Melded Panel]]); there are no tabs or halves |
| tre | `tre:docs/guide/docking.md`, `tre:crates/engine-core/src/dock.rs` | Primitive only: zones, `dock_panel`, `set_active_panel`, `undock_panel`, `start_panel_drag`, `dock_target` and `dock_drop`; no tab, handle, highlight or close |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has no dock panel; tabs are the nearest) | desktop tool windows | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tab height 40 at compact and 32 at dense (MD3 secondary tab container 48) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tabs are draggable between zones and halves, with a menu alternative | MD3 tabs are fixed; docking needs movement | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed layers 10 percent, dragged 16 | Material Web latest state tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Inward focus ring | the tab touches the strip edge | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Close button on a tab, 24 dp hit area | desktop panels are dismissable; MD3 tabs have no close | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- Secondary navigation tab tokens (container height 48, active indicator height 2, divider height 1 with `surface-variant`, indicator `primary`, active label `on-surface`, inactive label `on-surface-variant`, container `surface`, focus indicator `secondary`), verified 2026-11-21: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-secondary-navigation-tab.scss
- WAI-ARIA Authoring Practices tabs pattern (verified 2026-11-21: tablist, tab, tabpanel, aria-selected, Left and Right Arrow with wrap, Home and End optional, Space or Enter, Shift+F10, Delete optional): https://www.w3.org/WAI/ARIA/apg/patterns/tabs/
- WCAG 2.2 SC 2.5.7 Dragging Movements: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- State layers: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-state.scss
- tess-ui: `tess-ui:docs/components/dock-panel.md`, `tess-ui:docs/guide/docking.md`; engine: `tre:docs/guide/docking.md`.
- Not verified: compact and dense tab heights, the 240 dp tab maximum, strip overflow behaviour, touch long press, drop announcements and close button focus order are Tesserae design choices #needs-verification.
