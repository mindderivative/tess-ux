---
title: Title Bar
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, frame, title-bar, window, keyboard]
related: ["[[Window]]", "[[Title Bar|Window Title Bar]]", "[[Application Window]]", "[[Top App Bar]]", "[[Icon Button]]", "[[Tooltip]]", "[[Dialog]]", "[[State Layers]]", "[[Focus Ring]]", "[[Colour Roles]]", "[[Typography]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[Window]]"]
---

# Title Bar

> [!info] Summary
> The Title Bar is the window's own strip when the application draws it: icon, title, the application's own controls and the three window buttons (minimise, maximise or restore, close), and the region the user drags to move the window. MD3's [top app bar](https://m3.material.io/components/top-app-bar/overview) sits inside a window and is not a title bar, so this element is Tesserae-specific. Source of truth in code: see Status in code.

## Purpose

A title bar names the window, carries the window controls and gives a large target to move the window by. A framework-drawn bar lets the application put its own controls (tabs, search, menu) into the bar and follow its theme in light and dark.

## When to use and not

- Use when: the window is `Borderless` and the application draws its own title bar; or a header strip of a dialog or sheet needs a title and a close button (`Buttons: [dismiss]`).
- Do not use when: the window has the OS title bar (the OS draws it; a view may add a plain header without buttons); a bar inside the window content that is not the window's drag region ([[Top App Bar]]); the toolbar of an editor ([[Toolbar]]).
- The window buttons are never duplicated by a second set in the view.

## Anatomy

1. Container: full window width, height per density, the drag region.
2. Inset (macOS only): room at the start for the OS traffic lights; width from the window's `titlebar_inset`, 0 elsewhere.
3. Icon (optional): 20 dp.
4. Title: one line, `title_small` (14/20, weight 500); `title_dense` (13/18) at dense.
5. Content: the application's own controls between the title and the buttons, growing to push the buttons to the end.
6. Window buttons: minimise, maximise or restore, close; each 46 dp wide and as high as the bar; 16 dp glyph centred; hidden when the OS shows its own controls.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Window bar | Borderless window | Drag region; minimise, maximise, close; fades while the window is inactive |
| Surface bar | Header of a dialog or sheet | `Buttons: [dismiss]`: one 46 dp button that closes the nearest overlay up the tree; no drag region (a press does not move the window), no inset, no fade; in no overlay the button does nothing |
| Plain header | Bordered window (OS title bar) | `Title_Bar` without buttons: title and icon only |

## States

Applies to each window button. The bar itself has two states: active and inactive.

| State | Visual change | Token values |
|---|---|---|
| Bar active | Title, icon and buttons at full opacity | opacity 1.0 |
| Bar inactive | Title, icon and buttons fade | opacity 0.6 |
| Button rest | Glyph only | glyph `on_surface` |
| Button hover | State layer over the whole button | `on_surface` at 8 percent; close: `error` at 8 percent ([[ADR-0009 State layer percentages]]) |
| Button focus (keyboard) | State layer plus inward focus ring | layer 10 percent ([[ADR-0013 Focus and pressed state layer 10 percent]]); ring 3 dp `secondary`, inward ([[Focus Ring]]) |
| Button pressed | State layer | 10 percent; close in `error` |
| Button disabled | Not applicable: a window button is omitted instead of disabled (maximise is omitted for a fixed-size window) | not applicable |
| Maximised | Maximise button shows the restore glyph | glyph swap, one frame |

## Tokens used

| Part | Role or token |
|---|---|
| Container | `surface` |
| Title, icon, glyphs | `on_surface` |
| Title type | `title_small` ([[Typography]]); `title_dense` at dense |
| Bar border to content | none; the window border is [[Window]] (`outline_variant` 1 dp) |
| Close hover and pressed layer | `error` ([[Colour Roles]]) |
| Other hover, focus, pressed layers | `on_surface` ([[State Layers]]) |
| Spacing | start padding `density.row_padding_x`; gap `density.icon_label_gap` ([[Spacing and Density]]) |
| Shape | square; the buttons have no rounded container |

The close layer is `error` and not `error_container`, because `error_container` is too pale at an 8 percent layer (`tess-ui:src/tess_ui/spec/title_bar.py`, comment in `_button`).

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Bar height | 40 | 32 | 28 | `density.control_height`; tess-ui is 40 at all levels today |
| Window button width | 46 | 46 | 46 | the Windows desktop size, equals no MD3 value |
| Window button height | bar height | bar height | bar height | hit area 46 by 40, 46 by 32, 46 by 28, at least 24 by 24 at every level |
| Glyph | 16 | 16 | 16 | centred in the button |
| Icon | 20 | 20 | 20 | |
| Start padding | 12 | 8 | 4 | `density.row_padding_x` |
| Gap (icon, title, content) | 8 | 8 | 4 | `density.icon_label_gap` |
| Inactive opacity | 0.6 | 0.6 | 0.6 | |

