---
title: Popup Window
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, window, popup, engine, shell]
related: ["[[Popup]]", "[[Menu]]", "[[Tooltip]]", "[[Layer Window]]", "[[Layer Window|Overlay Window]]", "[[Anchored Placement]]", "[[Accessibility Tree]]", "[[12 Overlays]]", "[[Elevation#Margin a layer window reserves for its shadow|Surface Shadow]]", "[[Elevation]]", "[[Shape]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Popup]]", "[[12 Overlays]]", "[[ADR-0004 Tooltip rule]]"]
aliases: ["Popup window"]
---

# Popup Window

> [!info] Summary
> A Popup Window is an `xdg_popup` surface that the compositor places next to a rectangle of its parent (a bar or another popup), flipping and sliding it to stay on screen. The element's visual and interaction rules are in [[Popup]] and [[Menu]]; this note states the surface constraints. MD3 menus are the visual counterpart ([Menus](https://m3.material.io/components/menus/overview)).

## Purpose

Show menus, submenus, tray flyouts and tooltips outside the small surface of a bar, with placement, grabs and dismissal done by the compositor.

## When to use and not

- Use when: the content hangs off a rectangle of a [[Layer Window]] or another Popup Window.
- Do not use when: the popup lives inside an application window (use a layer of that window and [[Anchored Placement]]); the content needs exclusive keyboard from a shortcut (use a panel, [[Layer Window]]).

## Anatomy

1. Parent: an open layer window or popup window.
2. Anchor rectangle in the parent's coordinates, `anchor` point, `gravity` direction, `offset`.
3. Constraint adjustment: `flip_x`, `flip_y`, `slide_x`, `slide_y`, `resize_x`, `resize_y` (default flip_y and slide_x).
4. Surface size fixed for its life; `geometry` the body rectangle when a shadow margin surrounds it.
5. Input region, grab flag.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Menu | commands | `grab` true, dismissed by outside click and Escape |
| Submenu | nested menu | parent is the menu popup; closing the parent closes it |
| Tooltip | hint | no grab; opens 500 ms after hover, at once on keyboard focus, `input_region` the body ([[ADR-0004 Tooltip rule]]) |
| Catcher | detect an outside press | 1 by 1 transparent popup with `grab` true; closes with reason `dismissed` |

## States

| State | Visual change | Token values |
|---|---|---|
| Open | body drawn at the placed position | [[Elevation]] level 2 shadow in the margin |
| Placed | `configure` reports `x`, `y`, `width`, `height` after any flip or slide | none |
| Dismissed | `closed` with reason `dismissed` (outside click or Escape), `app` or `failed` | none |

## Tokens used

