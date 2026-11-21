---
title: Window
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, frame, window, keyboard]
related: ["[[Title Bar]]", "[[Application Window]]", "[[Window#Anatomy|Window Root]]", "[[Title Bar|Window Title Bar]]", "[[Application Window#Variants|Window Transparency]]", "[[Spacing and Density#Window size classes|Window Size Classes]]", "[[Spacing and Density|Scale Factor]]", "[[Dialog]]", "[[Scrim]]", "[[Panel and Surface]]", "[[Dock]]", "[[Routed View]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0005 Theme follows the system]]", "[[Title Bar]]"]
---

# Window

> [!info] Summary
> The Window is the operating-system window of an application seen as a view: the root of a window view with a title, a size, a minimum size, an optional custom title bar and optional state that is remembered between runs. Material Design 3 (MD3) describes how content adapts to a window (window size classes, canonical layouts) but has no window element, so this note is Tesserae-specific and rests on the [Window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes) page, the window docs of the engine and the project code. Source of truth in code: see Status in code.

## Purpose

A window frames one application surface: it gives the user a title to find it by, a size the layout can rely on, controls to move, resize, minimise, maximise and close it, and a first focus. The spec fixes what every window of every Tesserae project does so that apps behave alike.

## When to use and not

- Use when: the application needs a top-level OS window (the app's own window, or a second window for preferences or a tool).
- Do not use when: the surface is an overlay inside a window ([[Dialog]], [[Popup]], [[Menu]]); a shell surface that is a layer-shell window (bar, panel, launcher: [[Layer Window]]); a panel inside a window that the user rearranges ([[Dock]]).
- A `Window` is the root of its view: it cannot be nested or embedded. One window view per window. A second window uses a second window view (`tess-ui:docs/components/window.md`).
- The title bar is a separate element: [[Title Bar]]. A window is `Borderless` (the application draws the title bar) or bordered (the OS draws it and the window holds at most a plain header).

## Anatomy

1. Window frame: the OS title bar and borders (bordered) or the 1 dp border drawn by the framework (borderless).
2. Title bar: [[Title Bar]], 40, 32 or 28 dp high by density, the window's drag region (borderless only).
3. Content region: fills the rest, laid out by the view; the content root is a vertical container with the title bar above it.
4. Resize border: an invisible 6 dp band along each edge and corner of a borderless window (not drawn).
5. Window border: a 1 dp outline in `outline_variant`, drawn over everything, taking no presses (borderless, not maximised, not fullscreen, not macOS).
6. Modal dimming layer: [[Scrim]] over a parent window while a modal child window is open.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Bordered | Default on every platform | The OS draws title bar, border, shadow and the window buttons; the view may add a plain header with `Title_Bar` and no buttons |
| Borderless | The application draws its title bar | `Borderless: true`; the app draws [[Title Bar]], a 1 dp border and takes a 6 dp resize border; on macOS the OS keeps a transparent title bar with traffic lights |
| Second window | Preferences, tools | Own view with its own `Window` root; no screens and no routes; closing it leaves the app running |
| Modal second window | Blocks the parent until closed | Parent shows a dimming layer and takes no input |
| Transparent | Rounded or shaped windows | `Transparent: true`, `Blur_Behind`, `Click_Through`: see [[Application Window#Variants|Window Transparency]]; the view draws its own edge |
| Fullscreen | Media and presentation | Borderless, fills the monitor; drag region and resize border are off |

## States

| State | Visual change | Token values |
|---|---|---|
| Active (has OS focus) | Title bar parts at full opacity; keyboard focus ring visible after a key press | title bar opacity 1.0 |
| Inactive | Title bar title, icon and buttons fade; the focus ring hides; focus is kept and restored on activation | title bar opacity 0.6 ([[Title Bar]]) |
| Maximised | Border hidden; resize border off; maximise button shows the restore glyph | border 0 |
| Fullscreen | Border and chrome hidden; drag region and resize border off | not applicable |
| Minimised | Not drawn; the engine may pause drawing while occluded | `pause_when_occluded` true |
| Modal-blocked (parent of a modal child) | Dimming layer over the parent; no input reaches the parent | [[Scrim]] |

## Tokens used

| Part | Role or token |
|---|---|
| Window background | `surface` ([[Colour Roles]]) |
| Border (borderless) | `outline_variant`, 1 dp |
| Dimming layer (modal parent) | `scrim` at 32 percent: [[Scrim]] |
| Title bar | see [[Title Bar]] |
| Window size classes | [[Spacing and Density]] (breakpoints 600, 840, 1200, 1600 dp width; 480, 900 dp height) |
| Shape | square corners; rounded corners only with `Transparent` and a view-drawn edge ([[Shape]]) |

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Title bar height | 40 | 32 | 28 | `density.control_height`; see [[Title Bar]] |
| Minimum window width | 320 dp | 320 dp | 320 dp | Tesserae rule: the floor; a window with panes raises it to the sum of its shown panes' minimum widths ([[10 Layout Overflow and Scrolling]]) |
| Minimum window height | 240 dp | 240 dp | 240 dp | Tesserae rule: title bar plus a usable content area at every density |
| Resize border (borderless) | 6 dp | 6 dp | 6 dp | tess-ui default; see Accessibility for the target-size note |
| Border | 1 dp | 1 dp | 1 dp | `outline_variant` |
| Default size of a second window | 480 by 320 dp | same | same | when its view has no `Window` root (tess-ui) |

The window minimum is the same at every density: density changes control sizes, not what a window must hold. The title bar content needs at most 12 + 20 + 8 + 64 + 8 + 138 = 250 dp (padding, icon, gap, 64 dp of title, gap, three 46 dp buttons), which fits the 320 dp floor.

## Layout and overflow

- The view lays out inside the window in dp; the engine reports the scale factor and the window resizes by device pixels ([[Spacing and Density|Scale Factor]]).
- The window never paints content outside its bounds; a view that does not fit at the minimum size is a defect of the view (AC-WIN-2), not of the window.
- The width and height class are recomputed on every resize and exposed to the view (`app.width_class`, `app.height_class`); pane counts per class are in [[10 Layout Overflow and Scrolling]].
- The window is the outer clip: overlays (tooltips, menus, dialogs) are clipped to it. An overlay that must leave the window uses a popup window ([[Popup]]).

## Behaviour

- Pointer: a press on the drag region of the title bar moves the window (OS move); a double press within 500 ms and 4 px toggles maximise; a press within the resize border resizes the window from that edge or corner and shows the matching resize cursor. A press in the resize border never reaches a node. Details: [[Title Bar]].
- Keyboard: Tab order follows the view order. The title bar is the first child of the window, so its own controls and then its three window buttons come before the content region in Tab order (see [[Title Bar]]). Alt+F4 or the platform close shortcut closes the window as the user's close does. In a borderless window the system menu is on by default ([[ADR-0015 System menu default in borderless windows]]) and opens with Alt+Space, with a secondary press on the title bar, and from the title bar icon (see AC-WIN-10).
- Focus on open: the first focusable control of the content region receives keyboard focus, in document order, unless the view names an initial control. The focus ring is not shown until the first key press ([[Focus Ring]]). Focus does not start on a window button.
- Close: `close_requested` fires first; a listener may cancel it (a "save changes?" check). Closing the app's own window closes every second window; closing a second window leaves the app running.
- Modal second window: the parent takes no pointer or key input until the child closes; Tab does not leave the child; on close, focus returns to the control that had focus in the parent when the child opened.
- Remembered state: `Remember` keeps size, place (where the platform lets an app say: not Wayland) and maximised state between runs; a maximised window keeps the size it had before.
- Touch: window buttons keep their 46 dp width; in a touch context the resize border grows to 12 dp #needs-verification (a design choice, not found in a source).

## Tooltip and overlay behaviour

- The window itself shows no tooltip. Each title bar window button shows its own tooltip on the button only (Minimise, Maximise or Restore, Close): [[Title Bar]], [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]].
- A modal child window dims the parent with a [[Scrim]]; the parent's overlays close when the modal window opens.

## Motion

- Window state changes (maximise, restore, minimise) are animated by the OS; the framework adds none.
- The title bar fade between active and inactive is not animated (the opacity changes in the frame that follows the focus event).
- With reduced motion on ([[Accessibility Rules]]) nothing in the window animates beyond the OS's own behaviour.

## Accessibility

- The window's accessible name is its `Title`; it updates when the title changes (AC-WIN-11). A window name that is empty is a defect.
- Window moves and resizes are done by the OS; a borderless window leaves the OS's keyboard route for moving and resizing reachable: the system menu (Alt+Space, on by default per [[ADR-0015 System menu default in borderless windows]]) and the compositor's own keys on Linux. Resizing by dragging the border has the OS route as its alternative, per WCAG 2.2 SC 2.5.7 Dragging Movements, which exempts functionality "determined by the user agent and not modified by the author" ([WCAG 2.2 SC 2.5.7](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html)).
- The 6 dp resize border is below the 24 dp desktop minimum target ([[ADR-0002 Desktop density levels and target sizes]]). Per [[ADR-0014 Window resize border and splitter alternative]] it stays 6 dp and stays with the platform resize path: the window manager's keyboard resize and the title bar maximise and restore controls are the equivalent control for WCAG 2.2 SC 2.5.8 ([Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)).
- Focus order and first focus follow WCAG 2.2 SC 2.4.3 Focus Order ([focus order](https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html)).
- Announcements: `Window.announce` goes through the window that owns the screen reader connection; a screen change inside a window is announced by [[Routed View]].
- Contrast: every pair in the window follows [[Colour Roles]]; the 1 dp border carries no information and is exempt from 3:1.

## Dark and light

The window background is `surface`; it follows the theme of the application, which follows the system by default ([[ADR-0005 Theme follows the system]], [[Theme Following the System]]). The border colour `outline_variant` resolves from the scheme. The OS title bar of a bordered window follows the OS, not the application.

## Defaults

| Setting | Default |
|---|---|
| Borderless | false |
| Minimum size | 320 by 240 dp (tess-ui: 0 by 0, no limit) |
| Resize border | 6 dp when borderless, 0 when bordered; off on macOS, maximised and fullscreen |
| Window border | 1 dp, `outline_variant`, borderless only |
| Remember | off |
| System menu | on in borderless windows ([[ADR-0015 System menu default in borderless windows]]); a project may turn it off in its own decision record (tess-ui: off, fails AC-WIN-10) |
| Initial focus | first focusable control of the content |
| Title bar height | 40 dp at `default` |
| Second window size | 480 by 320 dp |
| Modal parent dimming | [[Scrim]] at 32 percent |

## Acceptance criteria

- [ ] AC-WIN-1 (token test): the application's window options carry `min_width` at least 320 and `min_height` at least 240 by default. Pass: both values read from the window are at or above the floor, in dp, for a window created with no explicit minimum.
- [ ] AC-WIN-2 (geometry check): after the window is resized to 320 by 240 dp (and requested to 100 by 100, which the minimum grows back), every focusable node and every title bar button lies inside the window rectangle, the title bar buttons are fully visible, and no node overlaps another interactive node. Pass: zero nodes outside and zero overlaps at scale 1.0 and 2.0.
- [ ] AC-WIN-3 (token test): the window's background is the role `surface` in light and dark and holds no colour literal. Pass: the resolved fill equals the scheme's `surface`.
- [ ] AC-WIN-4 (scripted input): in a borderless, not maximised window, a press within 6 dp of each of the four edges and four corners resizes (the press is not delivered to any node and the resize cursor shows); a press 7 dp inside reaches the node under it. With the window maximised or fullscreen a press at the edge is delivered to the node. Pass: delivered events equal the list in each of the 8 positions and both modes.
- [ ] AC-WIN-5 (pixel check): a borderless window shows a 1 dp line in `outline_variant` on all four edges (pixel colour within 2 channel values at the edge pixel row and column); with the window maximised or fullscreen the pixel equals the content colour. Pass in light and dark.
- [ ] AC-WIN-6 (scripted input): after the first frame of a window whose content has a focusable control, the focused node is the first focusable node of the content region in tree order (or the view's named initial control), never a title bar button, and `focus_visible` is false (no ring pixels) until the first key press, after which the ring shows ([[Focus Ring]]). Pass: focused node id and ring pixel state match.
- [ ] AC-WIN-7 (scripted input): on a simulated window `active` false the title bar title, icon and buttons read opacity 0.6 and the focus ring is hidden; on `active` true they read 1.0 and the ring shows again if the last input was a key, within one frame. Pass: values equal.
- [ ] AC-WIN-8 (scripted input): a `close_requested` listener that cancels keeps the window open (window still open after one frame); without the cancel the window closes; closing a second window leaves the app running; closing the app's own window closes every second window. Pass: open-window list equals the expected list in each of three runs.
- [ ] AC-WIN-9 (scripted input): with a modal second window open, a click and a key sent to the parent window reach no node of the parent; the parent shows the dimming layer (pixel at the parent centre differs from the unmodal frame by the scrim blend); Tab in the child cycles within the child; after the child closes focus is on the parent control that had it when the child opened. Pass: each of four conditions holds.
- [ ] AC-WIN-10 (scripted input): in a borderless window the system menu is on by default ([[ADR-0015 System menu default in borderless windows]]): `system_menu` reads true when the window options set nothing; the title bar icon, a secondary press on the drag region and Alt+Space each open the platform window menu (Restore, Move, Size, Minimise, Maximise, Close), and the secondary press ends with `pointer_cancel`. Pass: the setting reads true and the menu request is raised from each of the three routes; where the platform has no menu nothing opens. A project that turns the menu off has a decision record. Hand check on a real compositor (not automated).
- [ ] AC-WIN-11 (AT tree assertion): the window's accessible name equals its `Title`; after the title changes the name equals the new title within one frame. Pass: property equality #needs-verification (the engine exposes the OS window title through the platform; a tree assertion may need a platform-side check).
- [ ] AC-WIN-12 (scripted input): a window with `Remember` set, closed and reopened with the same name, opens at the same size (and place where the platform allows, not on Wayland); a window closed maximised reopens maximised and restores to the size it had before maximising. Pass: sizes equal to the dp.
- [ ] AC-WIN-13 (scripted input): `width_class` and `height_class` change on the frame after a resize crosses a breakpoint: widths 599 and 600 give compact and medium; 839 and 840 medium and expanded; 1199 and 1200 expanded and large; 1599 and 1600 large and extra-large; heights 479 and 480 compact and medium; 899 and 900 medium and expanded (also AC-DEN-10).
- [ ] AC-WIN-14 (review): each window option that a platform refuses (`Transparent`, `Blur_Behind`, `Click_Through`, window icon, `always_on_top`) is reported to the application by name; no option is ignored silently. Pass: reviewer finds the report path for each option and records the platform matrix (window icon only on Windows and X11; blur only on Wayland with the KDE blur protocol and on macOS).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/spec/window.py` (`Window` root, `_KEYS`, `min_width`, `min_height`, `remember`), `tess-ui:src/tess_ui/app.py` (`min_width`, `min_height`, `resize_border`, `system_menu`, `window_border`), `tess-ui:src/tess_ui/appwindows.py`, `tess-ui:docs/components/window.md`, tests `tess-ui:tests/test_window_view.py`, `tess-ui:tests/test_second_window.py`, `tess-ui:tests/test_window_border.py`, `tess-ui:tests/test_app_window.py` | Partly meets. Fails AC-WIN-1: `min_width` and `min_height` default to 0 (no limit). AC-WIN-6 fails: no code moves focus to the first control when an app window opens (the only `focus_first` is for overlays, `tess-ui:src/tess_ui/composed.py` line 1023). AC-WIN-10 fails: `system_menu` is off by default. Meets in design, per docs and tests: border 1 dp `outline_variant`, resize border 6, hidden when maximised or fullscreen (AC-WIN-4, AC-WIN-5), second windows, modal blocking (`test_a_modal_window_blocks_its_parent_until_it_closes`), `close_requested` cancel, `Remember`. Focus return to the parent control after a modal window closes (AC-WIN-9) is not found in `tess-ui:tests/test_second_window.py` and is not run. Not built: a native menu bar |
| tess-shell | `tess-shell:src/tess_shell/surfaces/` | Not applicable: shell surfaces are layer-shell windows ([[Layer Window]]); no application window with a title bar. The configuration app (`tess-ui:apps/shell_config`) has no `Window` root or `Title_Bar` and uses the OS frame |
| tre | `tre:docs/reference/window.md` (`decorations`, `min_width`, `min_height`, `resize_border`, `system_menu`, `maximized`, `active`, `fullscreen`, `window_region`), `tre:crates/engine-platform/src/lib.rs` | Exists. A window below its minimum is grown to it, except when maximised, fullscreen or held at its size by a tiling compositor (Wayland may report a window as tiled, COSMIC reports every window so), so AC-WIN-2 cannot assume the minimum is reached on tiled compositors. Drag region, double-click maximise and the resize border are exercised by `simulate` without a display; move, resize and the window menu need a real display |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A window element exists at all (MD3 has none; it covers window size classes only) | desktop applications own an OS window and need rules for it | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Window minimum size 320 by 240 dp at every density | no MD3 value; 320 dp is the pane minimum of [[10 Layout Overflow and Scrolling]] | [[ADR-0002 Desktop density levels and target sizes]] |
| Resize border 6 dp, below the 24 dp target minimum | the platform resize path (window manager keyboard resize, title bar maximise and restore) is the equivalent control for WCAG 2.5.8 | [[ADR-0014 Window resize border and splitter alternative]] |
| Initial focus on the first content control | desktop keyboard-first use; MD3 gives no window focus rule | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- Window size classes (breakpoints 600, 840, 1200, 1600 dp width; 480, 900 dp height), verified: https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes. The MD3 page https://m3.material.io/foundations/layout/applying-layout/window-size-classes is a script-rendered app and returns no text.
- WCAG 2.2 SC 2.5.7 Dragging Movements (verified 2026-11-21): https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- WCAG 2.2 SC 2.4.3 Focus Order (verified 2026-11-21): https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html
- WCAG 2.2 SC 4.1.3 Status Messages (verified 2026-11-21): https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html
- Engine window docs: `tre:docs/reference/window.md` (Window controls and state, Title bar and borders), `tre:docs/guide/custom-title-bars.md`.
- tess-ui docs: `tess-ui:docs/components/window.md`, `tess-ui:docs/guide/custom-title-bars.md`, `tess-ui:docs/guide/apps-and-screens.md` (The window), `tess-ui:docs/guide/windows-and-docks.md`.
- Not verified: the 12 dp touch resize border and the 320 by 240 dp floor are Tesserae design choices with no MD3 source #needs-verification.
