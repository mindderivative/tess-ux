---
title: Network Module
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, bar, status, service]
related: ["[[Bar]]", "[[Icon]]", "[[Text]]", "[[Icons]]", "[[Accessibility Announcements]]", "[[Accessibility Roles]]", "[[Empty and Error States]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Network Module

> [!info] Summary
> The Network Module shows how the machine is connected: an icon for the kind and state, a second icon while a VPN is up, an optional connection name and a tooltip with the details. No Material Design 3 counterpart (Tesserae-specific status indicator). Source of truth in code: see the last section.

## Purpose

Shows whether the machine is online, by which kind of connection and how strong the Wi-Fi signal is, from NetworkManager. Read-only in v1.

## When to use and not

- Use when: the Bar should show the primary connection.
- Do not use when: the user must switch Wi-Fi, join networks or control a VPN (not in v1; a [[Popup]] menu is a later module).

## Anatomy

1. Root: one box, role `IMG` recommended, carries the tooltip.
2. Level box: one of three boxes shown one at a time: connected or connecting, warning (limited, portal), muted (disconnected, disabled, unknown).
3. Glyph: [[Icon]] 16 dp: `wifi-strength-1` to `-4`, `wifi-alert`, `wifi-sync`, `ethernet`, `lan-disconnect`, `lan-pending`, `cellphone-wireless`, `bluetooth`, `network`, `network-off`, `wifi-off`, `network-outline`.
4. VPN glyph: `mdi:vpn`, 16 dp, shown while any VPN is active (`show_vpn`).
5. Name: [[Text]] `label_large`, optional (`show_name`).
6. Tooltip: plain, for example `Home-WiFi, Wi-Fi 70 %, connected`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Icon only | Default | `show_name` false, `show_vpn` true |
| With name | Wide bars | `show_name` true: the connection or access point name follows the glyph |

## States

| State | Visual change | Token values |
|---|---|---|
| Connected, connecting | Glyph in `on_surface`; connecting is a different glyph (`wifi-sync`, `lan-pending`) | text colour |
| Limited, portal | Alert glyph in `warning` | `warning` 10.02:1 dark, 5.51:1 light on the surface |
| Disconnected, disabled, unknown | `network-off`, `wifi-off`, `network-outline` in `on_surface_muted` | `on_surface_muted` 7.96:1 dark, 6.70:1 light on the surface |
| VPN up | Second glyph beside the first, same colour as the level | `mdi:vpn` |
| Hover, focus, pressed, selected, disabled | Not applicable: no action, not focusable | not applicable |
| Hidden (service absent) | NetworkManager is not on the system bus: hidden. Hidden means `Visible: false` on the root: the module takes no space in the [[Bar]], no spacing is left beside it, no placeholder is drawn and the root is absent from the accessibility tree. A machine that is disconnected or has networking off is not hidden: the muted glyph says so | root `Visible: <| available and ready |>` |

## Tokens used

Roles: `on_surface`, `warning`, `on_surface_muted`; `label_large` for the name. Colour is never the only cue: every state has its own glyph (WCAG 2.2 SC 1.4.1).

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Glyph | 16 | 16 | 16 | inline status icon ([[Iconography]]) |
| Gap between glyphs and text | 4 | 4 | 4 | `space.2` |
| Hover box minimum height | 24 | 24 | 24 | `target.min` |
| Name text maximum width | 160 | 160 | 160 | ellipsis beyond; a Tesserae choice, not in code (code does not truncate) #needs-verification |

## Layout and overflow

One line. Vertical centring in the Bar row. The Root keeps its size from the shown level box. The connection name uses `Overflow: ELLIPSIS` at 160 dp and the tooltip carries the full name ([[10 Layout Overflow and Scrolling]]); today the name is not truncated.

## Behaviour

- Pointer: hover shows the tooltip; no click in v1.
- Keyboard: not focusable; name and description are read from the accessibility tree.
- Touch: long press shows the tooltip.
- Updates: NetworkManager `PropertiesChanged` on the manager, the primary connection, its device and its access point; never polls; `strength` is sent only when the icon step or the rounded value changes.

## Tooltip and overlay behaviour

One tooltip, on the content box (one control), never a group. 500 ms, 150 ms grace, dismissal list of ADR-0004 and ADR-0011. The tooltip text is also the accessible description.

Finding (shared): the tooltip card is a literal copy in the `.tdl` of Audio, Battery, Clock, Media, Network and Tray Item (six modules; the Volume OSD comment shows a seventh pattern): `Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`, padding `[12, 8, 12, 8]`, `Font_Size: 14`, `Foreground: $color.on_surface`, `Alignment: CENTER`, `Gap: 4`. [[Tooltip]] specifies the plain card as `inverse_surface` with `inverse_on_surface`, shape `extra_small` (4 dp), elevation level 0, padding 8 dp by 4 dp, `body_small` 12/16, maximum width 200 dp. The card belongs in one shared tooltip style, not in six modules (candidate request to tess-shell).

## Motion

No animation. Reduced motion has no effect.

## Accessibility

- Role: `IMG` with `Label` and `Description` (code today: `GROUP`).
- Name: `Network connected, Wi-Fi Home-WiFi` style text from the Python (`label`); description: the tooltip.
- Keys: none.
- Announcements: one polite announcement when `state` goes to or from `CONNECTED`: `Network connected, Wi-Fi Home-WiFi, VPN <name>` or `Network disconnected`; the signal strength is left out (`Network_Module.py` `announcement_text`).
- Colour is not the only cue; contrast 4.5:1 text and 3:1 glyph in all schemes.

## Dark and light

Colours resolve from theme tokens: the shell theme `Default` has a dark base block, a `Light` mode and a `High_Contrast` mode (`tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl`); the mode follows the system ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). The module uses roles only, no literal colour; the contrast acceptance criteria hold in all three.

