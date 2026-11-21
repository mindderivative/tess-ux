---
title: Motion
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, motion, tokens]
related: ["[[Colour Roles]]", "[[Scrim]]", "[[Elevation]]", "[[Theme Following the System]]", "[[14 Accessibility Basics]]", "[[Tooltip]]", "[[Dialog]]", "[[Existing Tokens]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# Motion

> [!info] Summary
> The 16 MD3 duration tokens, the seven easing curves (with the emphasized curve resolved), the spring tokens for named Expressive adoption, which duration each class of change uses, and the reduced-motion rule. Counterpart: [Material 3 easing and duration](https://m3.material.io/styles/motion/easing-and-duration/tokens-specs). Source of truth in code: see Status in code.

## Purpose

Motion explains a change (what opened, what moved) and gives state feedback. It must stay short on a desktop, never be the only carrier of information, and stop when the user asks for no animation.

## Tokens

The official page is script-rendered and could not be fetched. Values come from the published token sources [md-sys-motion v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-motion.scss) and [md-sys-motion latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-motion.scss), and from the [Android Motion guide](https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md), which agree with each other.

### Durations

| Token | ms |
|---|---|
| `short1`..`short4` | 50, 100, 150, 200 |
| `medium1`..`medium4` | 250, 300, 350, 400 |
| `long1`..`long4` | 450, 500, 550, 600 |
| `extra_long1`..`extra_long4` | 700, 800, 900, 1000 |

The sequence is short n = 50 n, medium n = 200 + 50 n, long n = 400 + 50 n, extra_long n = 600 + 100 n for n = 1 to 4.

### Easing

| Easing | cubic-bezier(x1, y1, x2, y2) | y at x = 0.25 / 0.5 / 0.75 |
|---|---|---|
| `linear` | (0, 0, 1, 1) | 0.250 / 0.500 / 0.750 |
| `standard` | (0.2, 0, 0, 1) | 0.607 / 0.878 / 0.975 |
| `standard_decelerate` | (0, 0, 0, 1) | 0.691 / 0.890 / 0.976 |
| `standard_accelerate` | (0.3, 0, 1, 1) | 0.129 / 0.372 / 0.668 |
| `emphasized` | (0.2, 0, 0, 1) as the single-curve form; the full curve is a two-segment path (see below) | 0.607 / 0.878 / 0.975 |
| `emphasized_decelerate` | (0.05, 0.7, 0.1, 1) | 0.832 / 0.950 / 0.991 |
| `emphasized_accelerate` | (0.3, 0, 0.8, 0.15) | 0.035 / 0.154 / 0.406 |

The y column was computed for this note from the control points.

Legacy curves (`legacy` (0.4, 0, 0.2, 1), `legacy_accelerate` (0.4, 0, 1, 1), `legacy_decelerate` (0, 0, 0.2, 1)) exist in the token file for older components; Tesserae does not use them.

### The emphasized curve, resolved

MD3 defines `emphasized` as a path of two Bezier segments, not a single cubic: `M 0,0 C 0.05, 0, 0.133333, 0.06, 0.166666, 0.4 C 0.208333, 0.82, 0.25, 1, 1, 1` ([Android Motion guide](https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md), `motionEasingEmphasizedInterpolator`). The CSS form cannot express a path; the Material Web token file sets `easing-emphasized` to cubic-bezier(0.2, 0, 0, 1), the same as `standard` (`$easing-emphasized: $easing-standard` in the latest token file).

Tesserae rule: `emphasized` is cubic-bezier(0.2, 0, 0, 1) in every project until an engine supports path easing, at which point the two-segment path replaces it. tess-ui has two values for the name: `tess-ui:src/tess_ui/theme.py` line 47 uses (0.2, 0, 0, 1), which equals the rule, and `tess-ui:src/tess_ui/spec/transition.py` line 36 uses (0.3, 0, 0, 1), which equals no MD3 value and is the drift to remove. The shell's `EMPHASIZED` (0.05, 0.7, 0.1, 1) is the MD3 `emphasized_decelerate` curve under the wrong name.

### Springs (named Expressive adoption only)

Spring tokens are part of the Expressive motion system. [[ADR-0006 MD3 baseline with named Expressive adoptions]] keeps the baseline duration and easing system; a project that adopts springs does so by a named entry in [[Deviations from MD3]]. Spatial springs move things and may overshoot; effects springs animate colour or opacity and do not overshoot. Values: [Android Motion guide, Springs](https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md) and the latest token file.

| Spring | Damping ratio | Stiffness |
|---|---|---|
| `fast_spatial` | 0.9 | 1400 |
| `fast_effects` | 1 | 3800 |
| `default_spatial` | 0.9 | 700 |
| `default_effects` | 1 | 1600 |
| `slow_spatial` | 0.9 | 300 |
| `slow_effects` | 1 | 800 |

Conversion of these values to the bounce parameter of an engine spring (tre: default bounce 0.2, range -1 to 1) is #needs-verification.

### Durations by class of change

| Class of change | Duration token | Easing | Source |
|---|---|---|---|
| Colour and opacity of a state change (background, border) | `short3` 150 ms | `standard` | `tess-ui:src/tess_ui/views/Button_Stylesheet.tdl` Background 150 ms |
| Shape, elevation or size change of a control | `short4` 200 ms | `standard` | Button, Fab, Card sheets: Corner_Radius and Elevation 200 ms |
| Dialog scrim fade in / out | 500 ms / 150 ms, linear | `linear` | [Material Web dialog animations](https://github.com/material-components/material-web/blob/main/dialog/internal/animations.ts) |
| Dialog open (slide 50 dp) / close | 500 ms `emphasized` / 150 ms `emphasized_accelerate` | as listed | same file |
| Screen change, fade through | 90 ms out, 210 ms in | `standard` | `tess-ui:src/tess_ui/screen_transition.py` lines 25 to 27 |
| Popup and menu open / close | 200 ms `emphasized_decelerate` / 100 ms `emphasized_accelerate` | as listed | this note, design choice #needs-verification |

### Mapping of the tess-shell motion tokens

| Shell token | Value | MD3 token of the same value |
|---|---|---|
| `$motion.duration.short` | 100 ms | `short2` |
| `$motion.duration.medium` | 200 ms | `short4` |
| `$motion.duration.long` | 400 ms | `medium4` |
| `$motion.easing.standard` | cubic-bezier(0.2, 0, 0, 1) | `standard` (equal) |
| `$motion.easing.emphasized` | cubic-bezier(0.05, 0.7, 0.1, 1) | `emphasized_decelerate`, not `emphasized` |

## Rules

1. A transition takes its duration from a duration token and its easing from an easing token. A literal ms value in a stylesheet is allowed only when it equals a token value and the allow-list in AC-MOT-6 lists it.
2. A duration is at most 1000 ms (`extra_long4`). A desktop control change is at most 200 ms; a modal open at most 500 ms.
3. Exit motion is shorter than enter motion: an element leaves with a duration at most 75 percent of its enter duration, using an accelerate easing (Tesserae choice; the Material Web dialog uses 150 ms out against 500 ms in).
4. Reduced motion. When the platform preference for reduced motion is on, or animations are off, every transition duration is 0 (the end state is drawn on the next frame), no repeating or auto-advancing animation that moves content plays (marquee, carousel advance, parallax), and no spring overshoots. A progress indicator may keep animating when the animation is the only way to show that work continues ([WCAG 2.3.3](https://www.w3.org/TR/WCAG22/#animation-from-interactions): interaction-triggered motion can be disabled unless essential). The preference is read with the scheme ([[Theme Following the System]] rule 9) and applies to the whole application.
5. Motion never carries information alone: the end state is also readable without the animation.
6. Hover delays and similar timings (tooltip 500 ms, rich tooltip grace 150 ms) are interaction timings, not motion tokens; they are owned by [[Tooltip]].
7. An animation does not block input: the element accepts the next input while animating, and a new transition replaces the running one from its current value.

## Acceptance criteria

- [ ] AC-MOT-1: Token test. The theme returns the 16 durations of the Durations table. Pass: 16 of 16 exact in ms.
- [ ] AC-MOT-2: Token test. The theme returns the 7 easings of the Easing table, and every definition of the name `emphasized` in the project (theme, transition spec, binder) equals cubic-bezier(0.2, 0, 0, 1). Pass: one value per name across all definitions.
- [ ] AC-MOT-3 (token test): Numeric test. Evaluate each easing at x = 0.25, 0.5, 0.75. Pass: results equal the y column within 0.005.
- [ ] AC-MOT-4 (pixel check): Scripted frame capture. Trigger a `short4` transition (Button Corner_Radius) at 60 Hz and capture frames. Pass: the end state appears no earlier than 200 ms and no later than 200 ms plus 2 frames (233 ms) after the trigger.
- [ ] AC-MOT-5 (scripted input): Scripted reduced motion. Set the platform stub to reduced motion and trigger a Button hover colour change, a popup open and a marquee. Pass: the Button and popup are in their end state on the next frame; the marquee offset is unchanged over 2 s.
- [ ] AC-MOT-6: Token test (static scan). No view stylesheet sets `Duration` to a literal that is not in the allow-list (values equal to a token, each listed with its token name), and no stylesheet sets an easing to a literal curve. Pass: zero hits outside the allow-list.
- [ ] AC-MOT-7 (token test): Numeric test. An effects spring (colour, opacity) never exceeds its target. Pass: the sampled value stays at or below the target (colour channel distance monotonic) for every frame; a spatial spring may exceed it by at most 10 percent of the distance.
- [ ] AC-MOT-8: Scripted input. Trigger a transition and send a second trigger after 50 ms. Pass: the second transition starts from the current value without a jump larger than 1 dp or 1 colour step.
- [ ] AC-MOT-9: Review. No element conveys state by motion alone (Rules 5). Pass: reviewer finds none.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/theme.py` (`DURATIONS`, `EASINGS`, `Theme.spring`); `tess-ui:src/tess_ui/spec/transition.py`; `tess-ui:src/tess_ui/motion.py`; `tess-ui:src/tess_ui/screen_transition.py` | Partly meets. AC-MOT-1 meets (16 durations equal the table). AC-MOT-2 fails: `emphasized` is (0.2, 0, 0, 1) in `theme.py` and (0.3, 0, 0, 1) in `spec/transition.py`. The other six easings equal the table. AC-MOT-5 meets in design: `motion.py` sets every animation duration to 0 and stops repeating animation, following the OS by default (not run here). AC-MOT-6 fails by name: stylesheets use the literals 150 and 200 ms, equal to `short3` and `short4`; Ripple timings are Material Web's own and not tokens. Springs exist (`Theme.spring(bounce)`) and are not mapped to the table. Screen transition 90 and 210 ms matches the fade-through values. |
| tess-shell | `tess-shell:src/tess_shell/binder/motion.py`; `tess-shell:src/tess_shell/model/look.py`; `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | Partly meets. 3 durations (100, 200, 400 ms) instead of 16 tokens; AC-MOT-1 does not apply in full form (values equal `short2`, `short4`, `medium4`). AC-MOT-2 fails: `EMPHASIZED` is (0.05, 0.7, 0.1, 1), the `emphasized_decelerate` curve; `STANDARD` equals the table. AC-MOT-5 meets in code: every `$motion.duration` is 0 under reduced motion and the Marquee does not scroll, from the portal preference or animations off; the theme's `Reduced_Motion { }` block is empty, so the behaviour is code, not theme. |
| tre | `tre:docs/guide/animation.md`; `tre:crates/engine-core/src/tree/scroll.rs` | Not applicable as tokens: default easing is linear, default duration 0 (snap), no named tokens; supports cubic Bezier, `spring` and a bounce parameter (default 0.2). Reduced motion is reported as a signal and is not enforced. Docs use the MD3 `standard` and `emphasized_decelerate` curves as examples. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| `emphasized` is a single cubic (0.2, 0, 0, 1) | The two-segment path cannot be expressed in the engines' easing forms; Material Web does the same | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Desktop limits on duration (control change at most 200 ms) | Pointer-driven desktop UI; MD3 durations are phone-scale | [[ADR-0002 Desktop density levels and target sizes]] |
| Springs are not in the baseline | Expressive; adopted by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-shell keeps 3 duration tokens | Shell has its own flat token set | [[ADR-0001 MD3 role names are the specification vocabulary]] |
