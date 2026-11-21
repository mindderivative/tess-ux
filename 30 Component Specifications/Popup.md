---
title: Popup
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, overlay, popup, shell, owner-feedback]
related: ["[[12 Overlays]]", "[[Menu]]", "[[Tooltip]]", "[[Dialog]]", "[[Panel and Surface]]", "[[Text Field]]", "[[List]]", "[[Scrollbar and Scroll Container]]", "[[Owner Feedback 2026-11-20]]", "[[Elevation]]", "[[Shape]]", "[[Colour Roles]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0003 Scrollbar rule]]"]
---

# Popup

> [!info] Summary
> A popup is a temporary, non-modal surface anchored to a rectangle of another element; it holds a menu, a flyout or a tooltip and closes on an outside click or Escape. The Material Design 3 counterpart is the surface of a [Menu](https://m3.material.io/components/menus/overview) (container `surface_container`, elevation level 2); the Tesserae shell has a Popup surface type of its own. Source of truth in code: see the last section.

## Purpose

A popup shows short-lived content next to the thing that opened it without leaving the current context: a tray menu, a context menu, a clock calendar, a search-and-launch list. It must be easy to open, easy to leave, and must never steal or lose the keyboard unexpectedly.

## When to use and not

- Use when: the content is transient, anchored to a control, and dismissed by a click elsewhere or Escape.
- Do not use when: the content is a hint (use [[Tooltip]]); the content must be answered before anything else (use [[Dialog]], modal); the surface stays open and holds state (use a Panel, see [[Panel and Surface]]); the content is a list of commands only (use [[Menu]], which is a popup with the menu behaviour on top).
- A launcher or menu opened by a global shortcut or an IPC command is not a popup: it has no user-action serial for a keyboard grab, so it is a Panel on the overlay layer with exclusive keyboard ([[Panel and Surface]]).

## Anatomy

1. Anchor rectangle: the caller's rectangle, in the host surface's coordinates.
2. Body: the visible container, placed against the anchor.
3. Shadow margin: transparent area around the body that holds the shadow; it is not part of the placed shape and takes no input.
4. Content: menu items, text, a text field, a list.
5. Opener: the control that had focus when the popup opened; focus returns to it on close.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Menu popup | Commands | Focused, arrows move, see [[Menu]] |
| Flyout | Calendar, small form, a search field with results | Focused; may contain a text input; default container `surface_container`, shape `medium` |
| Tooltip popup | Hover hint in a layer-surface host | Not focused, closes on pointer exit; rules in [[Tooltip]] |
| Submenu | Child of a menu | Hangs off the parent popup; closing the parent closes it; one level open at a time |

## States

| State | Visual change | Token values |
|---|---|---|
| Closed | Nothing exists (the shell creates the window on open and destroys it on close) | not applicable |
| Building | Content measured off screen, window created and placed; nothing visible | not applicable |
| Open | Body and shadow drawn | container `surface_container`, elevation level 2 |
| Closing | Removed in one frame (no exit animation required) | not applicable |

Item states (hover, focus, pressed) belong to the content ([[Menu]], [[List Item]]).

## Tokens used

| Part | Role or token |
|---|---|
| Body colour | `surface_container` |
| Body shape | menu: `extra_small` (4 dp); flyout: `medium` (12 dp) |
| Elevation | level 2 (3 dp in MD3 numbers), shadow colour role `shadow` |
| Scrim | none (a popup is not modal) |

See [[Colour Roles]], [[Shape]], [[Elevation]]. Values verified in Sources.

## Sizing and density

Popup size is the content size (AUTO) clamped to a maximum width and height set per project (the shell defaults are 300 by 400 dp, Tray_Menu 60 percent of the output height). Content beyond the maximum scrolls with the scrollbar rule ([[ADR-0003 Scrollbar rule]], [[Scrollbar and Scroll Container]]). Row heights follow the density level ([[Menu]], [[Spacing and Density]]). The shadow margin is at least blur plus spread plus offset of the shadow, so the shadow is not cut.

## Dimensions and defaults

The popup draws a body and a shadow margin; the content owns the rest (menu rows in [[Menu]], a form in a flyout). The shadow margin is the largest of blur plus spread plus the offset over the two shadows of the level: level 2 gives max(2+0+1, 6+2+2) = 10 ([[Elevation]]). The flyout padding is a Tesserae choice #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| body | height | - | N/A: content-sized, clamped to a project maximum (shell default 400, tray menu 60 percent of the output height) | N/A: same as the default level | N/A: same as the default level | [[Popup]] Sizing and density | tess-ui: yes (style height); tess-shell: yes (Height, Max_Height); tre: yes (height) |
| body | min width | - | N/A: the content sets it (a menu 112, see [[Menu]]) | N/A: same as the default level | N/A: same as the default level | [[Menu]] | tess-ui: yes (style min_width); tess-shell: via Min_Width on the content block (Popup has no Min_Width); tre: yes (min_width) |
| body, menu | padding | - | N/A: the menu content sets its own container padding (8, 4, 4) | N/A: same as the default level | N/A: same as the default level | [[Menu]] | tess-ui: yes (style padding); tess-shell: via Padding on the content block (Popup Padding is not built); tre: yes (padding) |
| body, flyout | padding | `space.4`, `space.3`, `space.2` | 12 12 12 12 | 8 8 8 8 | 4 4 4 4 | design choice, proposed ADR: panel and flyout padding per density, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style padding); tess-shell: via Padding on the content block (Popup Padding is not built); tre: yes (padding) |
| shadow margin | margin | - | 10 | 10 | 10 | [[Elevation]] (level 2 margin rule), tre:docs/reference/layer-window.md | tess-ui: n/a: overlay layers draw inside the window, no shadow margin; tess-shell: yes (Shadow_Bleed); tre: yes (margin) |
| body | gap | - | 0 | 0 | 0 | [[Popup]] Layout and overflow (`Gap`; the shell uses 4 for tray menus: tess-shell:src/tess_shell/schema/default_popups.py) | tess-ui: yes (style gap); tess-shell: yes (Gap, the distance to the opener); tre: yes (gap) |
| body | border width | - | 0 | 0 | 0 | [[Popup]] Tokens used (no border drawn) | tess-ui: yes (style border_width); tess-shell: yes (Border_Width in the Popup Style); tre: yes (border_width) |
| body | border color | - | N/A: the popup draws no border; the shadow separates it | N/A: same as the default level | N/A: same as the default level | [[Popup]] Tokens used | tess-ui: yes (style border_color); tess-shell: yes (Border_Color in the Popup Style); tre: yes (border_color) |
| body, menu | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius in the Popup Style); tre: yes (corner_radius) |
| body, flyout | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius in the Popup Style); tre: yes (corner_radius) |
| body | font | - | N/A: the popup draws no text; the content sets the font | N/A: same as the default level | N/A: same as the default level | [[Popup]] Anatomy | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| body | icon size | - | N/A: the popup draws no icon; the content sets the size | N/A: same as the default level | N/A: same as the default level | [[Popup]] Anatomy | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| body | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation in the Popup Style); tre: yes (shadows) |

