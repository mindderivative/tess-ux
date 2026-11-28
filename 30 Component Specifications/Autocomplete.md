---
title: Autocomplete
type: component
status: draft
owner: phil
created: 2026-11-28
updated: 2026-11-28
tags: [component, input, combobox, keyboard, desktop]
related: ["[[Text Field]]", "[[Choice Picker]]", "[[Search]]", "[[Menu]]", "[[Popup]]", "[[Active Descendant]]", "[[List]]", "[[Selection]]", "[[Empty States]]", "[[Font List]]", "[[Icon Picker]]", "[[Colour Picker]]", "[[Form Row]]", "[[Config App Layout]]", "[[Tooltip]]", "[[Keyboard Navigation]]", "[[Scrollbar and Scroll Container]]", "[[Focus Ring]]", "[[State Layers]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Typography]]", "[[Spacing and Density]]", "[[Accessibility Tree]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0029 Desktop density and type scale]]"]
depends_on: ["[[Text Field]]", "[[Popup]]", "[[ADR-0029 Desktop density and type scale]]"]
---

# Autocomplete

> [!info] Summary
> A text field with a popup list of suggestions that narrows as the user types (the combo box): the user types to find an option in a long closed set, or types a free value and may take a suggestion. Material Design 3 has no combo box (it has the menu-based select, [[Choice Picker]], and the [[Search]] view); the baseline is the WAI-ARIA Authoring Practices combobox pattern with a listbox popup. Status in code: absent in every project.

## Purpose

Let a person choose one value from a set too long to scan (more than about 12 options) by typing a few letters, without leaving the keyboard, and see the value in the field afterwards. In the configuration application it is the control for the token, font and icon pickers, the Role of a block (24 values) and "Move block into".

## When to use and not

- Use when: the set has more than about 12 options, or the person knows part of the value and typing is faster than scrolling; or the value is free text with helpful suggestions.
- Do not use when: the set has 12 options or fewer ([[Choice Picker]]); the choices are commands ([[Menu]]); the control searches and runs a query, not a value ([[Search]]); the field only filters the visible rows of a list in place ([[Text Field]] with role `searchbox` and the list below it).
- A Choice Picker with a filter field (more than 12 options) is the same job through a button; the Autocomplete replaces it where the control is a field in a row and the value is a name the person types ([[Choice Picker]] keeps the swatch and hint dialog form).

## Anatomy

1. Field: a single-line [[Text Field]] (outlined at compact and dense) holding the typed text or the chosen label. Role `combobox`.
2. Chevron button (optional): opens and closes the list; not a Tab stop and not read separately; hidden at dense when the field is narrower than 120 dp.
3. Clear button (optional): empties the field; shown only with text, not a Tab stop.
4. Popup: an anchored [[Popup]] holding the list, role `listbox`.
5. Option row: a label, with an optional leading visual (a colour swatch, an icon, a font sample) and an optional hint line; the matched part of the label is emphasised.
6. Empty note: "No matches" when nothing matches ([[Empty States]]).
7. Status: a polite live region that announces the number of results.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Strict | the value must be one of the options (Role, token, Move into) | free text is only a query; leaving the field with text that is not an option restores the last value |
| Free | the value may be any text; the list only suggests | the typed text is the value unless an option is accepted |
| Inline completion (optional) | a prefix match that is unambiguous | the rest of the first match is shown selected after the caret; Strict and Free both |

Row templates (the rows follow the content, the shell of field and popup is the same): label only; label and hint; swatch and label (token, colour); icon and label ([[Icon Picker]]); label in its own font ([[Font List]]).

## States

| State | Visual change | Token values |
|---|---|---|
| Field rest | outline, label and value `on_surface` | [[Text Field]] outlined |
| Field hover | outline `on_surface` | [[Text Field]] |
| Field focus | outline 2 dp `primary`, focus ring per [[Focus Ring]] | [[Text Field]] |
| Open | the popup shown; `expanded` true; the field keeps keyboard focus | |
| Option rest | transparent, label `on_surface` | |
| Option hover | state layer `on_surface` | 8 percent ([[State Layers]]) |
| Option active (the active descendant) | state layer and an inner ring | 10 percent; ring [[Focus Ring]] |
| Option selected (the current value) | container `secondary_container`, label `on_secondary_container`, a check at the end | verified tokens |
| Option disabled | label and visual at 38 percent; skipped by keys; not pickable | 38 percent |
| Field disabled | does not take focus or open | 38 percent |
| Invalid | Strict: the text is not an option and the field was left; outline and helper text `error` | [[Text Field]] error state |
| No matches | the empty note in the popup, `on_surface_variant` | |

