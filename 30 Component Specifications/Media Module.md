---
title: Media Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, media]
related: ["[[Bar]]", "[[Icon Button]]", "[[Button]]", "[[Slider]]", "[[Marquee Text]]", "[[Image]]", "[[State Layers#Disabled scheme|Disabled State]]", "[[Iconography#Fallback icon|Empty and Error States]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "[[14 Accessibility Basics#Reduced motion|Reduced Motion]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Media Module

> [!info] Summary
> The Media Module shows what an MPRIS media player plays and offers previous, play or pause and next as icon buttons, the title in a [[Marquee Text]], optional artwork and a position slider. No Material Design 3 counterpart (Tesserae-specific; nearest patterns: [[Icon Button]] group, [[Slider]] and a media control bar). Source of truth in code: see the last section.

## Purpose

Control the playing media from the Bar and see the track, artist and player without switching windows.

## When to use and not

- Use when: the Bar should control a running MPRIS player.
- Do not use when: the user needs a playlist, a queue or a full player (not in v1).

## Anatomy

1. Root: horizontal box, role `GROUP`, name from `label`. It is a container and carries no tooltip.
2. Artwork (optional): [[Image]] 24 by 24 dp, placeholder `mdi:music`.
3. Previous, Play or Pause, Next: icon [[Button]]s with names `Previous`, `Play` or `Pause`, `Next`.
4. Title: [[Marquee Text]], width `max_width` (240 dp default), scrolls when the text is wider.
5. Position (optional): [[Slider]] named `Position` with value text `1:23 of 3:45`.
6. Tooltip: the title, artist, player and state, on the title.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Controls and title | Default | `show_controls`, `show_title` true |
| With artwork | Wide bars | `show_art` true |
| With position | Seekable players | `show_position` true: a slider and a one-second tick while the player plays |
| Title only | Narrow bars | `show_controls` false |

## States

| State | Visual change | Token values |
|---|---|---|
| Playing, paused, stopped | The play button's glyph changes (`pause` while playing, `play` otherwise) and its name changes (`Pause`, `Play`) | glyph shape, not colour |
| Control the player cannot do | That button is disabled (`can_previous`, `can_play_pause`, `can_next`; the slider when `can_seek` is false): label and icon at 38 percent, no hover, no press, no tooltip, no focus | [[State Layers#Disabled scheme|Disabled State]] |
| Hover, focus, pressed (buttons) | State layers 8, 10, 10 percent and focus ring ([[Button]], [[Icon Button]]) | [[State Layers]] |
| Title cut | Ellipsis while not scrolling (disabled or reduced motion), full text in the tooltip | [[Marquee Text]] |
| Hidden (service absent) | No bus or no player: hidden. Hidden means `Visible: false` on the root: the module takes no space in the [[Bar]], no spacing is left beside it, no placeholder is drawn and the root is absent from the accessibility tree. The player closing hides the module; a player starting shows it | root `Visible: <| available and has_player |>` |
| Loading artwork | Placeholder icon until the image decodes; a bad file shows the error image | [[Image]], [[Iconography#Fallback icon|Empty and Error States]] |

## Tokens used

Buttons and slider tokens come from [[Icon Button]] and [[Slider]]; title text is `label_large` in `on_surface`; no card, no elevation.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Control container (previous, play, next) | 40 | 32 | 28 | [[Icon Button]]; code: [[Button]] 32 px with an icon |
| Control icon | 24 | 20 | 20 | `density.icon_button_icon` |
| Artwork | 24 | 24 | 24 | fixed in the Bar row; at dense it is 24 inside a 28 dp row |
| Gap between parts | 4 | 4 | 4 | `space.2`; adjacent hit areas must not overlap (AC-DEN-8 of [[Spacing and Density]]) |
| Title width | 240 | 240 | 240 | `max_width` param |
| Position slider | see [[Slider]] | see [[Slider]] | see [[Slider]] | code 160 by 20 |

## Layout and overflow

One row, no wrapping. Vertical centring of every part. Title overflow: the Marquee scrolls when wider than `max_width`; with reduced motion the title ends in an ellipsis ([[Marquee Text]], [[10 Layout Overflow and Scrolling]]). When the Bar slot is too narrow the optional parts are switched off by params.

## Behaviour

- Pointer: click a control calls the player; the icon follows the player's own `PlaybackStatus` signal (the module changes nothing locally). The slider drag sends nothing until release: `On_Released` sends the position once.
- Keyboard: Tab through Previous, Play, Next, Position; Enter and Space press a button; Left and Right on the slider move by a step ([[Slider]]); a disabled control is skipped.
- Touch: tap controls; long press shows tooltips.

## Tooltip and overlay behaviour

Tooltips belong to controls: each of Previous, Play, Next has a tooltip equal to its name; the title has one tooltip carrying `Title, Artist (Player), state` (the Marquee's own whole-text tooltip is replaced by it: the module needs a way to override the Marquee tooltip text, a candidate request to tess-shell); the position slider has a tooltip with its value text. The root group has none (today the root carries the tooltip and the Marquee carries its own, so hovering the title shows two competing tooltips: fails AC-TIP-1 and F8). 500 ms, 150 ms grace, keyboard focus immediate, dismissal list as [[Tooltip]]. Icon-only controls name themselves with a tooltip equal to the accessible name ([[Icon Button]], AR-3 in [[Accessibility Rules]]).

Finding (shared): the tooltip card is a literal copy in the `.tdl` of Audio, Battery, Clock, Media, Network and Tray Item (six modules; the Volume OSD comment shows a seventh pattern): `Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`, padding `[12, 8, 12, 8]`, `Font_Size: 14`, `Foreground: $color.on_surface`, `Alignment: CENTER`, `Gap: 4`. [[Tooltip]] specifies the plain card as `inverse_surface` with `inverse_on_surface`, shape `extra_small` (4 dp), elevation level 0, padding 8 dp by 4 dp, `body_small` 12/16, maximum width 200 dp. The card belongs in one shared tooltip style, not in six modules (candidate request to tess-shell).

## Motion

The slider handle and the Marquee are the only moving parts. The one-second position tick moves the slider by value, not by animation. Reduced motion: the Marquee stops and shows an ellipsis ([[14 Accessibility Basics#Reduced motion|Reduced Motion]]).

## Accessibility

- Roles: root `GROUP` (holds controls), buttons `BUTTON`, slider `SLIDER` with `value_text`, artwork `IMG` hidden unless named.
- Names: `Previous`, `Play` or `Pause`, `Next`, `Position`; root name `label` = `Song, Artist (Player), paused`; description = the tooltip.
- Keys: as Behaviour.
- Announcements: with `announce` true a new track is said once, politely, `Track changed: Song, Artist` (`Media_Module.py`); default false. The position tick is never announced ([[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]).
- Disabled controls are not focusable (AR-7).

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `show_art` | false |
| `show_title` | true |
| `show_controls` | true |
| `show_position` | false |
| `max_width` | 240 |
| `announce` | false |

## Acceptance criteria

- [ ] AC-MOD-MED-1 (AT tree assertion): Previous, Play, Next have role `BUTTON` and names `Previous`, `Play` or `Pause`, `Next`; the position slider has role `SLIDER` and `value_text` of the form `m:ss of m:ss`.
- [ ] AC-MOD-MED-2 (scripted input): no player: root `Visible` false, width 0, absent from the accessibility tree, Bar spacing unchanged; a player appearing shows the module.
- [ ] AC-MOD-MED-3 (scripted input): a player with `can_next` false: Next is disabled, takes no focus, no press and no tooltip.
- [ ] AC-MOD-MED-4 (scripted input): Tab visits Previous, Play, Next and Position once each in order and leaves; Enter on Play calls play or pause once.
- [ ] AC-MOD-MED-5 (scripted input): hover Play for 500 ms: one tooltip layer with text `Play` or `Pause`; hover the title: one layer with title, artist, player and state; never two layers.
- [ ] AC-MOD-MED-6 (static check): no node with role `group` carries a tooltip; no tooltip-bearing node has a tooltip-bearing descendant.
- [ ] AC-MOD-MED-7 (scripted input): a slider drag to 50 percent sends no player call until release; release sends exactly one seek.
- [ ] AC-MOD-MED-8 (geometry check): control containers are 40, 32 and 28 dp square at default, compact and dense; hit areas at least 24 dp and non-overlapping.
- [ ] AC-MOD-MED-9 (scripted input): with reduced motion on, a long title shows an ellipsis and creates no animation.
- [ ] AC-MOD-MED-10 (pixel check): the tooltip card equals the plain [[Tooltip]] card; the module `.tdl` has no card literal.
- [ ] AC-MOD-MED-11 (scripted input): with `announce` true a track change queues exactly one polite `Track changed:` announcement.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Media/Media_Module.tdl`, `Media_Module.py` | partly meets: hides without a player, disabled controls, button names, position value text, optional track announcement (meets AC-MOD-MED-1, -2, -3, -4, -7, -11 by reading); tooltip on the group root and a second one on the Marquee (fails AC-MOD-MED-5, -6); controls are 32 px [[Button]]s with literal sizes (fails AC-MOD-MED-8 at default); tooltip literal (fails AC-MOD-MED-10) |
| shell-vault | `shell-vault:40 Specifications/Modules/Media Module.md` | exists |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status control | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Tooltip per control, none on the group | owner feedback F8 | [[ADR-0004 Tooltip rule]] |
| Control sizes by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
