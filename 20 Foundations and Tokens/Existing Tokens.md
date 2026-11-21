---
title: Existing Tokens
type: tokens
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [tokens, foundation, inventory]
related: ["[[Inventory]]", "[[Plan]]", "[[Gaps and Contradictions]]"]
depends_on: []
---

# Existing Tokens

The tokens and defaults that exist in code today, with values and files, and where tess-ui, the shell and Material Design 3 (MD3) differ. Phase 0 result: nothing here is a decision. The target values are set in the foundation notes written in later phases, each with a proposed ADR.

> [!note] Correction (Phase 1)
> tess-ui's elevation shadow formulas equal Material Web's; the remark below that they are a legacy formula is wrong. See [[Elevation]] and [[MD3 Verification Status]].

> [!info] Sources and trust
> Values were read from the project sources (`tess-ui:`, `tess-shell:`, `tre:`, `shell-vault:` path prefixes, relative to each project root). MD3 values quoted from memory by the readers carry `#needs-verification` until checked against [m3.material.io](https://m3.material.io) (see [[Open Questions]] OQ-12). The four sections below the comparison keep each project's table whole.

## Comparison at a glance

| Group | tess-ui | tess-shell | tre engine | MD3 |
|---|---|---|---|---|
| Colour roles | 49 MD3 roles generated from a seed (baseline seed `#6750A4`), light and dark; no-theme baseline of 24 roles that differs from the generated scheme (primary `#6750A4` against generated `#65558F`) | 12 flat roles (surface, surface_raised, on_surface, on_surface_muted, primary, on_primary, accent, error, warning, success, outline, scrim); dark steel-blue default (accent `#4682B4`); Light and High_Contrast overrides | none (8-bit sRGB, no roles) | tonal palette roles, light, dark, contrast levels standard, medium, high |
| Type scale | 15 MD3 roles; tracking 0 on all (`MD3_TRACKING` present, unused) | 5 roles: caption 12/16, label 13/500/18, body 14/20, title 18/500/24, display 28/36; names reuse MD3 words with other meanings | none; default Roboto 16 px, weight 400; bundled Roboto Regular and Medium | 15 roles with tracking per role |
| Shape | none 0, extra_small 4, small 8, medium 12, large 16, extra_large 28, full; per-component literals in view stylesheets | 0, 4, 8, 16, 999 (small is 4, equal to MD3 extra small) | per-node radius | extra small 4 to extra large 28, full; Expressive adds larger steps #needs-verification |
| Elevation | levels 0 to 5 as key plus ambient shadow pairs; no surface-tint overlay; ambient spread non-zero | one shadow scaled by a percentage (`Elevation.Max` `#00000066` in the theme, fallback `#00000040` in code); `Reach 64` kept in code although the vault dropped it | shadow list per node | five levels, tone-based surface containers; tint overlay retired #needs-verification |
| Motion | MD3 duration steps short1 to extra_long4 (50 to 1000 ms), 10 easings, spring; emphasized curve differs between `theme.py` and `spec/transition.py`; stylesheet literals 150 and 200 ms | 100, 200, 400 ms and two cubic curves (`standard`, `emphasized`) with no definition in the vault; reduced motion wired in code, theme block empty | default easing linear; reduced motion reported, not enforced | emphasized and standard families, accelerate and decelerate variants |
| Spacing | none; literals in stylesheets (one off-grid Snackbar padding 14) | `$space.step_1` to `step_8` (step_1 is 2 px) | none | no spacing tokens; 4 dp grid and per-component values |
| Density | none; only `Tree` has `Compact` (40 px rows instead of 56) | none; control heights are literals (Button 32, MenuItem 28, Checkbox 18, Toggle 40 by 22) | none; `touch_target_slop` default 0 | density steps for Android components (0, -1, -2, -3) #needs-verification |
| Icon sizes | 24 default; Button size s icon 18; two sets with different view boxes (Symbols 0 -960 960 960, MDI 0 0 24 24) | literals per module; fallback icon `mdi:image-broken-variant` | draws paths and SVG only, 24 by 24 view box | 24 dp default; Symbols axes weight, fill, grade, optical size |
| State layers | hover 8, focus 10, press 10, drag 16 percent; disabled content 38, container 12 percent; keyboard-only focus ring 3 px, 2 px offset, colour `secondary` | none; states change Background, Border_Color or Opacity (hover 0.85, pressed 0.7, disabled 0.5 literals); focus ring `primary`, 2 px | none by design (removed in 0.3.5); supplies `focus_visible` | hover 8, focus 10, press 10, drag 16 percent |
| Ripple | Material Web timings (press grow 450 ms, fade in 105, minimum press 225, release fade 375); shader option | none | none | ripple pattern |
| Scrollbar | colour only (`outline`); size owned by the engine | none; wheel scroll only | thumb 4 px, 2 px margin, 32 px minimum, 6 px grab slop, radius 2, fill `#CAC4D0` at 55 percent, no track, no auto-hide | scrollbars are platform concerns |
| Tooltip | 500 ms hover delay (code comment cites Material 3 without a link), immediate on keyboard focus, 150 ms rich grace; radius 4 or 12; literal fonts | `Tooltip` key and Popup with `Tooltip: true`; six modules repeat the same card literals | no timers; layer only | plain and rich tooltips; delays not numeric #needs-verification |
| Theme following the system | follows OS light and dark; starts dark on macOS and Windows and flips on the first frame | dark by default; Light and Dark blocks exist, Dark block empty | reports the preference | not applicable |
| High contrast | contrast 0 or 1 only | High_Contrast override, headless tests only | reported, not enforced | contrast levels standard, medium, high |

## Differences that need a decision

1. Two token vocabularies: tess-ui uses MD3 role names, the shell uses its own 12 names. The shell never imports tess-ui (ADR-0006 of the shell project), so parity is not enforced by code. See [[Open Questions]] OQ-02.
2. State feedback: tess-ui implements MD3 state layers and a ripple; the shell uses opacity literals. See OQ-05.
3. Motion: emphasized easing exists in two versions in tess-ui, and the shell's two curves have no recorded numbers.
4. Density and scrollbars have no token anywhere; both are owner-feedback items (config-app demo of 2026-11-20). See OQ-03 and OQ-04.
5. Elevation: no tonal elevation in any project; tess-ui and the shell use shadows only.
6. Contrast: the shell vault requires a contrast script over shipped themes (4.5 to 1 text, 3 to 1 large text and icons) and none exists.


## Current values: tess-ui


Sources: `tess-ui:src/tess_ui/tokens.py`, `tess-ui:src/tess_ui/theme.py`, `tess-ui:src/tess_ui/spec/default_theme.tdl`, `tess-ui:src/tess_ui/interaction.py`, `tess-ui:src/tess_ui/ripple.py`, `tess-ui:src/tess_ui/focusring.py`, `tess-ui:src/tess_ui/controls.py`, `tess-ui:src/tess_ui/screen_transition.py`, `tess-ui:src/tess_ui/composed.py`, `tess-ui:src/tess_ui/views/*_Stylesheet.tdl`, `tess-ui:docs/themes/index.md`. Colour values below were produced by calling `tokens.color_scheme` read-only. MD3 comparisons from memory of the published spec; unsure ones are marked #needs-verification.

### Colour roles

Generation: `materialyoucolor` SchemeTonalSpot, `spec_version="2021"`, seed to 49 roles, light and dark, contrast level -1..1 (`tess-ui:src/tess_ui/tokens.py` `color_scheme`). Four light `on_*_container` roles are forced to tone 10 (`_TONE_10_LIGHT`). Seed order: `App(theme_seed=)`, custom theme `Seed`, default theme `Seed`; the shipped default theme has no seed. With no seed the baseline palette applies (`baseline_scheme`: seed #6750A4 scheme overlaid with 24 published `BASELINE` values). Values below are the generated scheme for seed #6750A4.

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `primary` | light #65558F; dark #CFBDFE | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #6750A4. MD3: baseline light #6750A4 #needs-verification |
| `on_primary` | light #FFFFFF; dark #36275D | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` equals it. MD3: baseline light #FFFFFF #needs-verification |
| `primary_container` | light #E9DDFF; dark #4D3D75 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #EADDFF. MD3: baseline light #EADDFF #needs-verification |
| `on_primary_container` | light #201047; dark #E9DDFF | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #21005D. MD3: baseline light #21005D #needs-verification |
| `inverse_primary` | light #CFBDFE; dark #65558F | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #D0BCFF. MD3: baseline light #D0BCFF #needs-verification |
| `primary_fixed` | light #E9DDFF; dark #E9DDFF | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `primary_fixed_dim` | light #CFBDFE; dark #CFBDFE | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_primary_fixed` | light #201047; dark #201047 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_primary_fixed_variant` | light #4D3D75; dark #4D3D75 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `secondary` | light #625B71; dark #CBC2DB | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` equals it. MD3: baseline light #625B71 #needs-verification |
| `on_secondary` | light #FFFFFF; dark #332D41 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `secondary_container` | light #E8DEF8; dark #4A4458 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` equals it. MD3: baseline light #E8DEF8 #needs-verification |
| `on_secondary_container` | light #1E192B; dark #E8DEF8 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #1D192B. MD3: baseline light #1D192B #needs-verification |
| `secondary_fixed` | light #E8DEF8; dark #E8DEF8 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `secondary_fixed_dim` | light #CBC2DB; dark #CBC2DB | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_secondary_fixed` | light #1E192B; dark #1E192B | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_secondary_fixed_variant` | light #4A4458; dark #4A4458 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `tertiary` | light #7E5260; dark #EFB8C8 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_tertiary` | light #FFFFFF; dark #4A2532 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `tertiary_container` | light #FFD9E3; dark #633B48 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #FFD8E4. MD3: baseline light #FFD8E4 #needs-verification |
| `on_tertiary_container` | light #31101D; dark #FFD9E3 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #31111D. MD3: baseline light #31111D #needs-verification |
| `tertiary_fixed` | light #FFD9E3; dark #FFD9E3 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `tertiary_fixed_dim` | light #EFB8C8; dark #EFB8C8 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_tertiary_fixed` | light #31101D; dark #31101D | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_tertiary_fixed_variant` | light #633B48; dark #633B48 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `error` | light #BA1A1A; dark #FFB4AB | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #B3261E. MD3: baseline light #B3261E #needs-verification |
| `on_error` | light #FFFFFF; dark #690005 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` equals it. MD3: baseline light #FFFFFF #needs-verification |
| `error_container` | light #FFDAD6; dark #93000A | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_error_container` | light #410002; dark #FFDAD6 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `surface_dim` | light #DED8E0; dark #141218 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `surface` | light #FDF7FF; dark #141218 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #FFFBFE. MD3: baseline light #FFFBFE #needs-verification |
| `surface_tint` | light #65558F; dark #CFBDFE | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `surface_bright` | light #FDF7FF; dark #3B383E | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `surface_container_lowest` | light #FFFFFF; dark #0F0D13 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `surface_container_low` | light #F8F2FA; dark #1D1B20 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #F7F2FA. MD3: baseline light #F7F2FA #needs-verification |
| `surface_container` | light #F2ECF4; dark #211F24 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #F3EDF7. MD3: baseline light #F3EDF7 #needs-verification |
| `surface_container_high` | light #ECE6EE; dark #2B292F | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #ECE6F0. MD3: baseline light #ECE6F0 #needs-verification |
| `surface_container_highest` | light #E6E0E9; dark #36343A | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` equals it. MD3: baseline light #E6E0E9 #needs-verification |
| `on_surface` | light #1D1B20; dark #E6E0E9 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` equals it. MD3: baseline light #1D1B20 #needs-verification |
| `on_surface_variant` | light #49454E; dark #CAC4CF | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #49454F. MD3: baseline light #49454F #needs-verification |
| `outline` | light #7A757F; dark #948F99 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #79747E. MD3: baseline light #79747E #needs-verification |
| `outline_variant` | light #CAC4CF; dark #49454E | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #CAC4D0. MD3: baseline light #CAC4D0 #needs-verification |
| `inverse_surface` | light #322F35; dark #E6E0E9 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #313033. MD3: baseline light #313033 #needs-verification |
| `inverse_on_surface` | light #F5EFF7; dark #322F35 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` (no-theme) light override #F4EFF4. MD3: baseline light #F4EFF4 #needs-verification |
| `surface_variant` | light #E7E0EB; dark #49454E | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `background` | light #FDF7FF; dark #141218 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `on_background` | light #1D1B20; dark #E6E0E9 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `shadow` | light #000000; dark #000000 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated. MD3: baseline light see m3 baseline scheme #needs-verification |
| `scrim` | light #000000; dark #000000 | `tess-ui:src/tess_ui/tokens.py` (`color_scheme`, `ROLES`) | seed #6750A4 generated; `BASELINE` equals it. MD3: baseline light #000000 #needs-verification |
| `seed` (default) | absent in shipped default theme; baseline #6750A4 used when no seed | `tess-ui:src/tess_ui/tokens.py` `BASELINE`/`baseline_scheme` | MD3: baseline seed #6750A4 |
| `contrast` | 0.0 standard; 1.0 when OS asks high contrast (`App(high_contrast="system")`) | `tess-ui:src/tess_ui/theme.py` `Theme.contrast`, `tess-ui:src/tess_ui/app.py` | MD3 levels: standard, medium, high (-1/0/0.5/1 style) #needs-verification; only 0 and 1 are used by the app |
| scheme mode | `dark="system"` default; True/False fix it; headless and macOS/Windows start dark | `tess-ui:src/tess_ui/app.py` (`dark`, `_os_dark`) | MD3: light/dark both specified |
| alpha suffix | `role@N%` scales alpha (0..100) | `tess-ui:src/tess_ui/tokens.py` `resolve_color` | Tesserae extension |

### Type scale

Family Roboto for all roles (bundled families: Roboto, Noto Sans Arabic, Hack Nerd Font Mono; `tess-ui:docs/themes/index.md`). Line height is a multiple of font size. Tracking is 0 for every role unless a theme sets it (`MD3_TRACKING` holds MD3's values but is not applied). `tess-ui:src/tess_ui/tokens.py` `TYPE_SCALE`.

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `display_large` | 400 / 57 px / lh 1.12 (63.8) / track 0 | `tess-ui:src/tess_ui/tokens.py` TYPE_SCALE | MD3: 57/64, -0.25 tracking |
| `display_medium` | 400 / 45 / 1.16 (52.2) / 0 | same | MD3: 45/52, 0 |
| `display_small` | 400 / 36 / 1.22 (43.9) / 0 | same | MD3: 36/44, 0 |
| `headline_large` | 400 / 32 / 1.25 (40) / 0 | same | MD3: 32/40, 0 |
| `headline_medium` | 400 / 28 / 1.29 (36.1) / 0 | same | MD3: 28/36, 0 |
| `headline_small` | 400 / 24 / 1.33 (31.9) / 0 | same | MD3: 24/32, 0 |
| `title_large` | 400 / 22 / 1.27 (27.9) / 0 | same | MD3: 22/28, 0 |
| `title_medium` | 500 / 16 / 1.50 (24) / 0 | same | MD3: 16/24, 0.15 tracking |
| `title_small` | 500 / 14 / 1.43 (20) / 0 | same | MD3: 14/20, 0.1 |
| `body_large` | 400 / 16 / 1.50 (24) / 0 | same | MD3: 16/24, 0.5 |
| `body_medium` | 400 / 14 / 1.43 (20) / 0 | same | MD3: 14/20, 0.25 |
| `body_small` | 400 / 12 / 1.33 (16) / 0 | same | MD3: 12/16, 0.4 |
| `label_large` | 500 / 14 / 1.43 (20) / 0 | same | MD3: 14/20, 0.1 |
| `label_medium` | 500 / 12 / 1.33 (16) / 0 | same | MD3: 12/16, 0.5 |
| `label_small` | 500 / 11 / 1.45 (16) / 0 | same | MD3: 11/16, 0.5 |
| `MD3_TRACKING` | display_large -0.25; title_medium 0.15; title_small 0.1; body_large 0.5; body_medium 0.25; body_small 0.4; label_large 0.1; label_medium 0.5; label_small 0.5; others 0 | `tess-ui:src/tess_ui/tokens.py` MD3_TRACKING | defined, not applied by default (`tracking` 0 in TYPE_SCALE) |
| typography override | per role fields `font_family font_weight font_size line_height tracking`; custom entry replaces default entry, no merge | `tess-ui:src/tess_ui/theme.py` `_TYPE_FIELDS` | TextInput keeps its own font (docs) |

### Shape

`tess-ui:src/tess_ui/tokens.py` `SHAPES`, `FULL_RADIUS`.

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `none` | 0 px | tokens.py SHAPES | MD3: 0 dp |
| `extra_small` | 4 px | tokens.py SHAPES | MD3: 4 dp |
| `small` | 8 px | tokens.py SHAPES | MD3: 8 dp |
| `medium` | 12 px | tokens.py SHAPES | MD3: 12 dp |
| `large` | 16 px | tokens.py SHAPES | MD3: 16 dp |
| `extra_large` | 28 px | tokens.py SHAPES | MD3: 28 dp |
| `full` | 9999 px (engine clamps to half shorter side) | tokens.py FULL_RADIUS | MD3: full / 50% |
| `large_increased`, `extra_large_increased`, `extra_extra_large` | absent | tokens.py | MD3 Expressive adds 20, 32, 48 dp #needs-verification; Button sheet uses literal 12/16/28 instead |

#### Per-component corner radius and elevation, shipped defaults

`tess-ui:src/tess_ui/spec/default_theme.tdl` (`Components`, applies to widgets made in Python); views take shape from their own `*_Stylesheet.tdl`.

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| Rect / Container | radius 0 | default_theme.tdl:30,34 | |
| Checkbox | radius 2 | default_theme.tdl:38 | MD3: 2 dp |
| Slider | radius 8 | default_theme.tdl:42 | |
| TextField | radius 4 | default_theme.tdl:46 | MD3: extra small top 4 (filled) |
| Card | radius 12; Elevated elevation 1 | default_theme.tdl:71-73 | MD3: 12 dp, elevated level 1 |
| Chip | radius 8 | default_theme.tdl:75 | MD3: 8 dp |
| Tooltip | radius 4 | default_theme.tdl:76 | MD3 plain tooltip: extra small 4 dp; rich 12 |
| Dialog | radius 28, elevation 3 | default_theme.tdl:77 | MD3: 28 dp, level 3 |
| Snackbar | radius 4, elevation 3 | default_theme.tdl:78 | MD3: extra small 4, level 3 |
| Popover | radius 12, elevation 2 | default_theme.tdl:79 | |
| Side sheet | radius 16; Modal elevation 1 | default_theme.tdl:80-83 | MD3: modal 16 dp left corners, level 1 |
| Navigation drawer | radius 16; Modal elevation 1; Indicator radius 28 | default_theme.tdl:84-88 | MD3: 16, indicator 28 (full) |
| Navigation rail Indicator | radius 16 | default_theme.tdl:89-91 | MD3: full (pill) for active indicator #needs-verification |
| Search bar / view | radius 28, elevation 3 | default_theme.tdl:92-93 | MD3: full (28 of 56 high), level 3 |
| Date picker day | radius 24 | default_theme.tdl:94 | |
| Time input field, Period selector, Spin box | radius 8 | default_theme.tdl:95-97 | |
| Pagination item | radius 20 | default_theme.tdl:105 | |
| Tabs indicator | radius 3 | default_theme.tdl:106-108 | |
| Badge | dot radius 3; labeled radius 8 | default_theme.tdl:109-112 | MD3 badge: full |
| FAB | elevation 3; small 12, default 16, large 28 | default_theme.tdl:113-118 | MD3: small 12, standard 16, large 28 |
| Extended FAB | radius 16, elevation 3 | default_theme.tdl:119 | |
| Split button tightened | radius 8 | default_theme.tdl:120-122 | |
| Graph node | radius 12 | default_theme.tdl:123 | Tesserae-specific |
| Button sheet (views) | pill (`full`) or square by size: xs 12, s 12, m 16, l 28, xl 28 | `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl:32-55` | MD3 Expressive sizes #needs-verification |
| Dialog sheet (views) | radius 28 (0 fullscreen), padding 24, gap 16, elevation 3 | `tess-ui:src/tess_ui/views/Dialog_Stylesheet.tdl:14-17` | MD3: 28 dp, padding 24 |
| Menu sheet (views) | radius 4, elevation 2, vertical padding 8 | `tess-ui:src/tess_ui/views/Menu_Stylesheet.tdl:14-16` | MD3 menu: extra small 4, level 2, 8 dp vertical |
| Snackbar sheet (views) | radius 4, elevation 3 | `tess-ui:src/tess_ui/views/Snackbar_Stylesheet.tdl:13-14` | |
| Card sheet (views) | radius 12, body padding 16, gap 4 | `tess-ui:src/tess_ui/views/Card_Stylesheet.tdl:13,33` | |
| Chip sheet (views) | radius 8, gap 8, side padding 16 (8 with icon/avatar) | `tess-ui:src/tess_ui/views/Chip_Stylesheet.tdl:13-15` | |

### Elevation

Levels `level_0`..`level_5` = 0..5 (`tokens.py` ELEVATION_LEVELS). Level is turned into two shadows by `elevation_shadows` (`tokens.py`): key shadow 30% black (alpha 77/255) then ambient 15% black (alpha 38/255). Offsets (x 0): 

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| level 0 | no shadow | tokens.py elevation_shadows | MD3: 0 dp |
| level 1 | key y1 blur2 spread0; ambient y1 blur3 spread1 | tokens.py | MD3: 1 dp. Values derived from tre engine-render formula |
| level 2 | key y1 blur2; ambient y2 blur6 spread2 | tokens.py | MD3: 3 dp |
| level 3 | key y1 blur3; ambient y4 blur8 spread3 | tokens.py | MD3: 6 dp |
| level 4 | key y2 blur3; ambient y6 blur10 spread4 | tokens.py | MD3: 8 dp |
| level 5 | key y4 blur4; ambient y8 blur12 spread6 | tokens.py | MD3: 12 dp |
| tint overlay | absent (no surface-tint overlay by level; `surface_tint` role exists only) | tokens.py ROLES | MD3 uses tone-based surface container roles instead of tint since M3 2022 #needs-verification |
| hover/pressed elevation | Button filled/tonal hover 1; elevated hover 2, pressed 1; Fab hover 4, pressed 3; Card elevated hover 2 if actionable else 1 | `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl:88-91`, `Fab_Stylesheet.tdl:33-34`, `Card_Stylesheet.tdl:22` | |
| tooltip rich | elevation 2 shadows | `tess-ui:src/tess_ui/composed.py:811` | plain tooltip has none |

### Motion

Durations (ms), `tess-ui:src/tess_ui/theme.py` DURATIONS. Formula: short n = 50n; medium n = 200+50n; long n = 400+50n; extra_long n = 600+100n, n = 1..4.

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| short1..short4 | 50, 100, 150, 200 | theme.py DURATIONS | MD3: 50/100/150/200 |
| medium1..medium4 | 250, 300, 350, 400 | theme.py DURATIONS | MD3: 250/300/350/400 |
| long1..long4 | 450, 500, 550, 600 | theme.py DURATIONS | MD3: 450/500/550/600 |
| extra_long1..extra_long4 | 700, 800, 900, 1000 | theme.py DURATIONS | MD3: 700/800/900/1000 |
| easing `linear` | linear | theme.py EASINGS | |
| easing `standard` | (0.2, 0, 0, 1) | theme.py EASINGS, spec/transition.py EASINGS | MD3: cubic-bezier(0.2, 0, 0, 1) |
| easing `standard_decelerate` | (0, 0, 0, 1) | same | MD3: (0, 0, 0, 1) |
| easing `standard_accelerate` | (0.3, 0, 1, 1) | same | MD3: (0.3, 0, 1, 1) |
| easing `emphasized` | theme.py (0.2, 0, 0, 1); spec/transition.py (0.3, 0, 0, 1) | theme.py:47, transition.py:36 | DRIFT between the two files. MD3 emphasized is a two-segment path; Material Web approximates with (0.3, 0, 0, 1) #needs-verification |
| easing `emphasized_decelerate` | (0.05, 0.7, 0.1, 1) | both | MD3: (0.05, 0.7, 0.1, 1) |
| easing `emphasized_accelerate` | (0.3, 0, 0.8, 0.15) | both | MD3: (0.3, 0, 0.8, 0.15) |
| easing `spring` | spring; `Theme.spring(bounce)` bounce in (-1,1) | theme.py:49,154 | MD3 Expressive springs (spatial/effects) #needs-verification |
| default transition easing | `standard` | `tess-ui:src/tess_ui/spec/transition.py` DEFAULT_EASING | |
| stylesheet transitions | Button/Fab Corner_Radius 200, Elevation 200, Background 150 ms; Card Elevation 200, Background 150 | `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl:13`, `Fab_Stylesheet.tdl:14`, `Card_Stylesheet.tdl:14` | literal ms, not token names |
| screen transition | out 90 ms, in 210 ms (300 total); container transform one 300 ms move; shared axis slide 30 px | `tess-ui:src/tess_ui/screen_transition.py:25-27` | MD3 fade through 90/210 ms matches; kinds: none, fade_through, shared_axis_x/y/z, container_transform |
| reduced motion | all animation durations 0; no repeating animation | `tess-ui:src/tess_ui/motion.py` | follows OS by default |
| tooltip delay | 500 ms hover, immediate on keyboard focus | `tess-ui:src/tess_ui/composed.py:731` TIP_DELAY | MD3: hover delay not specified numerically #needs-verification; code comment says "Material 3: 500 ms" |
| rich tooltip grace | 150 ms | composed.py:733 TIP_GRACE | |

### Spacing

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| spacing scale | absent: no named spacing tokens in tess-ui; values are literals per stylesheet | `tess-ui:src/tess_ui/views/*_Stylesheet.tdl` | MD3 has no spacing tokens either (4 dp grid / 8 dp layout grid) |
| literals in use | 4, 8, 12, 14, 16, 20, 24, 28, 32, 48, 56, 64 (gaps and paddings) | views stylesheets | multiples of 4 except 14 (Snackbar text top/bottom, `Snackbar_Stylesheet.tdl:25`) |
| list item | padding 16/16/8/8, gap 16 | `tess-ui:src/tess_ui/views/ListItem_Stylesheet.tdl:12-13` | MD3 list item |
| status bar | horizontal padding 8 | `tess-ui:src/tess_ui/views/StatusBar_Stylesheet.tdl:12` | |
| Dock drag threshold | 4 px | `tess-ui:src/tess_ui/docking.py:67` DRAG_THRESHOLD | |
| shell Space tokens (shell_config fixture) | Step_1..Step_8 = 2, 4, 8, 12, 16, 24, 32, 48 | `tess-ui:apps/shell_config/tests/fixtures/shipped/Themes/Default_Theme.tdl` Space block | tess-shell theme vocabulary, not read by tess-ui engine |
| window size classes (width) | compact 0, medium 600, expanded 840, large 1200, extra_large 1600 | `tess-ui:src/tess_ui/tokens.py` WIDTH_CLASSES | MD3: compact <600, medium 600, expanded 840, large 1200, extra-large 1600 |
| window size classes (height) | compact 0, medium 480, expanded 900 | tokens.py HEIGHT_CLASSES | MD3: compact <480, medium 480, expanded 900 |

### Density

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| density scale | absent: no density token or setting in tess-ui code (grep for density found none) | `tess-ui:src/tess_ui` | MD3: density -1..-3 is a Material 2 style concept; M3 specifies none for components #needs-verification |
| size ramp (Expressive) | Button heights xs 32, s 40, m 56, l 96, xl 136; gap 4/8/8/12/16 | `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl:17-21` | MD3 Expressive: xs 32, s 40, m 56, l 96, xl 136 |
| Icon button widths | narrow/default/wide by size (xs 28/32/40, s 32/40/52, m 48/56/72, l 64/96/128, xl 104/136/184) | `tess-ui:src/tess_ui/views/IconButton_Stylesheet.tdl:25` | MD3 Expressive #needs-verification |
| touch target | 48 px | `tess-ui:src/tess_ui/controls.py:45` TARGET_SIZE | MD3: 48 dp |
| DPI scale | `App(dpi_scaling=True)`; `app.scale_factor` from window | `tess-ui:src/tess_ui/app.py:234,440` | px are engine logical pixels; dp = px at scale 1 |

### Icon sizes

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| icon set | curated Material Symbols paths, view box 0 -960 960 960; plus MDI set view box 0 0 24 24 | `tess-ui:src/tess_ui/icons.py` ICON_VIEW_BOX, MDI_VIEW_BOX | one weight/fill/grade (static paths); MD3 symbols have variable opsz, weight, fill, grade |
| default icon | 24 px (ListItem leading/trailing, Dialog icon, Snackbar close, Fab) | `tess-ui:src/tess_ui/views/ListItem_Stylesheet.tdl:21`, `Dialog_Stylesheet.tdl:20`, `Snackbar_Stylesheet.tdl:38` | MD3: 24 dp |
| Fab icon | 24; 36 for large | `tess-ui:src/tess_ui/views/Fab_Stylesheet.tdl:49` | MD3: 24, large 36 |
| Button icon by size | xs 20, s 18, m 24, l 32, xl 40 | `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl:162` | MD3 Expressive: 20/20/24/32/40 #needs-verification; s=18 looks inconsistent with IconButton s=24 |
| IconButton icon by size | xs 20, s 24, m 24, l 32, xl 40 | `tess-ui:src/tess_ui/views/IconButton_Stylesheet.tdl:52` | |
| Status bar icon | 16 px | `tess-ui:src/tess_ui/views/StatusBar_Stylesheet.tdl:17` | |
| Chip icon | 18 px; avatar 24 | `tess-ui:src/tess_ui/views/Chip_Stylesheet.tdl:48-53` | MD3 chip icon 18 |
| Checkbox / Radio / Spinner box | 18 / 20 / 48 (stroke 4) | `tess-ui:src/tess_ui/controls.py:188,308,1592` | MD3 checkbox 18, radio 20 |

### State layers

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| hovered | 0.08 | `tess-ui:src/tess_ui/interaction.py:43` HOVERED | MD3: 8% |
| focused (keyboard only) | 0.10 | interaction.py:43 FOCUSED | MD3: 10% |
| pressed | 0.10 | interaction.py:43 PRESSED | MD3: 10% |
| dragged | 0.16 | interaction.py:43 DRAGGED | MD3: 16% |
| precedence | dragged, else focused, else hovered | `tess-ui:src/tess_ui/interaction.py:116-122` | |
| tint | theme `on_surface` by default; controls pass their own | `tess-ui:docs/guide/interaction.md` | MD3: content colour of the component |
| disabled content | 0.38 | `tess-ui:src/tess_ui/controls.py:47` DISABLED_CONTENT; TextField sheet Opacity 0.38 (`TextField_Stylesheet.tdl:16`) | MD3: 38% |
| disabled container | 0.12 | controls.py:47 DISABLED_CONTAINER | MD3: 12% |
| state layer circle (controls) | 40 px | controls.py:46 STATE_LAYER_SIZE | MD3: 40 dp |
| hover fade | 15 ms layer opacity animation (HOVER_MS) | interaction.py:46,219 | Material Web md-ripple |
| ripple press grow | 450 ms, standard easing, initial scale 0.2 of larger side | interaction.py:47,54; ripple.py:25-31 | Material Web md-ripple |
| ripple fade-in | 105 ms | interaction.py:48; ripple.py:27 | |
| ripple minimum press | 225 ms | interaction.py:49; ripple.py:28 | |
| ripple release fade | 375 ms | interaction.py:50; ripple.py:29 | |
| ripple shader | 3 concurrent slots, 16 ms tick; `App(ripple="shader")` | `tess-ui:src/tess_ui/ripple.py:24-25` | optional renderer |
| duplicated constants | PRESS_GROW_MS and friends defined in both interaction.py and ripple.py | interaction.py:45-50, ripple.py:26-31 | see gaps |

### Focus ring

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| width | 3 px | `tess-ui:src/tess_ui/interaction.py:52` RING_WIDTH | MD3: focus indicator thickness 3 dp |
| offset | 2 px outside the node, follows corners | interaction.py:53 RING_OFFSET | MD3: 2 dp offset |
| colour | theme `secondary` (controls pass `color("secondary")`) | `tess-ui:src/tess_ui/controls.py:89`, `docs/guide/interaction.md:31` | MD3: `secondary` |
| shown when | keyboard focus only (`focus_visible`); click focus shows none | interaction.py header | |
| gradient mode | `App(focus_ring="gradient")`: sweep through secondary, primary, tertiary; one turn per 3000 ms; 33 ms tick | `tess-ui:src/tess_ui/focusring.py:20-21` | Tesserae-specific; static under reduced motion |

### Scrollbar

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| colour | role `outline` (`scrollbar_fill`) | `tess-ui:src/tess_ui/spec/build.py:697`; `tess-ui:docs/guide/layout.md:472` | MD3 defines no scrollbar spec |
| width, track, thumb radius, auto-hide, min thumb | absent in tess-ui (engine-owned, tre) | `tess-ui:src/tess_ui/spec/build.py` | see gaps |
| ScrollView | is a Tab stop (`focusable=True`); keys are engine's | build.py:697 | |

### Tooltip

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| delay | 500 ms | `tess-ui:src/tess_ui/composed.py:731` | |
| plain container | `inverse_surface`, text `inverse_on_surface`, radius 4, padding 8 x 4, max width 200 px, no shadow, text Roboto 12 | composed.py:803-814 | MD3 plain tooltip: inverse surface, 4 dp, body small 12 |
| rich container | `surface_container`, radius 12, padding 16 x 12, shadows level 2, hit testable, title Roboto 14 weight 500, body 12, action label 14 weight 500 in `primary`, action padding 12 x 6 radius 16 | composed.py:805-822 | MD3 rich tooltip: surface container, 12 dp, elevation level 2 |
| rich grace | 150 ms | composed.py:733 | |
| dismiss | Escape listener per showing tip; keyboard focus shows at once | composed.py:220,751 | |
| type roles | literals (12, 14/500), not token lookups | composed.py:813-819 | see gaps |

### Other

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| Theme file keys | `Seed`, `Dark`, `Colors`, `Styles`, `Components`, `Typography` | `tess-ui:src/tess_ui/schema/tess-ui-theme-schema.json`, `tess-ui:src/tess_ui/spec/tdl_theme.py` | |
| shell_config fixture theme keys | Color (Surface, Surface_Raised, On_Surface, On_Surface_Muted, Primary, On_Primary, Accent, Error, Warning, Success, Outline, Scrim), Type (Caption 12/400/16, Label 13/500/18, Body 14/400/20, Title 18/500/24, Display 28/400/36), Shape (None 0, Small 4, Medium 8, Large 16, Full 999), Elevation (Reach 64; Max shadow #00000066 y16 blur48), Motion (Duration Short 100, Medium 200, Long 400; Easing Standard, Emphasized), Modes (Light, Dark, High_Contrast, Reduced_Motion) | `tess-ui:apps/shell_config/tests/fixtures/shipped/Themes/Default_Theme.tdl` | tess-shell's own theme vocabulary (steel blue #4682B4, dark base). Differs from tess-ui MD3 tokens; fixture copy, may drift from tess-shell |
| shell fixture dark colours | Surface #12171D, Surface_Raised #1B222B, On_Surface #E4EAF1, Primary #5B97C9, Error #F2958C, Outline #55657A | same | |
| shell fixture light colours | Surface #F4F7FA, Surface_Raised #FFFFFF, On_Surface #16202B, Primary #2F6B9A, Error #B3261E, Outline #7A8896 | same, Modes.Light | |
| a11y roles | button checkbox radio switch slider progressbar link textbox tab tablist tabpanel menu menuitem dialog alert list listitem tree treeitem heading img group separator none | `tess-ui:src/tess_ui/a11y.py:26-30` | |
| a11y live | off, polite, assertive | a11y.py LIVE | |
| a11y extras | pressed invalid description current value_now value_text busy | a11y.py EXTRAS | |
| widget states in stylesheets | hovered focused focus_visible pressed disabled selected checked expanded error read_only visited | `tess-ui:docs/themes/index.md` (rules) | |
| sheet narrowing | Variant, Size, Shape, Classes, Name, Part, State | docs/themes/index.md | |
| Fonts | Roboto, Noto Sans Arabic, Hack Nerd Font Mono bundled; system fonts off unless `App(system_fonts=True)` | `tess-ui:docs/themes/index.md`, `tess-ui:src/tess_ui/app.py:240` | |
| Scrim | dialog and modal side-sheet scrim is a colour with alpha in the view, not the `scrim` role | `tess-ui:docs/themes/index.md` (Colour values) | The scrim itself is the modal Overlay's (Dialog_Stylesheet.tdl:7); value not found in the sheet. MD3: scrim role at 32% opacity #needs-verification |
| Divider | thickness property | `tess-ui:src/tess_ui/views/Divider_Stylesheet.tdl:12` | |


## Current values: tess-shell


Source of truth: `tesserae-shell schema --json` (saved as sh-schema.json) and the shipped theme `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`. Token references are written `$group.name`; the schema `tokens` object has six groups: color (12), type (15), shape (5), space (8), elevation (2), motion (5), plus one system token. Modes in the theme: Light, Dark, High_Contrast, Reduced_Motion.


### Colour roles

| Token | Value | File | Notes |
|---|---|---|---|
| `$color.surface` | `#12171D` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:15 | The ground of bars and panels; overridden in mode(s): Light, High_Contrast |
| `$color.surface_raised` | `#1B222B` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:16 | A surface above the ground: popups, buttons, tooltips; overridden in mode(s): Light, High_Contrast |
| `$color.on_surface` | `#E4EAF1` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:17 | Text and icons on a surface; overridden in mode(s): Light, High_Contrast |
| `$color.on_surface_muted` | `#9FAEBF` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:18 | Secondary text and icons on a surface, and a disabled state; overridden in mode(s): Light, High_Contrast |
| `$color.primary` | `#5B97C9` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:19 | The main colour of controls: a filled slider, a checked toggle; overridden in mode(s): Light, High_Contrast |
| `$color.on_primary` | `#08121C` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:20 | Text and icons on the primary colour; overridden in mode(s): Light, High_Contrast |
| `$color.accent` | `#4682B4` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:21 | The accent colour; DESKTOP follows the desktop's accent; overridden in mode(s): High_Contrast |
| `$color.error` | `#F2958C` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:22 | An error or a critical state; overridden in mode(s): Light |
| `$color.warning` | `#E6BB6A` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:23 | A warning or a low state; overridden in mode(s): Light |
| `$color.success` | `#8CCB9A` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:24 | A success state; overridden in mode(s): Light |
| `$color.outline` | `#55657A` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:25 | Borders, dividers and tracks; overridden in mode(s): Light, High_Contrast |
| `$color.scrim` | `#000000` | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:26 | The colour laid over what a modal surface covers |

#### Colour mode overrides (Default_Theme.tdl)

| Token | Light | High_Contrast | File | Notes |
|---|---|---|---|---|
| `$color.surface` | #F4F7FA | #000000 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.surface_raised` | #FFFFFF | #000000 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.on_surface` | #16202B | #FFFFFF | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.on_surface_muted` | #4A5967 | #FFFFFF | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.primary` | #2F6B9A | #8CC4F2 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.on_primary` | #FFFFFF | #000000 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.accent` | inherits base | #8CC4F2 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.error` | #B3261E | inherits base | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.warning` | #8A5A00 | inherits base | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.success` | #2E6B34 | inherits base | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.outline` | #7A8896 | #FFFFFF | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |
| `$color.scrim` | inherits base | inherits base | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:71-94 | Dark is the base block; mode `Dark { }` is empty |

### Type scale

| Token | Value | File | Notes |
|---|---|---|---|
| `$type.caption.font_size` | 12 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:30 | The size of caption type |
| `$type.caption.font_weight` | 400 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:30 | The weight of caption type |
| `$type.caption.line_height` | 16 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:30 | The line height of caption type |
| `$type.label.font_size` | 13 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:31 | The size of label type |
| `$type.label.font_weight` | 500 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:31 | The weight of label type |
| `$type.label.line_height` | 18 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:31 | The line height of label type |
| `$type.body.font_size` | 14 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:32 | The size of body type |
| `$type.body.font_weight` | 400 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:32 | The weight of body type |
| `$type.body.line_height` | 20 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:32 | The line height of body type |
| `$type.title.font_size` | 18 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:33 | The size of title type |
| `$type.title.font_weight` | 500 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:33 | The weight of title type |
| `$type.title.line_height` | 24 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:33 | The line height of title type |
| `$type.display.font_size` | 28 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:34 | The size of display type |
| `$type.display.font_weight` | 400 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:34 | The weight of display type |
| `$type.display.line_height` | 36 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:34 | The line height of display type |

### Shape

| Token | Value | File | Notes |
|---|---|---|---|
| `$shape.none` | 0 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:38 | No rounding |
| `$shape.small` | 4 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:39 | Slightly rounded corners |
| `$shape.medium` | 8 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:40 | Rounded corners |
| `$shape.large` | 16 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:41 | Strongly rounded corners |
| `$shape.full` | 999 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:42 | Fully rounded: a pill or a circle |

### Elevation

| Token | Value | File | Notes |
|---|---|---|---|
| `$elevation.reach` | 64 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:57 | How far the largest shadow reaches, in pixels |
| `$elevation.max` | one shadow `#00000066`, X 0, Y 16, Blur 48, Spread 0 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:58 | Shadow list at 100%; `Elevation: N%` scales it (guide: Elevation on a Bar, Panel, Popup, Rectangle or Box) |
| tooltip card Elevation | 20% | tess-shell:src/tess_shell/shipped/Clock/Clock_Module.tdl (tooltip block); same in Audio, Media, Network, Battery, Tray_Item | Literal per module, not a token |
| built-in fallback max shadow | one shadow #00000040 (alpha 0x40), X 0, Y 16, Blur 48, Spread 0 | tess-shell:src/tess_shell/binder/shadow.py:30 | Used when a theme has no Elevation.Max; alpha 0x40 differs from the theme's 0x66 |

### Motion

| Token | Value | File | Notes |
|---|---|---|---|
| `$motion.duration.short` | 100 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:66 | A short animation, in milliseconds |
| `$motion.duration.medium` | 200 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:66 | A medium animation, in milliseconds |
| `$motion.duration.long` | 400 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:66 | A long animation, in milliseconds |
| `$motion.easing.standard` | standard | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:67 | The standard curve |
| `$motion.easing.emphasized` | emphasized | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:67 | The emphasised curve |
| EASINGS.STANDARD | cubic-bezier(0.2, 0.0, 0.0, 1.0) | tess-shell:src/tess_shell/binder/motion.py | Curve behind `$motion.easing.standard` / `Easing: STANDARD` |
| EASINGS.EMPHASIZED | cubic-bezier(0.05, 0.7, 0.1, 1.0) | tess-shell:src/tess_shell/binder/motion.py | Curve behind `Easing: EMPHASIZED` |
| EASINGS.LINEAR | linear | tess-shell:src/tess_shell/binder/motion.py | Third enum value |
| DEFAULT_DURATION | 200 ms | tess-shell:src/tess_shell/binder/motion.py | Used when no theme gives motion.duration.medium; Transition without Duration takes medium |
| Reduced_Motion mode | every motion.duration is 0; Marquee does not scroll | tess-shell:src/tess_shell/model/look.py (_motion), tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:98 | Set from portal reduced-motion or animations off |
| Surface Animation.Type / Duration | SLIDE / 200 | tess-shell:src/tess_shell/schema/blocks.py (Animation root) | Panel show and hide |
| Peek.Enter_Delay / Exit_Delay | 150 ms / 300 ms | tess-shell:src/tess_shell/schema/blocks.py (Peek root) | Hover delays of a peek |
| Popup tooltip Enter_Delay / Exit_Delay | 500 ms / 200 ms | tess-shell:src/tess_shell/schema/blocks.py (Popup root) | Hover delays of a tooltip |

### Spacing

| Token | Value | File | Notes |
|---|---|---|---|
| `$space.step_1` | 2 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:46 | The smallest step of spacing |
| `$space.step_2` | 4 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:47 | A small step of spacing |
| `$space.step_3` | 8 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:48 | A step of spacing between small things |
| `$space.step_4` | 12 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:49 | A step of spacing inside controls |
| `$space.step_5` | 16 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:50 | A step of spacing between controls |
| `$space.step_6` | 24 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:51 | A step of spacing between groups |
| `$space.step_7` | 32 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:52 | A large step of spacing |
| `$space.step_8` | 48 | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:53 | The largest step of spacing |
| Popup.Gap default | 0 (Tray_Menu 4, submenus 0, Audio_Outputs 4) | tess-shell:src/tess_shell/schema/default_popups.py | Distance from caller to popup; module tooltips use literal 4 |
| Popup.Max_Width / Max_Height | 300 / 400 | tess-shell:src/tess_shell/schema/blocks.py (Popup root) | Defaults; Tray_Menu max_height 60% |
| Menu padding / min width | 4 / 160 | tess-shell:src/tess_shell/shipped/Menu/Menu_Module.tdl | Literal |
| Menu item height, padding | 28 px (separator 9), [10,0,10,0] | tess-shell:src/tess_shell/shipped/MenuItem/MenuItem_Module.tdl | Literal |
| Tooltip card padding | [12, 8, 12, 8] | tess-shell:src/tess_shell/shipped/Clock/Clock_Module.tdl | Literal, repeated in six modules |

### Density

| Token | Value | File | Notes |
|---|---|---|---|
| density setting | absent | absent | No density token or mode; control sizes are literals |
| Button height / min width | 32 / 32 | tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl | Literal |
| Toggle size | 40 x 22 (thumb 16) | tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl | Literal |
| Checkbox box / row | 18 / 22 | tess-shell:src/tess_shell/shipped/Checkbox/Checkbox_Module.tdl | Literal |
| Slider size | 160 x 20, track 4, handle 16 | tess-shell:src/tess_shell/shipped/Slider/Slider_Module.tdl | Literal |
| ProgressBar size | 160 x 8 | tess-shell:src/tess_shell/shipped/ProgressBar/ProgressBar_Module.tdl | Literal |
| Badge size | 18 high, 8 for a dot | tess-shell:src/tess_shell/shipped/Badge/Badge_Module.tdl | Literal |
| Launcher list | 456 wide, 40 px rows | tess-shell:src/tess_shell/shipped/Applications/Applications_Module.tdl | Literal |

### Icon sizes

| Token | Value | File | Notes |
|---|---|---|---|
| Icon module Size | 16 | tess-shell:src/tess_shell/shipped/Icon/Icon_Module.tdl | Param default |
| MenuItem icon | 16 | tess-shell:src/tess_shell/shipped/MenuItem/MenuItem_Module.tdl | Literal |
| Volume OSD icon | 24 | tess-shell:src/tess_shell/shipped/Volume_OSD/Volume_OSD_Module.tdl | Literal |
| Applications icon_size, Tasks icon_size, Tray icon_size | module params | tess-shell:src/tess_shell/shipped/Applications/, Tasks/, Tray/ | Defaults in each module's params |
| Icon set | mdi (Material Design Icons) | tess-shell:src/tess_shell/shipped/Icons/mdi.json | Plus user Iconify JSON sets; `+dot` suffix draws a dot |

### State layers

| Token | Value | File | Notes |
|---|---|---|---|
| state layers | absent | absent | No state-layer opacities; states are style rules |
| Hover (Toggle, Checkbox) | Opacity 0.85 | tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl | Rule `:hovered` |
| Pressed (Toggle, Checkbox) | Opacity 0.7 | tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl | Rule `:pressed` |
| Disabled (all widgets) | Opacity 0.5 | tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl | Rule `:disabled` per module |
| Hover (Button) | Border_Color primary | tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl | Rule `Button:hovered`; pressed Background outline |
| Hover (MenuItem) | Background outline; pressed primary | tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl | Rules |
| Hover (list, workspace, tray, task items) | Background surface_raised | tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl | Selected adds 2 px border (primary; warning for tray) |
| Focus ring | shadow, blur 0, offset 0, spread `$space.step_1` (2), colour `$color.primary`; fallback #5B97C9 / 2 | tess-shell:src/tess_shell/model/look.py:140-163 | Built from tokens, only on blocks that take Shadows |
| Scrim | `$color.scrim` #000000, no alpha | tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:26 | Token defined; no use found in shipped code |

### Other

| Token | Value | File | Notes |
|---|---|---|---|
| system `$type.system.font_family` | Roboto (until the portal reports a UI font) | tess-shell:src/tess_shell/schema/look.py (DEFAULT_FONT, SYSTEM_FONT) | Theme that sets it wins; multiple=true |
| Default stylesheet | Text and SVG take on_surface; Text Font_Size body | tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl:19-26 | Named `Default` |
| Frame defaults | Thickness None, Margin 0, Corner_Radius 0, Inner_Radius 0, Border Width/Color required | tess-shell:src/tess_shell/schema/blocks.py (Frame root) | Frame colours come from Background/Fill keys, no token |
| Peek defaults | Size 24, Handle_Opacity 0.6, Trigger HOVER, Handle AUTO | tess-shell:src/tess_shell/schema/blocks.py (Peek root) | Handle_Opacity decided 2026-11-08 |
| Panel defaults | Layer TOP, Inset 0, Visible true, Content_Fade true, Alignment CENTER, Gap 0 | tess-shell:src/tess_shell/schema/blocks.py (Panel root) |  |
| Bar defaults | Layer TOP, Gap 0, Reserve true, Keyboard NONE | tess-shell:src/tess_shell/schema/blocks.py (Bar root) |  |
| Popup defaults | Attach BOTTOM, Alignment START, Adjust [FLIP_Y, SLIDE_X], Focus true | tess-shell:src/tess_shell/schema/blocks.py (Popup root) |  |
| Settings Appearance | Theme, Stylesheets, Follow_Desktop (default true) | tess-shell:src/tess_shell/config/settings.py | Portal-driven mode selection |
| Fonts weights in modules | Badge 11 px / 600; Tooltip title 14 / 600 | tess-shell:src/tess_shell/shipped/Badge/Badge_Module.tdl, shipped/Clock/ | Literal, not type tokens |

### Differences from tess-ui (tess-ui:docs/themes/index.md)

- Colour roles: shell has 12 flat roles (surface, surface_raised, on_surface, on_surface_muted, primary, on_primary, accent, error, warning, success, outline, scrim). tess-ui follows MD3 roles generated from a seed (baseline seed 6750A4, cited in `tess-ui:docs/themes/index.md`). No role generation, tonal palette, container or inverse roles in the shell.
- Default look: shell is a dark blue-grey with steel blue accent #4682B4; tess-ui defaults to the MD3 baseline purple.
- Type: shell has 5 roles (caption 12/16 to display 28/36); MD3 has 15 (display, headline, title, body, label in three sizes). Names reuse MD3 words with different meaning (label 13/500, title 18/500).
- Shape: shell 0/4/8/16/999; MD3 has extra-small 4, small 8, medium 12, large 16, extra-large 28, full. Shell small=4 equals MD3 extra-small.
- Elevation: shell has one shadow scaled by percent; MD3 has five levels (surface tint plus shadow).
- Motion: shell 100/200/400 ms with two cubic curves; MD3 has emphasized/standard families with accelerate and decelerate.
- State layers: absent in the shell; MD3 and tess-ui use 8/10/10/16 percent overlays [INFERENCE for tess-ui values; verify against the ui token fragment].
- Spacing: shell has a named `$space.step_1..8` scale; MD3 gives no spacing tokens.
- The shell never imports tess-ui (ADR-0006, `tess-shell:docs/design/30 Decisions/ADR-0006 Shell Independent of Tesserae UI.md`); tokens are separate code.



## Current values: Shell vault (design intent)


Source: the Tesserae Shell Obsidian vault (design intent). Where the vault records a value as built, the code value was read in tess-shell for comparison; differences are flagged in sv-gaps. "File" is the vault path (prefix `shell-vault:`) that states the value; a `tess-shell:` path is the code that implements it.

### Colour roles

The vault names the role set (Style Schema, Theme Tokens) and gives a worked example in the dark theme. The shipped values are recorded in the vault only through the M3 build log (D33, as proposed by the code session). Current code values: `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`.

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `color.surface` | vault: role only (example `#1D1B20`); code `#12171D` | `shell-vault:41 TDL Reference/Style Schema.md` (Theme Tokens, example line 92); `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` Color.Surface | Vault example value is Material purple; shipped Default is a blue-grey |
| `color.surface_raised` | vault: role only; code `#1B222B` | `shell-vault:41 TDL Reference/Style Schema.md`; `shell-vault:00 Home/M3 Build Log.md` D33 | Used by Button, Toggle, list hover |
| `color.on_surface` | vault example `#E6E0E9`; code `#E4EAF1` | `shell-vault:41 TDL Reference/Style Schema.md` line 93 | Text and icon colour via the Default stylesheet |
| `color.on_surface_muted` | vault: role only; code `#9FAEBF` | `shell-vault:41 TDL Reference/Style Schema.md` | Muted network states, shortcut text, disabled fill |
| `color.primary` | vault example `#D0BCFF`; code `#5B97C9` (steel blue) | `shell-vault:41 TDL Reference/Style Schema.md` D33 | Focus ring colour (tess-shell:src/tess_shell/model/look.py `_RING_COLOR`) |
| `color.on_primary` | vault: role only; code `#08121C` | `shell-vault:41 TDL Reference/Style Schema.md` | Badge text, checked thumb and mark |
| `color.accent` | `DESKTOP` form follows portal accent; code `#4682B4` | `shell-vault:41 TDL Reference/Style Schema.md` D34 | Portal default 0.239, 0.682, 0.914 sRGB on this machine (shell-vault:40 Specifications/Integration/Portals.md) |
| `color.error` | vault: role only; code `#F2958C` | `shell-vault:41 TDL Reference/Style Schema.md` | Badge dot |
| `color.warning` | vault: role only; code `#E6BB6A` | `shell-vault:40 Specifications/Modules/Battery Module.md` | Battery low, Network limited, Tray attention |
| `color.success` | vault: role only; code `#8CCB9A` | `shell-vault:41 TDL Reference/Style Schema.md` | Not referenced by any vault module note |
| `color.outline` | vault: role only; code `#55657A` | `shell-vault:41 TDL Reference/Style Schema.md` | Borders, tracks, menu hover |
| `color.scrim` | vault: role only; code `#000000` | `shell-vault:41 TDL Reference/Style Schema.md` | No vault element uses a scrim (no modal dialog) |
| Light mode overrides | `Surface #F4F7FA`, `Surface_Raised #FFFFFF`, `On_Surface #16202B`, `On_Surface_Muted #4A5967`, `Primary #2F6B9A`, `On_Primary #FFFFFF`, `Error #B3261E`, `Warning #8A5A00`, `Success #2E6B34`, `Outline #7A8896` | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` Modes.Light; vault D33 says light variant on `#2F6B9A` | Vault M3 build log D33 |
| High_Contrast mode | `Surface #000000`, `Surface_Raised #000000`, `On_Surface #FFFFFF`, `On_Surface_Muted #FFFFFF`, `Primary #8CC4F2`, `On_Primary #000000`, `Accent #8CC4F2`, `Outline #FFFFFF` | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` Modes.High_Contrast | Vault: black and white, followed from portal `contrast` 1 |
| Dark mode | empty override (base is dark) | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` Modes.Dark | Vault D33: base block is the dark look |
| Theme modes | `Light`, `Dark`, `High_Contrast`, `Reduced_Motion` | `shell-vault:41 TDL Reference/Style Schema.md` | One theme, `Modes` block overrides tokens |
| Token reference form | `$group.name`, lowercase, matched ignoring case | `shell-vault:41 TDL Reference/Style Schema.md` D16 | |
| Colour literal | `"#RRGGBBAA"`, alpha last | `shell-vault:41 TDL Reference/Common Keys and Conventions.md` line 106 | |
| Border and shadow colours in Frame example | `#ffffff22` inner border, `#0b0c0d` background | `shell-vault:40 Specifications/Surfaces/Frame.md` lines 393 to 395 | Illustrative |

### Type scale

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `type.caption` | vault: names only; code 12 px, weight 400, line height 16 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` Type.Caption | Vault D33: type 12/13/14/18/28 px |
| `type.label` | code 13 px, weight 500, line height 18 | same | |
| `type.body` | code 14 px, weight 400, line height 20 | same | Only Body is applied by the Default stylesheet (Text rule) |
| `type.title` | code 18 px, weight 500, line height 24 | same | |
| `type.display` | code 28 px, weight 400, line height 36 | same | |
| `Font_Weight` range | 1 to 1000 | `shell-vault:41 TDL Reference/Block Reference.md` Text | tested 2026-11-04 |
| `type.system.font_family` | desktop `font-name` family, else `Roboto` (tre's bundled default) | `shell-vault:40 Specifications/Integration/Portals.md`; `shell-vault:00 Home/M5 Build Log.md` | Family only, no size token; a theme's own value wins |
| Font fallback | ordered list joined with `, ` | `shell-vault:41 TDL Reference/Style Schema.md` | decided 2026-11-04 |
| Text align values | `START`, `CENTER`, `END` | `shell-vault:41 TDL Reference/Block Reference.md` | |
| Clock example font size | 14 | `shell-vault:40 Specifications/Modules/Clock Module.md` line 94 | |

### Shape

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `shape.none` | 0 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | Vault Style Schema names the steps only |
| `shape.small` | 4 (vault example also 4) | `shell-vault:41 TDL Reference/Style Schema.md` line 97 | |
| `shape.medium` | 8 (vault example 8) | same line 98 | |
| `shape.large` | 16 (vault example 16) | same line 99 | |
| `shape.full` | 999 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | Pill; vault gives no value |
| Frame outer corner radius default | 0 | `shell-vault:40 Specifications/Surfaces/Frame.md` | Outer corners usually touch monitor corners |
| Panel example corner radius | 12 | `shell-vault:41 TDL Reference/Style Schema.md` line 59 | Illustrative |
| Corner radius form | one number, or four from top-left clockwise | `shell-vault:41 TDL Reference/Style Schema.md` | |
| Radius clamp | radius larger than half the thickness is clamped with a warning | `shell-vault:40 Specifications/Surfaces/Frame.md` Failure Modes | |

### Elevation

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `Elevation` key | percentage; 0 percent none, 100 percent about 64 px of reach | `shell-vault:41 TDL Reference/Style Schema.md` Shadow Keys (D88, D90) | Provisional: from tests on a different renderer |
| `elevation.max` shadow list | vault: scaled `X`, `Y`, `Blur`, `Spread` by the percentage; example Y 16, Blur 48, `#00000040`; D33 says 25 percent black; code `Y 16, Blur 48, #00000066` | `shell-vault:41 TDL Reference/Style Schema.md` lines 101 to 107; `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | 0x66 is 40 percent, not 25 percent |
| `Elevation.Reach` | code 64; vault D35 says dropped | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | See gaps |
| Popup default elevation | about 20 percent for a menu (proposed) | `shell-vault:40 Specifications/Surfaces/Popup.md` Design | |
| Panel shadow example | two shadows: `#00000040` Y 2 Blur 6 and `#00000020` Y 8 Blur 16 | `shell-vault:41 TDL Reference/Style Schema.md` lines 61 and 62 | Illustrative |
| `Shadow_Bleed` | `AUTO` (computed from the shadow) or a number | `shell-vault:41 TDL Reference/Style Schema.md` | Surfaces only |
| Shadow margin cost | 134 KB per buffer for a 32 px margin on a 320 by 140 body | `shell-vault:30 Decisions/ADR-0010 Surface Shadows.md` | |
| Shadows and hit region | shadows excluded from hit shape and input region | `shell-vault:40 Specifications/Surfaces/Frame.md` Shadows | decided 2026-10-27 |
| Frame input region cap | 256 rectangles; 66 measured for a 3840 by 2160 ring | `shell-vault:40 Specifications/Surfaces/Frame.md` | |

### Motion

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `motion.duration.short` | 100 ms | `shell-vault:60 Quality/Performance Budgets.md` line 69; code `Default_Theme.tdl` | Zero under reduced motion |
| `motion.duration.medium` | 200 ms | same | Also `DEFAULT_DURATION` 200 in tess-shell:src/tess_shell/binder/motion.py |
| `motion.duration.long` | 400 ms | same | |
| `motion.easing.standard` | name `standard`; curve absent | `shell-vault:41 TDL Reference/Style Schema.md` | Vault gives no cubic-bezier values |
| `motion.easing.emphasized` | name `emphasized`; curve absent | same | |
| Panel animation default | `SLIDE`, 200 ms, 24 px margin travel plus fade; `FADE` opacity only | `shell-vault:40 Specifications/Surfaces/Panel.md` D49 | 24 px is a constant, not a key |
| Expander duration | the theme's duration unless `Duration` set | `shell-vault:50 Design System/Standard Modules.md` | |
| Toggle thumb and ProgressBar fill | theme's motion duration | `shell-vault:50 Design System/Standard Modules.md` | |
| Marquee speed | 30 px per second | `shell-vault:50 Design System/Standard Modules.md`; `tess-shell:src/tess_shell/binder/marquee.py` | Tuned on KWin |
| Marquee pause | 1500 ms | same | |
| Peek enter delay | 150 ms | `shell-vault:40 Specifications/Surfaces/Frame.md`; `tess-shell:src/tess_shell/schema/model.py` line 55 | |
| Peek exit delay | 300 ms | same | |
| Tooltip enter delay | 500 ms | `shell-vault:40 Specifications/Surfaces/Popup.md`; `tess-shell:src/tess_shell/schema/model.py` line 125 | |
| Tooltip exit delay | 200 ms | same | |
| Bar auto-hide delay | 1000 ms (proposed) | `shell-vault:40 Specifications/Surfaces/Bar.md` | Not built |
| Volume OSD duration | 1500 ms, range 0 to 60000 | `shell-vault:40 Specifications/Modules/Volume OSD Module.md` | |
| Hot reload debounce | 200 ms | `shell-vault:60 Quality/Performance Budgets.md` | Not a visual value |
| Chevron turn | driven by slide progress (animate_param), not a timer | `shell-vault:40 Specifications/Surfaces/Frame.md` | |
| Slider drag events | coalesced to one per frame | `shell-vault:50 Design System/Standard Modules.md` | |
| Idle rule | 0 frames at rest for every module | `shell-vault:50 Design System/Standard Modules.md`; `shell-vault:60 Quality/Performance Budgets.md` | Measured in private sway |
| Reduced motion | all animation switches at once; durations 0; looping icons stop | `shell-vault:60 Quality/Accessibility.md` rule 7; `shell-vault:40 Specifications/Integration/Portals.md` | Portal reduced-motion 1 or enable-animations false |

### Spacing

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `space.step_1` to `space.step_8` | 2, 4, 8, 12, 16, 24, 32, 48 (code) | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`; vault names only in `shell-vault:41 TDL Reference/Style Schema.md` | Vault D33 lists the same numbers |
| Focus ring thickness | `space.step_1`, 2 px | `tess-shell:src/tess_shell/model/look.py` `_RING_SPREAD` | Vault gives no number (see gaps) |
| `Spacing`, `Padding`, `Margin` | logical pixels, `Padding` and `Margin` four-sided (left, top, right, bottom) | `shell-vault:41 TDL Reference/Style Schema.md` | |
| Frame thickness plus border plus margin | total reserved zone, e.g. 10 + 5 + 2 = 17 | `shell-vault:40 Specifications/Surfaces/Frame.md` | |
| Popup `Max_Width` and `Max_Height` | 300 and 400 default | `shell-vault:40 Specifications/Surfaces/Popup.md`; `tess-shell:src/tess_shell/schema/shell.py` line 2035 | Clamp then scroll |
| Tray menu max height | 60 percent of screen height | `shell-vault:40 Specifications/Modules/Tray Module.md` | |
| Launcher panel size | 480 wide, height AUTO with `Max_Height` 400 (earlier fixed 480 by 400) | `shell-vault:40 Specifications/Modules/Applications Module.md`; `shell-vault:40 Specifications/Surfaces/Panel.md` | |
| Volume OSD panel example | 260 by 60, 80 px above the bottom edge | `shell-vault:40 Specifications/Surfaces/Panel.md` | Illustrative |
| Panel attach gap example | 8 | `shell-vault:40 Specifications/Surfaces/Panel.md` | Illustrative |
| Popup attach gap example | 4 | `shell-vault:40 Specifications/Surfaces/Popup.md` | |
| Default list item padding (code) | `[10, 6, 10, 6]` | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | Not stated in the vault |
| Peek `Size` | 24 | `shell-vault:40 Specifications/Surfaces/Frame.md`; `tess-shell:src/tess_shell/schema/shell.py` line 1708 | Sliver left at rest |
| Edge Shell reference peek | 14 px slide, 16 px hover zone, 3 px dots with 3 px gaps, 4 px click slop, 50 percent snap | `shell-vault:40 Specifications/Surfaces/Panel.md` Collapsed Handle | Source design for peek |
| Peek click slop | 4 px | `shell-vault:40 Specifications/Surfaces/Frame.md` | |
| Peek drag snap | 50 percent of depth | same | |
| Text default size | `fit-content` width and height | `shell-vault:41 TDL Reference/Block Reference.md` Text | bridge for tre |
| Bitmap max side | 8192 px (tre) | `shell-vault:41 TDL Reference/Block Reference.md` | |
| Image refusal limit | 4096 by 4096 | `shell-vault:50 Design System/Standard Modules.md`; `tess-shell:src/tess_shell/binder/images.py` | |
| Window memory | Bar about 18 MiB, small window about 31 MiB, 4K full-screen about 177 MiB | `shell-vault:40 Specifications/Surfaces/Surface Types.md` | tre 0.5.8; re-measure on 0.5.9 |

### Density

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| Density setting | absent | none | The vault has no compact, default or comfortable density scale |
| Minimum pointer or touch target size | absent | none | No 24 px or 44 px rule is stated anywhere in the vault |
| Block defaults | Spacer, Label, Button have no default height or padding in the vault | `shell-vault:50 Design System/Standard Modules.md` | Sizes come from content and the stylesheet |

### Icon sizes

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| `Icon.Size` default | 16 | `shell-vault:50 Design System/Standard Modules.md` | Width and height in px |
| Shipped icon grid | 24 by 24, currentColor | `shell-vault:41 TDL Reference/Block Reference.md` Icon Set Files | mdi |
| Media artwork | 24 by 24 | `shell-vault:40 Specifications/Modules/Media Module.md` | `show_art` |
| Peek handle boxes | dots 24 by 8 (viewBox 6.35 by 2.12), bar 22 by 4, chevron 24 by 8 | `shell-vault:40 Specifications/Surfaces/Frame.md`; `tess-shell:src/tess_shell/surfaces/handle.py` ICON_BOX | Min thickness 8 px |
| Icon decode time | icons and thumbnails up to 512 px under 5 ms; 1080p JPEG about 10 ms; 1080p PNG about 18 ms | `shell-vault:50 Design System/Standard Modules.md` | Off-thread decode threshold 8 ms |
| mdi set | 7,447 icons, 2.7 MB, Apache 2.0 | `shell-vault:41 TDL Reference/Block Reference.md` | |
| mli set (not shipped) | 1,218 animated icons, MIT, SMIL | same | Waits for TRE-REQ-008 |
| Fallback icon | `mdi:image-broken-variant` (code); `image-missing` (Standard Modules text) | `tess-shell:src/tess_shell/model/icons.py`; `shell-vault:50 Design System/Standard Modules.md` | See gaps |

### State layers

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| State layer opacity (MD3 8, 10, 12 percent) | absent | none | The vault has no state-layer scale |
| Style states | `Hovered`, `Pressed`, `Focused`, `Disabled`, plus `Selected`, `Checked` in code | `shell-vault:41 TDL Reference/Style Schema.md`; `tess-shell:src/tess_shell/schema/look.py` line 276 | Selectors `:hovered`, `:pressed`, `:focused`, `:disabled`, `::part` |
| Disabled opacity | 0.5 (code) | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | Vault says "more than colour" only |
| Toggle and Checkbox hover and press | opacity 0.85 and 0.7 (code) | same | Not in vault |
| Peek handle opacity at rest | 0.6, hover raises to 1.0, range 0 to 1 | `shell-vault:40 Specifications/Surfaces/Frame.md`; `tess-shell:src/tess_shell/schema/model.py` line 61 | |
| Focus ring | one shadow, no blur, no offset, spread; colour `color.primary`, thickness `space.step_1` | `shell-vault:41 TDL Reference/Block Reference.md` Accessibility Defaults; `tess-shell:src/tess_shell/model/look.py` | Vault does not state colour or width |
| Slider handle | border 2 px in surface colour; hovered muted; pressed 3 px in on_surface (code) | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | |
| Selected row | 2 px primary border over `surface_raised` (code) | same | |
| Tray attention item | 2 px warning border (code) | same | Vault: "selected look with the warning token" |

### Other

| Token | Value | File | Notes |
| --- | --- | --- | --- |
| Text contrast | at least 4.5 to 1 against background in shipped themes | `shell-vault:60 Quality/Accessibility.md` rule 9 | WCAG 1.4.3; to be checked by a script in M4 |
| Large text, icon and widget edge contrast | at least 3 to 1 | same | WCAG 1.4.11 |
| Colour not sole cue | required (rule 8) | same | WCAG 1.4.1 |
| High contrast source | portal `contrast` 1 | `shell-vault:40 Specifications/Integration/Portals.md` | Desktop has no such setting; headless tested only |
| Reduced motion source | portal `reduced-motion` 1 or `enable-animations` false | same | Combined flag `Appearance.motion_reduced` |
| Colour scheme source | portal `color-scheme` 0, 1, 2 | same | |
| Tab_Index range | integer 0 to 2 147 483 647 | `shell-vault:40 Specifications/Integration/Focus and Keyboard.md` | |
| Slider keys | arrows by `Step`; PageUp and PageDown by ten steps; Home and End to `Min` and `Max` | `shell-vault:50 Design System/Standard Modules.md` | |
| Slider defaults | `Min` 0, `Max` 100, `Step` 1 | same | |
| Submenu depth | 3 levels | `shell-vault:50 Design System/Standard Modules.md`; `shell-vault:40 Specifications/Modules/Tray Module.md` | |
| Badge `Max` | 99 (shows `99+`) | `shell-vault:50 Design System/Standard Modules.md` | |
| Text input `Max_Length` | 0 (no limit) | same | |
| Performance: module callback | under 4 ms (a 60 Hz frame is 16.7 ms) | `shell-vault:60 Quality/Performance Budgets.md` | |
| Performance: idle CPU | limit 0.5 percent of one core; measured 0.03 | same | |
| Performance: time to ready | limit 2 s; measured 0.264 s | same | |
| Performance: hot reload | under 100 ms for ten surfaces | same | |
| Performance: default shell memory | 209 MiB RSS, 141 MiB PSS measured | same | No limit set |
| Portal fallback values | `color-scheme` 0, no accent, `contrast` 0, `reduced-motion` 0 | `shell-vault:40 Specifications/Integration/Portals.md` | |
| Settings keys for look | `Appearance { Theme, Stylesheets, Follow_Desktop }` | `shell-vault:00 Home/M3 Build Log.md` D32 | Absent `Stylesheets` means `[Default]` (ADR-0022) |
| Config app budgets | start to usable 1.5 s; open 500-line file 100 ms; one edit 16 ms | `shell-vault:40 Specifications/Configuration Application.md` | |
| Layer values | `BACKGROUND`, `BOTTOM`, `TOP`, `OVERLAY`; reserving only on `TOP` | `shell-vault:40 Specifications/Surfaces/Surface Types.md` | |
| Layer namespace | `tesserae-shell.<type>.<name>` | same | |


## Current values: tre engine

### Colour roles

The engine has no colour role system (ARCHITECTURE section 7: engine-md3 removed in 0.3.5, M99). Only the defaults below exist; every other colour is transparent until set.

| Token | Value | File | Notes |
|---|---|---|---|
| Colour format | 8-bit straight-alpha sRGB tuple (r, g, b, a) 0-255 | tre:docs/guide/painting.md (Color) | No wide gamut or HDR; gradient interpolation in sRGB |
| Default fill of box, path, canvas | transparent | tre:docs/reference/properties.md (Kinds) | |
| Default text fill (text, text_input) | (0, 0, 0, 255) | tre:crates/engine-py/src/window_events.rs:299-316 | Opaque black, CSS-like |
| Scroll thumb fill (default) | (0xCA, 0xC4, 0xD0, 0x8C) = #CAC4D0 at 55 percent | tre:crates/engine-render/src/lib.rs:1984 (DEFAULT_SCROLLBAR_FILL) | Comment calls it MD3 outline_variant at 55 percent; overridable by scrollbar_fill |
| Placeholder fill (default) | text colour at 60 percent | tre:docs/reference/paint.md (Text inputs, scroll views, and terminals) | placeholder_fill overrides |
| Selection fill, text input and selectable text (default) | text colour at 30 percent | tre:docs/reference/paint.md; tre:docs/guide/text.md | selection_fill overrides |
| Caret colour (default) | text colour | tre:docs/reference/paint.md | caret_color overrides, animatable |
| Terminal foreground | (0x1C, 0x1B, 0x1F, 0xFF) | tre:crates/engine-core/src/node.rs:~187 (TerminalPalette::default) | |
| Terminal background | transparent | tre:crates/engine-core/src/node.rs:~188 | |
| Terminal cursor | (0x1C, 0x1B, 0x1F, 0x80) | tre:crates/engine-core/src/node.rs:~189 | |
| Terminal selection | (0x1C, 0x1B, 0x1F, 0x4D) | tre:crates/engine-core/src/node.rs:~190 | |
| Terminal ANSI 16 | (28,28,33) (222,89,89) (140,191,102) (217,178,89) (102,153,230) (191,128,217) (102,191,204) (204,204,209) / bright (102,107,117) (242,115,115) (166,217,128) (242,204,115) (140,178,242) (217,153,242) (140,217,230) (242,242,247) | tre:crates/engine-core/src/node.rs:~166-181 | Dark-on-light foreground with dark-style ANSI set; mismatch noted in gaps |
| Initial renderer clear colour | (0x67, 0x50, 0xA4, 0xFF) | tre:crates/engine-render/src/lib.rs:74 (INITIAL_COLOR) | MD3 baseline primary purple |
| Scrim | absent | tre:docs/reference/layers.md | Engine draws no scrim |
| Focus ring colour | absent | tre:docs/guide/painting.md | Engine draws no focus ring |
| Disabled colours | absent | tre:docs/guide/painting.md | disabled styling is the app's |
| Dark/light scheme | window.get("dark"), event color_scheme; None when unknown | tre:docs/reference/events.md (Window properties) | Signal only |
| High contrast | window.get("high_contrast"), event high_contrast | tre:docs/reference/events.md | Signal only |

### Type scale

| Token | Value | File | Notes |
|---|---|---|---|
| Type scale roles | absent | tre:ARCHITECTURE.md section 7 | No display/headline/title/body/label roles in engine |
| Default text font size | 16 px | tre:crates/engine-py/src/window_events.rs:~305 | text node |
| Default text_input font size | 16 px at creation (docs examples and core tests use 14) | tre:crates/engine-py/src/window_events.rs:~314 | |
| Default font family | Roboto | tre:crates/engine-py/src/window_events.rs:~303 | |
| Default font weight | 400 | tre:crates/engine-py/src/window_events.rs:~304 | Range 1-1000 |
| Bundled faces | Roboto Regular, Roboto Medium, Noto Sans Arabic Regular, Hack Nerd Font Mono Regular | tre:crates/engine-render/src/text.rs:32-50 | No Hebrew, CJK, Indic, Thai, emoji |
| Monospace family constant | tess_re.MONOSPACE_FONT_FAMILY (Hack Nerd Font Mono) | tre:docs/guide/text.md (Fonts) | |
| Line height | None = the font's own; else multiple of font size | tre:docs/reference/properties.md (Text) | Text node only |
| Letter spacing | extra px per char, default 0 | tre:docs/reference/properties.md | Text node only |
| Fit-content text width slack | 2 px | tre:crates/engine-core/src/tree/layout.rs:97 (FIT_CONTENT_SLACK) | Height exact |
| Code editor line height ratio | 1.35 | tre:crates/engine-core/src/tree/mod.rs:1254 | Multiline input without wrap |
| Code editor char width ratio | 0.6 | tre:crates/engine-core/src/tree/mod.rs:1267 | Monospace assumption |
| System fonts | off by default (set_system_fonts) | tre:docs/guide/text.md | |
| Glyph cache | off by default (glyph_cache) | tre:docs/reference/window.md | Edge pixels differ up to ~45/255 |
| Subpixel (LCD) text | absent, declined | tre:docs/design/gaps.md (7) | Grayscale only |

### Shape

| Token | Value | File | Notes |
|---|---|---|---|
| Corner radius default | 0 | tre:docs/reference/properties.md | single value or (tl, tr, br, bl), animatable |
| Corner style | round (default) or concave per corner | tre:docs/guide/painting.md | |
| Scroll thumb radius | 2 px | tre:crates/engine-render/src/lib.rs:2010 (SCROLLBAR_THUMB_RADIUS) | |
| Square border limit | 1.0 | tre:crates/engine-render/src/lib.rs:1092 (SQUARE_BORDER_MAX) | Renderer detail |
| Stroke | drawn inside the box, never changes layout; round caps and joins on paths | tre:docs/guide/painting.md | |
| Mask | None, circle, {rounded: r}, {path, view_box} | tre:docs/reference/properties.md | |

### Elevation

| Token | Value | File | Notes |
|---|---|---|---|
| Elevation levels | absent; an elevation level is a shadow list | tre:ARCHITECTURE.md section 7 | |
| Shadow tuple | (colour, offset_x, offset_y, blur, spread); first on top | tre:docs/guide/painting.md (Shadows) | |
| Example raised card | [((0,0,0,77),0,1,2,0), ((0,0,0,38),0,2,6,2)] | tre:docs/guide/painting.md | Doc example, not a default |
| Focus ring recipe | ((r,g,b,255),0,0,0,3): zero blur, spread 3 | tre:docs/guide/painting.md | Doc example |
| Blur | node blur (std dev px) and backdrop_blur (px) | tre:docs/reference/paint.md | Animatable |
| Popup shadow margin | transparent margin plus geometry=(x,y,w,h) | tre:docs/reference/layer-window.md (PopupWindow) | Shadow must live inside surface |

### Motion

| Token | Value | File | Notes |
|---|---|---|---|
| Default easing | linear | tre:docs/guide/animation.md (Easing) | |
| Easing forms | linear, cubic bezier (x1,y1,x2,y2), "spring", ("spring", bounce) | tre:docs/guide/animation.md | No named tokens in engine |
| Spring default bounce | 0.2 (range -1 to 1 exclusive) | tre:docs/guide/animation.md (Springs) | duration_ms is the period; settles within 0.1 percent |
| Duration default | 0 = snap on next frame | tre:docs/guide/animation.md | No default duration |
| MD3 standard easing used in docs | (0.2, 0.0, 0.0, 1.0) | tre:docs/guide/animation.md | Doc example |
| MD3 emphasized decelerate in docs | (0.05, 0.7, 0.1, 1.0) | tre:docs/guide/animation.md | Doc example |
| Scroll snap settle delay | 120 ms | tre:crates/engine-core/src/tree/scroll.rs:43 (SNAP_SETTLE) | |
| Scroll snap duration | 200 ms | tre:crates/engine-core/src/tree/scroll.rs:44 (SNAP_DURATION) | |
| Fling decay constant | 0.35 s | tre:crates/engine-core/src/tree/scroll.rs:47 (FLING_TAU) | |
| Fling stop speed | 30 px/s | tre:crates/engine-core/src/tree/scroll.rs:49 (FLING_STOP) | |
| Fling minimum release speed | 150 px/s | tre:crates/engine-core/src/tree/scroll.rs:51 (FLING_MIN) | |
| Gesture velocity window | 100 ms | tre:crates/engine-core/src/gesture.rs:258 | |
| Long press | 500 ms | tre:crates/engine-core/src/gesture.rs:152 | |
| Tap max duration | 300 ms | tre:crates/engine-core/src/gesture.rs:153 | |
| Double tap gap | 300 ms | tre:crates/engine-core/src/gesture.rs:154 | |
| Caret blink | caret_blink ms or None (steady); engine default value not found in code (TextFieldState caret_blink_ms initialised 0) | tre:crates/engine-core/src/node.rs:705,923 | Treat as no blink unless set |
| Resize hold (low latency while resizing) | 400 ms | tre:crates/engine-render/src/present.rs:94 | |
| Reduced motion | signal only | tre:docs/reference/events.md | |
| Animatable properties | fill, stroke_color, stroke_width, opacity, blur, backdrop_blur, corner_radius, shadows, translate_x/y, scale, rotation_deg, scroll_offset, path data/trim, svg_time, width/height/min/max, flex_basis, x, y, padding*, margin*, gap*; LayerWindow margins | tre:docs/guide/animation.md; tre:docs/reference/layer-window.md | font_size not animatable |

### Spacing

| Token | Value | File | Notes |
|---|---|---|---|
| Window root padding | 16 px | tre:crates/engine-py/src/window.rs:23 (PADDING) | Window only; LayerWindow root has none |
| Window root gap | 16 px | tre:crates/engine-py/src/window.rs:24 (GAP) | |
| Default gap, padding, margin | 0 | tre:docs/reference/properties.md | No spacing scale in engine |
| Spacing scale | absent | tre:ARCHITECTURE.md section 7 | |
| Keyboard scroll line | 40 px | tre:crates/engine-core/src/tree/scroll.rs:7 (KEY_SCROLL_LINE) | |
| Wheel line | 20 px per line | tre:crates/engine-py/src/listeners.rs:86 (WHEEL_LINE_PX) | |
| Double click slop | 4 px | tre:crates/engine-py/src/dispatch.rs:778 | |
| Touch slop | 10 px (touch_slop) | tre:docs/guide/events-and-input.md | window.set |
| Touch target slop | 0 px, off (touch_target_slop) | tre:docs/guide/events-and-input.md | window.set |
| Scroll thumb thickness | 4 px | tre:crates/engine-core/src/node.rs:518 (SCROLLBAR_THICKNESS) | scrollbar_width overrides, painted and grabbed |
| Scroll thumb margin from edge | 2 px | tre:crates/engine-core/src/node.rs:519 (SCROLLBAR_MARGIN) | |
| Scroll thumb min length | 32 px | tre:crates/engine-core/src/node.rs:520 (SCROLLBAR_MIN_LENGTH) | |
| Scroll thumb grab slop | 6 px either side | tre:crates/engine-core/src/node.rs:525 (SCROLLBAR_GRAB_SLOP) | |
| Resize border | 0 (off); set N logical px | tre:docs/reference/window.md | |
| Default window size | 480 x 200, title "tess_re v2", decorations on | tre:docs/reference/window.md | |
| Layer window default | size (0, 0), margin 0, exclusive_zone 0, keyboard none | tre:docs/reference/layer-window.md | |
| Popup default constraint adjustment | (flip_y, slide_x) | tre:docs/reference/layer-window.md | |
| Layer placement default | below, flip=True | tre:docs/reference/layers.md | Aligned with anchor start |

### Density

| Token | Value | File | Notes |
|---|---|---|---|
| Density | absent | tre:ARCHITECTURE.md section 7 | No density concept or touch-target minimum in engine |

### Icon sizes

| Token | Value | File | Notes |
|---|---|---|---|
| Icon size default | absent; path/svg node sized by width and height | tre:docs/reference/paint.md | Docs example uses 24 px |
| Icon set viewBox | 24 x 24 | tess-icons:icon-sets/Material-Design-Icons/material-design-icons.json (width, height) | MDI, 7447 icons |
| Line icon set viewBox | 24 x 24 | tess-icons:icon-sets/Material-Design-Icons/material-line-icons.json | Line MD, 1218 icons |
| Icon colour | currentColor in set bodies; engine path takes fill or stroke_color | tess-icons:icon-sets/Material-Design-Icons/*.json | Consumer maps currentColor |
| Path stroke default | caps and joins round; width stays in px under view_box scaling | tre:docs/reference/paint.md | |
| Max image side | 8192 px | tre:crates/engine-render/src/image_cache.rs:54 | |
| decode_image default max side | 4096 px | tess-utils:docs/reference.md (Images) | decode_image_file: no limit |
| Cursor image | 1-256 px per side, device pixels, hotspot | tre:docs/reference/node.md (Cursors) | Not scaled for HiDPI |
| Window icon | (rgba, w, h); Windows and X11 only | tre:docs/reference/window.md | |

### State layers

| Token | Value | File | Notes |
|---|---|---|---|
| Hover, focus, press, drag opacities (8/10/10/16 percent) | absent | tre:docs/guide/painting.md (What Tesserae Engine leaves to you) | Engine paints no state layers |
| Ripple | recipe only (round box scaled and faded inside clip_children) | tre:docs/guide/building-a-widget.md; tre:examples/ripple.py | |
| Focus visible signal | focus event field focus_visible (True for keyboard or AT, False after pointer) | tre:docs/guide/events-and-input.md | |
| Disabled | accessibility flag only | tre:docs/reference/node.md | |

### Other

| Token | Value | File | Notes |
|---|---|---|---|
| DPI scaling | dpi_scaling off by default on Window; on for LayerWindow; fractional scale_factor | tre:docs/reference/window.md | Offsets rounded to device pixel |
| Headless layer window size | 1920 x 1080 | tre:crates/engine-py/src/layer_window.rs:40-41 | |
| Layout calc passes | 4; anchor passes 4 | tre:crates/engine-core/src/tree/layout.rs:50,54 | |
| Damage rects | max 4; full redraw above 50 percent area | tre:crates/engine-render/src/damage.rs:84,86 | |
| Scroll blit minimum nodes | 200 | tre:crates/engine-render/src/damage.rs:97 | |
| Accessibility announcement queue | 16 | tre:crates/engine-core/src/tree/access.rs:35 | |
| Max build nodes / depth | 1,000,000 / 256 | tre:crates/engine-py/src/window_build.rs:17-18 | |
| Max input region rects | 256 | tre:crates/engine-platform/src/layer_config.rs:152 | |
| Terminal size range | 1-1000 cols and rows | tre:docs/reference/properties.md | |
| Caret default width | 1.5 px, shape bar | tre:crates/engine-core/src/node.rs:921 | |
| Colour parse | tess_utils.parse_color returns tre bytes; alpha float rounds half up (0.3 -> 77) | tess-utils:docs/reference.md (Colour) | |
| Fractional scale | Output.scale_factor float | tre:docs/reference/outputs.md | |


Back to [[20 Foundations and Tokens]].
