---
title: Choice Picker
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, picker, choice, popup, listbox, keyboard]
related: ["[[Menu]]", "[[Popup]]", "[[Dialog]]", "[[List]]", "[[List Item]]", "[[Button]]", "[[Text Field]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Form Row]]", "[[Font List]]", "[[Icon Picker]]", "[[Colour Picker]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[State Layers]]", "[[Colour Roles]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Menu]]", "[[Popup]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]"]
---

# Choice Picker

> [!info] Summary
> A control that shows the current choice on a button and lets the person pick one of a known set of options, each with a label, an optional colour swatch and an optional hint. Material Design 3 counterpart: [Menus](https://m3.material.io/components/menus/overview) used as a select (Material Web `md-outlined-select`). The config app builds it as a modal dialog of option rows; this note specifies the anchored popup form as the target and records the dialog form as built. Source of truth in code: the last section.

## Purpose

Choose exactly one value from a closed set (an enum key, a unit, a mode) and see the value without opening anything.

## When to use and not

- Use when: the set is closed, has 2 to about 12 options, and each option may need a hint to explain it.
- Do not use when: the set is open or long and searchable ([[Font List]], [[Icon Picker]]); the value is a colour ([[Colour Picker]]); the choices are commands ([[Menu]]); there are 2 options that read as on and off ([[Switch]]).
- Over about 12 options the picker adds a search field (filter, specified below).

## Anatomy

1. Button: outlined control showing the current option label (and swatch) and a chevron; the form row label sits outside ([[Form Row]]).
2. Overlay: anchored [[Popup]] below or above the button (target), or a modal [[Dialog]] with a Cancel action (built).
3. Filter field (more than 12 options): [[Text Field]] at the top of the overlay.
4. List: role `listbox` of option rows with a [[Scrollbar and Scroll Container]].
5. Option row: optional 20 dp colour swatch (4 dp corners, 1 dp `outline`), label (`body_medium`), hint (`body_small`, `on_surface_variant`, at most 2 lines).
6. Selected mark: filled row `secondary_container` plus a check icon at the end edge (the check is specified; the fill alone is built).
7. Empty note "No matches" when the filter finds nothing.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Anchored popup | default target; 12 options or fewer | opens at the button, width equals the button width at least |
| Dialog | options with long hints, narrow windows (built in the config app) | modal, 440 dp wide, maximum 400 dp high, Cancel action |
| With filter | more than 12 options | filter field with focus on open |
| With swatch | colour options | a 20 dp swatch before the label |

## States

| State | Visual change | Token values |
|---|---|---|
| Option rest | transparent | label `on_surface` |
| Option hover | state layer | `on_surface` 8 percent ([[State Layers]]) |
| Option cursor | filled and ring on focus | `surface_container_highest`; [[Focus Ring]] |
| Option selected | filled, label `on_secondary_container`, check | `secondary_container` |
| Option disabled | skipped by keys, not pickable | 0.38 on content |
| Button rest, hover, focus, pressed, open | outline, layers, ring, `Expanded` true | `outline`; 8, 10, 10 percent |
| Button disabled | does not open | 0.38 |
| No value | the default or "choose" placeholder in `on_surface_variant` | `on_surface_variant` |

## Tokens used

[[Colour Roles]], [[Typography]] (`body_medium`, `body_small`), [[Shape]] (rows 8 dp, popup 12 dp, dialog 28 dp), [[Elevation]] (popup level 2, dialog level 3), [[Spacing and Density]], [[State Layers]], [[Focus Ring]]. Surface of the popup follows [[Menu]].

## Sizing and density

| Part | default | compact | dense | Code today |
|---|---|---|---|---|
| Button height | 40 | 32 | 28 | the config app's `xs` button |
| Option row, label only | 40 | 32 | 24 | label row padding 8 around a 20 dp line (about 36) |
| Option row with a hint | label row plus hint lines, at least the row height | same | same | padding 8, hint up to 2 lines |
| Row horizontal padding | 12 | 8 | 4 | 8 |
| Icon (swatch) to label gap | 8 | 8 | 4 | 8 |
| Popup width | button width, at least 160, at most 360 | same | same | not built |
| Dialog width, height | 440, 400 maximum | 440, 400 | 440, 400 | 440, 400 |
| Label column | the longest label, at most 40 percent of the row width | same | same | fixed 150 |

Hit area at least 24 by 24 dp at every density ([[ADR-0002 Desktop density levels and target sizes]]).

## Layout and overflow

- Label: one line, end ellipsis, minimum width 0. Hint: wraps to at most 2 lines, then end ellipsis; the full hint is the accessible description ([[10 Layout Overflow and Scrolling]]).
- The list scrolls vertically with a visible scrollbar when the content exceeds the popup or dialog maximum height ([[ADR-0003 Scrollbar rule]]); no horizontal scroll.
- The popup flips above the button when there is no room below; its maximum height is the free window height minus 8 dp margin.
- The button shows the label of the value on one line with end ellipsis; a value that is not an option shows as text with a warning state and nothing selected.
- Text and swatch are vertically centred in the row.

## Behaviour

- Pointer: a press on the button opens; a press on a row picks and closes; a press outside or Escape closes without a change.
- Keyboard. The button opens with Enter, Space or Alt+Down; on open focus is on the selected row, else the first enabled row (or the filter field when present).

| Key | Action |
|---|---|
| Down, Up | next, previous enabled option (no wrap) |
| Home, End | first, last option |
| Page Up, Page Down | by one visible page |
| Enter, Space | pick the option under the cursor and close |
| Printable characters | focus the next option whose label starts with the text; buffer resets after 1 s (Material Web select uses 200 ms #needs-verification) |
| Escape | close, focus to the button |
| Tab | close and move on |

- A pick writes the value, calls the change handler once and returns focus to the button.
- Touch: option rows keep a 48 dp hit area in a touch context.

## Tooltip and overlay behaviour

Tooltips belong to controls only ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]): the button shows the hint of the current option; an option row shows its hint as supporting text, not as a tooltip, so no row carries a tooltip; a truncated label shows its text on the label only. The overlay is a [[Popup]] (anchored) or a modal [[Dialog]] with a [[Scrim]]; Escape closes either ([[12 Overlays]]). Focus returns to the button on close.

