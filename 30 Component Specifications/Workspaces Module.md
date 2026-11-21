---
title: Workspaces Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, navigation]
related: ["[[Bar]]", "[[Button]]", "[[Text]]", "[[Selection]]", "[[Focus Ring]]", "[[State Layers]]", "[[Iconography#Fallback icon|Empty and Error States]]", "[[Keyboard Navigation]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Workspaces Module

> [!info] Summary
> The Workspaces Module shows KWin's virtual desktops as a row of buttons, the current one marked, a click switching to it. The nearest Material Design 3 counterparts are the [navigation rail](https://m3.material.io/components/navigation-rail/overview) and [navigation bar](https://m3.material.io/components/navigation-bar/overview) destinations, adapted to a Bar. Source of truth in code: see the last section.

## Purpose

Shows which desktop is current and switches to another in one click or one key press.

## When to use and not

- Use when: the Bar needs a desktop switcher on KWin.
- Do not use when: the user needs a desktop overview with window thumbnails or desktop management (not in v1).
- Not a tab list: the buttons switch the desktop, they do not control a panel in this window (navigation components).

## Anatomy

1. Root: horizontal box, role `GROUP`, name `Workspaces`.
2. Desktop button: one per desktop, role `BUTTON`, class `workspace`, corner 6, padding 10 by 4 (code).
3. Face: [[Text]] `label_large`: the desktop's name (its number when it has none) or the number (`label` param).
4. Current mark: the `:selected` look, a `surface_raised` fill and a 2 px `primary` border (shape and colour), plus the accessible state `selected`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| By name | Default (`label: name`) | each button shows the desktop's name or its number |
| By number | Narrow bars (`label: number`) | buttons show 1, 2, 3; the tooltip supplies the name |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Face in `on_surface`, no fill | [[Text]] |
| Hover | Fill `surface_raised` (code); spec: state layer 8 percent in `on_surface` ([[State Layers]]) | raised on surface is 1.12:1 dark, 1.08:1 light: a weak cue; the state layer is the spec |
| Focus (keyboard) | Focus ring 3 dp, 2 dp offset ([[Focus Ring]]); code: none built | [[Focus Ring]] |
| Pressed | State layer 10 percent | [[State Layers]] |
| Current (selected) | `surface_raised` fill and 2 px `primary` border; accessible `selected` | `primary` on surface: 5.76:1 dark, 5.29:1 light |
| Disabled | Not applicable: a desktop button is never disabled | not applicable |
| Hidden (service absent) | KWin is not on the session bus, or the first list has not arrived: hidden. Hidden means `Visible: false` on the root: the module takes no space in the [[Bar]], no spacing is left beside it, no placeholder is drawn and the root is absent from the accessibility tree. | root `Visible: <| available and ready |>` |

## Tokens used

Roles: `on_surface`, `primary` (current border), `surface_raised` (fill; nearest MD3 `surface_container`); `label_large`; shape `medium` 8 dp (code: 6). The MD3 navigation indicator uses `secondary_container` in a full-shaped pill ([[Colour Roles]], [[Shape]]); Tesserae keeps the border form because it works without a colour role.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Button height | 40 | 32 | 28 | [[Button]] heights; code: 24 text plus 8 padding |
| Minimum width | 40 | 32 | 28 | code: 28 literal; at least 24 dp |
| Maximum width | 160 | 160 | 160 | ellipsis beyond (code: `Max_Width: 160`) |
| Horizontal padding | 12 | 8 | 4 | `density.row_padding_x`; code: 10 |
| Gap between buttons | 4 | 4 | 4 | `space.2`; hit areas must not overlap |

## Layout and overflow

A button is one line with an ellipsis beyond 160 dp; the full text is the tooltip. Vertical centring of the Face. The row is as wide as its buttons; the Bar decides scrolling or hiding when it runs out of room (the Bar does not scroll modules). With 20 desktops the row is 20 buttons wide: spec: the module does not wrap.

## Behaviour

- Pointer: click a button sets KWin's current desktop; hover shows the tooltip.
- Keyboard: Tab visits each button in order; Enter and Space activate like a click; Left and Right move focus along the row.
- Touch: tap switches; long press shows the tooltip.
- The mark moves within one loop turn of KWin's signal, also when the desktop was switched elsewhere.

## Tooltip and overlay behaviour

Each button has one tooltip: its accessible name (`Desktop 2, Code`) so a number-only face is explained; shown 500 ms after hover and at once on keyboard focus; the Root group has none (ADR-0004). No tooltip is needed when the visible text equals the name and fits; spec still shows one on number-only faces. Today no tooltip exists on any button (fails AC-MOD-WSP-4). 150 ms grace and the dismissal list of [[Tooltip]] apply. The tooltip card is the plain card of [[Tooltip]], not a literal.

## Motion

The mark moves in one frame; no module animation. Reduced motion: none to remove.

## Accessibility

- Roles: row `GROUP` named `Workspaces`; each button `BUTTON` named `Desktop 2, Code`, state `selected` for the current one.
- Keys: as Behaviour.
- Announcements: none; a desktop change is the desktop switcher's to announce.
- The current desktop is conveyed by fill, border and the state, not by colour alone.
- Target 24 dp minimum at every density.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `label` | `name` |
| Corner | 6 dp in code, 8 dp (`medium`) in spec |
| Min and max width | 28 and 160 dp in code |

## Acceptance criteria

- [ ] AC-MOD-WSP-1 (AT tree assertion): the row has role `GROUP` named `Workspaces`; each desktop button has role `BUTTON`, name `Desktop <n>, <name>`; exactly one has state `selected`.
- [ ] AC-MOD-WSP-2 (scripted input): KWin absent: root `Visible` false, width 0, absent from the accessibility tree, Bar spacing unchanged.
- [ ] AC-MOD-WSP-3 (scripted input): click button 3: KWin's current desktop becomes 3 and the mark moves within one loop turn; changing the desktop from outside moves the mark too.
- [ ] AC-MOD-WSP-4 (scripted input): hover a button for 500 ms: exactly one tooltip layer with the accessible name; hover the gap between buttons: 0 layers.
- [ ] AC-MOD-WSP-5 (scripted input): Tab visits each button once in visual order and leaves; Enter and Space each switch once.
- [ ] AC-MOD-WSP-6 (geometry check): button height is 40, 32 and 28 dp and the minimum width at least 24 dp at default, compact and dense; adjacent hit areas do not overlap.
- [ ] AC-MOD-WSP-7 (pixel check): the current button differs from others in fill and border in a greyscale render.
- [ ] AC-MOD-WSP-8 (pixel check): a desktop name longer than the maximum width ends with an ellipsis inside the button.
- [ ] AC-MOD-WSP-9 (contrast script): Face text against the Bar surface at least 4.5:1 and the 2 px border at least 3:1 in Light, Dark and High_Contrast.
- [ ] AC-MOD-WSP-10 (static check): no node with role `GROUP` carries a tooltip.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Workspaces/Workspaces_Module.tdl`, `Workspaces_Style.tdl`, `Workspaces_Module.py` | partly meets: hides without KWin, names, `selected` state, border plus fill (meets AC-MOD-WSP-1, -2, -3, -7); no tooltips (fails AC-MOD-WSP-4); height is text plus padding, not a density value, padding 10 literal (fails AC-MOD-WSP-6 at default and compact); keyboard focus ring not built (AC-MOD-WSP-5 unverified) |
| shell-vault | `shell-vault:40 Specifications/Modules/Workspaces Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Current desktop shown by fill and a 2 px border, not an MD3 `secondary_container` pill | works for a Bar button of 28 to 40 dp height; shape cue without a role | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights and padding by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
- Material Web navigation bar and rail tokens (active indicator `secondary_container`, shape full, 64 by 32 px bar and 56 by 32 px rail): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-bar.scss and `_md-comp-navigation-rail.scss`. Verified 2026-11-21.
