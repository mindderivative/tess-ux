---
title: Extended Floating Action Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, action]
related: ["[[Button]]", "[[Icon Button]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[Floating Action Button]]", "[[Toolbar]]"]
depends_on: ["[[Button]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Floating Action Button]]"]
---

# Extended Floating Action Button

> [!info] Summary
> A [[Floating Action Button]] with a text label, for a primary action that an icon alone does not explain: Material Design 3 [extended FAB](https://m3.material.io/components/extended-fab/overview). It shares colours, elevation and states with the FAB; this note holds only what differs. Source of truth in code: see Status in code.

## Purpose

Names the single main action of a view region in words ("Compose", "New") and can collapse to an icon FAB while the list under it scrolls.

## When to use and not

- Use when: the main action needs a word to be understood; the view has room for a 56 dp wide-to-content control.
- Do not use when: the action is common knowledge (use [[Floating Action Button]]); there are several equal actions ([[Button Group]]); the action fits a [[Button]] in the form or toolbar. At most one per view region, and never together with a plain FAB in the same region.

## Anatomy

1. Container: pill-sized rounded rectangle, 56 dp high, as wide as its content.
2. Leading icon (optional), 24 dp.
3. Label, `label_large`.
4. State layer, shadow, focus ring as for the FAB ([[State Layers]], [[Elevation]], [[Focus Ring]]).

## Variants

Same four colour variants as the [[Floating Action Button]] (primary, secondary, tertiary, surface; label and icon use the same "on" role). Forms: icon plus label; label only (no icon); collapsed (icon only, the label becomes the tooltip and stays the name).

## States

States, state layers (8, 10, 10 percent) and elevation (rest level_3, hover level_4, focus level_3, pressed level_3) are those of [[Floating Action Button]]; the state layer uses the label colour. The collapsed form behaves as the FAB. Verified in the `extended-fab-primary` tokens (hover level4, focus, pressed level3, rest level3; lowered rest level1, not adopted) #needs-verification for lowered hover and pressed.

## Tokens used

As [[Floating Action Button]]; label `label_large` ([[Typography]]: 14 on 20, weight 500, `label-text-size` and `label-text-weight` map to the `label-large` tokens); shape `large` (16 dp).

## Sizing and density

MD3 (Material Web `extended-fab-primary`): container height 56 px, shape corner-large (16 px), icon 24 px, label `label-large`; padding inline 16 px before the icon and 20 px after the label, 20 px on both sides when there is no icon ([Material Web FAB styles](https://github.com/material-components/material-web/blob/main/fab/internal/_fab.scss)). The gap between icon and label is 8 dp in tess-ui and was not verified in Material Web #needs-verification.

Tesserae by density ([[ADR-0002 Desktop density levels and target sizes]]; compact and dense are design choices #needs-verification):

| Level | Height | Padding before icon, after label | Padding with no icon | Icon | Gap icon to label | Corner |
|---|---|---|---|---|---|---|
| default | 56 | 16, 20 | 20, 20 | 24 | 8 | 16 |
| compact | 40 | 12, 16 | 16, 16 | 20 | 8 | 12 |
| dense | 32 | 8, 12 | 12, 12 | 20 | 4 | 8 |

- Width is the content width, minimum height by height (never narrower than a square FAB of the same height); maximum width is the region width minus twice the margin.
- The label line box is vertically centred in the container (space above equals space below ±0.5 dp) at every density.
- Collapsed: the container is the square of the [[Floating Action Button]] size for the same density.
- Hit area as the FAB.

## Dimensions and defaults

Values agree with the Sizing table above and the FAB elevations; compact and dense values and the placement margin are design choices (#needs-verification-as-design-choice).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | 56 | 40 | 32 | [Material Web extended FAB tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-extended-fab-primary.scss); compact and dense design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | min width | - | 56 | 40 | 32 | never narrower than a square FAB of the same height, [[Extended Floating Action Button]] Sizing | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| container | min height | `target.min` | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| container (touch hit area) | min height | `target.touch` | 48 | 48 | 48 | [[Spacing and Density]], touch context only | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| container (icon and label) | padding | `space.*` | 0 20 0 16 | 0 16 0 12 | 0 12 0 8 | [Material Web FAB styles](https://github.com/material-components/material-web/blob/main/fab/internal/_fab.scss); compact and dense design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container (label only) | padding | `space.*` | 0 20 0 20 | 0 16 0 16 | 0 12 0 12 | Material Web FAB styles; compact and dense design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container (placement in the view region) | margin | `space.5` | 0 16 16 0 | 0 12 12 0 | 0 8 8 0 | as [[Floating Action Button]]; design choice, proposed ADR for FAB placement margins | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| container | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| container | border width | - | 0 | 0 | 0 | [Material Web extended FAB tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-extended-fab-primary.scss) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| container | border color | - | N/A: the extended FAB container draws no border | N/A: the extended FAB container draws no border | N/A: the extended FAB container draws no border | [[Extended Floating Action Button]] Variants | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container | corner radius | `shape.large` | 16 | 12 | 8 | [[Shape]] (`large`, `medium`, `small`); compact and dense design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| label | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height, letter_spacing) |
| leading icon | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Iconography]], [[Extended Floating Action Button]] Sizing | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| container (rest, focus, pressed) | elevation | `elevation.level3` | 3 | 3 | 3 | as [[Floating Action Button]], [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| container (hover) | elevation | `elevation.level4` | 4 | 4 | 4 | as [[Floating Action Button]], [[Elevation]] | tess-ui: via stylesheet Rule (State: hovered, Elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| focus ring | border width | - | 3 | 3 | 3 | [[Focus Ring]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring | border color | `secondary` | `secondary` | `secondary` | `secondary` | [[Focus Ring]] | tess-ui: via App(focus_ring=) ring colour argument; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring | margin | - | 2 2 2 2 | 2 2 2 2 | 2 2 2 2 | [[Focus Ring]] (offset outside the container) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |

## Layout and overflow

- One line. A label longer than the maximum width ends with an ellipsis; the full label stays the name and the tooltip ([[10 Layout Overflow and Scrolling]]).
- Out of flow, positioned and padded as the FAB ([[Floating Action Button]]).
- Collapse and extend: bound to scroll direction (collapse when the list scrolls down, extend when it scrolls up) or to the user's choice. The width change animates over 200 ms where the engine can; a width that switches at once is a deviation of the engine, not of the spec ([[Motion]]) #needs-verification.

## Behaviour

As [[Floating Action Button]]. Collapse never changes focus: a focused FAB stays focused and keeps its ring when it collapses.

## Tooltip and overlay behaviour

Extended form with a visible label: no tooltip needed unless the label is truncated. Collapsed form: plain tooltip with the label on the FAB ([[ADR-0004 Tooltip rule]], [[Tooltip]]).

## Motion

Collapse and extend: width and label opacity ease together over `medium2` 300 ms (MD3 extended FAB) #needs-verification; with reduced motion the change is instant. State layer and elevation as the FAB.

## Accessibility

- Role `button`; the name is the label in both forms (WCAG 2.5.3 label in name).
- A collapse is not announced; the name does not change.
- Contrast: label against container at least 4.5 to 1 (WCAG 1.4.3).

## Dark and light

As [[Floating Action Button]]; AC-EFB-7 runs in both.

## Defaults

Variant primary, icon plus label, extended (not collapsed).

## Acceptance criteria

- [ ] AC-EFB-1 (token test): heights 56, 40, 32 dp at default, compact, dense; paddings, icon sizes and gaps equal the Sizing table. Pass: values equal.
- [ ] AC-EFB-2 (geometry check): the label line box is vertically centred (offset at most 0.5 dp) at each density and scale 1.0, 1.25, 2.0. Pass: offset at most 0.5 dp.
- [ ] AC-EFB-3 (pixel check): label glyph box centre within 1 px of the container centre vertically for "Hg". Pass: offset at most 1 px.
- [ ] AC-EFB-4 (token test): colours, elevation levels (3, 4, 3, 3) and state layer opacities (8, 10, 10) equal those of [[Floating Action Button]] with the label colour for the layer. Pass: values equal.
- [ ] AC-EFB-5 (geometry check): a label longer than the maximum width shows an ellipsis and no text pixel lies outside the container. Pass: ellipsis present, zero pixels outside.
- [ ] AC-EFB-6 (AT tree assertion): role `button`, name equal to the label in the extended and in the collapsed form. Pass: both equal.
- [ ] AC-EFB-7 (contrast script): light and dark, label and icon on container at least 4.5 to 1 for all variants. Pass: ratios at or above 4.5.
- [ ] AC-EFB-8 (scripted input): collapsing while focused keeps focus on the control; collapsed hover shows a tooltip with the label; extended hover shows none unless truncated. Pass: focus owner equals the FAB, tooltip text equals the label or is absent as stated.
- [ ] AC-EFB-9 (geometry check): the collapsed width equals the height of the matching FAB size at every density; the width change is monotonic over at most 300 ms with motion enabled and a single frame with reduced motion. Pass: values equal, frame count as stated.
- [ ] AC-EFB-10 (scripted input): Enter, Space, pointer counts as in AC-FAB-7. Pass: counts equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Fab_View.tdl`, `Fab_Stylesheet.tdl`, `tess-ui:docs/components/extended-fabs.md`, `tess-ui:src/tess_ui/widgets/buttons.py` (`extended_fab`) | partly meets: 56 high, padding 16 and 20 for icon plus label (AC-EFB-1 meets at default; fails compact and dense; label-only padding is 16 and 20 not 20 and 20), gap 8 (meets), `label_large`, name from `Label`, collapsed form with label tooltip (AC-EFB-6, AC-EFB-8 meet by reading), no easing of collapse because the width goes between a number and `auto` (AC-EFB-9 fails), disabled fades the whole control (AC-EFB-4 partly), label centring not measured (AC-EFB-2 unmeasured) |
| tess-ui | `tess-ui:src/tess_ui/views/Fab_Stylesheet.tdl` dimensions | differs: height 56 at every density (spec 40, 32 at compact and dense; AC-EFB-1); label-only padding 16 and 20 (spec 20 and 20); icon 24 at every density (spec 20) |
| tess-shell | none found | absent |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense heights 40 and 32 | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the container with a 24 dp floor | desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| State layer 10 percent for focus and pressed | latest tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Other deviations as [[Floating Action Button]] | shared | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- Material Web [extended-fab-primary tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-extended-fab-primary.scss): height 56 px, corner-large, icon 24 px, label-large, container elevation level3, hover level4, focus and pressed level3, lowered level1.
- [Material Web FAB styles](https://github.com/material-components/material-web/blob/main/fab/internal/_fab.scss): padding inline 16 px and 20 px, 20 px without icon.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.3, 2.5.3; [WAI-ARIA button](https://www.w3.org/TR/wai-aria-1.2/#button).
- Code: `tess-ui:docs/components/extended-fabs.md`, `tess-ui:docs/components/fabs.md`.
