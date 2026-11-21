---
title: Layer Window
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, window, engine, shell]
related: ["[[Popup Window]]", "[[Application Window]]", "[[Layer Window|Overlay Window]]", "[[Panel and Surface]]", "[[Popup]]", "[[Accessibility Tree]]", "[[Anchored Placement]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[Elevation#Margin a layer window reserves for its shadow|Surface Shadow]]", "[[Drag and Drop]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[14 Accessibility Basics]]", "[[12 Overlays]]"]
aliases: ["Layer window", "Content-sized layer window"]
---

# Layer Window

> [!info] Summary
> A Layer Window is a window whose Wayland role is a layer surface: a bar, panel, dock, OSD or wallpaper that the compositor places on a stacking layer, optionally reserving screen space and taking the keyboard. It has no MD3 counterpart (Tesserae shell surfaces). This note states the constraints the surface specifications ([[Panel and Surface]], [[Popup]]) must respect.

## Purpose

Let the shell draw bars and panels at screen edges, reserve space, accept input only where it draws, and be reachable by assistive technology and the keyboard.

## When to use and not

- Use when: the surface is anchored to screen edges and placed by the compositor (bars, panels, launchers, OSDs).
- Do not use when: a normal application window ([[Application Window]]); a menu or flyout that the compositor flips next to a rectangle ([[Popup Window]]); content that floats inside a window (a layer of that window, [[Anchored Placement]]).

## Anatomy

1. Namespace (what the surface is for, for example `tesserae-shell.bar`).
2. Layer: `background`, `bottom`, `top`, `overlay`.
3. Anchor edges, size, margin, exclusive zone and exclusive edge.
4. Keyboard mode: `none`, `on_demand`, `exclusive`.
5. Input region: whole surface, nothing, rectangles, or the union of drawn nodes (`auto`).
6. Root node: transparent, no padding or gap, drawn at the surface scale.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Bar | edge strip | anchored to one edge and both across; `exclusive_zone` equals its thickness; `keyboard` none or on_demand |
| Panel | floating or attached surface | anchored to edges or centred; keyboard on_demand or exclusive |
| Launcher or dialog panel | opened by shortcut | `layer: overlay`, `keyboard: exclusive`, content-sized, role `dialog` |
| OSD | transient indicator | click-through (`input_region` empty), no keyboard |
| Content-sized | result lists that grow | `size: ("content", "content")` with `min_size` and `max_size` |

## States

| State | Visual change | Token values |
|---|---|---|
| Active (keyboard) | focus ring on the focused node only; the surface itself shows nothing | [[Focus Ring]] |
| Hidden or occluded | no frames drawn (compositor dependent) | none |
| Closed by compositor | the window object is dead; a new window is made | none |

## Tokens used

