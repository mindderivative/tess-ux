---
title: Token Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, selection, tesserae-specific, config-app]
related: ["[[Button]]", "[[Icon Button]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[Text Field]]", "[[Menu]]", "[[Popup]]", "[[List]]", "[[List Item]]", "[[Form Row]]", "[[12 Overlays]]", "[[Existing Tokens]]"]
depends_on: ["[[Button]]", "[[Text Field]]", "[[Popup]]", "[[List]]", "[[Colour Roles]]", "[[Shape]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Token Button

> [!info] Summary
> A button that shows the theme token a setting holds (such as `$color.primary`, with a swatch for a colour) and opens a searchable list of tokens in a layer under it. Tesserae-specific: Material Design 3 has no token picker; the spec rests on the MD3 outlined button, the menu surface, the WAI-ARIA menu button and the combobox patterns. Source of truth in code: see Status in code.

## Purpose

Lets a person point a setting at a token of the theme instead of typing a literal value or a reference. Used in the shell configuration app for every key that accepts a token.

## When to use and not

- Use when: a value is a reference to a design token and the app can list the tokens (the app supplies them as data).
- Do not use when: the value is a free colour or number (use a colour picker or a [[Text Field]]); the choice is among a handful of fixed options (use a menu button or a [[Segmented Button]]); the list is not a token list.
- The control is built in tess-ui; a project does not hand-roll one.

## Anatomy

1. Field: an outlined container (1 dp `outline`) with the current value.
2. Swatch (optional): 24 dp rounded square with a 1 dp `outline` border, shown when the held token is a colour the control knows.
3. Value text: the token's ref, `body_large`; the placeholder ("Choose a token") in `on_surface_variant` while empty.
4. Chevron icon: 24 dp, `on_surface_variant`, turned over while the layer is open.
5. Layer: a [[Popup]] anchored below the field, a `surface_container` surface, elevation level_2, with
   1. search field ([[Text Field]], label "Search tokens"),
   2. list of token rows (a virtual list, 7 rows visible by default),
   3. empty note when the search finds nothing.
6. Row: swatch (32 dp) or none, name (`body_large`), a line under it with the group and the doc line (`body_small`, `on_surface_variant`), the value at the end (`label_medium`, `on_surface_variant`, at most 120 dp wide).
7. State layer and focus ring on the field ([[State Layers]], [[Focus Ring]]).

## Variants

None. The list may hold ungrouped tokens, grouped tokens (each row names its group) and preferred tokens (listed first). A colour token (`Kind` colour, value `#rrggbb` or `#rrggbbaa`) shows a swatch; any other kind shows its value as text. Not built: tree of the dotted names, alias display, preview for kinds other than colour, reading tokens from the theme (the app passes them).

## States

State layer on the field in `on_surface` ([[State Layers]]: hover 8, focus 10, pressed 10 percent).

| State | Visual change |
|---|---|
| Rest | outlined field, `outline` 1 dp |
| Hover | state layer 8 percent |
| Focus (keyboard) | state layer 10 percent plus focus ring 3 dp, 2 dp offset, role `secondary`; the outline stays 1 dp |
| Pressed | state layer 10 percent |
| Open | chevron turned over; the layer shows; the field keeps the pressed layer #needs-verification (design choice) |
| Unknown ref | the held ref is shown as it is, kept, no swatch; no error state |
| Disabled | value, chevron on `on_surface` at 38 percent, outline at 12 percent; the layer does not open; not focusable |
| Row: held token | `secondary_container` with value on `on_secondary_container` |
| Row: keyboard cursor | `surface_container_highest` |
| Row: hover | state layer 8 percent |

## Tokens used

[[Colour Roles]] (`outline`, `on_surface`, `on_surface_variant`, `surface_container`, `surface_container_highest`, `secondary_container`), [[Shape]] (field and row corners: 12 dp in tess-ui; the menu surface uses 4 dp `extra_small`, see Deviations), [[Elevation]] (level_2), [[Typography]], [[Motion]], [[Spacing and Density]].

## Sizing and density

The field takes the height of a [[Text Field]] at each level ([[ADR-0002 Desktop density levels and target sizes]]); rows are two-line list rows. Row, swatch and padding values are design choices modelled on [[List Item]] #needs-verification.

| Level | Field height | Field padding (sides) | Field swatch | Row height | Row swatch | Row padding (sides) | Layer padding |
|---|---|---|---|---|---|---|---|
| default | 40 | 12 | 24 | 56 | 32 | 12 | 8 |
| compact | 32 | 8 | 20 | 48 | 28 | 8 | 4 |
| dense | 28 | 8 | 16 | 40 | 24 | 8 | 4 |

- The field is as wide as its form row cell; the layer's width is the `Width` parameter, 240 to 640 dp, default 360, never wider than the window minus 16 dp.
- Visible rows 3 to 12, default 7; the list is as tall as rows times row height, scrolls when more tokens match and builds only the rows in view plus three at each edge. The layer height never exceeds the space below the field, else it flips above ([[12 Overlays]]).
- The value text is vertically centred in the field (space above equals space below ±0.5 dp) at every density, as [[Text Field]].
- Hit area: the whole field (at least 24 dp high at every density, 48 dp in touch contexts).

## Dimensions and defaults

The field follows [[Text Field]] heights; every other value is a design choice modelled on [[List Item]] and on the tess-ui build (#needs-verification-as-design-choice). The field and row corners keep the 12 dp of the build, the swatch corners are scale steps.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| field | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| row | height | - | 56 | 48 | 40 | [[Token Button]] Sizing; design choice, proposed ADR for token list row heights | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| field | min height | `target.min` | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| field (touch hit area) | min height | `target.touch` | 48 | 48 | 48 | [[Spacing and Density]], touch context only | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| layer | min width | - | 240 | 240 | 240 | the `Width` parameter range 240 to 640, [[Token Button]] Sizing | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| field | padding | `density.field_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 8 0 8 | [[Spacing and Density]], as [[Text Field]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| row | padding | `density.row_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 8 0 8 | [[Token Button]] Sizing; design choice, proposed ADR for token list row heights | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| layer | padding | `space.3` | 8 8 8 8 | 4 4 4 4 | 4 4 4 4 | [[Token Button]] Sizing; design choice, proposed ADR for token list row heights | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| field | margin | - | N/A: the form row cell sets the outer space | N/A: the form row cell sets the outer space | N/A: the form row cell sets the outer space | [[Form Row]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| field (swatch, value, chevron) | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]]; design choice, proposed ADR for token list row heights | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| row (swatch, text, value) | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]]; design choice, proposed ADR for token list row heights | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| field | border width | - | 1 | 1 | 1 | [[Token Button]] Anatomy (the outline stays 1 dp when focused) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| swatch | border width | - | 1 | 1 | 1 | [[Token Button]] Anatomy | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| field | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| swatch | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| layer | border width | - | 0 | 0 | 0 | the layer is a raised surface and draws no outline, [[Token Button]] Anatomy | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| layer | border color | - | N/A: the layer draws no border; elevation separates it | N/A: the layer draws no border; elevation separates it | N/A: the layer draws no border; elevation separates it | [[Token Button]] Anatomy | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| field, row, layer | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]]; tess-ui build, [[ADR-0006 MD3 baseline with named Expressive adoptions]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| field swatch | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]]; design choice, proposed ADR for token list row heights | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| row swatch | corner radius | `shape.small` | 8 | 8 | 8 | [[Shape]]; design choice, proposed ADR for token list row heights | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| field value text, row name | font | `body_large` | 16/24/400/0.5 | 16/24/400/0.5 | 16/24/400/0.5 | [[Typography]], [[Token Button]] Anatomy | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height, letter_spacing) |
| row detail line | font | `body_small` | 12/16/400/0.4 | 12/16/400/0.4 | 12/16/400/0.4 | [[Typography]], [[Token Button]] Anatomy | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height, letter_spacing) |
| row value | font | `label_medium` | 12/16/500/0.5 | 12/16/500/0.5 | 12/16/500/0.5 | [[Typography]], [[Token Button]] Anatomy | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height, letter_spacing) |
| field chevron | icon size | - | 24 | 24 | 24 | [[Token Button]] Anatomy, [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| field swatch | icon size | - | 24 | 20 | 16 | swatch box size, [[Token Button]] Sizing | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| row swatch | icon size | - | 32 | 28 | 24 | swatch box size, [[Token Button]] Sizing | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| field | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| layer | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]], [[Token Button]] Anatomy | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| focus ring (field) | border width | - | 3 | 3 | 3 | [[Focus Ring]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring (field) | border color | `secondary` | `secondary` | `secondary` | `secondary` | [[Focus Ring]] | tess-ui: via App(focus_ring=) ring colour argument; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring (field) | margin | - | 2 2 2 2 | 2 2 2 2 | 2 2 2 2 | [[Focus Ring]] (offset outside the field) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |

## Layout and overflow

- The value text is one line; a long ref ends with an ellipsis and the full ref is the tooltip on the field ([[ADR-0004 Tooltip rule]]). The swatch and chevron keep their size.
- A row's name and detail are one line each with an ellipsis; the value has a maximum width of 120 dp with an ellipsis. Nothing draws outside the row.
- The list scrolls inside the layer ([[Scrollbar and Scroll Container]]); on open it is scrolled so the held token is visible with the cursor on it.

## Behaviour

- Pointer: a press on the field toggles the layer; a press on a row picks it; a press outside or Escape closes the layer without picking.
- Pick: writes the token's ref to `Value`, calls the pick handler, closes the layer (unless `Close_On_Pick` is false) and returns focus to the field.
- Search: keeps the tokens whose name, ref, group or doc contain every word typed, in any order and without regard to case; a name that starts with the first word comes first; preferred tokens stay first among equals; the search is empty on each open.
- Keyboard: Enter or Down on the field opens the layer and focuses the search field. In the search field Up, Down, Page Up and Page Down move the cursor by a row or by the visible row count, Enter picks the token under the cursor; Left, Right, Home, End and Space belong to the text. Tab moves from the search field to the list, where Up, Down, Page Up, Page Down, Home and End move the cursor, and Enter and Space pick. Escape closes the layer and focus returns to the field. A closed field takes Tab and Shift+Tab as any control.
- Touch: tap on the field and on rows (rows at least 48 dp high in touch contexts).

## Tooltip and overlay behaviour

The field carries a plain tooltip with the full ref (or the label when empty) when the text is truncated ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]], [[Tooltip]]). Rows have no tooltips (name, group, doc and value are visible); no tooltip on the layer. The layer is a [[Popup]] ([[12 Overlays]]): it closes on a press outside and on Escape, with no scrim, and focus returns to the field. Opening the layer dismisses the field's tooltip.

