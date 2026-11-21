---
title: Application Window
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, window, engine]
related: ["[[Window]]", "[[Title Bar|Window Title Bar]]", "[[Window#Anatomy|Window Root]]", "[[Spacing and Density#Window size classes|Window Size Classes]]", "[[Application Window#Variants|Window Transparency]]", "[[Layer Window]]", "[[Popup Window]]", "[[Dialog]]", "[[Panel and Surface]]", "[[Accessibility Tree]]", "[[10 Layout Overflow and Scrolling]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[10 Layout Overflow and Scrolling]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
aliases: ["Application window"]
---

# Application Window

> [!info] Summary
> The Application Window is the engine's top-level OS window: a node tree, a minimum size, optional framework-drawn title bar and borders, and events for size, scale, colour scheme and activity. This note states what the UX specification requires of it. MD3 describes content adapting to a window by window size classes, not the window itself ([Window size classes](https://m3.material.io/foundations/layout/applying-layout/window-size-classes)). The tess-ui `Window` view is the [[Window]] note; the title bar is [[Title Bar|Window Title Bar]].

## Purpose

Give applications a predictable frame: a size that adapts by class, a minimum that never hides content, a drag and resize behaviour a keyboard user can match, and a state the UX can read.

## When to use and not

- Use when: a top-level application window is opened.
- Do not use when: the surface is a bar, panel or OSD placed by the compositor ([[Layer Window]]); a menu or flyout ([[Popup Window]]); a modal question inside the window ([[Dialog]], a layer in the same window).

## Anatomy

1. OS frame (decorated) or framework chrome (`decorations=False`: [[Title Bar|Window Title Bar]], resize border).
2. Root node: a flex row with 16 dp padding and 16 dp gaps by default; sized to the window ([[Window#Anatomy|Window Root]]).
3. Content tree; overlays are layers inside the window ([[Popup]], [[Dialog]]).
4. Optional dock zones.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Decorated | default apps | the OS draws title bar and borders |
| Undecorated | framework chrome | `decorations=False`, own title bar, `resize_border`, drag region |
| Transparent | floating cards | `transparent=True`, root `fill` alpha below 255; see [[Application Window#Variants|Window Transparency]] |
| Fullscreen | media, presentations | borderless; drag and resize regions inactive |

## States

| State | Visual change | Token values |
|---|---|---|
| Active | normal appearance | `active` event true |
| Inactive | title bar and window controls dim to opacity 0.6 or the role `on_surface_variant`; content unchanged | opacity 0.6 is the engine example, #needs-verification as a design choice |
| Maximized, fullscreen | resize border off, corner radius 0 | none |
| Occluded | draws nothing (engine) | none |

## Tokens used

Window background `surface`; scheme per [[Theme Following the System]]; padding of the root 16 dp (`space.5`); corner radius of an undecorated window 12 dp `medium` when not maximized ([[Shape]]); no elevation, the OS or [[Application Window#Variants|Window Transparency]] owns shadows.

## Sizing and density

- Window size classes: width compact below 600 dp, medium 600 to 839, expanded 840 to 1199, large 1200 to 1599, extra-large from 1600; height below 480, 480 to 899, 900 and above ([[Spacing and Density]], [[Spacing and Density#Window size classes|Window Size Classes]]). A boundary value belongs to the larger class.
- Minimum size: `min_width` and `min_height` are set so that every shown pane has its minimum width (320 dp) and no content is unreachable ([[10 Layout Overflow and Scrolling]]); a project sets a floor of 320 by 240 dp unless its panes need more (Tesserae design choice #needs-verification).
- Density is independent of the window size class.
- Not a per-density element otherwise.

## Layout and overflow

- The class is recomputed on each `resize` event and layout changes at class boundaries, not by clipping ([[10 Layout Overflow and Scrolling]]).
- A window smaller than its minimum is grown to it, except when maximized, fullscreen or held at a size by a tiling compositor, where `get("width")` is the truth; layouts must not assume the minimum was reached.
- Overflow of the window: content scrolls inside panes; the window never scrolls.
- Overlays are clipped to the window.

## Behaviour

- Pointer: a primary press on a drag region (not on an interactive node) moves the window; double-click within 500 ms and 4 px toggles maximize (on macOS the user's setting); a press within `resize_border` of an edge resizes; the cursor shows the matching resize cursor.
- Keyboard: Tab order and focus ring per [[14 Accessibility Basics]]; Alt+F4 or the OS shortcut closes; closing fires `close_requested`, which a handler may cancel (unsaved changes ask with a [[Dialog]]). On Windows, Alt+Space opens the window menu when `system_menu` is true.
- Drag and resize have keyboard equivalents through the OS window menu (move, size) where the platform has one; where it does not, an undecorated window offers none and fails the equivalent rule (WCAG 2.2 SC 2.5.7 for dragging, and SC 2.1.1).
- Touch: the OS moves and resizes.

## Tooltip and overlay behaviour

Not applicable on the window. Overlays inside it follow [[12 Overlays]]; losing window focus dismisses tooltips ([[ADR-0004 Tooltip rule]]).

## Motion

Window show, maximise and resize animation belongs to the OS. Inside, the window itself does not animate; reduced motion is read through `get("reduced_motion")` ([[14 Accessibility Basics]]).

## Accessibility

- The window is published as one window of the application with its title as name; the framework sets `title` (`set(title=...)`), which must be non-empty and describe the document or app ([[Accessibility Tree]]).
- `active` tells the reader whether the window has focus.
- Resize border target: the engine grab zone is set in logical pixels (6 dp in its example), below the 24 dp minimum; it relies on the equivalent control exception (OS window menu or keyboard resize) of WCAG 2.2 SC 2.5.8 #needs-verification.
- The reduced-motion and high-contrast preferences are read at start and tracked.

## Dark and light

Follows the system scheme at start where the platform tells it (Linux portal known at start; macOS and Windows after the first frame) ([[Theme Following the System]]).

## Defaults

Size 480 by 200 in the engine, so the project sets its own; decorations on; resizable; transparent off; root 16 dp padding and gap; `partial_redraw` on.

## Acceptance criteria

- [ ] AC-APW-1 (token test): `width_class(w)` and `height_class(h)` return the classes at the boundary values 599, 600, 839, 840, 1199, 1200, 1599, 1600 and 479, 480, 899, 900 as in [[Spacing and Density]].
- [ ] AC-APW-2 (geometry check): after `resize(300, 200)` on a window with minimum 320 by 240, the laid-out window is 320 by 240 (unless maximized or tiled), and no pane is narrower than 320 dp at the minimum size.
- [ ] AC-APW-3 (scripted input): a primary press on a node with `window_region: drag` and no interactive child sends `pointer_down` then `pointer_cancel` and no `click`; a press on a focusable child inside it is an ordinary press.
- [ ] AC-APW-4 (scripted input): two primary presses on a drag region within 500 ms and 4 px toggle maximize; outside those limits they do not.
- [ ] AC-APW-5 (scripted input): with `resize_border` 6, a press at 3 dp inside the left edge starts a resize and never reaches a node; at 8 dp it is an ordinary press; while maximized or fullscreen the border is inert.
- [ ] AC-APW-6 (AT tree assertion): the window exposes a non-empty title as its name; after `set(title="B")` the name is "B".
- [ ] AC-APW-7 (scripted input): `close()` fires `close_requested` first, and a listener that cancels keeps the window open.
- [ ] AC-APW-8 (scripted input): a `resize` event re-evaluates the class and the pane count of [[10 Layout Overflow and Scrolling]] (AC-LAY-9) in the same frame.
- [ ] AC-APW-9 (pixel check): overlays opened near the window edge are clipped to the window and nothing paints outside it.
- [ ] AC-APW-10 (review): an undecorated window offers a keyboard path to move, resize, minimize and close (OS window menu or in-app commands); the reviewer records which platforms lack it.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/spec/window.py`, `tess-ui:src/tess_ui/appwindows.py`, `tess-ui:src/tess_ui/tokens.py` (width and height classes), `tess-ui:docs/components/window.md` | partly meets: size classes meet AC-APW-1; `Title`, `Borderless`, `Min_Width`, `Min_Height`, `Remember`; second windows and modal dimming layer; no native menu bar; minimum size set per view, floor not enforced (AC-APW-2 not verified); keyboard path for undecorated windows not verified (AC-APW-10) |
| tess-shell | none | not applicable: the shell draws layer surfaces ([[Layer Window]]); its settings app is a tess-ui window |
| tre | `tre:docs/reference/window.md`, `tre:crates/engine-platform/src/lib.rs` | meets AC-APW-3 to 5, 7 by documented behaviour; `min_width` and `min_height` grow the window except where tiled; `parent`, `modal` and centring on a parent are not provided (winit); Wayland gives no window position |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Desktop window with minimum size, drag regions and resize border | MD3 specifies content for window size classes, not the window | [[ADR-0002 Desktop density levels and target sizes]] |
| Minimum pane width 320 dp and the minimum window rule | desktop panes; chapter 10 | [[ADR-0010 Document structure of the specifications]] |

## Sources

- `tre:docs/reference/window.md` (Window controls and state, Title bar and borders, Placement, Hidden windows), `tre:docs/guide/nodes-and-layout.md`, `tre:docs/guide/custom-title-bars.md`.
- `tess-ui:docs/components/window.md`.
- Window size classes verified: https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes. MD3 page (JavaScript app #needs-verification): https://m3.material.io/foundations/layout/applying-layout/window-size-classes.
- WCAG 2.2 SC 2.5.7, 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html.
