---
title: Menu Item
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, menu]
related: ["[[Menu]]", "[[Divider|Menu Separator]]", "[[Audio Outputs]]", "[[Tray Menu]]", "[[Popup]]", "[[12 Overlays]]", "[[List Item]]", "[[State Layers#Disabled scheme|Disabled State]]", "[[State Layers]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Menu Item

> [!info] Summary
> A Menu Item is one row of a [[Menu]]: an icon, the text, a key hint, an arrow when it opens a submenu, or a rule when it is a separator. It is the shell module behind the [menu item](https://m3.material.io/components/menus/overview) of Material Design 3. This note records the module; row geometry, keys and popup behaviour are specified once in [[Menu]]. Source of truth in code: see the last section.

## Purpose

Gives one command or choice in a menu a place, a name and an optional shortcut hint.

## When to use and not

- Use when: a row inside a [[Menu]], [[Audio Outputs]] or [[Tray Menu]].
- Do not use when: the control stands alone in a layout (use [[Button]]); a rule is all that is needed in a custom list ([[Divider|Menu Separator]]).

## Anatomy

1. Root: row box, role `MENUITEM` (`SEPARATOR` for a rule), `Menu_Item: true`.
2. Icon slot: 16 dp in code; the slot is kept even without an icon so labels align.
3. Label: part `::label`, grows.
4. Shortcut: part `::shortcut`, display only, in `on_surface_muted`.
5. Arrow: part `::arrow`, `mdi:chevron-right`, when a submenu exists.
6. Rule: part `::rule`, 1 dp, when `Separator` is true.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Command | Default | `On_Click` runs the action, then the whole menu closes |
| Submenu | `Submenu` names a Popup | opens to the right (left without room) after 250 ms rest or at a click; closes after 300 ms on another row; one open at a time, three levels deep |
| Separator | `Separator: true` | a rule between groups; no events, 9 dp high in code |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Text `on_surface` | [[Menu]] |
| Hover or lit by keys | Fill `outline` (code); spec: state layer 8 percent in `on_surface` | `on_surface` on `outline`: 4.12:1 dark, 4.54:1 light (the dark value fell from 4.91 when ADR-0025 raised the shell `outline`; 4.12 is below 4.5, one more reason the spec uses a state layer and not an `outline` fill) |
| Focus (keyboard) | The lit row is the focus indication (a row is no Tab stop; the Menu holds focus) | [[Menu]] |
| Pressed | Fill `primary` (code); spec: state layer 10 percent | `on_surface` on `primary`: 2.58:1 dark, 2.89:1 light (fails 4.5:1) |
| Disabled | Opacity 0.5; no click, no focus; no tooltip | [[State Layers#Disabled scheme|Disabled State]] |
| Submenu open | `expanded` true on the row | [[Menu]] |

## Tokens used

Roles and shape as [[Menu]]: row corner `small` 4 dp (code), text `label_large` or `body_medium`, icon colour `on_surface_variant`.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Row height | 40 | 32 | 28 | [[Menu]]; code: 28 (separator 9) |
| Icon | 24 | 20 | 20 | [[Menu]]; code: 16 |
| Horizontal padding | 12 | 8 | 4 | [[Menu]]; code: 10 |
| Icon-to-label gap | 8 | 8 | 4 | [[Menu]]; code: 8 |
| Separator | 9 | 9 | 9 | 1 dp rule with 4 dp above and below |

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| root | height | `density.menu_item_height` | 40 | 32 | 28 | [[Spacing and Density]]; code 28 | tess-ui: yes (style height); tess-shell: yes (Height); tre: n/a: element absent in tre |
| rule | height | - | 9 | 9 | 9 | [[Menu Item]] (Sizing, separator: 1 dp rule with 4 dp above and below); code 9 | tess-ui: yes (style height); tess-shell: yes (Height); tre: n/a: element absent in tre |
| root | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.2 SC 2.5.8 | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: n/a: element absent in tre |
| root | padding | `density.row_padding_x` | 0 12 0 12 | 0 8 0 8 | 0 4 0 4 | [[Spacing and Density]]; code 0 10 0 10 | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: n/a: element absent in tre |
| rule | padding | `space.2` | 4 0 4 0 | 4 0 4 0 | 4 0 4 0 | [[Menu Item]] (Sizing, separator); code 4 0 4 0 | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: n/a: element absent in tre |
| root | margin | - | N/A: the Menu container sets the outer space | N/A: same as the default column | N/A: as in Default | [[Menu]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: n/a: element absent in tre |
| root | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]]; code 8 | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: n/a: element absent in tre |
| root | border width | - | 0 | 0 | 0 | MD3 menu item https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu-item.scss; code sets none | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: n/a: element absent in tre |
| root | border color | - | N/A: a row has no border; the state is a fill | N/A: same as the default column | N/A: as in Default | MD3 menu item https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu-item.scss | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| rule | border width | - | 1 | 1 | 1 | [[Menu Item]] (Anatomy 6, 1 dp rule), [[Divider]] | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: n/a: element absent in tre |
| rule | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Roles]]; code `MenuItem::rule` fill `outline` | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| root | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]], [[Menu Item]] (Tokens used, 4 dp); code `$shape.small` | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: n/a: element absent in tre |
| label | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]], [[Menu Item]] (Tokens used); code body 14/20/400 | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| shortcut | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]], same type as the label; colour `on_surface_muted` | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| icon, arrow | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Menu]], [[Spacing and Density]]; code 16 | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: n/a: element absent in tre |
| root | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]]; the Menu container carries the elevation | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: n/a: element absent in tre |

