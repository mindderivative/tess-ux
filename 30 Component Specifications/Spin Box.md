---
title: Spin Box
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, input, number]
related: ["[[Text Field]]", "[[Icon Button]]", "[[Form Row]]", "[[Switch]]", "[[Tooltip]]", "[[Validation]]", "[[Forms and Settings]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Text Field]]", "[[Icon Button]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Spin Box

> [!info] Summary
> A number field flanked by a decrease and an increase button that steps the value by a fixed amount within a range. Material Design 3 (MD3) has no spin box; Tesserae builds it from an outlined [[Text Field]] and two [[Icon Button]] parts. Source of truth in code: see the last section.

## Purpose

The user sets a bounded number (a count, a size in px, a delay in ms, a percentage) by typing it or by stepping it with buttons, arrow keys or a wheel-less keyboard. The control refuses values outside the range and shows the number in one fixed format. The settings app uses numeric keys with a range and unit constantly (`tess-ui:apps/shell_config/src/tess_shell_config/widgets.py`, `NumberWidget`: minimum, maximum, step, unit).

## When to use and not

- Use when: the value is a number with a known range and a natural step, and the user often adjusts it by small amounts.
- Do not use when: the range is large and only a rough value matters (use a slider; specified later), the value is one of a few named options (use a [[Menu]]), the value is a free-form identifier or a code that merely looks numeric (use a [[Text Field]]), or the value is a clock time (use [[Time Input]]).
- A spin box with a visible label above it and supporting or error text under it is the labelled form; a label in a settings row belongs to [[Form Row]].

## Anatomy

1. Decrease button: icon `remove`, an [[Icon Button]] part.
2. Number field: an outlined field holding the value text, caret and selection.
3. Prefix text (optional): a currency sign, shown with the number.
4. Suffix text (optional): a unit.
5. Increase button: icon `add`.
6. Label (optional, above the field; names the control for assistive technology).
7. Supporting or error text (optional, under the control).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Horizontal (buttons at both ends) | default | decrease, field, increase in one row |
| Labelled field (`SpinBoxField`) | forms and dialogs | adds the label above and the supporting or error line under |
| Wrapping | cyclic values (hours, angles) | a step past one bound lands on the other; the buttons never disable; needs both bounds |
| Vertical (buttons stacked at the field end) | very narrow cells such as table cells | not built in tess-ui (`tess-ui:docs/components/spin-boxes.md`); specified here so a project can build it: increase above decrease, each half the control height, same behaviour |

## States

State layers and focus come from [[State Layers]] and [[Focus Ring]]. Buttons take the states of [[Icon Button]]; the field takes the states of the outlined [[Text Field]].

| State | Visual change | Token values |
|---|---|---|
| Rest | field outline 1 dp `outline`, value `on_surface`, button icons `on_surface_variant` | as [[Text Field]] outlined, [[Icon Button]] standard |
| Hover (button) | state layer `on_surface_variant` at 8 percent | [[State Layers]] |
| Hover (field) | outline `on_surface` | as [[Text Field]] |
| Focus (field) | outline 2 dp `primary`, caret `primary` | as [[Text Field]] |
| Focus (button, keyboard) | 10 percent layer plus focus ring 3 dp `secondary` offset 2 dp | [[ADR-0013 Focus and pressed state layer 10 percent]], [[Focus Ring]] |
| Pressed (button) | 10 percent layer; while held the step repeats | [[State Layers]] |
| Button at a bound | the button is disabled: icon `on_surface` at 38 percent, no layer, not focusable by pointer; keyboard focus on a button that disables moves to the field | [[State Layers]] |
| Error | field outline `error`, supporting text `error`; the buttons keep their rest look | as [[Text Field]] |
| Disabled | whole control: icons, value and outline `on_surface` at 38 percent, outline 12 percent; no focus, no input | as [[Text Field]] |
| Read-only | value selectable and copyable, buttons disabled, arrow keys inert | design choice, review |

## Tokens used

- Colour: roles as in the State table ([[Colour Roles]]); no literal colour.
- Type: value `body_large` at default density, `body_medium` at compact and dense; label `label_medium`; supporting text `body_small` ([[Typography]]).
- Shape: field corners 4 dp (`corner-extra-small`); buttons per [[Icon Button]] ([[Shape]]). The tess-ui field corner is 8 dp (`tess-ui:src/tess_ui/controls.py`, `SpinBox.__init__`); see Status in code.
- Spacing and density: [[Spacing and Density]].

## Sizing and density

The control is as high as a single-line text field and the buttons are icon button containers, so the three parts align ([[ADR-0002 Desktop density levels and target sizes]]).

| Level | Control height | Button container | Button icon | Field width (minimum) | Field horizontal padding | Gap between parts | Value type |
|---|---|---|---|---|---|---|---|
| default | 40 dp | 40 dp | 24 dp | 64 dp | 12 dp | 4 dp | `body_large` |
| compact | 32 dp | 32 dp | 20 dp | 56 dp | 8 dp | 4 dp | `body_medium` |
| dense | 28 dp | 28 dp | 20 dp | 56 dp | 8 dp | 2 dp | `body_medium` |

- The tess-ui default field is 64 by 40 px and the buttons 40 px (`tess-ui:src/tess_ui/controls.py`: `BUTTON = 40.0`, `FIELD = (64.0, 40.0)`); the compact and dense field widths of 56 dp are Tesserae design choices #needs-verification-as-design-choice. The field grows with its content up to the parent; the minimum fits the longest value at the range limits (digits, sign, decimal separator, prefix, suffix) without ellipsis, and a project sets the width from that.
- Hit area: every part at least 24 by 24 dp (met at all densities); 48 by 48 dp in a touch context ([[Spacing and Density]]).
- The value is centred vertically by construction, as in [[Text Field]] (AC-DEN-9).

## Layout and overflow

- Value text is one line, never wraps. Numbers align to the end of the field by default so that digits line up in a column of spin boxes (a numeric field may align end, [[Text Field]]); prefix and suffix stay beside the number.
- A value that does not fit its field is a defect: the field width is chosen from the range (see Sizing). If it still overflows, the focused field scrolls the caret into view and the unfocused field truncates with an ellipsis at the end ([[10 Layout Overflow and Scrolling]]).
- The control never grows past its parent; the field has `min-width: 0` so it shrinks before the buttons do.
- The control sits in a flex row without `flex: fill` on the field unless the form asks for equal widths ([[Form Row]]).

## Behaviour

- Pointer: a click on a button steps once; a hold steps again after 400 ms and then every 80 ms until release or until a bound is reached; the click that ends a hold does not step again (`tess-ui:src/tess_ui/controls.py`, `HOLD`, `REPEAT`). The accelerating hold (the longer it is held, the larger the repeat rate) is not built; the spec asks for the repeat interval to fall from 80 ms to 40 ms after 2 s of hold and to 20 ms after 5 s, a design choice #needs-verification-as-design-choice. A press in the field places the caret; the field behaves as a [[Text Field]].
- Keyboard (focus in the field):

| Keys | Result |
|---|---|
| Up, Down | increase, decrease by `Step` |
| Page Up, Page Down | increase, decrease by 10 steps |
| Home, End | set the minimum, the maximum (only when the bound exists) |
| Shift+Up, Shift+Down | no assigned action (the key goes to the enclosing container) |
| Digits, sign, decimal separator, prefix, suffix characters | edit the text; the value changes only when the text parses and lies inside the range |
| Enter | commit the typed text; an invalid text keeps the previous value and shows the error |
| Escape | revert the typed text to the last committed value; if the field text is unchanged the key goes to the enclosing dialog |
| Tab, Shift+Tab | the field is the one tab stop; the step buttons are not in the Tab order and are reached by pointer and by assistive technology actions |

- Rationale for one tab stop: the arrow keys in the field already step, so two more tab stops per number would cost the keyboard user two keystrokes per field in a long form (see [[Forms and Settings]]). A project that wants the buttons focusable sets the buttons to focusable and records it.
- A typed number is accepted once it parses and fits the range; leaving the field puts back the value's formatted text if the typed text did not commit (`tess-ui:docs/components/spin-boxes.md`).
- Decimals: `Decimals` fixes the places shown; without it only as many as the number needs. Stepping a decimal value rounds to the step's precision so that 0.1 + 0.2 shows 0.3, not 0.30000000000000004.
- Wrap: with `Wrap` and both bounds, a step past one bound lands on the other and the buttons never disable.
- Touch: tap on a button steps; a touch hold repeats as the pointer hold; the platform number keyboard opens when the platform has one (`input_mode: numeric` or `decimal`, kept for a keyboard that can adapt, `tre:docs/guide/text.md`).
- IME: the field accepts only digits and the allowed characters; composition text that is not numeric is shown while composing and removed on commit if it does not parse. Full-width digits commit as the ASCII digits #needs-verification-as-design-choice. The candidate window follows the caret ([[Text Field]]).
- Validation hooks: the control reports a refused value (out of range, not a number) as `Error` text; the pattern for when and how errors are shown is in [[Validation]] and the row layout in [[Forms and Settings]]. The control itself never shows an error before the user has committed (Enter, blur or a button) once.

## Tooltip and overlay behaviour

The control opens no overlay. The tooltip belongs to the control that carries the label ([[ADR-0004 Tooltip rule]]): the two step buttons have the tooltips "Decrease" and "Increase" (their accessible names), hover delay as [[Tooltip]]; the field container has none. When the range is not visible, the supporting text states it ("from 0 to 50 kg").

## Motion

None beyond the button and field state transitions of [[Icon Button]] and [[Text Field]] (at most 150 ms). Reduced motion: no ripple, steady caret ([[14 Accessibility Basics]]).

## Accessibility

- Role of the field: `spinbutton` ([WAI-ARIA spinbutton](https://www.w3.org/TR/wai-aria-1.2/#spinbutton)) with the numeric value, minimum, maximum and the text value (the formatted string with prefix and suffix) exposed; the AT `increment` and `decrement` actions step the value. The buttons are `button` nodes named "Decrease" and "Increase" and are hidden from the Tab order, not from the accessibility tree.
- tess-ui gives the field `role="textbox"` with `increment` and `decrement` actions (`tess-ui:src/tess_ui/controls.py`); the spec role is `spinbutton`, see Status in code.
- Name: the visible label; without one the `Label` property; the shell warns when neither exists.
- Description: supporting or error text; `invalid` while an error is shown; the error is a polite live region ([[Text Field]]).
- Keys: the table above, consistent with the [APG spin button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/) (Up, Down, Home, End, Page Up, Page Down).
- Contrast: value text 4.5 to 1 on the container; outline and icons 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)).
- A disabled button at a bound is announced as unavailable; the field announces the new value after each step (the platform announces value changes of a spinbutton).
- See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Dark and light

All colours are roles; the control follows the system theme ([[Theme Following the System]]); the contrast criterion runs in both schemes.

## Defaults

- Step 1, no bounds, no decimals, no wrap, no prefix or suffix.
- Density from the container; the config tool uses `compact` (32 dp).
- Hold repeat: 400 ms delay, 80 ms interval; Page Up and Page Down step 10.
- Outlined field, aligned to the end.

## Acceptance criteria

- [ ] AC-SPN-1 (token test): the control height, button container and button icon equal 40/32/28 dp, 40/32/28 dp and 24/20/20 dp at default, compact, dense; field horizontal padding equals 12/8/8 dp. Pass: values equal.
- [ ] AC-SPN-2 (geometry check): the decrease button, field and increase button have the same height and their vertical centres coincide within 0.5 dp, at scale 1.0, 1.25 and 2.0; the value's line box is centred in the field with space above and below differing by at most 1 px (AC-DEN-9). Pass: within tolerance.
- [ ] AC-SPN-3 (geometry check): every part has a hit area of at least 24 by 24 dp (48 by 48 dp in a touch context) and the hit areas of the three parts do not overlap. Pass: sizes at or above the limits, zero overlap area.
- [ ] AC-SPN-4 (scripted input): with min 0, max 10, step 1, value 5, focus the field and press Up three times, Down once: value 7. Page Up from 7 yields 10 (clamped), Home yields 0, End yields 10. Pass: value after each key equals the expected.
- [ ] AC-SPN-5 (scripted input): type "42" into a field with max 10 and press Enter: the value stays at its previous value, the field shows the previous formatted text or the error text, and `invalid` is true. Type "7" and press Enter: value 7, no error. Pass: values and flag equal.
- [ ] AC-SPN-6 (scripted input): at value 10 with max 10 and no wrap, the increase button is disabled and Up leaves the value 10; with wrap, Up gives the minimum and no button is disabled. Pass: value and disabled flags equal.
- [ ] AC-SPN-7 (scripted input): press and hold the increase button on a mocked clock: one step at 0 ms, the next at 400 ms (±20 ms), then one every 80 ms (±10 ms); release stops the stream, and the click that ends a hold adds no step. Pass: step timestamps within tolerance.
- [ ] AC-SPN-8 (scripted input): with decimals 1 and step 0.1, ten Up presses from 0 show 1.0 and the value equals 1.0 within 1e-9. Pass: shown text and value equal.
- [ ] AC-SPN-9 (scripted input): with prefix "$" and suffix " kg", the field shows "$12.5 kg"; typing "12.5", "$12.5" and "12.5 kg" each commit 12.5. Pass: value 12.5 in all three.
- [ ] AC-SPN-10 (AT tree assertion): the field node has role `spinbutton`, a non-empty name equal to the label, numeric value, minimum, maximum and the text value; the `increment` and `decrement` actions change the value by the step; the buttons have role `button` and the names "Decrease" and "Increase". Pass: all properties equal.
- [ ] AC-SPN-11 (scripted input): the Tab order from the previous control goes to the field and then to the next control; the two step buttons take no Tab stop (unless the project sets them focusable). Pass: focus sequence equals field, next control.
- [ ] AC-SPN-12 (contrast script): in light and dark, value on container 4.5 to 1 or more, outline and button icons against the surface 3 to 1 or more, the error text 4.5 to 1. Pass: ratios at or above the limits.
- [ ] AC-SPN-13 (token test): no literal colour in the control's stylesheet; the disabled state uses `on_surface` at 38 percent (content) and 12 percent (outline). Pass: every colour is a role reference.
- [ ] AC-SPN-14 (geometry check): the field is wide enough to show the longest value at the range limits, with prefix and suffix, without ellipsis, at each density. Pass: text width at most content width.
- [ ] AC-SPN-15 (geometry check): hover over the field container for 600 ms shows no tooltip; hover over a button for 600 ms shows a tooltip equal to its name ([[ADR-0004 Tooltip rule]]). Pass: zero tooltips on the container, one on each button.
- [ ] AC-SPN-16 (scripted input): a value of 0.1 + 0.2 reached by stepping shows "0.3" with decimals 1 and the stored value is within 1e-9 of 0.3. Pass: equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`SpinBox`), `tess-ui:src/tess_ui/views/SpinBoxField_View.tdl`, `tess-ui:src/tess_ui/views/SpinBoxField_Stylesheet.tdl` | partly meets: step, bounds, wrap, decimals, prefix, suffix, hold 400 and 80 ms, Page Up and Page Down by ten, AT increment and decrement exist (AC-SPN-4 to AC-SPN-9 meet as documented, unmeasured); fixed 40 px buttons, 64 by 40 px field and 14 px type, no density setting (AC-SPN-1 fails at compact and dense); field role is `textbox` not `spinbutton` (AC-SPN-10 fails); field corner 8 dp instead of 4 dp (AC-SPN-13 token test ok, shape differs); no accelerating hold and no vertical arrangement; Home and End not documented (AC-SPN-4 partial); buttons Tab behaviour not documented (AC-SPN-11 unmeasured); tooltips on the buttons not documented (AC-SPN-15 unmeasured) |
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`NumberWidget`) | partly meets: numeric keys with range, step and unit are refused with the range text; not built on `SpinBox` in the shipped views found; AC-SPN-5 meets in behaviour |
| tess-shell | none | absent: no spin box block or module (shipped modules: `Slider`, `TextInput`, no number input) |
| tre | engine `text_input` with `input_mode` `numeric` or `decimal` (`tre:docs/guide/text.md`) | not applicable (primitive): no spin box node; `input_mode` is kept for a keyboard that can adapt |

