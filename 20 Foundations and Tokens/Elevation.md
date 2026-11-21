---
title: Elevation
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, elevation, tokens]
related: ["[[Colour Roles]]", "[[Shape]]", "[[Scrim]]", "[[Tooltip]]", "[[Popup]]", "[[Menu]]", "[[Dialog]]", "[[Existing Tokens]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]"]
---

# Elevation

> [!info] Summary
> Elevation levels 0 to 5 in dp, the two-shadow geometry of each level, the tonal surface container each level uses, and the rule that no tint overlay is drawn. Counterpart: [Material 3 elevation](https://m3.material.io/styles/elevation/tokens). Source of truth in code: see Status in code.

## Purpose

Elevation separates a layer from the layer below. Since the 2022 role scale, MD3 expresses it with a shadow and a tonal container colour (a surface container role), not with a primary-colour tint blended into the surface.

## Tokens

### Levels, shadows and containers

- Level dp values: [md-sys-elevation v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-elevation.scss) (level 0 to 5 are 0, 1, 3, 6, 8, 12 dp).
- Shadow geometry: the Material Web elevation implementation [elevation/internal/_elevation.scss](https://github.com/material-components/material-web/blob/main/elevation/internal/_elevation.scss) draws two shadows per level (a key shadow at 30 percent opacity and an ambient shadow at 15 percent opacity, shadow colour the role `shadow`). The table evaluates its formulas for level 0 to 5 (the "level" there is the index 0 to 5, not the dp value).
- Container mapping: the component token files listed below. The official page [m3.material.io/styles/elevation/tokens](https://m3.material.io/styles/elevation/tokens) could not be fetched. The mapping for level 4 and 5 is not in any component token file read and is a design choice.

| Level | Elevation (dp) | Key shadow x / y / blur / spread (dp), black at 30 percent | Ambient shadow x / y / blur / spread (dp), black at 15 percent | Tonal container role |
|---|---|---|---|---|
| `level_0` | 0 | none | none | `surface` |
| `level_1` | 1 | 0 / 1 / 2 / 0 | 0 / 1 / 3 / 1 | `surface_container_low` |
| `level_2` | 3 | 0 / 1 / 2 / 0 | 0 / 2 / 6 / 2 | `surface_container` |
| `level_3` | 6 | 0 / 1 / 3 / 0 | 0 / 4 / 8 / 3 | `surface_container_high` |
| `level_4` | 8 | 0 / 2 / 3 / 0 | 0 / 6 / 10 / 4 | `surface_container_highest` #needs-verification (design choice) |
| `level_5` | 12 | 0 / 4 / 4 / 0 | 0 / 8 / 12 / 6 | `surface_container_highest` #needs-verification (design choice) |

Shadow colour is the role `shadow` ([[Colour Roles]]), `#000000` in both schemes. Shadows are drawn in the dark scheme too.

### Elements and their level

| Element | Level | Container role | Source (component token file, v0_192) |
|---|---|---|---|
| Elevated card, elevated button | 1 | `surface_container_low` | _md-comp-elevated-card.scss, _md-comp-elevated-button.scss |
| Menu | 2 | `surface_container` | _md-comp-menu.scss |
| Rich tooltip | 2 | `surface_container` | _md-comp-rich-tooltip.scss |
| Navigation bar | 2 | `surface_container` | _md-comp-navigation-bar.scss |
| Dialog | 3 | `surface_container_high` | _md-comp-dialog.scss |
| Search bar | 3 | `surface_container_high` | _md-comp-search-bar.scss |
| Snackbar | 3 | `inverse_surface` | _md-comp-snackbar.scss |
| Plain tooltip | 0 (no elevation token) | `inverse_surface` | _md-comp-plain-tooltip.scss |
| Popup (Tesserae) | 2 | `surface_container` | this note, design choice #needs-verification |

### Margin a layer window reserves for its shadow

A surface rendered in its own layer window (a popup, a tooltip, a shell panel) draws its shadow inside its own window, so it reserves a transparent margin. The required margin per side is the largest of `blur + spread + |y|` over the level's two shadows (a Gaussian blur of radius b is visible out to about b). Source for the layer constraint: `tre:docs/reference/layer-window.md` (PopupWindow: transparent margin plus geometry; the shadow must live inside the surface).

| Level | Transparent margin required around a layer window (dp per side) |
|---|---|
| `level_0` | 0 |
| `level_1` | 5 |
| `level_2` | 10 |
| `level_3` | 15 |
| `level_4` | 20 |
| `level_5` | 26 |

### Tint overlay

None. The generated role `surface_tint` equals `primary` and names the tint colour of the retired overlay; it is not applied. Android states that surface colours with an elevation overlay were replaced by the tonal surface container roles ([Android Color guide](https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md), "Using Surface with Elevation Overlay").

### Mapping of the tess-shell elevation tokens

tess-shell has no levels. It has one maximum shadow and a percentage: `$elevation.max` is one shadow `#00000066`, x 0, y 16, blur 48, spread 0, and a block sets `Elevation: N%` to scale it (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` line 58). Tooltip cards use 20 percent literally. There is no mapping to levels 0 to 5; see Deviations.

## Rules

1. An element has one elevation level. The level sets its shadow and, for a surface container, its container role; both come from the tables above.
2. No tint is blended into any surface. A container at level N draws exactly its container role colour.
3. Shadows follow the container shape ([[Shape]]) and use the role `shadow`.
4. A layer window reserves at least the margin in the margin table for its level, on every side, and the shadow is not clipped by the window edge.
5. An overlay that has an elevation draws its shadow and container together. No overlay is drawn without a container colour ([[Tooltip]] rule on opaque containers).
6. Elevation changes with state (hover, press) are listed by each element note; a change animates with the `short4` duration ([[Motion]]).
7. A modal surface sits above its scrim ([[Scrim]]); the scrim has no elevation.

## Acceptance criteria

- [ ] AC-ELV-1: Token test. The theme returns elevation dp 0, 1, 3, 6, 8, 12 for `level_0` to `level_5`. Pass: 6 of 6 exact.
- [ ] AC-ELV-2: Token test. For each level 1 to 5 the shadow list equals the table: two shadows, key first, with the listed y, blur, spread and alpha 0.30 / 0.15 (alpha tolerance 1/255). Pass: 10 of 10 shadows equal.
- [ ] AC-ELV-3: Pixel check. Render a level 3 dialog container on a `surface` background and sample its inner area away from content. Pass: the sampled colour equals `surface_container_high` within 1 per channel in light and in dark, and does not equal `surface_container_high` blended with `primary` (no tint).
- [ ] AC-ELV-4: Pixel check. Sample the pixel 2 dp outside the bottom edge of a level 2 menu on a `surface` background. Pass: it is darker than `surface` (shadow present) and the pixel 40 dp outside equals `surface`.
- [ ] AC-ELV-5: Geometry check. For a popup layer window at each level, the transparent margin measured from the window edge to the container edge is at least the margin table value on all four sides. Pass: 4 of 4 sides.
- [ ] AC-ELV-6: Pixel check. The shadow of a level 5 element in a layer window is not clipped: the rendered shadow alpha at the window edge is at most 1/255. Pass.
- [ ] AC-ELV-7: Token test. Each row of the elements-and-level table resolves to the listed container role in the shipped stylesheet or theme of the project. Pass: all rows the project implements match.
- [ ] AC-ELV-8: Review. No project code blends `primary` into a surface by elevation. Pass: reviewer finds none.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/tokens.py` (`ELEVATION_LEVELS`, `elevation_shadows`); `tess-ui:src/tess_ui/views/*_Stylesheet.tdl`; `tess-ui:src/tess_ui/composed.py` line 811 | Partly meets. AC-ELV-2 meets: the shadow offsets, blurs and spreads in `elevation_shadows` equal the table for levels 1 to 5 (alpha 77 and 38 of 255); the Phase 0 remark that they follow a legacy formula and not MD3's is corrected here, they equal the Material Web values. Ambient spread is non-zero by design, as in the source. AC-ELV-1 fails as written: `ELEVATION_LEVELS` holds the level index 0 to 5 and no dp value (3, 6, 8, 12 for levels 2 to 5). AC-ELV-3 meets for the tint (no tint overlay; `surface_tint` unused); container roles by level are not verified in the view stylesheets (AC-ELV-7 not checked). Rich tooltip has elevation 2 shadows; plain tooltip none. AC-ELV-5 not checked. |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`; `tess-shell:src/tess_shell/binder/shadow.py` | Absent against the levels: one scalable shadow, no level tokens, no tonal container ladder (the shell has `surface` and `surface_raised`). The built-in fallback maximum shadow is `#00000040` where the theme has `#00000066`, so a theme without `Elevation.Max` draws a lighter shadow. AC-ELV-3 meets (no tint). |
| tre | `tre:docs/guide/painting.md` (Shadows); `tre:docs/reference/layer-window.md` | Not applicable as levels. The engine draws a shadow list per node and supports no tonal elevation; shadows in a popup need the transparent margin and `input_region="geometry"`. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Container role for levels 4 and 5 is `surface_container_highest` | No component token file read gives a level 4 or 5 container; choice keeps the ladder monotonic | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Popup container at level 2 | MD3 has no popup; the menu level is used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell expresses elevation as a percentage of one shadow | The shell has its own flat token set; an adoption of levels is not decided | [[ADR-0001 MD3 role names are the specification vocabulary]] |