## Defaults

| Setting | Default |
|---|---|
| `show_name` | false |
| `show_vpn` | true |
| Hidden without NetworkManager | yes |

## Acceptance criteria

- [ ] AC-MOD-NET-1 (AT tree assertion): with a fake NetworkManager (Wi-Fi 70 percent, connected): the root has role `IMG`, a name containing `Wi-Fi` and `connected`, a description equal to the tooltip text.
- [ ] AC-MOD-NET-2 (scripted input): NetworkManager absent: root `Visible` false, width 0, no accessibility node, no spacing left in the Bar; NetworkManager present with networking off: root visible with the `wifi-off` glyph.
- [ ] AC-MOD-NET-3 (scripted pointer): hover 500 ms shows one tooltip, text equal to the description; leave removes it within 150 ms plus one frame.
- [ ] AC-MOD-NET-4 (static check): one node with a `Tooltip`, role not `group`, no tooltip descendants.
- [ ] AC-MOD-NET-5 (pixel check): a greyscale render distinguishes connected, limited and disconnected by glyph shape alone.
- [ ] AC-MOD-NET-6 (contrast script): glyph and text colours (`on_surface`, `warning`, `on_surface_muted`) against the Bar surface: text at least 4.5:1, glyph at least 3:1 in Light, Dark and High_Contrast.
- [ ] AC-MOD-NET-7 (scripted input): a state change CONNECTED to DISCONNECTED queues exactly one polite announcement; a strength change alone queues none.
- [ ] AC-MOD-NET-8 (pixel check): the tooltip card equals the plain [[Tooltip]] card; the module `.tdl` holds no card literal.
- [ ] AC-MOD-NET-9 (geometry check): glyphs are 16 dp square; hover box at least 24 dp high.
- [ ] AC-MOD-NET-10 (token test): the icon table of the shell vault note maps every (kind, state) pair to an existing `mdi` icon name; a missing name fails.

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Network/Network_Module.tdl`, `Network_Style.tdl`, `Network_Module.py` | partly meets: hides without NetworkManager, three boxes with `Visible`, state glyphs, polite announcement (meets AC-MOD-NET-2, -5, -7); root role `GROUP` with tooltip (fails AC-MOD-NET-1, -4); tooltip literal (fails AC-MOD-NET-8); name is not truncated (the ellipsis rule is not built) |
| shell-vault | `shell-vault:40 Specifications/Modules/Network Module.md` | exists, status accepted |
| tess-ui | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| No MD3 counterpart | Tesserae-specific status module | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Roles `warning` and `on_surface_muted` for state | second cue is the glyph | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- WCAG 2.2 SC 1.4.13 Content on Hover or Focus: https://www.w3.org/WAI/WCAG22/Understanding/content-on-hover-or-focus.html (dismissible, hoverable, persistent). Verified 2026-11-21.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html. SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. Verified 2026-11-21 (pages return 200; claims taken from the Understanding documents).
- WAI-ARIA 1.2 roles (`img`, `group`, `button`, `status`, `switch`, `list`, `listitem`, `menu`, `menuitem`, `textbox`): https://www.w3.org/TR/wai-aria-1.2/
- WAI-ARIA Authoring Practices, tooltip pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Modules.md`, `tess-shell:docs/guide/modules.md`, and the paths in Source of truth in code.
