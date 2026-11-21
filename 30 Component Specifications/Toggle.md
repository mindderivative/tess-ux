---
title: Toggle
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, selection, switch]
related: ["[[Switch]]", "[[Form Row]]", "[[Focus Ring]]", "[[State Layers]]", "[[State Layers#Disabled scheme|Disabled State]]", "[[14 Accessibility Basics#Reduced motion|Reduced Motion]]", "[[Existing Tokens]]", "[[Owner Feedback 2026-11-20]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Toggle

> [!info] Summary
> A Toggle is the shell module for an on and off switch: a track and a thumb that slides. It is the shell's implementation of the [[Switch]] specification (Material Design 3 [switch](https://m3.material.io/components/switch/overview)); sizes, states, keys and tests of [[Switch]] apply and this note records what the shell module must change. Source of truth in code: see the last section.

## Purpose

Applies one binary setting at once, for example the config app's options.

## When to use and not

- Use when: a setting turns on or off immediately.
- Do not use when: the choice needs Apply (use a checkbox, see [[Switch]]), or there are more than two states.

## Anatomy

1. Root: `Box`, role `SWITCH`, `Toggles: true`, name from `Label`.
2. Track: rectangle, part `::track`, border 2 dp.
3. Thumb: circle, part `::thumb`, 16 dp in code.
4. State layer and focus ring: from [[State Layers]] and [[Focus Ring]] (spec; code uses an opacity change).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Off, on | Default | `Checked` false or true, set from outside; a click flips it and raises `On_Changed` once with `event.old`, `event.new`, `event.value` |

## States

| State | Visual change | Token values |
|---|---|---|
| Off | Track fill `surface_raised` with a 2 dp `outline` border; thumb `on_surface_muted` at the track start | [[Switch]] |
| On | Track fill and border `primary`; thumb `on_primary` slid to the end | [[Switch]] |
| Hover | Code: root opacity 0.85. Spec: state layer 8 percent | [[State Layers]] |
| Focus (keyboard) | Focus ring 3 dp, 2 dp offset; the shell draws a generic ring (2 px, `color.primary`) that the Toggle gets; width and offset differ from the spec | [[Focus Ring]] |
| Pressed | Code: root opacity 0.7. Spec: state layer 10 percent and the larger thumb | [[Switch]] |
| Disabled | Opacity 0.5; no focus, no key, no pointer ([[State Layers#Disabled scheme|Disabled State]]) | [[State Layers#Disabled scheme|Disabled State]] |

## Tokens used

As [[Switch]]: track `primary` on, `surface_variant` off with `outline` border; handle `on_primary` on, `outline` off; state layer in `on_surface` / `primary`. Shell roles map per [[Existing Tokens]].

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Track | 52 by 32 | 52 by 32 | 46 by 28 | [[Switch]]; code: 40 by 22 at all densities |
| Handle off, on, pressed | 16, 24, 28 | 16, 24, 28 | 14, 21, 24 | [[Switch]]; code: 16 fixed |
| Hit area | at least 40 by 32 and 24 by 24 floor |  |  | code 40 by 22: 22 is below the 24 dp floor |

## Dimensions and defaults

Values follow [[Switch]] (MD3 track 52 by 32 scaled by density).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| root | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], [[Switch]]; code 22 | tess-ui: yes (switch height=); tess-shell: yes (Height); tre: n/a: element absent in tre |
| track | height | - | 32 | 32 | 28 | [[Switch]] sizing rule; code 22 | tess-ui: no hook; tess-shell: yes (Height); tre: n/a: element absent in tre |
| track | min width | - | 52 | 52 | 46 | [[Switch]], MD3 switch https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-switch.scss; code 40 | tess-ui: no hook; tess-shell: yes (Min_Width); tre: n/a: element absent in tre |
| root | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.2 SC 2.5.8 | tess-ui: no hook; tess-shell: yes (Min_Height); tre: n/a: element absent in tre |
| thumb (off) | height | - | 16 | 16 | 14 | [[Switch]]; code 16 | tess-ui: no hook; tess-shell: yes (Height); tre: n/a: element absent in tre |
| thumb (on) | height | - | 24 | 24 | 21 | [[Switch]]; code 16 | tess-ui: no hook; tess-shell: yes (Height); tre: n/a: element absent in tre |
| thumb (pressed) | height | - | 28 | 28 | 24 | [[Switch]]; code 16 | tess-ui: no hook; tess-shell: yes (Height); tre: n/a: element absent in tre |
| root | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]]; the track fills the root | tess-ui: n/a: the track is centred in the target, no padding; tess-shell: yes (Padding); tre: n/a: element absent in tre |
| thumb | margin | - | N/A: the thumb is inset by half the track-handle difference (8 off, 4 on at default), placed by track state | N/A: same as the default column | N/A: as in Default | [[Switch]]; code `Margin [3, 3, 0, 0]` off, `[21, 3, 0, 0]` on | tess-ui: no hook; tess-shell: yes (Margin); tre: n/a: element absent in tre |
| root | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Switch]] (label gap to track); the label is a separate control, [[Form Row]] | tess-ui: n/a: the switch has no label; tess-shell: yes (Spacing); tre: n/a: element absent in tre |
| track | border width | - | 2 | 2 | 2 | MD3 switch https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-switch.scss; code 2 | tess-ui: no hook; tess-shell: yes (Border_Width); tre: n/a: element absent in tre |
| track (off) | border color | `outline` | `outline` | `outline` | `outline` | [[Switch]], [[Colour Roles]]; code `outline` | tess-ui: no hook; tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| track (on) | border color | `primary` | `primary` | `primary` | `primary` | [[Switch]], [[Colour Roles]]; code `primary` | tess-ui: yes (color=); tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| track | corner radius | `shape.full` | 16 | 16 | 14 | [[Shape]]; half the track height | tess-ui: no hook; tess-shell: yes (Corner_Radius); tre: n/a: element absent in tre |
| root | font | - | N/A: the Toggle draws no text; the label is a separate control | N/A: same as the default column | N/A: as in Default | [[Typography]] | tess-ui: n/a: the switch draws no text; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| thumb | icon size | - | N/A: the Toggle draws no handle icon; the thumb position and size show the state | N/A: same as the default column | N/A: as in Default | [[Iconography]] | tess-ui: no hook; tess-shell: yes (Width, Height of the SVG block); tre: n/a: element absent in tre |
| track | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]], MD3 switch https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-switch.scss | tess-ui: n/a: the switch has no elevation; tess-shell: yes (Elevation percentage); tre: n/a: element absent in tre |

