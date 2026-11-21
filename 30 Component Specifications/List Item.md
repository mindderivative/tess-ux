---
title: List Item
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, list, density]
related: ["[[List]]", "[[Tree Node]]", "[[Form Row]]", "[[Scrollbar and Scroll Container]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[State Layers]]", "[[Focus Ring]]", "[[Typography]]", "[[Iconography]]", "[[Shape]]", "[[Elevation]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]"]
---

# List Item

> [!info] Summary
> One row of a [[List]]: optional leading element, one to three lines of text, optional trailing element. Counterpart: the Material Design 3 list item (https://m3.material.io/components/lists/overview; values below verified in the Material Web tokens, see Sources). Source of truth in code: the last section.

## Purpose

Present one entity in a column with its identity (headline), detail (supporting text) and an action or status at the end, and let the pointer and keyboard choose or act on it.

## When to use and not

- Use when: rows are homogeneous entities (applications, files, outputs, tasks).
- Do not use when: rows are hierarchical ([[Tree Node]]), label-plus-control settings ([[Form Row]]), or menu commands ([[Menu]]).

## Anatomy

1. Container: full row width, height by lines and density.
2. Leading (optional): icon, avatar (letters in a circle), image, or a slot (checkbox).
3. Overline (optional, `label_small`).
4. Headline (`body_large` at `default`, `body_medium` at `compact` and `dense`).
5. Supporting text (`body_medium` at `default`, `body_small` at `compact` and `dense`, one or two lines).
6. Trailing (optional): supporting text (`label_small`), icon, or a slot (switch, button).
7. Divider (optional): 1 dp line along the bottom edge.

## Variants

| Variant | Use | Differences |
|---|---|---|
| One line | headline only | height table below |
| Two line | headline and supporting text | |
| Three line | overline, headline and supporting text, or headline and two supporting lines | |
| Selectable | rows that are chosen | selected container, `aria-selected` |
| Action | row is a button | pressable, no selection |

## States

State layer role `on_surface`; percentages from [[ADR-0009 State layer percentages]] ([[State Layers]]).

| State | Visual change | Token values |
|---|---|---|
| Rest | container `surface` (or transparent over the list surface); headline `on_surface`; supporting, overline, trailing text and icons `on_surface_variant` | MD3 list item tokens |
| Hover | state layer | 8 percent |
| Focus (keyboard) | state layer plus focus ring drawn inset in the row | 10 percent; ring 3 dp `secondary` ([[Focus Ring]]) |
| Pressed | state layer | 10 percent |
| Dragged | state layer and elevation level 4 (planned: drag to reorder) | 16 percent; MD3 `dragged-container-elevation` level4 |
| Selected | container `secondary_container`, headline `on_secondary_container` | Tesserae choice, #needs-verification (MD3 list tokens define no selected container) |
| Disabled | text and icons at 0.38 of `on_surface`; no layers, no focus stop | MD3: label 0.30, icons 0.38 (see Deviations) |
| Error | not applicable | none |
| Loading, empty | not applicable to the item; see [[List]] | none |

## Tokens used

[[Colour Roles]] (`surface`, `on_surface`, `on_surface_variant`, `secondary_container`, `on_secondary_container`, `outline_variant`), [[Typography]], [[Shape]] (container shape `none`; a selected or hovered row in a card list may use `small` 8 dp), [[Spacing and Density]], [[Iconography]].

## Sizing and density

Heights follow the binding density table for the single-line case ([[ADR-0002 Desktop density levels and target sizes]]). Two- and three-line heights are derived by one rule, so that they are testable: height = sum of the line heights + vertical padding, with padding 16 dp (default), 12 dp (compact), 4 dp (dense) in total. #needs-verification (design choice; the contract fixes only the single-line values).

| Token | default | compact | dense | MD3 |
|---|---|---|---|---|
| Height, one line | 40 dp | 32 dp | 24 dp | 56 dp |
| Height, two lines | 60 dp | 48 dp | 40 dp | 72 dp |
| Height, three lines | 80 dp | 64 dp | 56 dp | 88 dp |
| Line heights (headline, supporting) | 24, 20 | 20, 16 | 20, 16 | 24, 20 |
| Horizontal padding (leading and trailing space) | 12 dp | 8 dp | 4 dp | 16 dp |
| Gap between parts | 8 dp | 8 dp | 4 dp | 16 dp |
| Leading icon size | 24 dp | 20 dp | 20 dp | 24 dp |
| Leading avatar size | 40 dp | 32 dp | 24 dp | 40 dp |
| Leading image size | 56 dp | 48 dp | 40 dp | 56 by 56 dp |
| Trailing icon size | 24 dp | 20 dp | 20 dp | 24 dp |

The line-height rows give 24 + 20 = 44 for two lines at `default`; with 16 dp padding the height is 60 dp. The three-line height is fixed by the table whether the third line is an overline or a second supporting line (the content is centred in the row). A trailing control or icon button (container 40, 32, 28 dp) fits inside the row at its density; an avatar or image larger than the row content height is not allowed (the row grows to the next line count). The pointer target is the whole row, at least 24 dp tall at every density ([[ADR-0002 Desktop density levels and target sizes]]).

## Dimensions and defaults

Heights are the binding density table for one line and the derived rule of [[List Item#Sizing and density]] for two and three lines. The icon sizes below follow this note's Sizing table (dense 20); [[Iconography]] gives 16 for a list row at dense, and the two notes disagree until the owner decides #needs-verification-as-design-choice (proposed ADR: list row icon size at dense).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container (one line) | height | `density.row_height` | 40 | 32 | 24 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container (two lines) | height | - | 60 | 48 | 40 | design choice, proposed ADR (list row height for two and three lines); [[List Item#Sizing and density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container (three lines) | height | - | 80 | 64 | 56 | design choice, proposed ADR (list row height for two and three lines); [[List Item#Sizing and density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| container | padding | `density.row_padding_x` | 8 12 8 12 | 6 8 6 8 | 2 4 2 4 | [[Spacing and Density]] (horizontal); vertical is half of the total 16, 12, 4 of [[List Item#Sizing and density]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| container | margin | - | N/A: a row fills the list width; the list sets any outer space | N/A: same as default | N/A: same as default | [[List Item#Layout and overflow]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| container | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| leading avatar | height | - | 40 | 32 | 24 | [[List Item#Sizing and density]], MD3 avatar 40 | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| leading image | height | - | 56 | 48 | 40 | [[List Item#Sizing and density]], MD3 image 56 | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container | border width | - | 0 | 0 | 0 | MD3 [list item tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu-item.scss) | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| container | border color | - | N/A: the row draws no border; selection is a container fill | N/A: same as default | N/A: same as default | [[List Item#States]] | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| divider | border width | `md.comp.divider.thickness` | 1 | 1 | 1 | [[List Item#Layout and overflow]] | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| divider | border color | `outline_variant` | `outline_variant` | `outline_variant` | `outline_variant` | [[List Item#Layout and overflow]] | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| container | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] ([[List Item#Tokens used]]) | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| container (in a card list) | corner radius | `shape.small` | 8 | 8 | 8 | [[Shape]] ([[List Item#Tokens used]]) | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| headline | font | `body_large`, `body_medium`, `body_medium` | 16/24/400/0.5 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| supporting text | font | `body_medium`, `body_small`, `body_small` | 14/20/400/0.25 | 12/16/400/0.4 | 12/16/400/0.4 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| overline, trailing text | font | `label_small` | 11/16/500/0.5 | 11/16/500/0.5 | 11/16/500/0.5 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| leading icon | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[List Item#Sizing and density]] | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| trailing icon | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[List Item#Sizing and density]] | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| container | elevation | `elevation.level_0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| container (dragged) | elevation | `elevation.level_4` | 4 | 4 | 4 | [[Elevation]] (planned; MD3 `dragged-container-elevation`) | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |

## Layout and overflow

- Leading and trailing parts do not shrink. The text column takes the remaining width with a minimum width of 0.
- Headline: one line, ellipsis when cut. Supporting text: one line (two in a three-line item with two supporting lines), ellipsis when cut. Overline: one line.
- Vertical alignment: leading and trailing parts are centred on the row in one- and two-line items; in a three-line item they align to the top of the text column (MD3 behaviour, #needs-verification).
- A divider is inset by the row horizontal padding on both sides (MD3: 16 dp inset at both ends) and is 1 dp thick in `outline_variant`.
- A row never widens its list: its content truncates; the list scrolls only vertically for long lists ([[List]], [[Scrollbar and Scroll Container]]).

## Behaviour

- Pointer: press or click activates the row (or selects it when selectable); hover and press show state layers.
- Keyboard: focus and keys are handled by the [[List]]; Enter activates the focused row, Space selects it.
- Touch: 48 dp rows in touch contexts; swipe actions are not applicable on desktop and are not specified.

## Tooltip and overlay behaviour

The row has no tooltip. A truncated headline or supporting text shows a tooltip on that text element ([[ADR-0004 Tooltip rule]]); the trailing icon button carries its own label tooltip ([[Icon Button]]). The row itself never carries one.

## Motion

State layer changes use 100 ms (`short2`, [[Motion]]); there is no row animation on selection; reduced motion sets 0 ms.

## Accessibility

- Role `listitem` in a plain list; role `option` in a selectable list (listbox); name = headline; description = supporting text; `aria-selected` only in a selectable list (WAI-ARIA listbox pattern, https://www.w3.org/WAI/ARIA/apg/patterns/listbox/).
- Contrast: headline on the row container 4.5 to 1; supporting text 4.5 to 1; icons 3 to 1.
- Target size of at least 24 dp ([[ADR-0002 Desktop density levels and target sizes]]).

## Dark and light

Roles only ([[Theme Following the System]]).

## Defaults

One line, no leading, no trailing, no divider, not selectable, `default` density unless the project sets a level.

## Acceptance criteria

- [ ] AC-LSI-01: Token test. The row tokens equal the sizing table for the three densities.
- [ ] AC-LSI-02: Geometry check. Heights are 40, 32, 24 dp for one line; 60, 48, 40 for two lines; 80, 64, 56 for three lines, for the matching densities.
- [ ] AC-LSI-03: Geometry check. Left padding of the first part equals 12, 8, 4 dp and the gap between parts 8, 8, 4 dp; the right padding equals the left.
- [ ] AC-LSI-04: Geometry check. A 400-character headline in a 240 dp row ends in an ellipsis, the row has no horizontal overflow and the headline right edge is at most the row width minus the right padding minus the trailing part.
- [ ] AC-LSI-05: Geometry check. Leading icon, avatar and image sizes equal the table; an avatar taller than the row content height is rejected by a build-time check or grows the row to the next line count.
- [ ] AC-LSI-06: Pixel check. Hover shows an 8 percent `on_surface` layer, pressed and focus 10 percent, with the keyboard focus ring (3 dp, `secondary`) inset in the row; a mouse click does not show the ring.
- [ ] AC-LSI-07: Contrast script. Headline and supporting text reach 4.5 to 1 on the row container and on `secondary_container` in light and dark baseline schemes; icons 3 to 1.
- [ ] AC-LSI-08: Scripted input. A disabled row ignores click, Enter and Space, shows content at opacity 0.38 and is not a focus stop.
- [ ] AC-LSI-09: AT tree assertion. Role is `listitem` in a plain list and `option` in a selectable one; name equals headline; description equals supporting text; `aria-selected` exists only in a selectable list.
- [ ] AC-LSI-10: Geometry check. A divider is 1 dp thick, colour `outline_variant`, inset by the row horizontal padding on both ends.
- [ ] AC-LSI-11: Scripted input. Hovering the row away from a truncated headline shows no tooltip; hovering a truncated headline for 500 ms shows its full text; no tooltip key is set on the row.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/ListItem_View.tdl`, `ListItem_Stylesheet.tdl`, `tess-ui:docs/stylesheets/lists/` | partly meets. Heights 56, 72, 88 (MD3 values, no density: fails AC-LSI-02); padding 16 and gap 16 with 8 dp top and bottom (fails AC-LSI-03); headline `body_large`, supporting `body_medium` with ellipsis (meets AC-LSI-04 as designed); avatar 40, image 56, icons 24 (default only); role `listitem` with `Selected` and `Description` (AC-LSI-09 partly: no `option` role in a selectable list); selected `secondary_container`; state layer and ripple through the interaction layer (AC-LSI-06 not measured); divider from 16 dp to the right edge, not inset at both ends (AC-LSI-10 fails); swipe and drag not built |
| tess-shell | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` (`.list_item`) | partly meets. Padding `[10, 6, 10, 6]`, radius small; hover `surface_raised`; selected raised fill with 2 px border; disabled opacity 0.5; no density levels (fails AC-LSI-01 to 03, 06, 08 value 0.38 vs 0.5) |
| tre | none | not applicable (no list item; roles `list`, `listitem` available) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 24 (one line) instead of 56 | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Padding 12, 8, 4 dp and gap 8, 8, 4 dp instead of 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Disabled text 0.38 instead of MD3 label opacity 0.30 | one disabled content value across Tesserae ([[State Layers]]) | [[ADR-0009 State layer percentages]] |
| State layer focus and pressed 10 percent instead of the 12 percent listed in the Material Web tokens | decided state layer scale | [[ADR-0009 State layer percentages]] |
| Selected container `secondary_container` | MD3 list tokens give no selected container | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- Material Web list item tokens, https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-list.scss (read 2026-11-21): one, two, three line heights 56, 72, 88 dp; leading and trailing space 16 dp; leading icon 24 dp; avatar 40 dp; image 56 by 56 dp; container shape none; container colour `surface`; label `body-large`, supporting `body-medium`, trailing supporting text and overline `label-small`; disabled label opacity 0.3, icons 0.38; dragged elevation level4; divider leading and trailing space 16 dp.
- Layout (gap 16 px, padding top and bottom 12 px from `top-space`, `bottom-space` in `tokens/_md-comp-list-item.scss`): https://github.com/material-components/material-web/blob/main/list/internal/listitem/_list-item.scss and https://github.com/material-components/material-web/blob/main/tokens/_md-comp-list-item.scss.
- Divider thickness 1 px, colour `outline-variant`: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-divider.scss.
- State layer values in the Material Web tokens (hover 0.08, focus 0.12, pressed 0.12, dragged 0.16): https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-state.scss; Tesserae uses [[ADR-0009 State layer percentages]].
- WAI-ARIA listbox pattern: https://www.w3.org/WAI/ARIA/apg/patterns/listbox/.
- Code: `tess-ui:src/tess_ui/views/ListItem_View.tdl`, `ListItem_Stylesheet.tdl` (origin/main c7117cb); `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl`.
