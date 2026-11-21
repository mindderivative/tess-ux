---
title: State Layers
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, state, interaction, tokens]
related: ["[[Focus Ring]]", "[[Colour Roles]]", "[[Motion]]", "[[Shape]]", "[[Scrim]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[Existing Tokens]]", "[[Button]]", "[[Icon Button]]", "[[Switch]]", "[[List Item]]", "[[Tree Node]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]"]
depends_on: ["[[ADR-0009 State layer percentages]]", "[[Colour Roles]]"]
---

# State Layers

> [!info] Summary
> The opacities that show hover, focus, pressed and dragged states, the disabled scheme and the ripple timings, taken from Material Design 3 (MD3) and its Material Web reference implementation. The focus indicator itself is in [[Focus Ring]].

Decision: [[ADR-0009 State layer percentages]]. The percentages are a specification rule for every project; whether a project has adopted them is a status in the tables below, not a promise.

## What a state layer is

A state layer is a rectangle (or circle, for icon-sized controls) over the container of a control, in the content colour of the control, drawn at a fixed opacity while a state holds. The layer follows the shape of the control ([[Shape]]). It does not change the content colour and does not add elevation.

Result colour of a pixel in the layer: `container * (1 - a) + layer_colour * a`, with `a` the opacity of the state.

## Opacities

| State | Opacity | MD3 value | Token (Material Web) |
|---|---|---|---|
| Hover (pointer over the control) | 8 percent (0.08) | 8 | `md.sys.state.hover.state-layer-opacity` |
| Focus (keyboard focus) | 10 percent (0.10) | 10 (the earlier published value was 12, see note) | `md.sys.state.focus.state-layer-opacity` |
| Pressed (pointer or key held) | 10 percent (0.10) | 10 (earlier 12) | `md.sys.state.pressed.state-layer-opacity` |
| Dragged | 16 percent (0.16) | 16 | `md.sys.state.dragged.state-layer-opacity` |
| Disabled content (label, icon, text) | 38 percent (0.38) | 38 | `md.sys.state.disabled.state-layer-opacity` and `md.comp.*.disabled.label-text.opacity` |
| Disabled container | 12 percent (0.12) | 12 | `md.comp.filled-button.disabled.container.opacity` |

Note on 10 versus 12: Material Web `tokens/versions/v0_192` carries focus 0.12 and pressed 0.12; `tokens/versions/latest` carries 0.10 and 0.10. Tesserae adopts the latest values (10). Both are verified at the URLs below.

### Layer colour

The layer colour is the content colour of the component: `on_surface` on a surface or text-style control, `on_primary` on a filled primary button, `on_secondary_container` on a tonal control, `primary` on selected text controls. The control's note lists the role per part ([[Colour Roles]]). A control with no stated layer colour uses `on_surface`.

### Which layer shows

Only one layer shows at a time. Precedence, highest first: dragged (16), pressed (10), focused (10), hovered (8). The precedence is a Tesserae rule; MD3 does not state one #needs-verification. tess-ui draws dragged, else focused, else hovered, and shows pressed through the ripple (`tess-ui:src/tess_ui/interaction.py` lines 116 to 122).

### Focus layer versus focus ring

Keyboard focus draws both the 10 percent layer and the ring ([[Focus Ring]]). Pointer focus (a mouse click that moves focus) draws neither, except in text inputs ([[Focus Ring]]).

## Disabled scheme

| Part | Rule |
|---|---|
| Content (label, icon, value) | `on_surface` at 38 percent opacity |
| Container | `on_surface` at 12 percent opacity where the enabled control has a filled container; no container where it has none (text and outlined controls keep their outline at 12 percent `on_surface`) |
| State layers | none: a disabled control shows no hover, focus, pressed or dragged layer and no ripple |
| Pointer | the control does not activate |
| Contrast | exempt from the 4.5 to 1 text rule (WCAG 2.2 SC 1.4.3 exempts inactive components); the disabled state must not be the only carrier of information |

The 0.5 opacity the shell applies to disabled widgets is a deviation (see Status in code). Disabled in the accessibility tree: the node is exposed with the disabled flag ([[14 Accessibility Basics]]).

## Ripple

The ripple is the pressed feedback of tess-ui and follows the Material Web `md-ripple`. Timings:

| Part | Value | Source constant |
|---|---|---|
| Hover layer fade | 15 ms, linear | `transition: opacity 15ms linear` in `_ripple.scss` |
| Press grow | 450 ms | `PRESS_GROW_MS` in `ripple.ts` |
| Press fade-in | 105 ms | `transition-duration: 105ms` in `_ripple.scss` |
| Minimum press duration | 225 ms | `MINIMUM_PRESS_MS` |
| Release fade-out | 375 ms, linear | `transition: opacity 375ms linear` |
| Initial origin scale | 0.2 of the larger side | `INITIAL_ORIGIN_SCALE` |
| Touch delay (touch input only) | 150 ms | `TOUCH_DELAY_MS` |
| Ripple opacity (end of grow) | the pressed opacity, 10 percent | `pressed-opacity` token |

