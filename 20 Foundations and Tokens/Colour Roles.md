---
title: Colour Roles
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, colour, tokens]
related: ["[[Theme Following the System]]", "[[State Layers]]", "[[Focus Ring]]", "[[Elevation]]", "[[Scrim]]", "[[Typography]]", "[[02 Colour and Theming]]", "[[Existing Tokens]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[Owner Feedback 2026-11-20]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# Colour Roles

> [!info] Summary
> The 49 Material Design 3 colour roles with light and dark hex values for the baseline seed `#6750A4` at the standard, medium and high contrast levels, the pairing and contrast rules, and the mapping of the shell's 12 flat roles to them. Counterpart: [Material 3 colour roles](https://m3.material.io/styles/color/roles). Chapter-level principles: [[02 Colour and Theming]]. Source of truth in code: see Status in code.

## Purpose

Every surface, text, icon and line takes its colour from a named role so that one scheme change (light, dark, contrast level, seed) re-colours the whole application. A literal hex in a view breaks that guarantee and is the cause of owner feedback F1 in [[Owner Feedback 2026-11-20]]: a dark system theme with a white application. The role names are the specification vocabulary ([[ADR-0001 MD3 role names are the specification vocabulary]]).

## Tokens

### Sources and how the values were verified

- The official page [m3.material.io/styles/color/roles](https://m3.material.io/styles/color/roles) is a script-rendered application that the fetch tool cannot read. The hex values below are taken from the published Material Web token sources instead, which are generated from the same design data: standard light and dark from [md-sys-color v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-color.scss) with the palette in [md-ref-palette](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-ref-palette.scss); medium and high contrast from the `latest` token set ([medium](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-color__medium-contrast.scss), [high](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-color__high-contrast.scss), [dark medium](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-color__dark__medium-contrast.scss), [dark high](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-color__dark__high-contrast.scss)).
- Two published generations exist. The `v0_192` set is the 2022 role scale that [[ADR-0006 MD3 baseline with named Expressive adoptions]] selects as the baseline. The `latest` set differs from it in four light roles only: `on_primary_container` `#4F378B`, `on_secondary_container` `#4A4458`, `on_tertiary_container` `#633B48`, `on_error_container` `#8C1D18` (tone 30) against `#21005D`, `#1D192B`, `#31111D`, `#410E0B` (tone 10) in `v0_192`. The dark set is identical. Tesserae uses the tone 10 values at the standard level; the medium and high tables below come from `latest` because no other source publishes them. `surface_tint` is absent from `latest`; here it equals `primary` (as `md.sys.elevation.surface-tint-color` in [md-sys-elevation](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-elevation.scss)).
- Contrast level numbers: medium and high are the Material contrast levels; the numeric values 0.5 and 1.0 passed to a generator, and the numbering of the OS preference to a level, are #needs-verification (the official page was not readable).

### Role set and baseline values (standard contrast, seed `#6750A4`)

The baseline scheme is the published scheme for seed `#6750A4`. A role is spelled in snake case in code (`on_primary_container`) and in kebab case in CSS (`--md-sys-color-on-primary-container`).

| Role | Use | Light | Dark |
|---|---|---|---|
| `primary` | Key components: filled button, active indicator, switch track (on), focus accent text | #6750A4 | #D0BCFF |
| `on_primary` | Text and icons on `primary` | #FFFFFF | #381E72 |
| `primary_container` | Standout fill for key components: filled tonal emphasis, selected chip, FAB | #EADDFF | #4F378B |
| `on_primary_container` | Text and icons on `primary_container` | #21005D | #EADDFF |
| `inverse_primary` | Accent on `inverse_surface` (snackbar action) | #D0BCFF | #6750A4 |
| `primary_fixed` | Primary container that keeps its tone in light and dark | #EADDFF | #EADDFF |
| `primary_fixed_dim` | Dimmer fixed primary | #D0BCFF | #D0BCFF |
| `on_primary_fixed` | Text on `primary_fixed` and `primary_fixed_dim` | #21005D | #21005D |
| `on_primary_fixed_variant` | Lower-emphasis text on fixed primary | #4F378B | #4F378B |
| `secondary` | Less prominent components; Tesserae focus ring colour (see [[Focus Ring]]) | #625B71 | #CCC2DC |
| `on_secondary` | Text and icons on `secondary` | #FFFFFF | #332D41 |
| `secondary_container` | Less prominent fill: tonal button, selected navigation item | #E8DEF8 | #4A4458 |
| `on_secondary_container` | Text and icons on `secondary_container` | #1D192B | #E8DEF8 |
| `secondary_fixed` | Secondary container that keeps its tone in both schemes | #E8DEF8 | #E8DEF8 |
| `secondary_fixed_dim` | Dimmer fixed secondary | #CCC2DC | #CCC2DC |
| `on_secondary_fixed` | Text on fixed secondary | #1D192B | #1D192B |
| `on_secondary_fixed_variant` | Lower-emphasis text on fixed secondary | #4A4458 | #4A4458 |
| `tertiary` | Contrasting accent that balances primary and secondary | #7D5260 | #EFB8C8 |
| `on_tertiary` | Text and icons on `tertiary` | #FFFFFF | #492532 |
| `tertiary_container` | Contrasting accent fill | #FFD8E4 | #633B48 |
| `on_tertiary_container` | Text and icons on `tertiary_container` | #31111D | #FFD8E4 |
| `tertiary_fixed` | Tertiary container that keeps its tone in both schemes | #FFD8E4 | #FFD8E4 |
| `tertiary_fixed_dim` | Dimmer fixed tertiary | #EFB8C8 | #EFB8C8 |
| `on_tertiary_fixed` | Text on fixed tertiary | #31111D | #31111D |
| `on_tertiary_fixed_variant` | Lower-emphasis text on fixed tertiary | #633B48 | #633B48 |
| `error` | Errors: invalid field outline, error text, destructive emphasis | #B3261E | #F2B8B5 |
| `on_error` | Text and icons on `error` | #FFFFFF | #601410 |
| `error_container` | Error fill (banner, field error background) | #F9DEDC | #8C1D18 |
| `on_error_container` | Text and icons on `error_container` | #410E0B | #F9DEDC |
| `surface_dim` | Surface that stays dimmer than `surface` in both schemes | #DED8E1 | #141218 |
| `surface` | Default background of windows, panels and pages | #FEF7FF | #141218 |
| `surface_tint` | Equals `primary`; names the tint colour; Tesserae applies no tint overlay (see [[Elevation]]) | #6750A4 | #D0BCFF |
| `surface_bright` | Surface that stays brighter than `surface` in both schemes | #FEF7FF | #3B383E |
| `surface_container_lowest` | Lowest-emphasis container, below `surface_container_low` | #FFFFFF | #0F0D13 |
| `surface_container_low` | Low-emphasis container: elevated card (level 1) | #F7F2FA | #1D1B20 |
| `surface_container` | Default container: menu, rich tooltip, navigation bar (level 2) | #F3EDF7 | #211F26 |
| `surface_container_high` | High-emphasis container: dialog, search bar (level 3) | #ECE6F0 | #2B2930 |
| `surface_container_highest` | Highest-emphasis container: filled text field, segmented controls | #E6E0E9 | #36343B |
| `on_surface` | Primary text and icons on any surface role | #1D1B20 | #E6E0E9 |
| `on_surface_variant` | Secondary text and icons on surface roles; default outline-icon colour | #49454F | #CAC4D0 |
| `outline` | Component boundaries that must be seen (text field border); 3:1 against `surface` required | #79747E | #938F99 |
| `outline_variant` | Decorative dividers only; below 3:1 against `surface` (measured 1.62 light, 1.99 dark) | #CAC4D0 | #49454F |
| `inverse_surface` | Plain tooltip and snackbar container | #322F35 | #E6E0E9 |
| `inverse_on_surface` | Text and icons on `inverse_surface` | #F5EFF7 | #322F35 |
| `surface_variant` | Legacy variant surface (kept for compatibility; prefer container roles) | #E7E0EC | #49454F |
| `background` | Legacy page background (equal to `surface` in the baseline) | #FEF7FF | #141218 |
| `on_background` | Legacy text on `background` | #1D1B20 | #E6E0E9 |
| `shadow` | Shadow colour (see [[Elevation]]) | #000000 | #000000 |
| `scrim` | Scrim colour (see [[Scrim]]) | #000000 | #000000 |

### Medium and high contrast values

Source: the `latest` token files listed above. The OS high contrast preference selects the high level ([[Theme Following the System]] rule 8).

| Role | Light medium | Light high | Dark medium | Dark high |
|---|---|---|---|---|
| `primary` | #4F378B | #381E72 | #EADDFF | #F6EDFF |
| `on_primary` | #FFFFFF | #FFFFFF | #21005D | #000000 |
| `primary_container` | #6750A4 | #4F378B | #9A82DB | #D0BCFF |
| `on_primary_container` | #FFFFFF | #FFFFFF | #000000 | #000000 |
| `inverse_primary` | #D0BCFF | #D0BCFF | #4F378B | #381E72 |
| `primary_fixed` | #6750A4 | #4F378B | #EADDFF | #EADDFF |
| `primary_fixed_dim` | #4F378B | #381E72 | #D0BCFF | #D0BCFF |
| `on_primary_fixed` | #FFFFFF | #FFFFFF | #000000 | #000000 |
| `on_primary_fixed_variant` | #FFFFFF | #FFFFFF | #381E72 | #000000 |
| `secondary` | #4A4458 | #332D41 | #E8DEF8 | #F6EDFF |
| `on_secondary` | #FFFFFF | #FFFFFF | #1D192B | #000000 |
| `secondary_container` | #625B71 | #4A4458 | #958DA5 | #CCC2DC |
| `on_secondary_container` | #FFFFFF | #FFFFFF | #000000 | #000000 |
| `secondary_fixed` | #625B71 | #4A4458 | #E8DEF8 | #E8DEF8 |
| `secondary_fixed_dim` | #4A4458 | #332D41 | #CCC2DC | #CCC2DC |
| `on_secondary_fixed` | #FFFFFF | #FFFFFF | #000000 | #000000 |
| `on_secondary_fixed_variant` | #FFFFFF | #FFFFFF | #332D41 | #000000 |
| `tertiary` | #633B48 | #492532 | #FFD8E4 | #FFECF1 |
| `on_tertiary` | #FFFFFF | #FFFFFF | #31111D | #000000 |
| `tertiary_container` | #7D5260 | #633B48 | #B58392 | #EFB8C8 |
| `on_tertiary_container` | #FFFFFF | #FFFFFF | #000000 | #000000 |
| `tertiary_fixed` | #7D5260 | #633B48 | #FFD8E4 | #FFD8E4 |
| `tertiary_fixed_dim` | #633B48 | #492532 | #EFB8C8 | #EFB8C8 |
| `on_tertiary_fixed` | #FFFFFF | #FFFFFF | #000000 | #000000 |
| `on_tertiary_fixed_variant` | #FFFFFF | #FFFFFF | #492532 | #000000 |
| `error` | #8C1D18 | #601410 | #F9DEDC | #FCEEEE |
| `on_error` | #FFFFFF | #FFFFFF | #410E0B | #000000 |
| `error_container` | #B3261E | #8C1D18 | #E46962 | #F2B8B5 |
| `on_error_container` | #FFFFFF | #FFFFFF | #000000 | #000000 |
| `surface_dim` | #DED8E1 | #DED8E1 | #141218 | #141218 |
| `surface` | #FEF7FF | #FEF7FF | #141218 | #141218 |
| `surface_tint` | #4F378B | #381E72 | #EADDFF | #F6EDFF |
| `surface_bright` | #FEF7FF | #FEF7FF | #3B383E | #3B383E |
| `surface_container_lowest` | #FFFFFF | #FFFFFF | #0F0D13 | #0F0D13 |
| `surface_container_low` | #F7F2FA | #F7F2FA | #1D1B20 | #1D1B20 |
| `surface_container` | #F3EDF7 | #F3EDF7 | #211F26 | #211F26 |
| `surface_container_high` | #ECE6F0 | #ECE6F0 | #2B2930 | #2B2930 |
| `surface_container_highest` | #E6E0E9 | #E6E0E9 | #36343B | #36343B |
| `on_surface` | #000000 | #000000 | #FFFFFF | #FFFFFF |
| `on_surface_variant` | #322F37 | #000000 | #E7E0EC | #FFFFFF |
| `outline` | #49454F | #322F37 | #AEA9B4 | #F5EEFA |
| `outline_variant` | #79747E | #49454F | #938F99 | #CAC4D0 |
| `inverse_surface` | #322F35 | #322F35 | #E6E0E9 | #E6E0E9 |
| `inverse_on_surface` | #FFFFFF | #FFFFFF | #1D1B20 | #000000 |
| `surface_variant` | #E7E0EC | #E7E0EC | #49454F | #49454F |
| `background` | #FEF7FF | #FEF7FF | #141218 | #141218 |
| `on_background` | #000000 | #000000 | #FFFFFF | #FFFFFF |
| `shadow` | #000000 | #000000 | #000000 | #000000 |
| `scrim` | #000000 | #000000 | #000000 | #000000 |

### Surface container ladder

The container roles replace the earlier tint-by-elevation overlay ([Android Color guide, Using Surface Colors](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md)). Tone values come from the baseline palette (`md-sys-color` light and dark, links above).

| Role | Light tone | Dark tone | Light hex | Dark hex |
|---|---|---|---|---|
| `surface_container_lowest` | neutral 100 | neutral 4 | #FFFFFF | #0F0D13 |
| `surface_container_low` | neutral 96 | neutral 10 | #F7F2FA | #1D1B20 |
| `surface_container` | neutral 94 | neutral 12 | #F3EDF7 | #211F26 |
| `surface_container_high` | neutral 92 | neutral 17 | #ECE6F0 | #2B2930 |
| `surface_container_highest` | neutral 90 | neutral 22 | #E6E0E9 | #36343B |
| `surface_dim` | neutral 87 | neutral 6 | #DED8E1 | #141218 |
| `surface_bright` | neutral 98 | neutral 24 | #FEF7FF | #3B383E |
| `surface` | neutral 98 | neutral 6 | #FEF7FF | #141218 |

### Required pairs and measured contrast ratios

Contrast ratio is the WCAG 2.2 relative-luminance formula. The ratios below were computed from the hex tables above for this note; the contrast script in AC-COL-3 reproduces them. Minimum text pair ratio across the table: light standard 6.44, dark standard 7.17, light medium 6.44, dark medium 6.50, light high 9.11, dark high 12.27.

| Pair | Light std | Dark std | Light med | Dark med | Light high | Dark high |
|---|---|---|---|---|---|---|
| `on_primary` on `primary` | 6.44 | 7.71 | 9.33 | 13.32 | 13.15 | 18.48 |
| `on_primary_container` on `primary_container` | 13.32 | 7.23 | 6.44 | 6.59 | 9.33 | 12.32 |
| `on_secondary` on `secondary` | 6.45 | 7.74 | 9.30 | 13.24 | 13.19 | 18.48 |
| `on_secondary_container` on `secondary_container` | 13.24 | 7.19 | 6.45 | 6.63 | 9.30 | 12.32 |
| `on_tertiary` on `tertiary` | 6.47 | 7.75 | 9.33 | 13.18 | 13.17 | 18.52 |
| `on_tertiary_container` on `tertiary_container` | 13.18 | 7.20 | 6.47 | 6.63 | 9.33 | 12.36 |
| `on_error` on `error` | 6.54 | 7.66 | 9.11 | 12.77 | 13.08 | 18.60 |
| `on_error_container` on `error_container` | 12.77 | 7.17 | 6.54 | 6.50 | 9.11 | 12.30 |
| `on_surface` on `surface` | 16.23 | 14.35 | 19.96 | 18.59 | 19.96 | 18.59 |
| `on_surface` on `surface_container_lowest` | 17.07 | 14.90 | 21.00 | 19.31 | 21.00 | 19.31 |
| `on_surface` on `surface_container_highest` | 13.17 | 9.47 | 16.20 | 12.27 | 16.20 | 12.27 |
| `on_surface_variant` on `surface` | 8.88 | 10.91 | 12.50 | 14.41 | 19.96 | 18.59 |
| `on_surface_variant` on `surface_container_highest` | 7.21 | 7.20 | 10.14 | 9.51 | 16.20 | 12.27 |
| `inverse_on_surface` on `inverse_surface` | 11.65 | 10.17 | 13.18 | 13.17 | 13.18 | 16.20 |
| `on_background` on `background` | 16.23 | 14.35 | 19.96 | 18.59 | 19.96 | 18.59 |
| `on_primary_fixed` on `primary_fixed` | 13.32 | 13.32 | 6.44 | 16.29 | 9.33 | 16.29 |
| `on_secondary_fixed` on `secondary_fixed` | 13.24 | 13.24 | 6.45 | 16.24 | 9.30 | 16.24 |
| `on_tertiary_fixed` on `tertiary_fixed` | 13.18 | 13.18 | 6.47 | 16.19 | 9.33 | 16.19 |

Non-text pairs (measured against `surface` of the same scheme and level):

| Pair | Light std | Dark std | Light med | Dark med | Light high | Dark high |
|---|---|---|---|---|---|---|
| `outline` on `surface` | 4.33 | 5.87 | 8.88 | 8.09 | 12.50 | 16.37 |
| `primary` on `surface` | 6.12 | 10.91 | 8.87 | 14.42 | 12.50 | 16.36 |
| `secondary` on `surface` | 6.13 | 10.91 | 8.84 | 14.37 | 12.54 | 16.36 |
| `error` on `surface` | 6.21 | 10.89 | 8.66 | 14.62 | 12.44 | 16.47 |

`outline_variant` on `surface` measures 1.62 (light standard) and 1.99 (dark standard). It fails the 3:1 non-text threshold, so it is a decorative divider colour only (Rules 5).

### Seed generation compared with the published baseline

Generating a scheme from the seed `#6750A4` with the tonal-spot method gives values that differ from the published baseline in 19 of the 49 light roles. The seed scheme is what a project with its own seed gets; the published baseline is what an application with no seed gets ([[Theme Following the System]] rule 7). The values below were produced by calling tess-ui's `color_scheme` read-only for this note (`tess-ui:src/tess_ui/tokens.py`).

| Role | Published light | Seed-generated light | tess-ui no-theme light | Published dark | Seed-generated dark |
|---|---|---|---|---|---|
| `primary` | #6750A4 | #65558F | #6750A4 | #D0BCFF | #CFBDFE |
| `on_primary_container` | #21005D | #201047 | #21005D | #EADDFF | #E9DDFF |
| `secondary` | #625B71 | #625B71 | #625B71 | #CCC2DC | #CBC2DB |
| `surface` | #FEF7FF | #FDF7FF | #FFFBFE | #141218 | #141218 |
| `surface_container` | #F3EDF7 | #F2ECF4 | #F3EDF7 | #211F26 | #211F24 |
| `inverse_surface` | #322F35 | #322F35 | #313033 | #E6E0E9 | #E6E0E9 |
| `outline` | #79747E | #7A757F | #79747E | #938F99 | #948F99 |
| `surface_tint` | #6750A4 | #65558F | #65558F | #D0BCFF | #CFBDFE |
| `error_container` | #F9DEDC | #FFDAD6 | #FFDAD6 | #8C1D18 | #93000A |

tess-ui's no-theme scheme overlays 24 older published values on the generated scheme. The overlay is the 2021 baseline (`surface` `#FFFBFE`, `inverse_surface` `#313033`); the 2022 baseline that this specification selects has `surface` `#FEF7FF` and `inverse_surface` `#322F35`.

### Mapping of the tess-shell flat roles

tess-shell keeps its own 12 roles (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`, schema `color` group) and does not import tess-ui (shell ADR-0006). The mapping documents how each shell role reads in this vocabulary ([[ADR-0001 MD3 role names are the specification vocabulary]]). The contrast figures below were computed for this note from the values in the shipped theme.

| Shell role | Dark / Light / High_Contrast value | MD3 role | Kind | Note |
|---|---|---|---|---|
| `$color.surface` | #12171D / #F4F7FA / #000000 | `surface` | exact | Ground of bars and panels. |
| `$color.surface_raised` | #1B222B / #FFFFFF / #000000 | `surface_container` | nearest | Popups, buttons and rich tooltips sit one container step above `surface`. A plain tooltip uses `inverse_surface` (see [[Tooltip]]). |
| `$color.on_surface` | #E4EAF1 / #16202B / #FFFFFF | `on_surface` | exact | Text and icons on a surface. |
| `$color.on_surface_muted` | #9FAEBF / #4A5967 / #FFFFFF | `on_surface_variant` | exact | Secondary text. Disabled content is `on_surface` at 38 percent ([[State Layers]]), not this role. |
| `$color.primary` | #5B97C9 / #2F6B9A / #8CC4F2 | `primary` | exact | Filled slider, checked toggle. |
| `$color.on_primary` | #08121C / #FFFFFF / #000000 | `on_primary` | exact |  |
| `$color.accent` | #4682B4 / inherits / #8CC4F2 | seed colour (input), then `primary` | no role | The desktop accent is an input to scheme generation, not an output role. Until the shell generates a scheme, `accent` stays a shell-only role. #needs-verification (design choice). |
| `$color.error` | #F2958C / #B3261E / inherits | `error` | exact | Critical state. |
| `$color.warning` | #E6BB6A / #8A5A00 / inherits | custom colour `warning` | extension | MD3 has no warning role. See the extension rule in Rules. |
| `$color.success` | #8CCB9A / #2E6B34 / inherits | custom colour `success` | extension | Same rule. |
| `$color.outline` | #55657A / #7A8896 / #FFFFFF | `outline` | exact | Borders and tracks that must be seen. |
| `$color.scrim` | #000000 / inherits / inherits | `scrim` | exact | Opacity 0.32 per [[Scrim]]. |

Measured contrast of the shipped shell theme (WCAG formula):

| Pair (shell role names) | Dark | Light | High_Contrast |
|---|---|---|---|
| `on_surface` on `surface` | 14.87 | 15.31 | 21.00 |
| `on_surface` on `surface_raised` | 13.23 | 16.46 | 21.00 |
| `on_surface_muted` on `surface` | 7.96 | 6.70 | 21.00 |
| `on_surface_muted` on `surface_raised` | 7.08 | 7.20 | 21.00 |
| `on_primary` on `primary` | 6.03 | 5.69 | 11.29 |
| `error` on `surface` | 8.11 | 6.08 | 9.45 |
| `warning` on `surface` | 10.02 | 5.51 | 11.68 |
| `success` on `surface` | 9.54 | 5.98 | 11.12 |
| `accent` on `surface` | 4.38 | 3.82 | 11.29 |
| `primary` on `surface` (non-text) | 5.76 | 5.29 | 11.29 |
| `outline` on `surface` (non-text) | 3.03 | 3.37 | 21.00 |

### Tesserae extensions

| Extension | Definition | Source |
|---|---|---|
| Alpha suffix | `role@N%` is the role colour with alpha N percent (0 to 100). Contrast is measured on the colour composited over its background. | `tess-ui:src/tess_ui/tokens.py` `resolve_color` |
| Custom colours | A colour outside the 49 roles (warning, success) is a named custom colour with four derived roles: `x`, `on_x`, `x_container`, `on_x_container`, each pair meeting Rules 3. | This note |

## Rules

1. Components take colours from roles by name. A hex literal in a view, stylesheet or module is allowed only for: a user-authored colour, content (image, syntax highlighting, terminal palette), and a brand mark.
2. A surface colour is always paired with its `on_` role for text and icons placed on it (table of required pairs).
3. Text and icons meet 4.5:1 against the colour behind them ([WCAG 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum)); large-scale text (24 px regular or 18.67 px bold and above, being 18 and 14 point) meets 3:1. Non-text parts that identify a component or its state, and focus indicators, meet 3:1 against adjacent colours ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)). Inactive components and pure decoration are exempt.
4. At the high contrast level every text pair meets 7:1 ([WCAG 1.4.6](https://www.w3.org/TR/WCAG22/#contrast-enhanced), Tesserae choice for the high level); the measured minimum in the baseline is 9.11 light and 12.27 dark.
5. `outline` draws boundaries that must be perceived (text field border, switch track outline). `outline_variant` draws dividers that carry no meaning; no information depends on it.
6. Colour is never the only cue for state, error or action ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)): a second cue (icon, text, shape, position) accompanies it.
7. A project with a seed generates all 49 roles for light and dark and for each contrast level from that seed. A project without a seed uses the published baseline tables above and still follows light and dark.
8. The role set is closed: a project adds colours only as custom colours with the four-role extension, never as one-off hex values.
9. Disabled content uses `on_surface` at 38 percent and disabled containers `on_surface` at 12 percent ([[State Layers]]); disabled content is exempt from the contrast rule.
10. Every surface follows the scheme, not only overlays: the window background, each panel, each row and each popup resolve their colour from roles at the time the scheme changes.

## Acceptance criteria

- [ ] AC-COL-1: Token test. For seed `#6750A4`, the scheme generator returns exactly the 49 role names of the Role set table for each of light and dark at each of the standard, medium and high levels, and no value is missing or duplicated. Pass: set of names equals the table, 6 schemes.
- [ ] AC-COL-2: Token test. A project that claims the baseline fallback returns, for every role in the Role set table, the hex in the Light and Dark columns (exact 24-bit match, alpha 255). Pass: 98 of 98 values equal.
- [ ] AC-COL-3: Contrast script. For every pair in the required-pairs table, in each of the six schemes, the script computes the WCAG ratio from the shipped values. Pass: text pairs at least 4.5 at the standard and medium levels and at least 7 at the high level; the non-text pairs `outline`, `primary`, `secondary`, `error` on `surface` at least 3 at every level. The script output lists each ratio and exits non-zero on a failure.
- [ ] AC-COL-4: Contrast script over shipped project themes. The same script runs over each project theme file (tess-shell `Default_Theme.tdl` Dark, Light, High_Contrast; each tess-ui app theme with its seed) with the pairs mapped through the shell mapping table. Pass: no text pair under 4.5 and no non-text pair under 3, or the failing pair appears in a recorded exemption list.
- [ ] AC-COL-5: Token test (static scan). No view stylesheet, module file or Python view code contains a colour literal (`#RRGGBB`, `rgb(`) outside an allow-list of the three exemptions in Rules 1. Pass: scan reports zero hits.
- [ ] AC-COL-6: Pixel check. Render each top-level surface type of the project with the dark scheme: window background, each panel, list and tree rows, popup. Sample the background pixel of each. Pass: relative luminance below 0.05 for every dark sample and above 0.6 for every light sample (the baseline dark surface roles measure 0.004 to 0.041, the light ones 0.70 to 1.0). This is the check that catches an all-white application under a dark scheme.
- [ ] AC-COL-7: Token test. Every row of the shell mapping table resolves: each of the 12 shell roles maps to a role named in the Role set table or to a custom colour with the four derived roles. Pass: 12 of 12 documented.
- [ ] AC-COL-8: Scripted scheme switch. Change the scheme from light to dark at runtime and capture each surface of AC-COL-6. Pass: no sampled surface keeps a light-scheme colour (luminance rule of AC-COL-6) after 200 ms.
- [ ] AC-COL-9: Contrast script on composited colours. For each role used with an alpha suffix, the ratio is computed on the colour composited over the actual background. Pass: the composited pair meets the threshold of Rules 3.
- [ ] AC-COL-10: Review. Each colour used for a state or error has a second cue per Rules 6. Pass: reviewer finds none that is colour only.

## Status in code

Evidence: [[Owner Feedback 2026-11-20]] F1 (dark system theme, white application) and the shell Launcher unreadable without a stylesheet.

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/tokens.py` (`ROLES`, `color_scheme`, `baseline_scheme`, `BASELINE`) | Partly meets. AC-COL-1 meets (49 roles generated, light and dark, contrast level from -1 to 1; only 0 and 1 are used by the app). AC-COL-2 fails: the no-theme scheme overlays 2021 values and differs from the published 2022 baseline in 19 of 49 light roles. Four light `on_*_container` roles are forced to tone 10 (`_TONE_10_LIGHT`), which matches the standard table. AC-COL-3 and AC-COL-4 absent (no contrast script). AC-COL-5 not scanned. AC-COL-6 fails for an App with no `theme_seed` (no scheme, ignores `dark`; the config app now sets one). |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`; schema `color` group | Partly meets. 12 flat roles map as documented above (AC-COL-7 meets in this note). Measured contrast of the shipped Dark, Light and High_Contrast pairs passes the thresholds in the measured table for every text pair (lowest `on_surface_muted` pair 6.70). `accent` on `surface` measures 4.38 dark and 3.82 light: it passes the 3:1 non-text rule and fails 4.5:1, so it must not carry text. AC-COL-3 and AC-COL-4 absent: no script exists (shell vault Accessibility rule 9 asks for it). `$color.scrim` is defined and no surface uses it. |
| tre | `tre:docs/guide/painting.md`; no role set | Not applicable by design: the engine takes 8-bit sRGB colours and has no roles. Defaults: text fill `(0,0,0,255)`, scroll thumb `#CAC4D0` at 55 percent, initial clear colour `#6750A4`. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Role names from MD3, values from a project's own flat roles in tess-shell (12 roles, mapping above) | The shell is independent of tess-ui and ships its own theme format | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Light `on_*_container` roles at tone 10 (2022 scale), not tone 30 (latest token set) | The 2022 role scale is the baseline | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| High contrast level requires 7:1 for every text pair | Tesserae choice, matches WCAG 1.4.6; the measured baseline already meets it | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| `outline_variant` limited to decoration | Its measured contrast is under 3:1 | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Custom colours (warning, success) with four derived roles | MD3 defines the extension method but no warning or success role | [[ADR-0001 MD3 role names are the specification vocabulary]] |