## Motion

Layer appears with `short3` 150 ms fade and no movement; chevron turn 100 ms; scroll to the held token is instant. Reduced motion: no fade #needs-verification.

## Accessibility

- Field: role `button`, `haspopup` list (the layer is a list popup, not a menu), `expanded` while open, name "{label}: {ref}" (for example "Accent: $color.primary"), or the label alone when empty. Matches the [WAI-ARIA APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) keys with the combobox-style search field.
- Layer: role `group` named with the label; the search field has the name "Search tokens"; the list has role `list` named "{label} tokens" with `listitem` rows, each named "{name}: {value}" and `selected` when it is the held token; an empty result is announced by an `alert` with polite live region.
- The count of matches is available to assistive technology (`Count`, tess-ui) #needs-verification (not announced today).
- Contrast: value text on the field surface at least 4.5 to 1; swatch border and field outline at least 3 to 1 (WCAG 1.4.3, 1.4.11). The swatch is decoration: the value text carries the information.

## Dark and light

All roles; the swatch shows the token value of the current scheme as the app supplies it. AC-TKB-10 runs in both ([[Theme Following the System]]).

## Defaults

Rows 7, width 360, close on pick true, placeholder "Choose a token", label "Token". Density from the container (the config app uses compact).

## Acceptance criteria