## Motion

The popup fades in 150 ms and out in 100 ms; the dialog follows [[Dialog]] ([[Motion]]). Reduced motion: 0 ms.

## Accessibility

- The button has role `button` with `haspopup` listbox, `expanded`, and the name "Label: current option". The list is `listbox` named by the title ("Choose Label") with rows `option`, `selected` for the value, described by the hint (code today: `list` and `listitem`, name only). The filter is a `searchbox`.
- Selection announcements: moving the cursor announces label, hint and "n of N"; a pick announces "label selected"; filtering announces "n matches" or "No matches" once (role `status`, polite).
- Keys: the table above; every pointer action has a key equivalent.
- Contrast: label on `secondary_container` uses `on_secondary_container` at least 4.5:1; hint `on_surface_variant` on the surface at least 4.5:1; the swatch border `outline` at least 3:1 ([[Colour Roles]]).
- Target size at least 24 by 24 dp at every density.
- The value is never carried by the swatch alone: the label names it.

## Dark and light

Roles only ([[Theme Following the System]]); a swatch shows the resolved colour of the option for the active scheme.

## Defaults

Anchored popup, no filter at 12 options or fewer, no wrap, placeholder "choose" until a value exists, level per project.

## Acceptance criteria

- [ ] AC-CHO-1 (geometry check): at default, compact and dense the button is 40, 32 and 28 dp high and a label-only row is 40, 32 and 24 dp high, at scale 1.0 and 2.0.
- [ ] AC-CHO-2 (scripted input): Enter, Space and Alt+Down on the focused button open the overlay with focus on the selected row; with no value, on the first enabled row.
- [ ] AC-CHO-3 (scripted input): with 6 options Down, Up, Home, End and Page Down move by one, one, to 0, to 5, to the last row of the page and never wrap or leave the list; disabled options are skipped.
- [ ] AC-CHO-4 (scripted input): Enter and Space on the cursor row write the value, call the change handler once, close the overlay and put focus on the button within one frame; Escape closes without a write.
- [ ] AC-CHO-5 (scripted input): typing "co" within 1 s focuses the next option whose label starts with "co"; after 1 s idle the buffer is empty.
- [ ] AC-CHO-6 (AT tree assertion): the button has `haspopup` and `expanded` matching the overlay; the list has role `listbox` and a name; rows have role `option`, a name equal to the label, a description equal to the hint and `selected` for the value only.
- [ ] AC-CHO-7 (scripted input): with 13 or more options a filter field takes focus on open; typing "mode" keeps options whose label contains it in any case; "zzz" shows "No matches" and announces it once.
- [ ] AC-CHO-8 (pixel check): a label 300 dp wide in a 100 dp cell ends in `…`; a hint of 5 lines shows 2 lines, the second ending in `…`; no ink leaves the row.
- [ ] AC-CHO-9 (geometry check): content taller than the overlay maximum shows a vertical scrollbar thumb of at least the minimum thumb length; the cursor row is scrolled into view by Down.
- [ ] AC-CHO-10 (scripted input): a tooltip appears on the button after 500 ms hover and at once on focus, no tooltip appears over an option row or the overlay background, and Escape, a press, a scroll and leaving remove it.
- [ ] AC-CHO-11 (contrast script): the selected row label on `secondary_container` is at least 4.5:1 and the hint on `surface_container` at least 4.5:1 in light and dark, standard contrast.
- [ ] AC-CHO-12 (geometry check): the anchored popup is at least as wide as the button, at most 360 dp, and flips above the button when below-space is less than the list height and above-space is larger.
- [ ] AC-CHO-13 (review): the note records the built dialog form and the not built anchored form, filter and selected check in Status in code.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (parts `picker`, `picker_list`, `option`), `tess-ui:apps/shell_config/src/tess_shell_config/formcontrol.py` (`pick_option`), `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`ChoiceWidget`) | partly meets. A modal Dialog (440 by at most 400) lists options as `listitem` rows with `selected`, swatch, label (fixed 150 dp) and a hint of at most 2 lines; a press picks and closes; Cancel closes. Passes AC-CHO-4 for pointer and Cancel, AC-CHO-8 in part. Fails AC-CHO-1 (no density), AC-CHO-2 and AC-CHO-3 and AC-CHO-5 (no arrow, Home, End, type-ahead keys in `picker_list`), AC-CHO-6 (roles `list` and `listitem`, no `haspopup`), AC-CHO-7 (no filter), AC-CHO-9 (no scrollbar rule applied to the list), AC-CHO-10 (no button tooltip), AC-CHO-12 (no anchored form) |
| tess-ui | the toolkit has no choice picker view; the toolkit [[Menu]] and Dialog are the parts | absent as a shipped view |
| tess-shell | none | absent: the shell has a Menu only |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Built as a modal Dialog, not an anchored menu | the config app picks options with long hints in a narrow window; recorded as built, anchored form is the target | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hint as supporting text, not as a tooltip | tooltips are for controls only | [[ADR-0004 Tooltip rule]] |
| Rows 40, 32, 24 dp (Material Web menu item 48 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Type-ahead buffer 1 s (Material Web 200 ms) | consistent with [[List]] | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- tess-ui config app: `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` lines 1116 to 1175, `tess-ui:apps/shell_config/src/tess_shell_config/formcontrol.py`, `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py`.
- Material Web select https://raw.githubusercontent.com/material-components/material-web/main/docs/components/select.md (typeahead delay property) and menu https://raw.githubusercontent.com/material-components/material-web/main/docs/components/menu.md (type-ahead 200 ms default; verified 2026-11-21). The MD3 menus page https://m3.material.io/components/menus/overview is a JavaScript app and is not readable.
- WAI-ARIA APG listbox https://www.w3.org/WAI/ARIA/apg/patterns/listbox/; WCAG 2.2 SC 1.4.11, 2.5.8, 4.1.3 (links in [[File Dialog]]).
- Alt+Down to open a select-like button is the APG combobox and menu button convention, not re-read #needs-verification.
