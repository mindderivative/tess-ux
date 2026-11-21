---
title: 06 Motion Rules
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, motion, animation, reduced-motion]
related: ["[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Elevation]]", "[[Scrim]]", "[[Theme Following the System]]", "[[14 Accessibility Basics]]", "[[12 Overlays]]", "[[02 Colour and Theming]]", "[[Tooltip]]", "[[Dialog]]", "[[Menu]]", "[[Popup]]", "[[Switch]]", "[[Scrollbar and Scroll Container]]", "[[Accordion]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[Deviations from MD3]]"]
depends_on: ["[[Motion]]", "[[14 Accessibility Basics]]"]
---

# 06 Motion Rules

> [!info] Summary
> Chapter-level principles for when to animate, how long, and what happens under reduced motion. The 16 duration tokens, the easing curves and the duration per class of change live in [[Motion]]; this chapter links and copies no value. Material Design 3 baseline: [motion](https://m3.material.io/styles/motion/overview).

## Purpose

Motion explains a change and confirms an action. On a desktop where the pointer is already at the target, long motion is delay. The chapter keeps motion short, tokenised, interruptible and removable.

## Scope

- In scope: which changes animate, which do not, tokens per class, interruption, exit versus enter, reduced motion, motion that never carries information alone.
- Out of scope: duration and easing values ([[Motion]]), ripple timings ([[State Layers]]), hover delays of tooltips ([[Tooltip]]).

## Principles

1. Animate only to explain. A change animates when the user would otherwise lose track of it: an overlay opening from its opener, an accordion expanding, a switch moving. A change that the user caused and sees at once (typing, selection by key, a scroll) does not animate beyond the engine's own scroll behaviour.
2. Tokens, not numbers. Each animation takes a duration token and an easing token of [[Motion]]. A literal that equals a token is allowed only on the allow-list of [[Motion]] AC-MOT-6.
3. Short on desktop. A control state change takes at most the `short3` to `short4` tokens; a modal opens in at most 500 ms; nothing exceeds 1000 ms ([[Motion]] rule 2, [[ADR-0002 Desktop density levels and target sizes]]).
4. Exit is faster than enter, at most 75 percent of the enter duration, with an accelerate easing ([[Motion]] rule 3).
5. Never block. An element accepts the next input while it animates; a new transition replaces the running one from its current value ([[Motion]] rule 7).
6. Never alone. Motion is not the only carrier of a state; the end state is readable without the animation ([[Motion]] rule 5, [[14 Accessibility Basics]]).
7. Reduced motion removes motion, not feedback. With the platform preference on, durations are 0, no repeating or auto-advancing motion plays, no spring overshoots, and the end state shows on the next frame; state layers and the focus ring still appear ([[Motion]] rule 4, [[State Layers]]).
8. The user setting is read once for the whole application, with the scheme ([[Theme Following the System]]); a change applies to running animations without a restart.
9. Baseline first. Springs and spatial overshoot are Expressive; they enter only through a named deviation ([[ADR-0006 MD3 baseline with named Expressive adoptions]]).

## What animates and what does not

| Change | Animates | Token class (see [[Motion]]) | Reduced motion |
|---|---|---|---|
| Hover, press, focus layer on a control | yes, a fade | state colour, `short3` | next frame |
| Ripple on press | yes | ripple timings of [[State Layers]] | no ripple, pressed layer in one frame |
| Control shape or elevation change | yes | `short4` | next frame |
| Switch handle move | yes | `short3` to `short4` per [[Switch]] | next frame |
| Menu and popup open and close | yes, fade and scale from the opener | open 200 ms, close 100 ms | next frame |
| Dialog open and close, scrim | yes | per [[Motion]] (dialog and scrim rows) | next frame |
| Tooltip appear | fade, after the hover delay owned by [[Tooltip]] | `short2` #needs-verification | next frame; the delay stays |
| Accordion expand and collapse | yes, height | `short4` to `medium1` per [[Accordion]] #needs-verification | next frame |
| Screen or view change | fade through | per [[Motion]] | cut |
| Focus ring | no: drawn in the first frame | none ([[Focus Ring]]) | unchanged |
| Scroll position by wheel or key | engine scroll behaviour; smooth scroll uses `short4` at most | | immediate |
| Text caret blink | no; caret stays visible | none | none |
| Progress indicator | yes (essential) | indeterminate loop | may keep animating when it is the only sign of work |
| Marquee, carousel advance, parallax | not used on desktop controls | | never plays |
| Typing, selection, list reorder by keyboard | no | | |

## Interruption and consistency

- Starting a transition during another of the same property continues from the current value (AC-MOT-8).
- Close during open reverses from the current value; it does not jump to the start.
- Two elements of one class use the same token (every menu opens with the same duration).
- A transition that changes layout does not change the hit area during the animation by more than the final change.

## Where each rule lives

| Topic | Note |
|---|---|
| Durations, easings, springs, class of change | [[Motion]] |
| Ripple, state layer timings | [[State Layers]] |
| Reduced motion signal, scheme | [[Theme Following the System]], [[14 Accessibility Basics]] |
| Overlay open and close | [[12 Overlays]] |
| Hover delay | [[Tooltip]] |

## Acceptance criteria

The criteria AC-MOT-1 to AC-MOT-9 are defined in [[Motion]].

- [ ] AC-C06-1 (token test): every animation named in a component note of `30 Component Specifications` names a duration token of [[Motion]] (`short1` to `extra_long4`) or a ripple timing of [[State Layers]]. Pass: a script over the notes finds zero animations with a literal ms value and zero without a token.
- [ ] AC-C06-2 (token test): every animation in the specification has a duration of at most 1000 ms, every control state change at most 200 ms and every modal open at most 500 ms. Pass: zero durations above these limits.
- [ ] AC-C06-3 (token test): for each pair of enter and exit durations named in a component note, exit is at most 75 percent of enter. Pass: zero pairs above 75 percent.
- [ ] AC-C06-4 (scripted input): with reduced motion on, every row of the animates table marked "next frame" reaches its end state in the next frame (frame 1), and the marquee, carousel and parallax offsets stay unchanged over 2 s. Pass: all rows.
- [ ] AC-C06-5 (scripted input): with reduced motion on, hover, focus and press still show the layer opacities of [[State Layers]] (0.08, 0.10, 0.10) and the focus ring appears. Pass: pixel values equal.
- [ ] AC-C06-6 (scripted input): a close command sent 50 ms into a dialog or menu open reverses from the current opacity with a jump of at most 5 percent opacity. Pass.
- [ ] AC-C06-7 (scripted input): switching the reduced-motion platform preference while a transition runs finishes it on the next frame and changes the next transition to 0. Pass.
- [ ] AC-C06-8 (review): every animated state change has a non-animated equivalent in the end state (a screenshot after the animation shows the full state). Pass: reviewer finds no state shown only during motion.
- [ ] AC-C06-9 (token test): no component note specifies a spring or an overshoot unless a named entry in [[Deviations from MD3]] adopts it. Pass: zero unnamed.

## Status in code

Detail per criterion is in [[Motion]].

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/theme.py` (`DURATIONS`, `EASINGS`); `tess-ui:src/tess_ui/spec/transition.py`; `tess-ui:src/tess_ui/motion.py`; `tess-ui:src/tess_ui/screen_transition.py` | Partly meets. 16 durations meet; `emphasized` has two values (fails AC-MOT-2); stylesheets use literals 150 and 200 equal to `short3` and `short4` (AC-C06-1 fails by name); `motion.py` zeroes durations under reduced motion by design (AC-C06-4 not run). Ripple and screen-transition timings are Material Web's own numbers, not tokens. |
| tess-shell | `tess-shell:src/tess_shell/binder/motion.py`; `tess-shell:src/tess_shell/model/look.py`; `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | Partly meets. 3 duration tokens whose values equal `short2`, `short4`, `medium4`; every duration is 0 under reduced motion and the Marquee does not scroll (AC-C06-4 meets in code, not run); the theme's `Reduced_Motion` block is empty, so the behaviour lives in code. |
| tre | `tre:docs/guide/animation.md`; `tre:crates/engine-core/src/tree/scroll.rs` | Not applicable as tokens. Default easing linear, default duration 0; cubic Bezier and spring supported. Reduced motion is reported as a signal and is not enforced, so enforcement lies with the project. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Desktop duration limits (control change at most 200 ms) | pointer-driven UI; MD3 durations are phone-scale | [[ADR-0002 Desktop density levels and target sizes]] |
| No focus ring animation, no caret blink, no marquee | testable in one frame; accessibility | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Springs excluded from the baseline | Expressive | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Reduced motion removes the ripple | accessibility | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- Motion tokens: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-motion.scss and Android Motion guide https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md (verified in [[Motion]]).
- WCAG 2.2 SC 2.3.3 Animation from Interactions: https://www.w3.org/TR/WCAG22/#animation-from-interactions (verified in [[Motion]]).
- MD3 motion overview: https://m3.material.io/styles/motion/overview (script-rendered, not readable by tools).
- Tooltip fade duration and accordion duration are design choices #needs-verification.