A project sets the bar height with `Style { Height: ... }`; every part follows (glyphs stay centred). A height outside the three-value set is a defect (AC-DEN-11).

## Dimensions and defaults

Bar height at each density is derived from the control heights (`density.control_height` 40, 32, 28), which the Sizing table already states; MD3 has no title bar. The window buttons are 46 dp wide (the Windows desktop size) and as high as the bar.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| Bar container | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], [[Title Bar]] Sizing | tess-ui: yes (TitleBar style height); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Bar container | padding | `density.row_padding_x` | 0 0 0 12 | 0 0 0 8 | 0 0 0 4 | [[Title Bar]] Sizing (start padding; the buttons sit flush at the end) | tess-ui: yes (TitleBar style padding); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Bar container | margin | - | N/A: the bar fills the window width at the top edge; it has no outer space | N/A: same as default | N/A: same as default | [[Window]] Anatomy | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Bar container | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Title Bar]] Sizing | tess-ui: yes (TitleBar style gap); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Bar container | border width | - | 0 | 0 | 0 | [[Title Bar]] Tokens used (no border to the content) | tess-ui: yes (TitleBar style border_width); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Bar container | border color | - | N/A: the bar draws no border; the window border belongs to the window | N/A: same as default | N/A: same as default | [[Window]] | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Bar container | corner radius | `shape.none` | 0 | 0 | 0 | [[Title Bar]] Tokens used, [[Shape]] | tess-ui: yes (TitleBar style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Bar container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (TitleBar style elevation); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Title | font | `title_small` | 14/20/500/0.1 | 14/20/500/0.1 | 13/18/500/0.1 | [[Title Bar]] Anatomy, [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via theme typography (role title_small); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Icon | icon size | - | 20 | 20 | 20 | [[Title Bar]] Sizing | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Window button | min width | - | 46 | 46 | 46 | [[Title Bar]] Sizing | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Window button | min height | - | 24 | 24 | 24 | [[Spacing and Density]] Target sizes (the button is as high as the bar) | tess-ui: via stylesheet class title_bar_button (min_height); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Window button | height | `density.control_height` | 40 | 32 | 28 | [[Title Bar]] Sizing | tess-ui: via TitleBar style height (the buttons are 100 percent of the bar); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Window button | padding | - | N/A: the 16 dp glyph is centred in the button, so it has no padding | N/A: same as default | N/A: same as default | [[Title Bar]] Anatomy | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Window button | corner radius | `shape.none` | 0 | 0 | 0 | [[Title Bar]] Tokens used (no rounded container) | tess-ui: via stylesheet class title_bar_button (corner_radius); tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |
| Window button glyph | icon size | - | 16 | 16 | 16 | [[Title Bar]] Sizing | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: element absent in tre |

## Layout and overflow

- Single row, vertical centring by construction: the 20 dp title line box is centred in the bar height (difference above and below at most 1 px, AC-DEN-9).
- The title is a single line with `overflow: ellipsis`; it never wraps and never overlaps the buttons. The application content area shrinks before the title; the buttons never shrink ([[10 Layout Overflow and Scrolling]]).
- At the window minimum of 320 dp the buttons (3 times 46 = 138 dp) are fully visible and the title ellipsises (AC-TTB-3).
- The application's children sit between the title and the buttons. A control wider than the room it has overflows by clipping the content area, not by pushing the buttons out.
- No scroll in the bar.

## Behaviour

- Pointer: a primary press on the bar, its icon or its title moves the window (OS move). A press on a window button, a focusable control, a text field or a control with a click handler in the bar is an ordinary press, not a drag. `Window_Region: none` on a node (and its descendants) removes it from the drag region; `Window_Region: drag` on a node inside a button restores it. When the OS takes the press, the pressed node gets `pointer_cancel` and no click follows. A double press within 500 ms and 4 px on the drag region toggles maximise (on macOS the user's System Settings choice applies). A secondary press opens the system menu, which is on by default in borderless windows ([[ADR-0015 System menu default in borderless windows]]); where a project has turned `system_menu` off in its own decision record, a secondary press is an ordinary press for the application's own menu. A press on the title bar icon opens the same menu.
- Keyboard: Tab order is the application's own children, then minimise, maximise, close. Enter and Space activate the focused button. Escape does nothing. Alt+Space opens the system menu in a borderless window ([[ADR-0015 System menu default in borderless windows]]); the other window shortcuts of the platform (Alt+F4) are the OS's.
- Touch: a long press on the bar behaves as the secondary press; the 46 by 28 dp minimum button hit area meets the 24 dp minimum; in a touch context hit areas are at least 48 dp ([[ADR-0002 Desktop density levels and target sizes]]), so the bar height is 48 dp in a touch context.
- macOS: with a transparent OS title bar the bar leaves `titlebar_inset` room at its start and hides its own buttons while `native_controls` is true; in fullscreen the inset is 0 and the OS controls are hidden.

## Tooltip and overlay behaviour

- Each window button shows a tooltip on the button only: text is the button's action (Minimise, Maximise, Restore, Close), delay 500 ms, shown at once on keyboard focus, one frame to dismiss ([[ADR-0004 Tooltip rule]], [[Tooltip]]). The Maximise tooltip reads Restore while the window is maximised.
- The title, icon and bar show no tooltip. A truncated title shows its full text as the tooltip of the title only #needs-verification (a design choice: [[ADR-0004 Tooltip rule]] puts the tooltip on the smallest element carrying the label).
- The bar opens no overlay. A bar in an overlay closes it with its button; the overlay's focus rules are in [[Dialog]].

## Motion

- No animation on state changes: the active and inactive fade is a single-frame opacity change; the maximise and restore glyph swap is one frame.
- The state layers follow [[State Layers]] (ripple timings there). With reduced motion on, ripples are off ([[Accessibility Rules]]).

## Accessibility

- Roles and names: each window button has role `button` with an accessible name that states the current action: Minimise, Maximise (Restore while maximised), Close. The `dismiss` button is named Close. The bar container is a group named by the window title; the window title is also the window's accessible name ([[Window]]).
- Keys: Tab, Shift+Tab, Enter, Space as above. No arrow-key navigation inside the bar.
- Contrast: title and glyph `on_surface` on `surface` at least 4.5:1 active; inactive (opacity 0.6) at least 3:1 (inactive window chrome; a Tesserae floor, see AC-TTB-9). Focus ring `secondary` at least 3:1 against `surface` ([[Focus Ring]]).
- Target size: every window button at least 24 by 24 dp at every level (WCAG 2.2 SC 2.5.8).
- Announcements: toggling maximise announces the new state through the window's state, not a live region; the OS announces the window state change.
- The focus ring uses the inward variant because the button touches the window edge and the ring would be clipped ([[Focus Ring]] rule on clip edges).

## Dark and light

All colours are role references and follow the scheme. The unthemed app gets the MD3 baseline (light) scheme. The bar is `surface` in both schemes; the close layer is `error` in both. The title bar of an app with `theme_seed` follows the system scheme ([[Theme Following the System]]).

## Defaults

| Setting | Default |
|---|---|
| Buttons | minimise, maximise, close |
| Height | 40 dp at `default` (32 compact, 28 dense) |
| Button width | 46 dp |
| Glyph, icon | 16 dp, 20 dp |
| Title role | `title_small`; `title_dense` at dense |
| Inactive opacity | 0.6 |
| System menu (icon, secondary press on the bar, Alt+Space) | on in borderless windows ([[ADR-0015 System menu default in borderless windows]]); tess-ui: off, fails AC-TTB-18 |
| Windows 11 snap layouts on maximise hover | not built |

## Acceptance criteria

- [ ] AC-TTB-1 (geometry check): bar height is 40, 32 and 28 dp at default, compact and dense, at scale 1.0 and 2.0 (twice the px). Pass: equal to the dp.
- [ ] AC-TTB-2 (geometry check): the window buttons are 46 dp wide and bar-height high, in the order minimise, maximise, close, and the right edge of the close button equals the right edge of the bar. Pass: widths 46, right edge difference 0 dp, hit area at least 24 by 24 dp at each density.
- [ ] AC-TTB-3 (geometry check): at a window width of 320 dp the three buttons lie fully inside the bar, the title right edge is at least 8 dp left of the first button, the title is one line with `overflow: ellipsis`, and the vertical centre of the title line box and of each glyph lies within 1 px of the bar centre. Pass: all four measures at each density.
- [ ] AC-TTB-4 (scripted input): a press and move on the bar background, on the icon and on the title delivers `pointer_down` then `pointer_cancel` to the pressed node and no click (the OS takes the move); a press on a window button, on a focusable child and on a text field child delivers the ordinary click; a node with `Window_Region: none` (and its descendants) is not a drag handle. Pass: event lists equal for six presses.
- [ ] AC-TTB-5 (scripted input): two presses on the drag region within 500 ms and 4 px toggle maximised (state flips); two presses 600 ms apart or 5 px apart do not; two presses on a window button run its action, not the toggle. Pass: `maximized` value after each of four runs.
- [ ] AC-TTB-6 (scripted input): click on minimise, maximise, close calls the window actions `window.minimize`, `window.toggle_maximized`, `window.close` once each (close raises `close_requested`, which a listener can cancel); the maximise glyph reads restore opacity 1 and maximise opacity 0 while maximised, and the reverse otherwise. Pass: call counts and glyph opacities.
- [ ] AC-TTB-7 (token test): bar fill is role `surface`, title, icon and glyph fill role `on_surface`, close layer colour role `error`; the title bar builder holds no colour literal. Pass: resolved values equal the scheme's roles in light and dark; zero literals.
- [ ] AC-TTB-8 (pixel check): in the button state layer the pixel colour equals container blended with the layer colour at 8 percent (hover), 10 percent (focus) and 10 percent (pressed) within 2 channel values; close uses `error`; a keyboard-focused button draws a 3 dp inward ring in `secondary` inside its box; a pointer-clicked button draws no ring. Pass in light and dark.
- [ ] AC-TTB-9 (contrast script): title and glyph `on_surface` on `surface` at least 4.5:1 with the window active; with the window inactive (opacity 0.6 composited over `surface`) at least 3:1; focus ring `secondary` on `surface` at least 3:1. Pass: all three in light and dark.
- [ ] AC-TTB-10 (scripted input): on simulated `active` false the title, icon and buttons read opacity 0.6; on `active` true they read 1.0 within one frame; the dismiss variant never fades. Pass: values equal.
- [ ] AC-TTB-11 (AT tree assertion): the three buttons have role `button` and names Minimise, Maximise (Restore while `maximized` is true) and Close; the dismiss button is named Close; the tooltip text of each equals its name. Pass: property equality in both window states.
- [ ] AC-TTB-12 (scripted input): Tab from the last application control in the bar focuses minimise, then maximise, then close; Shift+Tab reverses; Enter and Space on each run the action; Escape changes nothing. Pass: focused node ids and action counts match.
- [ ] AC-TTB-13 (scripted input): each window button shows its tooltip 500 ms (plus one frame) after pointer enter and at once on keyboard focus, and removes it within one frame on leave, press and Escape (see AC-TIP-3 to AC-TIP-5 in [[Tooltip]]). Pass: layer counts at 499, 517 ms and after each dismissal.
- [ ] AC-TTB-14 (scripted input): on macOS (`native_controls` true) the bar's own buttons are not visible, the inset width equals `titlebar_inset[1]`, and content starts at or after it; with `native_controls` false the inset is 0 and the buttons are visible. Pass: widths and visibility equal.
- [ ] AC-TTB-15 (scripted input): a bar with `Buttons: [dismiss]` has no drag region, no inset and a single 46 dp button; pressing it closes the nearest overlay up the tree (open state false) and does nothing in a bar that is in no overlay; naming `dismiss` together with window buttons is a build error. Pass: overlay open state and error list.
- [ ] AC-TTB-16 (scripted input): the bar height read from the density token after a level change equals 40, 32 or 28 and every part follows (glyphs stay centred within 1 px). Pass: values at each level after `Style { Height }` is not set.
- [ ] AC-TTB-17 (review): the bar's controls follow platform placement: window buttons at the end on Windows and Linux, OS traffic lights at the start on macOS; the application's own controls never duplicate a window button. Pass: reviewer sign-off per platform.
- [ ] AC-TTB-18 (scripted input): in a borderless window with no `system_menu` setting the system menu is on ([[ADR-0015 System menu default in borderless windows]]); a press on the title bar icon, a secondary press on the drag region and Alt+Space each raise the platform window menu request; where a project has turned it off the secondary press reaches the application's own handler. Pass: the setting reads true and three menu requests are raised. Hand check on a real compositor.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/spec/title_bar.py` (`HEIGHT` 40, `BUTTON_WIDTH` 46, `GLYPH` 16, `INACTIVE` 0.6, `STYLES`, `_button`, `_dismiss`), `tess-ui:docs/components/title-bar.md`, `tess-ui:docs/guide/custom-title-bars.md`, tests `tess-ui:tests/test_title_bar.py`, `test_title_bar_macos.py`, `test_title_bar_reload.py`, `test_title_bar_surface.py`, `test_title_bar_theme.py`, `test_title_bar_vocabulary.py`, `test_title_bar_widgets.py` | Partly meets. Meets: AC-TTB-2, AC-TTB-4 to AC-TTB-7 and AC-TTB-10 as designed (drag region, double-click maximise, window actions, glyph swap, role references, fade to 0.6, dismiss variant, macOS inset); not run against the numbers here. Fails AC-TTB-1 and AC-TTB-16 at compact and dense: the height is a constant 40, there is no density setting. Fails AC-TTB-11: the maximise button's label and tooltip are the fixed text Maximise (`_LABELS`, `_TIPS`) and do not become Restore while maximised. AC-TTB-8, AC-TTB-9, AC-TTB-12 (ring variant, state layer values, contrast of the 0.6 fade) are not run and not found in the tests. The start padding is 12 and gap 8 at all levels (AC-DEN-6 at compact and dense fails). Not built: Windows 11 snap layouts on the maximise button, a different glyph set for the buttons. A top app bar made in code on a borderless window acts as a title bar (`top_app_bar(..., window_controls=)`): the `TopAppBar` view is not a title bar |
| tess-ui (dimensions) | `tess-ui:src/tess_ui/spec/title_bar.py` | Differences in [[#Dimensions and defaults]]: bar height 40 at all levels, spec 32 and 28 at compact and dense (AC-TTB-1, AC-DEN-11); start padding 12 and gap 8 at all levels, spec 8 and 8 at compact, 4 and 4 at dense (AC-DEN-6). Button width 46 and glyph 16 meet the table. Not settable from the project layer (no hook): the title icon size 20 (literal in `expand`), the button width `BUTTON_WIDTH` 46 and the glyph size `GLYPH` 16, which are inline node style that a stylesheet cannot override |
| tess-shell | not applicable | Not applicable: no application windows; shell surfaces are layer-shell windows. The shell has no title bar element |
| tre | `tre:docs/reference/window.md` (Title bar and borders), `tre:docs/guide/custom-title-bars.md` (`window_region`, `titlebar_inset`, `native_controls`, `system_menu`, `minimize`, `maximize`, `restore`, `close`) | Exists as primitives: drag region with the interactive-node rule, `pointer_cancel` when the OS takes a press, double-click maximise (500 ms and 4 px on platforms without a system value), resize border, macOS inset and `native_controls`. The engine draws no title bar; see [[Title Bar|Window Title Bar]] |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists (MD3 has the top app bar inside the window, no title bar) | a framework-drawn window frame needs a drag region and window buttons | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Height 40, 32, 28 dp by density (MD3 small top app bar container 64 dp in the deprecated tokens of Material Web `_md-comp-top-app-bar-small.scss`) | desktop title bars are about 30 to 40 dp; the bar follows the control height tokens | [[ADR-0002 Desktop density levels and target sizes]] |
| Window buttons 46 dp wide, 16 dp glyph | the desktop standard on Windows; MD3 icon button is 40 by 40 | [[ADR-0002 Desktop density levels and target sizes]] |
| Close hover and pressed layer in `error` | desktops colour close red; `error_container` is too pale at an 8 percent layer | [[ADR-0009 State layer percentages]] |
| Inactive fade to 0.6 | desktop convention for an inactive title bar; MD3 has no window focus state | [[ADR-0002 Desktop density levels and target sizes]] |
| Inward focus ring on the window buttons | the buttons touch the window edge; an outward ring would be clipped | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |

## Sources

- MD3 top app bar (the nearest counterpart; small container height 64 dp in the deprecated tokens, headline `title-large`, leading icon 24 dp), verified in Material Web: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-top-app-bar-small.scss. The MD3 page https://m3.material.io/components/top-app-bar/overview is a script-rendered app and returns no text.
- Secondary navigation tab tokens (container `surface`, active label `on_surface`, inactive `on_surface_variant`): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-secondary-navigation-tab.scss. Used by [[Dock Panel]], not here.
- State layers: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-state.scss (hover 0.08, focus 0.10, pressed 0.10), see [[State Layers]].
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Engine: `tre:docs/reference/window.md` (Title bar and borders, macOS overlay title bar), `tre:docs/guide/custom-title-bars.md`.
- tess-ui: `tess-ui:docs/components/title-bar.md`, `tess-ui:docs/guide/custom-title-bars.md`.
- Not verified: the 0.6 inactive opacity has no MD3 source; it is the tess-ui value; and the 3:1 floor for it is a Tesserae rule #needs-verification. The tooltip on a truncated title is a design choice #needs-verification.