The pointer highlight and the keyboard active row are one: moving the pointer onto a row makes it the active row, arrow keys move it away.

## Tokens used

[[Text Field]] (field container, label, helper); [[Menu]] (popup container `surface_container`, elevation level 2, `shape.extra_small`, selected row `secondary_container`); [[State Layers]]; [[Typography]] (`density.font_body` for the field and the rows, `body_small` for the hint) and [[Colour Roles]], [[Shape]], [[Elevation]] as named there.

## Sizing and density

| Measure | default | compact | dense |
|---|---|---|---|
| Field height | 40 | 32 | 28 |
| Option row height (label only) | 40 | 32 | 28 |
| Row with hint | 56 | 48 | 40 |
| Visible rows before the list scrolls | 8 | 8 | 8 |
| Text role | `body_large` | `body_medium` | `body_dense` |

The popup is at least as wide as the field and at most 360 dp (a font or icon template may be wider, never past the window less the 8 dp edge margin). The field follows the [[Text Field]] density rules ([[ADR-0029 Desktop density and type scale]]); the popup takes the density of its opener ([[Spacing and Density]]). Hit areas are at least 24 by 24 dp.

## Dimensions and defaults

Values come from [[Text Field]] and [[Menu]]; the rows and the hint rows are Tesserae choices #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| field | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], [[Text Field]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| field | padding | `density.field_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 8 0 8 | [[Spacing and Density]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| field | margin | - | N/A: the form row places the field | N/A: as in Default | N/A: as in Default | [[Form Row]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| field | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] (text to chevron and clear button) | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| field | border width | - | 1 (2 when focused) | 1 (2 when focused) | 1 (2 when focused) | [[Text Field]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| field | border color | `outline` | `outline` (`primary` focused, `error` invalid) | `outline` (`primary` focused, `error` invalid) | `outline` (`primary` focused, `error` invalid) | [[Text Field]], [[Colour Roles]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| field | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]], [[Text Field]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| field | font | `density.font_body` | 16/24/400/0.5 | 14/20/400/0.25 | 13/18/400/0.25 | [[Typography]], [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| field | icon size | `density.icon_button_icon` | 24 | 20 | 18 | [[Iconography]], [[Spacing and Density]] (chevron and clear) | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| field | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| popup | height | - | N/A: content-sized, at most 8 rows, then it scrolls | N/A: as in Default | N/A: as in Default | [[Menu]] Layout and overflow | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| popup | padding | `space.3`, `space.2` | 8 0 8 0 | 4 0 4 0 | 4 0 4 0 | [[Menu]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| popup | margin | - | N/A: the popup is placed 0 dp under the field and kept 8 dp inside the window | N/A: as in Default | N/A: as in Default | [[Popup]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| popup | border width | - | 0 | 0 | 0 | [[Menu]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| popup | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]], [[Menu]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| popup | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]], [[Menu]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| option row | height | `density.menu_item_height` | 40 | 32 | 28 | [[Spacing and Density]], [[Menu Item]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| option row | padding | `density.row_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 4 0 4 | [[Spacing and Density]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| option row | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| option row | font | `density.font_body` | 16/24/400/0.5 | 14/20/400/0.25 | 13/18/400/0.25 | [[Typography]], [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| option row | icon size | `density.icon_button_icon` | 24 | 20 | 18 | [[Iconography]] (leading icon template) | tess-ui: n/a: component absent, a new view; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |

## Layout and overflow

- The popup opens under the field, start-aligned, at least as wide as the field, and flips above when there is no room below and more above, then slides to stay 8 dp inside the window ([[Popup]], [[Menu]]).
- More than 8 rows scroll with the scrollbar of [[ADR-0003 Scrollbar rule]]; the active row is scrolled into view by the keys.
- A label wider than the row ends in an ellipsis; the accessible name keeps the full label. A hint is at most 2 lines.
- Matching is by containing text, case-insensitive; the matched characters of the label are emphasised (weight 500, not colour alone). Options are shown in the order of the source set, not by relevance, unless the source says otherwise.

## Behaviour

- Pointer: a press in the field places the caret and, when the field has focus and a list exists, opens it; a press on the chevron toggles it; a press on a row picks it and closes; a press outside closes the popup and keeps the text. Hover on a row makes it the active row.
- Typing: each change of the text narrows the list at once (no delay) and opens it when closed; with no match the popup shows "No matches". The active row is none while the person types, unless Inline completion is on (then the first match).
- Keyboard (the field keeps focus; the active row is exposed as the active descendant, [[Active Descendant]]):

