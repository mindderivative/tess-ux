---
title: 09 State Feedback Rules
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, state, interaction, feedback, disabled, ripple, focus]
related: ["[[State Layers]]", "[[Focus Ring]]", "[[Colour Roles]]", "[[Motion]]", "[[Shape]]", "[[06 Motion Rules]]", "[[08 Iconography Rules]]", "[[03 Typography and Text Rules]]", "[[02 Colour and Theming]]", "[[14 Accessibility Basics]]", "[[01 Principles and Scope]]", "[[Button]]", "[[Icon Button]]", "[[Switch]]", "[[List Item]]", "[[Tree Node]]", "[[Text Field]]", "[[Form Row]]", "[[Menu]]", "[[Tooltip]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[ADR-0004 Tooltip rule]]", "[[Deviations from MD3]]"]
depends_on: ["[[State Layers]]", "[[Focus Ring]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
---

# 09 State Feedback Rules

> [!info] Summary
> Chapter-level principles for how every interactive element answers the user: hover, focus, pressed, dragged, disabled, selected and error feedback. Opacities, ring geometry and ripple timings live in [[State Layers]] and [[Focus Ring]]; this chapter links and copies no value, and states the rules that every component shares. Material Design 3 baseline: [interaction states](https://m3.material.io/foundations/interaction/states/overview).

## Purpose

The user needs to see at once what the pointer is over, what has keyboard focus, what is pressed, what cannot be used and what is wrong. If each component answers differently, the user must relearn them. The chapter makes the answers identical.

## Scope

- In scope: the feedback vocabulary across components, precedence, focus visibility, ripple on desktop, disabled and read-only, selected, error and warning consistency, feedback in touch and under reduced motion.
- Out of scope: opacity values, ring geometry and ripple timings ([[State Layers]], [[Focus Ring]]), the motion tokens ([[06 Motion Rules]]), validation logic of forms ([[Form Row]], [[Text Field]]).

## Principles

1. One vocabulary. Hover, focus, pressed, dragged, disabled, selected and error look the same on every component of the same kind of surface. A component note lists its states and refers to the shared feedback, and does not invent its own opacity ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]).
2. A layer, not a colour change. State shows as a state layer in the content colour at a fixed opacity over the container; the content colour and the container colour of the control do not change by state, except selected and error, which have their own roles ([[State Layers]]).
3. One layer at a time with a fixed precedence: dragged, pressed, focused, hovered ([[State Layers]]).
4. Focus is visible for the keyboard. Keyboard focus shows the ring and the focus layer; pointer focus on non-text controls shows neither; text inputs show an indicator for pointer focus too ([[Focus Ring]]). The ring is never clipped and never hidden by another layer.
5. Feedback arrives in the first frame. A state layer changes within one frame at 60 Hz of the input (hover with the 15 ms fade of [[State Layers]]); the control never waits for a handler.
6. Disabled is one scheme. Content at 38 percent, filled container at 12 percent, no layers, no ripple, no focus, no activation, and the disabled flag in the accessibility tree ([[State Layers]]).
7. Disabled is never the only cue. A disabled control that carries information (a setting value) remains readable by text, and a reason is available on request: the tooltip on the control states why ([[ADR-0004 Tooltip rule]]).
8. Error is text plus colour plus a mark. An error state uses the `error` role, a supporting text that says what is wrong and how to fix it, and an icon or shape cue; colour alone never marks it ([[Colour Roles]], [[14 Accessibility Basics]]).
9. Selected is a state of its own. Selected shows by a container or content role and a second cue (a check, a bar, weight), not by the hover layer; hover and focus layers still show on a selected element.
10. Feedback respects reduced motion. The layer and ring still appear; fades and the ripple do not ([[06 Motion Rules]]).
11. Feedback follows the shape. Layer, ripple and ring are clipped or offset by the element's shape ([[Shape]]).

## The feedback table