tess-ui matches these values: hover 15 ms, grow 450, fade-in 105, minimum 225, release 375 (`tess-ui:src/tess_ui/interaction.py` lines 45 to 50, `tess-ui:src/tess_ui/ripple.py` lines 26 to 31). The constants are defined twice in tess-ui; one definition is required ([[Gaps and Contradictions]]).

Rules:
- The ripple is clipped to the control's shape and never paints outside the control.
- Reduced motion (the user's platform setting): no ripple grow and no fade durations; the state layer changes colour in one frame. This is a Tesserae rule; Material Web hides the ripple only in forced-colours mode #needs-verification as MD3 guidance.
- The ripple is optional per project (`App(ripple="shader")` in tess-ui is a renderer option with no MD3 counterpart); a project without a ripple draws the pressed state layer at 10 percent instead.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/interaction.py` (HOVERED 0.08, FOCUSED 0.10, PRESSED 0.10, DRAGGED 0.16), `tess-ui:src/tess_ui/controls.py` (DISABLED_CONTENT 0.38, DISABLED_CONTAINER 0.12) | meets AC-STL-1, AC-STL-2, AC-STL-3, AC-STL-5 by constants. AC-STL-4 (single layer precedence) meets for plain nodes, not verified for the MD3 controls. The layer and ripple apply to `Rect` and `Container` among plain nodes; other controls draw their own (`tess-ui:docs/guide/interaction.md`, "Not yet covered") |
| tess-shell | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | absent. States change Background, Border_Color or Opacity: Toggle and Checkbox hovered 0.85 and pressed 0.7, disabled 0.5 on all widgets, Button hover changes Border_Color. Fails AC-STL-1 to AC-STL-3 and AC-STL-5. Adoption is a gap, not a promise ([[ADR-0009 State layer percentages]]) |
| tre | `tre:docs/guide/painting.md` | not applicable: the engine paints no state layers; it supplies a ripple recipe (`tre:examples/ripple.py`) and `focus_visible` |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Focus and pressed use 10 percent (the latest MD3 tokens), not the 12 percent of older tokens | follows the current published tokens | [[ADR-0009 State layer percentages]] |
| One layer at a time, with precedence | avoids stacked opacity that changes contrast unpredictably | [[ADR-0009 State layer percentages]] |
| Reduced motion removes the ripple | accessibility | [[ADR-0009 State layer percentages]] |

## Acceptance criteria

- [ ] AC-STL-1 (token test): the state tokens are hover 0.08, focus 0.10, pressed 0.10, dragged 0.16, disabled content 0.38 and disabled container 0.12. Pass: the project's constants equal these values exactly.
- [ ] AC-STL-2 (pixel check): for a control of known container colour and content colour, the composited pixel in hover equals `container * 0.92 + content * 0.08` with a tolerance of 1 per 8-bit channel; the same for focus and pressed at 0.10 and dragged at 0.16 (after any ripple or fade has ended).
- [ ] AC-STL-3 (scripted input): moving the pointer over the control shows the hover layer within 15 ms of the layer animation start and removes it on leave; no layer remains after the pointer leaves.
- [ ] AC-STL-4 (pixel check): when hover and focus hold together, the layer opacity is 0.10 (focus), not 0.18; when pressed and focus hold, 0.10; when dragged and any other hold, 0.16.
- [ ] AC-STL-5 (pixel check): a disabled control's content pixels equal `on_surface` at 0.38 over the container; a filled disabled container equals `on_surface` at 0.12 over the surface; hover, press and focus produce no change on a disabled control.
- [ ] AC-STL-6 (scripted input): press on a control with a ripple: the grow runs 450 ms, fade-in 105 ms, the ripple stays at least 225 ms after press, release fades in 375 ms (timestamps from a frame log, tolerance one frame at 60 Hz).
- [ ] AC-STL-7 (scripted input): with reduced motion on, press shows the pressed layer at 0.10 in the next frame and no ripple geometry grows.
- [ ] AC-STL-8 (geometry check): the layer and the ripple stay inside the control shape: no painted pixel of the layer lies outside the control's border box with its corner radius.
- [ ] AC-STL-9 (AT tree assertion): a disabled control has the disabled flag in the accessibility tree and rejects activation.

## Sources

- State layer opacities (hover 0.08, focus 0.10, pressed 0.10, dragged 0.16, disabled 0.38): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-state.scss (verified 2026-11-21). Older values (focus 0.12, pressed 0.12): https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-state.scss.
- Disabled container 0.12 and label 0.38 and icon 0.38: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filled-button.scss.
- Ripple timings: https://github.com/material-components/material-web/blob/main/ripple/internal/ripple.ts and https://github.com/material-components/material-web/blob/main/ripple/internal/_ripple.scss (verified).
- MD3 states page: https://m3.material.io/foundations/interaction/states is a JavaScript app that tools cannot read; the numbers above come from the token repository.
- WCAG 2.2 SC 1.4.3 inactive component exemption #needs-verification (quoted from the Success Criterion text, not opened).
- tess-ui values: [[Existing Tokens]].
