---
title: Theme Following the System
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, theme, dark-mode]
related: ["[[Colour Roles]]", "[[02 Colour and Theming]]", "[[Motion]]", "[[State Layers]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0005 Theme follows the system]]", "[[14 Accessibility Basics]]", "[[Existing Tokens]]"]
depends_on: ["[[ADR-0005 Theme follows the system]]", "[[Colour Roles]]"]
---

# Theme Following the System

> [!info] Summary
> How an application picks light or dark (and the contrast level), keeps a persistent user override, and never shows a wrong-scheme frame. Decided in [[ADR-0005 Theme follows the system]]; this note turns the decision into testable rules. Material Design 3 defines both schemes ([colour roles](https://m3.material.io/styles/color/roles)) but not how an application chooses between them, so this note has no MD3 counterpart for the selection rules.

## Purpose

A user who sets the desktop to dark gets a dark application on the first frame, and a user who prefers a different scheme in one application keeps that choice. Evidence: [[Owner Feedback 2026-11-20]] F1 (the system theme was dark and the config app was white except tooltips) and the shell default stylesheet decision (shell ADR-0022).

## Tokens

| Token | Value | Source |
|---|---|---|
| Scheme mode setting | one of `system`, `light`, `dark`; default `system` | [[ADR-0005 Theme follows the system]] |
| Contrast level | `standard`, `medium`, `high`; selected from the OS contrast preference; `high` when the OS reports high contrast, else `standard` | [[Colour Roles]]; mapping of the OS preference to `medium` #needs-verification |
| Resolve budget | 200 ms: the longest wait for the platform's first answer before the project default scheme is used | `tess-shell:src/tess_shell/services/portal.py` `first(timeout=0.2)` |
| Re-theme budget | 200 ms: from a scheme-change signal to the last surface drawn in the new scheme | Tesserae choice, equals the Motion token `short4` ([[Motion]]) #needs-verification (design choice) |
| Pending surface | a uniform fill with no content, in the dark baseline `surface` `#141218`, drawn only when a frame must be shown before the scheme is known and the window cannot stay hidden | Tesserae choice #needs-verification (design choice) |
| Stored value key | one persistent key per application holding `system`, `light` or `dark` | this note; storage location is project-owned |

## Rules

1. The default is `system`: the application follows the platform's light or dark preference and its contrast preference, and re-themes when either changes.
2. A user override is one of `system`, `light`, `dark`. `light` and `dark` fix the scheme and ignore later platform changes. `system` restores following.
3. The override persists across restarts in the application's own settings store. An unreadable or unknown stored value is treated as `system`; the application starts and does not raise.
4. No first-frame flash. The scheme is resolved before the first frame is drawn. When the platform answers late, the window is not shown until it answers (preferred); when the window must be shown, the frame is the pending surface, a uniform fill with no content, until resolved. The first drawn content frame uses the resolved scheme.
5. When the platform does not answer within the resolve budget, the project default scheme is used (the dark baseline for Tesserae shell and tess-ui) and the application re-themes when the answer arrives.
6. Every surface uses colour roles, so one scheme change re-colours the window background, panels, rows, popups and overlays ([[Colour Roles]] Rules 10). No surface keeps a literal colour.
7. An application with no seed colour falls back to the published baseline scheme ([[Colour Roles]] baseline tables) and still follows light and dark. It never renders with no scheme.
8. The contrast level follows the OS high contrast preference with the same no-flash rule; a change re-themes in place.
9. The reduced motion and animations-off preferences are read in the same step as the scheme ([[Motion]] reduced-motion rule).
10. The scheme choice is exposed to the user in the application's settings or a menu, and the current value is readable by assistive technology ([[14 Accessibility Basics]]).

## Acceptance criteria

- [ ] AC-TH-1 (scripted input): Scripted launch with a platform stub reporting dark and the setting `system`. Capture the first presented frame. Pass: every sampled surface in that frame has luminance below 0.05 and no frame with luminance above 0.6 for the window background appears before or after.
- [ ] AC-TH-2 (scripted input): The same with the stub reporting light. Pass: the first presented frame has window-background luminance above 0.6 and no dark frame precedes it.
- [ ] AC-TH-3 (scripted input): Scripted runtime switch. With setting `system`, change the stub from light to dark and back. Pass: within 200 ms of each signal every surface sampled by AC-COL-6 in [[Colour Roles]] shows the new scheme, and no restart is needed.
- [ ] AC-TH-4 (scripted input): Persistence. Set the override to `dark` while the stub reports light, close, and start the application twice. Pass: both starts draw the dark scheme on the first frame (AC-TH-1 luminance rule) and the stored value reads `dark`.
- [ ] AC-TH-5 (scripted input): Return to following. Set the override to `system` after AC-TH-4 and switch the stub to light. Pass: the application re-themes to light within 200 ms and the stored value reads `system`.
- [ ] AC-TH-6 (scripted input): Corrupt store. Write the value `purple` to the store and start. Pass: the application starts, follows the platform, and does not raise.
- [ ] AC-TH-7 (scripted input): Late platform answer. The stub answers dark after 500 ms. Pass: until the answer, either no window is mapped or each presented frame is a single uniform colour (pixel variance zero); after the answer the first content frame is dark.
- [ ] AC-TH-8 (scripted input): Silent platform. The stub never answers. Pass: at 200 ms the project default scheme is drawn; when the stub then answers light at 2 s the application re-themes within 200 ms.
- [ ] AC-TH-9 (scripted input): No-seed application. Start an application with no seed under the stub in dark, then light. Pass: the window background is within the tolerance of [[Colour Roles]] Rules 11 (per channel plus or minus 2, or CIEDE2000 below 1.0) of the baseline `surface` (`#141218` dark, `#FEF7FF` light) and role-coloured text is within the same tolerance of the baseline `on_surface`.
- [ ] AC-TH-10 (scripted input): Contrast preference. With the stub reporting high contrast, start and switch at runtime. Pass: the window background and `on_surface` equal the high-contrast table values of [[Colour Roles]] and the contrast script AC-COL-3 passes on the drawn frame colours.
- [ ] AC-TH-11 (scripted input): Surface coverage. Under a forced dark override, run the luminance check of AC-COL-6 on every surface type the project defines, popups and tooltips included. Pass: none has a light-scheme colour.
- [ ] AC-TH-12: AT tree assertion. The settings control for the scheme exposes its role, its name and the current value (`system`, `light`, `dark`) in the accessibility tree. Pass: the assertion finds all three.

## Status in code

Evidence: [[Owner Feedback 2026-11-20]] F1.

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/app.py` (`App(dark="system")`, `_os_dark`, `_adopt_os_appearance`, `set_dark`), `tess-ui:src/tess_ui/follow.py` | Partly meets. Rule 1 meets (`dark="system"` default, `color_scheme` event re-themes; high contrast and reduced motion follow the OS). AC-TH-1 and AC-TH-2 meet on Linux (the OS answer is read at construction) and fail on macOS and Windows (the app starts dark and flips after the window opens, a visible flash). AC-TH-3 meets in design (the 200 ms budget is not timed). AC-TH-4 and AC-TH-5 absent: `set_dark` changes the live value, no persistent store exists. AC-TH-6 not applicable until a store exists. AC-TH-7 fails (no hold of the first frame). AC-TH-9 fails: an App with no `theme_seed` has no scheme and ignores `dark`; the config app now sets a seed. AC-TH-12 not checked. |
| tess-shell | `tess-shell:src/tess_shell/services/portal.py` (`first(timeout=0.2)`), `tess-shell:src/tess_shell/appearance.py` (`Appearance.scheme` default `"default"`), `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | Partly meets. The portal read has a 200 ms budget and a late answer arrives through `on_change`, so rule 5 and AC-TH-8 meet in design (not run here). Default scheme is the theme's dark base; the `Dark { }` block is empty and a `Light` block exists. No persistent user override found (AC-TH-4 and AC-TH-5 absent). High contrast and reduced motion are read from the portal. First-frame behaviour with a slow portal is not tested (AC-TH-7 not verified). |
| tre | `tre:docs/reference/events.md` (`window.get("dark")`, `color_scheme` event, `high_contrast`) | Not applicable: the engine reports the platform preference (None when unknown) and draws no scheme. It supplies the signal the rules need. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Selection of scheme, override and flash rules are Tesserae-specific | MD3 specifies the schemes, not how an application chooses one | [[ADR-0005 Theme follows the system]] |
| Pending surface and re-theme budget values | Design choices to make the no-flash rule testable | [[ADR-0005 Theme follows the system]] |