| Key | Result |
|---|---|
| Down | open the list if closed and make the first enabled row active (the selected row when there is one); with the list open, the next enabled row (no wrap; Alt+Down opens without moving) |
| Up | the last enabled row when the list was closed; otherwise the previous enabled row; from the first row it returns to none |
| Page Down, Page Up | by one visible page of rows |
| Home, End | move the caret in the text (the list keeps its active row) |
| Enter | with an active row: pick it, close, put the label in the field; with none: Strict keeps the last value and closes; Free takes the typed text as the value |
| Tab | Strict: when the text equals an option label (case-insensitive) pick it, else restore the last value; Free: keep the text; then focus leaves; Tab never picks the active row unless the active row was chosen by an arrow key |
| Escape | list open: close it and keep the text; list closed: Strict restores the last value and selects the text, Free leaves it; the key is not consumed when nothing changed |
| Printable character | edits the text |

- Picking writes the value and calls the change handler once; the field shows the label; focus stays in the field. In Strict, text that is not an option never becomes the value.
- Empty field: Strict with a required value shows the placeholder; clearing with the clear button leaves the field empty and the value unset (or the default).
- Touch: rows keep a 48 dp hit area in a touch context.

## Tooltip and overlay behaviour

The field shows a tooltip only for a truncated value ([[Tooltip]]); the chevron button has none (it is not a separate control for assistive technology). The popup is a non-modal [[Popup]]: no scrim, outside press closes and is consumed, focus never leaves the field, one popup at a time.

## Motion

None required. Where a project animates, open uses a fade of `short3` to `short4` and close is instant ([[Menu]]); reduced motion makes both instant.

## Accessibility

- The field has role `combobox`, a name (the Form Row label), the current value as its text, `expanded` matching the popup, `haspopup` listbox, `controls` the listbox and, while a row is active, `active_descendant` of that row (the engine has a settable `active_descendant`, TRE-REQ-023; not checked with a screen reader, [[Active Descendant]]); autocomplete mode `list` (or `both` with Inline completion).
- The popup has role `listbox` and a name; rows have role `option`, a name equal to the label, a description equal to the hint, and `selected` for the current value only.
- A polite status announces the count after the list changes, once, after 300 ms of quiet ("12 results", "No matches"), not on every keystroke.
- Keys follow the APG combobox pattern (Sources); the Home and End keys move the caret because the field is a text input.
- Contrast: label `on_surface` on the container, selected label on `secondary_container` and hint on `surface_container` at least 4.5:1; the emphasis is weight, not colour.
- Target size: field and rows at least 24 dp high; no keyboard trap: Tab and Escape leave.

## Dark and light

All roles come from the scheme ([[Theme Following the System]]).

## Defaults

Strict, no inline completion, no chevron at dense, open on typing and on Down, 8 rows visible, contains-matching, placeholder "Type to search", level per project.

## Acceptance criteria

