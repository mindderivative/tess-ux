---
title: Switch
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, selection, owner-feedback]
related: ["[[Owner Feedback 2026-11-20]]", "[[Form Row]]", "[[Text Field]]", "[[Tooltip]]", "[[Icon Button]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[Colour Roles]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Tooltip]]"]
---

# Switch

> [!info] Summary
> A control that turns one setting on or off and takes effect at once: the Material Design 3 [switch](https://m3.material.io/components/switch/overview), with a density scaling rule for desktop. Source of truth in code: see the last section.

## Purpose

Apply a binary setting immediately (Wi-Fi, a feature flag in the config app). The owner's live demo (2026-11-20) showed F8 and F9 on switches: the whole row's tooltip appeared when the switch was hovered, and clicking the switch drew tooltip text over everything with no background ([[Owner Feedback 2026-11-20]]).

## When to use and not

- Use when: the change applies immediately, the two states are on and off, and a label names the setting.
- Do not use when: the choice needs Save or Apply to take effect, or several options may be picked from a list (use a Checkbox, specified later); or the two states are not on and off (use a segmented control or radio group).

## Anatomy

1. Track: a pill, 52 by 32 dp at scale 1.0.
2. Handle (thumb): a circle that slides along the track and grows (16 dp off, 24 dp on, 28 dp pressed; 24 dp off and on when icons are shown).
3. Handle icon (optional): check when on, cross when off, 16 dp.
4. State layer: a circle of 40 dp centred on the handle, drawn on hover, focus and press per [[State Layers]].
5. Label: text beside the track, part of the press target.
6. Focus ring: around the track, keyboard focus only ([[Focus Ring]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Plain | default | no icon on the handle; off handle 16 dp, on handle 24 dp |
| With icons | when state needs a shape cue beyond colour | check on, cross off; off and on handles both 24 dp |
| Labelled | always in forms | label to the end side of the track (start side in right-to-left locales) |

## States

State layer percentages and the focus ring come from [[State Layers]] (hover 8, focus 10, pressed 10 percent; disabled content 38, container 12 percent, [[ADR-0009 State layer percentages]]). Colours from the Material Web switch tokens, [v0_192/_md-comp-switch.scss](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-switch.scss):

| State | Track | Handle | Other |
|---|---|---|---|
| Off, rest | fill `surface_container_highest`, 2 dp border `outline` | 16 dp, `outline` | icon (if shown) `surface_container_highest` |
| Off, hover, focus, pressed | as rest | as rest, pressed 28 dp | state layer in `on_surface` at the State Layers percentage |
| On, rest | fill `primary` | 24 dp, `on_primary` | icon `on_primary_container` |
| On, hover, focus, pressed | as rest | as rest, pressed 28 dp | state layer in `primary` at the State Layers percentage |
| Disabled, off | fill `surface_container_highest` at 12 percent, border `on_surface` at 12 percent | `on_surface` at 38 percent | label `on_surface` at 38 percent |
| Disabled, on | fill `on_surface` at 12 percent | `surface` | icon `on_surface` at 38 percent |
| Keyboard focus | as the state | as the state | focus ring 3 dp wide, 2 dp offset, role `secondary`, around the track |

State changes show more than colour: the handle moves and changes size, and the on state carries the icon option ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).

## Tokens used

[[Colour Roles]] (roles above), [[Shape]] (track and handle `corner-full`), [[Motion]] (handle slide `medium2` 300 ms with `emphasized_decelerate`; colour fade `short3` 150 ms; handle growth `short2` 100 ms), [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

MD3 track 52 by 32 dp, handles 16, 24, 28 dp, state layer 40 dp, track border 2 dp, handle icon 16 dp: [Material Web switch tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-switch.scss).

Rule: track height equals the smaller of 32 dp and the control height of the density level; track width is 52/32 of the height; the handle sizes, the handle icon, the border and the state layer scale by the same factor `s = track height / 32`, rounded to whole dp at scale 1.0. Control heights come from [[Spacing and Density]] ([[ADR-0002 Desktop density levels and target sizes]]).

| Level | Control (row) height | Track | Handle off, on, pressed | State layer | Label gap to track |
|---|---|---|---|---|---|
| default | 40 dp | 52 by 32 dp | 16, 24, 28 dp | 40 dp | 8 dp |
| compact | 32 dp | 52 by 32 dp | 16, 24, 28 dp | 32 dp | 8 dp |
| dense | 28 dp | 46 by 28 dp | 14, 21, 24 dp | 28 dp | 4 dp |

The compact and dense rows are Tesserae design choices #needs-verification-as-design-choice (MD3 gives one size). Compact keeps the MD3 track because the track height equals the 32 dp control height.

- Pointer target: the track and label together; at least 24 dp by 24 dp ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)); in touch contexts the hit area extends to 48 dp high, centred on the track, beyond the visual track and without overlapping a neighbouring control's hit area.
- Row horizontal padding and gaps follow [[Spacing and Density]].

## Layout and overflow

- The track keeps its size; it never shrinks, wraps or clips. The label may wrap (at most 2 lines) or truncate with an ellipsis; the track stays visible and aligned to the first line's centre.
- Label placement: label after the track in a plain row; in a [[Form Row]] the label sits in the label column and the switch in the control column, aligned to the row's vertical centre.
- A switch paints only inside its own box plus the 40 dp state layer and the focus ring plus 2 dp offset; it draws nothing outside that region on press, release or hover (AC-SWI-5).

## Behaviour

- Pointer: press shows the pressed state (handle 28 dp); release inside the track or label toggles once; pointer leave or cancel before release cancels without toggling. Dragging the handle past the middle and releasing is optional and unspecified.
- Keyboard: Space toggles the focused switch ([WAI-ARIA Authoring Practices, Switch pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch/): Space toggles; Enter is optional). Enter does not toggle a switch in tess-shell; tess-ui toggles on Enter too: a project states which. Tab and Shift+Tab move focus in and out; a disabled switch takes no focus and no key.
- Touch: tap on the 48 dp hit area toggles.
- Event: `On_Change` (tess-ui) or `On_Changed` (tess-shell, with `old`, `new`, `value`) runs once per user toggle, after the state changes; setting the state from code raises nothing (tess-shell) and tess-ui `Selected` is two-way.

## Tooltip and overlay behaviour

Per [[ADR-0004 Tooltip rule]] the tooltip belongs to the control that carries the label or icon, never to a row or group. For a switch:

- The switch (track plus its own label, one control) may carry one tooltip; the row, the group heading and the reset button each carry their own, and hovering the switch shows only the switch's tooltip (F8).
- A press on the switch dismisses its tooltip and no tooltip returns until the pointer leaves and re-enters and 500 ms pass (F9).
- The tooltip is opaque with the inverse container ([[Tooltip]]), never plain text over the content.

## Motion

Handle slide 300 ms, colour 150 ms, handle growth 100 ms as in Tokens used. Reduced motion: the state switches at once, no slide, no growth animation ([[14 Accessibility Basics]]).

## Accessibility

- Role: `switch` with the state `checked` (true or false) ([WAI-ARIA switch](https://www.w3.org/TR/wai-aria-1.2/#switch)).
- Name: the label text; an unlabelled switch gets its name from the row's label control through an explicit association ([[Form Row]]); a switch with no name fails AC-SWI-6.
- State change announcement: the platform announces `on` and `off` from `checked`; no extra live region.
- Disabled: exposed as disabled; focus and key input suppressed by the control, since the engine flag alone does not block them (`tre:docs/guide/accessibility.md`).
- Contrast: handle against track, track against surface at least 3 to 1 in both states ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); label text at least 4.5 to 1.
- Focus: ring visible, 3 dp, not clipped by the row.

## Dark and light

All roles; the switch follows the scheme ([[Theme Following the System]]). AC-SWI-7 runs in both.

## Defaults

Density from the container; plain variant; label after the track; both `Selected` false; no tooltip unless the control sets one.

## Acceptance criteria

- [ ] AC-SWI-1: Token test. Track, handle, icon and state-layer sizes equal the table at each density (52 by 32, 16/24/28 and 40 dp at default; 52 by 32 and 32 dp at compact; 46 by 28, 14/21/24 and 28 dp at dense). Pass: all values equal.
- [ ] AC-SWI-2: Geometry check. The handle centre travels from track-height/2 to track-width minus track-height/2 and never leaves the track; the handle never overlaps the track border in the on state. Pass: handle bounds inside track bounds at every animation frame of a captured toggle.
- [ ] AC-SWI-3: Scripted input. Focus the switch, press Space: `checked` flips once and `On_Change` fires once; a second Space flips it back. On a disabled switch Space does nothing and the switch cannot take focus. Pass: state and event counts equal.
- [ ] AC-SWI-4: Scripted input. Press and release the pointer on the track toggles once; press on the track, move the pointer outside, release toggles nothing. Pass: state unchanged in the second case.
- [ ] AC-SWI-5: Pixel check (F9). Render the window before and after a pointer click on a switch (state change and tooltip dismissal included, 600 ms elapsed): every pixel that differs lies inside the union of the switch box, its 40 dp state layer and its focus ring plus offset, or inside an opaque tooltip container that is clipped to the window. Pass: zero differing pixels outside that union and zero tooltip text pixels without an opaque container behind them.
- [ ] AC-SWI-6: AT tree assertion. The node has role `switch`, a non-empty name, `checked` equal to the state, and `disabled` equal to the state. Pass: all equal.
- [ ] AC-SWI-7: Contrast script. Light and dark scheme: handle against track at least 3 to 1 in off and on; track (or its border in off) against the adjacent surface at least 3 to 1; label against surface at least 4.5 to 1. Pass: ratios at or above the limits.
- [ ] AC-SWI-8: Scripted input (F8). Hover the switch for 600 ms: exactly the switch's own tooltip (if it has one) is visible and no row or group tooltip is; hover the row's label: only the label's tooltip. Pass: visible tooltip count and owners equal.
- [ ] AC-SWI-9: Geometry check. The hit area is at least 24 dp by 24 dp at every density, and 48 dp high in the touch context. Pass: measured bounds at or above the limits.
- [ ] AC-SWI-10: Scripted input. With reduced motion on, a toggle completes the state change within one frame. Pass: handle at final position in the first frame after the event.
- [ ] AC-SWI-11: Token test. The state layer opacities resolve to the [[State Layers]] tokens and the disabled colours to 12 and 38 percent. Pass: values equal.
- [ ] AC-SWI-12: Geometry check. A switch inside a [[Form Row]] stays vertically centred on the row at every density (±0.5 dp). Pass: offset at most 0.5 dp.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`Switch`) | partly meets: 52 by 32, handles 16/24/28, role `switch` with `checked`, Space and Enter toggle, pointer cancel handled, reduced motion handled in durations (AC-SWI-1 meets at default, AC-SWI-3, AC-SWI-4, AC-SWI-6 meet by reading the code, unrun); disabled colours use 12 and 38 percent (AC-SWI-11 partly); no density scaling (AC-SWI-1 fails at compact and dense); the tooltip of the config form sits on the label box only per the 2026-11-21 bot facts, so F8 against the switch is addressed in the config form but the toolkit allows tooltips on rows (AC-SWI-8 unmeasured); F9 not reproduced in code, unmeasured (AC-SWI-5) |
| tess-shell | `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | partly meets: role SWITCH with `checked`, Space toggles, Enter does not, disabled takes no focus or key (AC-SWI-3 meets by reading); 40 by 22 dp track with a 16 dp thumb: not the MD3 or density size (AC-SWI-1 fails); state looks are opacity 0.85 hover, 0.7 pressed, 0.5 disabled literals, not State Layers (AC-SWI-11 fails; status `absent` for State Layers); no icon variant |
| tre | none (no switch primitive; composed from box and path nodes) | not applicable |

Evidence: F8, F9 in [[Owner Feedback 2026-11-20]].

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`Switch`), `tess-ui:docs/components/switches.md` | exists |
| tess-shell | `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl` | exists as Toggle |
| tess-ui (config app) | `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`SwitchWidget`) | uses the tess-ui Switch |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Track 46 by 28 dp with scaled handles at dense | dense row height 28 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| 40 dp state layer is 32 dp at compact and 28 dp at dense | the layer must not exceed the row | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard focus ring 3 dp, 2 dp offset, role `secondary` | [[Focus Ring]] rule for all controls | [[ADR-0009 State layer percentages]] |
| Enter optional for toggling | follows the WAI-ARIA Authoring Practices | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |

## Sources

- [Material Web switch tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-switch.scss): `track-width` 52 px, `track-height` 32 px, `track-outline-width` 2 px, `unselected-handle` 16 px, `selected-handle` 24 px, `pressed-handle` 28 px, `with-icon-handle` 24 px, icon 16 px, `state-layer-size` 40 px, `disabled-track-opacity` 0.12, colours `primary`, `on_primary`, `outline`, `surface_container_highest`.
- [Material Components Android Switch](https://github.com/material-components/material-components-android/blob/master/docs/components/Switch.md): thumb icon 16 dp, switch padding 16 dp.
- [WAI-ARIA Authoring Practices switch pattern](https://www.w3.org/WAI/ARIA/apg/patterns/switch/) and [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.5.8.
- Code facts: `tess-ui:src/tess_ui/controls.py`, `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl`.
- The m3.material.io switch specification page could not be fetched (script-rendered site); the values above are those of the Material Web token source.
