---
title: Tray Menu
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, menu, tray]
related: ["[[Tray Module]]", "[[Tray Item]]", "[[Menu]]", "[[Menu Item]]", "[[Popup]]", "[[12 Overlays]]", "[[Scrollbar and Scroll Container]]", "[[ADR-0003 Scrollbar rule]]", "[[Divider|Menu Separator]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Tray Menu

> [!info] Summary
> Tray Menu is the content of the popups the [[Tray Module]] opens for an item: one level of the application's dbusmenu tree drawn as a [[Menu]] of [[Menu Item]]s, up to three levels. The Material Design 3 counterpart is the [menu](https://m3.material.io/components/menus/overview) with submenus. Source of truth in code: see the last section.

## Purpose

Shows an application's own menu in the shell's look and sends the click to the application.

## When to use and not

- Use when: a tray item has a menu.
- Do not use when: the menu belongs to the shell (use [[Menu]] directly).

## Anatomy

1. Popups `Tray_Menu`, `Tray_Menu_2`, `Tray_Menu_3`: `Attach: BOTTOM`, `Gap: 4` (the first), `Max_Height: 60%`, `surface_raised`, corner 8.
2. [[Menu]] labelled with the item's title.
3. [[Menu Item]] rows: label (mnemonic underscore removed), icon (theme icon, own picture, check or radio mark for toggle entries), key hint, arrow for a submenu, rule for a separator.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Level 1 | The root menu | `Level: 1`, rows of parent 0 |
| Level 2 and 3 | Submenu of the row that opened it | reads the row's `Id` through `caller.use.params` |

## States

| State | Visual change | Token values |
|---|---|---|
| Row rest, hover, pressed, focus, disabled | As [[Menu Item]] | [[Menu Item]] |
| Submenu open | The row shows `expanded`; the submenu opens to the right (to the left without room) after a 250 ms pointer rest or a click and closes after 300 ms on another row | [[Menu]] |
| Toggle entry | A check mark or radio mark in the icon slot (shape, not colour) | [[Menu Item]] |
| Empty tree | A menu with no entries does not open (spec; code opens an empty popup, unverified) | [[Iconography#Fallback icon|Empty and Error States]] |
| Error | A failed `Event` call logs one warning a minute per service; the menu still closes | not applicable |

## Tokens used

As [[Menu]] and [[Menu Item]]. Container `surface_container` (code `surface_raised`), shape from [[Shape]].

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Row height | 40 | 32 | 28 | [[Menu]]; code 28 |
| Icon | 24 | 20 | 20 | code 16 |
| Row horizontal padding | 12 | 8 | 4 | code 10 |
| Maximum height | 60% of the output | 60% | 60% | scrolls beyond ([[Scrollbar and Scroll Container]]) |
| Maximum depth | 3 levels | 3 | 3 | fixed |

## Layout and overflow

Rows are single line; a long label ends with an ellipsis and the full text is the accessible name. A menu taller than the popup's maximum height scrolls with the wheel and a scrollbar ([[ADR-0003 Scrollbar rule]]). Vertical centring in the row.

## Behaviour

- Pointer: hover lights a row; click a row sends `Event(id, "clicked")` to the application and closes the whole menu; a click on a row with a submenu only opens the submenu.
- Keyboard: Up and Down, Home and End, Enter and Space pick, Right opens a submenu, Left or Escape closes the innermost level, Escape on the root closes the menu with focus back on the tray item ([[Menu]]).
- Touch: tap a row.

## Tooltip and overlay behaviour

No tooltips on rows: every row has visible text and a row is never a tooltip trigger (ADR-0004). The popup is a focused-grab popup window ([[Popup]], [[12 Overlays]]); one submenu open at a time.

## Motion

Popups open and close as [[Popup]]; no animation required. Reduced motion: none to remove.

## Accessibility

- Roles: `MENU` named by the item's title; rows `MENUITEM` with `expanded` on rows that have a submenu, `SEPARATOR` for rules; checked and disabled states in the names or states.
- Keys: as Behaviour.
- Announcements: none beyond the screen reader's own menu reading.
- Contrast: row text 4.5:1 on the container; the pressed row uses `primary`, against which `on_surface` is 2.58:1 dark and 2.89:1 light (fails; see [[Menu Item]]).

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| Levels | 3 |
| Max height | 60% |
| Attach | BOTTOM, gap 4 for level 1 |

## Acceptance criteria

- [ ] AC-MOD-TRM-1 (AT tree assertion): the popup root has role `MENU` with a name equal to the item's title; every row has role `MENUITEM` or `SEPARATOR`; a row with a submenu has `expanded`.
- [ ] AC-MOD-TRM-2 (scripted input): click a row: exactly one `Event(id, clicked)` call is sent and the whole menu closes; a click on a row with a submenu sends none and opens level 2.
- [ ] AC-MOD-TRM-3 (scripted input): Right on a row with a submenu opens it and moves focus into it; Left closes it; Escape on level 1 closes the menu and focus returns to the tray item.
- [ ] AC-MOD-TRM-4 (scripted input): a pointer rest of 250 ms on a submenu row opens the submenu; 300 ms on another row closes it; never two submenus open at once.
- [ ] AC-MOD-TRM-5 (geometry check): rows are 40, 32, 28 dp and icons 24, 20, 20 dp at default, compact, dense; popup height at most 60 percent of the output height.
- [ ] AC-MOD-TRM-6 (scripted input): a menu of 100 entries scrolls with the wheel and a drag on the scrollbar thumb; the popup shows within 100 ms.
- [ ] AC-MOD-TRM-7 (static check): no node of the module carries a `Tooltip`.
- [ ] AC-MOD-TRM-8 (contrast script): row text against the container, and against the pressed-row fill, at least 4.5:1 in Light, Dark and High_Contrast.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Tray_Menu/Tray_Menu_Module.tdl`, `Tray_Menu_Module.py`, `tess-shell:src/tess_shell/schema/default_popups.py` | partly meets: three levels, 60 percent maximum height, click sends the event and closes, submenu timings of [[Menu Item]] (meets AC-MOD-TRM-1, -2, -4 by reading); row sizes are the [[Menu Item]] literals (fails AC-MOD-TRM-5); pressed-row contrast fails (AC-MOD-TRM-8); keyboard path in the Menu per M6, not verified (AC-MOD-TRM-3) |
| shell-vault | `shell-vault:40 Specifications/Modules/Tray Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Popup corner 8 dp and `surface_raised`, not `extra_small` and `surface_container` | shell theme tokens; recorded in [[Menu]] | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
- WAI-ARIA Authoring Practices, menu and menubar: https://www.w3.org/WAI/ARIA/apg/patterns/menubar/
