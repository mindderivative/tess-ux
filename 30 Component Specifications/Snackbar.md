---
title: Snackbar
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, communication, snackbar, live-region]
related: ["[[Banner]]", "[[Notifications]]", "[[Notifications|Notification Window]]", "[[12 Overlays#Layers and routes|Layer]]", "Timers", "[[Button]]", "[[Icon Button]]", "[[Dialog]]", "[[Popup]]", "[[Tooltip]]", "[[Colour Roles]]", "[[Elevation]]", "[[Shape]]", "[[Typography]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[12 Overlays]]", "[[Colour Roles]]", "[[Elevation]]", "[[Motion]]"]
---

# Snackbar

> [!info] Summary
> A short, non-modal message about a process that has happened or will happen, shown near the bottom of the window with at most one action, that goes away by itself. Counterpart: Material Design 3 [Snackbar](https://m3.material.io/components/snackbar/overview). Source of truth in code: see Status in code.

## Purpose

Confirm what the app did ("Note saved"), offer an immediate undo or retry, and report a result that does not need a decision, without interrupting the user.

## When to use and not

- Use when: the message is brief (one or two lines), the user need not act, and a single optional action (Undo, Retry, View) is enough.
- Do not use when: the user must decide or the message must stay until read (use [[Banner]] or [[Dialog]]); the message belongs to a field (inline error text, [[Text Field]]); the message is a system notification from another program (outside v1: [[Notifications|Notification Window]]); the information is only in the snackbar and is needed later (put it in a log or a list).

## Anatomy

1. Container: `inverse_surface`, 4 dp corners, elevation level 3.
2. Supporting text: one or two lines, `body_medium`, `inverse_on_surface`.
3. Action (optional): one text button, `label_large`, `inverse_primary`.
4. Close control (optional): an icon button, 24 dp `close` icon in `inverse_on_surface`.
5. Host: the region of the window that positions the snackbar (window bottom, start edge).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Single line | message of one line | container 48 dp high at default density |
| Two lines | message of two lines | container grows to fit, 64 dp at default |
| With action | undo, retry, view | action button after the text; duration 10 s |
| With close | the message may stay until dismissed | close icon button at the end; required for an untimed snackbar |
| Centred | narrow windows or centred layouts | horizontally centred instead of at the start |

MD3 also describes a longer action layout below the text for long labels; it is not specified here #needs-verification.

## States

| State | Visual change | Token values |
|---|---|---|
| Entering | fade in over 150 ms (`short3`), slide up 8 dp | see Motion |
| Shown | static | container `inverse_surface`, text `inverse_on_surface` |
| Timer paused | the timer stops while the pointer is over it or focus is inside it | no visual change |
| Action hover, focus, pressed | state layer in `inverse_primary` at 8, 10 and 10 percent | [[ADR-0009 State layer percentages]], Material Web snackbar tokens |
| Close hover, focus, pressed | state layer in `inverse_on_surface` at 8, 10 and 10 percent | same |
| Keyboard focus on action or close | focus ring 3 dp, 2 dp offset, role `inverse_primary` for the action | [[Focus Ring]]: the ring role `secondary` is invisible on `inverse_surface`, so the role is `inverse_primary` here #needs-verification |
| Leaving | fade out over 75 ms | see Motion |
| Disabled | not applicable: a snackbar is never disabled |  |

## Tokens used

| Part | Token | Value |
|---|---|---|
| Container colour | `md.comp.snackbar.container.color` | `inverse_surface` (#322F35 light, #E6E0E9 dark) |
| Container elevation | `container.elevation` | `level_3` (6 dp, see [[Elevation]]) |
| Container shape | `container.shape` | `extra_small`, 4 dp ([[Shape]]) |
| Single-line height | `with-single-line.container.height` | 48 dp |
| Two-line height | `with-two-lines.container.height` | 68 dp (see Sizing and density) |
| Icon size and colour | `icon.size`, `icon.color` | 24 dp, `inverse_on_surface` |
| Supporting text | `supporting-text.*` | `body_medium` 14/20, `inverse_on_surface` |
| Action label | `action.label-text.*` | `label_large` 14/20, 500, `inverse_primary` |

Source: [Material Web snackbar tokens, latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-snackbar.scss), read 2026-11-21. Contrast, computed for this note from the role values: text on container 11.6 to 1 light and 10.2 to 1 dark; action `inverse_primary` on container 7.7 to 1 light and 5.0 to 1 dark. All pass 4.5 to 1.

## Sizing and density

The snackbar is a transient message surface, so it follows the control heights of its density level for its action and for its minimum height; text stays `body_medium` at all levels.

| Level | Minimum height (single line) | Text vertical padding | Two-line height | Margin to window edge | Action button |
|---|---|---|---|---|---|
| default | 48 | 12 | 64 | 16 | 40 dp high ([[Button]]) |
| compact | 40 | 8 | 56 | 8 | 32 |
| dense | 32 | 4 | 48 | 8 | 28 |

- Width: at least 344 dp and at most 560 dp (the tess-ui range); in a window narrower than 344 dp plus twice the margin the snackbar is the window width minus twice the margin. Material Components Compose caps the container at 600 dp #needs-verification.
- Horizontal padding: 16 dp at the start of the text, 8 dp after the last button (MD3 value, kept at all levels so the text edge aligns across levels).
- The two-line default height is 64 dp, not the MD3 68 dp: the text padding is 12 dp (on the 4 dp grid, [[Spacing and Density]]) instead of the 14 dp that gives 68 dp.
- Hit areas: the action and the close button are at least 24 dp by 24 dp at every level; the close button is 40 dp at default (equal to an icon button), 32 at compact and 28 at dense; in a touch context 48 dp ([[ADR-0002 Desktop density levels and target sizes]]).

## Layout and overflow

- Position: inside the window, above the content, at the bottom edge, `margin` from the edge, at the start side (left in left-to-right locales) or centred. It sits in an in-window layer ([[12 Overlays#Layers and routes|Layer]]); it is clipped to the window, never a separate window ([[12 Overlays]]).
- Text wraps at word boundaries to at most 2 lines; a third line is truncated with an ellipsis and the full text stays in the accessible name. The text width is the container width minus paddings minus the action and close controls. Text is vertically centred in the container within 1 px for one line.
- Action label: one line, at most 1 word to 3 words; a label longer than the available space truncates with an ellipsis and keeps its full name.
- Focus not obscured: if the control that has keyboard focus lies under the snackbar rectangle, the snackbar moves up by its own height plus 8 dp until the control is fully visible, or hides, so the focused control is never covered ([WCAG 2.4.11](https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum)) #needs-verification-as-design-choice.
- Lifting above a floating action button or a bottom bar is not built in tess-ui; the spec requires it where those elements exist (the snackbar never covers them).

## Behaviour

- Duration. A snackbar with text only stays 4000 ms; one with an action stays 10000 ms. A caller may set a duration from 4000 to 10000 ms, or untimed with a close control. The range comes from Compose Material 3: `SnackbarDuration.Short` is 4000 ms, `Long` is 10000 ms, and `Indefinite` stays until dismissed or replaced ([source](https://github.com/androidx/androidx/blob/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/SnackbarHost.kt), `toMillis`, verified 2026-11-21). Material Components Android presets are shorter (`LENGTH_SHORT` 1500 ms, `LENGTH_LONG` 2750 ms, in `SnackbarManager.java`); Tesserae takes the Compose figures because a desktop user reads while their pointer is elsewhere and [WCAG 2.2.1](https://www.w3.org/TR/WCAG22/#timing-adjustable) asks for enough time. The statement "4 to 10 seconds" in the Material Design 3 guidelines is not readable by tools: #needs-verification.
- The timer is a project timer (Timers); it stops while the pointer is over the snackbar or keyboard focus is inside it, and restarts at the full duration when the pointer leaves or focus leaves.
- One at a time. At most one snackbar is visible per window. A new message waits in a first-in first-out queue and shows when the current one has closed; no gap longer than 100 ms between them. A message with the same `id` as the visible or a queued one replaces it. A queue of more than 5 drops the oldest message that has no action. Rationale: MD3 and Material Components show one snackbar at a time ([Android docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Snackbar.md): "Only one snackbar will be shown at a time"), but the Android library dismisses the old one on a new `show`; Tesserae queues so that a result is not lost.
- Dismissal: timeout, the action (runs the action then closes), the close control, a replacing message. A press elsewhere in the window does not dismiss it and is not consumed by it. Escape while focus is inside it dismisses it and returns focus to the control that had it.
- Keyboard. The snackbar is not modal and takes no focus when it appears, so typing is not interrupted. An action must still be reachable: while a snackbar with an action or close control is visible, its controls are the last stops of the window's Tab cycle, and the chord Alt+Shift+N moves focus to the current snackbar's action ([[ADR-0019 Banner and snackbar focus chords]]). Without this a keyboard user cannot undo (WCAG 2.1.1). Alt+Shift+N is a proposed default: a collision check against the shell's shortcut map and the application's own map is required before a project adopts it, and the chord table of [[11 Interaction]] lists it as proposed.
- Touch: swipe to dismiss is MD3 behaviour and is not built; where touch is the primary input it is required (swipe toward the nearest window edge dismisses).
- The action runs once per snackbar; after it runs the snackbar closes and the action text is not shown again for the same message.

## Tooltip and overlay behaviour

The snackbar carries no tooltip ([[ADR-0004 Tooltip rule]]). Its close control, an icon-only button, carries the tooltip "Close". It is a non-modal in-window layer: no scrim, not dismissed by outside press, below tooltips, popups and dialogs in the stacking order ([[12 Overlays]]: snackbars are layer 2 of the stacking table, above content). A dialog hides it or shows above it; a snackbar never shows above a modal scrim.

## Motion

| Animation | Duration | Easing | Source |
|---|---|---|---|
| Enter: fade in and slide up 8 dp | 150 ms (`short3`) fade, 250 ms slide | linear fade, `emphasized_decelerate` slide | Material Components Android `BaseTransientBottomBar` (fade in 150 ms, slide 250 ms) |
| Exit: fade out | 75 ms (the Android value; no MD3 duration token is 75) | linear | same |

Reduced motion: appears and disappears in one frame, no slide ([[Motion]], rule 4). The timer still runs. The exit is at most 75 percent of the enter ([[Motion]], rule 3).

## Accessibility

- Role and live region: role `status` with `live="polite"`. A snackbar never interrupts: assertive announcements are reserved for what the user must act on ([[14 Accessibility Basics]]), and anything that needs action is a [[Banner]] or a [[Dialog]]. tess-ui exposes role `alert` with live polite; an `alert` role implies assertive in WAI-ARIA, so the combination is ambiguous: AC-SNK-3 pins `status`.
- Announcement: the text is announced once, when the snackbar enters the tree (tre announces a live node when it enters the tree or its name changes, `tre:docs/guide/accessibility.md`). The queue shows one message at a time, so announcements are sequential and in call order. A message with an action announces "message, action label" through the name. No announcement on timer expiry or on exit.
- Name: the message text; the action is a button named by its label; the close control is a button named "Close".
- Focus: none moved on appearance. A user who triggers the action by keyboard gets focus returned to the element that had it ([[Popup]], focus return).
- Contrast: text and action at least 4.5 to 1; computed values in Tokens used. Focus ring 3 to 1 against `inverse_surface`.
- Timing: untimed or at least 4 s, paused on hover and focus ([WCAG 2.2.1](https://www.w3.org/TR/WCAG22/#timing-adjustable) offers a way to extend: the pause and the proposed Alt+Shift+N chord of [[ADR-0019 Banner and snackbar focus chords]]).
- Content that is the only record of an event is also kept elsewhere (a log), since the snackbar disappears.

## Dark and light

Roles only. `inverse_surface` is dark in light theme and light in dark theme, so the snackbar always contrasts with the page. High contrast adds a 1 dp `outline` stroke ([[Colour Roles]]).

## Defaults

Single or two lines per text; bottom, start-aligned; margin 16 dp; width 344 dp; duration 4000 ms (10000 ms with an action); no close control; polite status; one at a time with a queue of 5.

## Acceptance criteria

- [ ] AC-SNK-1 (token test): container `inverse_surface`, radius 4 dp, elevation level 3 (6 dp); text `body_medium` in `inverse_on_surface`; action `label_large` in `inverse_primary`; close icon 24 dp in `inverse_on_surface`. Pass: all are role and token references with these values.
- [ ] AC-SNK-2 (geometry check): at default, compact and dense a one-line snackbar is 48, 40 and 32 dp high and a two-line one 64, 56 and 48 dp; width at least 344 and at most 560 dp; text start 16 dp from the container edge; no padding literal outside {0, 2, 4, 8, 12, 16, 24, 32, 48} (AC-DEN-1). Pass: equal within 0.5 dp (the tess-ui text padding 14 fails).
- [ ] AC-SNK-3 (AT tree assertion): the node has role `status` (not `alert`), live `polite`, a name equal to the message, an action button named by its label, and a close button named "Close". Pass: all equal.
- [ ] AC-SNK-4 (scripted input): show a snackbar with text only; it disappears no earlier than 4000 ms and no later than 4000 ms plus 2 frames; with an action it stays 10000 ms; with duration 0 and a close control it stays until closed; with duration 0 and no close control the call is refused. Pass: times equal.
- [ ] AC-SNK-5 (scripted input): hover the pointer over the snackbar at 3 s and keep it there for 10 s: it is still shown; move the pointer away: it closes after the full duration again. The same with keyboard focus inside it. Pass: shown at each check and closed on time.
- [ ] AC-SNK-6 (scripted input): queue three messages in one loop turn: exactly one snackbar node exists at every frame; they show in call order; the gap between one closing and the next showing is at most 100 ms; a fourth with the id of the second replaces it in place. Pass: visible count at most 1 on each frame and order equal.
- [ ] AC-SNK-7 (scripted input): queue 7 messages without actions: the queue length is at most 5 after the call and the dropped ones are the oldest. Pass: lengths and order equal.
- [ ] AC-SNK-8 (scripted input): the action runs once on a pointer click and once on Enter or Space when it has focus; the snackbar closes after it; a second activation does nothing. Pass: handler count 1.
- [ ] AC-SNK-9 (scripted input): with a snackbar with action visible and focus in a text field, typing continues to reach the field (the snackbar took no focus); Tab reaches the action as the last stop; the chord Alt+Shift+N (proposed default, [[ADR-0019 Banner and snackbar focus chords]]) moves focus to the action; Escape dismisses it and returns focus to the text field. Pass: focus owner equals at each step.
- [ ] AC-SNK-10 (pixel check): the snackbar rectangle never overlaps the keyboard-focused control: place focus on a field under the snackbar; within 2 frames the snackbar is moved above it or hidden. Pass: bounds do not intersect.
- [ ] AC-SNK-11 (scripted input): the announce queue holds exactly one polite entry per displayed message, none on timeout, none assertive; queued messages announce when they appear and not when they are queued. Pass: counts and politeness equal.
- [ ] AC-SNK-12 (contrast script): text and action against the container at least 4.5 to 1, the focus ring against the container at least 3 to 1, in light, dark and high contrast. Pass: no ratio below the limit.
- [ ] AC-SNK-13 (scripted input): with reduced motion on the snackbar is present on the first frame after show and absent on the first frame after close; with it off the enter takes 250 ms (within 2 frames). Pass: frame counts equal.
- [ ] AC-SNK-14 (pixel check): a press on window content outside the snackbar reaches the content and leaves the snackbar open; a window narrower than 344 dp plus margins gives a snackbar of window width minus twice the margin. Pass: handler fired on content, snackbar still present, width equal.
- [ ] AC-SNK-15 (review): a project that adopts Alt+Shift+N has run the collision check against the shell's shortcut map and each application's own map and records the result and any replacement chord ([[ADR-0019 Banner and snackbar focus chords]]). Pass: the record exists and lists no collision, or names the replacement.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Snackbar_View.tdl`, `tess-ui:src/tess_ui/views/SnackbarHost_View.tdl`, `tess-ui:src/tess_ui/views/Snackbar_Stylesheet.tdl`, `tess-ui:src/tess_ui/overlays.py`, `tess-ui:docs/components/snackbars.md` | partly meets: `inverse_surface`, 4 dp radius, elevation 3, 344 to 560 dp wide, 48 dp minimum height, non-modal, takes no focus, `Duration` default 4000 with 0 as untimed and pointer hold, one at a time through `SnackbarHost` with a queue (AC-SNK-1, AC-SNK-6 partly, AC-SNK-14 meet by reading, unrun); fails AC-SNK-2 (no density levels, text padding 14), AC-SNK-3 (role `alert` with live polite), AC-SNK-4 (action default is 4000, not 10000; untimed without a close control allowed), AC-SNK-5 (focus does not pause: no focus enters), AC-SNK-7, AC-SNK-9 (no keyboard path to the action while it takes no focus), AC-SNK-10, AC-SNK-13 (no enter or exit animation specified in the view); swipe to dismiss and lift above a FAB are not built; action hit area is 8 dp padding around the label, so AC-DEN-7 is unmeasured |
| tess-shell | none (no snackbar or toast; notification server is outside v1, `tess-shell:docs/design/10 Vision/V1 Scope.md`) | absent |
| tre | `tre:docs/guide/layers.md` (Tooltips and snackbars), `tre:docs/reference/layers.md` | not applicable as a component: the engine provides a non-dismissible layer, `live` and `window.announce`; the toolkit owns the timer |

Evidence: [[Gaps and Contradictions]] (snackbar: swipe to dismiss, lift above FAB; off-grid padding 14).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Snackbar_View.tdl`, `SnackbarHost_View.tdl` | exists |
| tre | `tre:docs/guide/layers.md` | mechanism only |
| tess-shell | none | absent; OSD is [[Volume OSD|On-Screen Display]] |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Duration 4000 ms, 10000 ms with an action (Android presets 1500 and 2750 ms) | desktop reading time and WCAG 2.2.1; figures from Compose Material 3 | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Messages queue (Android replaces the visible snackbar) | a result must not be lost | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights 48, 40, 32 and two lines 64, 56, 48 (MD3 48 and 68) | density levels; padding on the 4 dp grid | [[ADR-0002 Desktop density levels and target sizes]] |
| Keyboard path: last Tab stops and `Alt+Shift+N` (proposed default) | desktop keyboard-first; MD3 describes touch | [[ADR-0019 Banner and snackbar focus chords]] |
| Role `status` with polite live region, never assertive | assertive is reserved for what must be acted on | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Focus ring role `inverse_primary` on the snackbar (vault ring role is `secondary`) | `secondary` has too little contrast on `inverse_surface` #needs-verification | [[ADR-0009 State layer percentages]] |

## Sources

- [Material Web snackbar tokens (latest)](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-snackbar.scss): container `inverse-surface`, elevation `level3`, shape `corner-extra-small`, icon 24 px, single-line height 48 px, two-line 68 px, action `inverse-primary` `label-large`, state layer opacities from `md-sys-state`. Verified 2026-11-21.
- [Compose Material 3 `SnackbarHost.kt`](https://github.com/androidx/androidx/blob/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/SnackbarHost.kt): `Short` 4000 ms, `Long` 10000 ms, `Indefinite`; default `Short` without an action and `Indefinite` with one. Verified.
- [Material Components Android Snackbar](https://github.com/material-components/material-components-android/blob/master/docs/components/Snackbar.md): one at a time, swipe to dismiss, appears temporarily towards the bottom; `SnackbarManager.java` (1500 and 2750 ms); `BaseTransientBottomBar.java` (slide 250 ms, fade in 150 ms, fade out 75 ms).
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 2.1.1, 2.2.1, 2.4.11, 4.1.3; [WAI-ARIA 1.2 status](https://www.w3.org/TR/wai-aria-1.2/#status) and [alert](https://www.w3.org/TR/wai-aria-1.2/#alert).
- Code: `tess-ui:docs/components/snackbars.md`, `tre:docs/guide/accessibility.md` (live regions and `announce`).
- Not verified: the Material Design 3 page statements (4 to 10 s, width limits, long-action layout, placement above FABs); m3.material.io returns nothing to the tools.
