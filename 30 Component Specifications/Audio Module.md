---
title: Audio Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, audio]
related: ["[[Bar]]", "[[Icon Button]]", "[[Slider]]", "[[Menu]]", "[[Audio Outputs]]", "[[Volume OSD]]", "[[Popup]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "[[Iconography#Fallback icon|Empty and Error States]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Audio Module

> [!info] Summary
> The Audio Module controls the default sound output from a [[Bar]]: a mute button with the output kind and level as icon, volume steps by scroll, the list of outputs on a secondary click, an optional percentage and slider, and a mark while the microphone is muted. No Material Design 3 counterpart (Tesserae-specific; nearest patterns: [[Icon Button]], [[Slider]] and [[Menu]]). Source of truth in code: see the last section.

## Purpose

Mute, unmute and change the volume of the default output without opening a settings application, and see which output and level are active.

## When to use and not

- Use when: the Bar controls the machine's sound.
- Do not use when: the user needs per-application volumes or device settings (not in v1).
- The one-off volume feedback after a keyboard key is the [[Volume OSD]], not this module.

## Anatomy

1. Root: a horizontal box that takes scroll (volume step) and secondary click (outputs). It is a container; it carries no tooltip (see Tooltip and overlay behaviour).
2. Mute button: an icon button, role `BUTTON`, name `Mute` or `Unmute`. Two glyph nodes exist from the start, one shown at a time: normal glyph, muted glyph in `on_surface_muted` (the glyph also changes shape).
3. Percentage: optional [[Text]] `label_large`.
4. Volume slider: optional [[Slider]], label `Volume`, value text `40 percent`.
5. Microphone mark: `mdi:microphone-off`, shown while the default microphone is muted, label `Microphone muted`.
6. Outputs menu: the [[Audio Outputs]] popup, opened by the secondary click.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Icon only | Default | `show_percent` false, `show_slider` false |
| With percent | Wide bars | `show_percent` true |
| With slider | Pointer users | `show_slider` true; the slider drag sends the volume at most 20 times a second, the release sends the final value |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | Glyph for the output kind and level in `on_surface` | [[Iconography#Icon set|Icons]] |
| Muted | Glyph shape changes and colour is `on_surface_muted`; the button name becomes `Unmute` | `on_surface_muted` 7.96:1 dark, 6.70:1 light on the surface |
| Hover, focus, pressed (mute button) | State layer 8, 10, 10 percent in `on_surface` over the button; focus ring 3 dp, 2 dp offset ([[State Layers]], [[Focus Ring]]) | as [[Icon Button]] |
| Disabled | Not applicable: the module is never disabled; with no sound server it is hidden | not applicable |
| Hidden (service absent) | No sound server: `ready` false, the module is hidden. Hidden means `Visible: false` on the root: the module takes no space in the [[Bar]], no spacing is left beside it, no placeholder is drawn and the root is absent from the accessibility tree. | root `Visible: <| ready |>` |
| Microphone muted | A second glyph appears (`show_mic`, default true) | `on_surface_muted` |

## Tokens used

Roles: `on_surface`, `on_surface_muted`; type `label_large`; the mute button follows [[Icon Button]] tokens; the slider follows [[Slider]].

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Mute button container | 40 by 40 | 32 by 32 | 28 by 28 | [[Icon Button]] container; code: 32 by 32 at all densities |
| Mute button icon | 24 | 20 | 20 | `density.icon_button_icon`; code: 16 |
| Gap between parts | 4 | 4 | 4 | `space.2` |
| Microphone mark | 16 | 16 | 16 | inline status icon ([[Iconography]]) |
| Slider | see [[Slider]] | see [[Slider]] | see [[Slider]] | code: 160 by 20 |

## Layout and overflow

One row. Vertical centring of every part in the Bar row ([[10 Layout Overflow and Scrolling]]). The percentage text is at most 4 characters (`100 %`). The module never wraps; when the Bar slot is too narrow the optional parts (slider, percentage) are omitted by params, not truncated.

## Behaviour

- Pointer: click the mute button toggles mute; scroll over the root steps the volume by `step` percent (5 by default; up for scroll up); secondary click opens [[Audio Outputs]]; drag on the slider sets the volume.
- Keyboard: Tab to the mute button; Enter and Space toggle mute. Up and Down on the focused mute button change the volume by `step`; Menu key or Shift+F10 opens the outputs menu. These two key paths are required by AR-9 (every pointer action reachable by keyboard) and are not built (see Status in code).
- Touch: tap toggles mute; long press shows the tooltip; the slider takes a drag.

## Tooltip and overlay behaviour

The tooltip belongs to controls, not to the root group: ADR-0004 says never on a group. Spec: the mute button has one tooltip with the output name, state and volume (`Speakers, muted` or `Speakers, 40 percent`); the slider has its own tooltip `Volume` plus its value; the microphone mark has its own tooltip `Microphone muted`. Hovering the root outside these parts shows nothing. One tooltip at a time; 500 ms, 150 ms grace; keyboard focus shows it at once ([[Tooltip]]). Icon-only controls name themselves with a tooltip equal to the accessible name ([[Icon Button]], AR-3 in [[Accessibility Rules]]).

Finding (shared): the tooltip card is a literal copy in the `.tdl` of Audio, Battery, Clock, Media, Network and Tray Item (six modules; the Volume OSD comment shows a seventh pattern): `Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`, padding `[12, 8, 12, 8]`, `Font_Size: 14`, `Foreground: $color.on_surface`, `Alignment: CENTER`, `Gap: 4`. [[Tooltip]] specifies the plain card as `inverse_surface` with `inverse_on_surface`, shape `extra_small` (4 dp), elevation level 0, padding 8 dp by 4 dp, `body_small` 12/16, maximum width 200 dp. The card belongs in one shared tooltip style, not in six modules (candidate request to tess-shell). The Audio root also carries the tooltip today (a group with a tooltip, fails AC-TIP-1).

Overlay: the secondary click opens the Popup `Audio_Outputs` of the same monitor (`Attach: BOTTOM`, `Gap: 4`, `surface_raised`, corner 8); focus moves into the menu on a keyboard open and returns to the mute button on close ([[Popup]], [[12 Overlays]]). Without that Popup in the shell file the click logs a warning and does nothing.

## Motion

The slider handle and the volume change have no module animation. Reduced motion has no effect on the module itself ([[14 Accessibility Basics#Reduced motion|Reduced Motion]]).

## Accessibility

- Roles: root `GROUP` with `Label` (output name) and `Description` (the tooltip text) is accepted because the group holds several controls; mute button `BUTTON`; slider `SLIDER` with `value`, `value_text`, min, max; microphone mark `IMG` with `Label`.
- Names: `Mute` / `Unmute`; `Volume`; `Microphone muted`.
- Keys: see Behaviour.
- Announcements: with `announce` true the module says mute, unmute and a settled volume, politely (`ctx.announce`); default false (the specification names none). Rules in [[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]; a volume drag announces only the settled value.
- Muted is shown by glyph shape and colour (WCAG 2.2 SC 1.4.1).
- Targets: 24 dp minimum at every density.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `show_percent` | false |
| `show_slider` | false |
| `show_mic` | true |
| `step` | 5 percent |
| `announce` | false |

## Acceptance criteria

- [ ] AC-MOD-AUD-1 (AT tree assertion): the mute button has role `BUTTON` and a name `Mute` when unmuted and `Unmute` when muted; the slider has role `SLIDER` and `value_text` ending in `percent`.
- [ ] AC-MOD-AUD-2 (scripted input): no sound server: root `Visible` false, width 0, absent from the accessibility tree, Bar spacing unchanged.
- [ ] AC-MOD-AUD-3 (scripted input): a scroll step of +1 raises the volume by `step` and -1 lowers it; the volume never leaves 0 to 100.
- [ ] AC-MOD-AUD-4 (scripted input): with the mute button focused, Enter and Space toggle mute once each; Up and Down change the volume by `step`; the Menu key opens the outputs popup and Escape closes it with focus back on the mute button.
- [ ] AC-MOD-AUD-5 (scripted input): hover the mute button for 500 ms: exactly 1 tooltip layer whose text names the output and the volume; hover the root gap between two parts: 0 layers.
- [ ] AC-MOD-AUD-6 (static check): no node with role `GROUP` carries a tooltip and no tooltip-bearing node has a tooltip-bearing descendant (AC-TIP-1 of [[Tooltip]]).
- [ ] AC-MOD-AUD-7 (pixel check): muted differs from unmuted in glyph shape as well as colour in a greyscale render.
- [ ] AC-MOD-AUD-8 (geometry check): the mute button container is 40, 32 and 28 dp square and its icon 24, 20 and 20 dp at default, compact and dense; its hit area is at least 24 dp.
- [ ] AC-MOD-AUD-9 (scripted input): with `announce` true, muting queues exactly one polite announcement; with it false none.
- [ ] AC-MOD-AUD-10 (pixel check): the tooltip card equals the plain [[Tooltip]] card; the module `.tdl` holds no card literal.
- [ ] AC-MOD-AUD-11 (contrast script): glyph and text against the Bar surface: text 4.5:1, glyph 3:1 in Light, Dark and High_Contrast.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Audio/Audio_Module.tdl`, `Audio_Style.tdl`, `Audio_Module.py` | partly meets: hides without a sound server, mute button names, muted shape plus colour, slider labels and value text, optional announcements (meets AC-MOD-AUD-1 by reading, -2, -7, -9); tooltip is on the group root, not on controls (fails AC-MOD-AUD-5, -6); scroll and secondary click have no key path (fails AC-MOD-AUD-4); mute button is 32 by 32 with a 16 dp icon at every density (fails AC-MOD-AUD-8 at default); tooltip literal (fails AC-MOD-AUD-10) |
| shell-vault | `shell-vault:40 Specifications/Modules/Audio Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status control | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tooltips per control, none on the root group | owner feedback F8 | [[ADR-0004 Tooltip rule]] |
| Icon button sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