## Layout and overflow

- Placement: the body edge meets the anchor edge at `Gap` dp (default 0; the shell uses 4 for tray menus), aligned by `Alignment` (`START`, `CENTER`, `END`). The shadow margin is ignored for placement.
- Flip: when the body would leave the output (or window) on the placement axis and fits on the opposite side, the popup opens on the opposite side (under a bottom bar it opens upward with no setting). Slide: it then slides along the other axis to stay inside the output.
- The body always lies inside the output (window) rectangle.
- Text and rows truncate with ellipsis at the maximum width; they do not wrap unless the content declares wrap ([[10 Layout Overflow and Scrolling]]).

## Behaviour

- Pointer: a press outside the popup dismisses it and is consumed: the press does not reach the element underneath and does not activate the opener again. A press on another surface of the same application closes a focused popup and is consumed the same way. A press on the shadow margin passes through to what is underneath (the popup's input region is its body). A press inside the popup never dismisses a popup beneath it (submenus keep their parent open).
- Keyboard: Escape closes the innermost open level (a submenu closes alone; the root closes and focus returns to the opener). Opening moves keyboard focus into the popup; closing returns it to the opener, or to the next logical element when the opener no longer exists.
- Text input rule (the Launcher rule): a popup that takes text input keeps keyboard focus while the pointer presses anywhere inside the popup, including areas that are not focusable. A press on a non-focusable area leaves focus on the text input. The mechanism that dismisses the popup on an outside click (click catcher, input grab) must not itself take keyboard focus; the popup that was shown keeps the keyboard from its first frame (no keyboard loss within the first 500 ms and while open).
- Open and close: opening an already open popup from the same opener closes it (toggle) and does not reopen; at most one popup is open at a time, except a submenu chain (a parent and its open children); opening another closes the first.
- Touch: a tap outside dismisses; the tap is consumed.

## Tooltip and overlay behaviour

- Layer route: inside an application window a popup is a layer over the content (`show_layer`), clipped to the window by the engine. In a layer-surface host (a bar) a layer is clipped to the host surface, so a popup that must extend past the bar uses a popup window (`xdg_popup` through tre `PopupWindow`, Wayland layer-shell only, size fixed for its life, needs an open layer or popup window as parent). The overlay route (a transparent output-sized layer window that draws the popup with `show_layer`) is available for popups that must span outputs; it costs hundreds of MB while open, so it is the exception ([[12 Overlays]]).
- The outside click on the popup-window route is delivered to the popup's grab and consumed ("the click is the popup's"); on the overlay route and in an application window it is delivered as `dismiss` to the layer and goes no further. Both consume it.
- A tooltip never opens over a focused popup.
- Focus on open: into the popup (first item for a menu, the text input for a launcher). Focus on close: the opener, with its focus ring state preserved.
- A grab (keyboard and pointer) needs a fresh user action: a focused popup opens in response to input on a shell surface; a global shortcut or IPC cannot grant it (use a Panel).

## Motion

No animation is required. Where a project animates, a fade of 100 ms ([[Motion]] `short2`) is the recommended bound; popups have no slide because the compositor places them. With reduced motion on, open and close are instant #needs-verification-as-design-choice.

## Accessibility

- The popup window is one more window of the application in the accessibility tree; its root node has a role (`menu`, `dialog` for a flyout with input, `listbox` for a result list) and an accessible name set by the author.
- Keyboard focus moves in on open and returns on close (WAI-ARIA Authoring Practices menu pattern: Escape closes the menu and returns focus to the invoking element; see Sources).
- No keyboard trap (WCAG 2.2 SC 2.1.2): Escape always leaves; a text-input popup is dismissed by Escape.
- A popup does not obscure the focused element of its opener (WCAG 2.2 SC 2.4.11 Focus Not Obscured, minimum): the popup is placed beside the anchor, not over it.

## Dark and light

All colours are roles ([[Theme Following the System]]); the shadow colour is the `shadow` role. The body is opaque in both schemes.

## Defaults

| Setting | Default |
|---|---|
| Attach, Alignment | `BOTTOM`, `START` |
| Adjust | flip on Y, slide on X |
| Gap | 0 dp (tray menus 4 dp) |
| Maximum size | 300 by 400 dp (shell) |
| Focus | on (tooltip popups off) |
| Shape, colour, elevation | 4 dp (menu) or 12 dp (flyout), `surface_container`, level 2 |

## Acceptance criteria

Scripted input uses the toolkit's simulated pointer and key events and frame clock ([[Test Method]]); items marked manual are hand checks on a real compositor.

- [ ] AC-POP-1 (scripted input, Escape): open a focused popup with a submenu open; Escape closes the submenu only (popup count 1); Escape again closes the root (count 0) and the focused node is the opener. Both within one frame (17 ms). Also as a manual hand check on KWin (Escape is not verified on KWin 6.8.1 after the input-region fix).
- [ ] AC-POP-2 (scripted input, outside click): with a popup open over a button B, a pointer press and release on B closes the popup and B's click handler runs 0 times. A press on empty window area closes it and nothing underneath reacts. Pass: popup count 0 and handler count 0.
- [ ] AC-POP-3 (scripted input, toggle): with a popup open, a press on its opener closes it; the popup does not reopen within 1000 ms. Pass: popup count 0 at t+1000 ms.
- [ ] AC-POP-4 (scripted input, other surface): with a focused shell popup open, a press on another surface of the same application (bar, panel) closes it and the opener's click is swallowed for 1000 ms. Pass: popup count 0 and the opener did not reopen it.
- [ ] AC-POP-5 (scripted input, focus on open and close): after open, the focused node is inside the popup within one frame; after close, the focused node is the opener and the opener's focus-visible state equals its state before opening. Pass: node ids match.
- [ ] AC-POP-6 (scripted input, Launcher rule): in a popup or panel with a text input, focus the input, press the pointer on a non-focusable area inside the popup (title, padding, empty list area), then type "abc". Pass: the input still has focus after the press and its value ends with "abc".
- [ ] AC-POP-7 (scripted input, event log, keyboard retention, owner feedback on the Launcher): show the popup, type "abc" within 50 ms of the first frame, and sample the keyboard-gained and keyboard-lost events for 500 ms after show. Pass: the keyboard-lost event count is 0 and the input value is "abc". The click-catcher or grab that dismisses on outside click is active during this test.
- [ ] AC-POP-8 (scripted input, input region): press at a point 2 dp outside the body and inside the shadow margin, over a button of the window underneath. Pass: the underlying button receives the press. The popup's input region equals its body rectangle ±1 px (geometry check).
- [ ] AC-POP-9 (geometry check, placement): for each of the four attach sides at the centre of an output and at each edge, the distance between the body edge and the anchor edge equals `Gap` ±1 px when the popup fits, regardless of shadow margin; when it does not fit it opens on the opposite side; the body rectangle is inside the output rectangle in all cases.
- [ ] AC-POP-10 (geometry check, size): with AUTO size, the body size equals the content size ±1 px; content taller than the maximum makes the body exactly the maximum and a vertical scrollbar thumb appears ([[ADR-0003 Scrollbar rule]]).
- [ ] AC-POP-11 (scripted input, one at a time): open popup P1, then call popup P2 (not a submenu of P1). Pass: popup count 1 and the open one is P2. Opening a submenu leaves count 2 (parent and child); closing the parent closes the child.
- [ ] AC-POP-12 (geometry check, clipping): a popup 200 dp tall opened from a 32 dp high bar is fully visible (pixel check at its four corners reads the body colour); it uses the popup-window route.
- [ ] AC-POP-13 (token test, look): a menu popup body has fill `surface_container`, radius 4 dp, elevation level 2, no scrim; a flyout has radius 12 dp. Pass: values equal the tokens, and the pixel at the body's top-left padding reads `surface_container` of the active scheme with alpha 255.
- [ ] AC-POP-14 (scripted input, lifetime): closing or removing the opener's surface, or removing its monitor, closes the popup within one frame and logs the reason.
- [ ] AC-POP-15 (AT tree assertion): the popup root has a role and a non-empty accessible name; the tooltip popup root is hidden from the tree and its text is the trigger's description.
- [ ] AC-POP-16 (review): a launcher opened by shortcut or IPC is a Panel on the overlay layer with exclusive keyboard, not a focused popup.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/composed.py` (`_wire_overlays`, `_show_layer`, `_dismiss_layer`), `tess-ui:src/tess_ui/overlays.py` (`Popover`, `Menu`), `tess-ui:docs/guide/overlays.md`, tests `tess-ui:tests/test_overlay_state_escape.py`, `tess-ui:tests/test_anchored_overlay.py`, `tess-ui:tests/test_overlay_widget.py` | Partly meets. `Overlay` shows a layer, Escape and an outside press dismiss it (`Dismissible`, `On_Dismiss`), the engine consumes the outside press, focus returns to where it was, `Focus_First` is off by default. Meets AC-POP-1, AC-POP-2 in part; AC-POP-5 in part (focus into the popup only with `Focus_First`); AC-POP-9 in part (flip and shift by engine, no explicit `Gap` in the default, corner placements are not flipped); AC-POP-11 not enforced (layers stack in show order, no one-at-a-time rule); AC-POP-6, AC-POP-7, AC-POP-8, AC-POP-12 not applicable (no popup window or click catcher; layers are clipped to the window); AC-POP-13 meets for Menu (`Menu_Stylesheet.tdl`: `surface_container`, radius 4, elevation 2), Popover radius 12. |
| tess-shell | `tess-shell:src/tess_shell/surfaces/popup.py` (`Popups`, `_key`, `surface_pointer_down`, `choose_attach`, `_listen`), `tess-shell:src/tess_shell/schema/blocks.py` (Popup), `tess-shell:src/tess_shell/schema/default_popups.py`, vault `shell-vault:40 Specifications/Surfaces/Popup.md`, tests `tess-shell:tests/test_popup.py`, `tess-shell:tests/test_popup_live.py` | Partly meets. Meets AC-POP-3 and AC-POP-4 (`SWALLOW_MS` 1000), AC-POP-8 (`input_region="geometry"` on a shadowed popup, owner retest 2026-11-07 passed), AC-POP-9 (`choose_attach` flips by hand, compositor adjust as backup; owner faults on a top bar placement and a 30 px edge gap, 2026-11-06, status after fixes not re-verified), AC-POP-10 (`measure`, `Max_Width` 300, `Max_Height` 400, scrolls), AC-POP-11 (one `current` popup plus submenu chain), AC-POP-12 (popup window route). AC-POP-1 not verified: the shell closes a focused popup on Escape itself (`_key`) because the grab did not on KWin; no test found, not verified on real KWin. AC-POP-6 and AC-POP-7 fail on KWin for the Launcher as built in M7k (PR #108): the click catcher (`PopupWindow(grab=True)`) took the keyboard, the Launcher received "keyboard gained" and 5 ms later "keyboard lost" at every show, and clicks off the field closed it; failed the owner hand check of 2026-11-20; revert PR #111 (merge state not checked here). AC-POP-5 meets (opener recorded, focus returns, Accessibility rule 12). AC-POP-13 look: Menu module uses `surface_raised`, `Corner_Radius` 8 literal, not the role mapping. |
| tre | `tre:docs/reference/layer-window.md` (PopupWindow), `tre:docs/reference/layers.md`, `tre:docs/guide/menus-from-a-bar.md` | Provides the mechanisms: `PopupWindow(parent, anchor_rect, anchor, gravity, constraint_adjustment, offset, grab, geometry, input_region)`, `dismiss` event, layer flip and shift. Engine has no menu node, no click-outside event by design (TRE-REQ-024); KWin behaviour of the grab-dismissal trick is not verified (sway accepts it). |

Evidence: Launcher failure and the keyboard grab are recorded in `shell-vault:00 Home/M7 Build Log.md` (M7k, 2026-11-20); they feed AC-POP-6 and AC-POP-7. The popup faults of 2026-11-06 are in `shell-vault:40 Specifications/Surfaces/Popup.md`. The tooltip feedback F2, F8 and F9 are in [[Owner Feedback 2026-11-20]]; their rules are in [[Tooltip]].

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A popup that takes text input is allowed; MD3 menus hold commands only | Launcher and search flyouts; the text input rule is needed because the outside-click mechanism broke typing on KWin | [[ADR-0001 MD3 role names are the specification vocabulary]] (vocabulary); behaviour recorded here |
| The popup-window route (`xdg_popup`) and its grab have no MD3 counterpart | MD3 is platform-agnostic; Wayland layer-shell hosts clip layers to the surface | [[Deviations from MD3]] |
| Outside click is consumed | MD3 menus dismiss on outside tap; whether the tap is consumed is not specified in the sources read | [[Deviations from MD3]] |

## Sources

- Menu container tokens (colour `surface-container`, elevation `level2`, shape `corner-extra-small`, shadow colour `shadow`), verified: `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-menu.scss`.
- Material Web menu: closes on focusout and on Escape, restores focus to the previously focused element unless `skip-restore-focus`, default focus first item: `https://github.com/material-components/material-web/blob/main/menu/internal/menu.ts`.
- WAI-ARIA Authoring Practices, menu and menubar pattern (Escape closes the menu and returns focus to the invoking element; Tab and Shift+Tab move focus out and close all menus): `https://www.w3.org/WAI/ARIA/apg/patterns/menubar/`.
- WCAG 2.2 Understanding SC 2.1.2 No Keyboard Trap: `https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html`. SC 2.4.11 Focus Not Obscured (Minimum): `https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html`.
- tre layers: placement flip and shift, `dismiss` event, outside press goes no further, each layer its own focus scope, hide returns focus: `tre:docs/reference/layers.md`.
- tre popup window and the overlay route cost: `tre:docs/reference/layer-window.md`, `tre:docs/guide/menus-from-a-bar.md`.
- Shell: `shell-vault:40 Specifications/Surfaces/Popup.md`, `shell-vault:40 Specifications/Surfaces/Surface Types.md`, `shell-vault:00 Home/M7 Build Log.md`.
- xdg-shell `xdg_popup.grab`: an explicit grab is dismissed when the user clicks outside, uses the keyboard, or the compositor denies the grab; the request must be used in response to a user action, with that event's serial; verified: `https://wayland.app/protocols/xdg-shell`. WCAG 2.2 SC 2.5.8 Target Size (Minimum), at least 24 by 24 CSS pixels: `https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html`.
