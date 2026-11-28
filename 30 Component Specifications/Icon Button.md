---
title: Icon Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, action, owner-feedback]
related: ["[[Owner Feedback 2026-11-20]]", "[[Button]]", "[[Tooltip]]", "[[Text Field]]", "[[Form Row]]", "[[Iconography]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0007 Icon set and Material Symbols deviation]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[Colour Roles]]", "[[Iconography]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Tooltip]]"]
---

# Icon Button

> [!info] Summary
> A button shown as a glyph alone: the Material Design 3 [icon button](https://m3.material.io/components/icon-buttons/overview) in standard, filled, tonal and outlined emphasis, with a toggle form. Source of truth in code: see the last section.

## Purpose

An action or a toggle that a glyph names well enough, in toolbars, form rows (reset, browse, reveal), and tree or list rows. Because the glyph has no text, the name and the tooltip carry the meaning.

## When to use and not

- Use when: the action is common and the glyph is standard; space is tight; a tooltip names it.
- Do not use when: the action is rare or its glyph ambiguous (use a [[Button]] with a label); the control needs both icon and text (use a [[Button]] with a leading icon).

## Anatomy

1. Container: a circle (round) or rounded square, 40 dp at default; absent for the standard variant (the state layer shows the 40 dp shape).
2. Icon: 24 dp at default, 20 dp at compact and 18 dp at dense ([[Iconography]]).
3. State layer: same shape as the container ([[State Layers]]).
4. Hit area: the container, extended to 48 dp in touch contexts.
5. Focus ring: around the container, keyboard focus only ([[Focus Ring]]).

## Variants

| Variant | Container | Icon | Border |
|---|---|---|---|
| Standard | none | `on_surface_variant` (selected: `primary`) | none |
| Filled | `primary` (toggle off: `surface_container_highest`) | `on_primary` | none |
| Tonal | `secondary_container` | `on_secondary_container` | none |
| Outlined | none (selected: `inverse_surface`) | `on_surface_variant` (selected: `inverse_on_surface`) | 1 dp `outline` |

Toggle form: any variant with `selected` and an optional different icon for the selected state. Values: Material Web [icon button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-icon-button.scss), [filled](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-icon-button.scss), [tonal](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-tonal-icon-button.scss), [outlined](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-icon-button.scss).

## States

State layer percentages from [[State Layers]] (hover 8, focus 10, pressed 10 percent; disabled content 38, disabled container 12 percent).

| State | Visual change | Token values |
|---|---|---|
| Rest | variant colours above | roles |
| Hover | state layer over the container in the icon colour at 8 percent | [[State Layers]] |
| Focus (keyboard) | state layer 10 percent plus focus ring 3 dp, 2 dp offset, role `secondary` | [[State Layers]], [[Focus Ring]] |
| Pressed | state layer 10 percent; shape may square off (Expressive, see Deviations) | [[State Layers]] |
| Selected (toggle) | selected colours above; selected icon if given | roles |
| Disabled | icon `on_surface` at 38 percent; filled and tonal container `on_surface` at 12 percent; outlined border `on_surface` at 12 percent | Material Web `disabled-*` tokens |
| Loading | not applicable; use a [[Button]] with loading | none |

## Tokens used

[[Colour Roles]] (variant roles above), [[Shape]] (`corner-full` round; 12 dp square form is an Expressive adoption), [[Motion]] (state layer 15 ms at most in tess-ui; icon morph 200 ms; reduced motion switches at once), [[Spacing and Density]], [[Iconography]].

## Sizing and density

MD3: container 40 by 40 dp, icon 24 dp, touch target 48 dp ([Material Web icon button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-icon-button.scss): `container-height` and `container-width` 40 px, `icon-size` 24 px; [Material Web touch-target style](https://github.com/material-components/material-web/blob/main/button/internal/_touch-target.scss): height `max(48px, 100%)`; [Material Components Android IconButton](https://github.com/material-components/material-components-android/blob/master/docs/components/IconButton.md): "default dimensions allow for a touch target of 48dp").

Tesserae by density ([[ADR-0002 Desktop density levels and target sizes]], [[Spacing and Density]]):

| Level | Container | Icon | Minimum pointer hit area | Touch hit area |
|---|---|---|---|---|
| default | 40 dp | 24 dp | 40 dp (at least 24 dp) | 48 dp |
| compact | 32 dp | 20 dp | 32 dp (at least 24 dp) | 48 dp |
| dense | 28 dp | 18 dp | 28 dp (at least 24 dp) | 48 dp |

- Pointer target never falls below 24 dp by 24 dp ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)).
- In touch contexts the hit area extends to 48 dp beyond the container (centred, transparent), and must not overlap another control's hit area; where neighbours are closer than 48 dp the hit areas split the gap at the midpoint.
- Width kinds (narrow and wide, from MD3 Expressive) are allowed as named adoptions only; the default width equals the height.
- Gap between adjacent icon buttons: 4 dp at default and compact, 2 dp at dense, unless a [[Spacing and Density]] row says otherwise.

## Dimensions and defaults

Values agree with the Sizing table above. The padding is the margin around the icon inside the container, `(container - icon) / 2`; compact and dense values, the square-form radius and the gap at dense are design choices (#needs-verification-as-design-choice).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | `density.icon_button_container` | 40 | 32 | 28 | [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container | min width | `density.icon_button_container` | 40 | 32 | 28 | width equals height; [filled icon button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-icon-button.scss) | tess-ui: yes (style min_width); tess-shell: yes (Min_Width); tre: yes (min_width) |
| container | min height | `target.min` | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| container (touch hit area) | min height | `target.touch` | 48 | 48 | 48 | [[Spacing and Density]], touch context only | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| container | padding | `space.*` | 8 8 8 8 | 6 6 6 6 | 4 4 4 4 | derived from container and icon size, [[Spacing and Density]]; design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| container | margin | - | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| adjacent icon buttons | gap | `space.2` | 4 | 4 | 2 | [[Icon Button]] Sizing; design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| container | border width | - | 0 | 0 | 0 | [filled icon button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-icon-button.scss) | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| container (outlined variant) | border width | - | 1 | 1 | 1 | [outlined icon button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-icon-button.scss) | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| container | border color | - | N/A: standard, filled and tonal variants draw no border | N/A: standard, filled and tonal variants draw no border | N/A: standard, filled and tonal variants draw no border | [[Icon Button]] Variants table | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| container (outlined variant) | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| container (round form) | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]] (half the height) | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| container (square form) | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]], Expressive adoption, [[ADR-0006 MD3 baseline with named Expressive adoptions]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| container | font | - | N/A: the icon button shows no text; the label is only the name and tooltip | N/A: the icon button shows no text; the label is only the name and tooltip | N/A: the icon button shows no text; the label is only the name and tooltip | [[Icon Button]] Anatomy | tess-ui: n/a: the element shows no text; tess-shell: n/a: the element shows no text; tre: n/a: the element shows no text |
| icon | icon size | `density.icon_button_icon` | 24 | 20 | 18 | [[Spacing and Density]], [[Iconography]], [[ADR-0029 Desktop density and type scale]] (dense 20 to 18) | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]]; the icon button tokens define no elevation | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| focus ring | border width | - | 3 | 3 | 3 | [[Focus Ring]] | tess-ui: no hook; tess-shell: via Shadows (spread and offset of the block shadow ring); tre: n/a: tre draws no focus ring |
| focus ring | border color | `secondary` | `secondary` | `secondary` | `secondary` | [[Focus Ring]] | tess-ui: via App(focus_ring=) ring colour argument; tess-shell: via Shadows (colour of the block shadow ring); tre: n/a: tre draws no focus ring |
| focus ring | margin | - | 2 2 2 2 | 2 2 2 2 | 2 2 2 2 | [[Focus Ring]] (offset outside the container) | tess-ui: no hook; tess-shell: via Shadows (spread and offset of the block shadow ring); tre: n/a: tre draws no focus ring |

