---
title: Tray Item
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, tray]
related: ["[[Tray Module]]", "[[Tray Menu]]", "[[Iconography#Icon sizes|Icon]]", "[[Icon Button]]", "[[Iconography#Icon set|Icons]]", "[[Focus Ring]]", "[[State Layers]]", "[[Iconography#Fallback icon|Empty and Error States]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Tray Item

> [!info] Summary
> A Tray Item is one icon of the [[Tray Module]]: an application's StatusNotifierItem icon with a tooltip and the item's click actions. The nearest Material Design 3 counterpart is the [icon button](https://m3.material.io/components/icon-buttons/overview). Source of truth in code: see the last section.

## Purpose

Gives an application a status icon in the Bar with its title and text on hover, and a click, secondary click and wheel for the application.

## When to use and not

- Use when: the [[Tray Module]] shows an item.
- Do not use when: a built-in shell action is needed (use [[Icon Button]]).

## Anatomy

1. Root: box, class `tray_item`, role `BUTTON`, name from `label`, description from `description`.
2. Icon: [[Iconography#Icon sizes|Icon]] (SVG document or pixels), `size` 18 dp default.
3. Attention look: the `:selected` look, a 2 px `warning` border.
4. Tooltip: a rich tooltip with the title (weight 600) and the text.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Passive | Status `Passive` | hidden unless `show_passive` |
| Active | Default | shown |
| Needs attention | Status `NeedsAttention` | attention look and the word in the name |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Icon only | [[Iconography#Icon sizes|Icon]] |
| Hover | Fill `surface_raised` (code); spec: state layer 8 percent | [[State Layers]] |
| Focus (keyboard) | Focus ring 3 dp, 2 dp offset; not built | [[Focus Ring]] |
| Pressed | State layer 10 percent | [[State Layers]] |
| Attention | 2 px `warning` border (code); spec: the border plus a dot of 6 dp so the cue is not colour alone | `warning` 10.02:1 dark, 5.51:1 light |
| Disabled | Not applicable | not applicable |
| Icon missing | Broken-image icon, one warning ([[Iconography#Fallback icon|Empty and Error States]]) | [[Iconography#Icon set|Icons]] |

## Tokens used

Roles: `on_surface` icon, `surface_raised` fill, `warning` border. Tooltip: rich variant ([[Tooltip]]): `surface_container`, elevation 2, subhead `title_small`, text `body_medium`.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Hit area (square) | 32 | 24 | 24 | shell sizes, not the [[Icon Button]] container ([[ADR-0024 Shell tray and task item sizes]]); 24 dp is the pointer minimum; code today: 24 by 24 at every level |
| Icon | 20 | 18 | 18 | shell sizes ([[ADR-0024 Shell tray and task item sizes]]); code today: 18 |
| Gap between items | 4 | 4 | 4 | code: `spacing` 6 |

## Dimensions and defaults

The item is the icon-button geometry of [[Icon Button]] by density; the attention dot is a design choice #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| root | height | - | 32 | 24 | 24 | [[ADR-0024 Shell tray and task item sizes]]; 24 dp pointer minimum, [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height); tre: n/a: element absent in tre |
| root | min width | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.2 SC 2.5.8 | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Width); tre: n/a: element absent in tre |
| root | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.2 SC 2.5.8 | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Height); tre: n/a: element absent in tre |
| root | padding | `space.*` | 6 6 6 6 | 3 3 3 3 | 3 3 3 3 | container minus icon, halved ([[ADR-0024 Shell tray and task item sizes]]); code 3 3 3 3 | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Padding); tre: n/a: element absent in tre |
| root | margin | - | N/A: the Tray Module sets the space between items | N/A: same as the default column | N/A: as in Default | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Margin); tre: n/a: element absent in tre |
| root | gap | `space.2` | 4 | 4 | 4 | gap between items, [[Spacing and Density]]; code 6 | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Spacing); tre: n/a: element absent in tre |
| root | border width | - | 0 | 0 | 0 | MD3 icon button https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-icon-button.scss | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: n/a: element absent in tre |
| root (attention) | border width | - | 2 | 2 | 2 | code `tess-shell:src/tess_shell/shipped/Tray_Item/Tray_Item_Module.tdl` (2 px) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: n/a: element absent in tre |
| root | border color | - | N/A: no border at rest | N/A: same as the default column | N/A: as in Default | MD3 icon button https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-icon-button.scss | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| root (attention) | border color | `warning` | `warning` | `warning` | `warning` | [[Colour Roles]], [[Tray Item]] (States) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| root | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]]; half the container; code 6 | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: n/a: element absent in tre |
| attention dot | height | - | 6 | 6 | 6 | design choice, proposed ADR: tray attention cue not by colour alone; [[Tray Item#States]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height); tre: n/a: element absent in tre |
| icon | font | - | N/A: the icon draws no text | N/A: same as the default column | N/A: as in Default | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| tooltip title | font | `title_small` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Tooltip]] (rich, geometry does not scale with density) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| tooltip text | font | `body_medium` | 14/20/400/0.25 | 14/20/400/0.25 | 14/20/400/0.25 | [[Tooltip]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| icon | icon size | - | 20 | 18 | 18 | [[ADR-0024 Shell tray and task item sizes]]; code 18 | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width, Height of the SVG block); tre: n/a: element absent in tre |
| root | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: n/a: element absent in tre |
| tooltip | elevation | `elevation.level2` | 2 | 2 | 2 | [[Tooltip]], [[Elevation]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: n/a: element absent in tre |

## Layout and overflow

The item is square; the icon is centred. Application icons that are not square are fitted (`xMidYMid meet`) and never stretched. A tooltip text longer than the maximum width wraps (320 dp maximum for a rich tooltip).

## Behaviour

- Pointer: click activates the item; middle click sends the secondary action; secondary click opens the item's menu ([[Tray Menu]]); wheel sends scroll to the application.
- Keyboard: Tab to the item; Enter and Space activate; Menu key or Shift+F10 opens the menu (required by AR-9; not built).
- Touch: tap activates; long press shows the tooltip.

## Tooltip and overlay behaviour

One tooltip, on the item (the control): a rich tooltip without actions with title and text; the title is the accessible name and the text the description. 500 ms, 150 ms grace, keyboard focus immediate ([[Tooltip]]). The menu opens beside the item (a popup).

Finding (shared): the tooltip card is a literal copy in the `.tdl` of Audio, Battery, Clock, Media, Network and Tray Item (six modules; the Volume OSD comment shows a seventh pattern): `Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`, padding `[12, 8, 12, 8]`, `Font_Size: 14`, `Foreground: $color.on_surface`, `Alignment: CENTER`, `Gap: 4`. [[Tooltip]] specifies the plain card as `inverse_surface` with `inverse_on_surface`, shape `extra_small` (4 dp), elevation level 0, padding 8 dp by 4 dp, `body_small` 12/16, maximum width 200 dp. The card belongs in one shared tooltip style, not in six modules (candidate request to tess-shell).

## Motion

No animation. Reduced motion: none to remove.

## Accessibility

- Role: `BUTTON`; name = the item's title with `needs attention` when it applies; description = the tooltip text.
- Keys: as Behaviour.
- Announcements: none.
- Target at least 24 dp square (code: 18, fails).
- Contrast: the icon is an application image and is not under the shell's control; the attention border is at least 3:1.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `size` | 18 dp in code, 24 dp in spec |
| Passive items | hidden |

## Acceptance criteria

- [ ] AC-MOD-TRI-1 (AT tree assertion): the item has role `BUTTON`, a non-empty name equal to the item title (plus `needs attention` when it applies) and a description equal to the tooltip text.
- [ ] AC-MOD-TRI-2 (geometry check): the hit area is 32, 24 and 24 dp square and the icon 20, 18 and 18 dp at default, compact and dense ([[ADR-0024 Shell tray and task item sizes]]); never below 24 dp.
- [ ] AC-MOD-TRI-3 (scripted input): click, middle click, secondary click and wheel each send the matching action once.
- [ ] AC-MOD-TRI-4 (scripted input): Enter and Space activate; the Menu key opens the item's menu and focus enters the menu.
- [ ] AC-MOD-TRI-5 (scripted input): hover for 500 ms: exactly 1 tooltip layer with the title and the text; leave removes it within 150 ms plus one frame.
- [ ] AC-MOD-TRI-6 (static check): only the item root carries a `Tooltip`; the icon child carries none.
- [ ] AC-MOD-TRI-7 (pixel check): the attention look differs from rest in a greyscale render.
- [ ] AC-MOD-TRI-8 (pixel check): the tooltip card equals the rich [[Tooltip]] card; the module `.tdl` holds no card literal.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Tray_Item/Tray_Item_Module.tdl`, `Tray_Item_Style.tdl` | partly meets: role, name, description, one tooltip on the root, attention look (meets AC-MOD-TRI-1, -3 by reading, -5, -6); hit area is 24 by 24 dp, the icon is 18 (meets the 24 dp floor, fails the 40, 32, 28 dp sizes of AC-MOD-TRI-2); Menu key absent (fails AC-MOD-TRI-4); tooltip literal (fails AC-MOD-TRI-8); attention is colour plus border only (AC-MOD-TRI-7 unverified) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Tray_Item/Tray_Item_Style.tdl` (dimensions) | differs: padding 3 (spec 8, 6, 4), corner 6 (spec 20, 16, 14), icon 18 (spec 24, 20, 20), gap 6 (spec 4); fails AC-MOD-TRI-2; letter spacing (tracking) has no hook in tess-shell |
| shell-vault | `shell-vault:40 Specifications/Modules/Tray Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Hit area 32, 24, 24 dp and icon 20, 18, 18 dp instead of the icon button's 40, 32, 28 and 24, 20, 20 | the shell keeps today's compact sizes (owner principle: compact keeps today's sizes); 24 dp is the pointer minimum (WCAG 2.2 SC 2.5.8) | [[ADR-0024 Shell tray and task item sizes]] |
| Rich tooltip without actions | title and text, no interactive parts | [[ADR-0004 Tooltip rule]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
