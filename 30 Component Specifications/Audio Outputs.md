---
title: Audio Outputs
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, menu, audio]
related: ["[[Audio Module]]", "[[Menu]]", "[[Menu Item]]", "[[Popup]]", "[[12 Overlays]]", "[[Scrollbar and Scroll Container]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Audio Outputs

> [!info] Summary
> Audio Outputs is the content of the popup the [[Audio Module]] opens on a secondary click: a [[Menu]] with one row per sound output, the current one marked, a click making that output the default. No direct Material Design 3 counterpart; it is a [menu](https://m3.material.io/components/menus/overview) with a single-choice selection. Source of truth in code: see the last section.

## Purpose

Choose the default sound output in one click and see which one is active.

## When to use and not

- Use when: the Audio module offers an output choice.
- Do not use when: the list needs volumes per device, input devices or application routing (not in v1).

## Anatomy

1. Popup: `Audio_Outputs`, attached below the Audio module (`Attach: BOTTOM`, `Gap: 4`, container `surface_raised`, corner 8).
2. [[Menu]] labelled `Outputs`.
3. [[Menu Item]] per output: icon of its kind, name, a bullet in the shortcut slot on the current output.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Single level | Only form | no submenus |

## States

| State | Visual change | Token values |
|---|---|---|
| Row rest | Name in `on_surface`, kind icon | [[Menu Item]] |
| Row hover, pressed, focus | As [[Menu Item]] | as [[Menu Item]] |
| Current output | A bullet `•` in the end slot and the accessible name ends `, current` (shape and word, not colour) | `on_surface_variant` text |
| Empty | No outputs known at the click: the list is empty; spec: the popup does not open and the module logs one warning (an empty menu is a dead end) | not applicable |
| Open, closed | Popup opens at the click with the outputs known at that moment (`caller.data.outputs`), closes after a pick, Escape or an outside press | [[Popup]] |

## Tokens used

All parts use [[Menu]] and [[Menu Item]] tokens: container `surface_container` (code: `surface_raised`), shape `extra_small` (MD3 menu uses `extra_small`; the shell uses corner 8, a deviation recorded in [[Menu]]), `label_large`/`body_medium` text.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Row height | 40 | 32 | 28 | [[Menu]] single-line item |
| Icon | 24 | 20 | 20 | [[Menu]] |
| Row horizontal padding | 12 | 8 | 4 | [[Menu]] |
| Popup width | 112 minimum, 280 maximum | same | same | [[Menu]] #needs-verification |

## Layout and overflow

Rows are single line. A long device name ends with an ellipsis and the row keeps its height; the full name is in the accessible name. A list taller than 60 percent of the output height scrolls ([[Scrollbar and Scroll Container]]). Vertical centring in the row.

## Behaviour

- Pointer: click a row to make that output the default and close the popup; hover lights a row.
- Keyboard: Up and Down move the lit row, Home and End jump, Enter and Space pick, Escape closes and returns focus to the Audio mute button ([[Menu]]).
- Touch: tap a row.

## Tooltip and overlay behaviour

No tooltip: every row has visible text, and a row is not a tooltip trigger (ADR-0004). The popup is a popup window with a focus grab ([[Popup]], [[12 Overlays]]). The popup opens in response to input on a Bar surface and is dismissed by an outside press or Escape.

## Motion

Popup open and close follow [[Popup]] (no animation required). Reduced motion: none to remove.

## Accessibility

- Roles: `MENU` named `Outputs`, rows `MENUITEM` named by the output name, `, current` appended for the default.
- Keys: as [[Menu]].
- Announcements: none beyond the screen reader's own menu reading.
- Contrast: row text 4.5:1 on the popup container in all schemes.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| Popup attach | BOTTOM, gap 4 |
| Item set | outputs at the time of the click |

## Acceptance criteria

- [ ] AC-MOD-AOU-1 (AT tree assertion): the popup root has role `MENU` with name `Outputs`; each row has role `MENUITEM`; the default output's name ends with `, current`.
- [ ] AC-MOD-AOU-2 (scripted input): click a non-current row: the default output changes once and the popup closes within one frame.
- [ ] AC-MOD-AOU-3 (scripted input): Down, Down, Enter on a three-row menu picks the third row; Escape closes with focus on the Audio mute button.
- [ ] AC-MOD-AOU-4 (scripted input): with an empty output list the popup does not open and one warning is logged.
- [ ] AC-MOD-AOU-5 (pixel check): the current row differs from the others by the bullet in a greyscale render.
- [ ] AC-MOD-AOU-6 (geometry check): row heights are 40, 32 and 28 dp and icons 24, 20 and 20 dp at default, compact and dense.
- [ ] AC-MOD-AOU-7 (static check): no node of the module carries a `Tooltip`.
- [ ] AC-MOD-AOU-8 (contrast script): row text against the popup container is at least 4.5:1 in Light, Dark and High_Contrast.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Audio_Outputs/Audio_Outputs_Module.tdl`, `Audio_Outputs_Module.py` | partly meets: menu roles and the current marker with the word `, current` (meets AC-MOD-AOU-1, -5); rows use [[Menu Item]] literals (28 high, 16 dp icon: fails AC-MOD-AOU-6 at default and compact); the empty case is not handled (AC-MOD-AOU-4 absent) |
| shell-vault | `shell-vault:40 Specifications/Modules/Audio Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Single-choice marker is a bullet in the end slot, not a leading check | the shell Menu Item has no check slot; shape plus the word in the name | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row heights by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
- WAI-ARIA Authoring Practices, menu and menubar: https://www.w3.org/WAI/ARIA/apg/patterns/menubar/ (menu keys).
