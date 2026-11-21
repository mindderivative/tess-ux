---
title: Toggle
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, selection, switch]
related: ["[[Switch]]", "[[Form Row]]", "[[Focus Ring]]", "[[State Layers]]", "[[Disabled State]]", "[[Reduced Motion]]", "[[Existing Tokens]]", "[[Owner Feedback 2026-11-20]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
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
| Focus (keyboard) | Focus ring 3 dp, 2 dp offset; not built | [[Focus Ring]] |
| Pressed | Code: root opacity 0.7. Spec: state layer 10 percent and the larger thumb | [[Switch]] |
| Disabled | Opacity 0.5; no focus, no key, no pointer ([[Disabled State]]) | [[Disabled State]] |

## Tokens used

As [[Switch]]: track `primary` on, `surface_variant` off with `outline` border; handle `on_primary` on, `outline` off; state layer in `on_surface` / `primary`. Shell roles map per [[Existing Tokens]].

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Track | 52 by 32 | 52 by 32 | 46 by 28 | [[Switch]]; code: 40 by 22 at all densities |
| Handle off, on, pressed | 16, 24, 28 | 16, 24, 28 | 14, 21, 24 | [[Switch]]; code: 16 fixed |
| Hit area | at least 40 by 32 and 24 by 24 floor |  |  | code 40 by 22: 22 is below the 24 dp floor |

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

The thumb and the track ease over the theme's medium duration (200 ms, `$motion.duration.medium`, `short4`-equal, standard easing) and switch at once under reduced motion ([[Motion]], [[Reduced Motion]]).

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
- [ ] AC-MOD-TGL-8 (scripted pointer): hover the Toggle for 500 ms: only the Toggle's own tooltip, if it has one; hover the row label: only the label's.

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl`, `Stylesheets/Default_Stylesheet.tdl` | partly meets: role, `checked`, Space, disabled, thumb moves (meets AC-MOD-TGL-1, -2, -3, -5 by reading); 40 by 22 track and 16 handle at all densities (fails AC-MOD-TGL-4); hover and pressed are opacity, not state layers; no focus ring |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (Toggle) | exists |
| tess-ui | `tess-ui:src/tess_ui/controls.py`, `src/tess_ui/widgets/selection.py` | see [[Switch]] |
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
