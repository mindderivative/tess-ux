---
title: Scrim
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, scrim, overlay]
related: ["[[Colour Roles]]", "[[Elevation]]", "[[Motion]]", "[[Dialog]]", "[[Popup]]", "[[Menu]]", "[[Tooltip]]", "[[12 Overlays]]", "[[Existing Tokens]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]"]
---

# Scrim

> [!info] Summary
> The scrim is the translucent layer drawn between a modal surface and the content it blocks: colour role `scrim`, opacity 0.32, drawn only behind modal surfaces. Counterpart: [Material 3 scrim in colour roles](https://m3.material.io/styles/color/roles) and the [dialog](https://m3.material.io/components/dialogs/specs) specification. Source of truth in code: see Status in code.

## Purpose

A scrim marks everything outside a modal surface as inactive and focuses attention on the modal. It is not a click-away catcher: an invisible input layer that closes a popup (as under the shell Launcher) draws nothing and is not a scrim.

## Tokens

The official pages are script-rendered and could not be fetched. The values are verified in Material Web: the token file [md-comp-scrim](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-scrim.scss) maps `container-color` to the system role `scrim` and `container-opacity` to 0.32, and the [dialog animations](https://github.com/material-components/material-web/blob/main/dialog/internal/animations.ts) fade the scrim from 0 to 0.32 over 500 ms and back over 150 ms, both linear.

| Token | Value | Source |
|---|---|---|
| Colour role | `scrim`; `#000000` in light and dark at the standard level | [md-sys-color v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-color.scss) (neutral 0) |
| Opacity | 0.32 | `md.comp.scrim.container-opacity` above |
| Fade in | 500 ms, linear | Material Web dialog animations |
| Fade out | 150 ms, linear | Material Web dialog animations |
| Extent | the whole window, over every other surface and under the modal surface | this note |

Android's modal navigation drawer scrim defaults to black at 60 percent ([NavigationDrawer guide](https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationDrawer.md), Scrim attributes); Tesserae uses the Material Web value of 0.32 for all modal surfaces, so the platform value is a deviation of the Android library, not a Tesserae value.

### Surfaces that use a scrim

| Surface | Scrim | Note |
|---|---|---|
| Modal dialog ([[Dialog]]) | yes | MD3 dialog; blocks the window behind it |
| Modal side sheet and modal bottom sheet | yes | MD3 modal sheets |
| Modal navigation drawer | yes | MD3 modal drawer |
| Menu ([[Menu]]), popup ([[Popup]]), tooltip ([[Tooltip]]) | no | non-modal; Material Web `md-menu` has no scrim element |
| Standard (non-modal) side sheet, docked panel | no | non-modal |
| Shell Launcher and shell popups | no | non-modal; the click-away layer under them is an invisible input layer |

## Rules

1. A scrim is drawn only behind a modal surface, over every other surface in the window and under the modal surface. A non-modal surface never draws one.
2. The scrim colour is the role `scrim` at opacity 0.32. A project changes the scrim by changing the role, and the change reaches every modal surface; the transparency is not baked into a per-component colour literal.
3. The scrim covers the whole window, not only the parent panel.
4. A pointer press on the scrim dismisses a dismissible modal and is consumed: it does not reach the content below. A modal that must not be dismissed (a destructive confirmation in progress) ignores the press and keeps the scrim.
5. Escape dismisses a dismissible modal; focus moves into the modal on open and returns to the invoking control on close. Content behind the scrim is not reachable by Tab and is exposed to assistive technology as inactive ([[Dialog]]).
6. The scrim fades with the durations above; under reduced motion it appears and disappears with duration 0 ([[Motion]] rule 4).
7. Only one scrim is visible at a time. A modal opened over a modal replaces the lower scrim by a deeper one only if the project spec says so; the default is a single scrim under the topmost modal.
8. A scrim is not a way to hide missing content: text and icons below it are unchanged.
9. An engine that draws no scrim (tre) leaves it to the application; the application draws the scrim as the lowest child of the modal layer.

## Acceptance criteria

- [ ] AC-SCR-1: Token test. The theme returns the role `scrim` as `#000000` in light and dark and the scrim opacity 0.32. Pass: both equal.
- [ ] AC-SCR-2: Pixel check. Open a modal dialog over a region of colour C. Sample the region outside the dialog after the fade completes. Pass: each 8-bit channel equals 0.68 times the channel of C within 2 levels.
- [ ] AC-SCR-3: Token test. Change the `scrim` role to `#101010` at runtime. Pass: the sampled colour of AC-SCR-2 changes to 0.68 C plus 0.32 times the new role colour, which shows the opacity is applied to the role.
- [ ] AC-SCR-4: Geometry check. The scrim rectangle equals the window rectangle. Pass: width and height equal the window's, on all four sides.
- [ ] AC-SCR-5: Pixel check. Open a menu, a tooltip and a popup in turn. Pass: the window background pixel stays equal to its value before opening in each case (no scrim).
- [ ] AC-SCR-6: Scripted input. With a dismissible dialog open, click a button located under the scrim. Pass: the dialog closes and the button's action is not invoked.
- [ ] AC-SCR-7: Scripted input. With a non-dismissible dialog open, click the scrim and press Escape. Pass: the dialog stays open and the scrim stays.
- [ ] AC-SCR-8: Scripted input. Press Tab 20 times with a modal open. Pass: focus never leaves the modal.
- [ ] AC-SCR-9: Scripted frame capture. Open a dialog at 60 Hz. Pass: scrim opacity reaches 0.32 between 500 ms and 533 ms; on close it reaches 0 between 150 ms and 183 ms; under reduced motion it reaches the end value on the next frame.
- [ ] AC-SCR-10: Pixel check. In dark and light, the surface under the scrim and the modal surface on top both resolve from roles ([[Colour Roles]] AC-COL-6). Pass: luminance rules hold.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Dialog_Stylesheet.tdl` line 7; `tess-ui:docs/themes/index.md`; `tess-ui:src/tess_ui/tokens.py` (`scrim` role) | Partly meets. The `scrim` role exists (`#000000` generated, equal to the baseline). Docs say the Dialog and modal side sheet scrims put transparency in the colour, so a `Colors { Scrim }` override does not reach them: AC-SCR-3 fails. Fade durations and the extent are not verified (AC-SCR-4, AC-SCR-9 not checked). |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` (`$color.scrim` `#000000`) | Absent. The token is defined and no surface references it; the shell has no modal surface. The invisible click-away layer under the Launcher is input handling and is correct to draw nothing (AC-SCR-5 meets). |
| tre | `tre:docs/reference/layers.md` | Not applicable by design: a modal layer blocks input and draws nothing; scrim colour, opacity and animation are the application's (Rules 9). |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| One scrim opacity (0.32) for every modal surface | Material Web uses 0.32 for the dialog; Android uses other values per component; one value is testable | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Scrim fade-in of 500 ms is a Material Web value | Verified in Material Web; a desktop shortening is not decided | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
