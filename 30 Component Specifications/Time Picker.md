---
title: Time Picker
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, picker, input, dial]
related: ["[[Date Picker]]", "[[Time Input]]", "[[Dialog]]", "[[Popup]]", "[[Text Field]]", "[[Button]]", "[[Icon Button]]", "[[Radio Button]]", "[[Slider]]", "[[Tooltip]]", "[[Form Row]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Typography]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Scrim]]", "[[Validation]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Dialog]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Time Picker

> [!info] Summary
> A dialog in which the user sets an hour and a minute on a clock dial, with an AM and PM selector in 12-hour time and a typed-entry mode: the Material Design 3 [time pickers](https://m3.material.io/components/time-pickers/overview), with density levels and a keyboard model derived from the WAI-ARIA slider and radio group patterns. Source of truth in code: see Status in code.

## Purpose

Choose a time of day by pointing at a clock face, or type it. The picker returns an hour from 0 to 23 and a minute from 0 to 59 and never a date or a zone.

## When to use and not

- Use when: the time is on a clock face the user can reason about (a meeting at 3 pm); the user may prefer pointing.
- Do not use when: the time is typed faster than it is picked (an exact timestamp: use [[Time Input]] or a masked [[Text Field]]); a date is needed ([[Date Picker]]); a duration or an elapsed time is needed (a [[Spin Box]]).

## Anatomy

Modal picker (a [[Dialog]] over a [[Scrim]]):

1. Heading: the small title ("Select time"), `label_medium`, `on_surface_variant`.
2. Hour selector: a button 96 by 80 dp showing the hour in `display_large`; it chooses which value the dial sets.
3. Colon: `display_large`.
4. Minute selector: as the hour selector.
5. Period selector (12-hour time): two halves, AM above PM, 52 dp wide, 80 dp high, 1 dp `outline` frame, corner `small`.
6. Dial (dial mode): a 256 dp circle of `surface_container_highest` with twelve labels, a 2 dp hand from the centre, an 8 dp centre dot and a 48 dp selector circle with the chosen number.
7. Typed fields (typed mode, replaces 6): the [[Time Input]] fields, 96 by 72 dp.
8. Footer: a mode button (keyboard icon or clock icon) at the start, Cancel and OK at the end.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Dial, 12-hour | default | dial with 12 labels, period selector |
| Dial, 24-hour | 24-hour locales | the dial layout is not specified: the inner ring of the MD3 24-hour dial is not verified #needs-verification; until then 24-hour time opens in typed mode |
| Input (typed) | the user knows the time | [[Time Input]] fields replace the dial; the mode button swaps; 12-hour keeps the period selector |
| Docked (popup under a field) | not specified | not built; Material Web tokens exist for the modal and input forms only |

## States

State layer percentages come from [[State Layers]] ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). Colours from the Material Web time picker tokens ([`_md-comp-time-picker.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-time-picker.scss)):

| Part and state | Container | Content | Layer colour |
|---|---|---|---|
| Dialog | `surface_container_high`, corner `extra_large` (28 dp) | heading `on_surface_variant` | not applicable |
| Hour or minute selector, chosen | `primary_container` | `on_primary_container` | `on_primary_container` |
| Hour or minute selector, not chosen | `surface_container_highest` | `on_surface` | `on_surface` (tess-ui; the token set names `on_primary_container` for the chosen state only) |
| Period half, chosen | `tertiary_container` | `on_tertiary_container` | `on_tertiary_container` |
| Period half, not chosen | none | `on_surface_variant` | `on_surface_variant` |
| Period frame | none | 1 dp `outline` | not applicable |
| Dial face | `surface_container_highest` | labels `on_surface`; label under the selector `on_primary` | not applicable |
| Dial hand, centre dot, selector | `primary` | none | `primary` on the selector |
| Dial dragging | as above | as above | selector layer 16 percent |
| Disabled dial | face `on_surface` at 12 percent | hand, dot, selector `on_surface` at 38 percent | none |
| Keyboard focus | as the state | as the state | focus ring 3 dp, offset 2 dp, role `secondary` on the focused part (the dial face, a selector, a period half) |

Layer opacities: hover 8, focus 10, pressed 10, dragged 16 percent. Chosen is shown by the filled container and the number under the selector, not by colour alone ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).

## Tokens used

[[Colour Roles]] (roles above), [[Shape]] (dialog `extra_large`, selectors and period `small`, dial, selector and dot `corner-full`), [[Typography]] (`display_large` times, `title_medium` period labels, `body_large` dial labels, `label_medium` heading), [[Motion]] (hand sweep `medium1` 250 ms with `emphasized_decelerate` in tess-ui), [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

MD3 values (Material Web tokens): dial 256 dp, selector handle 48 dp, selector centre 8 dp, selector track 2 dp, time selector 96 by 80 dp (24-hour vertical 114 dp wide), period selector vertical 52 by 80 dp and horizontal 216 by 38 dp, period outline 1 dp, shapes `small` for selectors and periods and `extra_large` for the container; input form: field 96 by 72 dp, period 52 by 72 dp ([time picker](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-time-picker.scss), [time input](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-time-input.scss)).

Rule: dial, selector circle, time selector, period selector and time text scale down together; the dialog content width equals the header row (two time selectors, the colon, the period selector and three gaps); a part is never smaller than 24 dp in either direction.

| Level | Dial | Selector circle | Centre dot | Time selector | Period selector (halves) | Time text | Header gap |
|---|---|---|---|---|---|---|---|
| default | 256 dp | 48 dp | 8 dp | 96 by 80 dp | 52 by 80 dp (40 dp) | `display_large` | 12 dp |
| compact | 224 dp | 40 dp | 8 dp | 80 by 64 dp | 48 by 64 dp (32 dp) | `display_medium` | 8 dp |
| dense | 192 dp | 32 dp | 6 dp | 64 by 48 dp | 44 by 48 dp (24 dp) | `display_small` | 8 dp |

The compact and dense rows are Tesserae design choices #needs-verification-as-design-choice. The dial labels sit on a circle of radius dial/2 minus selector/2 minus 4 dp, so neighbouring selector circles never overlap (the circumference spacing is at least the selector diameter at all levels).

- Hit areas: the dial is one hit area (the whole circle); each selector and period half is its own hit area at least 24 by 24 dp ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)); 48 dp in touch contexts for the period halves and mode button.
- Footer buttons and the mode button use the sizes of [[Button]] and [[Icon Button]] at the level.

## Layout and overflow

- The dialog is centred; content width as in Sizing and density; heights follow the content; a window shorter than the dialog scrolls the dialog body with the scrollbar rule ([[Scrollbar and Scroll Container]], [[ADR-0003 Scrollbar rule]]).
- The time text is two digits and never truncates; the hour shows 1 to 12 in 12-hour time and 00 to 23 otherwise; the minute shows 00 to 59.
- The period selector sits to the end of the minute selector in the header row (right in left-to-right locales); the dial is centred below.
- Dial labels are text centred on their position (vertical centring by line box); the selected label sits in the selector circle.

## Behaviour

- Pointer: press or drag on the dial points the hand; in hour mode the hour snaps to one of 12 positions and keeps the AM or PM half; in minute mode the minute snaps to the nearest mark of 5 minutes (tess-ui; the MD3 snap is not verified #needs-verification); the pointer is captured, so a drag may leave the dial. Releasing in hour mode moves on to minute mode (the picker announces "Minutes"). A press on the hour or minute selector chooses the mode. A press on a period half chooses AM or PM.
- Keyboard (no APG pattern exists for a time dial; the dial follows the [slider pattern](https://www.w3.org/WAI/ARIA/apg/patterns/slider/) and the period selector the [radio group pattern](https://www.w3.org/WAI/ARIA/apg/patterns/radio/) #needs-verification as MD3 behaviour):
  - Tab order: hour selector, minute selector, period selector (one stop), dial (one stop), mode button, Cancel, OK; Shift+Tab reverses; the dialog traps focus ([[Dialog]]); initial focus is the hour selector.
  - Dial, focused: Right Arrow and Up Arrow increase by one unit (one hour in hour mode, one minute in minute mode); Left Arrow and Down Arrow decrease by one unit; Page Up and Page Down by a quarter of the dial in hour mode (3 hours) and by 5 minutes in minute mode; Home and End go to the first and last value of the face (hour 12 and 11, minute 00 and 59). Values wrap; the AM or PM half does not change by hour keys. Enter and Space in hour mode move on to minute mode; in minute mode they do nothing (OK is a Tab stop and Enter on OK commits).
  - Hour and minute selectors: Enter and Space choose the mode.
  - Period selector: Tab enters on the chosen half; Up, Down, Left and Right Arrow choose the other half (two items, wrapping), Space chooses the focused half; the hour in 24-hour terms updates by 12 hours.
  - Escape closes the dialog and leaves the time unchanged; focus returns to the control that opened it.
- Typed mode: the fields take two digits; hour in 1 to 12 (12-hour) or 0 to 23; minute 0 to 59; a value out of range shows the field error and disables OK; Up and Down Arrow in a field step by one with wrap ([[Time Input]]).
- Touch: tap on the dial, selectors and period halves behaves as a press.
- Events: `On_Ok` once after OK, with the time; Cancel and Escape raise a cancel event; the hour and minute values change only on OK; reopening starts from the current values; setting the time from code raises no event.
- Time limits (earliest, latest): not specified; not built.

## Tooltip and overlay behaviour

- The picker is a [[Dialog]] over a [[Scrim]]; focus trapped; Escape cancels.
- The dial, the hour and minute selectors and the period halves carry no tooltips (their content is visible text); the mode button, as an [[Icon Button]], carries its own tooltip with its name, 500 ms after hover and at once on keyboard focus ([[ADR-0004 Tooltip rule]], [[Tooltip]]). The slider value label of [[Slider]] is not used; the header shows the value.
- Focus on open: the hour selector; on close: the control that opened the picker.

## Motion

Hand and selector sweep `medium1` 250 ms with `emphasized_decelerate` (tess-ui); no animation while dragging; the mode change from hour to minute sweeps the hand once. Colour fades `short3` 150 ms. The modal opens and closes per [[Dialog]]. Reduced motion: the hand jumps in one frame ([[14 Accessibility Basics]]).

## Accessibility

- Dialog: role `dialog`, modal, name from the title.
- Dial: role `slider` named after the mode ("Hour" or "Minute", not a fixed "Clock"), `value`, `value_min`, `value_max`, `value_step` for the mode (hour 0 to 23 step 1; minute 0 to 59 step 1), value text in words ("3 pm", "15 minutes"); increment and decrement actions step by one unit.
- Selectors: role `button` named "Hour" and "Minute" with `selected` for the chosen mode; the header time is a live region (polite) so a change by dial or key is announced; a mode change announces "Minutes".
- Period selector: role `radiogroup` named "Period" with two `radio` nodes "AM" and "PM", `checked`, position 1 of 2 and 2 of 2.
- Mode button: named "Switch to typing" and "Switch to the clock".
- Typed fields: names "Hour" and "Minute"; an invalid value exposes the error ([[Validation]]).
- Contrast: dial labels `on_surface` against the face at least 4.5 to 1; label under the selector `on_primary` against `primary` at least 4.5 to 1; hand against the face at least 3 to 1; chosen selector text `on_primary_container` against `primary_container` at least 4.5 to 1; focus ring at least 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)).
- The dial is never the only way: typed mode is one key press (the mode button) away and the dial is operable from the keyboard.

## Dark and light

All roles; follows the scheme ([[Theme Following the System]]). AC-TMP-11 runs in both.

## Defaults

Modal, dial mode, hour mode, 12-hour (`Twelve` true), density from the container, time 00:00 until set, English labels in tess-ui, 24-hour time opens in typed mode.

## Acceptance criteria

- [ ] AC-TMP-1 (token test): dial, selector circle, centre dot, track width 2 dp, time selector and period selector sizes equal the table at each level (256, 48, 8, 96 by 80, 52 by 80 at default; 224, 40, 8, 80 by 64, 48 by 64 at compact; 192, 32, 6, 64 by 48, 44 by 48 at dense); period frame 1 dp; dialog corner 28 dp. Pass: all values equal.
- [ ] AC-TMP-2 (geometry check): the dialog content width equals two time selectors plus colon plus period selector plus three gaps; the 12 dial labels lie on a circle of radius dial/2 minus selector/2 minus 4 dp within 0.5 dp; adjacent selector circles do not overlap; every hit area is at least 24 by 24 dp at each level and the touch hit areas are at least 48 dp. Pass: measured values within tolerance.
- [ ] AC-TMP-3 (scripted input): in hour mode a press at 3 o'clock sets hour 3 (or 15 when the PM half is chosen), keeps the half, and releasing moves to minute mode; a press at 6 o'clock in minute mode sets minute 30. Pass: hour, minute, mode and half equal.
- [ ] AC-TMP-4 (scripted input): on the focused dial in hour mode the arrows change the hour by one with wrap and without changing the half; Page Up and Page Down by 3 hours; Home and End to 12 and 11; in minute mode the arrows by one minute, Page keys by 5 minutes, Home and End to 00 and 59; Enter in hour mode moves to minute mode. Pass: the value sequence equals the list.
- [ ] AC-TMP-5 (scripted input): the Tab order is hour selector, minute selector, period selector, dial, mode button, Cancel, OK, then the hour selector; Shift+Tab reverses; the period selector and the dial are one stop each. Pass: the focus owner sequence equals the list.
- [ ] AC-TMP-6 (scripted input): Tab enters the period selector on the chosen half; each arrow key chooses the other half and fires one change event; Space on the unchosen focused half chooses it; the 24-hour hour changes by 12. Pass: chosen half, hour and event counts equal.
- [ ] AC-TMP-7 (scripted input): OK sets hour and minute once and runs `On_Ok` once; Cancel and Escape leave them unchanged and return focus to the opener; reopening shows the stored time. Pass: values, event counts and focus owner equal.
- [ ] AC-TMP-8 (scripted input): typed mode: "12" in the hour field (12-hour) and "75" in the minute field shows the minute error and disables OK; "07" and "45" enable OK; the mode button swaps and keeps the draft time both ways. Pass: draft time, error flag and OK state equal.
- [ ] AC-TMP-9 (AT tree assertion): dialog role and name; the dial is `slider` named after the mode with `value`, `value_min`, `value_max`, `value_step` and value text; selectors are `button` with `selected`; the period selector is `radiogroup` named "Period" with two `radio` nodes and `checked`; the header time is a live region. Pass: all equal.
- [ ] AC-TMP-10 (token test): colours per the States table; state layer opacities 0.08, 0.10, 0.10 and 0.16 (dragged); disabled face 0.12, disabled hand, dot and selector 0.38. Pass: values equal.
- [ ] AC-TMP-11 (contrast script): light and dark, the pairs listed under Contrast. Pass: ratios at or above 4.5 to 1 for text and 3 to 1 for the hand and ring.
- [ ] AC-TMP-12 (scripted input): hover the dial, a selector and a period half 1000 ms: no tooltip is visible; hover the mode button 600 ms: exactly its own tooltip. Pass: visible tooltip count and owner equal.
- [ ] AC-TMP-13 (scripted input): with reduced motion on, setting the hour by key places the hand and selector in the first frame. Pass: hand end point at the final position in that frame.
- [ ] AC-TMP-14 (pixel check): the modal container is opaque `surface_container_high` over the scrim; the focused part's ring is fully visible inside the dialog; the hand runs from the centre dot to the selector circle centre (end point within 1 dp of the label position of the chosen value). Pass: pixels and geometry within tolerance.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TimePicker_View.tdl`, `TimePicker_Stylesheet.tdl`, `PeriodSelector_View.tdl`, `TimeInput_View.tdl`, `tess-ui:src/tess_ui/controls.py` (`TimePickerDial`), `tess-ui:docs/components/time-pickers.md` | partly meets: modal overlay, dialog role with title, 328 dp wide, 256 dp dial, 48 dp selector, 8 dp centre, 2 dp hand, 96 by 80 dp selectors with `primary_container` chosen, period selector 52 by 80 dp with 40 dp halves, 1 dp `outline`, `tertiary_container`, radios inside a `group` with `Checked`, mode button, typed fields with masks and ranges, OK sets hour and minute, Cancel, Escape and scrim leave them, reopening starts from the stored time, auto-advance from hour to minute, dial role `slider` with value range and increment and decrement actions, reduced motion respected (AC-TMP-3, AC-TMP-7, AC-TMP-8 meet by reading, unrun). Fails: no density, one size (AC-TMP-1, AC-TMP-2 at compact and dense); dial arrows step the minute by 5 and have no Page, Home, End, Enter keys (AC-TMP-4); dial name is the fixed label "Clock" and no value text (AC-TMP-9); header time not a live region (AC-TMP-9); period selector is role `group`, not `radiogroup`, and no set position (AC-TMP-9, AC-TMP-6 partly: only Up and Down arrows through `Focus_Group: vertical`); selector layer colour not read (AC-TMP-10); no tooltips read (AC-TMP-12); `Twelve: false` opens straight on typed fields: no 24-hour dial (consistent with the Variants note); not built: time limits, locale time formats |
| tess-shell | none | absent |
| tre | `tre:docs/reference/node.md` (`role="slider"`, `value_text`, `live`, `selected`) | not applicable: the engine has the slider role, `value_text` and live regions; no `radiogroup` role and no modal flag; candidate requests as in [[Radio Button]] and [[Date Picker]] |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Dial 224 and 192 dp, selectors and period sizes scaled at compact and dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Dial keyboard model (arrows, Page, Home, End, Enter) from the slider pattern | MD3 and the APG give no time dial keys | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Period selector is a radio group with arrow keys | APG radio group model | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| 24-hour time opens in typed mode; no 24-hour dial yet | the MD3 24-hour dial layout is not verified | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Invalid typed time shows the field error and disables OK | WCAG 3.3.1 error identification | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule) |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |

## Sources

- Material Web tokens: [time picker](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-time-picker.scss) (clock dial 256 px, selector handle 48 px, selector centre 8 px, selector track 2 px, time selector 96 by 80 px, 24-hour vertical selector 114 px, period vertical 52 by 80 px, horizontal 216 by 38 px, period outline 1 px, shapes `small` and `extra_large`, colours `surface_container_highest`, `primary`, `on_primary`, `primary_container`, `tertiary_container`, `outline`; fonts `display_large`, `title_medium`, `body_large`, `label_medium`), [time input](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-time-input.scss) (field 96 by 72 px, period 52 by 72 px) (verified 2026-11-21).
- [Material Components Android TimePicker](https://github.com/material-components/material-components-android/blob/master/docs/components/TimePicker.md): clock and keyboard modes, parts list.
- [WAI-ARIA Authoring Practices slider](https://www.w3.org/WAI/ARIA/apg/patterns/slider/) and [radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/) patterns (verified 2026-11-21); there is no APG pattern for a time dial.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.5.8, 3.3.1.
- The m3.material.io time picker page could not be fetched (script-rendered site); Material Web has no time picker component, only tokens.
- Code: `tess-ui:src/tess_ui/views/TimePicker_View.tdl`, `PeriodSelector_View.tdl`, `TimeInput_View.tdl`, `tess-ui:src/tess_ui/controls.py` (`TimePickerDial`), `tess-ui:docs/components/time-pickers.md`, `tre:docs/reference/node.md`.
