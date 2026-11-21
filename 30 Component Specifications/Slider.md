---
title: Slider
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, input, slider]
related: ["[[Spin Box]]", "[[Text Field]]", "[[Form Row]]", "[[Tooltip]]", "[[Switch]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Typography]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Colour Roles]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Tooltip]]"]
---

# Slider

> [!info] Summary
> A control that picks a number, or a range of two numbers, by moving a handle along a track or with the keyboard: the Material Design 3 [slider](https://m3.material.io/components/sliders/overview) (baseline 2022 form, with the Expressive sizes as a named adoption), with a value label that is the tooltip of the handle. Source of truth in code: see Status in code.

## Purpose

Adjust a value in a known range where the position matters more than the exact number: volume, brightness, zoom, a price range. The result is usually visible or audible at once.

## When to use and not

- Use when: the value is a number in a bounded range; approximate input is acceptable; the effect is seen while adjusting.
- Do not use when: the user needs an exact number (use [[Spin Box]] or [[Text Field]], optionally beside the slider); the range is unbounded; the choice is a few named options (use [[Radio Button]] or [[Segmented Button]]); the control only turns something on or off ([[Switch]]).

## Anatomy

1. Track: the full length, 4 dp thick, split at the handle into the active part (`primary`, start to handle) and the inactive part (`surface_container_highest`, handle to end).
2. Handle: a circle of 20 dp in `primary` (a 4 dp wide bar in the Expressive form).
3. State layer: a circle of 40 dp centred on the handle ([[State Layers]]).
4. Tick marks (discrete slider): a 2 dp mark at each step.
5. Stop indicator: a 4 dp dot at the end of the inactive track (Tesserae, see Deviations).
6. Value label: a 28 dp high bubble above the handle with the value; the tooltip of the handle.
7. Inset icon (Expressive, optional).
8. Focus ring: around the state layer, keyboard focus only ([[Focus Ring]]).

A range slider has two handles; the track between them is active and the parts outside are inactive.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Continuous | default | any value in the range, snapped to the key step |
| Discrete | a small set of steps | `step` set, tick marks at each step, snap on drag |
| Range | a lower and an upper value | two handles that never cross; each is its own focus stop |
| Vertical | a slider that is taller than wide (levels) | the bottom is the minimum; the same keys |
| Expressive sizes (named adoption, ADR-0006) | media and hero contexts at default density only | thicker track in pieces with a 6 dp gap, 4 dp wide handle; sizes below |

## States

State layer percentages come from [[State Layers]] (hover 8, focus 10, pressed 10, dragged 16 percent; [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). Colours from the Material Web slider tokens ([v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss) for the baseline form):

| State | Active track | Inactive track | Handle | State layer | Other |
|---|---|---|---|---|---|
| Rest | `primary` | `surface_container_highest` | `primary` | none | tick marks: over the active part `on_primary` at 38 percent, over the inactive part `on_surface_variant` at 38 percent |
| Hover | as rest | as rest | as rest | `primary` 8 percent | |
| Focus (keyboard) | as rest | as rest | as rest | `primary` 10 percent | focus ring 3 dp, offset 2 dp, role `secondary`, around the layer; the value label shows |
| Pressed and dragged | as rest | as rest | as rest | `primary` 10 percent (pressed), 16 percent (dragged) | the value label shows |
| Disabled | `on_surface` at 38 percent | `on_surface` at 12 percent | `on_surface` at 38 percent | none | no label, no focus |

The handle moves; the active track grows; the value label shows the number; a state is never carried by colour alone ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).

## Tokens used

[[Colour Roles]] (roles above), [[Shape]] (track and handle `corner-full`), [[Elevation]] (the handle has no shadow in Tesserae), [[Typography]] (`label_medium` for the value label), [[Motion]] (colour `short3` 150 ms; the handle follows the pointer without animation while dragged), [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

MD3 baseline values (Material Web v0_192 slider tokens): active and inactive track height 4 dp, handle 20 by 20 dp, state layer 40 dp, label container height 28 dp, tick mark container 2 dp; the Android slider keeps a 48 dp touch height. The latest Material Web set moves to a 16 dp track, a 4 dp handle and a 6 dp gap ([latest `_md-comp-slider.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-slider.scss)); Tesserae keeps the baseline per [[ADR-0006 MD3 baseline with named Expressive adoptions]].

Rule: the slider height (the hit band across the track) equals the control height of the level; the state layer equals that height; the track stays 4 dp; the handle is 20 dp at default and compact and 16 dp at dense.

| Level | Hit band (across) | Track | Handle | State layer | Value label height | Default length |
|---|---|---|---|---|---|---|
| default | 40 dp | 4 dp | 20 dp | 40 dp | 28 dp | 200 dp |
| compact | 32 dp | 4 dp | 20 dp | 32 dp | 28 dp | 200 dp |
| dense | 28 dp | 4 dp | 16 dp | 28 dp | 24 dp | 160 dp |

The compact and dense rows are Tesserae design choices #needs-verification-as-design-choice. The minimum length is 96 dp; the handle centre travels from half a handle to length minus half a handle.

Expressive sizes (Material Web latest tokens `_md-comp-slider-xsmall` to `-xlarge`; default density only; the compact and dense levels use the standard form):

| Size | Track thickness | Handle length across | Inset icon | Handle width | Gap handle to track |
|---|---|---|---|---|---|
| xs | 16 dp | 44 dp | none | 4 dp | 6 dp |
| s | 24 dp | 44 dp | none | 4 dp | 6 dp |
| m | 40 dp | 44 dp | 24 dp | 4 dp | 6 dp |
| l | 56 dp | 68 dp | 24 dp | 4 dp | 6 dp |
| xl | 96 dp | 108 dp | 32 dp | 4 dp | 6 dp |

- Pointer target: the hit band across and the full length along, at least 24 dp across ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum), the 28 dp dense band meets it); 48 dp across in touch contexts. The handle is inside the band; a press outside the handle but inside the band sets the value.
- Adjacent sliders in a column do not overlap hit bands.

## Dimensions and defaults

Baseline form (Material Web v0_192 slider tokens, [[ADR-0006 MD3 baseline with named Expressive adoptions]]); the Expressive sizes keep their own table in Sizing and density. Compact and dense are Tesserae choices (#needs-verification-as-design-choice).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| slider | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]] (the hit band across the track) | tess-ui: yes (style width, height or widget option width, height); tess-shell: yes (Height on the call); tre: yes (height) |
| slider | min width | - | 96 | 96 | 96 | [[Slider]], Sizing and density (minimum length; default length 200, 200, 160) | tess-ui: yes (style width, height or widget option width, height); tess-shell: yes (Min_Width); tre: yes (min_width) |
| slider | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style width, height or widget option width, height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| slider | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | design choice, [[ADR-0002 Desktop density levels and target sizes]] (the track and handle are centred in the band) | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| slider | margin | - | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| slider | gap | `space.0` | 0 | 0 | 0 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss) (no gap between handle and track in the baseline; the Expressive form has 6) | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| slider | border width | - | 0 | 0 | 0 | [[Spacing and Density]], the slider draws no border; the focus ring is separate | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| slider | border color | - | N/A: the slider draws no border | N/A: the slider draws no border | N/A: the slider draws no border | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss) | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| slider | corner radius | - | N/A: the slider has no container; parts have their own | N/A: the slider has no container; parts have their own | N/A: the slider has no container; parts have their own | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss) | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| slider | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| slider | icon size | - | N/A: the baseline slider carries no icon (Expressive m and l 24, xl 32) | N/A: the standard form carries no icon | N/A: the standard form carries no icon | [md-comp-slider latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-slider.scss) | tess-ui: via widget option icon (size from Slider.SIZES); tess-shell: n/a: element absent in tess-shell (no icon on the track); tre: yes (width, height of the svg node) |
| track | height | - | 4 | 4 | 4 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss) (active and inactive); compact and dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: no hook (Slider.TRACK, and the widget option size picks Expressive tracks only); tess-shell: via module override (Height: 4 in Slider_Module.tdl); tre: yes (height) |
| track | corner radius | `shape.full` | 2 | 2 | 2 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss) (half of the track) | tess-ui: no hook (half of the track in controls.py); tess-shell: yes (Corner_Radius on the Slider::track Rectangle); tre: yes (corner_radius) |
| track (Expressive xs to xl) | height | - | 16 to 96 | N/A: Expressive sizes apply at default density only | N/A: Expressive sizes apply at default density only | [md-comp-slider latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-slider.scss) | tess-ui: via widget option size (xs to xl, Slider.SIZES); tess-shell: n/a: element absent in tess-shell (no Expressive sizes); tre: yes (height) |
| handle | height | - | 20 | 20 | 16 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: no hook (Slider.HANDLE); tess-shell: via module override (Diameter: 16 in Slider_Module.tdl); tre: yes (height) |
| handle | corner radius | `shape.full` | 10 | 10 | 8 | [[Shape]] (half of the handle) | tess-ui: no hook (half of Slider.HANDLE); tess-shell: n/a: a Circle part has no corner radius, it follows its Diameter; tre: yes (corner_radius) |
| handle | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] (the MD3 baseline handle is level 1; Tesserae draws no handle shadow, see Tokens used) | tess-ui: no hook (handle is a Python-drawn node with no elevation option); tess-shell: n/a: Elevation is not a key of a Circle part; tre: yes (shadows) |
| tick mark | height | - | 2 | 2 | 2 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss) | tess-ui: no hook (drawn in controls.py with a fixed size); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| stop indicator | height | - | 4 | 4 | 4 | [[Slider]], Anatomy; design choice, proposed ADR: slider stop indicator | tess-ui: no hook (drawn in controls.py with a fixed size); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| state layer | height | `density.control_height` | 40 | 32 | 28 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss); compact and dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: no hook (STATE_LAYER_SIZE 40 in controls.py); tess-shell: no hook (no state layer in the key table); tre: yes (height) |
| state layer | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]] (half of the layer) | tess-ui: no hook (STATE_LAYER_SIZE 40 in controls.py); tess-shell: no hook (no state layer in the key table); tre: yes (corner_radius) |
| value label | height | - | 28 | 28 | 24 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: no hook (bubble drawn in controls.py with fixed size, radius 14 and font); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| value label | padding | `space.3` | 0 8 0 8 | 0 8 0 8 | 0 8 0 8 | [[Spacing and Density]], design choice, proposed ADR: slider value label padding | tess-ui: no hook (bubble drawn in controls.py with fixed size, radius 14 and font); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| value label | corner radius | `shape.full` | 14 | 14 | 12 | [[Shape]]; design choice, proposed ADR: slider value label padding (the tokens set no label shape) | tess-ui: no hook (bubble drawn in controls.py with fixed size, radius 14 and font); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| value label | font | `label_medium` | 12/16/500/0.5 | 12/16/500/0.5 | 12/16/500/0.5 | [md-comp-slider v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss), [[Typography]] | tess-ui: no hook (bubble drawn in controls.py with fixed size, radius 14 and font); tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |

## Layout and overflow

- The track and handle never shrink below the minimum length; a slider in a flexible row takes the room it is given (minimum 96 dp, then the row scrolls or wraps per [[10 Layout Overflow and Scrolling]]).
- Label placement: the name sits before the slider in a [[Form Row]] label column; a current-value readout may sit after the slider and must not rely on the value label.
- The track is vertically centred in the hit band; the handle is centred on the track.
- The value label is clipped to the window only, never to the slider; it flips below the handle when there is no room above (within 4 dp of the window top).
- A slider paints only inside its band, the state layer, the focus ring and its value label.

## Behaviour

- Pointer: a press on the track or handle sets the value to the pointer position (snapped to the step) and begins a drag; the handle follows while the pointer moves, with the pointer captured so a drag may leave the slider; release ends the drag. A press on the handle itself does not move it by the press offset. The mouse wheel over a slider scrolls the container and never changes the value.
- Keyboard ([WAI-ARIA Authoring Practices slider](https://www.w3.org/WAI/ARIA/apg/patterns/slider/), verified 2026-11-21): the slider takes focus on its handle (a range slider has two focus stops, lower then upper).
  - Right Arrow and Up Arrow increase by one step; Left Arrow and Down Arrow decrease by one step, in both orientations.
  - Page Up increases and Page Down decreases by ten steps (APG: optional, "an amount larger than the step").
  - Home sets the first allowed value; End sets the last. In a range slider, Home and End go to the end of what the handle may reach (the other handle's value).
  - A key with Ctrl, Alt or Meta is not the slider's.
  - A key at an end that cannot move the value changes nothing and fires nothing.
  - The step of a continuous slider (no `step`) is one hundredth of the range, so Page Up moves 10 percent of the range #needs-verification as MD3 value (Material Web uses the native range input).
  - In right-to-left locales a horizontal slider increases leftwards and Left Arrow increases; Up and Down are unchanged (APG leaves reversal optional).
- Touch: touch-drag on the 48 dp band behaves like a pointer drag.
- Events: an input event for every value change while a drag is going and for each key; a change event once when a drag ends with a value different from its start and after each key. Setting the value from code raises no event.
- Assistive technology: increment, decrement and set-value actions change the value by the key step.

## Tooltip and overlay behaviour

The only overlay of a slider is its value label, and it belongs to the handle ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]); Material Components Android implements the value label as a tooltip ([Slider docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Slider.md)).

- Content: the formatted value; a range slider shows one label per handle while that handle is pressed or focused.
- Shows: while the handle is pressed or dragged; on keyboard focus and after each key change; after 500 ms of pointer hover on the handle (not on the track). It never shows for a hover on the track, the row or the label.
- Hides: on release of the pointer (after the drag ends), on blur, on Escape (without moving focus), when the window loses focus, and when the pointer leaves the handle while neither pressed nor focused (150 ms grace, ADR-0011).
- Appearance: 28 dp high, `primary` container, text `on_primary` in `label_medium`, opaque, 8 dp above the handle's upper edge #needs-verification (the gap is a tess-ui value; the baseline tokens give none).
- The slider's name and any descriptive tooltip belong to the label control in the [[Form Row]], not to the track.

## Motion

Handle position follows the pointer in the same frame (no easing while dragged). Key steps move the handle in one frame. Colour changes fade `short3` 150 ms. The value label fades in and out `short2` 100 ms. Reduced motion: no fades; the state changes in one frame ([[14 Accessibility Basics]]).

## Accessibility

- Role: `slider` with `value`, `value_min`, `value_max`, `value_step` ([WAI-ARIA slider](https://www.w3.org/TR/wai-aria-1.2/#slider)); orientation vertical for a vertical slider.
- Name: the visible label; a range slider's handles are named "{label}, minimum" and "{label}, maximum" (tess-ui).
- Value text: when the number needs units or words ("45 percent", "1:23 of 3:45"), the slider sets the value text; without it the number is read.
- Actions: increment, decrement and set-value are offered (the engine derives them from role and value range, `tre:docs/reference/node.md`).
- Disabled: exposed as disabled; no focus, no key.
- Contrast: handle against the surface at least 3 to 1; active track against the surface at least 3 to 1; the inactive part is identified by the stop indicator (`on_surface_variant` against the surface at least 3 to 1) because `surface_container_highest` against the surface does not reach 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); value label text against its container at least 4.5 to 1.
- Focus ring visible, not clipped.

## Dark and light

All roles; follows the scheme ([[Theme Following the System]]). AC-SLD-11 runs in both.

## Defaults

Continuous, horizontal, 0 to 1 in tess-ui and 0 to 100 in tess-shell, length 200 dp, density from the container, no value label, no ticks, no icon; key step one hundredth of the range (continuous) or `step`.

## Acceptance criteria

- [ ] AC-SLD-1 (token test): track thickness, handle, state layer and label height equal the table at each level (4, 20, 40, 28 dp at default; 4, 20, 32, 28 at compact; 4, 16, 28, 24 at dense) and the Expressive sizes equal the size table. Pass: all values equal.
- [ ] AC-SLD-2 (geometry check): the hit band across is 40, 32 and 28 dp at the three levels (at least 48 dp in the touch context) and at least 24 dp always; adjacent sliders' bands do not overlap. Pass: measured bounds at or above the limits.
- [ ] AC-SLD-3 (geometry check): the handle centre is at half a handle from the start at the minimum and at length minus half a handle at the maximum; the active track ends at the handle centre; vertical: the minimum is at the bottom. Pass: positions equal within 0.5 dp.
- [ ] AC-SLD-4 (scripted input): Right, Up, Left, Down change the value by one step; Page Up and Page Down by ten steps; Home and End set minimum and maximum; at an end the same key fires no event; Ctrl+Right changes nothing. Pass: value sequence and event counts equal.
- [ ] AC-SLD-5 (scripted input): press on the track at 25, 50 and 100 percent sets the value there (snapped); drag with the pointer leaving the slider keeps following; release fires exactly one change event if the value differs from the start; the input event count equals the number of distinct values passed. Pass: values and counts equal.
- [ ] AC-SLD-6 (scripted input): a discrete slider with step 5 from 0 to 20 snaps a drag to 0, 5, 10, 15 or 20 and shows 5 tick marks. Pass: values and mark count equal.
- [ ] AC-SLD-7 (scripted input): in a range slider the handles never cross (drag the lower past the upper: it stops at the upper), Tab visits lower then upper, End on the lower handle sets it to the upper's value. Pass: values and focus order equal.
- [ ] AC-SLD-8 (scripted input): the mouse wheel over the slider does not change the value. Pass: value unchanged and the scroll event reaches the container.
- [ ] AC-SLD-9 (scripted input): the value label is visible while the handle is pressed, while it has keyboard focus and 500 ms after hover on the handle; it is not visible after hover on the track for 1000 ms or hover on the row label; it hides on blur and on Escape; exactly one slider tooltip is visible at a time. Pass: visible label count and owner equal at each time.
- [ ] AC-SLD-10 (pixel check): the value label is opaque (container pixels, no transparent pixels under its text), `primary` container with `on_primary` text, 28 dp high at default, and fully inside the window (flips below the handle at the top edge); the focused slider's ring is not clipped. Pass: pixels equal within 1 per 8-bit channel; ring pixels 100 percent visible.
- [ ] AC-SLD-11 (contrast script): light and dark, handle and active track against the surface at least 3 to 1, stop indicator against the surface at least 3 to 1, value label text against the label container at least 4.5 to 1. Pass: ratios at or above the limits.
- [ ] AC-SLD-12 (AT tree assertion): the node has role `slider`, a non-empty name, `value`, `value_min`, `value_max`, `value_step` equal to the state, `disabled` equal to the state; a slider with a value text exposes it; each range handle has its own node named "{label}, minimum" and "{label}, maximum". Pass: all equal.
- [ ] AC-SLD-13 (scripted input): the assistive actions increment, decrement and set-value change the value by the key step or to the given value and fire the same events as keys. Pass: values and counts equal.
- [ ] AC-SLD-14 (token test): state layer opacities 0.08, 0.10, 0.10 and 0.16 (dragged); disabled active track and handle 0.38, inactive track 0.12. Pass: values equal.
- [ ] AC-SLD-15 (scripted input): with reduced motion on, a key step moves the handle and colour in the first frame. Pass: handle at the final position in that frame.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`Slider`, `RangeSlider`), `tess-ui:docs/components/sliders.md` | partly meets: 4 dp track, 20 dp handle, 40 dp layer in a 48 dp target, `primary` and `surface_container_highest`, ticks, drag capture, press sets value, arrows (all four), Page by ten steps, Home, End, assistive increment, decrement, set-value, vertical, range with separate focus stops and names, dragged layer 16 percent, disabled 38 and 12 percent (AC-SLD-3 to AC-SLD-7, AC-SLD-12 to AC-SLD-14 meet by reading, unrun). Fails: no density (AC-SLD-1, AC-SLD-2 at compact and dense; fixed 48 dp target); the value label (`Value_Indicator`) is `inverse_surface` with `inverse_on_surface`, not `primary` and `on_primary`, shows on drag or key focus but not on handle hover (AC-SLD-9, AC-SLD-10); no stop indicator (AC-SLD-11 unmeasured); Expressive sizes written "from memory, not checked" in code (#250): the medium handle is 52 dp, the token value is 44 dp, and size `s` has a 16 dp inset icon where the tokens give none below `m` (AC-SLD-1); no right-to-left reversal (AC-SLD-4 in RTL); the mouse wheel behaviour is not read (AC-SLD-8 unmeasured); no value text property in the TDL view (AC-SLD-12); settable: track, handle, tick, state layer and value bubble sizes are class constants and literals in `controls.py`, with no style or token hook |
| tess-shell | `tess-shell:src/tess_shell/shipped/Slider/Slider_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | partly meets: role `SLIDER` with `value`, `value_min`, `value_max`, `value_step`, `Value_Text`, `Label`; Left and Down decrease, Right and Up increase, Page by ten steps, Home and End, Ctrl, Alt or Meta ignored, no event at an end, pointer capture, press jumps (AC-SLD-4, AC-SLD-5, AC-SLD-12 meet by reading). Fails: 160 by 20 dp, hit band 20 dp, below the density and 24 dp rules (AC-SLD-1, AC-SLD-2); handle 16 dp with a 2 dp `surface` ring, track 4 dp `outline`, no `surface_container_highest` (AC-SLD-1, AC-SLD-14); no state layer: handle border changes, disabled 0.5 literal (AC-SLD-14); no value label, no ticks, no range (AC-SLD-6, AC-SLD-7, AC-SLD-9); no focus-ring spec match; settable: track and handle sizes are literals in `Slider_Module.tdl` (a same-named module file overrides them); the state layer has no hook (absent) |
| tre | `tre:docs/reference/node.md` (`role="slider"`, `value`, `value_min`, `value_max`, `value_step`, `value_text`) | not applicable: the engine has the role and the value properties and offers increment, decrement and set-value to assistive technology; no vertical orientation property for AT (candidate request: orientation) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Hit band 40, 32, 28 dp; handle 16 dp and label 24 dp at dense | desktop rows | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Expressive sizes xs to xl adopted (track in pieces with 6 dp gap, 4 dp handle), default density only | tess-ui ships them; named adoption | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| 4 dp stop indicator at the inactive end in `on_surface_variant` | the inactive track `surface_container_highest` is below 3 to 1 against the surface; WCAG 1.4.11 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (accessibility rule; Material Components Android adds a 4 dp stop indicator for the same reason) |
| Value label is the handle's tooltip, shown on hover after 500 ms as well as on press and focus | tooltip belongs to the control; keyboard users see it on focus | [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Wheel does not change the value | a wheel over a slider in a scrolling panel changes a value by accident | [[ADR-0002 Desktop density levels and target sizes]] (desktop use) |
| Focus layer and pressed layer 10 percent; ring 3 dp, offset 2 dp | foundation rule | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |

## Sources

- [Material Web slider tokens, v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-slider.scss): active and inactive track height 4 px, handle 20 by 20 px, state layer 40 px, label container 28 px, `label-container-color` `primary`, `label-label-text-color` `on_primary`, `inactive-track-color` `surface_container_highest`, disabled opacities 0.38 and 0.12, tick mark size 2 px (verified 2026-11-21).
- [Material Web slider tokens, latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-slider.scss) and the size sets `_md-comp-slider-xsmall.scss`, `-small`, `-medium`, `-large`, `-xlarge`: track heights 16, 24, 40, 56, 96 px; handle heights 44, 44, 44, 68, 108 px; handle width 4 px; handle padding 6 px; stop indicator 4 px; icon 24 px (medium and large) and 32 px (xlarge) (verified).
- [Material Web slider docs](https://github.com/material-components/material-web/blob/main/docs/components/slider.md): continuous, discrete with ticks, range, value label shown when the handle is selected.
- [Material Components Android Slider](https://github.com/material-components/material-components-android/blob/master/docs/components/Slider.md): value label is a tooltip, label behaviour, thumb to track gap 6 dp, stop indicator 4 dp.
- [WAI-ARIA Authoring Practices slider pattern](https://www.w3.org/WAI/ARIA/apg/patterns/slider/): arrows, Home, End, Page Up and Page Down keys, focus on the thumb (verified 2026-11-21).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.5.8.
- The m3.material.io sliders page could not be fetched (script-rendered site).
- Code: `tess-ui:src/tess_ui/controls.py`, `tess-ui:docs/components/sliders.md`, `tess-shell:src/tess_shell/shipped/Slider/Slider_Module.tdl`, `shell-vault:50 Design System/Standard Modules.md` (Slider), `tre:docs/reference/node.md`.
