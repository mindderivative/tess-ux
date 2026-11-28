---
title: Menu
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, overlay, menu, keyboard]
related: ["[[12 Overlays]]", "[[Popup]]", "[[Tooltip]]", "[[List Item]]", "[[Icon Button]]", "[[Button]]", "[[Scrollbar and Scroll Container]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Colour Roles]]", "[[Elevation]]", "[[Shape]]", "[[Typography]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0009 State layer percentages]]"]
---

# Menu

> [!info] Summary
> A menu shows a list of commands or choices on a temporary surface next to the control that opened it. Material Design 3 counterpart: [Menus](https://m3.material.io/components/menus/overview) (container `surface_container`, 4 dp corners, elevation level 2, list items of 48 dp). In Tesserae a menu is a [[Popup]] with menu content and menu keyboard behaviour. Source of truth in code: see the last section.

## Purpose

Offer a short list of actions or one-of-many choices, reachable by pointer and fully by keyboard.

## When to use and not

- Use when: the user picks one command or choice from a list of up to about 15 entries, opened from a button, a right click, a keyboard shortcut or a tray icon.
- Do not use when: the list is long and searchable (use a search list with a text field, see [[Popup]] flyout and [[List]]); the choices must always be visible (use [[List]] or segmented controls); the content is not commands (use [[Popup]] flyout).

## Anatomy

1. Container: the popup body.
2. Item: leading icon or check slot, label, trailing text (shortcut), trailing icon or submenu chevron.
3. Divider: 1 dp line between groups.
4. Heading: non-interactive group title.
5. Submenu: a menu opened beside an item.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Plain | Actions | Items run a command and close the menu |
| Check | Independent toggles | Items flip a check, the check shows in the leading slot |
| Radio | One of many | One item is checked |
| With submenus | Nested commands | Depth at most 3 levels, one submenu open at a time |

## States

| State | Visual change | Token values |
|---|---|---|
| Enabled | Label `on_surface`, leading and trailing icon `on_surface_variant` | verified tokens, see Sources |
| Hover | State layer `on_surface` | 8 percent ([[ADR-0009 State layer percentages]], matches `md.comp.menu.list-item.hover.state-layer.opacity`) |
| Focus (keyboard) | State layer `on_surface`; the highlighted item is the keyboard focus indicator, drawn inside the item in colour `secondary` (menu token `focus-indicator-color`, inner offset per `md.sys.state.focus-indicator`) | 10 percent |
| Pressed | State layer `on_surface` | 10 percent |
| Selected (check or radio on) | Container `secondary_container`, label `on_secondary_container` | verified tokens |
| Disabled | Label and icons at 38 percent of `on_surface`; no state layer; skipped by keyboard | 38 percent |

Pointer hover and keyboard highlight share one highlighted item: moving the pointer onto an item moves the highlight, and arrow keys move it away from the pointer.

## Tokens used

| Part | Role or token |
|---|---|
| Container colour | `surface_container` |
| Shape | `extra_small` (4 dp) |
| Elevation | level 2 (3 dp in MD3 numbers); shadow colour `shadow` |
| Label | `on_surface`, `label_large` (14/20; `title_dense` 13/18 at dense) |
| Icons | `on_surface_variant`, trailing submenu indicator `on_surface_variant` |
| Divider | `surface_variant` (token `md.comp.menu.divider.color`) |
| Selected item | container `secondary_container`, content `on_secondary_container` |

See [[Colour Roles]], [[Shape]], [[Elevation]], [[Typography]], [[State Layers]], [[Focus Ring]].

## Sizing and density

Item and spacing values per density level, from [[Spacing and Density]] (binding numbers of [[ADR-0002 Desktop density levels and target sizes]]):

| Measure | default | compact | dense |
|---|---|---|---|
| Single-line item height | 40 dp | 32 dp | 28 dp |
| Item horizontal padding | 12 dp | 8 dp | 4 dp |
| Icon-to-label gap | 8 dp | 8 dp | 4 dp |
| Leading and trailing icon size | 24 dp | 20 dp | 20 dp |
| Container vertical padding | 8 dp | 4 dp | 4 dp |
| Divider thickness | 1 dp | 1 dp | 1 dp |

- Minimum menu width 112 dp, maximum 280 dp #needs-verification (112 dp is in Material Web `menu.scss`; 280 dp is the tess-ui bound, MD3 spec page not readable).
- The smallest pointer target is 24 dp (WCAG 2.2 SC 2.5.8); dense items (28 dp) meet it. In touch contexts the item height is 48 dp, which is also the MD3 value ([[ADR-0002 Desktop density levels and target sizes]]).
- Container vertical padding 8 dp default, 4 dp at compact and dense #needs-verification-as-design-choice (MD3 token not read).

## Dimensions and defaults

Values agree with Sizing and density above. Compact and dense paddings and the divider margin are Tesserae choices #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | N/A: content-sized, the sum of the items, clamped to the available height | N/A: same as the default level | N/A: same as the default level | [[Menu]] Layout and overflow | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container | min width | - | 112 | 112 | 112 | https://github.com/material-components/material-web/blob/main/menu/internal/_menu.scss | tess-ui: yes (style min_width); tess-shell: yes (Min_Width); tre: yes (min_width) |
| container | padding | `space.3`, `space.2` | 8 0 8 0 | 4 0 4 0 | 4 0 4 0 | design choice, proposed ADR: menu container padding per density, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| container | margin | - | N/A: the opener places the menu with the Popup gap; the menu has no margin of its own | N/A: same as the default level | N/A: same as the default level | [[Popup]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| container | gap | - | N/A: items stack with no gap; each item carries its own height | N/A: same as the default level | N/A: same as the default level | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| container | border width | - | 0 | 0 | 0 | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu.scss | tess-ui: yes (style border_width); tess-shell: yes (Border_Width in the Popup Style); tre: yes (border_width) |
| container | border color | - | N/A: the container draws no border; the shadow separates it | N/A: same as the default level | N/A: same as the default level | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu.scss | tess-ui: yes (style border_color); tess-shell: yes (Border_Color in the Popup Style); tre: yes (border_color) |
| container | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius in the Popup Style); tre: yes (corner_radius) |
| container | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation in the Popup Style); tre: yes (shadows) |
| item | height | `density.menu_item_height` | 40 | 32 | 28 | [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| item | min height | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| item | padding | `density.row_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 4 0 4 | [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| item | margin | - | N/A: the item fills the container width; the container padding sets the outer space | N/A: same as the default level | N/A: same as the default level | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| item | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| item | corner radius | `shape.none` | 0 | 0 | 0 | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu-item.scss | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| item | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 13/18/500/0.1 | [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| item | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Iconography]], [[Spacing and Density]] | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| item | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| divider | height | - | 1 | 1 | 1 | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu.scss | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| divider | margin | `space.3`, `space.2` | 8 0 8 0 | 4 0 4 0 | 4 0 4 0 | design choice, proposed ADR: menu container padding per density (MD3 divider margin 8: https://github.com/material-components/material-web/blob/main/menu/internal/_menu.scss) | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| divider | border color | `surface_variant` | `surface_variant` | `surface_variant` | `surface_variant` | [[Colour Roles]], md.comp.menu.divider.color | tess-ui: yes (style background); tess-shell: yes (Fill of the rule Rectangle); tre: yes (background) |

## Layout and overflow

- Width follows the widest item, clamped to 112 to 280 dp. A label wider than the item area truncates with an ellipsis at the end; the accessible name keeps the full label. Menu items do not wrap.
- Height follows the items. When the menu would exceed the available height (the project maximum, for example 60 percent of the output height) it is clamped and scrolls. A scrollbar thumb is visible on overflow ([[ADR-0003 Scrollbar rule]]) and the keyboard scrolls by moving the highlighted item into view.
- Placement: opens `below` its anchor, start-aligned, 0 dp gap; flips above when there is no room below and more room above; then slides to stay inside the window or output. A submenu opens beside its item (`end`), flipping to `start` when there is no room.
- Trailing text (shortcuts) is right-aligned in the item and never truncated before the label.

## Behaviour

- Pointer: click or press-and-release on an item runs it and closes the whole menu; disabled items do nothing. Hover on an item highlights it. Hover rest on a submenu item opens the submenu after 250 ms; hover rest on another item of the same menu closes the open submenu after 300 ms (shell values; Material Web uses 400 ms for both, see Sources). Click on a submenu item opens it at once. Outside press dismisses and is consumed ([[Popup]]).
- Keyboard (when the menu has focus):
  - Down Arrow, Up Arrow: move the highlight to the next or previous enabled item, wrapping at the ends. Disabled items, dividers and headings are skipped.
  - Home, End: first and last enabled item.
  - A printable character: move to the next enabled item whose label starts with it (case-insensitive, wrapping). Further characters within 500 ms extend the prefix #needs-verification-as-design-choice (Material Web default buffer 200 ms).
  - Enter, Space: run the highlighted item; on a submenu item open its submenu.
  - Right Arrow (Left in right-to-left): open the submenu of the highlighted item and highlight its first enabled item.
  - Left Arrow (Right in right-to-left), Escape: close the current submenu and return the highlight to its parent item; Escape in the root menu closes it and returns focus to the opener. Escape closes one level.
  - Tab, Shift+Tab: close all menus and move focus out of the menu, to the control after (before) the opener.
- On open, focus moves to the menu and the first enabled item is highlighted, whether opened by pointer or keyboard. The focus ring (keyboard focus indicator) is visible only when opened by keyboard.
- Touch: tap an item runs it; a long press on a control may open a context menu.

## Tooltip and overlay behaviour

A menu is a non-modal [[Popup]]: scrim none, one popup at a time (a submenu chain counts as one), outside click closes and is consumed, focus returns to the opener on close. Menu items do not show tooltips by default; if an item's label is truncated, the full label is the item's accessible name ([[Tooltip]] rule: the tooltip never is the only source).

## Motion

No animation is required. Where a project animates, open uses a fade or scale from [[Motion]] `short3` to `short4` and close is instant #needs-verification-as-design-choice. With reduced motion on, open and close are instant.

## Accessibility

- Role `menu` for the container, named by the opener's label; items `menuitem`; check items `menuitemcheckbox` with `checked`; radio items `menuitemradio`; a submenu parent has `expanded` set while its submenu is open; disabled items expose `disabled`.
- Keys: the table above (WAI-ARIA Authoring Practices menu pattern, see Sources).
- Contrast: `on_surface` on `surface_container` at least 4.5:1; disabled items are exempt from contrast requirements (WCAG) but remain at 38 percent; the highlight (state layer) must not reduce label contrast below 4.5:1 (check with the 10 percent layer applied).
- Focus indicator: the highlighted item is the keyboard focus indicator; on `forced-colors` or high contrast it also carries a 3 dp outline #needs-verification-as-design-choice.
- No keyboard trap: Escape and Tab leave the menu (WCAG 2.2 SC 2.1.2).

## Dark and light

All roles come from the scheme ([[Theme Following the System]]); state layers use `on_surface` so they work in both schemes. The container stays opaque (a frosted variant with 72 percent container colour and 20 px backdrop blur exists in tess-ui; it is optional and must keep text contrast at least 4.5:1 over any background, which is not guaranteed: see AC-MEN-15).

## Defaults

| Setting | Default |
|---|---|
| Density | per project (config-style tools `compact`) |
| Width | 112 to 280 dp, content-sized |
| Placement | below, start, flip, slide |
| Scrim | none |
| Focus on open | first enabled item |
| Submenu open delay, close delay | 250 ms, 300 ms |
| Typeahead buffer | 500 ms |
| Maximum submenu depth | 3 |

## Acceptance criteria

- [ ] AC-MEN-1 (geometry check, density): open a menu with plain single-line items at each density level; each item height measures 40 / 32 / 28 dp ±0.5 (default / compact / dense); in touch context 48 dp.
- [ ] AC-MEN-2 (geometry check, width): a menu with one short item is 112 dp wide; with a 400 dp label it is 280 dp wide #needs-verification (280) and the label shows an ellipsis; its accessible name is the full label.
- [ ] AC-MEN-3 (token test, spacing): item horizontal padding 12 / 8 / 4 dp, icon-to-label gap 8 / 8 / 4 dp, icon size 24 / 20 / 20 dp, container vertical padding 8 / 4 / 4 dp, divider 1 dp, for default / compact / dense.
- [ ] AC-MEN-4 (pixel check, look): in light and dark schemes, the container pixel equals `surface_container` (alpha 255), container radius 4 dp, elevation level 2; label colour `on_surface`, icon colour `on_surface_variant`; selected item container `secondary_container` with label `on_secondary_container`; no pixel outside the menu changes when it opens (diff of the window outside the menu and shadow area is 0, so no scrim).
- [ ] AC-MEN-5 (pixel check, states): the item pixel under hover equals `on_surface` blended at 8 percent over the container; focus 10 percent; pressed 10 percent (±1 per channel).
- [ ] AC-MEN-6 (scripted input, disabled): a disabled item draws label and icon at 38 percent alpha; a click on it does nothing and the menu stays open; Down Arrow never highlights it; a typeahead character matching only a disabled item moves nowhere.
- [ ] AC-MEN-7 (scripted input, arrows): with items A, B (disabled), C highlighted at A: Down highlights C, Down wraps to A, Up wraps to C. Pass: highlighted id after each key equals the expectation.
- [ ] AC-MEN-8 (scripted input, Home and End): Home highlights the first enabled item and End the last enabled item, with the highlight starting anywhere; in a menu starting with a disabled item Home skips it.
- [ ] AC-MEN-9 (scripted input, typeahead): with items Apple, Avocado, Banana: typing "b" highlights Banana; typing "a" highlights Apple, "a" again Avocado, "a" again wraps to Apple; "a" then "v" within 1000 ms highlights Avocado; typing "z" changes nothing. Pass: highlighted id after each key.
- [ ] AC-MEN-10 (scripted input, activation): Enter on the highlighted item runs its action once and closes the menu; Space does the same; focus returns to the opener. Check mode: Enter flips the check and (project setting) closes the menu.
- [ ] AC-MEN-11 (scripted input, Escape and Tab): in a menu with an open submenu, Escape closes the submenu and highlights its parent item; Escape again closes the menu and focus is the opener. Tab closes all levels and the focused node is the control after the opener.
- [ ] AC-MEN-12 (scripted input, submenu): Right Arrow, Enter and Space on a submenu item open it with its first enabled item highlighted; Left Arrow closes it. Under a fake clock, hover rest of 249 ms on a submenu item opens nothing, 251 ms opens it; moving hover rest to another item of the parent closes it after 300 ms ±17 ms; the third level opens, a fourth is not offered; only one submenu is open at a time. In a right-to-left locale Left opens and Right closes.
- [ ] AC-MEN-13 (geometry check, placement): the menu opens below its anchor with its start edge aligned and 0 dp gap; with the anchor at the bottom edge of the window it opens above; its rectangle is inside the window in every case; a submenu opens at the item's end edge and flips to the start side when it does not fit.
- [ ] AC-MEN-14 (scripted input, open focus): after opening by pointer or by keyboard, the first enabled item is highlighted within one frame and keyboard events reach the menu; the focus ring is shown only when opened by keyboard.
- [ ] AC-MEN-15 (contrast script): `on_surface` on `surface_container`, label at the highlighted state (container plus 10 percent `on_surface`), and `on_secondary_container` on `secondary_container` each at least 4.5:1 in light and dark; the frosted variant over the worst-case backdrop (white and black) at least 4.5:1, or the variant is not offered.
- [ ] AC-MEN-16 (scripted input, scrolling): a menu with 100 items in a window 300 dp high is clamped to the available height with a visible scrollbar thumb; pressing Down 50 times keeps the highlighted item fully visible; Home scrolls to the top and End to the bottom.
- [ ] AC-MEN-17 (AT tree assertion): the menu node has role `menu` and a name; items have role `menuitem`, check items `menuitemcheckbox` with `checked`, submenu parents `expanded`, disabled items `disabled`; dividers and headings are not focusable.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Menu_View.tdl`, `Menu_Stylesheet.tdl`, `MenuItem_View.tdl`, `MenuItem_Stylesheet.tdl`, `tess-ui:src/tess_ui/overlays.py` (`Menu`), `tess-ui:docs/components/menus.md`, tests `tess-ui:tests/test_menu.py`, `tess-ui:tests/test_menu_item.py` | Partly meets. Fails AC-MEN-1 and AC-MEN-3 (item height 48 literal at every size, padding 12, gap 12, no density), AC-MEN-14 (`Focus_First` default false: a pointer-opened menu is not focused), AC-MEN-12 in part (submenu opens by press or Right, no hover timer documented, no third-level limit stated), AC-MEN-16 not verified, AC-MEN-8, AC-MEN-11 (Tab) not documented. Meets in part: AC-MEN-2 (width held 112 to 280), AC-MEN-4 (surface `surface_container`, radius 4, elevation 2, 8 above and below, label `on_surface`, icon `on_surface_variant`), AC-MEN-6 (dimmed, not focusable, does not respond; 38 percent not verified), AC-MEN-7, AC-MEN-9 (arrows and typing the start of a label jump, tested), AC-MEN-10, AC-MEN-11 (Escape closes the submenu first, tested). |
| tess-shell | `tess-shell:src/tess_shell/shipped/Menu/Menu_Module.tdl`, `MenuItem/MenuItem_Module.tdl`, `tess-shell:src/tess_shell/surfaces/popup.py` (`_menu_key`, `OPEN_REST_MS` 250, `CLOSE_REST_MS` 300), `tess-shell:src/tess_shell/schema/default_popups.py`, tests `tess-shell:tests/test_menu.py`, `tess-shell:tests/test_popup.py` | Partly meets. Meets AC-MEN-7 and AC-MEN-8 (Up and Down round the ends over a disabled row, Home and End), AC-MEN-10, AC-MEN-11 in part (Escape closes the innermost level and gives focus back; Tab not specified), AC-MEN-12 (Right opens, Left closes, 250 and 300 ms, 3 levels, one at a time; right-to-left not specified). Fails AC-MEN-1 and AC-MEN-3 (item 28 dp literal, padding 10, spacing 8, icon 16, container padding 4, no density), AC-MEN-2 (minimum width 160 not 112), AC-MEN-4 and AC-MEN-5 (`surface_raised`, radius 8 literal; hover is a `outline` background, pressed `primary`, no state layers), AC-MEN-6 (disabled at 0.5 opacity), AC-MEN-9 (no typeahead found), AC-MEN-14 in part. |
| tre | `tre:docs/reference/layers.md`, `tre:docs/reference/node.md` (role) | Not applicable as a component: no menu node, item model, arrow keys, typeahead or submenu timing in the engine; only `role="menu"`, `menuitem`, `dismiss` and layers. All menu behaviour is framework code. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |
| Item height 40 / 32 / 28 dp (MD3: 48 dp) | Desktop density with a 24 dp minimum target; 48 dp kept for touch | [[ADR-0002 Desktop density levels and target sizes]] |
| State layers 8, 10, 10 percent on items | Same as MD3; the shell has none yet (gap, not a promise) | [[ADR-0009 State layer percentages]] |
| Tab closes the menu | WAI-ARIA Authoring Practices menu pattern; Material Web closes on focusout | [[Deviations from MD3]] |
| Typeahead buffer 500 ms, submenu hover delays 250 and 300 ms | Material Web defaults are 200 ms and 400 ms; shell values are built and decided in the shell vault | [[Deviations from MD3]] |

## Sources

- Menu tokens (container `surface-container`, elevation `level2`, shape `corner-extra-small`, selected container `secondary-container`, selected label `on-secondary-container`, item container height 48 px, leading and trailing icon size 24 px, disabled opacity 0.38, divider height 1 px, divider colour `surface-variant`, state layer colour `on-surface` with the state opacities, focus indicator colour `secondary`), verified: `https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu.scss`; baseline set: `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-menu.scss`.
- Minimum menu width 112 px, divider margin 8 px: `https://github.com/material-components/material-web/blob/main/menu/internal/_menu.scss`.
- Keyboard and timing implementation (arrow, Home, End navigation keys; wrapping on by default; typeahead buffer 1000 ms (as in [[11 Interaction]]); sub-menu hover open and close delay 400 ms; Escape closes one menu; Right, Left, Space, Enter open and close submenus, right-to-left aware; default focus first item): `https://github.com/material-components/material-web/blob/main/menu/internal/menu.ts` and `.../submenu/sub-menu.ts`.
- WAI-ARIA Authoring Practices menu and menubar pattern (Home, End, printable character, Escape closes and returns focus, Tab and Shift+Tab move focus out and close all menus): `https://www.w3.org/WAI/ARIA/apg/patterns/menubar/`; menu button: `https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/`.
- Shell menu behaviour and keys: `tess-shell:src/tess_shell/shipped/Menu/Menu_Module.tdl`, `MenuItem_Module.tdl`; `shell-vault:50 Design System/Standard Modules.md` (Menu and MenuItem).
- tess-ui menu documentation: `tess-ui:docs/components/menus.md`.
