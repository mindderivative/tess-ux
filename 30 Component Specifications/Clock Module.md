---
title: Clock Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, status]
related: ["[[Bar]]", "[[Label]]", "[[Text]]", "[[Popup]]", "[[Theme Following the System]]", "[[14 Accessibility Basics#Reduced motion|Reduced Motion]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Clock Module

> [!info] Summary
> The Clock Module shows the current time as one line of text in a [[Bar]] and the date in a tooltip. It has no Material Design 3 counterpart (Tesserae-specific; nearest patterns: [[Label]] text with a plain [[Tooltip]]). Source of truth in code: see the last section.

## Purpose

Shows the time at a glance. Several uses can show different formats and time zones (`format`, `locale`, `hour_cycle`, `timezone`). The date is secondary information and lives in the tooltip; the time is never only in the tooltip.

## When to use and not

- Use when: the Bar needs the time of the local zone or of one fixed zone.
- Do not use when: the user needs a calendar, alarms or timers (not in v1; a [[Popup]] calendar flyout is a later module); the text is static (use [[Label]]).

## Anatomy

1. Face: one [[Text]] node (class `clock_text`) with the formatted time.
2. Hover box: the box around the Face. A box takes the pointer, a Text does not, so the tooltip sits on this box (`tess-shell:src/tess_shell/shipped/Clock/Clock_Module.tdl` comment).
3. Tooltip: plain, one line, the date from `tooltip_format` (default `%A, %d %B %Y`).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Time only | Default | `format` empty: the pattern follows `hour_cycle` (`desktop`, `12`, `24`) |
| Custom format | Seconds, date in the bar | `format` is a strftime pattern; the ticker runs once a second when the pattern has seconds, else once a minute |
| Zone clock | A second clock for another place | `timezone` is an IANA name; the use shows that zone |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Time in `on_surface`; weight 500 | `label_large` 14/20/500 (code: Font_Size 14, Font_Weight 500; the style file sets Foreground `#ffffff`, see Status in code) |
| Hover | No visual change on the face; tooltip after 500 ms | [[Tooltip]] |
| Focus | Not applicable: the Clock is not focusable (no action) | not applicable |
| Pressed, selected | Not applicable: no action | not applicable |
| Disabled | Opacity 0.5 through `Label:disabled` is not defined for the Clock; the Clock is never disabled | not applicable |
| Hidden | Never hidden: no service | not applicable |
| Empty or error | A bad `timezone` or `locale` is warned about once and ignored; the local zone and the process locale show | not applicable (log only) |

## Tokens used

Role `on_surface` for the face; `label_large` ([[Typography]]); no shape, no elevation; the tooltip card is the [[Tooltip]] plain variant. Spacing steps from [[Spacing and Density]]. See Dark and light.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Face line box height | 20 | 20 | 20 | `label_large` line height; type does not scale with density |
| Hover box minimum height | 24 | 24 | 24 | `target.min` so the pointer finds the box |
| Horizontal padding of the box | 0 | 0 | 0 | the Bar sets the gap between modules (`space.3`, 8 dp) |
| Tooltip gap to the box | 4 | 4 | 4 | [[Tooltip]] |

The Clock does not scale with density except through the [[Bar]] height; it has no pointer action, so the 24 dp hit area rule applies only to the tooltip hover box.

## Layout and overflow

The Face is one line and never wraps (`Wrap` is not set; the text is short). Vertical centring: the line box is centred in the Bar row ([[10 Layout Overflow and Scrolling]]). A format that produces a text wider than the Bar slot clips; the module does not ellipsise. The width follows the text: a 24-hour time at `label_large` is about 5 characters; the module does not reserve width for a changing digit (a proportional font may move neighbours by 1 dp; a tabular-figure font is a later request).

## Behaviour

- Pointer: hover shows the date tooltip; click, secondary click and scroll do nothing in v1.
- Keyboard: not focusable; the time and date are read through the accessible name and description (see Accessibility).
- Touch: a long press shows the tooltip ([[Tooltip]]).
- Tick: once a second when the format has seconds, else at the start of each minute; the module sends the new string only when it changes.

## Tooltip and overlay behaviour

One tooltip, on the hover box around the Face (the control), text = the date. ADR-0004 and ADR-0011 apply: 500 ms show delay, 150 ms hover grace, dismissed by pointer leave, Escape, scroll, press, trigger removal, window focus loss; the tooltip is opaque and one at a time ([[Tooltip]]).

Finding (shared): the tooltip card is a literal copy in the `.tdl` of Audio, Battery, Clock, Media, Network and Tray Item (six modules; the Volume OSD comment shows a seventh pattern): `Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`, padding `[12, 8, 12, 8]`, `Font_Size: 14`, `Foreground: $color.on_surface`, `Alignment: CENTER`, `Gap: 4`. [[Tooltip]] specifies the plain card as `inverse_surface` with `inverse_on_surface`, shape `extra_small` (4 dp), elevation level 0, padding 8 dp by 4 dp, `body_small` 12/16, maximum width 200 dp. The card belongs in one shared tooltip style, not in six modules (candidate request to tess-shell).

The tooltip text is not the only place the information lives: the accessible description carries the same date text, so a screen reader user and a keyboard user are not dependent on hover. The Clock opens no popup.

## Motion

No animation. The time changes in one frame. Reduced motion has no effect ([[14 Accessibility Basics#Reduced motion|Reduced Motion]]).

## Accessibility

- Role: none (static text); the Face carries `Label` = the time text and `Description` = the date text (`Clock_Module.tdl`).
- Name: the formatted time, for example `14:05`; description: `Friday, 20 November 2026`.
- Keys: none (not focusable).
- Announcements: none; a ticking clock is never announced (WCAG 2.2 SC 4.1.3 does not call for it).
- Contrast: `on_surface` on the Bar surface at least 4.5:1 in light, dark and high contrast (measured: 14.87:1 dark, 15.31:1 light for `#E4EAF1` on `#12171D` and `#16202B` on `#F4F7FA`).

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three. The style file sets the Face foreground to the literal `#ffffff`; on the Light mode surface `#F4F7FA` that is 1.06:1, which fails AC-MOD-CLK-6.

## Defaults

| Setting | Default |
|---|---|
| `format` | empty (by `hour_cycle`) |
| `locale` | empty (the process locale) |
| `hour_cycle` | `desktop` |
| `timezone` | empty (local) |
| `tooltip_format` | `%A, %d %B %Y` |

## Acceptance criteria

- [ ] AC-MOD-CLK-1 (AT tree assertion): the Face has a non-empty `Label` equal to the visible time text and a `Description` equal to the tooltip text; the node has no role `group`.
- [ ] AC-MOD-CLK-2 (scripted input): pointer enters the hover box at t0: 0 tooltip layers at t0+499 ms, 1 layer at t0+517 ms; the layer text equals the `tooltip_format` date.
- [ ] AC-MOD-CLK-3 (scripted input): pointer leaves the box and the tooltip: 0 layers within 150 ms plus one frame after leaving both (ADR-0011); Escape removes it within one frame.
- [ ] AC-MOD-CLK-4 (static check): the Clock tree has exactly one node with a `Tooltip` and it has no tooltip-bearing descendant and no ancestor tooltip.
- [ ] AC-MOD-CLK-5 (pixel check): the tooltip card equals the plain [[Tooltip]] card: container `inverse_surface`, text `inverse_on_surface`, corner 4 dp, padding 8 by 4 dp, `body_small`; the Clock's own `.tdl` contains no card literal.
- [ ] AC-MOD-CLK-6 (contrast script): the Face foreground against the Bar surface is at least 4.5:1 in Light, Dark and High_Contrast; the style file holds no colour literal.
- [ ] AC-MOD-CLK-7 (geometry check): the hover box is at least 24 dp high and as wide as the text; the Face line box is centred in it within 1 px.
- [ ] AC-MOD-CLK-8 (token test): with `hour_cycle` 24, `format` empty and the fake time 14:05:09, the Face text is the 24-hour form without seconds and the ticker next fires at the next minute boundary; with `%H:%M:%S` it fires every second.
- [ ] AC-MOD-CLK-9 (scripted input): an invalid `timezone` leaves the local zone shown and logs exactly one warning.
- [ ] AC-MOD-CLK-10 (scripted input): with reduced motion on, nothing changes: the Face is identical (no animation exists).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Clock/Clock_Module.tdl`, `Clock_Style.tdl`, `Clock_Module.py` | partly meets: tooltip on the box with the date and description (meets AC-MOD-CLK-1, AC-MOD-CLK-4 by reading); tooltip card is a literal that differs from the plain card (fails AC-MOD-CLK-5); style file sets Foreground to `#ffffff` (fails AC-MOD-CLK-6 in Light mode); Face has no role and `Label` is set (meets AC-MOD-CLK-1) |
| shell-vault | `shell-vault:40 Specifications/Modules/Clock Module.md` | exists, status review; names the Label and a tooltip date |
| tess-ui | none | not applicable: no clock widget |
| tre | none | not applicable: no tooltip or timer primitive (see [[Tooltip]]) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Tooltip and Clock have no MD3 counterpart | Tesserae-specific status module; nearest pattern is the MD3 plain tooltip | [[ADR-0004 Tooltip rule]] |
| Hover grace for the plain tooltip | WCAG 2.2 SC 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Hover box minimum 24 dp | desktop target floor | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
- Material Web typography tokens (label large 14/20/500): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-typescale.scss (see [[Typography]]).
