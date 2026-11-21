---
title: 05 Elevation Rules
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, elevation, tone, shadow]
related: ["[[Elevation]]", "[[Scrim]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[02 Colour and Theming]]", "[[12 Overlays]]", "[[01 Principles and Scope]]", "[[Panel and Surface]]", "[[Menu]]", "[[Tooltip]]", "[[Popup]]", "[[Dialog]]", "[[Button]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[Deviations from MD3]]"]
depends_on: ["[[Elevation]]", "[[Colour Roles]]"]
---

# 05 Elevation Rules

> [!info] Summary
> Chapter-level principles for when an element is elevated, when a tonal container is enough, and how layers, shadows and scrims relate. The levels, shadows and the container per level live in [[Elevation]]; this chapter links and copies no value. Material Design 3 baseline: [elevation](https://m3.material.io/styles/elevation/overview).

## Purpose

Elevation shows which layer is above which. On a desktop with many regions side by side, shadows everywhere add noise; tone separates regions more cheaply. The chapter keeps shadows for the layers that float and uses tone for the regions that sit.

## Scope

- In scope: choosing between a shadow, a tonal container and a plain surface; layer ordering; shadows in layer windows; state-driven elevation; scrim.
- Out of scope: level values, shadow geometry and container mapping ([[Elevation]]), scrim values ([[Scrim]]), overlay behaviour ([[12 Overlays]]).

## Principles

1. Tone first, shadow for what floats. Regions that sit in the window (panels, sidebars, cards in a grid, list groups) separate by container role. Elements that float above the window (menu, popup, rich tooltip, dialog, snackbar) have a level and a shadow ([[Elevation]]).
2. One level per element. An element is at one level; its container role comes from the level table, so level and tone cannot disagree ([[Elevation]] rule 1).
3. No tint. No colour is blended into a surface because of elevation ([[Elevation]] rule 2); the tonal ladder is the only tone change.
4. Levels are for layers, not decoration. Elevation never highlights content (a selected row does not rise). Selection and emphasis use state layers and colour roles ([[State Layers]], [[Colour Roles]]).
5. Higher layer, higher level. A layer opened from another layer has a level at least equal to its opener; a modal sits above its scrim ([[Scrim]]).
6. The ceiling is level 5 (12 dp). No element and no state goes above it.
7. A shadow is part of the surface. A layer window reserves a transparent margin for its shadow and the shadow is never clipped by the window edge ([[Elevation]] rule 4).
8. Elevation change is state feedback. A hover or press elevation change animates with the duration token of [[Elevation]] rule 6 and is zero under reduced motion ([[06 Motion Rules]]).
9. Dark scheme keeps shadows. The container ladder carries the separation in dark; the shadow stays at the same level values ([[Elevation]]).

## When to elevate and when to use tone

| Situation | Use | Why |
|---|---|---|
| Panel, sidebar, region of the window | tonal container (`surface_container_low` to `surface_container`), level 0 | regions touch each other; a shadow between neighbours is noise |
| Card inside a panel | filled or outlined card, level 0; elevated card at level 1 only when it must read as lifted | MD3 offers three card styles |
| Elevated button | level 1 only where it sits on a surface of its own tone | [[Button]] |
| Menu, popup, rich tooltip | level 2 shadow plus container | floating, closes on outside click |
| Dialog and search bar | level 3 | modal or focus-capturing |
| Plain tooltip | no shadow, container `inverse_surface` | MD3 plain tooltip has no elevation token |
| Snackbar | level 3, `inverse_surface` | MD3 |
| Dragged item | pressed or dragged state layer, no extra level | [[State Layers]] |
| Scrollbar thumb, divider, selected row | none | primitives and state |

## Layers and ordering

- Z-order follows level: a menu opened from a dialog is above it, a tooltip on a menu item is above the menu ([[12 Overlays]]).
- Two layers of the same level never overlap without a scrim or a gap; the later one is above.
- A modal layer dims what is below with the scrim and blocks input to it ([[Scrim]], [[Dialog]]).
- A layer window (popup, tooltip, shell panel) is transparent around the container so that the shadow lives inside it; the margin is the one in [[Elevation]].

## Where each rule lives

| Topic | Note |
|---|---|
| Levels, shadow geometry, container per level, margins | [[Elevation]] |
| Colour roles of the containers | [[Colour Roles]] |
| Scrim | [[Scrim]] |
| Layer behaviour | [[12 Overlays]] |
| State layers on elevated elements | [[State Layers]] |

## Acceptance criteria

The criteria AC-ELV-1 to AC-ELV-8 are defined in [[Elevation]].

- [ ] AC-C05-1 (token test): the maximum elevation level in the theme and in every component note is at most 5, and the maximum dp is at most 12. Pass: zero values above level 5 or 12 dp.
- [ ] AC-C05-2 (token test): every component note that names an elevation level names a level from `level_0` to `level_5` and the container role equal to the level row of [[Elevation]]. Pass: zero mismatches.
- [ ] AC-C05-3 (pixel check): a panel, a sidebar and a region at level 0 show no shadow: the pixel 2 dp outside each region's border equals the neighbour's container colour. Pass: 3 of 3.
- [ ] AC-C05-4 (pixel check): for each floating element (menu, popup, rich tooltip, dialog, snackbar) the pixel 2 dp outside the bottom edge is darker than the surface below, and the pixel 40 dp outside equals it. Pass: 5 of 5; the plain tooltip passes the inverse (no shadow).
- [ ] AC-C05-5 (scripted input): a layer opened from a layer is drawn above it and its level is at least the opener's level. Pass: z-order and level checks hold for menu from dialog and tooltip from menu.
- [ ] AC-C05-6 (scripted input): with reduced motion on, an elevation change by hover or press reaches its end state on the next frame; with it off it finishes within the `short4` duration plus 2 frames ([[Motion]]).
- [ ] AC-C05-7 (review): no selected, focused or hovered element changes its elevation level to show that state, except an element whose note lists the change. Pass: reviewer finds none unlisted.
- [ ] AC-C05-8 (token test): in dark and light, a modal layer is drawn above a scrim of the opacity in [[Scrim]] and the scrim has level 0. Pass: both schemes.

## Status in code

Detail per criterion is in [[Elevation]].

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/tokens.py` (`ELEVATION_LEVELS`, `elevation_shadows`); `tess-ui:src/tess_ui/views/*_Stylesheet.tdl` | Partly meets. Shadows equal the table for levels 1 to 5; the maximum level is 5 (AC-C05-1 meets as index; the dp values are not stored). Container role per level in the view stylesheets is not verified (AC-C05-2 not run). No tint (AC-ELV-8 meets). |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`; `tess-shell:src/tess_shell/binder/shadow.py` | Absent against levels. One maximum shadow scaled by percent; no tonal ladder, only `surface` and `surface_raised`. AC-C05-1, AC-C05-2 and AC-C05-4 cannot pass in their level form. |
| tre | `tre:docs/guide/painting.md` (Shadows); `tre:docs/reference/layer-window.md` | Not applicable as levels. A shadow list per node; layer windows need a transparent margin and `input_region="geometry"`. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Containers for level 4 and 5 are `surface_container_highest` | no component token file gives them; keeps the ladder monotonic | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Regions of a window separate by tone at level 0, not by shadow | desktop windows have many neighbouring regions | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell keeps one scalable shadow | shell has its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- Elevation levels and shadows: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-elevation.scss and `elevation/internal/_elevation.scss` (verified in [[Elevation]], 2026-11-21).
- Surface with elevation overlay replaced by surface container roles: https://github.com/material-components/material-components-android/blob/master/docs/theming/Color.md (verified in [[Elevation]]).
- MD3 elevation overview: https://m3.material.io/styles/elevation/overview (script-rendered, not readable by tools).
- The choice of tone for window regions is a Tesserae rule #needs-verification (no MD3 page read for desktop regions).