Background of the body: roles `surface` or `surface_container` ([[Colour Roles]]); shadow margin and corner radius by [[Elevation#Margin a layer window reserves for its shadow|Surface Shadow]], [[Shape]] and [[Elevation]]; padding 0 on the root and `space.*` steps inside; the root is transparent.

## Sizing and density

- Bar thickness follows the density of its content: control height plus vertical padding (40, 32, 28 dp controls, [[Spacing and Density]]). The bar height is a project setting, not specified here beyond fitting the controls with at least `space.2` (4 dp) padding.
- A content-sized axis is the root's outer size with padding, whole logical pixels rounded up, clamped by `min_size` and `max_size`; content past the maximum is clipped, so it goes in a [[ScrollBox]].
- Exclusive zone: positive only for one anchored edge, or one edge plus both across; a corner-anchored surface sets `exclusive_edge`.

## Dimensions and defaults

A layer window has no look of its own: the root is transparent. Rows below give the values for the surface and the bodies drawn in it. The panel body padding follows [[Panel and Surface]] (a design choice there, #needs-verification-as-design-choice); the elevation of a floating panel is a Tesserae design choice #needs-verification.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| surface | height | - | N/A: a project sets size per surface; a bar sets thickness, a content-sized panel measures its content | N/A: same as the Default column | N/A: same as the Default column | [[Layer Window#Sizing and density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height of a Panel, Thickness of a Frame); tre: yes (size) |
| bar | min height | `density.control_height` plus 2 x `space.2` | 48 | 40 | 36 | control height from [[Spacing and Density]] plus the 4 dp minimum padding of this note | tess-ui: n/a: element absent in tess-ui; tess-shell: via Frame Thickness; tre: yes (min_size) |
| surface | min width | - | N/A: the surface width is set by anchors or content, no floor is specified | N/A: same as the Default column | N/A: same as the Default column | [[Layer Window#Sizing and density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook; tre: yes (min_size) |
| root node | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Layer Window#Defaults]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Padding on the body); tre: yes (padding on the root) |
| floating panel body | padding | `space.4`, `space.3`, `space.2` | 12 12 12 12 | 8 8 8 8 | 4 4 4 4 | design choice, [[Panel and Surface]], [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Padding); tre: yes (padding) |
| surface | margin | - | 0 | 0 | 0 | [[Layer Window#Defaults]] (layer `margin`, screen edge to surface) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Inset on a Panel, Margin on a Frame); tre: yes (margin) |
| floating panel shadow margin | margin | `elevation.level2` | 10 | 10 | 10 | [[Elevation#Margin a layer window reserves for its shadow]] | tess-ui: n/a: element absent in tess-ui; tess-shell: via Elevation or Shadows (the bleed is computed from them); tre: yes (margin) |
| dialog panel shadow margin | margin | `elevation.level3` | 15 | 15 | 15 | [[Elevation#Margin a layer window reserves for its shadow]] | tess-ui: n/a: element absent in tess-ui; tess-shell: via Elevation or Shadows (the bleed is computed from them); tre: yes (margin) |
| root node | gap | `space.0` | 0 | 0 | 0 | [[Layer Window#Defaults]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Spacing); tre: yes (gap) |
| bar and panel body | border width | - | 0 | 0 | 0 | [[Panel and Surface]] (no border by default) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: yes (border_width) |
| bar and panel body | border color | - | N/A: no border is drawn | N/A: same as the Default column | N/A: same as the Default column | [[Panel and Surface]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color); tre: yes (border_color) |
| floating panel body | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]], [[Panel and Surface]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| bar | corner radius | - | N/A: the Bar has no look of its own; the Frame or project style sets corners | N/A: same as the Default column | N/A: same as the Default column | [[Panel and Surface]] (AC-PNL-10) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| surface | font | - | N/A: the layer surface draws no text; its content nodes carry type roles | N/A: same as the Default column | N/A: same as the Default column | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| surface | icon size | - | N/A: the layer surface draws no icon; content nodes carry icon sizes | N/A: same as the Default column | N/A: same as the Default column | [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| bar | elevation | - | N/A: the Bar has no look of its own and no shadow | N/A: same as the Default column | N/A: same as the Default column | [[Panel and Surface]] (AC-PNL-10) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| floating panel body | elevation | `elevation.level2` | 2 | 2 | 2 | design choice, proposed ADR floating panel elevation, [[Elevation]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| launcher or dialog panel body | elevation | `elevation.level3` | 3 | 3 | 3 | [[Panel and Surface]] (AC-PNL-5, dialog level 3) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: yes (shadows) |

## Layout and overflow

- Layout in logical pixels at the surface scale; fractional scale allowed.
- A layer window clips its own layers (the `show_layer` layers) to its small surface; a menu from a bar is a [[Popup Window]] instead, which is not clipped by the bar.
- Overflow: content past a fixed size is clipped; there is no scrolling of the surface itself.
- Input: a transparent area that must not catch clicks is excluded by `input_region`; `auto` follows painted, hit-testable shapes, with rounded corners and the painted hit shape counted.

## Behaviour

- Pointer: events as a window; a press on a bar does not move another window's keyboard focus.
- Keyboard: `none` never gets keys; `on_demand` gets keys after a click; `exclusive` takes the keyboard on opening and nothing else gets keys until it closes. Escape closes an exclusive panel; Tab stays in the surface.
- A surface that holds the keyboard exclusively cannot be left by a click elsewhere; it closes itself on the `active` event or by a 1 by 1 grabbing popup (engine behaviour); the click that dismisses is not delivered to what lies under it.
- Moving: `window_region: drag_margin` on a handle node moves a movable panel by its margins; only anchored edges move; margins clamp so the surface stays on its output. A keyboard alternative to drag is required (WCAG 2.2 SC 2.5.7): a movable panel offers a command or key to reposition it (not built).
- Touch: as pointer.

## Tooltip and overlay behaviour

Tooltips and menus of a bar are popups ([[Popup Window]], [[Popup]]); the bar surface does not enlarge for them. A tooltip opens after 500 ms of hover and at once on keyboard focus ([[ADR-0004 Tooltip rule]]).

## Motion

Margins animate through the engine (`animate("margin_top", to, ms, easing)`), one small commit per step, whole pixels; size and exclusive zone change in steps, not animations. Slide durations come from [[Motion]]; with reduced motion the slide is a jump.

## Accessibility

- A layer surface is published as one more window of the application; its nodes carry their role, name and state; the window node has no name of its own, so the shell names it from the surface name ("Top bar") and a panel that takes the keyboard exclusively is a dialog ([[Accessibility Tree]]).
- Under Wayland the reader gets the tree but no screen position of the surface.
- Keyboard focus entering or leaving tells the reader whether the window is active.
- Announcements from a hidden module go through the window's announce queue ([[Accessibility Tree]]).
- Not tried with Orca, NVDA or VoiceOver.

## Dark and light

Follows the scheme; the transparent root shows the desktop; text on bars keeps 4.5 to 1 against the composed background where known (a translucent bar over a wallpaper cannot be guaranteed: use an opaque or sufficiently opaque body).

## Defaults

`layer` top, no anchor (centred), size (0, 0), `exclusive_zone` 0, `margin` 0, `keyboard` none, whole-surface input, transparent root with no padding or gap.

## Acceptance criteria

- [ ] AC-LYW-1 (scripted input): a bar anchored `top, left, right` with size (0, 32) and `exclusive_zone` 32 is created without a warning; a corner-anchored surface without `exclusive_edge` raises a `warning` event and reserves nothing.
- [ ] AC-LYW-2 (geometry check): a content-sized panel of 200 by 80 dp content with 16 dp root padding is 232 by 112 dp, and with `max_size` height 100 the surface is 100 dp high with content clipped.
- [ ] AC-LYW-3 (scripted input): with `input_region: []` a click passes to the window below; with `auto`, a click in a transparent corner of a 12 dp rounded body passes through and a click on the body is delivered.
- [ ] AC-LYW-4 (scripted input): a panel with `keyboard: exclusive` receives a key typed immediately after opening; a bar with `keyboard: none` receives none.
- [ ] AC-LYW-5 (scripted input): the `active` event fires false when a second exclusive surface takes the keyboard and true when it closes.
- [ ] AC-LYW-6 (AT tree assertion): each bar and panel window node has a non-empty name; an exclusive-keyboard panel body has role `dialog`.
- [ ] AC-LYW-7 (scripted input): dragging a handle with `drag_margin` on a surface anchored `top, left` changes only `margin_top` and `margin_left`, and the final margins are clamped to the output.
- [ ] AC-LYW-8 (review): every movable panel has a keyboard way to move it, or the audit records the gap.
- [ ] AC-LYW-9 (pixel check): in a layer window, a layer shown with `show_layer` is clipped to the surface and no ink lies outside it.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/surfaces/manager.py` (`_make_window`: namespace, layer, anchor, size, margin, `exclusive_zone`, `exclusive_edge`, `keyboard`, `input_region`; window node named from the surface; `dialog` role for exclusive panels), `tess-shell:src/tess_shell/surfaces/frame.py` | meets AC-LYW-1, 3, 4, 6 by construction; Movable Panel uses `drag_margin` (AC-LYW-7 not verified); no keyboard way to move a panel (fails AC-LYW-8); the surface min width has no key (tre `min_size` is not exposed), a project request |
| tess-ui | none | not applicable |
| tre | `tre:docs/reference/layer-window.md`, `tre:docs/guide/bars-and-panels.md`, `tre:crates/engine-platform/src/layer.rs` | meets by documented behaviour; content size is unreleased (TRE-REQ-022 at the time of reading) #needs-verification; screen position not given under Wayland |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Layer surfaces have no MD3 counterpart | desktop shell element | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Keyboard-exclusive panels are a dialog, not a popup | no grab without a user-action serial | [[ADR-0004 Tooltip rule]] |

## Sources

- `tre:docs/reference/layer-window.md` (settings, content size, keyboard, drag by margin, accessibility), `tre:docs/guide/bars-and-panels.md`.
- `tess-shell:src/tess_shell/surfaces/manager.py`.
- WCAG 2.2 SC 2.5.7: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html. wlr-layer-shell protocol: https://wayland.app/protocols/wlr-layer-shell-unstable-v1 (not opened #needs-verification).
