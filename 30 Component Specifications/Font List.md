---
title: Font List
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, picker, font, list, search, keyboard]
related: ["[[List]]", "[[List Item]]", "[[Text Field]]", "[[Popup]]", "[[Menu]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Icon Picker]]", "[[Choice Picker]]", "[[Typography]]", "[[Typography#Rules|Desktop Font]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[State Layers]]", "[[Colour Roles]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[List]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]"]
---

# Font List

> [!info] Summary
> A searchable, virtualised list of the installed font families, each row drawn in its own face where the engine can draw it, inline or behind a button in a popup. Material Design 3 has no font picker; the note builds on the MD3 outlined text field, [Menus](https://m3.material.io/components/menus/overview) and [[List]]. Source of truth in code: the last section.

## Purpose

Let a person choose one font family for something they configure (a terminal, a launcher, a block) by seeing the families, finding one by name and choosing it with the keyboard or the pointer.

## When to use and not

- Use when: the value is the name of a font family.
- Do not use when: the choice is among fewer than about 8 fixed options ([[Choice Picker]], [[Menu]]); the value also needs weight and style (not built); the value is free text ([[Text Field]]).

## Anatomy

1. Trigger (popup variant): outlined button showing the family name in its own face and a chevron.
2. Layer ([[Popup]]): `surface_container` surface, 12 dp corners, 8 dp padding, level 2.
3. Search field ([[Text Field]]), role `searchbox`, focus on open.
4. List: virtual [[List]] of family rows (role `listbox`), with a [[Scrollbar and Scroll Container]] on the end edge.
5. Row: family name in its own face (`body_large` size), one line.
6. Sample sentence (optional): "The quick brown fox" under the name in `body_small`, `on_surface_variant`. Not built.
7. Empty note ("No fonts match") and fallback text field when families cannot be listed.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Inline | the list is part of a panel | search and list always visible |
| Popup | a form row | trigger button opens the layer; a pick closes it unless `Close_On_Pick` is false |
| Fallback | no font enumerator (no `fc-list`, failure, more than 5 s, empty) | an outlined text field for the family name and the reason under it replaces search, list and layer |

## States

| State | Visual change | Token values |
|---|---|---|
| Row rest | transparent | name `on_surface` |
| Row hover | state layer | `on_surface` at 8 percent ([[State Layers]]) |
| Row cursor | filled, ring when focused | `surface_container_highest`; [[Focus Ring]] |
| Row selected (the value) | filled | `secondary_container`, name `on_secondary_container` |
| Row not drawable | listed in the ordinary face, not the family face | same roles |
| Trigger rest, hover, focus, pressed | outline, state layer, ring | `outline` 1 dp; `on_surface` 8, 10, 10 percent |
| Disabled | popup does not open | 0.38 on content |
| Empty search | note | `on_surface_variant` |

## Tokens used

[[Colour Roles]], [[Shape]] (12 dp rows and layer), [[Elevation]] (level 2), [[Typography]] (`body_large` rows, face from the family), [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

| Part | default | compact | dense | Code today |
|---|---|---|---|---|
| Trigger height | 40 | 32 | 28 | 48 minimum |
| Search field height | 40 | 32 | 28 | text field default |
| List row | 40 | 32 | 24 | 40 at every level |
| Row horizontal padding | 12 | 8 | 4 | 12 |
| Layer padding | 8 | 8 | 4 | 8 |
| Visible rows (`Rows`) | 8 | 8 | 8 | 8 (3 to 16) |
| Width | 280 | 280 | 240 | 280 (160 to 640) |

The list height is `Rows` times the row height. Hit area at least 24 by 24 dp ([[ADR-0002 Desktop density levels and target sizes]]).

## Dimensions and defaults

The trigger follows the outlined [[Button]] (heights from the control height; padding mirrored for a trailing chevron).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| Trigger | height | `density.control_height` | 40 | 32 | 28 | [[Font List]] Sizing, [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | min width | - | 64 | 48 | 48 | [[Button]] Sizing | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | padding | `space.6` | 0 16 0 24 | 0 12 0 16 | 0 8 0 12 | [[Button]] Sizing; design choice, [[ADR-0002 Desktop density levels and target sizes]] #needs-verification-as-design-choice | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | border width | - | 1 | 1 | 1 | [[Button]] Variants (outlined) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | border color | `outline` | `outline` | `outline` | `outline` | [[Button]] Variants, [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]], [[Button]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 13/18/500/0.1 | [[Button]], [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger chevron | icon size | - | 18 | 18 | 16 | [[Iconography]] (icon next to a button label) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | min width | - | 160 | 160 | 160 | [[Font List]] Sizing (`Width` range 160 to 640; default 280, 240 at dense) | tess-ui: yes (FontListPanel Width option); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | padding | `space.3` | 8 8 8 8 | 8 8 8 8 | 4 4 4 4 | [[Font List]] Sizing | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | margin | - | N/A: the popup is placed by the anchor; it has no outer space of its own | N/A: same as default | N/A: same as default | [[Popup]] | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Layer | gap | `space.0` | 0 | 0 | 0 | [[Font List]] Sizing (search field above the list, no gap stated) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | corner radius | `shape.medium` | 12 | 12 | 12 | [[Font List]] Tokens used, [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | border width | - | 0 | 0 | 0 | [[Popup]] (separated by its level 2 shadow) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | border color | - | N/A: the layer draws no border; the level 2 shadow separates it | N/A: same as default | N/A: same as default | [[Font List]] Anatomy part 2 | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Layer | elevation | `elevation.level2` | 2 | 2 | 2 | [[Font List]] Tokens used, [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Search field | height | `density.control_height` | 40 | 32 | 28 | [[Font List]] Sizing, [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Search field | font | `body_large` | 16/24/400/0.5 | 14/20/400/0.25 | 13/18/400/0.25 | [[Text Field]] Tokens used, [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| List row | height | `density.row_height` | 40 | 32 | 24 | [[Font List]] Sizing, [[Spacing and Density]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| List row | padding | `density.row_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 4 0 4 | [[Font List]] Sizing, [[Spacing and Density]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| List row | margin | - | N/A: rows abut in the virtual list; the list sets no outer space per row | N/A: same as default | N/A: same as default | [[Font List]] Layout and overflow | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| List row | corner radius | `shape.medium` | 12 | 12 | 12 | [[Font List]] Tokens used, [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| List row | font | `body_large` | 16/24/400/0.5 | 14/20/400/0.25 | 13/18/400/0.25 | [[Font List]] Anatomy part 5, [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |

## Layout and overflow

- Rows are one line, end ellipsis, minimum width 0; the full family name is the accessible name and the tooltip text when truncated ([[10 Layout Overflow and Scrolling]]).
- Vertical scroll only, visible scrollbar when more than `Rows` families match ([[ADR-0003 Scrollbar rule]]); the scrollbar thumb is draggable.
- The list is virtual: it builds the rows in view plus three past each edge, so seven thousand families open at once. It opens scrolled so that the value shows, cursor on it.
- The trigger shows one line with end ellipsis; the chevron stays at the end edge.
- Text is vertically centred in the row.

## Behaviour

- Search: keeps families whose name contains every typed word, in any order, without regard to case; a name that starts with the first word comes first.
- Pointer: a press picks; the wheel scrolls; pressing the trigger again, Escape or a press outside closes the popup.
- Keyboard: focus starts in the search field when a popup opens.

| Where | Key | Action |
|---|---|---|
| Search field | Up, Down | move the cursor in the list (focus stays in the field) |
| Search field | Page Up, Page Down | move by `Rows` |
| Search field | Enter | pick the family under the cursor |
| Search field | Left, Right, Home, End, Space | text editing |
| List | Up, Down | one row |
| List | Page Up, Page Down | `Rows` rows |
| List | Home, End | first, last row |
| List | Enter, Space | pick |
| List | printable characters | next family starting with the typed text, buffer reset after 1 s |
| Popup | Escape | close, focus returns to the trigger |
| Popup | Tab | search, list, then out of the popup closes it |

- A pick writes `Value`, calls `On_Change` once and closes a popup unless `Close_On_Pick` is false.
- Touch: rows keep the 48 dp hit area in a touch context; drag scrolls.

## Tooltip and overlay behaviour

The trigger shows a tooltip with the full family name when the name is truncated (500 ms hover, immediate on keyboard focus; [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]). A truncated row shows its name on the name text only. No tooltip on the layer, the search field or the list container. The layer is a [[Popup]] ([[12 Overlays]]): focus moves to the search field on open and back to the trigger on close; Escape and an outside press close it.

## Motion

The layer fades in 150 ms and out in 100 ms ([[Motion]]); reduced motion 0 ms. Scrolling by keys jumps; no row animation.

## Accessibility

- The picker is a `group` named by `Label` (default "Font"). The trigger is a `button` named "Font: family" with `expanded`. The list is a `listbox` (code today: `list` named "Font families") of `option` rows (code: `listitem`) each named by its family and `selected` for the value. The search is a `searchbox` with the same label.
- Keys: the table above.
- Announcements: moving the cursor announces the family and "n of N"; a pick announces "family selected"; a search that finds nothing announces "No fonts match" once (role `alert`, polite); the fallback text field announces its reason.
- Contrast: row name on `secondary_container` uses `on_secondary_container` at least 4.5:1; the trigger border `outline` at least 3:1 against `surface` ([[Colour Roles]]).
- Target size: at least 24 by 24 dp at every density.
- A row shown in a decorative face stays legible: the accessible name is the plain family string, and the face is not the only carrier of the name.

## Dark and light

Roles only ([[Theme Following the System]]). Faces are theme independent.

## Defaults

Inline, `Rows` 8, `Width` 280, label "Font", placeholder "Choose a font", `Close_On_Pick` true, families from `fc-list : family` once with a 5 s limit, de-duplicated without regard to case and sorted without regard to case.

## Acceptance criteria

- [ ] AC-FNT-1 (geometry check): at default, compact and dense the trigger and search field are 40, 32 and 28 dp high and a list row is 40, 32 and 24 dp high, at scale 1.0 and 2.0.
- [ ] AC-FNT-2 (scripted input): typing "fira code" keeps exactly the families containing both words in any case; a family whose name starts with "fira" is first; an empty search lists all families.
- [ ] AC-FNT-3 (scripted input): in the search field Down moves the cursor one row without moving focus; Enter writes `Value` to that family, calls `On_Change` once and closes a popup.
- [ ] AC-FNT-4 (scripted input): in the list Home, End, Page Down give rows 0, N-1 and min(N-1, Rows); Space picks; typing "ro" within 1 s moves to the next family starting with "ro".
- [ ] AC-FNT-5 (scripted input): a popup opens with focus in the search field and the value row scrolled into view with the cursor on it; Escape closes it and focus is on the trigger within one frame.
- [ ] AC-FNT-6 (AT tree assertion): the picker is a `group` with a name; the list has role `listbox` or `list` with a name; each row is named by its family and `selected` equals the value; the trigger has `expanded` equal to the popup state.
- [ ] AC-FNT-7 (geometry check): 7000 families build at most `Rows` + 6 row nodes, and a scrollbar thumb is visible and draggable with length at least the minimum thumb length.
- [ ] AC-FNT-8 (pixel check): a 400 dp family name in a 200 dp row ends in `…` with no ink past the row's inner edge.
- [ ] AC-FNT-9 (scripted input): with no font enumerator the picker shows a text field and a reason and no list; typing a name writes `Value`.
- [ ] AC-FNT-10 (scripted input): a search that matches nothing shows the empty note and announces it once.
- [ ] AC-FNT-11 (scripted input): a tooltip on the trigger appears after 500 ms hover when its text is truncated, none over the layer background or the search field, and Escape, a press or a scroll removes it.
- [ ] AC-FNT-12 (review): the status of each Not built item (sample sentence, favourites, recent families, grouping, weights and styles, system fonts the engine cannot draw in their own face) is recorded in this note.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/FontList_View.tdl`, `FontListPanel_View.tdl`, `FontList_Stylesheet.tdl`, `FontListPanel_Stylesheet.tdl`, `tess-ui:src/tess_ui/font_controls.py`, `tess-ui:src/tess_ui/font_families.py`, `tess-ui:docs/components/font-lists.md` | partly meets. Passes AC-FNT-2, 3, 4, 5, 7, 9, 10 by documented behaviour. Fails AC-FNT-1 (trigger 48, row 40 at every level), AC-FNT-6 in part (`list` and `listitem` roles), AC-FNT-11 (no tooltip on the trigger) |
| tess-ui (dimensions) | `tess-ui:src/tess_ui/views/FontList_Stylesheet.tdl` | Differences in [[#Dimensions and defaults]]: trigger minimum 48 at all levels, spec 40, 32 and 28; list row 40 at all levels, spec 32 and 24 at compact and dense (AC-FNT-1); layer padding 8 at dense, spec 4; width 280 at dense, spec 240. Not settable from the project layer (no hook): the trigger gap 8 and chevron 24, panel gap 8, row height `Item_Height` 40 and row padding 12, which are inline in `FontList_View.tdl` and `FontListPanel_View.tdl` |
| tess-ui | Not built (component doc) | sample sentence in each row, favourites or recently used families, grouping by foundry or script, weights and styles of a family, system fonts the engine cannot draw (listed in the ordinary face) |
| tess-shell | `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`FontWidget`), `Main_View.tdl` | partly meets: the config app uses the popup variant; same gaps as tess-ui |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |
| Element has no MD3 counterpart | desktop apps pick installed fonts | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Trigger and rows 40, 32 and 28 or 24 dp (MD3 menu item 48 dp in Material Web) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Scrollbar visible when the list overflows | desktop pointer use | [[ADR-0003 Scrollbar rule]] |
| Tooltip on the trigger and truncated name only | owner feedback F2, F8 | [[ADR-0004 Tooltip rule]] |

## Sources

- tess-ui: `tess-ui:docs/components/font-lists.md`, `tess-ui:src/tess_ui/views/FontList_Stylesheet.tdl`, `tess-ui:src/tess_ui/views/FontListPanel_View.tdl`.
- WAI-ARIA APG listbox https://www.w3.org/WAI/ARIA/apg/patterns/listbox/ (Home, End, Page Up and Page Down, Space, type-ahead recommended for lists of more than seven options); combobox https://www.w3.org/WAI/ARIA/apg/patterns/combobox/ (search field with an owned list; not re-read #needs-verification).
- Material Web menu https://raw.githubusercontent.com/material-components/material-web/main/docs/components/menu.md (type-ahead buffer 200 ms); the 1 s buffer used here follows [[List]].
- WCAG 2.2 SC 2.5.8, 1.4.11, 4.1.3 (links in [[File Dialog]]).
