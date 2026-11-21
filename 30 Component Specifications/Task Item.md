---
title: Task Item
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, tasks]
related: ["[[Tasks Module]]", "[[Marquee Text]]", "[[Icon]]", "[[Icon Button]]", "[[Button]]", "[[Selection]]", "[[Disabled State]]", "[[Focus Ring]]", "[[State Layers]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Task Item

> [!info] Summary
> A Task Item is one button of the [[Tasks Module]] row: the application's icon and, optionally, the window's title in a [[Marquee Text]]. The nearest Material Design 3 counterpart is a navigation bar item without a label. Source of truth in code: see the last section.

## Purpose

Represents one open window, shows whether it is active, minimised or wants attention, and is the target of activate, minimise and close.

## When to use and not

- Use when: the [[Tasks Module]] lists a window (it calls the item in a repeater).
- Do not use when: a plain launcher button is needed (use [[Icon Button]]) or a tray icon (use [[Tray Item]]).

## Anatomy

1. Root: box, class `task_item`, role `BUTTON`, name from `label`.
2. Icon: the application's icon (`Icon` module; an SVG document or pixels), 18 dp default.
3. Title (optional, `show_title`): [[Marquee Text]], width `max_width - icon_size - 18`.
4. Attention mark: a 6 by 6 dp dot in `warning`, hidden from assistive technology, shown while the window wants attention.
5. Tooltip: window title and application name.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Icon and title | Default | `show_title` true; width `max_width` (180 dp) |
| Icon only | Narrow bars | `show_title` false; the tooltip is the only visible name |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Icon and title in `on_surface` | [[Icon]] |
| Hover | Fill `surface_raised` (code); spec: state layer 8 percent | [[State Layers]] |
| Focus (keyboard) | Focus ring 3 dp, 2 dp offset | [[Focus Ring]] |
| Pressed | State layer 10 percent | [[State Layers]] |
| Active window | `:selected`: `surface_raised` fill and 2 px `primary` border; state `selected` | primary on surface 5.76:1 dark, 5.29:1 light |
| Minimised | Opacity 0.5 (code). The same look as disabled: spec requires a second cue that is not the disabled look (for example a 2 dp underline bar); the name says `minimised` | [[Disabled State]] |
| Wants attention | 6 dp `warning` dot beside the title (shape appears, not only colour) | `warning` 10.02:1 dark, 5.51:1 light |
| Disabled | Not applicable: an item is never disabled | not applicable |

## Tokens used

Roles: `on_surface`, `primary`, `warning`, `surface_raised`; shape: corner 6 (code), spec `small` 4 dp or `medium` 8 dp from [[Shape]]; label `label_large`.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Height | 40 | 32 | 28 | [[Button]] heights; code: 18 icon plus 6 padding = 24 |
| Icon with title | 18 | 18 | 16 | `Icon next to a button label` in [[Iconography]]; code 18 |
| Icon only | 24 | 20 | 20 | icon button icon in [[Iconography]] |
| Horizontal padding | 12 | 8 | 4 | `density.row_padding_x`; code: 6 |
| Gap icon to title | 8 | 8 | 4 | `density.icon_label_gap`; code: 6 |
| Width with title | 180 maximum | 180 | 180 | `max_width` param |

## Layout and overflow

One line. The title is a Marquee: it scrolls when wider than its box and, with reduced motion or when disabled, ends in an ellipsis ([[Marquee Text]]). Vertical centring of icon and title. Icon-only items are square at the density height.

## Behaviour

- Pointer: click on a window that is not active activates it (un-minimising); click on the active window minimises it; middle click closes it; wheel over the row (the Tasks root) cycles windows.
- Keyboard: Enter and Space do what a click does; Delete closes the window (the key equivalent of the middle click, required by AR-9; not built).
- Touch: tap activates or minimises; long press shows the tooltip.

## Tooltip and overlay behaviour

One tooltip, on the item (the control), with the window title and the application name; it is the name of an icon-only item. The Marquee inside the item does not open its own tooltip (nested tooltips are forbidden by AC-TIP-1 and were the F8 failure): spec requires a Marquee option that turns its automatic whole-text tooltip off inside a control (candidate request to tess-shell). Today the item has no tooltip of its own and the Marquee carries the title tooltip; an icon-only item has none at all (fails AR-3). 500 ms, 150 ms grace, keyboard focus immediate ([[Tooltip]]).

## Motion

The Marquee scrolls the title; the opacity of a minimised item changes in one frame. Reduced motion: the Marquee stops and ellipsises ([[Reduced Motion]]).

## Accessibility

- Role: `BUTTON`; name `Document - Editor, Kate, active` style (`label` from the Tasks module: the title and the application, with `active`, `minimised` or `wants attention` said in words); state `selected` while active.
- Keys: as Behaviour.
- Announcements: none from the item; the Tasks module can announce open, close and attention ([[Tasks Module]]).
- The attention dot is `A11y_Hidden`; the state is in the name.
- Target at least 24 dp at every density.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `show_title` | true |
| `max_width` | 180 |
| `icon_size` | 18 |
| Corner | 6 dp in code |

## Acceptance criteria

- [ ] AC-MOD-TIT-1 (AT tree assertion): the item has role `BUTTON` and a name that contains the window title and the application name, and the word `active`, `minimised` or `wants attention` when it applies; `selected` is set only while the window is active.
- [ ] AC-MOD-TIT-2 (scripted input): click an inactive item: the window activates once; click the active item: it minimises once; middle click: the window closes once.
- [ ] AC-MOD-TIT-3 (scripted input): Enter and Space on a focused item act as a click; Delete closes the window.
- [ ] AC-MOD-TIT-4 (scripted pointer): hover an icon-only item for 500 ms: exactly 1 tooltip layer with the title and application; hover an item whose title is cut: exactly 1 layer, never 2.
- [ ] AC-MOD-TIT-5 (static check): no node under the item other than the item itself carries a `Tooltip`.
- [ ] AC-MOD-TIT-6 (geometry check): item height is 40, 32 and 28 dp, with-title icon 18, 18 and 16 dp, icon-only icon 24, 20 and 20 dp at default, compact and dense; hit area at least 24 dp.
- [ ] AC-MOD-TIT-7 (pixel check): active, minimised and attention each differ from rest in a greyscale render (fill and border; underline or equivalent; dot shape).
- [ ] AC-MOD-TIT-8 (contrast script): title text against the Bar surface and the 2 px border at least 4.5:1 and 3:1 respectively in Light, Dark and High_Contrast.

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Task_Item/Task_Item_Module.tdl`, `Task_Item_Style.tdl` | partly meets: role, name with state words, active border plus fill, attention dot (meets AC-MOD-TIT-1, -2, -7 partly); no tooltip on the item and a Marquee tooltip inside (fails AC-MOD-TIT-4, -5); minimised is opacity 0.5 only, the disabled look (fails AC-MOD-TIT-7); sizes are 24 high, padding 6, gap 6 literals (fails AC-MOD-TIT-6); Delete key absent (fails AC-MOD-TIT-3) |
| shell-vault | `shell-vault:40 Specifications/Modules/Tasks Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Active window marked by fill and 2 px border, not a `secondary_container` pill | legible at 28 dp height without a colour role | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights, paddings by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