| State | Visible feedback | Applies to | Source |
|---|---|---|---|
| Hover | state layer, content colour, hover opacity | every interactive element under a pointer | [[State Layers]] |
| Focus (keyboard) | ring plus focus layer | every focusable element | [[Focus Ring]], [[State Layers]] |
| Focus (pointer) | nothing on buttons, switches, rows; an indicator on text inputs | | [[Focus Ring]] |
| Pressed | pressed layer, ripple where the project has one | every activating element | [[State Layers]] |
| Dragged | dragged layer | a dragged item or thumb | [[State Layers]] |
| Selected | selection role plus a second cue | rows, tabs, chips, segmented controls | component notes |
| Disabled | content 38 percent, container 12 percent, no layers | every control | [[State Layers]] |
| Read-only | normal content colour, no edit affordance, focusable, no error | text fields and values | [[Text Field]] |
| Error | `error` role, supporting text, mark | fields, rows, form groups | [[Form Row]], [[Text Field]] |
| Warning | warning cue by text and icon; no MD3 role | forms, status | #needs-verification (MD3 has no warning role) |
| Loading or busy | progress indicator or busy text; the element ignores activation | buttons, panels | component notes |

## Ripple on desktop

- The ripple is the pressed feedback of tess-ui. It starts at the pointer position, grows, and fades on release, clipped to the control ([[State Layers]], Ripple).
- A project may omit the ripple: it then draws the pressed layer alone at the pressed opacity. Both are valid; a project never draws a ripple on one element class and nothing on a sibling class of the same surface.
- With keyboard activation (Space or Enter) the ripple starts at the centre of the control.
- A press that ends outside the control cancels activation and fades the ripple.
- Touch input uses the touch delay of [[State Layers]]; pointer input has none.
- Under reduced motion no ripple grows; the pressed layer shows in one frame.
- The ripple is never the only sign of activation: the action's result is the primary feedback.

## Disabled and read-only

- Every disabled control is in the tab order only when its note says so; otherwise it is skipped, and the accessibility tree still lists it with the disabled flag ([[14 Accessibility Basics]]).
- A disabled element takes no hover, focus, pressed or dragged layer and no tooltip except the one that gives the reason, which shows on hover and is also reachable by keyboard on the enclosing focusable control #needs-verification (a disabled element is not focusable, so the keyboard route is the note of the control that explains it).
- Disabled content does not need 4.5 to 1; it must stay legible enough to read (38 percent of `on_surface`) and must not be the only way a value is shown ([[State Layers]]).
- The text field disabled container follows the field's own tokens, which are 4 percent in the Material Web token file, not 12 ([[Text Field]], Deviations).

## Error and warning consistency

1. One role for error: `error` for the mark and the border or indicator, `on_surface` or `on_error_container` for text as the component note states.
2. The supporting text is below the control, in the same type role as helper text ([[03 Typography and Text Rules]]), and replaces the helper text while the error holds.
3. The icon cue comes from [[08 Iconography Rules]] and has an accessible name or is covered by the supporting text.
4. The field is exposed as invalid in the accessibility tree and the message is announced once in a polite live region ([[14 Accessibility Basics]] AC-A11Y-11).
5. A form summarises errors at the top only when more than one field is wrong; each message still sits at its field.
6. Error feedback survives hover, focus and press: those layers draw on top, the error indicator stays.

## Where each rule lives

| Topic | Note |
|---|---|
| Opacities, disabled scheme, ripple timings | [[State Layers]] |
| Ring geometry, visibility, clipping | [[Focus Ring]] |
| Colour roles, contrast | [[Colour Roles]] |
| Motion tokens and reduced motion | [[Motion]], [[06 Motion Rules]] |
| Accessibility tree flags and announcements | [[14 Accessibility Basics]] |
| Icon cues | [[08 Iconography Rules]] |
| Per-component states | component notes |

## Acceptance criteria

The criteria AC-STL-1 to AC-STL-9 are defined in [[State Layers]] and AC-FOC-1 to AC-FOC-9 in [[Focus Ring]].

