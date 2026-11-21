---
title: Date Picker
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, picker, input, grid]
related: ["[[Time Picker]]", "[[Time Input]]", "[[Dialog]]", "[[Popup]]", "[[Text Field]]", "[[Button]]", "[[Icon Button]]", "[[Tooltip]]", "[[Form Row]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Typography]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Scrim]]", "[[Validation]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Dialog]]", "[[Popup]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Date Picker

> [!info] Summary
> A calendar grid in which the user picks one date, in a modal dialog or in a popup under a field, with a typed-entry mode: the Material Design 3 [date pickers](https://m3.material.io/components/date-pickers/overview) (modal, docked, input), with density levels and the keyboard grid of the WAI-ARIA Authoring Practices date picker dialog. Source of truth in code: see Status in code.

## Purpose

Choose a calendar date by seeing the month around it, or type it. The picker returns one date as text in the form `year-month-day` (tess-ui) and never a time.

## When to use and not

- Use when: the date is near today or relative to a visible weekday (appointments, deadlines); the range of valid dates is limited.
- Do not use when: the date is far from today and known to the user (birth dates: type it in a [[Text Field]] with a mask); a time is needed ([[Time Picker]]); a free period is needed (range picker, not specified here).

## Anatomy

Modal picker (a [[Dialog]] with a [[Scrim]]):

1. Heading: the small title ("Select date"), `label_medium`, `on_surface_variant`.
2. Header: the chosen date in `headline_large`, `on_surface`, as a live region ("Fri, Nov 20", or "No date"); a mode button (keyboard icon) after it.
3. Divider.
4. Month bar: the month and year in `title_small`, a previous-month and a next-month icon button, and the month-year selector.
5. Weekday row: seven column headers, initials in `body_large`.
6. Day grid: six rows of seven day cells.
7. Typed field (typed mode, replaces 4 to 6): a `Text Field` with a mask.
8. Footer: Cancel and OK (text buttons).

Docked picker (a [[Popup]] anchored below a [[Text Field]] with a calendar icon button): parts 4 to 6 only, no header and no footer.

Day cell: a circle holding the number (`body_large`), the state layer over the circle, a 1 dp outline for today.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Modal | forms and dialogs; the date is chosen in focus | Dialog, Scrim, header, Cancel and OK; the date is committed on OK |
| Docked | a date field in a form on desktop | popup under the field, no header, no footer; Enter or Space on a day commits and closes |
| Input (typed) | the user knows the date | a masked text field replaces the grid in the modal picker; the mode button swaps |
| Range | a period between two dates | not specified: not built in tess-ui and not used in a project; MD3 has it |

## States

State layer percentages come from [[State Layers]] ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). Colours from the Material Web modal date picker tokens ([`_md-comp-date-picker-modal.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-date-picker-modal.scss)):

| State of a day cell | Container | Outline | Number | State layer (colour) |
|---|---|---|---|---|
| Normal | none | none | `on_surface` | `on_surface_variant` |
| Today | none | 1 dp `primary` | `primary` | `primary` |
| Selected | `primary` | none | `on_primary` | `on_primary` |
| Outside the shown month | none | none | `on_surface_variant` (Tesserae, tess-ui) | `on_surface_variant` |
| Disabled (outside `earliest` and `latest`) | none | none | `on_surface` at 38 percent | none |
| Focused day (keyboard) | as the state | as the state | as the state | layer 10 percent, ring 3 dp, offset 2 dp, role `secondary` |

Layer opacities: hover 8, focus 10, pressed 10 percent. Today and selected are not carried by colour alone: today has the outline and `aria-current`, selected has the filled circle and the selected state ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)). The dialog container is `surface_container_high` with corner `extra_large` (28 dp); the docked container is `surface_container_high` with corner `large` (16 dp).

## Tokens used

[[Colour Roles]] (roles above), [[Shape]] (modal `extra_large` 28 dp, docked `large` 16 dp, day circle `corner-full`), [[Typography]] (`headline_large` header, `label_large` supporting text, `body_large` days and weekdays, `title_small` month), [[Elevation]] (level 3 for the modal container in tess-ui), [[Motion]], [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

MD3 values (Material Web tokens): modal container 360 by 524 dp, header 120 dp, day container 40 by 40 dp, today outline 1 dp, year cell 72 by 36 dp; docked container 360 by 456 dp, day container 48 by 48 dp with a 40 dp state layer, header 64 dp, menu button 40 dp; date input modal 328 by 512 dp ([modal](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-date-picker-modal.scss), [docked](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-date-picker-docked.scss), [input](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-date-input-modal.scss)).

Rule: the day pitch (cell width and height, circle diameter and hit area) equals the control height of the level; the dialog width is seven pitches plus twice the dialog padding, at least 280 dp, with the grid centred; the header height scales down with the level.

| Level | Day pitch (circle, hit area) | Weekday row height | Dialog padding | Dialog width | Header height | Month bar height |
|---|---|---|---|---|---|---|
| default | 40 dp | 40 dp | 24 dp | 328 dp | 120 dp | 40 dp |
| compact | 32 dp | 32 dp | 16 dp | 280 dp | 96 dp | 32 dp |
| dense | 28 dp | 28 dp | 12 dp | 280 dp | 80 dp | 28 dp |

Default width 328 dp equals the Material Web date input modal width. The compact and dense rows are Tesserae design choices #needs-verification-as-design-choice. In a touch context the day pitch is 48 dp (the tess-ui size and the MD3 docked container) and the dialog is 384 dp wide.

- Hit area: the day pitch square, at least 24 by 24 dp at every level ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)); 48 dp in touch contexts. Adjacent cells do not overlap.
- The grid is always six rows by seven columns so the dialog does not change height between months.
- Month bar buttons are [[Icon Button]]s at the level's size; Cancel and OK are [[Button]]s at the level's size.

## Layout and overflow

- The dialog is centred in the window and never larger than the window minus 24 dp on each side; if the window is shorter than the dialog, the grid keeps its size and the dialog body scrolls under the header with the scrollbar rule ([[Scrollbar and Scroll Container]], [[ADR-0003 Scrollbar rule]]).
- Day numbers are one or two digits and never truncate; the weekday initials are one character in the shown locale; the header date truncates with an ellipsis only when it exceeds the dialog width.
- The docked popup opens below the field, left-aligned with it; when there is no room below it opens above ([[Popup]]); its width is 7 pitches plus padding.
- Month names and weekday initials come from the platform locale; the first weekday is the locale's unless the project sets it.

## Behaviour

- Pointer: press on a day shows the pressed layer; release inside selects it (modal: the draft date; docked: the date, then the popup closes). A press on an outside-month day selects it and shows its month. Previous and next buttons change the month by one. A press on the month-year selector toggles a year list (cells 72 by 36 dp); choosing a year returns to the grid.
- Keyboard ([APG date picker dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/), verified 2026-11-21):

| Key | In the day grid |
|---|---|
| Right Arrow, Left Arrow | next day, previous day; at a month edge the grid shows the neighbouring month |
| Down Arrow, Up Arrow | same weekday next week, previous week; at a month edge the grid changes month |
| Home, End | first and last day of the current week |
| Page Up, Page Down | previous and next month; the same day number, else the last day of that month |
| Shift+Page Up, Shift+Page Down | same month in the previous and next year; the same day number, else the last day of the month |
| Space, Enter | select the focused day (modal: set the draft date; docked: set the date and close) |
| Escape | close without changing the date; focus returns to the opener |
| Tab, Shift+Tab | next and previous element of the dialog; the grid is one Tab stop |

  - The Tab order in the modal picker is: mode button, previous month, next month, month-year selector, the grid (one stop: the focused day), Cancel, OK; Shift+Tab reverses; Tab from OK goes to the mode button (the dialog traps focus, [[Dialog]]).
  - Initial focus: the day of the current date; with no date, today; if that day is disabled, the nearest enabled day. Disabled days are skipped by the arrow keys (focus moves to the next enabled day in the direction; at the last enabled day the key does nothing).
  - Enter on Cancel or OK activates it. OK sets the date and closes; Cancel and Escape leave the date unchanged.
  - Typed mode: the field takes `####-##-##`; a value that is not a real day or is outside `earliest` and `latest` shows the field error with the description "Enter a date as year-month-day between <earliest> and <latest>" and disables OK; a valid value sets the draft date. The mode button swaps the grid and the field and keeps the draft date.
- Touch: tap on the 48 dp day cell selects.
- Events: `On_Ok` runs once after OK (modal) or once after a docked selection; Cancel and Escape raise a cancel event; the date value changes only on OK (modal) or on selection (docked); setting the date from code raises no event.

## Tooltip and overlay behaviour

- The picker is an overlay: the modal form is a [[Dialog]] over a [[Scrim]] (focus trapped, Escape cancels, [[Popup]] and Dialog rules apply); the docked form is a popup that closes on Escape, on a press outside and on window focus loss.
- Day cells carry no tooltips. The icon buttons (mode, previous, next, calendar icon of the field) each carry their own tooltip with their name, 500 ms after hover and at once on keyboard focus ([[ADR-0004 Tooltip rule]], [[Tooltip]]); the grid, the month bar and the header carry none.
- Focus on open: the focused day (see Behaviour). Focus on close: the control that opened the picker.

## Motion

The modal container opens and closes per [[Dialog]]. The month changes in one frame (no slide). State layers follow the fade timing of [[State Layers]]; colour changes use `short3` 150 ms ([[Motion]]). Reduced motion: no fades ([[14 Accessibility Basics]]).

## Accessibility

APG date picker dialog and grid pattern ([grid](https://www.w3.org/WAI/ARIA/apg/patterns/grid/)):

- Dialog: role `dialog`, `aria-modal` true, name from the title.
- Month heading: a live region (polite) so a month or year change is announced; so is the header date.
- Grid: role `grid` named by the month heading; header row with `columnheader` cells whose full names ("Monday") are exposed (the visible initial is the name's first letter); `row` per week; `gridcell` per day containing the focusable button; only one cell has tab index 0 (roving focus); `aria-selected` true on the chosen day; `aria-current="date"` on today; `aria-disabled` true on disabled days.
- Day name: the full date ("Friday, 20 November 2026"), not the number.
- Navigation buttons named "Previous month", "Next month", "Switch to typing" and "Switch to the calendar".
- Keyboard hints: a visually shown or live-announced hint on entering the grid, as in the APG example ("Arrow keys move by day, Page Up and Page Down by month").
- Error in typed mode: invalid text exposes the error and description ([[Validation]]).
- Contrast: day numbers against the container at least 4.5 to 1; selected circle against the container at least 3 to 1 and `on_primary` against `primary` at least 4.5 to 1; today outline at least 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)).
- Target sizes as in Sizing and density.

## Dark and light

All roles; follows the scheme ([[Theme Following the System]]). AC-DTP-11 runs in both.

## Defaults

Modal variant, grid mode, density from the container, week starts on the locale's first day (Sunday in tess-ui), no `earliest` and `latest`, date empty (shows "No date" and focuses today), six weeks of days, English names in tess-ui.

## Acceptance criteria

- [ ] AC-DTP-1 (token test): day pitch, circle, weekday row, dialog padding, dialog width and header height equal the table at each level (40, 40, 24, 328, 120 at default; 32, 32, 16, 280, 96 at compact; 28, 28, 12, 280, 80 at dense), corner 28 dp (modal) and 16 dp (docked), today outline 1 dp. Pass: all values equal.
- [ ] AC-DTP-2 (geometry check): the grid has exactly 6 rows by 7 columns at every month; day cells are pitch by pitch; no two cells overlap; at every level the hit area is at least 24 by 24 dp and in a touch context at least 48 by 48 dp. Pass: counts and bounds equal.
- [ ] AC-DTP-3 (scripted input): in the grid, Right, Left, Down, Up move the focused day by 1 and 7 days, crossing month borders and updating the month heading; Home and End go to the first and last day of the week; Page Up and Page Down change the month with the same day number or the month's last day (31 March, Page Down: 30 April); Shift+Page Up and Shift+Page Down change the year (29 February to 28 February). Pass: the focused ISO date equals the expected list after each key.
- [ ] AC-DTP-4 (scripted input): Space and Enter on a day set the draft date (modal) or set the date and close (docked); OK sets the date once and runs `On_Ok` once; Cancel and Escape leave the date unchanged and focus returns to the opener. Pass: date value, popup state, event counts and focus owner equal.
- [ ] AC-DTP-5 (scripted input): the Tab order in the modal picker is mode button, previous, next, month-year selector, one stop in the grid, Cancel, OK, then the mode button again; Shift+Tab reverses; the grid has exactly one Tab stop. Pass: the focus owner sequence equals the list.
- [ ] AC-DTP-6 (scripted input): with `earliest` and `latest` set, days outside are disabled, cannot be selected by pointer or Enter, and arrow keys skip them; initial focus on open is the current date's day, else today, else the nearest enabled day. Pass: focus owner and date equal.
- [ ] AC-DTP-7 (scripted input): in typed mode a valid text sets the draft date; an invalid or out-of-range text shows the field error, sets the description, disables OK and leaves the draft date unchanged; the mode button preserves the draft date both ways. Pass: draft date, error flag and OK state equal.
- [ ] AC-DTP-8 (AT tree assertion): the dialog has role `dialog`, a name and modal true; the grid has role `grid` with the month heading as name; weekday headers expose full names; each day is a `gridcell` with a name equal to the full date, `selected` equal to the state, current `date` on today and `disabled` on disabled days; the month heading and the header date are live regions (polite). Pass: all equal.
- [ ] AC-DTP-9 (token test): state layer opacities 0.08, 0.10, 0.10; layer colours per the States table; disabled day number 0.38; selected container `primary` and number `on_primary`; today outline `primary`. Pass: values equal.
- [ ] AC-DTP-10 (scripted input): hover a day cell 1000 ms: no tooltip is visible; hover the next-month button 600 ms: exactly its tooltip is visible. Pass: visible tooltip count and owner equal.
- [ ] AC-DTP-11 (contrast script): light and dark, day number against the container at least 4.5 to 1; `on_primary` against `primary` at least 4.5 to 1; selected circle and today outline against the container at least 3 to 1; focus ring against the container at least 3 to 1. Pass: ratios at or above the limits.
- [ ] AC-DTP-12 (pixel check): the modal container is opaque `surface_container_high` with the scrim over the window; the focused day's ring is fully visible inside the dialog (no clipped ring pixels); nothing paints outside the dialog except the scrim. Pass: pixels equal within 1 per 8-bit channel.
- [ ] AC-DTP-13 (scripted input): the docked picker opens below the field (above when there is no room), closes on Escape, on a press outside and on window focus loss, returns focus to the field and commits on selection. Pass: popup bounds, state and focus owner equal.
- [ ] AC-DTP-14 (scripted input): the month-year selector opens a year list; Enter on a year returns to the grid at that year with the same month. Pass: shown month and year equal.
- [ ] AC-DTP-15 (scripted input): month names and weekday initials equal the platform locale's (German locale: "Montag" and "M"); the first weekday follows the locale or the project setting. Pass: strings equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/DatePicker_View.tdl`, `DatePicker_Stylesheet.tdl`, `DatePickerDay_View.tdl`, `DatePickerDay_Stylesheet.tdl`, `tess-ui:docs/components/date-pickers.md` | partly meets: modal overlay with `Modal: true`, dialog role with title, 28 dp corner, `surface_container_high`, header with live date, mode button swapping a masked `####-##-##` field, month bar with live month, previous and next, six rows by seven, `earliest` and `latest` disable days, `Week_Starts`, today `current: date`, selected state, Cancel and OK, date set only on OK, Escape and scrim close (AC-DTP-4, AC-DTP-6 partly, AC-DTP-9 by reading). Fails: no density: 48 dp cells in a 384 dp dialog (AC-DTP-1, AC-DTP-2 at the three levels; the touch size is the only size); the grid is role `group` named "Days" with no `grid`, `row`, `gridcell` or `columnheader` and each day is a `button` named by its number only (AC-DTP-8; the engine has no grid roles); the grid is one Tab stop with arrows through `Focus_Group: both`, but Home, End, Page Up, Page Down and Shift variants are not built, and arrow behaviour across the 6 by 7 edges is not read (AC-DTP-3); disabled days are not focusable and the skip rule is untested (AC-DTP-6); an invalid typed date is left out silently and OK stays enabled (AC-DTP-7); no month-year selector (AC-DTP-14); no docked variant (AC-DTP-13); English names only (AC-DTP-15); tooltips of the icon buttons not read (AC-DTP-10 unmeasured); not built: range picker |
| tess-shell | none | absent |
| tre | `tre:docs/reference/node.md` (`current`, `selected`, `live`, `describedby`) | not applicable: the engine offers `current="date"`, `selected` and live regions; no `grid`, `row`, `gridcell`, `columnheader` roles and no `aria-modal`; candidate requests: grid roles and a modal flag |

Evidence: `tess-ui:docs/components/date-pickers.md` ("Not built: a range picker, a docked picker under a field, month and year selectors, Page Up and Page Down by month, and the names of the months and days in another language").

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Day pitch 40, 32, 28 dp and dialog width 328, 280, 280 dp (MD3 modal 360 dp, 48 dp cells in docked) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Fixed six-row grid | the dialog keeps its height; the number of rows MD3 shows is not verified #needs-verification | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (layout only) |
| Keyboard model, grid roles and day names follow the APG date picker dialog | MD3 gives no keyboard rules | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Docked picker commits on selection; modal commits on OK | MD3 modal has OK and Cancel; docked has none | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Invalid typed date shows the field error and disables OK | WCAG 3.3.1 error identification; MD3 shows a field error only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule) |
| Range picker not specified | not built; no project use | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- Material Web tokens: [date picker modal](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-date-picker-modal.scss) (container 360 by 524 px, header 120 px, date container 40 px, today outline 1 px, year cell 72 by 36 px, corner extra large, colours `primary`, `on_primary`, `on_surface`, `on_surface_variant`), [docked](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-date-picker-docked.scss) (360 by 456 px, date container 48 px, state layer 40 px, header 64 px, corner large), [date input modal](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-date-input-modal.scss) (328 by 512 px) (verified 2026-11-21).
- [Material Components Android DatePicker](https://github.com/material-components/material-components-android/blob/master/docs/components/DatePicker.md): modal, docked and range variants, switch-to-keyboard input icon, today outline 1 dp.
- [WAI-ARIA Authoring Practices date picker dialog example](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/examples/datepicker-dialog/): keyboard table, grid roles, live month heading, `aria-current`, roving tab stop (verified 2026-11-21); [grid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.5.8, 3.3.1.
- The m3.material.io date picker page could not be fetched (script-rendered site); Material Web has no date picker component, only the token set.
- Code: `tess-ui:src/tess_ui/views/DatePicker_View.tdl`, `DatePickerDay_View.tdl`, `DatePicker_Stylesheet.tdl`, `tess-ui:docs/components/date-pickers.md`, `tre:docs/reference/node.md`.
