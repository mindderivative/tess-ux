---
title: Shape
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, shape, tokens]
related: ["[[Elevation]]", "[[Colour Roles]]", "[[Focus Ring]]", "[[Tooltip]]", "[[Menu]]", "[[Dialog]]", "[[Existing Tokens]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# Shape

> [!info] Summary
> The Material Design 3 corner scale (7 baseline steps plus 3 named Expressive steps), the radius of each overlay and container element, and how each project maps to it. Counterpart: [Material 3 shape](https://m3.material.io/styles/shape/corner-radius-scale). Source of truth in code: see Status in code.

## Purpose

A small set of corner radii gives every container a recognisable family look and makes radius a token that a test can read.

## Tokens

Values were read from the Material Web token sources; the official page [m3.material.io/styles/shape/corner-radius-scale](https://m3.material.io/styles/shape/corner-radius-scale) is script-rendered and could not be fetched. 1 dp = 1 px at scale 1.0.

### Baseline scale

| Token | Radius (dp) | Source |
|---|---|---|
| `none` | 0 | [md-sys-shape v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-shape.scss) |
| `extra_small` | 4 | same |
| `small` | 8 | same |
| `medium` | 12 | same |
| `large` | 16 | same |
| `extra_large` | 28 | same |
| `full` | 9999 (clamped to half the shorter side) | same |

### Expressive steps (named adoption only)

[[ADR-0006 MD3 baseline with named Expressive adoptions]] keeps the baseline scale. A project uses these only through a named entry in [[Deviations from MD3]].

| Expressive token | Radius (dp) | Source |
|---|---|---|
| `large_increased` | 20 | [md-sys-shape latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-shape.scss) |
| `extra_large_increased` | 32 | same |
| `extra_extra_large` | 48 | same |

### Multi-corner shorthands

| Token | Corners (tl tr br bl, dp) | Source |
|---|---|---|
| `extra_small_top` | 4 4 0 0 | v0_192 source above |
| `large_top` | 16 16 0 0 | same |
| `large_start` | 16 0 0 16 | same |
| `large_end` | 0 16 16 0 | same |
| `extra_large_top` | 28 28 0 0 | same |

### Radius of elements

| Component | Shape token | Radius (dp) | Source (component token file, v0_192) |
|---|---|---|---|
| Menu container | `extra_small` | 4 | _md-comp-menu.scss |
| Plain tooltip container | `extra_small` | 4 | _md-comp-plain-tooltip.scss |
| Snackbar container | `extra_small` | 4 | _md-comp-snackbar.scss |
| Rich tooltip container | `medium` | 12 | _md-comp-rich-tooltip.scss |
| Elevated card container | `medium` | 12 | _md-comp-elevated-card.scss |
| Dialog container | `extra_large` | 28 | _md-comp-dialog.scss |
| Elevated button container | `full` | full (pill) | _md-comp-elevated-button.scss |
| Search bar container | `full` | full (pill) | _md-comp-search-bar.scss |
| Navigation bar container | `none` | 0 | _md-comp-navigation-bar.scss |

Element notes ([[Tooltip]], [[Menu]], [[Dialog]], [[Popup]], [[Button]]) carry the radius of their own element and link here for the token. [[Popup]] and shell panels have no MD3 counterpart: a popup container uses `extra_small` (like a menu) unless its note says otherwise #needs-verification (design choice).

### Mapping of the tess-shell shape tokens

| Shell token | Radius | MD3 token of the same value |
|---|---|---|
| `$shape.none` | 0 | `none` |
| `$shape.small` | 4 | `extra_small` |
| `$shape.medium` | 8 | `small` |
| `$shape.medium_large` | 12 | `medium` |
| `$shape.large` | 16 | `large` |
| `$shape.extra_large` | 28 | `extra_large` |
| `$shape.full` | 999 | `full` |

The shell names `small` and `medium` mean one step less than the MD3 names of the same value ([[ADR-0001 MD3 role names are the specification vocabulary]]). Decision for the two steps the shell added (tess-shell review of its shape token change, 2026-11-22, recorded by bot:Orchestrator): the shell keeps its existing names, so a theme that already says `small` or `medium` does not change meaning; the 12 dp step is `medium_large` (the MD3 name `medium` would collide with the shell's `medium` of 8 dp); the 28 dp step is `extra_large`, the same name and value as MD3. The mapping table is the single place that equates the two vocabularies; a project that adds a step adds its row here first.

## Rules

1. A container takes its radius from a shape token. Literal radii are allowed only for content (an image mask) and for primitives such as a scrollbar thumb, whose radius is half its width ([[Scrollbar and Scroll Container]]).
2. The `full` radius is clamped to half the shorter side of the box; a box never draws a radius larger than that.
3. Nested rounded containers: the inner radius is the outer radius minus the padding between them, never below 0.
4. A focus ring follows the container shape ([[Focus Ring]]): its radius is the container radius plus the ring offset.
5. A clipping container clips its children to its rounded shape.
6. Windows and panels that touch a screen edge use `none` on the touching side.

## Acceptance criteria

- [ ] AC-SHP-1: Token test. The theme returns `none` 0, `extra_small` 4, `small` 8, `medium` 12, `large` 16, `extra_large` 28 and `full` greater than or equal to 9999. Pass: 7 of 7 exact.
- [ ] AC-SHP-2: Geometry check. For each row of the Radius of elements table, render the element and read the container's corner radius from the layout tree. Pass: equals the table value (pill: half the shorter side).
- [ ] AC-SHP-3: Pixel check. For a 40 by 40 dp box with radius `full`, the pixel at (1,1) from the corner is the background and the pixel at the centre of the left edge is the container colour. Pass: both hold at scale 1.0 and 2.0.
- [ ] AC-SHP-4: Token test (static scan). No view stylesheet sets `Corner_Radius` to a number that is not in the baseline scale, except in the allow-list of Rules 1. Pass: zero hits outside the allow-list.
- [ ] AC-SHP-5: Geometry check. A child larger than its rounded parent is clipped at the parent's corner. Pass: the child pixel at the corner outside the radius equals the background.
- [ ] AC-SHP-6: Token test. The 7 shell shape tokens (`none`, `small`, `medium`, `medium_large`, `large`, `extra_large`, `full`) equal the mapping table values (0, 4, 8, 12, 16, 28, 999). Pass: 7 of 7.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/tokens.py` (`SHAPES`, `FULL_RADIUS`); `tess-ui:src/tess_ui/spec/default_theme.tdl`; `tess-ui:src/tess_ui/views/*_Stylesheet.tdl` | Partly meets. AC-SHP-1 meets (0, 4, 8, 12, 16, 28, `full` 9999). AC-SHP-2 meets for Menu 4, Tooltip 4 (rich 12), Snackbar 4, Card 12, Dialog 28; the navigation rail indicator is 16 where MD3 uses a pill #needs-verification. AC-SHP-4 fails: per-component literals in stylesheets (Button sheet 12, 16, 28 for sizes, Chip 8, Date picker day 24, Pagination item 20, Tabs indicator 3, Badge 3 and 8). Expressive tokens are absent as tokens. |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` lines 38 to 42 | Partly meets. AC-SHP-6 meets (0, 4, 8, 16, 999). The scale had 5 of 7 steps; the shell adds `medium_large` (12) and `extra_large` (28) in its shape token change (not yet verified here). AC-SHP-2 not checked per element. |
| tre | `tre:docs/reference/properties.md` (corner_radius); `tre:crates/engine-render/src/lib.rs` | Not applicable as a scale. The engine takes a radius per node (default 0, single value or four) and clamps by the renderer; scroll thumb radius 2 dp is a primitive. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Expressive steps 20, 32 and 48 dp excluded from the baseline | Baseline is the 2022 shape scale; Expressive adopted by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell scale has names shifted by one below `large` (`small` 4, `medium` 8) and two added steps `medium_large` (12) and `extra_large` (28) | The shell has its own flat token set; renaming would change the meaning of existing themes; the MD3 name `medium` would collide with the shell `medium` | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Popup container radius `extra_small` | MD3 has no popup; the menu value is used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
