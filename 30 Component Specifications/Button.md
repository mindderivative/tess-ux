---
title: Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, action, owner-feedback]
related: ["[[Owner Feedback 2026-11-20]]", "[[Icon Button]]", "[[Text Field]]", "[[Switch]]", "[[Form Row]]", "[[Dialog]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Iconography]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Button

> [!info] Summary
> A pressable control with a text label and an optional icon: the Material Design 3 common [buttons](https://m3.material.io/components/buttons/overview) (elevated, filled, tonal, outlined, text), sized by density. Source of truth in code: see the last section.

## Purpose

Starts one action: Save, Apply, Browse, Reset to default. The label names the action in the user's words. A button with no label is an [[Icon Button]].

## When to use and not

- Use when: the action needs a visible text label; a dialog or form needs confirm and cancel.
- Do not use when: the action is a glyph the user knows (use [[Icon Button]]); a setting turns on and off (use [[Switch]]); a navigation target that reads as a link (use a Link, later).
- Emphasis: one filled button per view region; tonal and elevated for important secondary actions; outlined for medium; text for the lowest, in dialogs, cards and toolbars (tess-ui `docs/components/buttons.md`, the MD3 emphasis order).

## Anatomy

1. Container (filled, tonal, elevated, outlined; absent in the text variant).
2. Leading icon (optional), 18 dp at default and compact, 16 dp at dense.
3. Label, `label_large`.
4. Trailing icon (optional).
5. Loading spinner (replaces the leading icon).
6. State layer ([[State Layers]]).
7. Focus ring, keyboard focus only ([[Focus Ring]]).

## Variants

| Variant | Container | Label and icon | Outline | Elevation: rest, hover, focus, pressed |
|---|---|---|---|---|
| Filled | `primary` | `on_primary` | none | 0, 1, 0, 0 |
| Tonal | `secondary_container` | `on_secondary_container` | none | 0, 1, 0, 0 |
| Elevated | `surface_container_low` | `primary` | none | 1, 2, 1, 1 |
| Outlined | none | `primary` | 1 dp `outline` | 0 |
| Text | none | `primary` | none | 0 |

Elevation levels are those of [[Elevation]]. Toggle form (tess-ui `Toggle`): the colours and shape swap while selected. Values: Material Web token files [filled](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-button.scss), [tonal](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-tonal-button.scss), [elevated](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-elevated-button.scss), [outlined](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-button.scss), [text](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-text-button.scss).

## States

State layer percentages from [[State Layers]]: hover 8, focus 10, pressed 10 percent; disabled content 38 percent, disabled container 12 percent ([[ADR-0009 State layer percentages]]). The state layer uses the label colour.

| State | Visual change | Token values |
|---|---|---|
| Rest | variant colours | roles |
| Hover | state layer 8 percent; filled, tonal: elevation 1; elevated: elevation 2 | [[State Layers]], [[Elevation]] |
| Focus (keyboard) | state layer 10 percent; focus ring 3 dp wide, 2 dp offset, role `secondary` | [[Focus Ring]] |
| Pressed | state layer 10 percent; shape may square off (Expressive adoption, see Deviations) | [[State Layers]] |
| Disabled | label and icon `on_surface` at 38 percent; filled, tonal, elevated container `on_surface` at 12 percent and elevation 0; outlined outline `on_surface` at 12 percent | Material Web `disabled-*` tokens |
| Loading | spinner replaces the leading icon; the button takes no press while it shows; accessible state `busy` | review |
| Toggle selected | colours and shape swap (tess-ui) | tess-ui stylesheet |

The disabled button is not focusable and takes no pointer or key; the engine `disabled` flag only announces, so the control suppresses input itself (`tre:docs/guide/accessibility.md`).

## Tokens used

[[Colour Roles]] (variant roles), [[Typography]] (label `label_large`: 14 dp on 20 dp, weight 500; [Material Web typescale](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss)), [[Shape]] (`corner-full`), [[Elevation]], [[Motion]], [[Spacing and Density]].

## Sizing and density

MD3 values from Material Web: container 40 px, shape `corner-full`, label `label_large`, icon 18 px, padding 24 px each side (text button 12 px), with a leading icon 16 px leading and 24 px trailing, gap 8 px, minimum width 64 px ([button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-button.scss), [shared button styles](https://github.com/material-components/material-web/blob/main/button/internal/_shared.scss), touch target 48 px in [touch-target styles](https://github.com/material-components/material-web/blob/main/button/internal/_touch-target.scss)).

Tesserae by density ([[ADR-0002 Desktop density levels and target sizes]]; the control heights are binding, the paddings are design choices #needs-verification-as-design-choice):

| Level | Height | Horizontal padding (no icon) | With leading icon (leading, trailing) | Text variant padding | Icon | Gap icon to label |
|---|---|---|---|---|---|---|
| default | 40 dp | 24 dp | 16, 24 dp | 12 dp | 18 dp | 8 dp |
| compact | 32 dp | 16 dp | 12, 16 dp | 8 dp | 18 dp | 8 dp |
| dense | 28 dp | 12 dp | 8, 12 dp | 8 dp | 16 dp | 4 dp |

- Minimum width: 64 dp at default, 48 dp at compact and dense; never below 24 dp by 24 dp pointer target ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)); in touch contexts the hit area extends to 48 dp high beyond the container.
- The label is vertically centred in the container by construction, as for [[Text Field]] (space above and below the label line box equal ±0.5 dp). The shell's frame look failed this on KWin ("text not centred in buttons and panels", `tess-shell:docs/design/40 Specifications/Surfaces/Frame.md`).
- The button is as wide as its content unless the author sets a width; a text that does not fit follows Layout.

## Layout and overflow

- The label is one line. Overlong label: ellipsis at the end, the icon and padding stay; the full label is the accessible name and the tooltip (a tooltip on the button, never on a group). A button never grows taller than its height token.
- A row of buttons that runs out of width moves the lowest-emphasis buttons into a [[Menu]] or wraps to the next line; buttons never overlap and never draw outside their container ([[10 Layout Overflow and Scrolling]]).
- In a [[Dialog]] the actions align to the end, the confirm action last, gap 8 dp.

## Behaviour

- Pointer: press shows pressed; release inside the container activates once; a press that starts on the button and ends outside is no click; a press dismisses the tooltip ([[ADR-0004 Tooltip rule]]).
- Keyboard: Tab and Shift+Tab move focus; Enter and Space activate a focused button once; the pressed state shows while the key is held (tess-shell does this, `tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl`); a disabled or loading button takes no key.
- Default action: Enter on a focused text field in a [[Dialog]] activates the dialog's default button, specified in [[Dialog]].
- Touch: tap on the 48 dp hit area.

## Tooltip and overlay behaviour

A button whose label is fully visible needs no tooltip; a button with a truncated label or an extra description (shortcut, consequence) carries a plain tooltip on the button itself. Rules: [[Tooltip]] and [[ADR-0004 Tooltip rule]]. A button that opens a [[Menu]] or popup sets `expanded` and returns focus to itself on close.

## Motion

State layer fade `short2` (100 ms in MD3; tess-ui 15 ms hover); elevation change `short3` (150 ms); shape squaring when pressed 100 ms (Expressive). Reduced motion: state and elevation change at once; spinner remains but slows or becomes a static progress cue #needs-verification-as-design-choice.

## Accessibility

- Role: `button`; a toggle has `pressed`; a menu opener has `expanded` ([WAI-ARIA button](https://www.w3.org/TR/wai-aria-1.2/#button)).
- Name: the visible label text (WCAG 2.5.3 label in name). If the visible label is shortened, the full text is the name.
- Loading: `busy` true; the label stays the name; the result of the action is announced politely by the action's owner ([[14 Accessibility Basics]]).
- Contrast: label against container at least 4.5 to 1; outline against surface at least 3 to 1 ([WCAG 1.4.3, 1.4.11](https://www.w3.org/TR/WCAG22/)).
- Focus: ring visible, never clipped.

## Dark and light

All roles; follows the scheme ([[Theme Following the System]]). AC-BTN-9 runs in both.

## Defaults

Variant filled in tess-ui; tess-shell ships one bordered surface-raised look. Density from the container. Shape full (pill). No tooltip unless set.

## Acceptance criteria

- [ ] AC-BTN-1: Token test. Heights 40, 32, 28 dp at default, compact, dense; paddings, icon sizes and gaps equal the Sizing table. Pass: values equal.
- [ ] AC-BTN-2: Geometry check. The label line box is vertically centred in the container (space above equals space below ±0.5 dp) at each density and scale 1.0, 1.25, 2.0. Pass: offset at most 0.5 dp.
- [ ] AC-BTN-3: Pixel check. Rendered label glyph box centre within 1 px of the container centre vertically, for "Hg" and for a one-glyph label. Pass: offset at most 1 px.
- [ ] AC-BTN-4: Token test. Each variant's container, label, icon and outline resolve to the roles in the Variants table; no literal colour. Pass: every colour is a role reference.
- [ ] AC-BTN-5: Scripted input. Focus, press Enter, then Space: activation count 1 each; pointer press and release inside: 1; press, move out, release: 0; disabled and loading: 0 and no focus (disabled). Pass: counts equal.
- [ ] AC-BTN-6: Token test. State layer opacities equal the [[State Layers]] tokens (8, 10, 10); disabled label and icon 38 percent, disabled container and outline 12 percent. Pass: values equal.
- [ ] AC-BTN-7: AT tree assertion. Role `button`, name equal to the label, `disabled`, `busy`, `pressed` and `expanded` set from the state. Pass: all equal.
- [ ] AC-BTN-8: Geometry check. Pointer hit area at least 24 by 24 dp at every density, 48 dp high in touch; minimum width 64 and 48 dp. Pass: bounds at or above the limits.
- [ ] AC-BTN-9: Contrast script. Light and dark: label on container at least 4.5 to 1 for each variant, rest and disabled-excluded; outline on surface at least 3 to 1. Pass: ratios at or above the limits.
- [ ] AC-BTN-10: Geometry check. A label longer than the available width shows an ellipsis and no text pixel lies outside the container. Pass: ellipsis present, zero pixels outside.
- [ ] AC-BTN-11: Pixel check. Under keyboard focus the focus ring is 3 dp wide, 2 dp outside the container, role `secondary`, absent under mouse-click focus. Pass: measured ring equals.
- [ ] AC-BTN-12: Review. One filled button per view region, enforced by review of each view (not automatable).

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Button_View.tdl`, `Button_Stylesheet.tdl` | partly meets: five variants, icon, trailing icon, toggle, loading, Enter and Space, role button (AC-BTN-4, AC-BTN-5, AC-BTN-7 meet by reading the docs); sizes xs to xl are 32, 40, 56, 96, 136 px, default 40, so heights match default and compact but not dense (AC-BTN-1 partly); padding 24 (16 with icon, text 12) and gap 8 match MD3 at default; state layer, ripple and focus ring are the node's interaction (AC-BTN-6 partly: 8, 10, 10 percent in `tess-ui:src/tess_ui/interaction.py`); disabled filled container at 12 percent not built, a whole-button fade is used (AC-BTN-6 fails); Button sheet hard-codes shape radii 12, 16, 28 (Expressive, undocumented as a deviation) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | partly meets: role BUTTON with name from `Label` else `Text`, icon position, Enter and Space with pressed state, disabled via `Enabled: false` (AC-BTN-5, AC-BTN-7 meet by reading); one bordered surface-raised look, no variants (AC-BTN-4 absent), 32 px height literal (AC-BTN-1 partly), hover changes only the border, pressed background `outline`, disabled opacity 0.5 (AC-BTN-6 fails), label centring failed on KWin in 2026-11 (AC-BTN-2 unmeasured) |
| tre | none (no button primitive; hit-testable box with text) | not applicable |

Evidence: F8 (reset button showed the row tooltip), the shell Launcher hand check, and S1 in [[Owner Feedback 2026-11-20]].

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Button_View.tdl`, `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl`, `tess-ui:docs/components/buttons.md` | exists |
| tess-shell | `tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | exists, one look |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 28 dp; paddings reduced at compact and dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Icon 16 dp at dense | 28 dp container | [[ADR-0002 Desktop density levels and target sizes]] |
| Sizes xs, m, l, xl (32 to 136 px) and the square shape, pressed squaring (Expressive) | tess-ui implements Expressive sizes; the baseline is the 2022 scale | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| Pointer hit area is the container (24 dp floor), 48 dp only in touch contexts | desktop density, WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus ring 3 dp, 2 dp offset, `secondary` | [[Focus Ring]] | [[ADR-0009 State layer percentages]] |

## Sources

- [Material Web filled button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-button.scss) and the tonal, elevated, outlined and text files: height 40 px, shape `corner-full`, padding 24 px (text 12 px), leading-icon padding 16 and 24 px, icon 18 px, disabled container 0.12, disabled label 0.38, outline 1 px, elevation 0 rest and 1 hover (filled, tonal), 1 rest and 2 hover (elevated).
- [Material Web shared button styles](https://github.com/material-components/material-web/blob/main/button/internal/_shared.scss): gap 8 px, minimum width 64 px; [touch target](https://github.com/material-components/material-web/blob/main/button/internal/_touch-target.scss): 48 px.
- [Material Web typescale](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss): label large 0.875 rem on 1.25 rem, weight medium.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.3, 1.4.11, 2.5.3, 2.5.8.
- Code: `tess-ui:docs/components/buttons.md`, `tess-shell:src/tess_shell/shipped/Button/Button_Module.tdl`.
- The m3.material.io button specification could not be fetched (script-rendered); Expressive button sizes were not verified.
