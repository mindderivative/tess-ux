---
title: Checkbox
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, selection, input]
related: ["[[Switch]]", "[[Toggle]]", "[[Radio Button]]", "[[Form Row]]", "[[List Item]]", "[[Tree Node]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Validation]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Colour Roles]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Switch]]"]
---

# Checkbox

> [!info] Summary
> A control that marks one option as chosen or not, or one parent as all, some or none of its children: the Material Design 3 [checkbox](https://m3.material.io/components/checkbox/overview), with the three density levels of [[Spacing and Density]]. Source of truth in code: see Status in code.

## Purpose

Let the user pick any number of options from a set, accept a single statement ("I have read the terms"), or choose all, some or none of a list through a parent checkbox. A checkbox records a choice that takes effect later (on Save, Apply or OK). A control that takes effect at once is a [[Switch]].

## When to use and not

- Use when: the user may pick zero, one or several options; the change applies later; a selection column in a [[List]] or [[Tree]] needs a per-row mark.
- Do not use when: the change applies at once (use [[Switch]]); exactly one of several options is chosen (use [[Radio Button]]); the choice is an action (use [[Button]]); the two states are not yes and no (use a segmented control).

## Anatomy

1. Container (box): an 18 dp square with a 2 dp corner and a 2 dp outline when unselected.
2. Mark: a check (selected) or a dash (indeterminate), drawn in a 18 dp view box.
3. State layer: a circle behind the box, drawn on hover, focus and press per [[State Layers]].
4. Label: text beside the box; part of the press target.
5. Supporting text (optional): error or help text below the label; supplied by [[Form Row]] or the surrounding pattern, never inside the box.
6. Focus ring: around the state layer, keyboard focus only ([[Focus Ring]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Two-state | default | unselected and selected |
| Three-state (indeterminate) | a parent of children that are partly selected | the dash replaces the check; state `mixed` |
| Labelled | always in forms | label after the box (before it in right-to-left locales) |
| Box only | in a table or list row where the row name serves as the label | no label; the row name must name the box (AC-CHK-8) |

## States

State layer percentages come from [[State Layers]] (hover 8, focus 10, pressed 10 percent; [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). Colours are those of the Material Web checkbox tokens ([latest `_md-comp-checkbox.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss)):

| State | Box fill | Outline | Mark | State layer (colour, opacity) |
|---|---|---|---|---|
| Unselected, rest | none | 2 dp `on_surface_variant` | none | none |
| Unselected, hover and focus | none | 2 dp `on_surface` | none | `on_surface`, 8 and 10 percent |
| Unselected, pressed | none | 2 dp `on_surface` | none | `primary`, 10 percent |
| Selected, rest | `primary` | 0 dp | `on_primary` check | none |
| Selected, hover and focus | `primary` | 0 dp | `on_primary` | `primary`, 8 and 10 percent |
| Selected, pressed | `primary` | 0 dp | `on_primary` | `on_surface`, 10 percent |
| Indeterminate | as Selected | as Selected | `on_primary` dash | as Selected |
| Error, unselected | none | 2 dp `error` | none | `error`, 8, 10, 10 percent |
| Error, selected or indeterminate | `error` | 0 dp | `on_error` | `error`, 8, 10, 10 percent |
| Disabled, unselected | none | 2 dp `on_surface` at 38 percent | none | none |
| Disabled, selected or indeterminate | `on_surface` at 38 percent | 0 dp | `surface` | none |
| Keyboard focus | as the state | as the state | as the state | focus ring 3 dp, offset 2 dp, role `secondary` |

The disabled container is 38 percent here, not the 12 percent of the generic scheme in [[State Layers]]: the Material Web checkbox tokens set `selected.disabled.container.opacity` and `unselected.disabled.container.opacity` to 0.38, which this note follows because the box is the only visible part of a disabled checkbox. The label is `on_surface` at 38 percent.

The pressed layer colour follows the tokens (`primary` for unselected, `on_surface` for selected); hover and focus layers use the colour of the state.

A state is never shown by colour alone: the check and dash shapes carry selected and indeterminate ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)); error adds supporting text with an icon outside the box ([[Validation]]).

## Tokens used

[[Colour Roles]] (roles above), [[Shape]] (box corner 2 dp, a component value below `extra_small`; state layer `corner-full`), [[Motion]], [[Spacing and Density]], [[State Layers]], [[Focus Ring]]. The mark stroke is 2 dp at all levels.

## Sizing and density

MD3 values (Material Web tokens): container 18 dp, icon 18 dp, state layer 40 dp, outline 2 dp, container shape 2 dp; the Material Web wrapper gives a touch target of 48 dp ([`checkbox/internal/_checkbox.scss`](https://github.com/material-components/material-web/blob/main/checkbox/internal/_checkbox.scss): `margin: max(0px, (48px - container-size) / 2)`, input 48 by 48 dp). Android: minimum size `minTouchTargetSize` (48 dp) ([Checkbox docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Checkbox.md)).

Rule: the row height is the control height of the level; the state layer equals the row height; the box is 18 dp at default, 16 dp at compact and 14 dp at dense (compact and dense are Tesserae design choices, [[ADR-0029 Desktop density and type scale]]); the icon-to-label gap is `density.icon_label_gap` (8, 8, 4 dp).

| Level | Row height | Box | State layer | Gap box to label | Mark view box |
|---|---|---|---|---|---|
| default | 40 dp | 18 dp | 40 dp | 8 dp | 18 dp |
| compact | 32 dp | 16 dp | 32 dp | 8 dp | 16 dp |
| dense | 28 dp | 14 dp | 28 dp | 4 dp | 14 dp |

The compact and dense rows are Tesserae design choices #needs-verification-as-design-choice (MD3 gives one size).

- Pointer target: the box plus its label, never smaller than 24 by 24 dp ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)); a box-only checkbox has a square target equal to the state layer (40, 32, 28 dp). In a touch context the hit area is 48 by 48 dp, centred on the box, without overlapping a neighbour ([[Spacing and Density]]).
- The row horizontal padding follows the container.

## Dimensions and defaults

Box sizes and outline come from the Material Web checkbox tokens; row heights, state layer sizes and the compact and dense box follow [[ADR-0002 Desktop density levels and target sizes]] (#needs-verification-as-design-choice for every compact and dense value and for the label font, which the tokens do not set).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| row | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| row | min width | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style min_width); tess-shell: yes (Min_Width); tre: yes (min_width) |
| row | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| row | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | design choice, [[ADR-0002 Desktop density levels and target sizes]] (the state layer supplies the space around the box) | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| row | margin | - | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| row | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| row | border width | - | 0 | 0 | 0 | [[Spacing and Density]], the row draws no border; the box has its own | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| row | border color | - | N/A: the row draws no border | N/A: the row draws no border | N/A: the row draws no border | [[Spacing and Density]] | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| row | corner radius | - | N/A: the row draws no container | N/A: the row draws no container | N/A: the row draws no container | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| row | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| box | height | - | 18 | 16 | 14 | [md-comp-checkbox](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss); compact and dense: design choice, [[ADR-0029 Desktop density and type scale]] | tess-ui: no hook (Checkbox.SIZE); tess-shell: via module override (Height: 18 in Checkbox_Module.tdl); tre: yes (height) |
| box | border width | - | 2 | 2 | 2 | [md-comp-checkbox](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss) (unselected; 0 when selected) | tess-ui: no hook (box built with stroke_width 2.0 in Checkbox._build); tess-shell: yes (Border_Width); tre: yes (border_width) |
| box | border color | `on_surface_variant` | `on_surface_variant` | `on_surface_variant` | `on_surface_variant` | [md-comp-checkbox](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss) (unselected rest) | tess-ui: via widget option color (selected colour) and theme roles on_surface_variant and error; tess-shell: yes (Border_Color); tre: yes (border_color) |
| box | corner radius | - | 2 | 2 | 2 | [md-comp-checkbox](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss), a component value below `shape.extra_small` | tess-ui: no hook (box built with corner_radius 2.0 in Checkbox._build); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| box | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: no hook (box is a Python-drawn node with no elevation option); tess-shell: yes (Elevation percentage on the Checkbox::box Rectangle); tre: yes (shadows) |
| mark | icon size | - | 18 | 16 | 14 | [md-comp-checkbox](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss); compact and dense: design choice, [[ADR-0029 Desktop density and type scale]] | tess-ui: no hook (Checkbox.SIZE and the CHECK path in controls.py); tess-shell: via module override (Width: 18, Height: 18 in Checkbox_Module.tdl); tre: yes (width, height of the svg node) |
| state layer | height | `density.control_height` | 40 | 32 | 28 | [md-comp-checkbox](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss); compact and dense: design choice, [[ADR-0029 Desktop density and type scale]] | tess-ui: no hook (STATE_LAYER_SIZE 40 in controls.py); tess-shell: no hook (no state layer in the key table); tre: yes (height) |
| state layer | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]] (half of the layer height) | tess-ui: no hook (STATE_LAYER_SIZE 40 in controls.py); tess-shell: no hook (no state layer in the key table); tre: yes (corner_radius) |
| label | font | `density.font_body` | `body_medium` 14/20/400/0.25 | `body_medium` 14/20/400/0.25 | `body_dense` 13/18/400/0.25 | [[Typography]]; dense: design choice, [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height, and no hook for letter spacing); tre: yes (font_size, font_weight, line_height) |
| label | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | design choice, [[ADR-0002 Desktop density levels and target sizes]] (the gap above separates label and box) | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |

## Layout and overflow

- The box never shrinks, wraps or clips. The label wraps to at most 2 lines, then truncates with an ellipsis; the box stays aligned to the vertical centre of the first line, and the row grows to fit the wrapped label.
- A one-line label is vertically centred in the row height (the space above and below differs by at most 1 px, AC-DEN-9 in [[Spacing and Density]]).
- Inside [[Form Row]]: the label sits in the label column and the box in the control column; a checkbox with its own label occupies the control column only.
- In a [[Tree Node]] or [[List Item]] row the box sits in the leading slot, after the chevron and before the icon, with the row padding of the level.
- The box and its layer paint only inside the state layer circle plus the focus ring; nothing paints outside on press or release.

## Behaviour

- Pointer: press shows the pressed layer; release inside the box or label toggles once and moves focus to the checkbox without a ring; leaving before release cancels. A press on the label toggles like a press on the box.
- Keyboard: Space toggles the focused checkbox ([WAI-ARIA Authoring Practices checkbox](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/): "pressing the Space key changes the state"). Enter also toggles in tess-ui and does nothing in tess-shell; a project states which, and neither is required by this specification. Tab and Shift+Tab move focus in and out; a disabled checkbox takes no focus and no key.
- Parent and children: toggling a child recomputes the parent (all selected: selected; none: unselected; otherwise indeterminate). A press on an indeterminate parent selects all children and sets the parent to selected; a second press clears all. The parent state is derived from the children and is never stored separately.
- Touch: tap on the 48 dp hit area toggles.
- Event: one change event per user toggle, after the state changes, carrying the old and new state; setting the state from code raises no event.

## Tooltip and overlay behaviour

Per [[ADR-0004 Tooltip rule]] the tooltip belongs to the control, never to a row or group.

- A checkbox may carry one tooltip, on the box plus label as one control. Hovering the box shows that tooltip only, never the row's or the group heading's.
- A press dismisses the tooltip and none returns until the pointer leaves, re-enters and 500 ms pass.
- A box-only checkbox in a table has no visible name, so its tooltip names the row action ("Select row 4"); the name is the same text.
- No overlay opens. The tooltip is opaque ([[Tooltip]]).

## Motion

Tesserae values (tess-ui `controls.py`): box fill and outline colour fade `short3` 150 ms; the mark draws on over `medium1` 250 ms with `emphasized_decelerate` and draws off over `short3` 150 ms with `emphasized_accelerate`. Reduced motion: the state changes in one frame, no mark animation ([[14 Accessibility Basics]]). Material Web does not publish checkbox durations in its tokens #needs-verification.

## Accessibility

- Role: `checkbox`; state `checked` true, false or `mixed` ([WAI-ARIA checkbox](https://www.w3.org/TR/wai-aria-1.2/#checkbox), [APG](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/)).
- Name: the visible label; a box-only checkbox takes its name from an explicit association with the row name; a checkbox with no name fails AC-CHK-8.
- Error: the node is exposed as invalid and the supporting text is its description ([[Validation]]).
- Group: checkboxes in a labelled set sit in a node with role `group` and the set label as name.
- Disabled: exposed as disabled; no focus, no key.
- Announcement: the platform announces the state from `checked`; no extra live region.
- Contrast: unselected outline `on_surface_variant` against the surface at least 3 to 1; selected box against the surface and the mark against the box at least 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); label at least 4.5 to 1; error outline likewise.
- Focus ring visible, not clipped.

## Dark and light

All roles; the checkbox follows the scheme ([[Theme Following the System]]). AC-CHK-10 runs in both.

## Defaults

Density from the container; two-state; unselected; label after the box; no error; no tooltip.

## Acceptance criteria

- [ ] AC-CHK-1 (token test): box, state layer, outline, mark stroke and corner equal the table at each level: 18, 40, 2, 2 and 2 dp at default; 16, 32, 2, 2, 2 at compact; 14, 28, 2, 2, 2 at dense. Pass: all values equal.
- [ ] AC-CHK-2 (geometry check): the row height is 40, 32 and 28 dp at the three levels and the gap box to label is 8, 8 and 4 dp (at scale 1.0 and 2.0). Pass: equal to the dp.
- [ ] AC-CHK-3 (geometry check): the hit area of a labelled checkbox is at least 24 by 24 dp at every level, a box-only checkbox at least 24 by 24 dp, and at least 48 by 48 dp in the touch context; two adjacent checkboxes do not overlap hit areas. Pass: measured bounds at or above the limits.
- [ ] AC-CHK-4 (scripted input): focus the checkbox and press Space: `checked` flips once and one change event fires; again: it flips back. On a disabled checkbox Space does nothing and Tab skips it. Pass: state and event counts equal.
- [ ] AC-CHK-5 (scripted input): press and release the pointer on the box toggles once; press on the label toggles once; press on the box, move out, release toggles nothing. Pass: state unchanged in the last case.
- [ ] AC-CHK-6 (scripted input): a parent with three children: select one child, the parent reads `mixed`; select all, `checked` true; clear all, false; press the mixed parent, all three children become selected. Pass: states and event counts equal.
- [ ] AC-CHK-7 (token test): state layer opacity resolves to 0.08 (hover), 0.10 (focus), 0.10 (pressed); layer colours per the States table (unselected hover and focus `on_surface`, unselected pressed `primary`, selected hover and focus `primary`, selected pressed `on_surface`, error `error`); disabled box 0.38, disabled label 0.38. Pass: values equal.
- [ ] AC-CHK-8 (AT tree assertion): the node has role `checkbox`, a non-empty name, `checked` equal to true, false or `mixed` as the state, and `disabled` equal to the state; in error the node has `invalid` true and a non-empty description. Pass: all equal.
- [ ] AC-CHK-9 (pixel check): in each of unselected, selected, indeterminate and error, the box shows a different shape or colour from the others and selected shows the check, indeterminate the dash (mark pixels inside the box, none outside). Pass: shape pixel masks differ between the three states and lie inside the 18 dp box.
- [ ] AC-CHK-10 (contrast script): light and dark, unselected outline against the surface, selected fill against the surface, mark against fill: at least 3 to 1; label against the surface at least 4.5 to 1. Pass: ratios at or above the limits.
- [ ] AC-CHK-11 (scripted input): hover the box 600 ms: exactly its own tooltip is visible (none if it has none) and no row or group tooltip; a press dismisses it. Pass: visible tooltip count and owner equal.
- [ ] AC-CHK-12 (scripted input): with reduced motion on, a toggle shows the final mark in the first frame after the event. Pass: mark fully drawn or fully absent in that frame.
- [ ] AC-CHK-13 (geometry check): a one-line label is vertically centred in the row at every level (offset at most 1 px); a 3-line label wraps to 2 lines with an ellipsis and the box stays centred on the first line (±0.5 dp). Pass: offsets within the limits.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`Checkbox`), `tess-ui:docs/components/checkboxes.md` | partly meets: 18 dp box, 2 dp outline and corner, 40 dp layer in a 48 dp target, check and dash marks, indeterminate through `Checked` null, error colours, disabled 38 percent, label in the press target, Space and Enter toggle, a press on an indeterminate box selects (AC-CHK-4, AC-CHK-5, AC-CHK-6 meet by reading, unrun). Fails AC-CHK-1 and AC-CHK-2 at compact and dense (no density; the 48 dp target is fixed); the pressed layer colour is `primary` when selected where the tokens give `on_surface` (AC-CHK-7); the node sets `checked` to None for indeterminate and no `mixed` (AC-CHK-8: the engine has no mixed value for `checked`, see tre); error sets colours only, no `invalid` and no description (AC-CHK-8); settable: box size, outline, corner and state layer are class constants of `Checkbox` and `STATE_LAYER_SIZE`, with no style or token hook |
| tess-shell | `tess-shell:src/tess_shell/shipped/Checkbox/Checkbox_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | partly meets: 18 dp frame, 2 dp border, mark path, label gap 8 dp, role `CHECKBOX` with `checked`, name from `Label` else `Text`, Space toggles, Enter does not (AC-CHK-4 meets by reading). Fails: row height 22 dp, below the 24 dp target and not 40, 32 or 28 (AC-CHK-2, AC-CHK-3); corner `$shape.small` 4 dp, not 2 dp (AC-CHK-1); no state layer: hover 0.85 and pressed 0.7 opacity and disabled 0.5 literals (AC-CHK-7, status `absent` for State Layers); no indeterminate state ("not in v1", AC-CHK-6); no error state (AC-CHK-8, AC-CHK-9); no focus-ring spec match (see [[Focus Ring]]); settable: the state layer has no hook (absent) |
| tre | `tre:docs/reference/node.md` (`role="checkbox"`, `checked`) | not applicable: the engine has the role and `checked` as bool or none; no `mixed` value (the `pressed` property takes `"mixed"` for toggle buttons only); candidate request: `checked="mixed"` |

Evidence: tess-ui `Checkbox._tint` and `_paint`; the tess-shell Checkbox module header comment ("A mixed state is not in v1"); `shell-vault:50 Design System/Standard Modules.md` (Checkbox).

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Row height 40, 32, 28 dp; state layer 32 dp at compact and 28 dp at dense; box 16 dp at compact and 14 dp at dense | desktop rows; the layer must not exceed the row | [[ADR-0002 Desktop density levels and target sizes]], [[ADR-0029 Desktop density and type scale]] |
| Pointer target 24 dp minimum; 48 dp only in touch contexts | WCAG 2.2 SC 2.5.8; desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp, role `secondary` | foundation rule for all controls | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Space toggles; Enter optional | follows the WAI-ARIA Authoring Practices | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Error also exposes `invalid` and supporting text | MD3 shows error by colour; WCAG 1.4.1 and 3.3.1 need more | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule only) |

## Sources

- [Material Web checkbox tokens, latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-checkbox.scss): container size 18 px, icon size 18 px, state layer 40 px, container shape 2 px, unselected outline 2 px, selected outline 0 px, disabled container opacity 0.38, colours `primary`, `on_primary`, `on_surface`, `on_surface_variant`, `error`, `on_error`, `surface`, pressed layer colours (verified 2026-11-21). The v0_192 set carries the same sizes ([v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-checkbox.scss)).
- [Material Web checkbox internals](https://github.com/material-components/material-web/blob/main/checkbox/internal/_checkbox.scss): 48 by 48 dp touch target.
- [Material Components Android Checkbox](https://github.com/material-components/material-components-android/blob/master/docs/components/Checkbox.md): selected, unselected, indeterminate, error, parent and children behaviour, minimum size.
- [WAI-ARIA Authoring Practices checkbox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/): Space toggles, `aria-checked` true, false or mixed, group labelling (verified 2026-11-21).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.5.8, 3.3.1.
- The m3.material.io checkbox page could not be fetched (script-rendered site); values above come from the token repository.
- Code: `tess-ui:src/tess_ui/controls.py`, `tess-ui:docs/components/checkboxes.md`, `tess-shell:src/tess_shell/shipped/Checkbox/Checkbox_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl`, `shell-vault:50 Design System/Standard Modules.md`, `tre:docs/reference/node.md`.