- [ ] AC-TKB-1 (token test): field height 40, 32, 28 dp, row height 56, 48, 40 dp, swatch sizes and paddings equal the Sizing table at default, compact, dense. Pass: values equal.
- [ ] AC-TKB-2 (geometry check): the value text line box is vertically centred in the field (offset at most 0.5 dp) at each density and scale 1.0, 1.25, 2.0; the field hit area is at least 24 dp high (48 in touch). Pass: offset at most 0.5 dp, bounds at or above limits.
- [ ] AC-TKB-3 (token test): field outline 1 dp `outline`; layer `surface_container` at elevation level_2; held row `secondary_container`; cursor row `surface_container_highest`; no literal colour. Pass: every colour is a role reference.
- [ ] AC-TKB-4 (scripted input): Enter on the closed field opens the layer with the focus in the search field; Down does the same; Escape closes it, focus is on the field and `Value` is unchanged. Pass: focus owner and value equal.
- [ ] AC-TKB-5 (scripted input): in the search field Down, Up, Page Down, Page Up move the cursor by 1 and by the visible row count; Enter picks the token under the cursor; `Value` equals its ref, the pick handler ran once and the layer closed. Pass: values and counts equal.
- [ ] AC-TKB-6 (scripted input): the search "prim col" (any order, any case) keeps exactly the tokens whose name, ref, group or doc contain both words; the layer reopens with an empty search and the held token scrolled into view with the cursor on it. Pass: result list equal to the expected list.
- [ ] AC-TKB-7 (scripted input): with 5000 tokens the number of built rows is at most visible rows plus 6 and opening takes at most 100 ms on the reference machine. Pass: row count and time within limits #needs-verification (time limit is a proposal).
- [ ] AC-TKB-8 (AT tree assertion): field role `button`, `expanded` equal to the open state, name "{label}: {ref}"; layer `group`; list `list` with `listitem` rows named "{name}: {value}", `selected` on the held token; an empty search exposes an `alert`. Pass: all equal.
- [ ] AC-TKB-9 (geometry check): a ref longer than the field shows an ellipsis with no text pixel outside the field; a row with long name, detail or value shows ellipses with no pixel outside the row; the layer lies fully inside the window (flips above when below does not fit). Pass: zero pixels outside, bounds inside.
- [ ] AC-TKB-10 (contrast script): light and dark, value text on the field at least 4.5 to 1, row value text on row at least 4.5 to 1 (held and unheld), outline and swatch border on the surface at least 3 to 1. Pass: ratios at or above limits.
- [ ] AC-TKB-11 (scripted input): a press outside closes the layer; hovering a truncated field for the tooltip delay shows a tooltip with the full ref; opening the layer hides it; no row shows a tooltip. Pass: events equal.
- [ ] AC-TKB-12 (pixel check): a colour token shows a swatch whose centre pixel equals the token's value; a ref unknown to the list shows the text and no swatch; a disabled field is at 38 percent content and 12 percent outline and does not open. Pass: pixel equals, states equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TokenButton_View.tdl`, `TokenButton_Stylesheet.tdl`, `tess-ui:src/tess_ui/token_controls.py` (`TokenList`), `tess-ui:docs/components/token-buttons.md`, test `tess-ui:tests/test_token_button.py` | partly meets: swatch, ref text, search, virtual list (rows in view plus three), keyboard as specified, Escape and outside press, `Expanded`, `list` and `listitem` roles, alert for no result (AC-TKB-4 to AC-TKB-6, AC-TKB-8 meet by reading; AC-TKB-7 meets for the row count); field height `Min_Height` 48 at every density (AC-TKB-1 fails: no 40, 32, 28), row height 56 literal at every density (fails at compact and dense), corners 12 dp and layer padding 8 literal, layer elevation 2 (AC-TKB-3 meets roles), disabled fades the whole control (AC-TKB-12 partly), no tooltip with the full ref on truncation (AC-TKB-11 partly), `haspopup` not set (AC-TKB-8 partly) |
| tess-ui | `tess-ui:src/tess_ui/views/TokenButton_Stylesheet.tdl` dimensions | differs: field min height 48 (spec 40, 32, 28; AC-TKB-1); row height 56 at every density (spec 48, 40 at compact and dense); gap 12 (spec 8, 8, 4); field swatch corner 6 (spec 4); layer padding 8 at every density (spec 4 at compact and dense) |
| tess-shell | not used by the shell; tess-ui:apps/shell_config uses it (below) | not applicable |
| tre | none | not applicable |

