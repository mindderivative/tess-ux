---
title: Icon Picker
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, picker, icon, grid, search, keyboard]
related: ["[[Font List]]", "[[Colour Picker]]", "[[Choice Picker]]", "[[Text Field]]", "[[Popup]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Iconography]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[State Layers]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Iconography]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0007 Icon set and Material Symbols deviation]]"]
---

# Icon Picker

> [!info] Summary
> A searchable grid of icons (the curated built-in set plus the `.svg` and `.png` files of a user folder), inline or behind a button in a popup. Material Design 3 has no icon picker; the note builds on the MD3 outlined text field, [Menus](https://m3.material.io/components/menus/overview) and the WAI-ARIA grid pattern. Source of truth in code: the last section.

## Purpose

Let a person choose an icon by name or by sight for a launcher, a button or a block, from the shipped set and from their own Icons folder.

## When to use and not

- Use when: the value is an icon name or an icon file name.
- Do not use when: the set is fewer than about 8 icons ([[Choice Picker]]); the value is a font ([[Font List]]) or a colour ([[Colour Picker]]).

## Anatomy

1. Trigger (popup variant): outlined button with the icon (24 dp), its name and a chevron.
2. Layer ([[Popup]]): `surface_container`, 12 dp corners, 8 dp padding, level 2.
3. Search field ([[Text Field]]).
4. Grid: virtual rows of `Columns` cells (role `grid`), with a [[Scrollbar and Scroll Container]].
5. Cell: a square holding the icon (24 dp glyph, 32 dp preview for a file); no visible label.
6. Empty note and message line (folder unreadable), role `alert`.
7. Categories and recent row (not built).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Inline | panel content | search and grid always visible |
| Popup | form row | trigger opens the layer; a pick closes it unless `Close_On_Pick` is false |
| Folder | `Icons_Folder` set | the folder's `.svg` and `.png` files come first; read when the grid opens, a preview only when its row comes into view |

## States

| State | Visual change | Token values |
|---|---|---|
| Cell rest | transparent, glyph `on_surface` | none |
| Cell hover | state layer | `on_surface` 8 percent |
| Cell cursor | filled; ring when focused | `surface_container_highest`; [[Focus Ring]] |
| Cell selected (the value) | filled | `secondary_container`, glyph `on_secondary_container` |
| Trigger rest, hover, focus, pressed | outline and layers | `outline` 1 dp; 8, 10, 10 percent |
| Disabled | does not open | 0.38 |
| Empty search | note | `on_surface_variant` |
| Folder error | message, built-in icons stay | `error` |
| Unknown value | value kept as is, no cell selected | none |

## Tokens used

[[Colour Roles]], [[Shape]] (cells 12 dp), [[Elevation]] (level 2), [[Iconography]] (glyph sizes, `currentColor` rule for SVG), [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

| Part | default | compact | dense | Code today |
|---|---|---|---|---|
| Trigger height | 40 | 32 | 28 | 48 minimum |
| Search field height | 40 | 32 | 28 | text field default |
| Cell (square) | 48 | 40 | 32 | 48 |
| Glyph | 24 | 24 | 20 | 24 (file preview 32) |
| Layer padding | 8 | 8 | 4 | 8 |
| Columns | 8 | 8 | 8 | 8 (3 to 16) |
| Visible rows (`Rows`) | 6 | 6 | 6 | 6 (2 to 12) |

Panel width is Columns times the cell size plus 16 dp. A cell is at least 24 by 24 dp so the dense cell of 32 dp meets the target size ([[ADR-0002 Desktop density levels and target sizes]]). Only 24 dp is built as a glyph size; other sizes are Not built.

## Dimensions and defaults

The trigger follows the outlined [[Button]] (heights from the control height; padding mirrored for a trailing chevron). The cell grid has no gap: the panel width is Columns times the cell size plus the 16 dp of layer padding.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| Trigger | height | `density.control_height` | 40 | 32 | 28 | [[Icon Picker]] Sizing, [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | min width | - | 64 | 48 | 48 | [[Button]] Sizing | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | padding | `space.6` | 0 16 0 24 | 0 12 0 16 | 0 8 0 12 | [[Button]] Sizing; design choice, [[ADR-0002 Desktop density levels and target sizes]] #needs-verification-as-design-choice | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | border width | - | 1 | 1 | 1 | [[Button]] Variants (outlined) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | border color | `outline` | `outline` | `outline` | `outline` | [[Button]] Variants, [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]], [[Button]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 13/18/500/0.1 | [[Button]], [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger icon | icon size | - | 24 | 24 | 24 | [[Icon Picker]] Anatomy part 1 | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger chevron | icon size | - | 18 | 18 | 16 | [[Iconography]] (icon next to a button label) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | padding | `space.3` | 8 8 8 8 | 8 8 8 8 | 4 4 4 4 | [[Icon Picker]] Sizing | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | margin | - | N/A: the popup is placed by the anchor; it has no outer space of its own | N/A: same as default | N/A: same as default | [[Popup]] | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Layer | gap | `space.0` | 0 | 0 | 0 | [[Icon Picker]] Sizing (cells touch; width equals Columns times cell plus 16) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | corner radius | `shape.medium` | 12 | 12 | 12 | [[Icon Picker]] Anatomy part 2, [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | border width | - | 0 | 0 | 0 | [[Popup]] (separated by its level 2 shadow) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | border color | - | N/A: the layer draws no border; the level 2 shadow separates it | N/A: same as default | N/A: same as default | [[Icon Picker]] Anatomy part 2 | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Layer | elevation | `elevation.level2` | 2 | 2 | 2 | [[Icon Picker]] Tokens used, [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Search field | height | `density.control_height` | 40 | 32 | 28 | [[Icon Picker]] Sizing, [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Search field | font | `body_large` | 16/24/400/0.5 | 14/20/400/0.25 | 13/18/400/0.25 | [[Text Field]] Tokens used, [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Cell | height | - | 48 | 40 | 32 | [[Icon Picker]] Sizing | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Cell | min width | - | 48 | 40 | 32 | [[Icon Picker]] Sizing (a square; at least 24 dp) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Cell | corner radius | `shape.medium` | 12 | 12 | 12 | [[Icon Picker]] Tokens used, [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Cell glyph | icon size | - | 24 | 24 | 20 | [[Icon Picker]] Sizing (file preview 32) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |

## Layout and overflow

- The grid scrolls vertically only; cells never truncate because they hold no text. The scrollbar is visible when more than `Rows` rows exist ([[ADR-0003 Scrollbar rule]]).
- Virtual: rows in view and three past each edge are built, however many icons exist; a new search makes new rows. The grid opens scrolled so the value shows.
- The trigger shows the icon and its name on one line with end ellipsis on the name.
- Glyphs are centred in the cell on both axes. A PNG scales down to fit the 32 dp preview box; an SVG draws in the text colour where it says `currentColor`; any other file shows a plain file glyph; an SVG with a document type or entity declaration is refused.

## Behaviour

- Search keeps icons whose name has every typed word, any order, case ignored, with `_`, `-` and `.` as spaces (`arrow back` finds `arrow_back`, `svg` finds `logo.svg`); a name that starts with the first word comes first.
- Pointer: a press picks; the wheel scrolls; Escape or a press outside closes.
- Keyboard: focus starts in the search field on open.

| Where | Key | Action |
|---|---|---|
| Search field | Up, Down, Page Up, Page Down | move the cursor in the grid |
| Search field | Enter | pick the cursor icon |
| Search field | Left, Right, Home, End, Space | text editing |
| Grid | Left, Right | previous, next icon |
| Grid | Up, Down | same column, previous, next row |
| Grid | Home, End | start, end of the row |
| Grid | Ctrl+Home, Ctrl+End | first, last icon |
| Grid | Page Up, Page Down | `Rows` rows |
| Grid | Enter, Space | pick |
| Popup | Escape | close, focus to the trigger |

- A pick writes `Value` (a name such as `home`, or a file name with extension such as `logo.svg`), calls `On_Change` once and closes a popup unless `Close_On_Pick` is false.
- Touch: 48 dp cells in a touch context; drag scrolls.

## Tooltip and overlay behaviour

Cells show no text, so each cell is a control with a tooltip naming its icon (`arrow_back`), after 500 ms of hover and immediately on keyboard cursor arrival; the tooltip is on the cell, never on the grid, the layer or a row ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]). The trigger shows the icon name when truncated. The layer is a [[Popup]] ([[12 Overlays]]): focus to the search field on open, back to the trigger on close. Selection preview: the trigger shows the chosen icon at once after a pick; a larger preview of the cursor icon is not built.

## Motion

Layer fade 150 ms in, 100 ms out ([[Motion]]); reduced motion 0 ms. No cell animation.

## Accessibility

- The picker is a `group` named by `Label` (default "Icon"). The trigger is a `button` named "Icon: name" with `expanded`. The grid is role `grid` with `row` and `gridcell` (code today: `list` of `listitem`), each cell named by its icon name and `selected` when it is the value. The search is a `searchbox`.
- Keys: the table above; the grid follows the WAI-ARIA grid keys (arrows, Home, End, Ctrl+Home, Ctrl+End, Page Up and Page Down).
- Announcements: moving the cursor announces the icon name and "n of N"; a pick announces "name selected"; no match and an unreadable folder are `alert` messages (polite).
- Contrast: glyph on `secondary_container` uses `on_secondary_container` at least 3:1 (icons) and the cell fill at least 3:1 against the layer ([[Colour Roles]]); the focus ring at least 3:1.
- Target size at least 24 by 24 dp at every density.

## Dark and light

Roles only; SVG icons that use `currentColor` follow the text colour, PNGs keep their own colours ([[Theme Following the System]]).

## Defaults

Inline, 8 columns, 6 rows, label "Icon", placeholder "Choose an icon", `Close_On_Pick` true, glyph 24 dp.

## Acceptance criteria

- [ ] AC-ICP-1 (geometry check): at default, compact and dense a cell is 48, 40 and 32 dp square, the trigger and search field are 40, 32 and 28 dp high, at scale 1.0 and 2.0.
- [ ] AC-ICP-2 (scripted input): "arrow back" finds `arrow_back`; "svg" finds `logo.svg`; a name starting with the first word is first; an empty query lists every icon.
- [ ] AC-ICP-3 (scripted input): in the grid Right moves one icon, Down one row in the same column, End the end of the row, Ctrl+End the last icon, Page Down `Rows` rows, and none leaves the grid; the cursor cell is scrolled into view.
- [ ] AC-ICP-4 (scripted input): Enter and Space in the grid and Enter in the search field write `Value`, call `On_Change` once and close a popup; with `Close_On_Pick` false it stays open.
- [ ] AC-ICP-5 (scripted input): a popup opens with focus in the search field and the value cell scrolled into view with the cursor on it; Escape closes and focus returns to the trigger within one frame.
- [ ] AC-ICP-6 (AT tree assertion): the grid has role `grid` (or `list`) with a name; each cell is named by its icon name; the value cell is `selected`; the trigger `expanded` equals the popup state.
- [ ] AC-ICP-7 (scripted input): hovering a cell for 500 ms shows a tooltip with its icon name, keyboard cursor arrival shows it at once, and no tooltip appears over the grid background or the layer; Escape, a press, scroll and leaving remove it.
- [ ] AC-ICP-8 (geometry check): 5000 icons build at most `Rows` + 6 rows of cells; a scrollbar thumb is visible and its length is at least the minimum thumb length.
- [ ] AC-ICP-9 (scripted input): a folder that cannot be read shows a message with role `alert` and the built-in icons stay; a file that is not SVG or PNG shows the file glyph; an SVG with a document type declaration is refused.
- [ ] AC-ICP-10 (scripted input): a `Value` that is no known icon is kept, no cell shows selected, and the trigger shows the placeholder.
- [ ] AC-ICP-11 (contrast script): cursor and selected cell fills measure at least 3:1 against the layer in light and dark at standard contrast, and the glyph at least 3:1 against the cell fill.
- [ ] AC-ICP-12 (review): each Not built item (categories or tags, recently used icons, other file types, a PNG's own colour, sizes other than 24 dp) is recorded in this note.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/IconPicker_View.tdl`, `IconPickerPanel_View.tdl`, `IconPicker_Stylesheet.tdl`, `IconPickerPanel_Stylesheet.tdl`, `tess-ui:src/tess_ui/icon_controls.py`, `tess-ui:docs/components/icon-pickers.md` | partly meets. Passes AC-ICP-2, 3, 4, 5, 8, 9, 10 by documented behaviour. Fails AC-ICP-1 (cell 48 and trigger 48 at every level), AC-ICP-6 in part (`list` and `listitem` roles), AC-ICP-7 (no tooltip on cells) |
| tess-ui (dimensions) | `tess-ui:src/tess_ui/views/IconPicker_Stylesheet.tdl` | Differences in [[#Dimensions and defaults]]: trigger 48 at all levels, spec 40, 32 and 28; cell 48 at all levels, spec 40 and 32 at compact and dense (AC-ICP-1); glyph 24 at dense, spec 20; layer padding 8 at dense, spec 4. Not settable from the project layer (no hook): the trigger gap 8, trigger and chevron icons 24, panel gap 8, cell 48 (`Item_Height`) and glyph 24, which are inline in `IconPicker_View.tdl` and `IconPickerPanel_View.tdl` |
| tess-ui | Not built (component doc) | icon categories or tags, recently used icons, other file types (`.jpg`, `.webp`), a PNG's own colour, sizes other than 24 pixels |
| tess-shell | `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`IconWidget`), `Main_View.tdl` | partly meets: popup variant with the user Icons folder; the shell-vault specification asks for a searchable picker over the shipped set and the user Icons folder, which it does |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |
| Element has no MD3 counterpart | desktop apps pick icons for launchers and blocks | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Icon set is Material Design Icons with Material Symbols names where they exist | existing assets | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Cell 48, 40, 32 dp; trigger 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltip on every cell | cells show no text; the tooltip is the name | [[ADR-0004 Tooltip rule]] |

## Sources

- tess-ui: `tess-ui:docs/components/icon-pickers.md`, `tess-ui:src/tess_ui/views/IconPickerPanel_Stylesheet.tdl` (cell 48, glyph 24, file preview 32), `tess-ui:src/tess_ui/views/IconPickerPanel_View.tdl`, `shell-vault:40 Specifications/Configuration Application.md`.
- WAI-ARIA APG grid https://www.w3.org/WAI/ARIA/apg/patterns/grid/ (arrows, Home, End, Ctrl+Home, Ctrl+End, Page Up and Page Down; verified reachable 2026-11-21); listbox https://www.w3.org/WAI/ARIA/apg/patterns/listbox/.
- WCAG 2.2 SC 1.4.11 https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html, SC 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, SC 4.1.3 https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html.
- Dense 20 dp glyph with a 32 dp cell and the 24 dp glyph at compact follow [[Iconography]] and [[Spacing and Density]] icon button values #needs-verification.