- [ ] AC-C09-1 (token test): every component note of `30 Component Specifications` for an interactive element lists the states hover, focus, pressed and disabled (or states "Not applicable: reason" for each) and names only state opacities equal to [[State Layers]]. Pass: a script finds zero notes missing a state and zero opacity values outside 0.08, 0.10, 0.16, 0.38 and 0.12.
- [ ] AC-C09-2 (pixel check): for a sample of one control per class (button, icon button, switch, list row, tree row, menu item, text field), hover, focus and pressed produce the opacities of [[State Layers]] (AC-STL-2) in the same content colour logic. Pass: 7 of 7 classes within 1 per 8-bit channel.
- [ ] AC-C09-3 (scripted input): for each class of AC-C09-2, a click with the mouse shows no ring (text field shows an indicator), and Tab shows the ring on the next control. Pass: 7 of 7.
- [ ] AC-C09-4 (pixel check): for each class, a disabled control's content equals `on_surface` at 0.38 over the container, hover, press and focus change no pixel, and the pointer cursor shows no activation. Pass: 7 of 7.
- [ ] AC-C09-5 (AT tree assertion): every disabled control is present in the tree with the disabled flag and rejects a click and the Enter key. Pass: zero exceptions.
- [ ] AC-C09-6 (scripted input): hovering a disabled control that has a reason shows a tooltip on that control with the reason text, within the hover delay of [[Tooltip]]. Pass: reason text equals the note.
- [ ] AC-C09-7 (pixel check): an error field shows the `error` role on its indicator, a supporting text below it and an icon or shape cue; the greyscale render differs from the valid state by a non-colour feature ([[14 Accessibility Basics]] AC-A11Y-16). Pass.
- [ ] AC-C09-8 (scripted input): in an error field, hover, focus and press keep the error indicator on screen and add their layers; the invalid flag stays and the message is announced once. Pass: indicator pixel equal in the 4 states, announcement count 1.
- [ ] AC-C09-9 (scripted input): a pointer press on a control with a ripple starts the ripple at the pointer position within 1 frame; a Space press starts it at the control centre within 1 dp; a press released outside the control does not activate. Pass: origin positions equal, no activation.
- [ ] AC-C09-10 (scripted input): with reduced motion on, press shows the pressed layer on the next frame and no ripple geometry; focus and hover layers appear; the ring appears. Pass.
- [ ] AC-C09-11 (token test): within one project, all element classes of one surface either draw the ripple or none do. Pass: a scan of the stylesheets finds no mixed surface.
- [ ] AC-C09-12 (pixel check): a selected row shows its selection cue and, on hover, the hover layer over it; the cue is not a layer opacity. Pass: both visible.

## Status in code

Detail per criterion is in [[State Layers]] and [[Focus Ring]].

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/interaction.py`; `tess-ui:src/tess_ui/controls.py`; `tess-ui:src/tess_ui/ripple.py`; `tess-ui:src/tess_ui/focusring.py` | Partly meets. Opacities and ripple timings equal the spec (AC-C09-1 by constants); layer and ripple apply to `Rect` and `Container` among plain nodes and other controls draw their own, so AC-C09-2 and AC-C09-11 are not proven for every class; ring is not recomputed on resize (AC-FOC-6 fails). |
| tess-shell | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl`; `tess-shell:src/tess_shell/model/look.py` | Absent for state layers. States change Background, Border_Color or Opacity (hover 0.85, pressed 0.7, disabled 0.5), ring is 2 px in `primary`. AC-C09-1, AC-C09-2 and AC-C09-4 fail; adoption is not decided ([[ADR-0009 State layer percentages]]). |
| tre | `tre:docs/guide/painting.md`; `tre:docs/guide/events-and-input.md`; `tre:examples/ripple.py` | Not applicable. The engine paints no state layers; it gives a ripple recipe and reports `focus_visible` and the disabled flag. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Focus and pressed layers 10 percent | latest published tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| One layer at a time with fixed precedence | avoids stacked opacity | [[ADR-0009 State layer percentages]] |
| Reduced motion removes the ripple | accessibility | [[ADR-0009 State layer percentages]] |
| Ring for pointer focus in text inputs; no ring animation | caret may be hidden; testable in one frame | [[ADR-0009 State layer percentages]] |
| Reason tooltip on disabled controls | desktop users need to know why | [[ADR-0004 Tooltip rule]] |

## Sources

- State tokens: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-state.scss and component files `_md-comp-filled-button.scss`, `_md-comp-filled-text-field.scss` (disabled container 0.12 on a button, 0.04 on a filled text field; verified 2026-11-21).
- Ripple and focus ring: https://github.com/material-components/material-web/blob/main/ripple/internal/ripple.ts and `focus/internal/focus-ring.ts` (verified in [[State Layers]] and [[Focus Ring]]).
- WCAG 2.2 SC 1.4.1 Use of Color, SC 1.4.3 inactive component exemption: https://www.w3.org/TR/WCAG22/ #needs-verification (text not opened for this chapter).
- MD3 states: https://m3.material.io/foundations/interaction/states/overview (script-rendered, not readable by tools).