- [ ] AC-ACP-1 (geometry check, density): at default, compact and dense the field is 40, 32 and 28 dp high, a label-only row 40, 32 and 28 dp, a row with a hint 56, 48 and 40 dp; the text roles are `body_large`, `body_medium` and `body_dense`. Pass: bounds and roles equal at scale 1.0 and 2.0.
- [ ] AC-ACP-2 (scripted input, filter): with the options Apple, Avocado, Banana, typing "a" shows Apple, Avocado and Banana (contains), "av" shows Avocado, "zzz" shows "No matches"; the list updates in the frame of the keystroke and the matched letters are weight 500. Pass: rows after each key equal.
- [ ] AC-ACP-3 (scripted input, arrows): Down on a closed field opens the list with the first enabled row active (the selected row when there is one); Down moves to the next row and stops at the last; Up from the first row makes the active row none; disabled rows are skipped; Home and End move the caret and leave the active row. Pass: active row after each key equal.
- [ ] AC-ACP-4 (scripted input, pick): Enter on an active row writes its label into the field, calls the change handler once, closes the list and leaves focus in the field; a press on a row does the same. Pass: value, call count, layer count, focus owner equal.
- [ ] AC-ACP-5 (scripted input, Strict): with the value "Banana", typing "xyz" and pressing Tab leaves the value "Banana" and the text "Banana"; typing "apple" and Tab picks Apple (equal ignoring case); Enter with no active row keeps the value. Pass: value after each step.
- [ ] AC-ACP-6 (scripted input, Free): typing "kiwi" and Enter makes "kiwi" the value; with Apple active by Down and Enter the value is "Apple". Pass: value equal.
- [ ] AC-ACP-7 (scripted input, Escape): with the list open Escape closes it and keeps the text; Escape again in Strict restores the last value; in Free leaves the text; Escape with nothing to undo is not consumed. Pass: text, layer count and consumed flag equal.
- [ ] AC-ACP-8 (AT tree assertion): the field has role `combobox`, `expanded`, `haspopup` listbox, `controls` the listbox and `active_descendant` equal to the active row; the popup has role `listbox`; rows have `option`, name, description and `selected` for the value only; the chevron and clear buttons are not in the tree as separate stops. Pass: property equality for 24 options.
- [ ] AC-ACP-9 (scripted input, announcement): typing "a" then "av" within 300 ms announces once, after the quiet period, "1 result"; clearing the text announces the full count once; "zzz" announces "No matches" once. Pass: announcement count and text equal.
- [ ] AC-ACP-10 (geometry check, popup): the popup is at least as wide as the field, at most 360 dp (or the window less 8 dp), opens under the field with 0 dp gap and flips above when below has less room than the list and above has more; with 24 options it shows 8 rows and a scrollbar and the active row stays visible by Down. Pass: rectangles equal.
- [ ] AC-ACP-11 (scripted input, focus): in every case above keyboard focus stays on the field; a press on a row, on the chevron or on the scrollbar thumb does not move it; Tab leaves in one press. Pass: focus owner after each step equal.
- [ ] AC-ACP-12 (scripted input, Inline completion): with it on and the options Apple, Avocado, typing "ap" shows "Apple" with "ple" selected; Backspace removes the selected part only; Enter accepts "Apple". Without it nothing is added to the text. Pass: text and selection equal.
- [ ] AC-ACP-13 (pixel check, states): the row under hover is `on_surface` at 8 percent over the container, the active row 10 percent with the ring, the selected row `secondary_container` with a check; field focus outline 2 dp `primary`; the invalid Strict field outline `error`. Pass: pixels within 1 per channel.
- [ ] AC-ACP-14 (contrast script): label, selected label and hint at least 4.5 to 1, the focus outline at least 3 to 1, in light and dark. Pass: ratios at or above the limits.
- [ ] AC-ACP-15 (review, config app): the token, font and icon pickers, the Role key and "Move block into" are Autocomplete controls with the row templates above; the Role key lists its 24 values in the source order. Pass: reviewer finds each, and no Choice Picker with a filter used for them.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | none (text search of `src`, `apps` and `docs` on `origin/main` finds the role name `combobox` in `tess-ui:src/tess_ui/a11y.py` and no component); the config app opens its token, font and icon pickers and its Role and Move choices as dialogs or lists | absent. Read at `origin/main`, nothing run |
| tess-shell | none | absent; the shell launcher's search list is the nearest ([[Search]], [[Launcher]]) |
| tre | `tre:docs/reference/node.md` (role list), `tre:LOG.md` (TRE-REQ-023) | the role `combobox` is in the 0.6.11 role list; a settable `active_descendant` exists. Missing, not requested yet: nothing known; a screen reader check of the active descendant is open ([[Active Descendant]]) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A combo box (field with a filtered list), which MD3 does not have | the configuration application needs to pick one of many names by typing; MD3 offers the select and the search view only | [[ADR-0029 Desktop density and type scale]] |
| Field 40, 32 and 28 dp and rows 40, 32 and 28 dp | desktop density | [[ADR-0029 Desktop density and type scale]] |

## Sources

- WAI-ARIA Authoring Practices, combobox pattern (list autocomplete with a listbox popup; Down and Alt+Down open; Up; Enter accepts; Escape closes then clears; Home and End move the caret; focus stays on the field and the active row is `aria-activedescendant`): `https://www.w3.org/WAI/ARIA/apg/patterns/combobox/`; list autocomplete example: `https://www.w3.org/WAI/ARIA/apg/patterns/combobox/examples/combobox-autocomplete-list/`.
- [[Text Field]], [[Menu]], [[Choice Picker]], [[Active Descendant]]; WCAG 2.2 SC 2.1.2 and 2.5.8. m3.material.io is not readable by tools; the combobox keys are taken from the APG pattern, not re-read in this session #needs-verification.
