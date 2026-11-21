---
title: Side Sheet
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, containment, overlay, sheet, modal]
related: ["[[Dialog]]", "[[Scrim]]", "[[Navigation Drawer]]", "[[Navigation Rail]]", "[[Panel and Surface]]", "[[Panel and Surface#Variants|Attached Panel]]", "[[Icon Button]]", "[[Button]]", "[[Tooltip]]", "[[Popup]]", "[[Scrollbar and Scroll Container]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Scrim]]", "[[Dialog]]", "[[12 Overlays]]", "[[Spacing and Density]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
---

# Side Sheet

> [!info] Summary
> A side sheet is a panel at the start or end edge that holds supplementary content or a secondary task next to the main content (standard, inline) or over it (modal, on a scrim). Material Design 3 counterpart: [Side sheets](https://m3.material.io/components/side-sheets/overview). Source of truth in code: see Status in code. No app or example uses it today.

## Purpose

Keep secondary content (details, filters, an inspector, a short form) reachable beside the main content without leaving it; the modal form blocks the main content for a focused secondary task.

## When to use and not

- Use when: the content supports the main region and fits a column of 256 to 400 dp (details of a selected item, filters, comments); on an expanded or larger window for the standard form; the modal form on narrower windows or for a task that must finish first.
- Do not use when: the task needs a decision and little text ([[Dialog]]); the content is a command list ([[Menu]]); the content is transient and anchored to a control ([[Popup]]); the content is a destination of the app ([[Navigation Drawer]], [[Navigation Rail]]); the content is a shell surface attached to a screen edge ([[Panel and Surface#Variants|Attached Panel]]).
- A modal side sheet does not open another modal ([[Scrim]] rule 7). A standard side sheet may sit beside a navigation region; both never overlap.

## Anatomy

1. Scrim (modal only): the whole window ([[Scrim]]).
2. Container: a full-height column at the start or end edge.
3. Header: back icon button (optional), headline, close icon button (optional).
4. Content: scrolls vertically.
5. Divider: 1 dp, above the actions, shown while content is scrolled.
6. Actions (optional): [[Button]] instances, end-aligned.
7. Focus ring (keyboard focus on a header control or action).

## Variants

| Variant | Container | Elevation | Shape | Scrim | Layout effect |
|---|---|---|---|---|---|
| Standard | `surface` | level 0 | `none` (0 dp) | none | inline: takes width from the main content while open |
| Modal | `surface_container_low` | level 1 | `large` (16 dp) on the corners facing the content (`corner-large-start`) | `scrim`, 0.32 | over the content; takes no room |
| Detached | `surface` or `surface_container_low` | level 0 or 1 | `large` (16 dp) all corners, inset from the edges | none | not built; see Deviations |

Values: Material Web [sheet-side tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-sheet-side.scss) (docked standard container `surface`, level 0, shape none; docked modal container `surface-container-low`, level 1, shape `corner-large-start`; detached shape `corner-large`; docked width 256 px).

Edge: start or end. The default is the end edge. A standard sheet takes its edge from its place in the row (first is start, last is end). A modal sheet takes the edge as a setting. The corner radius is on the side that faces the content; with the start edge the right corners are rounded, with the end edge the left corners.

## States

| State | Visual change | Token values |
|---|---|---|
| Closed | standard: zero width, not in the focus order; modal: no layer, no scrim | not applicable |
| Opening, closing | width or position animates (see Motion) | [[Motion]] |
| Open | container and content drawn; modal: scrim at 0.32 | see Variants |
| Content scrolled | divider shown above the actions (and under the header when scrolled from the top) | 1 dp `outline` |
| Header control, action: hover, focus, pressed | state layer over the control: icon buttons `on_surface_variant`, actions `primary`; 8, 10, 10 percent | [[State Layers]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Disabled action | content 38 percent, no state layer | [[State Layers]] |
| Loading | a progress indicator in the content; the header stays | not applicable |
| Empty | the caller shows an empty-state message in the content | not applicable |

## Tokens used

| Part | Role or token |
|---|---|
| Container | per Variants |
| Headline | `title_large`, `on_surface_variant` (Material Web `docked-headline-color`, `docked-headline-*` = title-large) |
| Body text | `body_medium`, `on_surface` |
| Header icon buttons | 24 dp icon, `on_surface_variant` ([[Icon Button]]) |
| Actions | `label_large`, `primary` (docked action state layers `primary`) |
| Divider | 1 dp, `outline` (`docked-divider-color`) |
| Scrim | `scrim` at 0.32 ([[Scrim]]) |
| Focus ring | `secondary`, 3 dp, 2 dp offset ([[Focus Ring]]) |

See [[Colour Roles]], [[Typography]], [[Shape]], [[Elevation]], [[Motion]], [[Spacing and Density]].

## Sizing and density

Width is a layout setting, held between 256 and 400 dp (the Material Web docked width is 256 px; the upper bound and the default 360 dp are tess-ui values, MD3 maximum #needs-verification). Header height, paddings and actions spacing follow the density level ([[ADR-0002 Desktop density levels and target sizes]]); values are Tesserae choices, as [[Spacing and Density]] has no sheet row (see Deviations).

| Item | default | compact | dense | MD3 or source value |
|---|---|---|---|---|
| Width (default) | 360 | 320 | 280 | 256 minimum token; 360 tess-ui |
| Header height | 56 | 48 | 40 | 56 (tess-ui, full-screen dialog header 56) |
| Header icon button container | 40 | 32 | 28 | [[Spacing and Density]] |
| Side padding (start, end) | 24 | 16 | 12 | 24 (tess-ui, left) |
| Gap between header items | 8 | 8 | 4 | 8 (tess-ui) |
| Actions row padding top | 16 | 12 | 8 | 16 (tess-ui) |
| Gap between actions | 8 | 8 | 4 | 8 (tess-ui) |
| Bottom padding | 24 | 16 | 12 | 24 (tess-ui) |
| Divider | 1 | 1 | 1 | 1 |

- The width range 256 to 400 holds at every density; compact and dense only change the default.
- Hit area of header buttons: at least 24 by 24 dp at every level; 48 by 48 dp in a touch context.

## Window size class behaviour

The size classes are those of [[Spacing and Density]] (compact below 600 dp, medium 600 to 839, expanded 840 to 1199, large 1200 to 1599, extra-large 1600 and up); pane rules are in [[10 Layout Overflow and Scrolling]]. A boundary value belongs to the larger class. Density does not change with the class.

| Width class | Standard sheet | Modal sheet |
|---|---|---|
| compact (below 600) | not shown; the content opens as a modal sheet | full window width, corner `none`, scrim not visible; closes with the close button, Escape or Back |
| medium (600 to 839) | not shown; modal | width as set, at most the window width minus 56 dp |
| expanded (840 to 1199) | inline, if the main content keeps at least 320 dp | as set |
| large, extra-large | inline, if the main content keeps at least 320 dp | as set |

If the main content would drop below 320 dp (the pane minimum of [[10 Layout Overflow and Scrolling]]), a standard sheet is shown as a modal sheet. The class is re-evaluated on each resize; an open standard sheet that no longer fits becomes modal in place (focus moves into it and the scrim appears), and a modal sheet that now fits does not turn into a standard one on its own (the user reopens it). The compact and medium rules are Tesserae design choices modelled on MD3 pane guidance #needs-verification.

## Layout and overflow

- The sheet is full height of its region. Content scrolls vertically with a visible scrollbar thumb ([[ADR-0003 Scrollbar rule]]); the header and the actions stay fixed.
- A standard sheet is clipped while it opens and closes (its width animates); content does not reflow during the animation: it keeps the final width and is clipped by the container.
- Headline: one line, end ellipsis, full text as name and tooltip (AC-LAY-3 to AC-LAY-5 apply); vertically centred in the header height.
- Content wider than the sheet does not scroll sideways: the sheet wraps text and forms keep one column; a table or code block inside scrolls on its own horizontal axis.
- When a modal sheet is taller than the window, the content area is the scroll region; the sheet never exceeds the window height.
- Space runs out: below 256 dp the sheet is not allowed; the parent chooses the modal form.

## Behaviour

- Pointer: the close button closes the sheet; the back button runs the caller's back handler. Modal: a press on the scrim closes a dismissible sheet and is consumed ([[Scrim]] rule 4); a press inside the sheet never closes it; input beneath the scrim reaches nothing. Standard: the main content stays fully interactive.
- Keyboard, modal: on open, focus moves into the sheet to the element marked initial focus, else the first focusable element in tab order (the back or close button, or first content control). Tab and Shift+Tab cycle inside the sheet only (focus trap with exit). Escape closes a dismissible sheet and returns focus to the control that opened it; a non-dismissible sheet ignores Escape and the scrim press but still closes by its close button or an action ([[Dialog]] alert behaviour). Enter and Space run the focused button.
- Keyboard, standard: no focus trap. When the user opens it with a control, focus moves to its first focusable element; when a program opens it, focus stays where it is. Tab order puts the sheet after the main content when it is at the end edge and before it when at the start edge. Escape inside a closable standard sheet closes it and returns focus to the opener; when the opener is gone, focus goes to the main content's first focusable element.
- Closing a standard sheet while focus is inside moves focus to the opener (never to the document start).
- Touch: a modal sheet can be dragged toward its edge to dismiss; the same dismiss is reachable by keyboard and button (WCAG 2.2 SC 2.5.7). Hit areas 48 by 48 dp at least in a touch context.
- A modal sheet closes any open [[Popup]] and removes any tooltip when it opens ([[12 Overlays]], z-order).

## Tooltip and overlay behaviour

The header buttons (Back, Close) carry plain tooltips with their names ([[Icon Button]], [[ADR-0004 Tooltip rule]]); a truncated headline shows a tooltip on the headline node. The sheet itself shows no tooltip. A modal sheet is a modal layer: one scrim under the topmost modal, above every non-modal overlay; tooltips of controls inside it show above it ([[12 Overlays]]). A standard sheet is part of the page layout, not a layer: it never draws a scrim and menus and popups opened from it layer above it normally.

## Motion

- Standard: width eases open and shut in 250 ms (`medium1`) with `standard` easing (tess-ui `Transition { Width: 250 }`); closing is not longer than opening ([[Motion]] rule 3). Content does not move during the animation.
- Modal: the scrim fades in 500 ms and out 150 ms, linear ([[Scrim]]). The sheet slides in from its edge over the `medium4` duration (400 ms) with `emphasized_decelerate` and out over 200 ms (`short4`) with `emphasized_accelerate` (Tesserae choice; MD3 slide durations are not published as tokens #needs-verification). Content is drawn from the first frame.
- Reduced motion: the sheet and scrim appear and disappear in one frame ([[Motion]] rule 4).

## Accessibility

- Role: standard sheet `complementary` named by its headline (supporting content); when the sheet is the main task of its pane (an editor the user works in, not supplementary) it is `region` named by the headline. Modal sheet `dialog`, named by the headline, modal. tre has none of `complementary` or `region` (its role list ends at `group`, `separator`): the sheet is a `group` with the headline as name until the engine adds the roles ([[Accessibility Rules]] AR-2; candidate request in the summary).
- Name: the headline; a sheet without a headline needs an explicit label.
- Keys: see Behaviour. Focus ring on every focusable element ([[Focus Ring]]); never clipped by the sheet's scroll container (the ring extends 5 dp beyond the border box, AC-LAY-14).
- Modal: content beneath is inert (not focusable, hidden from assistive technology while open) #needs-verification for the engine tree. Escape and the visible close button are the exit (WCAG 2.2 SC 2.1.2).
- Announcement: opening a modal sheet announces role and name; closing a standard sheet announces nothing; the opener's expanded state is updated (`expanded` true or false on the opener).
- Contrast: `on_surface_variant` on `surface` and on `surface_container_low` at least 4.5:1 in light and dark; ring 3:1 ([[Colour Roles]]).

## Dark and light

All colours are roles ([[Theme Following the System]]). The scrim is `scrim` at 0.32 in both schemes. In dark, `surface_container_low` is a lighter tone than `surface`, which separates the modal sheet from the dimmed content.

## Defaults

| Setting | Default |
|---|---|
| Form | standard where the window is expanded or larger, else modal |
| Edge | end |
| Width | 360 dp (256 to 400) |
| Closable | yes |
| Dismissible (modal) | yes (Escape, scrim press) |
| Scrim | `scrim` at 0.32 |
| Standard open state | closed |

## Acceptance criteria

- [ ] AC-SSH-1 (token test): standard container `surface`, level 0, shape 0 dp; modal container `surface_container_low`, level 1, corner 16 dp on the corners facing the content (start edge: right corners; end edge: left corners) and 0 on the others.
- [ ] AC-SSH-2 (token test): headline `title_large` in `on_surface_variant`, body `body_medium` in `on_surface`, actions `label_large` in `primary`, divider 1 dp `outline`.
- [ ] AC-SSH-3 (geometry check): width is clamped to 256 to 400 dp for requests of 100, 360 and 900 dp (256, 360, 400); header height 56, 48, 40 dp at default, compact, dense; side padding 24, 16, 12; actions top padding 16, 12, 8 (scale factors 1.0 and 2.0).
- [ ] AC-SSH-4 (geometry check): at window widths 599, 600, 839, 840, 1199, 1200 dp with a 360 dp sheet and a 72 dp rail, a standard sheet is shown inline only where the main content keeps at least 320 dp, and otherwise as a modal sheet; at width 599 the modal sheet is as wide as the window.
- [ ] AC-SSH-5 (geometry check): resizing across the boundary with a standard sheet open turns it modal (scrim drawn, focus inside it) and records a single state change; the main content is never narrower than 320 dp while shown.
- [ ] AC-SSH-6 (pixel check): while a modal sheet is open, a window pixel outside the sheet equals the underlying pixel blended with `scrim` at 0.32 (within 1 level per channel) at the four window corners; a standard sheet draws no scrim (pixel unchanged).
- [ ] AC-SSH-7 (scripted input): modal open moves focus to the initial-focus element within one frame (first focusable in tab order if none is marked); Tab x30 and Shift+Tab x30 keep focus inside the sheet (60 of 60); Escape closes it and focus is on the opener within one frame; a non-dismissible sheet stays open on Escape and scrim press.
- [ ] AC-SSH-8 (scripted input): a press on the scrim closes a dismissible modal sheet and the control under the press receives no event; a press inside the sheet does not close it; a wheel event aimed beneath produces 0 handler calls.
- [ ] AC-SSH-9 (scripted input): standard sheet opened by a user action focuses its first focusable element; opened by a program leaves focus unchanged; Tab leaves the sheet (no trap) in both directions; Escape inside a closable standard sheet closes it and focus returns to the opener.
- [ ] AC-SSH-10 (AT tree assertion): standard sheet role `complementary` (or `region`, or `group` where the engine lacks them) named by the headline; modal sheet role `dialog` named by the headline; the opener reports `expanded` matching the open state.
- [ ] AC-SSH-11 (scripted input): content 1000 dp tall in a 500 dp sheet scrolls with a visible scrollbar thumb; header and actions stay fixed; the divider above the actions shows while content is scrolled and hides at the end; keyboard focus scrolls into view with its ring visible.
- [ ] AC-SSH-12 (pixel check): standard width reaches its target 250 ms to 283 ms after the toggle at 60 Hz; the scrim reaches 0.32 between 500 ms and 533 ms after a modal open and 0 between 150 ms and 183 ms after close; with reduced motion both end states appear on the next frame.
- [ ] AC-SSH-13 (scripted input): the back button runs the back handler once; the close button closes the sheet; a sheet with `closable` off has no close button and a modal one without dismissal still offers an action or another exit.
- [ ] AC-SSH-14 (scripted input): a headline of 80 characters in a 256 dp sheet shows one line ending in `…`; the accessible name is the full headline; hovering 500 ms shows a tooltip whose trigger is the headline node; Back and Close show their tooltips on hover and keyboard focus.
- [ ] AC-SSH-15 (contrast script): `on_surface_variant` on `surface` and on `surface_container_low` and `primary` on the same containers measure at least 4.5:1 in light and dark.
- [ ] AC-SSH-16 (scripted input): opening a modal sheet closes an open popup and removes a visible tooltip within one frame; opening a second modal while one is open is refused by default ([[Scrim]] rule 7).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/SideSheet_View.tdl`, `SideSheet_Stylesheet.tdl`, `SideSheetModal_View.tdl`, `SideSheetModal_Stylesheet.tdl`, `SideSheetPanel_View.tdl`, `SideSheetPanel_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/overlays.py` (`side_sheet`), `tess-ui:docs/components/side-sheets.md`, tests `tess-ui:tests/test_side_sheet.py` | Partly meets. Meets AC-SSH-1 (standard `surface`; modal `surface_container_low`, level 1, 16 px corners on the open side, tested), AC-SSH-3 in part (width held 256 to 400, default 360, header 56, tested; no density levels, so compact and dense fail), AC-SSH-7 in part (modal layer: Escape and scrim press close, Tab stays inside, focus returns; initial focus is the engine's first focusable node, tested), AC-SSH-8, AC-SSH-11 (content scrolls, a line shows over the actions, tested), AC-SSH-13. Fails AC-SSH-2 (headline `on_surface`, not `on_surface_variant`), AC-SSH-4 and AC-SSH-5 (no size-class switch; the caller picks standard or modal), AC-SSH-6 (the modal scrim is a baked-in colour, not the `scrim` role at 0.32: AC-SCR-3 also fails), AC-SSH-9 (the standard sheet takes no focus when the user opens it), AC-SSH-10 (standard sheet role `group`, modal sheet role `dialog`; no `complementary`), AC-SSH-12 in part (standard width animates 250 ms; the modal sheet does not slide), and the detached sheet is not built. Modal sheet slide-in not built. Not used by any app or example |
| tess-shell | none | Not applicable. The shell has no Side Sheet element; its attached slide-in Panel is specified in [[Panel and Surface#Variants|Attached Panel]] and [[Panel and Surface|Panel Surface]] |
| tre | `tre:docs/reference/layers.md` | Mechanism only: `show_layer(modal=True, dismissible=True)` blocks input beneath, moves focus to the first focusable node, keeps Tab inside, delivers `dismiss` on a press outside and on Escape; the engine draws no scrim; a layer at its own `x`/`y` without an anchor; roles `complementary` and `region` do not exist |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Width, header and paddings per density level | desktop information density | [[ADR-0002 Desktop density levels and target sizes]] |
| Standard form only where the main content keeps 320 dp; else modal | pane minimum of the layout chapter; MD3 does not give a desktop rule | [[10 Layout Overflow and Scrolling]] |
| Standard sheet moves focus on user-initiated open; Escape closes it | keyboard-first desktop use; MD3 documents no keyboard model | [[14 Accessibility Basics]] |
| Drag-to-dismiss of a modal sheet must also be reachable by keyboard | WCAG 2.2 SC 2.5.7 | [[Accessibility Rules]] |
| Detached sheet not specified | no desktop use case in the projects | [[Deviations from MD3]] |
| Scrim 0.32 for the modal sheet | one scrim value for all modals; Material Web drawer token uses 0.4 | [[Scrim]] |
| Slide timings (400 ms in, 200 ms out) | not published as tokens; Tesserae choice from [[Motion]] | [[Deviations from MD3]] |

## Sources

- Material Web side sheet tokens (docked container width 256 px, standard container `surface` level 0 shape none, modal container `surface-container-low` level 1 shape `corner-large-start`, detached shape `corner-large`, headline `title-large` in `on-surface-variant`, divider `outline`, action state layers `primary`), verified 2026-11-21: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-sheet-side.scss
- Material Components Android Side Sheet guide (standard and modal anatomy; modal blocks interaction, scrim, tap outside dismisses, drag to dismiss; coplanar sheets not recommended on narrow screens): https://github.com/material-components/material-components-android/blob/master/docs/components/SideSheet.md
- WAI-ARIA 1.2 complementary and region roles; APG landmark regions: https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- APG modal dialog pattern (Tab cycles, Escape closes, focus returns): https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- WCAG 2.2 SC 2.1.2 No Keyboard Trap, SC 2.5.7 Dragging Movements: https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html, https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- tess-ui documentation: `tess-ui:docs/components/side-sheets.md`; engine layers: `tre:docs/reference/layers.md`.
- Not verified: MD3 specification page values (script-rendered app): sheet maximum width, compact and medium behaviour, slide durations #needs-verification; engine tree inertness under a modal layer #needs-verification.
