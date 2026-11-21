---
title: Time Input
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, input, time]
related: ["[[Time Picker]]", "[[Text Field]]", "[[Spin Box]]", "[[Segmented Button]]", "[[Dialog]]", "[[Form Row]]", "[[Validation]]", "[[Forms and Settings]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Text Field]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Time Input

> [!info] Summary
> The keyboard form of a time picker: an hour field, a colon, a minute field and, in 12-hour time, an AM or PM selector. Material Design 3 (MD3) counterpart: the [time picker](https://m3.material.io/components/time-pickers/overview) in input mode. Source of truth in code: see the last section.

## Purpose

The user enters a time of day by typing two numbers. The control keeps hour and minute separately valid and writes a time only when both parts are in range. The dial of the [[Time Picker]] is a separate element; this note specifies the typed form, which is the one a keyboard-first desktop uses.

## When to use and not

- Use when: the user types a time of day (alarm, schedule, a timeout written as a clock time).
- Do not use when: the value is a duration or a count of seconds (use [[Spin Box]] with a unit), the user picks from a dial or list on a touch device (use [[Time Picker]]), or the value is a date (a date input is specified later).
- Inside a settings row the label belongs to [[Form Row]]; the Time Input specifies the control only.

## Anatomy

1. Hour field: a two-digit [[Text Field]] (outlined).
2. Separator: a colon between the fields.
3. Minute field: a two-digit [[Text Field]] (outlined).
4. Period selector (12-hour time only): two-segment choice AM, PM ([[Segmented Button]] pattern; tess-ui draws it as a `PeriodSelector`).
5. Field labels "Hour" and "Minute": accessible names; visible in the picker variant (MD3 shows them under the fields), hidden in the inline variant.
6. Supporting or error text (optional) under the control.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Picker (MD3 input mode) | inside the [[Time Picker]] dialog | numerals in `display_medium` (45 on 52 dp), fields 96 dp wide and 72 dp high (tess-ui Python `time_input_field`: 96 by 72 px; MD3 value #needs-verification), visible "Hour" and "Minute" supporting labels |
| Inline | settings rows, forms, toolbars | fields at the control height of the density level, numerals `body_large` or `body_medium`, no visible field labels |
| 12-hour | locales with AM and PM | hour 1 to 12 plus the period selector |
| 24-hour | the rest | hour 0 to 23, no period selector |

The choice between 12 and 24-hour follows the system locale unless the project sets it. MD3 does the same (`TimeFormat.CLOCK_24H` from the system, [Material Components Android time picker](https://github.com/material-components/material-components-android/blob/master/docs/components/TimePicker.md)).

## States

Field states are those of the outlined [[Text Field]]; the period selector takes those of [[Segmented Button]].

| State | Visual change | Token values |
|---|---|---|
| Rest | outline 1 dp `outline`, numeral `on_surface`, colon `on_surface` | as [[Text Field]] |
| Hover | outline `on_surface` | as [[Text Field]] |
| Focus | outline 2 dp `primary`, caret `primary`; the digits are selected on focus so typing replaces them | as [[Text Field]] |
| Error | outline `error`, supporting text `error`; the field that holds the out-of-range or incomplete value, not both | as [[Text Field]] |
| Disabled | numerals and outline `on_surface` at 38 percent and 12 percent; no focus | as [[Text Field]] |
| Period selected | selected segment `secondary_container` with `on_secondary_container`; unselected `surface` with `on_surface_variant`, outline `outline` | [Material Web segmented button tokens](https://github.com/material-components/material-web/tree/main/tokens/versions/latest/sass), [[State Layers]] |

## Tokens used

- Colour: roles as above ([[Colour Roles]]).
- Type: picker numerals `display_medium` (45 on 52 dp); inline numerals `body_large` at default, `body_medium` at compact and dense; colon in the type role of the numerals ([[Typography]]).
- Shape: field corners 4 dp; period selector 8 dp (picker, MD3 value #needs-verification) or `corner-full` segments per [[Segmented Button]] ([[Shape]]).
- Spacing and density: [[Spacing and Density]].

## Sizing and density

| Level | Inline field height | Field width | Padding x | Numeral type | Gap field to colon | Period selector height |
|---|---|---|---|---|---|---|
| default | 40 dp | 48 dp | 12 dp | `body_large` | 4 dp | 40 dp |
| compact | 32 dp | 40 dp | 8 dp | `body_medium` | 4 dp | 32 dp |
| dense | 28 dp | 40 dp | 8 dp | `body_medium` | 2 dp | 28 dp |

- The picker variant keeps the MD3 sizes at every density: 96 by 72 dp fields, 12 dp gap in tess-ui (`tess-ui:src/tess_ui/views/TimeInput_View.tdl`: field width 96, Gap 12). The picker lives in a [[Dialog]] where touch use is likely.
- Inline field width fits two digits plus padding: two digits of `body_large` take about 18 dp, so 48 dp at default; the widths 48, 40, 40 dp are Tesserae design choices #needs-verification-as-design-choice.
- Hit area at least 24 by 24 dp at every density; 48 by 48 dp in a touch context ([[Spacing and Density]]).
- Vertical centring by construction, as [[Text Field]] (AC-DEN-9); in the picker the 72 dp field centres the 52 dp line box.

## Layout and overflow

- The control is a horizontal row: hour, colon, minute, period selector. It never wraps and never exceeds its parent; the fields have fixed widths because the content is exactly two digits.
- The numerals are centred in the field (the digits are a fixed-width pair, not prose); the colon is centred on the fields' vertical axis.
- Content is never truncated: two digits always fit. A narrower parent than the control's minimum scrolls horizontally ([[10 Layout Overflow and Scrolling]]).

## Behaviour

- Pointer: a press in a field places the caret and selects the two digits; a press on a period segment selects it.
- Keyboard (focus in the hour or minute field):

| Keys | Result |
|---|---|
| Digits 0 to 9 | enter at the caret; the field takes at most two digits (`Mask: "##"`, `Max_Length: 2`) |
| Up, Down | increase, decrease the field by 1, wrapping (59 to 0 for minutes, 12 to 1 or 23 to 0 for hours) (`tess-ui:docs/components/time-input.md`, Python `time_input_field`); wrapping does not carry into the other field |
| Page Up, Page Down | increase, decrease by 10 minutes in the minute field, by 3 hours in the hour field #needs-verification-as-design-choice |
| Colon, Right (caret at the end of the hour) | move focus to the minute field |
| Left (caret at the start of the minute) | move focus to the hour field |
| A, P (12-hour time) | set AM, PM |
| Enter | commit; an incomplete or out-of-range field shows the error |
| Escape | revert to the last committed time; otherwise the key goes to the enclosing dialog |
| Tab, Shift+Tab | hour, minute, period selector (if shown), next control |

- Entering an hour: typing "2" in 24-hour time may be a complete hour (02) or the start of 20 to 23. The field commits "2" as 02 on blur or Enter; the second digit is accepted only if the pair stays in range. A digit that would make a pair out of range is not inserted (tess-ui leaves a non-fitting number out until it fits, `tess-ui:src/tess_ui/views/TimeInput_View.tdl`, the `On_Edit` expressions).
- Auto-advance: after the second valid digit of the hour, focus moves to the minute field. This is the typed-time convention on desktop; tess-ui does not do it today #needs-verification-as-design-choice.
- 12-hour conversion: hour 12 AM is 0, 12 PM is 12; the stored `Hour` is 0 to 23 (`tess-ui:src/tess_ui/views/TimeInput_View.tdl`). Switching the period changes the stored hour by 12.
- Touch: a tap focuses a field and opens the platform numeric keyboard where one exists.
- IME: only ASCII digits are accepted; full-width digits commit as ASCII #needs-verification-as-design-choice; composition text that is not digits is removed on commit. The candidate window follows the caret ([[Text Field]]).
- Validation hooks: out-of-range values are refused at entry; incomplete values (an empty field at commit) show an error in the field that is empty. When and how errors appear: [[Validation]] and [[Forms and Settings]].

## Tooltip and overlay behaviour

The control has no tooltip and opens no overlay ([[ADR-0004 Tooltip rule]]). The labels "Hour" and "Minute" are the visible supporting labels in the picker; in the inline variant they are the accessible names only, and the row label of [[Form Row]] names the group.

## Motion

None. Digit entry and state changes follow [[Text Field]] (at most 150 ms). Reduced motion: steady caret ([[14 Accessibility Basics]]).

## Accessibility

- The group has role `group` named by the row label or "Time" (tess-ui: `A11y { Role: group, Label: Time }`).
- Each field has role `spinbutton` with minimum, maximum and value (hour 0 to 23 or 1 to 12, minute 0 to 59) and the accessible names "Hour" and "Minute"; `increment` and `decrement` actions step it ([WAI-ARIA spinbutton](https://www.w3.org/TR/wai-aria-1.2/#spinbutton)). tess-ui draws each field as a `TextField` with role `textbox`; see Status in code.
- The period selector is a radio group with the names "AM" and "PM", the selected one exposed.
- Error text is a polite live region and the field is `invalid` ([[Text Field]]).
- Contrast: numerals 4.5 to 1; outline and period selector segments 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)).
- See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Dark and light

All colours are roles; the control follows the system theme ([[Theme Following the System]]); AC-TMI-10 runs in both.

## Defaults

- 12-hour from the locale, 24-hour otherwise; tess-ui defaults `Twelve` to true.
- Hour 0, minute 0.
- Inline variant at `compact` in config tools; picker variant in a [[Dialog]].

## Acceptance criteria

- [ ] AC-TMI-1 (token test): inline field height equals 40, 32, 28 dp and width 48, 40, 40 dp at default, compact, dense; picker fields are 96 by 72 dp at every density. Pass: values equal.
- [ ] AC-TMI-2 (geometry check): numerals centre in the field horizontally within 1 dp and vertically with space above and below differing by at most 1 px; the colon's vertical centre equals the fields' within 1 dp, at scale 1.0, 1.25, 2.0. Pass: within tolerance.
- [ ] AC-TMI-3 (scripted input): in a 24-hour input type "2", "5": the second digit is refused and the field shows "2"; type "2", "3": the field shows "23" and `Hour` is 23. Pass: field text and `Hour` equal.
- [ ] AC-TMI-4 (scripted input): in a 12-hour input type "13": the second digit is refused; type "12" with AM: `Hour` is 0; with PM: `Hour` is 12; switching the period from AM to PM at hour 9 changes `Hour` from 9 to 21. Pass: `Hour` equals the expected values.
- [ ] AC-TMI-5 (scripted input): type "6" and "0" in the minute field: the zero is refused if the pair is out of range ("60"); "59" is accepted and `Minute` is 59. Pass: field text and `Minute` equal.
- [ ] AC-TMI-6 (scripted input): Up in the minute field at 59 gives 0 and leaves `Hour` unchanged; Down at 0 gives 59; Up in the 24-hour hour field at 23 gives 0; in 12-hour time at 12 gives 1. Pass: values equal.
- [ ] AC-TMI-7 (scripted input): Tab order from the previous control is hour, minute, period selector (12-hour only), next control; Right at the end of the hour field after two digits and the colon key move focus to the minute field. Pass: focus sequence equals the list.
- [ ] AC-TMI-8 (scripted input): Escape after editing restores the last committed time; Enter with an empty minute field sets `invalid` on the minute field and leaves `Minute` unchanged. Pass: values and flags equal.
- [ ] AC-TMI-9 (AT tree assertion): the group has role `group` and a non-empty name; the fields have role `spinbutton` (or `textbox` with min and max where the platform lacks spinbutton), names "Hour" and "Minute", numeric value, minimum, maximum; the period selector exposes "AM" and "PM" with one selected; `increment` and `decrement` actions step by 1. Pass: all properties equal.
- [ ] AC-TMI-10 (contrast script): in light and dark, numerals on the field container 4.5 to 1 or more; outline and selected period segment against the surface 3 to 1 or more; error text 4.5 to 1. Pass: ratios at or above the limits.
- [ ] AC-TMI-11 (token test): the control's stylesheet holds no literal colour; the colon is `on_surface`; disabled content is `on_surface` at 38 percent. Pass: every colour is a role reference.
- [ ] AC-TMI-12 (geometry check): every field and period segment has a hit area of at least 24 by 24 dp (48 by 48 dp in a touch context); no hit areas overlap. Pass: sizes at or above the limits, zero overlap.
- [ ] AC-TMI-13 (geometry check): hover over the control for 600 ms shows no tooltip ([[ADR-0004 Tooltip rule]]). Pass: zero tooltips.
- [ ] AC-TMI-14 (scripted input): with IME composition injected into the hour field, non-digit composition is not inserted and a full-width digit commits as its ASCII digit (record `not testable` where the platform cannot be driven). Pass: field text equals ASCII digits.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TimeInput_View.tdl`, `tess-ui:src/tess_ui/views/TimeInput_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/date_time.py` | partly meets: hour, minute, colon, optional period selector, 24 and 12-hour conversion, digits mask and out-of-range refusal exist (AC-TMI-3 to AC-TMI-5 meet as documented); picker variant only, 96 dp wide fields with a `display_medium` colon (AC-TMI-1 fails for the inline variant: absent; no density setting); Up and Down stepping exists in the Python `time_input_field` but not in the view (AC-TMI-6 fails for the view); no auto-advance, no Left and Right hand-over (AC-TMI-7 partly meets: Tab works); fields are `TextField` with role `textbox`, not `spinbutton` (AC-TMI-9 fails); the group name "Time" exists |
| tess-shell | none | absent: no time input block or module |
| tre | engine `text_input` (`tre:docs/guide/text.md`) | not applicable (primitive) |

Evidence: `tess-ui:docs/components/time-input.md`.

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TimeInput_View.tdl`, `tess-ui:docs/components/time-input.md` | exists, partial |
| tess-shell | none | absent |
| tre | `tre:docs/guide/text.md` | primitive only |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Inline variant with fields 40, 32, 28 dp high instead of the 72 dp picker field | desktop forms hold many rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Up, Down stepping, A and P keys, auto-advance and colon hand-over in the fields | keyboard-first entry | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Fields exposed as `spinbutton` | each field has a numeric range | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| The input is a stand-alone element, not only the keyboard mode of a dialog | desktop forms need a typed time without a dialog | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- [Material Components Android time picker docs](https://github.com/material-components/material-components-android/blob/master/docs/components/TimePicker.md): input mode, hour 0 to 23 and minute 0 to 59, system 12 or 24-hour format.
- tess-ui time input documentation: `tess-ui:docs/components/time-input.md`.
- [WAI-ARIA 1.2 spinbutton](https://www.w3.org/TR/wai-aria-1.2/#spinbutton), [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.11, 2.5.8.
- MD3 time input field size (96 by 72 dp), the period selector shape and the numeral type role could not be read from m3.material.io (script-rendered) and are marked #needs-verification.
