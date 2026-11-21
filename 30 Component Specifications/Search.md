---
title: Search
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, input, search]
related: ["[[Text Field]]", "[[Icon Button]]", "[[List]]", "[[List Item]]", "[[Popup]]", "[[Menu]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Empty State]]", "[[Active Descendant]]", "[[Launcher]]", "[[Applications Module]]", "[[Keyboard Navigation]]", "[[Validation]]", "[[Forms and Settings]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[State Layers]]", "[[Focus Ring]]", "[[Motion]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Text Field]]", "[[Icon Button]]", "[[List]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Search

> [!info] Summary
> The search bar (a rounded field that starts a search) and the search view (the panel under it that shows suggestions, history and results): the Material Design 3 (MD3) [search](https://m3.material.io/components/search/overview) component. Source of truth in code: see the last section.

## Purpose

The user types a query and picks a result or runs a search. The bar is the entry point; the view lists what matches while the query changes. The launcher and any filterable list are built on this pair ([[Launcher]], [[Applications Module]]).

## When to use and not

- Use when: the user searches a large set (applications, settings keys, files) and wants live suggestions or results.
- Do not use when: the field only filters the visible rows of a short list in place (use a [[Text Field]] with role `searchbox` and the list below it, the search field variant here), the value is any other text ([[Text Field]]), or the choices are few and known (use a [[Menu]]).

## Anatomy

Search bar:

1. Container: pill with the container colour and elevation.
2. Leading icon: a search glass, or a menu button (opens a drawer). While the search is active it is a back arrow.
3. Input: the query text, placeholder, caret and selection.
4. Clear button: shown once there is text.
5. Trailing icons (optional): a microphone or other actions, shown while the field is empty.
6. Avatar (optional).

Search view (docked):

7. Panel: surface under the bar with 28 dp corners.
8. Result count: a visually small line that announces the number of results.
9. Rows: [[List Item]] rows (history, suggestions, results) with optional supporting text and icon, in a scroll area.
10. Empty text: shown when there is a query and no rows ([[Empty State]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Search bar | primary search surface of a window or panel | pill, elevation level 3 in tess-ui, 56 dp at default density |
| Search field | search inside a toolbar, a list header or a dense panel | an outlined or filled [[Text Field]] with a leading search icon, a clear button and role `searchbox`; no pill, no elevation; Escape clears |
| Docked search view | results under the bar on desktop | panel under the bar, same width as the bar, maximum height 400 dp |
| Full-screen search view | compact windows (width below 600 dp, [[Spacing and Density]]) | the view replaces the screen; not built in tess-ui |
| Frosted | surfaces over imagery | container colour at 72 percent plus a 20 dp backdrop blur; text contrast must still pass on the worst backdrop (AC-SRB-12) |

## States

State layers come from [[State Layers]], focus from [[Focus Ring]]. Values below are the tess-ui values (`tess-ui:src/tess_ui/views/SearchBar_Stylesheet.tdl`, `SearchView_Stylesheet.tdl`).

| State | Visual change | Token values |
|---|---|---|
| Rest | bar `surface_container_high`, elevation 3, input text `on_surface`, leading icon `on_surface`, clear and trailing icons `on_surface_variant`, placeholder `on_surface_variant` | stylesheet |
| Hover | 8 percent layer of `on_surface` on the bar container; icon buttons their own 8 percent layer | [[State Layers]] |
| Focus (input, pointer or keyboard) | caret `primary`; the bar draws the focus ring 3 dp `secondary` offset 2 dp when focus is by keyboard | [[Focus Ring]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Focus (icon button, keyboard) | 10 percent layer plus focus ring | [[Icon Button]] |
| Active (search under way) | the leading icon becomes a back arrow; the view is open | `Active` and `Open` bound |
| Pressed (icon button) | 10 percent layer | [[State Layers]] |
| Has text | clear button visible; trailing icons hidden | design |
| Results shown | view panel `surface_container_high`, corners 28 dp | stylesheet |
| Empty result | empty text `on_surface_variant`, 16 dp horizontal padding | stylesheet |
| Disabled | bar and icons `on_surface` at 38 percent; no focus, no input | [[State Layers]] |

## Tokens used

- Colour: roles above ([[Colour Roles]]); no literal colour.
- Type: input `body_large` at default density, `body_medium` at compact and dense; result count `label_small`; empty text and rows per [[List Item]] ([[Typography]]).
- Shape: bar `corner-full`; view panel 28 dp (`corner-extra-large`) ([[Shape]]).
- Elevation: bar level 3 in tess-ui (the MD3 value could not be read, #needs-verification; a project may set level 0 and use an outline) ([[Elevation]]).
- Spacing and density: [[Spacing and Density]].

## Sizing and density

The bar keeps the MD3 56 dp at default density because it is the primary entry of a window; compact and dense shrink it so that it fits panels and toolbars ([[ADR-0002 Desktop density levels and target sizes]]).

| Level | Bar height | Leading and trailing icon button | Icon | Horizontal padding | Input type | Panel row height |
|---|---|---|---|---|---|---|
| default | 56 dp | 48 dp | 24 dp | 4 dp left, 12 dp right | `body_large` | 40 dp |
| compact | 40 dp | 32 dp | 20 dp | 4 dp | `body_medium` | 32 dp |
| dense | 32 dp | 28 dp | 20 dp | 4 dp | `body_medium` | 24 dp |

- The default row matches tess-ui (56 dp bar, 48 dp buttons, 24 dp icons, padding 4 and 12). Compact and dense are Tesserae design choices #needs-verification-as-design-choice: bar height equals the icon button container plus 8 dp at compact and 4 dp at dense so the pill keeps a margin around its buttons.
- Search field variant: the height of a single-line [[Text Field]] (40, 32, 28 dp).
- The view panel has the width of the bar (tess-ui `Width` default 360 dp), a maximum height of 400 dp (`Max_Height`), vertical padding 8 dp; rows beyond scroll with the scrollbar of [[ADR-0003 Scrollbar rule]]. Panel row heights are the [[List Item]] heights (40, 32, 24 dp) from [[Spacing and Density]].
- Hit area at least 24 by 24 dp at every density, 48 by 48 dp in a touch context.
- The bar's minimum width is 240 dp (input at least 120 dp after the icons) #needs-verification-as-design-choice; MD3 Android gives the bar a maximum width option, no minimum ([Material Components Android search](https://github.com/material-components/material-components-android/blob/master/docs/components/Search.md)).

## Layout and overflow

- The input is one line and never wraps. Overlong text: the unfocused bar truncates the query with an ellipsis; the focused input scrolls the caret into view ([[Text Field]], [[10 Layout Overflow and Scrolling]]).
- Input has `min-width: 0` so the trailing icons never leave the bar.
- Result rows are single-line with an ellipsis and an optional second line of supporting text, as [[List Item]]. Rows are selectable text only where the row says so; the full value appears in the row tooltip when truncated ([[ADR-0004 Tooltip rule]]: the tooltip is on the row's text control, not the panel).
- Vertical centring of the query: the line box is centred in the bar by construction (AC-DEN-9).
- The panel opens below the bar; when there is not enough room below it opens above, and it never leaves the window ([[12 Overlays]]).

## Behaviour

- Pointer: a press on the bar focuses the input and activates the search; a press on the leading icon runs its action (focus the input for the glass, `On_Leading` for the menu); a press on the back arrow deactivates and closes the view; a press on the clear button empties the query and keeps focus in the input; a press on a row chooses it, closes the view and sets `Chosen`; a press outside the bar and the view closes the view.
- Keyboard (focus in the input):

| Keys | Result |
|---|---|
| Printable keys | edit the query; the search activates and the view opens on the first key (tess-ui sets `Active` on any key except Escape) |
| Enter | run the search (`On_Search`); when a result row is the active row, choose it |
| Down, Up | move the active row in the view (focus stays in the input, rows are exposed as the active descendant, [[Active Descendant]]); Down from the input with the view closed opens it |
| Home, End | caret to the line start and end, as [[Text Field]]; Ctrl+Home, Ctrl+End move the active row to the first and the last row |
| Page Down, Page Up | move the active row by one viewport minus one row |
| Escape | 1st press: if the view is open, close it and keep the query; 2nd press: clear the query; 3rd press: deactivate the bar and return focus to where it was; in the search field variant a single Escape clears the query ([[Text Field]]) |
| Ctrl+A, Ctrl+C, Ctrl+X, Ctrl+V, Ctrl+Z | as [[Text Field]] |
| Tab | moves to the next control; the view closes |

- Focus handling: opening the view does not move focus; the input keeps it. Closing returns focus to the input. A global shortcut that focuses the bar is a project decision (tess-ui has none: "Not built: a keyboard shortcut that focuses the bar", `tess-ui:docs/components/search.md`; the spec asks every search bar that is the main entry of a window to expose Ctrl+F or Ctrl+K in the project's keyboard map, see [[Keyboard Navigation]]).
- Debounce: results update on each edit after at most 150 ms idle for local sets and 300 ms for remote sets, so a fast typist does not trigger a result list per key; the latest query always wins #needs-verification-as-design-choice.
- Result count: announced politely after the list settles, once per query change, not per key.
- Touch: a tap on the bar activates it and opens the platform keyboard; a 48 dp hit area for icon buttons in touch contexts; on compact windows the full-screen view is used.
- IME: composition text is shown inline; the results update on committed text only, not on the pre-edit string, so a half-composed word does not flash a result list; the candidate window follows the caret ([[Text Field]]).
- Validation hooks: a search query has no invalid value; a query that finds nothing is the empty state ([[Empty State]]), not an error. Patterns for filters, saved searches and errors from a search backend: [[Validation]] and [[Forms and Settings]].

## Tooltip and overlay behaviour

- The search view is a docked [[Popup]]-class overlay under the bar ([[12 Overlays]]): it does not trap focus, closes on Escape and on a press outside, and clips to the window, not to the scroll container.
- Tooltips: the leading, clear, trailing and avatar parts are icon buttons and carry a tooltip equal to their accessible name ("Search", "Menu", "Clear", "Back"); the bar container and the panel carry none ([[ADR-0004 Tooltip rule]]). A truncated result row shows the row's text in a tooltip on that row's text control.

## Motion

- Bar to back-arrow icon swap: 150 ms fade at most; MD3 animates a menu icon into a back arrow ([Material Components Android search](https://github.com/material-components/material-components-android/blob/master/docs/components/Search.md), "Menu to back arrow animation").
- View panel open: 200 ms fade and 8 dp slide down with `emphasized-decelerate`; close 150 ms with `emphasized-accelerate` ([[Motion]]) #needs-verification-as-design-choice.
- Reduced motion: no slide, no fade; the panel appears and disappears at once ([[14 Accessibility Basics]]).

## Accessibility

- The bar has role `group` named "Search" (tess-ui). The input has role `searchbox` ([WAI-ARIA searchbox](https://www.w3.org/TR/wai-aria-1.2/#searchbox)) named by the label, else the placeholder; tess-ui names it by the placeholder and leaves the role to the engine default (see Status in code).
- Where the app has a landmark structure, the bar or the field is wrapped in a `search` landmark ([WAI-ARIA search](https://www.w3.org/TR/wai-aria-1.2/#search)).
- The input is a combobox when the view is open: `expanded` true, `controls` the rows, active descendant set to the active row ([[Active Descendant]]; engine support is partial, TRE-REQ-023). Where active descendant is unavailable, the view is a separate focusable list and Down moves focus into it, Escape returns to the input.
- Buttons have role `button` and names "Search", "Menu", "Back", "Clear" and the trailing names; the icons are hidden from AT.
- The view group is named "Search results"; the count line is a polite live region ("5 results"); the empty text is announced the same way.
- Keys: the table above, compatible with the [APG combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/) (Down, Up, Enter, Escape).
- Contrast: input text 4.5 to 1 on the bar container; placeholder 4.5 to 1; icons 3 to 1; focus ring 3 to 1 ([WCAG 1.4.3, 1.4.11](https://www.w3.org/TR/WCAG22/)).
- See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Dark and light

All colours are roles; the frosted variant mixes the container role at 72 percent over the backdrop, so contrast is checked against the darkest and lightest backdrop the project allows. The control follows the system theme ([[Theme Following the System]]).

## Defaults

- Placeholder "Search"; leading icon a search glass; no trailing icons; no avatar; not frosted.
- Bar 56 dp at default density; compact 40 dp in config tools.
- View width equals the bar width (360 dp default), maximum height 400 dp, empty text "No results".

## Acceptance criteria

- [ ] AC-SRB-1 (token test): the bar height is 56, 40, 32 dp, the icon button containers 48, 32, 28 dp and icons 24, 20, 20 dp at default, compact, dense; the search field variant height is 40, 32, 28 dp. Pass: values equal.
- [ ] AC-SRB-2 (geometry check): the query's line box is centred vertically in the bar with space above and below differing by at most 1 px; icon buttons are centred vertically within 0.5 dp, at scale 1.0, 1.25, 2.0 (AC-DEN-9). Pass: within tolerance.
- [ ] AC-SRB-3 (geometry check): the bar's corner radius equals half its height (full) and the panel's corner radius is 28 dp. Pass: values equal.
- [ ] AC-SRB-4 (scripted input): focus the input and type "a": `Active` becomes true and the view opens; the clear button is visible; press the clear button: the query is empty, the input is focused, the view stays open. Pass: states equal.
- [ ] AC-SRB-5 (scripted input): with the view open and the query "ab", Escape closes the view and keeps the query; a second Escape clears the query; a third deactivates the bar and `Active` is false and focus returns to the previous control. In the search field variant one Escape clears the query. Pass: states after each key equal.
- [ ] AC-SRB-6 (scripted input): Down moves the active row from none to row 1, again to row 2; End with Ctrl moves to the last; Enter chooses it: `Chosen` equals its value and the view closes; the input keeps keyboard focus throughout. Pass: `Chosen` and focus equal.
- [ ] AC-SRB-7 (AT tree assertion): the input has role `searchbox` (or `combobox` with `expanded` while the view is open) and a non-empty name; the buttons have role `button` and the names Search or Menu, Clear, Back; the view group is named "Search results". Pass: all properties equal.
- [ ] AC-SRB-8 (AT tree assertion): after a query settles with 5 results a polite live region reads "5 results"; with none it reads the empty text; typing 10 keys in 1 s produces at most 1 announcement. Pass: announcement count and text equal.
- [ ] AC-SRB-9 (scripted input): with results exceeding the 400 dp panel height the rows scroll and a scrollbar exists; with fewer it does not ([[ADR-0003 Scrollbar rule]]); no row paints outside the panel. Pass: scrollbar presence and zero out-of-bounds pixels.
- [ ] AC-SRB-10 (scripted input): a press outside the bar and the view closes the view; a press inside the view on a row chooses it; the panel never lies outside the window at any bar position (opens above when below does not fit). Pass: panel bounds inside the window bounds.
- [ ] AC-SRB-11 (geometry check): a query at least 3 times wider than the input width shows an ellipsis when unfocused and a scrolled caret inside the content box when focused; the icons stay inside the bar. Pass: ellipsis present, caret inside, zero pixels outside the bar.
- [ ] AC-SRB-12 (contrast script): in light and dark, input text and placeholder on the bar container 4.5 to 1 or more, icons 3 to 1 or more; frosted: the same against the lightest and darkest allowed backdrop. Pass: ratios at or above the limits.
- [ ] AC-SRB-13 (token test): no literal colour in the stylesheets; every colour is a role or a role with an alpha (the 72 percent frosted container). Pass: every colour property is a role reference.
- [ ] AC-SRB-14 (geometry check): hover on the bar container for 600 ms shows no tooltip; hover on each icon button for 600 ms shows its name ([[ADR-0004 Tooltip rule]]). Pass: zero tooltips on the container and panel, one per icon button.
- [ ] AC-SRB-15 (scripted input): with an injected IME pre-edit string the results do not update; on commit they update once. Pass: result request count equals 0 during composition and 1 after commit (record `not testable` where the platform cannot be driven).
- [ ] AC-SRB-16 (scripted input): with the debounce set, 10 keystrokes 30 ms apart produce at most 2 result updates and the last update matches the final query. Pass: update count at most 2, last query equal.
- [ ] AC-SRB-17 (geometry check): the hit area of every icon button is at least 24 by 24 dp at each density (48 by 48 dp in a touch context). Pass: sizes at or above the limits.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/SearchBar_View.tdl`, `SearchBar_Stylesheet.tdl`, `SearchView_View.tdl`, `SearchView_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/search.py` | partly meets: bar 56 dp pill, elevation 3, 48 dp buttons with 24 dp icons, back arrow, clear button, trailing icons, avatar, frosted variant, panel with 28 dp corners and 400 dp maximum height, count and empty text, Escape and outside press close the view exist (AC-SRB-3, AC-SRB-4, AC-SRB-9, AC-SRB-10, AC-SRB-13 meet as documented); no density setting (AC-SRB-1 fails at compact and dense); the input is a `TextInput` named by the placeholder, no `searchbox` role documented (AC-SRB-7 unmeasured); Escape closes only, never clears (AC-SRB-5 fails); no Up and Down through the rows from the input (AC-SRB-6 fails, rows are pressed with the pointer); no full-screen view and no shortcut to focus the bar |
| tess-shell | `tess-shell:src/tess_shell/shipped/Applications/Applications_Module.tdl` (launcher filter input, placeholder "Search applications"), `shell-vault:40 Specifications/Modules/Applications Module.md` | partly meets: a filter input with a placeholder that updates a list on `On_Changed`; no bar, no back arrow, no clear button, no count announcement (AC-SRB-4, AC-SRB-8 absent); keyboard use of the launcher: `tess-shell:docs/guide/keyboard.md#the-launcher` |
| tre | `tre:docs/guide/text.md` (text input `input_mode: "search"`), `tre:docs/guide/accessibility.md` | not applicable (primitive): `input_mode` search is kept for a keyboard that can adapt; active descendant is TRE-REQ-023 ([[Active Descendant]]) |

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/SearchBar_View.tdl`, `tess-ui:src/tess_ui/views/SearchView_View.tdl`, `tess-ui:docs/components/search.md` | exists, partial |
| tess-shell | `tess-shell:src/tess_shell/shipped/Applications/` | launcher filter only |
| tre | `tre:docs/guide/text.md` | primitive only |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Bar height 40 and 32 dp at compact and dense (MD3 56 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Search field variant (a text field with role `searchbox`) beside the bar | filtering inside a dense panel needs no pill or elevation | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Down and Up move an active row while focus stays in the input; Escape steps through close, clear, deactivate | keyboard-first | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Global focus shortcut for the main search bar | keyboard-first | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Result updates debounced and not run on IME pre-edit text | desktop IME use | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- [Material Components Android search docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Search.md): search bar and search view, container colour `colorSurfaceContainerHigh`, clear button, menu-to-back-arrow animation, accessibility of siblings, soft keyboard flag.
- [Material Components Android search dimens](https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/search/res/values/dimens.xml): bar height, elevation and view heights are references to `m3_comp_search_*` tokens whose numbers were not read; the 56 dp bar height and 28 dp panel corner are the tess-ui values and are marked #needs-verification against the MD3 token set.
- [WAI-ARIA APG combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/), [WAI-ARIA 1.2 searchbox](https://www.w3.org/TR/wai-aria-1.2/#searchbox) and [search landmark](https://www.w3.org/TR/wai-aria-1.2/#search).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.3, 1.4.11, 2.5.8.
- tess-ui search documentation: `tess-ui:docs/components/search.md`.
- The MD3 specification page values (56 dp bar, level 3 elevation, 28 dp view corner) could not be read from m3.material.io (script-rendered) and are marked #needs-verification.