## Layout and overflow

The container never shrinks below its size, never clips its icon, and never draws a tooltip inside its own box. In a toolbar that runs out of width the toolbar scrolls or overflows into a [[Menu]] (toolbar rule, later); the icon buttons never overlap. In a [[Form Row]] the icon button sits at the row's end, aligned to the vertical centre.

## Behaviour

- Pointer: press shows the pressed state; release inside the container activates once; leaving before release cancels; a press dismisses the tooltip ([[ADR-0004 Tooltip rule]]).
- Keyboard: Tab focuses; Enter and Space activate (Space on key up, Enter on key down is allowed; the activation happens once); a toggle flips `selected`; a disabled icon button takes no focus and no key.
- Touch: tap on the 48 dp hit area activates.
- Long press: shows the tooltip in touch contexts; no other meaning.

## Tooltip and overlay behaviour

An icon-only button MUST have a tooltip, whose text equals its accessible name (WCAG 2.5.3 label in name is satisfied by construction). Per [[ADR-0004 Tooltip rule]]: plain tooltip, 500 ms hover delay, immediate on keyboard focus (not on mouse-click focus), dismissed on pointer leave, Escape, scroll of any ancestor, press or activation, removal, window focus loss; the tooltip is opaque (`inverse_surface`, `inverse_on_surface`) and clipped to the window ([[Tooltip]]). The tooltip belongs to the button, never to its row or toolbar.

