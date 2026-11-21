---
title: Panel and Surface
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, container, shell, owner-feedback]
related: ["[[12 Overlays]]", "[[Popup]]", "[[Dialog]]", "[[Menu]]", "[[Tooltip]]", "[[Tree]]", "[[Scrollbar and Scroll Container]]", "[[Colour Roles]]", "[[Theme Following the System]]", "[[Shape]]", "[[Elevation]]", "[[Spacing and Density]]", "[[Owner Feedback 2026-11-20]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# Panel and Surface

> [!info] Summary
> A surface is any painted container: a window background, a pane, a card, a sheet, a menu body. Its colour is a surface role, its corners a shape token, its separation from neighbours a tone step or an elevation shadow. The Tesserae shell adds four drawn surface types (Bar, Frame, Panel, Popup) on top of the same rules. Material Design 3 counterparts: [Color roles, surface and surface container](https://m3.material.io/styles/color/roles), [Elevation](https://m3.material.io/styles/elevation/overview), [Shape](https://m3.material.io/styles/shape/overview). Source of truth in code: see the last section.

## Purpose

State how containers are painted so every surface follows the colour scheme, has predictable corners and depth, and so a dark system theme never produces a white application (owner feedback F1, [[Owner Feedback 2026-11-20]]).

## When to use and not

- Use when: grouping content in a pane, a card-like region, a sidebar, a bar, a popup body or a dialog container.
- Do not use when: a hairline is enough (use a divider, see [[Tree]] and list notes); the element is a control with its own states (a button's container belongs to [[Button]]).
- Shell surfaces (Bar, Frame, Panel, Popup) are windows or window-like containers placed by the compositor; use them only for shell elements. Inside an application window, use containers.

## Anatomy

1. Container: a rectangle with corner radius, fill role, optional border and shadow.
2. Content area: padding inside the container.
3. Shadow: drawn in a transparent margin outside the container (shell) or around the node (toolkit).
4. Join (shell only): a drawn fillet where a melded Panel meets the Frame.

## Variants

| Variant | Use | Role and shape |
|---|---|---|
| Window background | The root of an application window | `surface` |
| Pane | Sidebar, tree pane, form pane, editor area | `surface_container_low`, `medium` (12 dp) corners |
| Card region | A contained group within a pane | `surface_container` |
| Overlay body | Menu, popover, rich tooltip | `surface_container`, level 2; dialog `surface_container_high`, level 3 |
| Banner and status regions | Non-blocking messages | role pairs such as `error_container` with `on_error_container`, `tertiary_container` with `on_tertiary_container` |
| Shell Bar | Edge-attached strip | same tokens as Panel; no look of its own |
| Shell Frame | Ring around the screen | `Background` colour or gradient, outer corners 0 dp, inner corners from shape tokens |
| Shell Panel | Floating, attached or melded surface | `surface`-family role, shape token, optional shadow |
| Shell Popup | Menu, flyout, tooltip | see [[Popup]] |

The assignment of container roles to uses is a Tesserae rule; MD3 defines the roles but not a fixed mapping of every use to a role #needs-verification-as-design-choice (tess-ui's config app uses `surface` for the window and `surface_container_low` for panes).

## States

A surface has no interaction states of its own. A pressable surface (an actionable card) adds state layers (see [[State Layers]]); a disabled surface fades its content to 38 percent.

| State | Visual change | Token values |
|---|---|---|
| Rest | Fill role, no shadow for panes | elevation level 0 |
| Elevated overlay | Shadow under the body | level 2 (menu, rich tooltip, popover), level 3 (dialog) |
| Melded (shell) | Panel and Frame share one fill, no seam at idle | same role as the Frame |
| Hidden (shell) | Not drawn, not in tab order | not applicable |

## Tokens used

| Part | Role or token |
|---|---|
| Fill | one of `surface_dim`, `surface`, `surface_bright`, `surface_container_lowest`, `surface_container_low`, `surface_container`, `surface_container_high`, `surface_container_highest`, `inverse_surface` |
| Content on a surface | `on_surface`; secondary text and icons `on_surface_variant` |
| Border | `outline` (strong) or `outline_variant` (subtle) |
| Shape | `none` 0, `extra_small` 4, `small` 8, `medium` 12, `large` 16, `extra_large` 28, `full` ([[Shape]]) |
| Elevation | levels 0 to 5 ([[Elevation]]); shadow colour role `shadow` |
| Scrim | `scrim` at 32 percent ([[Scrim]]) |

Shell mapping (the shell keeps its 12 flat roles; mapping per [[Colour Roles]]): `$color.surface` is the ground of bars and panels (maps to `surface`); `$color.surface_raised` is a surface above the ground for popups, buttons, tooltips (maps to `surface_container`); `$color.on_surface` to `on_surface`; `$color.on_surface_muted` to `on_surface_variant`; `$color.outline` to `outline`; `$color.scrim` to `scrim`. Shell `$shape.small` (4) equals MD3 `extra_small`, `$shape.medium` (8) equals MD3 `small`, `$shape.large` (16) equals MD3 `large`.

MD3 tokens also define a surface tint layer colour (`container-surface-tint-layer-color`, role `surface_tint`); Tesserae does not apply it. Depth comes from the container role step and the shadow.

## Sizing and density

- A surface has no intrinsic size; padding comes from [[Spacing and Density]]: container padding 8 dp for panes at `compact` (the config-style default) and 12 dp at `default`, 4 dp at `dense` #needs-verification-as-design-choice.
- Pane corner radius 12 dp (`medium`) for floating panes; 0 dp on the sides that touch the window edge.
- Shadow margin (shell): at least blur plus spread plus the larger offset of the shadow, so the shadow is never cut by the surface window.

## Layout and overflow

- Content that exceeds a pane scrolls inside the pane on both axes with visible scrollbars ([[ADR-0003 Scrollbar rule]], [[Scrollbar and Scroll Container]]); a surface never lets content paint beyond its container box (clip to the rounded container).
- Text inside a surface wraps or truncates with an ellipsis per [[10 Layout Overflow and Scrolling]]; it never runs past the container edge.
- A shell Bar or Panel that grows with its content clamps to its maximum and scrolls (`Max_Width`, `Max_Height`).

## Behaviour

- Pointer and keyboard: a plain surface is not focusable and not a tab stop; it can carry a group role and a label for assistive technology.
- Theme: every surface fill resolves from the scheme at draw time; switching the scheme repaints every surface ([[Theme Following the System]]).
- Shell placement: Bar attaches to one edge and reserves space; Frame surrounds the output and reserves space per side; Panel attaches to a frame, bar or other surface, or floats, and may be moved by the pointer; Popup hangs off a rectangle of another surface ([[Popup]]). Reserved space is allowed only on the `TOP` layer. A Frame is on `TOP` only; a Popup is compositor-stacked above its parent.
- Melding: a Panel attached to the Frame with no margin on the Frame-facing sides melds (same fill, drawn join, no seam at idle); a margin on those sides stops the meld and the Panel's corners round as a floating Panel's do. A melded Panel is drawn in the Frame's colour and ignores its own style keys (`Background`, `Fill`, `Opacity`, `Elevation`, `Shadows`).
- Shadows are excluded from the hit shape and the input region; clicks on a shadow reach the window underneath.

## Tooltip and overlay behaviour

A surface carries no tooltip itself (tooltips belong to controls, [[Tooltip]]). Overlay bodies are surfaces with the roles in the table above; the overlay rules (layers, dismissal, focus, scrim) are in [[12 Overlays]].

## Motion

Surface show and hide in the shell is a margin slide of 200 ms with content fade, or a fade, or none (`Animation.Type`, `Duration` 200); reduced motion makes show and hide instant. A scheme change repaints without animation unless the project animates it with [[Motion]] `medium2` (300 ms) #needs-verification-as-design-choice.

## Accessibility

- Each shell surface window is published as one more window of the application with an accessible name set per surface; a bar's window node has no name in tre, so the shell sets it.
- A pane carries role `group` with a label ("Files", "Structure") so assistive technology can name regions.
- Text on every surface role used for text meets 4.5:1 (3:1 for large text and icons); a surface boundary needs no contrast ratio unless it is the only cue to a control edge (3:1, WCAG 1.4.11).
- A hidden or collapsed shell surface has a keyboard way to open it: Shortcut Mode reveals a hidden Bar or Panel and moves focus to it ([[ADR-0021 Shortcut Mode reveals a hidden Bar]], [[Accessibility Rules]]).

## Dark and light

The window background and every pane resolve from the scheme; there is no literal colour in a view ([[ADR-0005 Theme follows the system]]). In dark, `surface` is a near-black tone and containers step lighter with the role number; in light, containers step slightly darker than `surface`. Owner feedback F1: the config app presented white surfaces under a dark system theme; the cause lay in surfaces that did not resolve from the scheme at the first frame (see Status and [[Theme Following the System]]).

## Defaults

| Setting | Default |
|---|---|
| Window background | `surface` |
| Pane | `surface_container_low`, 12 dp corners, level 0 |
| Overlay body | `surface_container`, level 2 (dialog `surface_container_high`, level 3) |
| Shell Frame outer corner radius | 0 dp |
| Shell Popup elevation | about 20 percent of the maximum shadow (proposed) |
| Shell show and hide | slide 200 ms (Panel), instant under reduced motion |

## Acceptance criteria

Test methods follow [[Test Method]]. Pixel checks sample both schemes.

- [ ] AC-PNL-1 (pixel check, dark window, F1): with the system scheme dark, at the first drawn frame and after 1 s, sample the window background and each pane at five points each. Pass: each sample equals the scheme's `surface` (window) or the pane's container role, and no sample inside a surface equals `#FFFFFF` unless a swatch or image.
- [ ] AC-PNL-2 (token test, no literals): in every view, stylesheet and module of a project, a `Background` or `Fill` value is a role name (or `transparent` or a role with an alpha), never a hex literal, except in colour pickers and swatches. Pass: zero literal fills in the scan.
- [ ] AC-PNL-3 (contrast script): in light and dark, contrast of `on_surface` and `on_surface_variant` on each of the nine surface roles at least 4.5:1; of `outline` on `surface` at least 3:1 where it is a control edge.
- [ ] AC-PNL-4 (token test, shape): every corner radius of a surface is a value of the shape scale (0, 4, 8, 12, 16, 28, full); panes use 12 dp, touching sides 0 dp. A literal radius outside the scale fails.
- [ ] AC-PNL-5 (token test, elevation): a pane at rest has elevation level 0 and no shadow; a menu, popover and rich tooltip level 2; a dialog level 3; a full-screen dialog level 0. The elevation levels exist as tokens in the project ([[Elevation]]).
- [ ] AC-PNL-6 (scripted input, scheme switch): switching the scheme (system, light, dark) repaints every surface; within one frame after the switch no surface pixel sampled (five per surface) equals its previous-scheme colour.
- [ ] AC-PNL-7 (geometry check, shadow margin, shell): the transparent margin of a shadowed Bar, Panel or Popup is at least blur plus spread plus the larger absolute offset of its shadow; the visible shadow has no clipped edge (pixel row at the margin boundary is fully transparent).
- [ ] AC-PNL-8 (scripted input, input region, shell): a press in the shadow area outside the body reaches the window underneath; the input region equals the body rectangle ±1 px.
- [ ] AC-PNL-9 (pixel check, melded Panel, shell): at idle, a Panel melded to the Frame has pixels in its body and on the join equal to the Frame's fill (difference 0), and the row of pixels across the seam shows no gap; with a margin on the Frame-facing sides the Frame edge is straight and the Panel corners are rounded.
- [ ] AC-PNL-10 (review, Bar look): a Bar defines no look keys that a Panel does not; Bar, Panel and Frame resolve the same token set (checked against the shell's style schema).
- [ ] AC-PNL-11 (geometry check, reserved space): an exclusive zone is accepted only on the `TOP` layer; on another layer loading fails with an error (shell load test).
- [ ] AC-PNL-12 (AT tree assertion): every shell surface window has a non-empty accessible name; every pane has role `group` and a label.
- [ ] AC-PNL-13 (geometry check, clipping): content that overflows a pane is clipped to the pane's rounded rectangle and a scrollbar thumb is visible on each overflowing axis; no pixel of the content lies outside the pane rectangle.
- [ ] AC-PNL-14 (scripted input, hidden Panel reachable by keyboard, ADR-0021): with a hidden Panel (`Hide_After` elapsed), `Enter_Shortcut_Mode` shows it and moves focus to it; Escape or `Exit_Shortcut_Mode` hides it again per its `Hide_After`; while it holds keyboard focus it is not hidden; a plain key press with no mode active leaves it hidden. Pass: states as stated.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (root `surface`, panes `surface_container_low` with 12 px corners and padding 8), `Main_Stylesheet.tdl`, `tess-ui:src/tess_ui/tokens.py` (49 roles, shapes, elevation levels), `tess-ui:src/tess_ui/views/Card_Stylesheet.tdl`, `Dialog_Stylesheet.tdl`, `Menu_Stylesheet.tdl` | Partly meets. Meets AC-PNL-1 for views that use roles (root and panes resolve from the scheme; first-frame scheme risk on macOS and Windows: the app starts dark and flips, an App with no `theme_seed` has no scheme and ignores dark, the config app now sets one), AC-PNL-2 in part (pane fills are roles; literal colours remain in a colour swatch and in `Elevation`/shape literals in stylesheets), AC-PNL-4 and AC-PNL-5 (shape scale 0, 4, 8, 12, 16, 28, full and levels 0 to 5 exist; per-sheet literals; the two sources `default_theme.tdl` `Components` and sheets must be kept in sync), AC-PNL-6 not verified, AC-PNL-13 fails for the horizontal axis (ScrollView scrolls one axis). Not applicable: AC-PNL-7 to AC-PNL-12 shell items. |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (Bar, Frame, Panel, Popup roots), `tess-shell:src/tess_shell/binder/shadow.py`, `tess-shell:src/tess_shell/surfaces/frame.py`, `join.py`, `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`, vault `shell-vault:40 Specifications/Surfaces/` (Surface Types, Bar, Frame, Panel, Popup) | Partly meets. Meets AC-PNL-8 (popup `input_region="geometry"`; owner retest 2026-11-07 passed), AC-PNL-10 (Bar has no look of its own; spec decided 2026-10-27), AC-PNL-11 (load error), AC-PNL-9 in part (join built, five variants behind `Debug { Frame_Join }`; owner on 2026-11-07 chose the PARAM join, "looks good"; one fault: border looks slightly thinner at the rounding, TRE-REQ-015). Fails or gaps: AC-PNL-5 (no elevation levels: one shadow list scaled by `Elevation: N%`, theme `Elevation.Max` `#00000066`, code fallback `#00000040`; Frame `Elevation`, `Shadows`, `Shadow_Bleed` not built; Bar and Frame keys `Exclusive_Zone`, `Input_Region`, `Meld`, `Animation` read but not built), AC-PNL-4 (shell shape scale 0, 4, 8, 16, 999 is not the MD3 scale; corner radii are literals such as 8 in module tooltips), AC-PNL-2 (module `Tooltip` and Menu use `surface_raised` role tokens, but pixel literals remain), AC-PNL-3 no contrast script exists, AC-PNL-6 and AC-PNL-1 depend on the Default stylesheet being applied (without a stylesheet the Launcher was unreadable; ADR-0022 default stylesheet accepted), AC-PNL-12 not verified (names set per surface in the shell file; Orca not tested), AC-PNL-7 not verified on KWin. A melded Panel ignores its own style keys (documented). |
| tre | `tre:docs/reference/layer-window.md`, `tre:docs/guide/painting.md` | Engine mechanisms only: shadows list, `clip_children`, `input_region`, popup `geometry`, window transparency. No surface roles, no scheme. Not applicable as a component. |

Evidence: F1 in [[Owner Feedback 2026-11-20]] (config app "all white except tooltips" under a dark system theme); the shell Launcher unreadable with no stylesheet (shell ADR-0022, default stylesheet accepted); popup shadow faults of 2026-11-06 and the click-through fix in `shell-vault:40 Specifications/Surfaces/Popup.md`; Frame join retests in `shell-vault:40 Specifications/Surfaces/Frame.md`.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Surface tint layer is not applied | tone steps and shadows carry depth in all three projects | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Shell uses 12 flat roles mapped to MD3 roles | shell independent of tess-ui (shell ADR-0006); mapping documented | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Shell elevation is one shadow scaled by a percentage | engine takes shadow lists; levels are a gap, not a promise | [[Deviations from MD3]] |
| Shell shape scale 0, 4, 8, 16, 999 | existing shell tokens; mapped to the MD3 names | [[Deviations from MD3]] |
| Shell surface types (Bar, Frame, Panel, Popup) and melding | desktop shell elements with no MD3 counterpart | [[Deviations from MD3]] |

## Sources

- Surface roles (`surface`, `surface-dim`, `surface-bright`, `surface-container-lowest`, `-low`, `surface-container`, `-high`, `-highest`, `inverse-surface`, `on-surface`, `on-surface-variant`, `outline`, `outline-variant`, `scrim`, `shadow`, `surface-tint`) as MD3 system colour tokens: `https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-color.scss` and the component token files for menu and dialog (container roles verified: menu `surface-container`, dialog `surface-container-high`, full-screen dialog `surface`, `container-surface-tint-layer-color` present): `https://github.com/material-components/material-web/tree/main/tokens/versions/latest/sass`.
- Elevation levels 0, 1, 3, 6, 8, 12 (levels 0 to 5 in dp): `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-elevation.scss`. Shape scale values 0, 4, 8, 12, 16, 28, 9999 px: `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-shape.scss`. Scrim opacity 0.32: `.../_md-comp-scrim.scss`.
- WCAG 2.2 SC 1.4.3 Contrast (Minimum), 4.5:1 for text and 3:1 for large-scale text; SC 1.4.11 Non-text Contrast, 3:1 against adjacent colours; verified: `https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html` and `https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html`.
- Shell: `shell-vault:40 Specifications/Surfaces/Surface Types.md`, `Bar.md`, `Frame.md`, `Panel.md`, `Popup.md`; `tess-shell:src/tess_shell/schema/blocks.py`.
- tess-ui: `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, `Main_Stylesheet.tdl`; `tess-ui:src/tess_ui/tokens.py`.
