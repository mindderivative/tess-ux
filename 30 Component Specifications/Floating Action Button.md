---
title: Floating Action Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, action]
related: ["[[Button]]", "[[Icon Button]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[Extended Floating Action Button]]", "[[Toolbar]]"]
depends_on: ["[[Button]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Floating Action Button

> [!info] Summary
> The floating action button (FAB) is the one primary action of a view as an icon in a raised container: Material Design 3 [floating action button](https://m3.material.io/components/floating-action-button/overview), in three sizes and four colours. The extended form with a label is [[Extended Floating Action Button]]. Source of truth in code: see Status in code.

## Purpose

Offers the single most important action of a view region (Compose, Add, New) where the user always finds it. It is the only control in the system that floats over content.

## When to use and not

- Use when: one action dominates the view and creating or adding is the main task; the view scrolls and the action must stay reachable.
- Do not use when: the view has several equal actions (use [[Button]] or a [[Button Group]]); the action is a toolbar command (use an [[Icon Button]]); the view is a dense config form where a [[Button]] in the form row is enough. A desktop view has at most one FAB. Config-style tools (the shell config app) use none.
- A FAB needs the icon to name the action: a FAB with an ambiguous glyph uses [[Extended Floating Action Button]].

## Anatomy

1. Container: square with rounded corners, raised.
2. Icon, 24 dp (36 dp at the large size).
3. Shadow from the elevation level ([[Elevation]]).
4. State layer in the icon colour ([[State Layers]]).
5. Focus ring, keyboard focus only ([[Focus Ring]]).

## Variants

| Variant | Container | Icon and state layer colour |
|---|---|---|
| Primary | `primary_container` | `on_primary_container` |
| Secondary | `secondary_container` | `on_secondary_container` |
| Tertiary | `tertiary_container` | `on_tertiary_container` |
| Surface | `surface_container_high` | `primary` |

Sizes: small, medium (the default FAB), large. Lowered variant: Material Web also defines a lowered elevation (rest level_1); Tesserae does not adopt it #needs-verification. Branded (Google logo) variants are not adopted: not applicable to Tesserae.

## States

State layer percentages from [[State Layers]] and [[ADR-0013 Focus and pressed state layer 10 percent]] (hover 8, focus 10, pressed 10 percent).

| State | Visual change | Token values |
|---|---|---|
| Rest | variant colours, elevation level_3 (6 dp) | `container-elevation` level3 |
| Hover | state layer 8 percent; elevation level_4 (8 dp) | `hover-container-elevation` level4 |
| Focus (keyboard) | state layer 10 percent; elevation level_3; focus ring 3 dp, 2 dp offset, role `secondary` | `focus-container-elevation` level3, [[Focus Ring]] |
| Pressed | state layer 10 percent; elevation level_3 | `pressed-container-elevation` level3 |
| Disabled | MD3 defines no disabled FAB. Tesserae: a view hides a FAB that cannot act; when it must stay visible, icon `on_surface` at 38 percent, container `on_surface` at 12 percent, elevation level_0, no state layer ([[State Layers]] disabled scheme) | design choice #needs-verification |

The disabled FAB is not focusable and takes no pointer or key; the control suppresses input itself (`tre:docs/guide/accessibility.md`).

## Tokens used

[[Colour Roles]] (the four variants), [[Shape]] (`medium` 12 dp small, `large` 16 dp medium, `extra_large` 28 dp large), [[Elevation]] (levels 3 and 4), [[Motion]], [[Spacing and Density]], [[Iconography]].

## Sizing and density

MD3 from Material Web v0_192 tokens (`fab-primary-small`, `fab-primary`, `fab-primary-large`): container 40, 56 and 96 px square, icon 24, 24 and 36 px, shape corner medium, large and extra-large; the touch target is 48 px for the small size ([Material Web FAB styles](https://github.com/material-components/material-web/blob/main/fab/internal/_fab.scss)).

Tesserae by density ([[ADR-0002 Desktop density levels and target sizes]]). Default keeps the MD3 sizes. Compact and dense shrink the small and medium FABs to the control heights of [[Button]]; the large FAB is a touch-context size and has no compact form below 72 dp. The compact and dense values are design choices #needs-verification.

| Size | default | compact | dense | Icon (default, compact, dense) | Corner |
|---|---|---|---|---|---|
| Small | 40 | 32 | 28 | 24, 20, 20 | 12 dp |
| Medium | 56 | 48 | 40 | 24, 24, 20 | 16 dp |
| Large | 96 | 72 | 56 | 36, 28, 24 | 28 dp |

- The container is square; the hit area is the container, at least 24 by 24 dp, and 48 dp in touch contexts (the small size grows its hit area to 48 dp, as Material Web does).
- The icon is centred in the container both ways (centre offset at most 0.5 dp).
- Position: the FAB sits 16 dp from the end and bottom edges of its view region at default, 12 dp at compact, 8 dp at dense (design choice #needs-verification); it never covers the scrollbar ([[Scrollbar and Scroll Container]]).

## Layout and overflow

- The FAB is out of flow in its region and floats over the content; the content gets bottom padding equal to the FAB size plus margin so the last item is reachable ([[10 Layout Overflow and Scrolling]]).
- No text: nothing to truncate. Never more than one FAB per region.
- A region too narrow for the FAB plus its margins moves the action into the toolbar as an [[Icon Button]] #needs-verification (design choice).

## Behaviour

- Pointer: press shows pressed; release inside activates once; press that ends outside is no click; a press dismisses the tooltip ([[ADR-0004 Tooltip rule]]).
- Keyboard: the FAB is a Tab stop in reading order after the region content it floats over (it is last in the focus order of its region); Enter and Space activate once; pressed state shows while the key is held.
- Touch: tap on the hit area.
- Scroll: a scrolling list may collapse an [[Extended Floating Action Button]]; a plain FAB does not move.

## Tooltip and overlay behaviour

A FAB has an icon only, so it carries a plain tooltip with its accessible name on the FAB itself ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]], [[Tooltip]]). The FAB menu (a speed dial that opens several actions) is not adopted: use a [[Split Button]] or a [[Menu]] #needs-verification (MD3 expressive FAB menu not verifiable).

## Motion

State layer fade `short2` (100 ms in MD3; tess-ui 15 ms hover); elevation change 200 ms (tess-ui `Transition`); shape changes follow the elevation transition. Reduced motion: state and elevation change at once ([[Motion]]).

## Accessibility

- Role: `button` ([WAI-ARIA button](https://www.w3.org/TR/wai-aria-1.2/#button)).
- Name: required, the action ("Compose"), never the icon name. It is also the tooltip text.
- Contrast: icon against container at least 3 to 1 for the non-text glyph (WCAG 1.4.11); container against the surface behind it is carried by the shadow, not a contrast rule.
- Focus ring visible and never clipped by the region.

## Dark and light

All four variants resolve from roles in both schemes ([[Theme Following the System]]); the shadow stays black at the levels of [[Elevation]]; in dark the tonal surface tint carries the level.

## Defaults

Variant primary, size medium, no tooltip text beyond the accessible name. Density from the container.

## Acceptance criteria

- [ ] AC-FAB-1 (token test): container sizes 40, 56, 96 dp at default for small, medium, large; compact 32, 48, 72; dense 28, 40, 56; icon sizes equal the Sizing table. Pass: values equal.
- [ ] AC-FAB-2 (token test): corner radii 12, 16, 28 dp for small, medium, large equal `medium`, `large`, `extra_large` of [[Shape]]. Pass: values equal, no literal.
- [ ] AC-FAB-3 (token test): each variant's container and icon resolve to the roles in the Variants table. Pass: every colour is a role reference.
- [ ] AC-FAB-4 (token test): elevation rest level_3, hover level_4, focus level_3, pressed level_3. Pass: values equal.
- [ ] AC-FAB-5 (token test): state layer opacities 8, 10, 10 percent from [[State Layers]]; disabled icon 38 percent, disabled container 12 percent. Pass: values equal.
- [ ] AC-FAB-6 (geometry check): the icon box centre is within 0.5 dp of the container centre on both axes at each size and density. Pass: offset at most 0.5 dp.
- [ ] AC-FAB-7 (scripted input): Tab to the FAB, press Enter then Space: 1 activation each; pointer press and release inside: 1; press, move out, release: 0; disabled: 0 and not focusable. Pass: counts equal.
- [ ] AC-FAB-8 (AT tree assertion): role `button`, non-empty name equal to the action text, `disabled` set from state. Pass: all equal.
- [ ] AC-FAB-9 (scripted input): hovering the FAB for the tooltip delay shows a tooltip with the accessible name; a press hides it; no tooltip appears on the region around the FAB ([[ADR-0004 Tooltip rule]]). Pass: tooltip text equals the name, hidden after press.
- [ ] AC-FAB-10 (geometry check): hit area at least 24 by 24 dp at every density, 48 by 48 dp in touch contexts; the FAB lies fully inside its region and does not overlap a visible scrollbar. Pass: bounds at or above limits, overlap area 0.
- [ ] AC-FAB-11 (pixel check): under keyboard focus the ring is 3 dp wide, 2 dp outside the container, role `secondary`, absent under mouse-click focus. Pass: measured ring equals.
- [ ] AC-FAB-12 (contrast script): light and dark, icon on container at least 3 to 1 for all four variants. Pass: ratios at or above 3.
- [ ] AC-FAB-13 (review): at most one FAB per view region. Pass: review of each view.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Fab_View.tdl`, `Fab_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/buttons.py` (`fab`), `tess-ui:docs/components/fabs.md`, test `tess-ui:tests/test_fab.py` | partly meets: four variants with the verified roles (AC-FAB-3 meets), sizes 40, 56, 96 and corners 12, 16, 28 as literals not role tokens (AC-FAB-1 partly at default, fails at compact and dense; AC-FAB-2 meets values, fails token), elevation 3 rest, 4 hover, 3 pressed (AC-FAB-4 meets; focus elevation not set), `Disabled` fades the whole FAB (AC-FAB-5 fails), role `button` with name from `Label` but a plain FAB has no `Label` unless given: icon-only FAB without `Label` has no accessible name and no tooltip (AC-FAB-8, AC-FAB-9 fail), no density, no placement or content padding (AC-FAB-10 not built) |
| tess-shell | none found | absent |
| tre | none | not applicable |

Use in tess-ui: the Toolbar view (`Fab_Icon`, `Fab_Label`, `On_Fab`) only; no app uses a FAB.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense FAB sizes (small 32 and 28, medium 48 and 40) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the container with a 24 dp floor; 48 dp only in touch contexts | WCAG 2.2 SC 2.5.8, desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed state layer 10 percent (Material Web v0_192 has 12) | latest tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Disabled FAB defined (MD3 has none) | a view may need to show an unavailable action | [[ADR-0009 State layer percentages]] |
| Lowered, branded and FAB menu variants not adopted | no desktop use | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- Material Web FAB tokens v0_192: [fab-primary](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-fab-primary.scss), [small](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-fab-primary-small.scss), [large](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-fab-primary-large.scss), [surface](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-fab-surface.scss), [tertiary](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-fab-tertiary.scss): sizes 40, 56, 96; icon 24, 24, 36; shapes corner-medium, corner-large, corner-extra-large; container elevation level3, hover level4, focus level3, pressed level3; primary container `primary-container`; surface container `surface-container-high`, icon `primary`.
- [Material Web elevation values](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-elevation.scss): level3 6 px, level4 8 px.
- [Material Web FAB styles](https://github.com/material-components/material-web/blob/main/fab/internal/_fab.scss) and [FAB docs](https://github.com/material-components/material-web/blob/main/docs/components/fab.md): sizes, 48 px touch margin for small.
- [WAI-ARIA 1.2 button](https://www.w3.org/TR/wai-aria-1.2/#button); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.11, 2.5.8.
- Code: `tess-ui:docs/components/fabs.md`. The m3.material.io FAB page could not be fetched (script-rendered).