## Motion

State layer fade at most 15 ms in tess-ui (hover), 100 ms in MD3 (`short2`); icon morph 200 ms between two closed shapes or two open lines in tess-ui; the toggle shape change at most 200 ms. Reduced motion: no morph, the new state at once.

## Accessibility

- Role: `button`; a toggle is `button` with state `pressed` (true or false) ([WAI-ARIA button](https://www.w3.org/TR/wai-aria-1.2/#button)).
- Name: required. The name is a verb phrase or the glyph's meaning ("Reset", "Browse", "Show password"). An icon button with no name fails AC-ICB-5; the shell warns at load for an unnamed icon-only Button (`tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl`).
- The icon is hidden from assistive technology (decorative) because the name carries the meaning.
- State: disabled; pressed for toggles; expanded when it opens a [[Menu]].
- Contrast: icon against container or surface at least 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); selected and unselected differ in more than colour (shape, icon swap or container).
- Focus: ring visible, not clipped.

## Dark and light

All roles; follows the scheme ([[Theme Following the System]]). The outlined selected colours (`inverse_surface`) invert with the scheme; AC-ICB-8 runs in both.

## Defaults

Variant standard; container and icon by the container's density; hit area equal to the container, 48 dp in touch contexts; tooltip from the name.

## Acceptance criteria

- [ ] AC-ICB-1: Token test. Container 40/32/28 dp and icon 24/20/18 dp at default, compact, dense. Pass: values equal.
- [ ] AC-ICB-2: Geometry check. The pointer hit area is at least 24 dp by 24 dp at every density; in the touch context at least 48 dp by 48 dp, centred on the container, extending beyond it. Pass: bounds at or above the limits.
- [ ] AC-ICB-3: Geometry check. The icon is centred in the container (±0.5 dp) and never clipped by it. Pass: offsets within tolerance, zero clipped icon pixels.
- [ ] AC-ICB-4: Scripted input. Focus, press Enter and separately Space: activation count 1 each; pointer press, drag out, release: count 0; disabled: no focus, count 0. Pass: counts equal.
- [ ] AC-ICB-5: AT tree assertion. Role `button`, non-empty name, `pressed` set for a toggle, `disabled` set when disabled, icon child hidden. Pass: all equal. A review of every icon button in the project's views confirms no unnamed icon button.
- [ ] AC-ICB-6: Scripted input. Hover for 600 ms shows a tooltip whose text equals the accessible name; press dismisses it; Tab focus shows it at once; Escape dismisses it. Pass: visibility at each step equals the [[Tooltip]] rule.
- [ ] AC-ICB-7: Token test. State layer opacities equal the [[State Layers]] tokens; disabled icon 38 percent, disabled container 12 percent. Pass: values equal.
- [ ] AC-ICB-8: Contrast script. In light and dark, icon on container 3 to 1 or more for each variant, selected and unselected, and icon against surface for the standard variant. Pass: ratios at or above the limit.
- [ ] AC-ICB-9: Pixel check. A toggle in selected and unselected state differs in shape, icon or container, not colour alone: the two renders differ in at least one non-colour feature (alpha-independent edge map). Pass: edge maps differ.
- [ ] AC-ICB-10: Geometry check. Two icon buttons in a row do not overlap hit areas in the touch context. Pass: intersection area zero.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/IconButton_View.tdl`, `IconButton_Stylesheet.tdl` | partly meets: four variants and toggle exist; `Label` is the name and the tooltip (AC-ICB-5 and AC-ICB-6 meet by reading the docs); sizes xs to xl are 32, 40, 56, 96, 136 px, not the 40/32/28 density levels (AC-ICB-1 fails at dense); 48 px touch target around a 40 px button not built (AC-ICB-2 fails); disabled filled container 12 percent not built, a whole-button fade is used (AC-ICB-7 fails); state layer percentages 8, 10, 10 and 16 match the [[State Layers]] tokens (`tess-ui:src/tess_ui/interaction.py`) |
| tess-ui | `tess-ui:src/tess_ui/views/IconButton_Stylesheet.tdl` dimensions | differs: icon 20, 24, 24 by size and container 32, 40, 56 by size, no density (spec icon 24, 20, 18 and container 40, 32, 28; AC-ICB-1) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl` dimensions | differs: icon-only Button uses the Button height literal 32 (spec container 40 at default; AC-ICB-1) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl` (icon-only Button) | partly meets: role BUTTON, `Label` is the name and the shell warns at load when an icon-only Button has no name (AC-ICB-5 meets by reading); no variants, no toggle form, no density, no tooltip tie-in for icon-only (AC-ICB-1, AC-ICB-6, AC-ICB-7 absent) |
| tre | none (no button primitive) | not applicable |

Evidence: F8 (the reset button showed the row tooltip) in [[Owner Feedback 2026-11-20]].

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/IconButton_View.tdl`, `tess-ui:src/tess_ui/views/IconButton_Stylesheet.tdl`, `tess-ui:docs/components/icon-buttons.md` | exists |
| tess-shell | `tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl` | Button with an icon, no icon-button variant |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Container 32 dp and 28 dp, icon 20 dp at compact and 18 dp at dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]], [[ADR-0029 Desktop density and type scale]] |
| 48 dp hit area only in touch contexts; pointer contexts use the container with a 24 dp floor | desktop density and WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Sizes xs to xl, width kinds, square shape and pressed squaring (Expressive) only as named adoptions | MD3 baseline is the 2022 scales | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| Icons from Material Design Icons, not Material Symbols | existing icon set | [[ADR-0007 Icon set and Material Symbols deviation]] |

## Sources

- [Material Web icon button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-icon-button.scss) and the filled, tonal and outlined files in the same folder: container 40 px, icon 24 px, state layer 40 px, disabled icon 0.38, disabled container 0.12, colours per variant.
- [Material Web touch target](https://github.com/material-components/material-web/blob/main/button/internal/_touch-target.scss): 48 px.
- [Material Components Android IconButton](https://github.com/material-components/material-components-android/blob/master/docs/components/IconButton.md): 48 dp touch target and the `contentDescription` requirement for icon-only buttons.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.11, 2.5.3, 2.5.8.
- Code: `tess-ui:docs/components/icon-buttons.md`, `tess-ui:src/tess_ui/interaction.py`.
- The size set xs to xl and width kinds in tess-ui are described there as Material 3 Expressive; the Expressive page was not fetched and is marked #needs-verification.
