---
title: Tray Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, tray]
related: ["[[Tray Item]]", "[[Tray Menu]]", "[[Bar]]", "[[Popup]]", "[[Menu]]", "[[12 Overlays]]", "[[Scrollbar and Scroll Container]]", "[[Iconography#Fallback icon|Empty and Error States]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Tray Module

> [!info] Summary
> The Tray Module is the system tray: one [[Tray Item]] per application that registers a StatusNotifierItem, with the item's tooltip, its click actions and its own menu drawn by the shell. No Material Design 3 counterpart (Tesserae-specific; nearest pattern: a toolbar of [[Icon Button]]s). Source of truth in code: see the last section.

## Purpose

Gives applications a status icon and a menu in the Bar. The shell is a second tray host beside Plasma's.

## When to use and not

- Use when: the Bar needs a tray for StatusNotifierItem applications.
- Do not use when: the shell must act as the only tray host and no watcher exists (the module hides).

## Anatomy

1. Root: horizontal box, role `GROUP`, name `Tesserae Shell tray` (so a screen reader user can tell it from Plasma's tray).
2. [[Tray Item]] per shown item.
3. [[Tray Menu]] popups `Tray_Menu`, `Tray_Menu_2`, `Tray_Menu_3`, provided by the shell.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Active items only | Default | `show_passive` false |
| With passive items | Debugging | `show_passive` true |

## States

| State | Visual change | Token values |
|---|---|---|
| Items present | One item per registered application, in registration order | [[Tray Item]] |
| Hover, focus, pressed, attention | Per item | [[Tray Item]] |
| Menu open | The popup shows below the clicked icon; the icon keeps its hover look | [[Tray Menu]] |
| Hidden (service absent) | No StatusNotifierWatcher, no item or no host registration: hidden. Hidden means `Visible: false` on the root: the module takes no space in the [[Bar]], no spacing is left beside it, no placeholder is drawn and the root is absent from the accessibility tree. | root `Visible: <| available and has_items |>` |
| Error | A failed menu fetch opens no menu and logs one warning a minute per service | not applicable |

## Tokens used

No tokens of its own; the items carry them ([[Tray Item]]). Gap between items `space.2` (4 dp) in spec (code: `spacing` 6).

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Item hit area | 32 | 24 | 24 | [[Tray Item]] ([[ADR-0024 Shell tray and task item sizes]]) |
| Gap between items | 4 | 4 | 4 | param `spacing` (code default 6) |
| Icon | 20 | 18 | 18 | param `icon_size` (code default 18); [[ADR-0024 Shell tray and task item sizes]] |

## Dimensions and defaults

The row is transparent and owns only the gap between items; every other size of an item is in [[Tray Item]]. Rows marked design choice carry #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| root | height | - | 32 | 24 | 24 | Sizing table of this note (item hit area), [[Tray Item]], [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| root | min height | `target.min` | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| root | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | `tess-shell:src/tess_shell/shipped/Tray/Tray_Module.tdl` (no padding set) | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| root | margin | - | N/A: the Bar sets the gap between modules | N/A: as in Default | N/A: as in Default | [[Bar]], [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| root | gap | `space.2` | 4 | 4 | 4 | Sizing table of this note (param `spacing`), design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| root | border width | - | 0 | 0 | 0 | [[Tray Item]], this note Tokens section: no tokens of its own | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| root | border color | - | N/A: the row draws no border; the items do | N/A: as in Default | N/A: as in Default | [[Tray Item]] | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| root | corner radius | - | N/A: the row draws no surface; the items do | N/A: as in Default | N/A: as in Default | [[Tray Item]], [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| root | font | - | N/A: the row draws no text; the items show icons only | N/A: as in Default | N/A: as in Default | [[Typography]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| root | icon size | - | N/A: the row holds no icon; the items do | N/A: as in Default | N/A: as in Default | [[Tray Item]], [[Iconography]] | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| root | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]], this note Tokens section | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| item | height | - | 32 | 24 | 24 | Sizing table of this note (item hit area), [[Tray Item]], [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| item | min width | `target.min` | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]]; 48 in a touch context | tess-ui: yes (style min_width); tess-shell: yes (Min_Width); tre: yes (min_width) |
| item | icon size | - | 20 | 18 | 18 | Sizing table of this note (param `icon_size`), [[Iconography]], [[Spacing and Density]] | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |

## Layout and overflow

A horizontal row, no wrapping. When the items do not fit the Bar slot the row clips at the slot edge; spec: overflow items move into a Tray overflow popup (not in v1; candidate request). The menu popup is at most 60 percent of the output height and scrolls ([[Scrollbar and Scroll Container]]). Vertical centring.

## Behaviour

- Pointer: as [[Tray Item]]. The menu opens beside the icon that was clicked (the event carries the icon's rectangle).
- Keyboard: Tab visits each item; keys per [[Tray Item]]; Left and Right move along the row.
- Touch: as [[Tray Item]].
- Updates: from the watcher's and items' signals (`NewIcon`, `NewToolTip`, `NewTitle`, `NewStatus`); no timer.

## Tooltip and overlay behaviour

The row has no tooltip; each [[Tray Item]] has one. The menu is a popup window opened in response to input on a Bar surface, with a focus grab, closed by an outside press, Escape or a pick; focus returns to the item ([[Popup]], [[12 Overlays]]). While a menu is open no item tooltip shows.

## Motion

No animation. Reduced motion: none to remove.

## Accessibility

- Roles: `GROUP` named `Tesserae Shell tray`; items `BUTTON`.
- Keys: as Behaviour.
- Announcements: none. An item whose status changes to `NeedsAttention` changes its name; it is not announced in v1.
- Targets as [[Tray Item]].

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `icon_size` | 18 dp in code |
| `show_passive` | false |
| `spacing` | 6 dp in code |

## Acceptance criteria

- [ ] AC-MOD-TRY-1 (AT tree assertion): the row has role `GROUP` named `Tesserae Shell tray`; every child has role `BUTTON` and a non-empty name.
- [ ] AC-MOD-TRY-2 (scripted input): no watcher or no item: root `Visible` false, width 0, absent from the accessibility tree, Bar spacing unchanged; a watcher appearing shows the module.
- [ ] AC-MOD-TRY-3 (scripted input): an item with status Passive is hidden unless `show_passive`; `NewIcon`, `NewToolTip`, `NewTitle` and `NewStatus` each update the matching value after one fresh read.
- [ ] AC-MOD-TRY-4 (scripted input): Tab visits each item once and leaves; the Menu key on an item opens its menu below the item and Escape returns focus to the item.
- [ ] AC-MOD-TRY-5 (scripted input): hover two different items in turn: at most one tooltip layer at any time.
- [ ] AC-MOD-TRY-6 (static check): the Root carries no `Tooltip`.
- [ ] AC-MOD-TRY-7 (geometry check): item hit areas are 32, 24, 24 dp at default, compact, dense and at least 24 dp ([[ADR-0024 Shell tray and task item sizes]]); gaps are 4 dp; hit areas do not overlap.
- [ ] AC-MOD-TRY-8 (scripted input): opening a menu of 100 entries shows the popup within 100 ms (budget of the vault note) and the popup height is at most 60 percent of the output height.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Tray/Tray_Module.tdl`, `Tray_Module.py`, `tess-shell:src/tess_shell/services/tray.py`, `tess-shell:src/tess_shell/schema/default_popups.py` | partly meets: group name, hidden without watcher or items, passive rule, the three menu popups at max 60 percent (meets AC-MOD-TRY-1, -2, -3, -8 by reading); no key path to the menu (fails AC-MOD-TRY-4); sizes literal 18 and 6 (fails AC-MOD-TRY-7); no overflow rule. Dimensions: icon 18 (spec 24/20/20), gap 6 (spec 4), item hit area 24 (18 icon plus 3 padding each side; spec 40/32/28); padding 0 and no border or elevation meet the table |
| shell-vault | `shell-vault:40 Specifications/Modules/Tray Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status area | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Hit areas 32, 24, 24 dp and icons 20, 18, 18 dp (items follow [[Tray Item]]) | the shell keeps today's compact sizes; 24 dp pointer minimum | [[ADR-0024 Shell tray and task item sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
- StatusNotifierItem and dbusmenu specifications are the shell's integration sources: `shell-vault:40 Specifications/Modules/Tray Module.md`.