## Layout and overflow

The module is a fixed-size box; vertical centring inside a [[Form Row]] by construction. The label is a separate control with its own tooltip and hit area ([[Form Row]], ADR-0004).

## Behaviour

- Pointer: press and release on the track flips it once; a press that ends outside cancels.
- Keyboard: Tab focuses; Space flips and raises `On_Changed` once; Enter does nothing (APG switch pattern: Space toggles).
- Touch: tap flips; hit area 48 dp high in touch contexts.
- `Checked` set from the module moves the thumb and raises nothing; the user's flip stays until `Checked` is set to a different value.

## Tooltip and overlay behaviour

A tooltip, if any, belongs to the Toggle only, never to its row; hovering the label shows only the label's tooltip ([[Tooltip]], [[Switch]] AC-SWI-8). A click never draws a tooltip and removes a shown one (F9). 500 ms, 150 ms grace.

## Motion

The thumb and the track ease over the theme's medium duration (200 ms, `$motion.duration.medium`, `short4`-equal, standard easing) and switch at once under reduced motion ([[Motion]], [[14 Accessibility Basics#Reduced motion|Reduced Motion]]).

## Accessibility

- Role: `SWITCH` with state `checked`; name from `Label` (the author must give one or associate the row's label).
- Keys: Space flips; Enter does nothing.
- Announcements: the state change is read by the screen reader from `checked`; the module announces nothing itself.
- Contrast: thumb against track 3:1, track or border against surface 3:1 in off and on ([[Switch]] AC-SWI-7); state is carried by position, not colour alone.

## Dark and light

Track and thumb roles follow the scheme ([[Theme Following the System]]); `Default_Stylesheet.tdl` sets them for dark base, `Light` and `High_Contrast`.

## Defaults

| Setting | Default |
|---|---|
| `Checked` | false |
| `Label` | empty |
| Size | 40 by 22 in code |

## Acceptance criteria

- [ ] AC-MOD-TGL-1 (AT tree assertion): the node has role `SWITCH`, a non-empty name, `checked` equal to the state and `disabled` equal to the state.
- [ ] AC-MOD-TGL-2 (scripted input): Space on the focused Toggle flips it once and raises `On_Changed` once with matching `old`, `new` and `value`; Enter flips nothing; setting `Checked` from the module raises none.
- [ ] AC-MOD-TGL-3 (scripted input): press on the track, move outside, release: no flip and no event.
- [ ] AC-MOD-TGL-4 (geometry check): track and handle sizes equal the [[Switch]] table at each density and the hit area is at least 24 dp by 24 dp.
- [ ] AC-MOD-TGL-5 (scripted input): with reduced motion on the thumb reaches its final position in the first frame after the event.
- [ ] AC-MOD-TGL-6 (pixel check): a pointer click leaves no pixel changed outside the Toggle box plus state layer and focus ring (F9).
- [ ] AC-MOD-TGL-7 (contrast script): thumb against track at least 3:1 and track against surface at least 3:1 in off and on, in Light, Dark and High_Contrast.
- [ ] AC-MOD-TGL-8 (scripted input): hover the Toggle for 500 ms: only the Toggle's own tooltip, if it has one; hover the row label: only the label's.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl`, `Stylesheets/Default_Stylesheet.tdl` | partly meets: role, `checked`, Space, disabled, thumb moves (meets AC-MOD-TGL-1, -2, -3, -5 by reading); 40 by 22 track and 16 handle at all densities (fails AC-MOD-TGL-4); hover and pressed are opacity, not state layers; no focus ring |
| tess-shell | `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl` (dimensions) | differs: root and track 40 by 22 (spec 52 by 32, 52 by 32, 46 by 28), thumb 16 fixed (spec 16, 24, 28 / 14, 21, 24); fails AC-MOD-TGL-4 |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (Toggle) | exists |
| tess-ui | `tess-ui:src/tess_ui/controls.py`, `src/tess_ui/widgets/selection.py` | see [[Switch]]; the track, handle and border sizes are class constants of `controls.Switch` with no hook |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Track and handle scaled by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltip on the Toggle only | owner feedback F8 | [[ADR-0004 Tooltip rule]] |

## Sources

- Material Web switch tokens (track 52 by 32, handles 16, 24, 28, state layer 40): https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-switch.scss (as cited in [[Switch]]).
- WAI-ARIA Authoring Practices, switch pattern: https://www.w3.org/WAI/ARIA/apg/patterns/switch/ (Space toggles; Enter optional).
- WCAG 2.2 SC 2.5.8: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