## Layout and overflow

One line. The label has `Flex_Grow` and ends with an ellipsis when the row is narrower than the text; the hint never truncates before the label. Vertical centring of all parts in the row ([[10 Layout Overflow and Scrolling]]).

## Behaviour

- Pointer: hover lights, click runs the action and closes the whole menu; a click on a submenu row opens the submenu and runs nothing.
- Keyboard: the row is not a Tab stop; the Menu's keys move the lit row and run it ([[Menu]]); Right opens a submenu, Left closes it.
- Touch: tap runs; a submenu opens on tap.

## Tooltip and overlay behaviour

No tooltip on a row (ADR-0004: a row is never a trigger). The label carries the full text when cut. A submenu is a popup parented to the row's popup ([[Popup]], [[12 Overlays]]).

## Motion

No animation required; the lit row changes in one frame. Reduced motion: none to remove.

## Accessibility

- Roles: `MENUITEM`, `SEPARATOR` for a rule; `expanded` on a row that has a submenu.
- Name: `Label` else `Text`.
- Keys: as [[Menu]].
- Announcements: none beyond the screen reader's own.
- Contrast: text 4.5:1 in every state, including pressed (fails in code, see Status).

## Dark and light

Colours follow the scheme ([[Theme Following the System]]); the hover and pressed fills use `outline` and `primary` in all modes.

## Defaults

| Setting | Default |
|---|---|
| Row height | 28 in code |
| Icon | 16 in code |
| Submenu delays | 250 ms open, 300 ms close |

## Acceptance criteria

- [ ] AC-MOD-MIT-1 (AT tree assertion): a command row has role `MENUITEM` and a non-empty name; a separator has role `SEPARATOR`; a submenu row has `expanded` false and true while open.
- [ ] AC-MOD-MIT-2 (scripted input): click a command row: its action runs once and the whole menu closes; click a submenu row: the submenu opens and no action runs.
- [ ] AC-MOD-MIT-3 (scripted input): a pointer rest of 250 ms on a submenu row opens the submenu; 300 ms on another row closes it; never two submenus of one menu open.
- [ ] AC-MOD-MIT-4 (geometry check): a row is 40, 32, 28 dp high and its icon 24, 20, 20 dp at default, compact, dense; padding is 12, 8, 4 dp.
- [ ] AC-MOD-MIT-5 (contrast script): row text against the row fill in rest, hover and pressed is at least 4.5:1 in Light, Dark and High_Contrast.
- [ ] AC-MOD-MIT-6 (static check): no `MenuItem` carries a `Tooltip`.
- [ ] AC-MOD-MIT-7 (scripted input): a disabled row takes no click and no key and is skipped by Up and Down.
- [ ] AC-MOD-MIT-8 (pixel check): a label wider than its row ends with `…` and the shortcut hint stays visible.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/MenuItem/MenuItem_Module.tdl`, `Stylesheets/Default_Stylesheet.tdl` | partly meets: roles, `expanded`, submenu delays, separator, disabled, no tooltip (meets AC-MOD-MIT-1, -2, -3, -6, -7 by reading); row 28, icon 16, padding 10 literals (fails AC-MOD-MIT-4 at default and compact); pressed fill `primary` with `on_surface` text fails contrast (fails AC-MOD-MIT-5) |
| tess-shell | `tess-shell:src/tess_shell/shipped/MenuItem/MenuItem_Module.tdl` (dimensions) | differs: height 28 (spec 40, 32, 28), icon and arrow 16 (spec 24, 20, 20), padding 10 (spec 12, 8, 4), label weight 400 (spec 500); fails AC-MOD-MIT-4; letter spacing (tracking) has no hook in tess-shell |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (Menu and MenuItem) | exists |
| tess-ui | `tess-ui:src/tess_ui/views/` menu views | see [[Menu]] |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Row heights, icon size and padding by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Key hint is display only | keys are bound elsewhere | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- Material Web menu item tokens (container height 48 px, as cited in [[Spacing and Density]]): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-menu-item.scss
- WAI-ARIA Authoring Practices, menu and menubar: https://www.w3.org/WAI/ARIA/apg/patterns/menubar/
- Contrast computed from `Default_Theme.tdl` values with the WCAG relative luminance formula (https://www.w3.org/TR/WCAG22/#dfn-contrast-ratio).
