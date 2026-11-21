---
title: Tasks Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, tasks]
related: ["[[Task Item]]", "[[Bar]]", "[[Iconography#Fallback icon|Empty and Error States]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "Pointer Events", "[[Keyboard Navigation]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Tasks Module

> [!info] Summary
> The Tasks Module shows the open windows as a row of [[Task Item]] buttons, one per window. The nearest Material Design 3 counterpart is the [navigation bar](https://m3.material.io/components/navigation-bar/overview), adapted to a Bar. Source of truth in code: see the last section.

## Purpose

Shows which windows are open, which is active, and lets the user activate, minimise or close them from the Bar. The list comes from the shell's KWin script.

## When to use and not

- Use when: the Bar needs a window list on KWin.
- Do not use when: the user needs window thumbnails, grouping by application or pinned launchers (not in v1).

## Anatomy

1. Root: horizontal box, role `GROUP`, name `Tesserae Shell windows`.
2. [[Task Item]] per window, keyed by window id.
3. Scroll handler on the Root: the wheel activates the next or previous window.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Icon and title | Default | `show_title` true |
| Icons only | Narrow bars | `show_title` false; each item needs a tooltip |
| This monitor, current desktop | Default | `monitor: THIS`, `desktop: CURRENT` |
| All monitors or desktops | Shared bars | `monitor: ALL`, `desktop: ALL` |

## States

| State | Visual change | Token values |
|---|---|---|
| Windows present | One item per window | [[Task Item]] |
| Empty (no window) | The module is hidden and takes no space; with `show_empty` it keeps its space (an empty box, no text) | [[Iconography#Fallback icon|Empty and Error States]] |
| Hover, focus, pressed, selected | Per item | [[Task Item]] |
| Hidden (service absent) | No KWin, no script, no first list yet, or no window: hidden. Hidden means `Visible: false` on the root: the module takes no space in the [[Bar]], no spacing is left beside it, no placeholder is drawn and the root is absent from the accessibility tree. | root `Visible: <| available and ready and (has_windows or params.show_empty) |>` |
| Error | A failed script load logs one warning and the module stays hidden | not applicable |

## Tokens used

No tokens of its own; the row is transparent and the items carry the tokens ([[Task Item]]). Gap `space.2` (4 dp).

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Item height | 40 | 32 | 28 | [[Task Item]] |
| Gap between items | 4 | 4 | 4 | `space.2` |
| Item maximum width | 180 | 180 | 180 | `max_width` |
| Icon size | see [[Task Item]] |  |  | `icon_size` param, code 18 |

## Layout and overflow

A horizontal row, no wrapping. When the windows do not fit the Bar slot the items shrink to their minimum (icon only) and then the row overflows; spec: the Tasks row clips at the slot edge and the active item is kept in view; no scrollbar (the Bar has no scroll). Vertical centring of the row. Code: the row is not clipped or scrolled (candidate request).

## Behaviour

- Pointer: click, middle click and wheel as [[Task Item]]; wheel over the row activates the next or the previous window.
- Keyboard: Tab visits each item; Left and Right move focus along the row; keys per [[Task Item]]. The wheel action is reachable by the Enter key on the next item (AR-9).
- Touch: as [[Task Item]].
- Updates: the list follows KWin's script messages; at most one update per frame per item for a title that changes quickly.

## Tooltip and overlay behaviour

The row (a group) has no tooltip. Each [[Task Item]] owns its tooltip (title and application). One tooltip at a time; 500 ms, 150 ms grace, dismissal list of [[Tooltip]]; scroll of the row (wheel) removes the tooltip of an item. The module opens no popup.

## Motion

Items appear and disappear by the keyed diff in one frame; spec allows a 100 ms fade-in of a new item ([[Motion]] `short2`) #needs-verification-as-design-choice, none is built. Reduced motion: no fade.

## Accessibility

- Roles: `GROUP` named `Tesserae Shell windows` (the vault note says `list`; a group is accepted because the items are buttons, not list items); items `BUTTON` ([[Task Item]]).
- Keys: as Behaviour.
- Announcements: with `announce` true the module says, politely, a window that opens, closes or wants attention; default false (the specification names none; AR-24). The `label` of each item is the stable name; title churn is not announced.
- Target 24 dp minimum.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `show_title` | true |
| `max_width` | 180 |
| `icon_size` | 18 |
| `monitor` | THIS |
| `desktop` | CURRENT |
| `show_empty` | false |
| `announce` | false |

## Acceptance criteria

- [ ] AC-MOD-TSK-1 (AT tree assertion): the row has role `GROUP` with a non-empty name; each child has role `BUTTON` and a name with the window title and application.
- [ ] AC-MOD-TSK-2 (scripted input): no KWin, or no windows: root `Visible` false, width 0, absent from the accessibility tree, Bar spacing unchanged; with `show_empty` the root keeps its space.
- [ ] AC-MOD-TSK-3 (scripted input): opening a window adds one item in the keyed diff and does not rebuild the others; closing removes one.
- [ ] AC-MOD-TSK-4 (scripted input): wheel +1 over the row activates the next window and -1 the previous, wrapping at the ends.
- [ ] AC-MOD-TSK-5 (scripted input): hover an item for 500 ms: one tooltip; wheel over the row with the tooltip shown removes it within one frame.
- [ ] AC-MOD-TSK-6 (static check): the Root carries no `Tooltip`.
- [ ] AC-MOD-TSK-7 (geometry check): items are 40, 32, 28 dp high at default, compact, dense; gaps 4 dp; no two hit areas overlap.
- [ ] AC-MOD-TSK-8 (scripted input): with `announce` true a window opening queues exactly one polite announcement; with it false none.
- [ ] AC-MOD-TSK-9 (scripted input): with more windows than fit, the active item is inside the slot and no item paints past the slot edge.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Tasks/Tasks_Module.tdl`, `Tasks_Module.py` | partly meets: hides without KWin or windows, keyed diff, wheel cycling, optional polite announcement (meets AC-MOD-TSK-1, -2, -3, -4, -8); row overflow rule absent (fails AC-MOD-TSK-9); items fail the size and tooltip criteria of [[Task Item]] |
| shell-vault | `shell-vault:40 Specifications/Modules/Tasks Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Row of buttons, not an MD3 navigation bar | a Bar window list differs from a bottom navigation of 3 to 5 destinations | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
