---
title: 04 Shape Rules
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, shape, corner-radius]
related: ["[[Shape]]", "[[Elevation]]", "[[Focus Ring]]", "[[State Layers]]", "[[02 Colour and Theming]]", "[[07 Spacing and Density Rules]]", "[[01 Principles and Scope]]", "[[Button]]", "[[Icon Button]]", "[[Menu]]", "[[Tooltip]]", "[[Dialog]]", "[[Popup]]", "[[Panel and Surface]]", "[[Text Field]]", "[[Scrollbar and Scroll Container]]", "[[Switch]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[Deviations from MD3]]"]
depends_on: ["[[Shape]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# 04 Shape Rules

> [!info] Summary
> Chapter-level principles for choosing a corner radius: which shape token belongs to which class of element, how nested shapes, rings and clipping follow it. The scale and the radius of each overlay live in [[Shape]]; this chapter links to them and copies no value. Material Design 3 baseline: [shape](https://m3.material.io/styles/shape/overview).

## Purpose

Shape tells the user what an element is: a pill is an action, a small-radius sheet is an overlay, a square-cornered region is part of the window. One small scale makes that readable and makes radius a value that a test can read.

## Scope

- In scope: the choice of shape token by element class, nesting, clipping, focus ring and state layer shape, edge-attached containers.
- Out of scope: the scale ([[Shape]]), Expressive shape morphing (not baseline, [[ADR-0006 MD3 baseline with named Expressive adoptions]]), shadows ([[Elevation]]).

## Principles

1. Radius is a token. A container takes its corner radius from the scale of [[Shape]]; literal radii are allowed only for content masks and primitives (a scrollbar thumb is half its width, [[Scrollbar and Scroll Container]]).
2. Shape follows the class of element, not the taste of the view. Two elements of one class (two menus, two dialogs, two buttons of one variant) have the same radius.
3. Smaller surfaces take smaller radii. Overlays that are small and dense (menu, plain tooltip, popup) use the small steps; large floating surfaces (dialog) use the large step; actions and fields use the pill or the small steps by variant.
4. A shape is one fact for all its decorations. State layer, ripple, focus ring, shadow and clip all follow the same shape ([[State Layers]], [[Focus Ring]], [[Elevation]]).
5. Nested radii shrink. An inner rounded container has the outer radius minus the gap between them, never below 0 ([[Shape]] rule 3).
6. Edges are square. A container that touches a screen or window edge uses `none` on the touching side; the window itself follows the compositor's decoration.
7. Shape does not carry state alone. A selected or error state changes colour and a second cue; a project that changes shape on state (MD3 changes a button's radius when pressed in Expressive) does so only through a named deviation.
8. Baseline first. Expressive steps are not used without a named entry in [[Deviations from MD3]] ([[ADR-0006 MD3 baseline with named Expressive adoptions]]).

## Which shape for which element class

The token per element is stated in [[Shape]] (Radius of elements) and repeated in the component note. This table gives the rule by class.

| Element class | Shape token | Notes |
|---|---|---|
| Menu, plain tooltip, snackbar, popup | `extra_small` | popup has no MD3 counterpart and takes the menu value ([[Shape]]) |
| Rich tooltip, card, filled or tonal container in a panel | `medium` | |
| Dialog | `extra_large` | |
| Button (all variants), search bar, switch track, badge, chip pill | `full` (pill), clamped to half the shorter side | MD3 button shape is `full`; chip uses `small` in MD3 #needs-verification |
| Text field container | `extra_small` top corners for filled, `extra_small` all corners for outlined | [[Text Field]] #needs-verification |
| Icon button | `full` | state layer is a circle at icon size |
| List row, tree row, menu item | `none` for the row; the hover and selection layer follows the row | rows sit edge to edge in a container |
| Navigation bar, status bar, toolbar attached to a window edge | `none` | |
| Scrollbar thumb | half the thumb width (primitive) | |
| Focus ring | container radius plus the ring offset | [[Focus Ring]] |

## Nesting, clipping and attached edges

- A clipping container clips children to its rounded shape ([[Shape]] rule 5); a child never draws a square corner outside a rounded parent.
- A container whose child is a row that touches the container edge (a list in a menu) clips the row layer to the container radius.
- A panel that is docked to a window edge takes `none` on the docked side and its normal radius on the free side ([[Panel and Surface]]).
- A project does not draw a radius larger than half the shorter side; `full` is the only token that reaches it.

## Where each rule lives

| Topic | Note |
|---|---|
| Scale, Expressive steps, multi-corner shorthands, element radii, shell mapping | [[Shape]] |
| Focus ring and state layer shape | [[Focus Ring]], [[State Layers]] |
| Shadow shape | [[Elevation]] |
| Per-element radius | the component notes |

## Acceptance criteria

The criteria AC-SHP-1 to AC-SHP-6 are defined in [[Shape]].

- [ ] AC-C04-1 (token test): every component note of `30 Component Specifications` that has a container names its shape token, and the named token is one of the 7 baseline steps or a multi-corner shorthand of [[Shape]]. Pass: zero containers without a token, zero tokens outside the set.
- [ ] AC-C04-2 (token test): the shape token named in each component note equals the class rule in the table above. Pass: zero mismatches, or a recorded deviation row.
- [ ] AC-C04-3 (geometry check): two instances of one element class in one project (two menus, two dialogs, two filled buttons) report the same corner radius. Pass: equal radii for every class.
- [ ] AC-C04-4 (geometry check): for each rounded element with a focus ring, the ring radius equals the element radius plus 2 dp (outward) within 0.5 dp ([[Focus Ring]]).
- [ ] AC-C04-5 (pixel check): the hover layer and the ripple of a `full` button stay inside the pill: no layer pixel outside the shape at scale 1.0 and 2.0 ([[State Layers]] AC-STL-8).
- [ ] AC-C04-6 (geometry check): a rounded container with a rounded child at padding p reports the child radius equal to `max(0, outer radius - p)` within 0.5 dp.
- [ ] AC-C04-7 (geometry check): a panel docked to a window edge reports radius 0 on the docked corners.
- [ ] AC-C04-8 (token test): a static scan of all stylesheets of a project lists every `Corner_Radius` literal; each is a baseline step value or sits in the allow-list of primitives and content masks. Pass: zero hits outside.

## Status in code

Details per criterion are in [[Shape]].

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/tokens.py` (`SHAPES`, `FULL_RADIUS`); `tess-ui:src/tess_ui/views/*_Stylesheet.tdl` | Partly meets. Scale and the overlay radii meet; component stylesheets carry literals (12, 16, 28 for button sizes, 8 chip, 24 date picker day, 20 pagination item, 3 tabs indicator) so AC-C04-8 fails. AC-C04-3 and AC-C04-4 not run. |
| tess-shell | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` (lines 38 to 42) | Partly meets. 5 steps, no 12 and no 28; the dialog and rich tooltip steps cannot be expressed by token, so AC-C04-1 fails for dialog. |
| tre | `tre:docs/reference/properties.md` (corner_radius), `tre:crates/engine-render/src/lib.rs` | Not applicable as tokens. The node takes a radius per node, single or four values; the renderer clamps. Clipping to a rounded shape is by node. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Popup takes `extra_small` | MD3 has no popup; menu value used | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| No shape change on state or press | baseline scale only; Expressive shape morphing is not adopted | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| List rows are square (`none`) | desktop rows run edge to edge for density | [[ADR-0002 Desktop density levels and target sizes]] |
| Shell shape names are shifted by one step | shell keeps its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- Shape scale and component radii: https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192 (`_md-sys-shape.scss`, component files named in [[Shape]]); verified in [[Shape]] on 2026-11-21.
- MD3 shape overview: https://m3.material.io/styles/shape/overview (script-rendered, not readable by tools).
- Chip and text field shapes: component token files not re-read for this chapter #needs-verification.