Evidence: `tess-ui:docs/components/spin-boxes.md`.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py`, `tess-ui:src/tess_ui/views/SpinBoxField_View.tdl`, `tess-ui:docs/components/spin-boxes.md` | exists, partial |
| tess-shell | none | absent |
| tre | `tre:docs/guide/text.md` | primitive only |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no spin box | desktop settings need stepped numbers | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights 40, 32, 28 dp (MD3 text field 56 dp, icon button 40 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| The step buttons are outside the Tab order, the field is one tab stop | keyboard-first forms: Up and Down already step | [[ADR-0002 Desktop density levels and target sizes]] (target sizes only; the tab-stop rule is a Tesserae convention) |
| Role `spinbutton` instead of a plain textbox | MD3 has no spin box; WAI-ARIA defines it | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- tess-ui spin box documentation: `tess-ui:docs/components/spin-boxes.md`.
- [WAI-ARIA APG spin button pattern](https://www.w3.org/WAI/ARIA/apg/patterns/spinbutton/): role, Up, Down, Home, End, Page Up, Page Down.
- [WAI-ARIA 1.2 spinbutton](https://www.w3.org/TR/wai-aria-1.2/#spinbutton): value, min, max.
- [Material Web outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss): outline widths, disabled opacities.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.11, 2.5.8.
- MD3 has no spin box: checked against the [Material Web components list](https://github.com/material-components/material-web/tree/main/docs/components) (no spin box or stepper). The accelerating-hold rates and the 56 dp field width at compact are Tesserae choices marked above.
