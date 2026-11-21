---
title: Radio Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, selection, input]
related: ["[[Checkbox]]", "[[Switch]]", "[[Segmented Button]]", "[[Form Row]]", "[[List Item]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Validation]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Colour Roles]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Checkbox]]"]
---

# Radio Button

> [!info] Summary
> One option of a group in which exactly one option is chosen: the Material Design 3 [radio button](https://m3.material.io/components/radio-button/overview), with the three density levels, a group keyboard model from the WAI-ARIA Authoring Practices and an error state that MD3 does not define. Source of truth in code: see Status in code.

## Purpose

Choose exactly one of a small set of mutually exclusive options that the user needs to see side by side (theme: light, dark, system; sort order). The checked option is always visible; the group is a single decision.

## When to use and not

- Use when: two to about seven options; all options deserve to be seen; one must be chosen; the choice applies on Save or at once, as the form says.
- Do not use when: several options may be chosen (use [[Checkbox]]); the choice is on or off ([[Switch]]); there are many options (use a dropdown or [[List]]); the options act as buttons in a bar (use [[Segmented Button]]).

## Anatomy

1. Group: a node with role `radiogroup` and a name (the question), holding two or more radio buttons.
2. Ring: a 20 dp circle, 2 dp wide.
3. Dot: a 10 dp circle at the centre of the ring, present when chosen.
4. State layer: a circle of 40 dp, drawn on hover, focus and press per [[State Layers]].
5. Label: text beside the ring; part of the press target.
6. Focus ring: around the state layer, keyboard focus only ([[Focus Ring]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Labelled | default | label after the ring (before it in right-to-left locales) |
| Ring only | in a table or list row | no label; the row name names the radio |
| Vertical group | default for 3 or more options | one option per row |
| Horizontal group | two or three short options | options in one row, gap `space.5` (16 dp) |

## States

State layer percentages come from [[State Layers]] ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). Colours are those of the Material Web radio tokens ([latest `_md-comp-radio-button.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-radio-button.scss)):

| State | Ring | Dot | State layer (colour, opacity) |
|---|---|---|---|
| Unchosen, rest | `on_surface_variant` | none | none |
| Unchosen, hover and focus | `on_surface` | none | `on_surface`, 8 and 10 percent |
| Unchosen, pressed | `on_surface` | none | `primary`, 10 percent |
| Chosen, rest | `primary` | `primary` | none |
| Chosen, hover and focus | `primary` | `primary` | `primary`, 8 and 10 percent |
| Chosen, pressed | `primary` | `primary` | `on_surface`, 10 percent |
| Error (Tesserae, see Deviations) | `error` | `error` | `error`, 8, 10, 10 percent |
| Disabled, unchosen | `on_surface` at 38 percent | none | none |
| Disabled, chosen | `on_surface` at 38 percent | `on_surface` at 38 percent | none |
| Keyboard focus | as the state | as the state | focus ring 3 dp, offset 2 dp, role `secondary` |

The label is `on_surface`; disabled `on_surface` at 38 percent. Chosen shows a dot, not only a colour ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).

## Tokens used

[[Colour Roles]] (roles above), [[Shape]] (`corner-full`), [[Motion]], [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

MD3 values (Material Web tokens): icon 20 dp, state layer 40 dp; in the component the outer circle has radius 10 dp with a 2 dp ring and the inner circle radius 5 dp ([`radio/internal/radio.ts`](https://github.com/material-components/material-web/blob/main/radio/internal/radio.ts): `r="10"`, mask `r="8"`, inner `r="5"`); touch target 48 by 48 dp ([`radio/internal/_radio.scss`](https://github.com/material-components/material-web/blob/main/radio/internal/_radio.scss)).

Rule: the row height is the control height of the level; the state layer equals the row height; the ring is 20 dp at default and compact and 18 dp at dense, with the dot half the ring; the gap to the label is `density.icon_label_gap`.

| Level | Row height | Ring | Dot | State layer | Gap ring to label | Row gap in a vertical group |
|---|---|---|---|---|---|---|
| default | 40 dp | 20 dp | 10 dp | 40 dp | 8 dp | 0 dp (rows touch) |
| compact | 32 dp | 20 dp | 10 dp | 32 dp | 8 dp | 0 dp |
| dense | 28 dp | 18 dp | 9 dp | 28 dp | 4 dp | 0 dp |

The compact and dense rows are Tesserae design choices #needs-verification-as-design-choice.

- Pointer target: ring plus label, at least 24 by 24 dp ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)); a ring-only radio has a square target equal to the state layer. In a touch context 48 by 48 dp.
- Adjacent radios in a vertical group have adjoining but not overlapping hit areas (row height at least 28 dp).

## Dimensions and defaults

Ring and dot come from the Material Web radio tokens and component internals; row heights, state layer sizes and the compact and dense ring follow [[ADR-0002 Desktop density levels and target sizes]] (#needs-verification-as-design-choice for every compact and dense value and for the label font, which the tokens do not set).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| row | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| row | min width | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| row | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| row | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | design choice, [[ADR-0002 Desktop density levels and target sizes]] (the state layer supplies the space around the ring) | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| row | margin | - | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| row | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| row | border width | - | 0 | 0 | 0 | [[Spacing and Density]], the row draws no border; the ring has its own | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| row | border color | - | N/A: the row draws no border | N/A: the row draws no border | N/A: the row draws no border | [[Spacing and Density]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| row | corner radius | - | N/A: the row draws no container | N/A: the row draws no container | N/A: the row draws no container | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| row | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| group | gap | `space.0` | 0 | 0 | 0 | [[Radio Button]], Sizing and density (rows touch); a horizontal group uses `space.5` (16) | tess-ui: via parent container gap (RadioGroup is a Python helper with no node); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| ring | height | - | 20 | 20 | 18 | [md-comp-radio-button](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-radio-button.scss) (icon size 20); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: no hook (RadioButton.SIZE); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| ring | border width | - | 2 | 2 | 2 | [radio.ts](https://github.com/material-components/material-web/blob/main/radio/internal/radio.ts) | tess-ui: no hook (ring stroke width literal in RadioButton._build); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| ring | border color | `on_surface_variant` | `on_surface_variant` | `on_surface_variant` | `on_surface_variant` | [md-comp-radio-button](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-radio-button.scss) (unchosen rest; `primary` when chosen) | tess-ui: via widget option color (chosen colour) and theme roles on_surface_variant and error; tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| ring | corner radius | `shape.full` | 10 | 10 | 9 | [[Shape]] (half of the ring) | tess-ui: no hook (half of RadioButton.SIZE); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| ring | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: no hook (ring is a Python-drawn node with no elevation option); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| dot | height | - | 10 | 10 | 9 | [radio.ts](https://github.com/material-components/material-web/blob/main/radio/internal/radio.ts) (inner radius 5); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: no hook (RadioButton.DOT); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| dot | icon size | - | 10 | 10 | 9 | [[Radio Button]], Sizing and density (half the ring) | tess-ui: no hook (RadioButton.DOT); tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| state layer | height | `density.control_height` | 40 | 32 | 28 | [md-comp-radio-button](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-radio-button.scss); compact and dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: no hook (STATE_LAYER_SIZE 40 in controls.py); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| state layer | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]] (half of the layer height) | tess-ui: no hook (STATE_LAYER_SIZE 40 in controls.py); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| label | font | `body_medium` | 14/20/400/0.25 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]]; design choice, proposed ADR: control label type role | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |

## Layout and overflow

- The ring never shrinks or clips. The label wraps to at most 2 lines, then truncates with an ellipsis; the ring stays centred on the first line.
- A group lays out vertically by default; a horizontal group wraps to a new row when the width runs out and never scrolls sideways.
- In a [[Form Row]] the group label sits in the label column and the radios in the control column.
- Nothing paints outside the state layer circle plus the focus ring on press or release.

## Behaviour

- Pointer: press shows the pressed layer; release inside the ring or label chooses the option; a press on a chosen option does nothing (a radio never unchooses itself); leaving before release cancels. Choosing an option unchooses the previous one in the same group.
- Keyboard (APG [radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/), roving focus):
  - Tab and Shift+Tab move focus into and out of the group. The group is one Tab stop. Focus lands on the chosen radio; when none is chosen, on the first enabled radio.
  - Space chooses the focused radio when it is not chosen.
  - Right Arrow and Down Arrow move focus to the next enabled radio, choose it and unchoose the previous one; from the last enabled radio focus wraps to the first.
  - Left Arrow and Up Arrow do the same backwards; from the first it wraps to the last.
  - Disabled radios are skipped; a group with one enabled radio ignores the arrows.
  - In a right-to-left locale Left Arrow moves to the next radio and Right Arrow to the previous #needs-verification (APG does not state it).
- Touch: tap on the 48 dp hit area chooses.
- Initial state: a group may start with no radio chosen (a form that forces a choice); it never returns to no choice by user action.
- Event: one change event on the radio that becomes chosen, after the state changes; arrow movement raises it too, because arrows choose; setting the choice from code raises no event.

## Tooltip and overlay behaviour

Per [[ADR-0004 Tooltip rule]] the tooltip belongs to the control.

- A radio (ring and label as one control) may carry one tooltip; the group and the row carry their own, and hovering a radio shows only its tooltip.
- A press dismisses the tooltip; none returns until the pointer leaves, re-enters and 500 ms pass.
- Keyboard focus moving by arrow shows the tooltip of the newly focused radio at once ([[Tooltip]]).
- No overlay opens.

## Motion

Tesserae values (tess-ui `controls.py`): ring colour fade `short3` 150 ms; the dot grows from scale 0 to 1 over `medium1` 250 ms with `emphasized_decelerate` and shrinks over `short3` with `emphasized_accelerate`. Material Web grows the dot over 300 ms with `emphasized_decelerate` and fades the ring colour in 50 ms (`radio/internal/_radio.scss`); Tesserae keeps its durations from [[Motion]]. Reduced motion: the dot appears in one frame ([[14 Accessibility Basics]]).

## Accessibility

- Group: role `radiogroup` with a name from the question label ([APG radio](https://www.w3.org/WAI/ARIA/apg/patterns/radio/)); radios are `radio` with `checked`.
- Name: the visible label; a ring-only radio gets its name from its row.
- Error: the group, not a single radio, carries invalid and the description ([[Validation]]).
- Disabled: exposed as disabled; no focus, no key.
- Announcement: the platform announces "radio button, 2 of 3, checked" from the role, set position and `checked`; the engine must expose the set size and position (see Status in code).
- Contrast: unchosen ring `on_surface_variant`, chosen ring and dot `primary`, each against the surface at least 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); label at least 4.5 to 1.
- Focus ring visible and not clipped.

## Dark and light

All roles; follows the scheme ([[Theme Following the System]]). AC-RAD-9 runs in both.

## Defaults

Density from the container; vertical group; labelled; first enabled radio in the Tab order when none is chosen; nothing chosen unless the form sets a value.

## Acceptance criteria

- [ ] AC-RAD-1 (token test): ring, dot and state layer equal the table at each level (20, 10, 40 dp at default; 20, 10, 32 at compact; 18, 9, 28 at dense), ring width 2 dp. Pass: all values equal.
- [ ] AC-RAD-2 (geometry check): row height 40, 32 and 28 dp and gap to label 8, 8 and 4 dp at the three levels (scale 1.0 and 2.0). Pass: equal to the dp.
- [ ] AC-RAD-3 (geometry check): hit area at least 24 by 24 dp at every level and at least 48 by 48 dp in the touch context; hit areas of two adjacent radios do not overlap. Pass: measured bounds at or above the limits.
- [ ] AC-RAD-4 (scripted input): in a group of three with the second chosen, Tab lands on the second; with none chosen Tab lands on the first enabled; the group has exactly one Tab stop (a second Tab leaves the group). Pass: the focused node equals the expected radio each time.
- [ ] AC-RAD-5 (scripted input): Down and Right choose and focus the next enabled radio, Up and Left the previous, with wrap at both ends, skipping a disabled radio; exactly one radio is chosen after each key and one change event fires per key. Pass: chosen radio, focused radio and event counts equal.
- [ ] AC-RAD-6 (scripted input): Space on an unchosen focused radio chooses it; Space on the chosen radio changes nothing and fires no event; a pointer press on a chosen radio changes nothing. Pass: state and event counts equal.
- [ ] AC-RAD-7 (AT tree assertion): the group node has role `radiogroup` and a non-empty name; each radio has role `radio`, a non-empty name, `checked` equal to the state, `disabled` equal to the state and position in set and set size. Pass: all equal.
- [ ] AC-RAD-8 (token test): state layer opacities 0.08, 0.10, 0.10; layer colours per the States table; disabled ring, dot and label 0.38. Pass: values equal.
- [ ] AC-RAD-9 (contrast script): light and dark, unchosen ring, chosen ring and dot, error ring against the surface at least 3 to 1; label at least 4.5 to 1. Pass: ratios at or above the limits.
- [ ] AC-RAD-10 (pixel check): chosen and unchosen differ by the dot (a filled circle of 10 dp, 9 dp at dense, centred within 0.5 dp in the ring); no painted pixel lies outside the 40 dp layer circle plus the ring. Pass: dot diameter and centre within tolerance, zero stray pixels.
- [ ] AC-RAD-11 (scripted input): hover a radio 600 ms: exactly its own tooltip (if any) is visible and no group or row tooltip; a press dismisses it. Pass: visible tooltip count and owner equal.
- [ ] AC-RAD-12 (scripted input): with reduced motion on, choosing shows the final dot in the first frame after the event. Pass: dot at scale 1.0 in that frame.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`RadioButton`, `RadioGroup`), `tess-ui:docs/components/radio-buttons.md` | partly meets: 20 dp ring 2 dp wide, 10 dp dot, 40 dp layer in a 48 dp target, group exclusion, one Tab stop (the chosen, else the first enabled), arrows move choice and focus with wrap and skip disabled, a press on a chosen radio does nothing, label in the target, error colours (AC-RAD-4, AC-RAD-5, AC-RAD-6 meet by reading, unrun). Fails AC-RAD-1 and AC-RAD-2 at compact and dense (no density); the layer colour is `primary` for chosen in every state where the tokens give `on_surface` when pressed (AC-RAD-8); the `RadioGroup` is a Python helper with no node, and TDL radios that share `Group:` have no `radiogroup` node, no group name and no set position (AC-RAD-7); settable: ring, dot and state layer sizes are class constants of `RadioButton` and `STATE_LAYER_SIZE`, with no style or token hook |
| tess-shell | none (`RADIO` is in the focus role list `tess-shell:src/tess_shell/binder/focus.py`; no shipped Radio module) | absent |
| tre | `tre:docs/reference/node.md` (`role="radio"`, `checked`) | not applicable: the engine has the `radio` role; no `radiogroup` role and no set position or set size property; candidate requests: role `radiogroup`, `pos_in_set` and `set_size` |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Row height 40, 32, 28 dp; ring 18 dp at dense; layer 32 and 28 dp | desktop rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Error state in `error` colours | the Material Web radio tokens define none; forms need group validation ([[Validation]]); only the group is exposed as invalid | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule) |
| Focus and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Group keyboard model of the APG (arrows choose, wrap) | MD3 gives no keyboard rules; APG is the reference | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |

## Sources

- [Material Web radio tokens, latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-radio-button.scss): icon size 20 px, state layer 40 px, colours `primary`, `on_surface`, `on_surface_variant`, disabled opacity 0.38, pressed layer colours (verified 2026-11-21).
- [Material Web radio internals](https://github.com/material-components/material-web/blob/main/radio/internal/radio.ts) and [`_radio.scss`](https://github.com/material-components/material-web/blob/main/radio/internal/_radio.scss): circle radii 10, 8 and 5, 48 dp touch target, dot grow 300 ms.
- [Material Components Android RadioButton](https://github.com/material-components/material-components-android/blob/master/docs/components/RadioButton.md): minimum size `minTouchTargetSize`.
- [WAI-ARIA Authoring Practices radio group pattern](https://www.w3.org/WAI/ARIA/apg/patterns/radio/): Tab, Space, arrows with wrap, roving focus (verified 2026-11-21).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.5.8.
- The m3.material.io radio page could not be fetched (script-rendered site).
- Code: `tess-ui:src/tess_ui/controls.py`, `tess-ui:docs/components/radio-buttons.md`, `tess-shell:src/tess_shell/binder/focus.py`, `tre:docs/reference/node.md`.