Body `surface_container`, radius `extra-small` to `medium` by the element ([[Shape]]), shadow by [[Elevation#Margin a layer window reserves for its shadow|Surface Shadow]]; shadow reach `m` (for example 20 dp) as a transparent margin inside the surface.

## Sizing and density

Size is fixed at creation: measured by building the content first (the shell measures in a headless window), then `size = body + 2 x shadow margin`. Menu rows and widths follow [[Menu]] and [[Spacing and Density]]. The body must fit the output with 8 dp space to the edge or scroll its rows.

## Dimensions and defaults

The popup window adds only a transparent shadow margin around the body and fixes the placement gap; body padding, rows and type belong to [[Menu]] and [[Tooltip]]. Density does not change the surface rules, so the three level columns repeat one value. The 8 dp output margin is the note's own rule; the tooltip rows come from [[Tooltip]] and the menu rows from [[Popup]]. Any value without a source in those notes is a Tesserae design choice #needs-verification.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| popup surface | height | - | N/A: fixed at creation from the measured body plus shadow margins | N/A: same as the Default column | N/A: same as the Default column | [[Popup Window#Sizing and density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height, measured from content otherwise); tre: yes (size at creation, fixed after) |
| catcher | height | - | 1 | 1 | 1 | `tre:docs/reference/layer-window.md` (1 by 1 transparent popup) | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: the shell opens popups with a grab and no catcher; tre: yes (size) |
| catcher | min width | - | 1 | 1 | 1 | `tre:docs/reference/layer-window.md` (1 by 1 transparent popup) | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: the shell opens popups with a grab and no catcher; tre: yes (size) |
| body | padding | - | N/A: the surface adds no padding; the element sets it ([[Menu]], [[Tooltip]]) | N/A: same as the Default column | N/A: same as the Default column | [[Menu]], [[Tooltip]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Padding); tre: yes (padding) |
| body (menu, flyout, rich tooltip) shadow margin | margin | `elevation.level2` | 10 | 10 | 10 | [[Elevation#Margin a layer window reserves for its shadow]] | tess-ui: n/a: element absent in tess-ui; tess-shell: via Elevation or Shadows (the bleed is computed from them); tre: yes (geometry, margin inside the surface) |
| body (plain tooltip) shadow margin | margin | `elevation.level0` | 0 | 0 | 0 | [[Elevation#Margin a layer window reserves for its shadow]] | tess-ui: n/a: element absent in tess-ui; tess-shell: via Elevation or Shadows (the bleed is computed from them); tre: yes (geometry, margin inside the surface) |
| body to output edge | margin | `space.3` | 8 | 8 | 8 | [[Popup Window#Sizing and density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook; tre: hardcoded in tre (compositor flip and slide through constraint_adjustment, margin 0) |
| body to anchor rectangle | gap | `space.0` | 0 | 0 | 0 | [[Popup]] (`Gap` default 0) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Gap); tre: yes (offset) |
| body to anchor rectangle, tray menu | gap | `space.2` | 4 | 4 | 4 | [[Popup]] (the shell uses 4 for tray menus) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Gap); tre: yes (offset) |
| body | border width | - | 0 | 0 | 0 | [[Popup]] (no border) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: yes (border_width) |
| body | border color | - | N/A: the popup body draws no border | N/A: same as the Default column | N/A: same as the Default column | [[Popup]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color); tre: yes (border_color) |
| body (menu, plain tooltip) | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]], [[Popup]], [[Tooltip]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| body (flyout, rich tooltip) | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]], [[Popup]], [[Tooltip]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| popup surface | font | - | N/A: the surface draws no text; the element sets its type role | N/A: same as the Default column | N/A: same as the Default column | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| popup surface | icon size | - | N/A: the surface draws no icon; the element sets icon size | N/A: same as the Default column | N/A: same as the Default column | [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| body (menu, flyout, rich tooltip) | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]], [[Popup]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| body (plain tooltip) | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]], [[Tooltip]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: yes (shadows) |

## Layout and overflow

- Placement is the compositor's: with `geometry` set, flips and slides apply to the body, not the margin; `configure` x and y are the body's.
- A body taller than the available space either flips, slides or is cut by the compositor; content that can exceed a maximum height scrolls inside the popup ([[ScrollBox]]); a fixed popup size cannot grow, so a popup whose content changes is closed and reopened.
- `resize_x` or `resize_y` resize the body; the input region is not rescaled and must be set again from the `configure` size.

## Behaviour

- Pointer: an outside click on another application or the desktop dismisses it and the click is the popup's, not delivered underneath; a click in the shadow margin follows `input_region` (`geometry` lets it pass through); a click on another window of the same application is delivered there and does not dismiss, so the opener listens and closes.
- Keyboard: with `grab` the popup has the keyboard; Escape dismisses and focus returns to the opener; arrows move within a menu ([[Menu]]); closing a popup closes its submenus.
- Touch: as pointer.

## Tooltip and overlay behaviour

A tooltip is a popup; one tooltip at a time; dismissed on pointer leave after 150 ms grace, Escape, scroll of an ancestor, activation, trigger removal and window focus loss ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]). A popup opens only from a user action that gives an input serial.

## Motion

Open and close are not animated by the surface (its settings cannot change after creation); an animation of content inside the body is the module's; durations from [[Motion]], reduced motion: immediate.

## Accessibility

The popup is published like a window; its body has the role of the element (`menu` with `menuitem`, `tooltip`); focus moves into it on open and back to the opener on close ([[14 Accessibility Basics]], [[Accessibility Tree]]). Hover content stays reachable: tooltips follow WCAG 2.2 SC 1.4.13 via ADR-0011.

## Dark and light

Roles per scheme; the body is opaque ([[ADR-0004 Tooltip rule]]).

## Defaults

`size` required, `anchor_rect` required, anchor and gravity `none`, adjustment (flip_y, slide_x), `grab` true, `geometry` the whole surface, `input_region` the whole surface.

## Acceptance criteria

- [ ] AC-PPW-1 (geometry check): a menu hung off a bottom bar with no room below is placed above: `configure.y` is negative (relative to the parent) and the body lies fully on the output.
- [ ] AC-PPW-2 (geometry check): with a shadow margin of 20 dp and `geometry` set, the body (not the surface) is within 1 dp of the anchor-based position and flips at the body edge.
- [ ] AC-PPW-3 (scripted input): with `input_region: "geometry"` a click in the shadow margin reaches the window below; without it, it is taken.
- [ ] AC-PPW-4 (scripted input): Escape closes a grabbing popup with reason `dismissed`, focus returns to the opener, and its submenus close.
- [ ] AC-PPW-5 (scripted input): an outside click on another application's surface dismisses; a click on another window of the same application leaves it open and delivers the click there.
- [ ] AC-PPW-6 (scripted input): a tooltip popup opens 500 ms after hover and at once on keyboard focus; it stays open while the pointer moves from trigger to tooltip and closes 150 ms after the pointer left both.
- [ ] AC-PPW-7 (AT tree assertion): a menu popup exposes role `menu` with `menuitem` children and focus is on the first item or the opener-defined item.
- [ ] AC-PPW-8 (scripted input): a popup with no parent that is open fails with reason `failed` and no surface remains.
- [ ] AC-PPW-9 (pixel check): the body is opaque: no pixel of the body area has alpha below 255 at the container colour.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/surfaces/popup.py` (a `PopupWindow` per open, measured in a headless window, one open at a time, tooltips as popups with `Enter_Delay` and `Exit_Delay`), `tess-shell:src/tess_shell/surfaces/popup_measure.py` | partly meets: tooltip exit delay 200 ms in the shell against 150 ms in ADR-0011 (fails AC-PPW-6, #needs-verification of the shipped value); the other criteria not verified; the 8 dp body to output edge margin cannot be set (no key; the compositor adjusts by `Adjust`), a project request |
| tess-ui | `tess-ui:src/tess_ui/overlays.py`, `tess-ui:src/tess_ui/composed.py` | not applicable: tess-ui popups are layers inside its window |
| tre | `tre:docs/reference/layer-window.md` (`PopupWindow`), `tre:docs/guide/menus-from-a-bar.md`, `tre:crates/engine-py/src/popup_window.rs` | meets by documented behaviour; `geometry` since 0.6.3 and `input_region` since 0.6.5; settings fixed after creation; a keyboard-exclusive panel cannot be a popup (no grab without a serial); the output edge margin is not settable (the compositor flips and slides to the edge, margin 0), an engine request |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Menu surface placed by the compositor, shadow in a transparent margin | Wayland protocol | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tooltip hover grace for all tooltips | WCAG 2.2 SC 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |

## Sources

- `tre:docs/reference/layer-window.md` (PopupWindow, geometry, input region, dismissal), `tre:docs/guide/menus-from-a-bar.md`.
- `tess-shell:src/tess_shell/surfaces/popup.py`.
- WCAG 2.2 SC 1.4.13: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html. xdg-shell popup: https://wayland.app/protocols/xdg-shell (not opened #needs-verification). MD3 menus (JavaScript app #needs-verification): https://m3.material.io/components/menus/overview.