Use in tess-ui: the shell configuration app, `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (`TokenButton` for each key that accepts tokens, `Groups` and `Preferred` from the schema, width 360, `On_Pick` writes `$group.name`) and `tess-ui:apps/shell_config/README.md`.

## Deviations from Material Design 3

There is no MD3 token button; deviations are from the nearest patterns.

| Deviation | Reason | ADR |
|---|---|---|
| Field height 40, 32, 28 dp (outlined button and field are 40 and 56 in MD3) | desktop forms need rows per screen | [[ADR-0002 Desktop density levels and target sizes]] |
| Rows 56, 48, 40 dp two-line (MD3 list row 56 for two lines, 48 in menus) | density | [[ADR-0002 Desktop density levels and target sizes]] |
| Layer corners 12 dp and a search field in a menu-like surface (MD3 menu: 4 dp, no search) | tess-ui build; the layer is a searchable list | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hit area is the field with a 24 dp floor | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- Nearest MD3 patterns: [[Button]] (outlined), [[Menu]] (surface `surface_container`, elevation level_2), [[Text Field]], [[List Item]]. Values for those notes are verified there.
- [WAI-ARIA APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/); [APG combobox](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.3, 1.4.11, 2.5.8.
- Code: `tess-ui:docs/components/token-buttons.md`, `tess-ui:src/tess_ui/views/TokenButton_View.tdl`, `tess-ui:src/tess_ui/views/TokenButton_Stylesheet.tdl`.
