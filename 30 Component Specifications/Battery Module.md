---
title: Battery Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, status, service]
related: ["[[Bar]]", "[[Icon]]", "[[Text]]", "[[Icons]]", "[[Accessibility Announcements]]", "[[Accessibility Roles]]", "[[Empty and Error States]]", "[[Existing Tokens]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Battery Module

> [!info] Summary
> The Battery Module shows the charge of the machine's battery as an icon, a percentage and a tooltip with the state and the time left; it hides itself when there is no battery. No Material Design 3 counterpart (Tesserae-specific status indicator). Source of truth in code: see the last section.

## Purpose

Shows the charge level, the charging state and the time to empty or full from UPower's aggregate display device, and warns at the levels the desktop sets (`low`, `critical`). Read-only in v1.

## When to use and not

- Use when: the Bar runs on a machine that can have a battery.
- Do not use when: the user needs per-device batteries, history or power profiles (not in v1).
- Not a progress indicator: it states a level, it is not a task progress ([[Progress Bar]]).

## Anatomy

1. Root: one box, role `IMG` recommended (see Accessibility), carries the tooltip.
2. Level box: one of three boxes shown one at a time (normal, low, critical).
3. Glyph: an [[Icon]] 16 dp tall, chosen from the charge step and state (`battery-10` to `battery-90`, `battery-charging-*`, `battery-alert`); at low and critical the glyph is the alert icon with a `+dot` beside it in one document, 24 by 16 dp.
4. Percentage: [[Text]] `label_large`, optional (`show_percent`, default true).
5. Tooltip: plain, for example `82 %, discharging, 2 h 14 min left`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Icon and percent | Default | `show_percent` true |
| Icon only | Narrow bars | `show_percent` false; accessible name still carries the percentage |

## States

| State | Visual change | Token values |
|---|---|---|
| Normal | Glyph and text in `on_surface` | the Level box |
| Low (UPower WarningLevel 3) | Alert glyph with dot (shape change) and glyph and text in `warning` | `warning` on the surface: 10.02:1 dark, 5.51:1 light (measured from `Default_Theme.tdl`) |
| Critical (WarningLevel 4 and 5) | Alert glyph with dot and glyph and text in `error`; announced once | `error`: 8.11:1 dark, 6.08:1 light |
| Charging, full, empty, unknown | The glyph changes shape (charging bolt, full battery, `battery-alert-variant-outline`, `battery-unknown`); colour is the text colour | icon table in the shell vault note |
| Hover, focus, pressed, selected, disabled | Not applicable: no action, not focusable | not applicable |
| Hidden (service absent) | No UPower on the bus, or `IsPresent` false: the module is hidden. Hidden means `Visible: false` on the root: the module takes no space in the [[Bar]], no spacing is left beside it, no placeholder is drawn and the root is absent from the accessibility tree. The user sees nothing and the Bar closes up; when a battery appears the module shows itself | root `Visible: <| available and present |>` |
| Loading | Before the first read the module is hidden (`present` false); no spinner | not applicable |

## Tokens used

Roles: `on_surface` (normal), `warning` and `error` (the shell's extended roles, not MD3 roles; see [[Existing Tokens]]); `label_large` for the percentage; no shape, no elevation. A colour change never stands alone: low and critical also change the glyph shape (WCAG 2.2 SC 1.4.1).

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Glyph | 16 | 16 | 16 | inline status icon ([[Iconography]]) |
| Alert glyph (with dot) | 24 by 16 | 24 by 16 | 24 by 16 | one document, dot beside the icon |
| Gap glyph to percentage | 4 | 4 | 4 | `space.2` |
| Hover box minimum height | 24 | 24 | 24 | `target.min` |

## Layout and overflow

One line. Vertical centring of the glyph and the text in the row ([[10 Layout Overflow and Scrolling]]). The Root keeps its size from the shown level box so the hover area does not depend on the glyph. No truncation: the text is at most 4 characters (`100 %`). The three level boxes exist from the start and only `Visible` changes (a created box with a coloured icon was left undrawn on KWin, M5b).

## Behaviour

- Pointer: hover shows the tooltip; no click action in v1.
- Keyboard: not focusable; the name and description are read through the accessibility tree.
- Touch: long press shows the tooltip.
- Updates: UPower `PropertiesChanged`; the module never polls; a value is sent only when it changes.

## Tooltip and overlay behaviour

One tooltip, on the content box (the single control of the module). The module is not a group of controls, so the tooltip may stay on the module box; the box carries role `IMG` (never `group`, AC-TIP-1 of [[Tooltip]]). ADR-0004 and ADR-0011 apply (500 ms, 150 ms grace, dismissal list).

Finding (shared): the tooltip card is a literal copy in the `.tdl` of Audio, Battery, Clock, Media, Network and Tray Item (six modules; the Volume OSD comment shows a seventh pattern): `Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`, padding `[12, 8, 12, 8]`, `Font_Size: 14`, `Foreground: $color.on_surface`, `Alignment: CENTER`, `Gap: 4`. [[Tooltip]] specifies the plain card as `inverse_surface` with `inverse_on_surface`, shape `extra_small` (4 dp), elevation level 0, padding 8 dp by 4 dp, `body_small` 12/16, maximum width 200 dp. The card belongs in one shared tooltip style, not in six modules (candidate request to tess-shell).

The tooltip text is also the accessible description; the percentage, the state and the time left are therefore not hover-only.

## Motion

No animation (the glyph changes in one frame). Reduced motion has no effect.

## Accessibility

- Role: `IMG` with `Label` (name) and `Description` (the tooltip text). Code today: `GROUP` with `Label` and `Description` (see Status in code).
- Name: `Battery 82 percent, discharging` (`label` from the Python); description: the tooltip.
- Keys: none.
- Announcements: when the level becomes critical the module says once, politely, `Battery critical, 4 percent, discharging` through `ctx.announce` (`Battery_Module.py` `announcement_text`); no other change is announced; mute and repeat rules in [[Accessibility Announcements]].
- Colour is not the only cue: shape of the glyph plus the word in the name.
- Contrast: text 4.5:1 and glyph 3:1 against the Bar surface in all three schemes.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three. `warning` is `#E6BB6A` on dark and `#8A5A00` on light; `error` is `#F2958C` and `#B3261E`; high contrast inherits the dark values of both (the theme `High_Contrast` mode sets no `Warning` or `Error`).

## Defaults

| Setting | Default |
|---|---|
| `show_percent` | true |
| Glyph size | 16 dp (alert 24 by 16) |
| Hidden without UPower or battery | yes |

## Acceptance criteria

- [ ] AC-MOD-BAT-1 (AT tree assertion): with a fake UPower reporting 82 percent discharging: the root has a non-empty name containing `82` and the word `discharging`, a description equal to the tooltip text, and role `IMG`.
- [ ] AC-MOD-BAT-2 (scripted input): UPower absent: the root has `Visible` false, width 0, no accessibility node, and the Bar siblings keep their spacing (no gap left).
- [ ] AC-MOD-BAT-3 (scripted input): UPower present with `IsPresent` false then true: the module hides then shows within one loop turn, no restart.
- [ ] AC-MOD-BAT-4 (scripted pointer): hover for 500 ms shows one tooltip with the state text; leaving removes it within 150 ms plus one frame; Escape within one frame.
- [ ] AC-MOD-BAT-5 (static check): exactly one node of the module has a `Tooltip`; none has role `group`; none has a tooltip-bearing descendant.
- [ ] AC-MOD-BAT-6 (pixel check): low and critical differ from normal in glyph shape (the alert glyph with dot) as well as colour: a greyscale render distinguishes all three.
- [ ] AC-MOD-BAT-7 (contrast script): percentage text in normal, low and critical against the Bar surface is at least 4.5:1 and the glyph at least 3:1 in Light, Dark and High_Contrast.
- [ ] AC-MOD-BAT-8 (scripted input): with a fake WarningLevel 4: exactly one polite announcement `Battery critical, <n> percent` is queued; repeating the same level queues none.
- [ ] AC-MOD-BAT-9 (pixel check): the tooltip card equals the plain [[Tooltip]] card; the module's `.tdl` holds no tooltip card literals.
- [ ] AC-MOD-BAT-10 (geometry check): the hover box is at least 24 dp high at every density; the glyph is 16 dp square, 24 by 16 for the alert glyph.

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Battery/Battery_Module.tdl`, `Battery_Style.tdl`, `Battery_Module.py` | partly meets: hides without UPower (meets AC-MOD-BAT-2), colour plus shape (meets AC-MOD-BAT-6), one polite announcement at critical (meets AC-MOD-BAT-8), name and description set; root role is `GROUP` and carries the tooltip (fails AC-MOD-BAT-1 and AC-MOD-BAT-5); tooltip card literal (fails AC-MOD-BAT-9); alert glyph width is 24 literal |
| shell-vault | `shell-vault:40 Specifications/Modules/Battery Module.md` | exists, status draft |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status module; baseline MD3 only for roles and shape names | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Roles `warning` and `error` for state text | the shell theme has no MD3 tertiary or extended roles; state keeps a second cue | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
