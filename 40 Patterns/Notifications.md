---
title: Notifications
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, notification, snackbar, banner]
related: ["[[40 Patterns]]", "[[Snackbar]]", "[[Banner]]", "[[Dialog]]", "[[Notification Window]]", "[[On-Screen Display]]", "[[Volume OSD]]", "[[Error States]]", "[[Loading States]]", "[[Validation]]", "[[Popup]]", "[[Button]]", "[[Motion]]", "[[Elevation]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[12 Overlays]]", "[[14 Accessibility Basics]]"]
---

# Notifications

> [!info] Summary
> How the interface tells the user something they did not just ask for: choose the surface (snackbar, banner, dialog, system notification, shell on-screen display) by urgency and persistence, queue messages, and announce them. The MD3 counterparts are the [snackbar](https://m3.material.io/components/snackbar/overview) and the dialog; the banner and system notification are Tesserae's.

## Problem

tess-ui has only `Snackbar` and `SnackbarHost`, not used by any app; the config app hand-builds a disk-change banner; the shell has a Volume OSD and no notification server (outside v1, shell ADR-0004); the engine has non-dismissible layers, `live` regions and `window.announce`, and no timer or queue ([[Gaps and Contradictions]], summary items 8 and 9 and "Notifications: Snackbar only").

## Purpose

Match the interruption to the message: the least intrusive surface that still reaches the user, never lost to a screen reader, never blocking more than the situation requires.

## When to use and not

- Use when: the app or the system reports an event the user did not just cause (a result, a background change, a warning).
- Do not use when: feedback to a typed value ([[Validation]]); the failure of what the user is looking at ([[Error States]], inline or region); progress ([[Loading States]]); a decision is required before continuing and only a [[Dialog]] fits.

## Rules

1. One surface per message by the decision table; the same event never appears on two surfaces.
2. A snackbar is transient, not modal, takes no focus, does not block input, and holds at most one message and one action; one is visible at a time and the rest queue (rule 5). Material Components Android: "Only one snackbar will be shown at a time. Showing a new snackbar will dismiss any previous ones first" (the Tesserae queue differs, see Deviations).
3. Duration (design choice, #needs-verification-as-design-choice): 4 s for text only (tess-ui default 4000 ms), 10 s with an action, never less than 1 s per 12 characters; the pointer over the snackbar or keyboard focus in it holds the timer; 0 keeps it until dismissed. The timer is the app's (`window.after`).
4. A banner persists until the user resolves or dismisses it, sits at the top of the content region it concerns (not the window), pushes content down and does not cover it, and offers at most two actions (the primary first).
5. Queue: first in, first out within one priority; an assertive message jumps the queue; messages with the same id within 2 s are merged; the queue holds 5, then drops the oldest low-priority message; the shell sends announcements through one window ([[14 Accessibility Basics]]).
6. Every notification is announced: a snackbar and a banner are live regions, polite by default; assertive only for what the user must act on (data loss, critical battery). A dialog takes focus and announces itself through its role.
7. Keyboard: the action and the close button of a snackbar are Tab stops reachable while it shows, and F6 reaches a banner and a persistent snackbar ([[Keyboard Navigation]]); the app may also bind a shortcut for the action (Ctrl+Z for Undo) and names it in the text. Escape is not defined for snackbars and banners: [[11 Interaction]] gives Escape one transient layer per press in a fixed order that has no snackbar step (record in the audit of that order). A transient message whose action cannot be reached by keyboard within its duration fails WCAG 2.2 SC 2.2.1 and is not allowed.
8. Position: snackbar at the bottom start of the window, 16 dp from the edges, above a bottom bar or FAB (tess-ui "Not built"); never over the focused control; a window of width below 600 dp centres it. A system notification and an on-screen display belong to the shell and are placed by the shell ([[Notification Window]], [[On-Screen Display]]).
9. A snackbar and a banner never carry the only copy of an outcome that the user must keep: the result is also in the document, a log or the status line.
10. Reduced motion: appearance by fade of at most 100 ms or none; no slide ([[Motion]]).
11. Colour: snackbar `inverse_surface` with `inverse_on_surface` text and `inverse_primary` action; banner `tertiary_container` or `error_container` with the matching `on_` role plus an icon (config app disk banner uses `tertiary_container`); dialogs per [[Dialog]].
12. System notifications (outside the app window) are only for events the user wants while the app is not in front; the app asks before using them. The shell OSD is transient (default 1500 ms in the shipped Volume OSD), takes no keyboard (`Keyboard: NONE`) and no pointer input (`Input_Region: []`).

## Decision table

| Message | Urgency | Persistence | Surface | Action | Live politeness |
|---|---|---|---|---|---|
| Saved, copied, applied | low | 4 s | [[Snackbar]] | Undo (optional) | polite |
| Operation failed, recoverable, not blocking | medium | 10 s with Retry | [[Snackbar]] | Retry | polite |
| File changed on disk, connection lost, sync paused | medium | until resolved | [[Banner]] | Reload, Keep mine | polite |
| About to lose data, critical battery | high | until answered | [[Dialog]] (modal) | confirm, cancel | assertive |
| Destructive action needs a decision | high | until answered | [[Dialog]] | confirm, cancel | role `alertdialog` |
| A system value changed by a key (volume, brightness) | low | 1.5 s | shell [[On-Screen Display]] | none | polite |
| Event while the app is not in front | per event | OS decides | system notification ([[Notification Window]]) | open | OS |
| Background refresh finished | none | none | no notification; `busy` only | none | none |

## Examples (short snippets only)

```tdl
SnackbarHost { Messages: <| toasts |>, Chosen: <| undo |> }
```

The config app banner: a `Container` with role `group`, an alert icon, a `Text` with `Live: assertive`, and Reload and Keep mine buttons (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, `disk_banner`). By the decision table a polite live region fits this banner unless unsaved changes would be lost; the file's unsaved-changes case justifies assertive.

## States

| State | Visual change | Token values |
|---|---|---|
| Entering | fade in, 100 ms at most | [[Motion]] |
| Shown | surface per rule 11, level 3 for snackbar (6 dp shadow in Android), no shadow for banner | [[Elevation]] |
| Held (pointer or focus inside) | timer paused, no visual change | none |
| Action pressed | closes and runs the action once | none |
| Dismissed | fade out, 100 ms at most, focus unchanged | [[Motion]] |
| Queued | not drawn, counted | none |

## Sizing and density

Snackbar: 344 to 560 dp wide, 48 dp high (68 dp for two lines), 4 dp corners, 16 dp margin (`tess-ui:docs/components/snackbars.md`); Material Components Android uses `shapeAppearanceCornerExtraSmall`, 6 dp elevation, 8 dp margin and body-medium text ([Snackbar docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Snackbar.md)). Snackbar height does not scale with density (the action button inside follows 40, 32, 28 dp but the container stays 48 dp at minimum). Banner: padding 8 dp, gap 8 dp, icon 18 dp, `body_small` text, action buttons at the density height; width follows the region.

## Accessibility

- Role: snackbar `status` (polite) or `alert`; banner `group` with a name; dialog `dialog` or `alertdialog` (modal).
- Announcement through the live region text or `window.announce(text, politeness)`; repeated identical text is announced again, so duplicates are removed by the sender ([[14 Accessibility Basics]]).
- A transient message gives users time: the minimum durations of rule 3, hold on focus, and the information is also in the document or log (rule 9).
- Focus is not moved by a snackbar or banner; a modal dialog moves and returns it.
- Contrast: text on the container 4.5 to 1; the action text 4.5 to 1 on `inverse_surface`.

## Acceptance criteria

- [ ] AC-NOT-1 (scripted input): two snackbars posted 100 ms apart show one at a time in posting order, and the second appears in the frame after the first closes. Pass: visible count 1 at every frame; order equals.
- [ ] AC-NOT-2 (scripted input): with a simulated clock a text-only snackbar closes at 4 s plus or minus one frame; one with an action closes at 10 s; with the pointer over it or focus inside it the close time does not advance. Pass: close times equal.
- [ ] AC-NOT-3 (scripted input): a banner stays until its action or dismiss is activated, however long the clock advances (tested to 600 s). Pass: still present.
- [ ] AC-NOT-4 (AT tree assertion): each notification is a live region (polite) or is announced once through `announce`; an assertive one exists only for the high-urgency rows. Pass: politeness equals the decision table; announcement count 1.
- [ ] AC-NOT-5 (scripted input): showing a snackbar or a banner leaves the focus owner unchanged; a modal dialog moves focus into itself and returns it to the opener on close. Pass: focus owners equal.
- [ ] AC-NOT-6 (geometry check): a snackbar is 344 to 560 dp wide, 48 dp high (68 dp with two lines), 16 dp from the window edge, and does not overlap the focused control or a bottom bar. Pass: bounds equal.
- [ ] AC-NOT-7 (scripted input): the action of a snackbar is reachable by Tab (F6) and Enter within its duration, and activation closes it once and runs the action once. Pass: counts equal.
- [ ] AC-NOT-8 (token test): snackbar roles `inverse_surface`, `inverse_on_surface`, `inverse_primary`; banner roles `tertiary_container` or `error_container` with matching `on_` roles; no literal. Pass: role references.
- [ ] AC-NOT-9 (scripted input): with `reduced_motion` true, appearance and dismissal complete within 1 frame or fade at most 100 ms. Pass: frame count at most 6 at 60 Hz.
- [ ] AC-NOT-10 (scripted input): 7 messages posted at once keep the queue at 5; the oldest low-priority is dropped; an assertive message posted last is shown next. Pass: order and count equal.
- [ ] AC-NOT-11 (review): each message in a view maps to one row of the decision table and its outcome is also in the document, a log or the status line.
- [ ] AC-NOT-12 (scripted input): the shell OSD takes no keyboard or pointer input (`Keyboard: NONE`, empty input region) and closes after its duration (1500 ms default). Pass: events pass through; close time equals.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Snackbar_View.tdl`, `SnackbarHost_View.tdl`, `tess-ui:src/tess_ui/overlays.py`, `tess-ui:docs/components/snackbars.md`, `Main_View.tdl` (`disk_banner`) | partly meets: `Snackbar` 4000 ms default, pointer holds time, action, close button, 344 to 560 wide, 48 high, 16 margin, `inverse_surface`, not modal, takes no focus, polite alert (AC-NOT-2 partly, AC-NOT-5, AC-NOT-6, AC-NOT-8 meet by reading); `SnackbarHost` queues without a limit or priority (AC-NOT-10 fails); action snackbar default 4 s (AC-NOT-2 fails); no keyboard path to a snackbar action (AC-NOT-7 fails); swipe and lift above FAB or bottom bar not built; no banner view, the config app builds one by hand and no app or example uses Snackbar |
| tess-shell | `tess-shell:src/tess_shell/shipped/Volume_OSD/Volume_OSD_Module.tdl`, `tess-shell:src/tess_shell/surfaces/panel.py` | partly meets: Volume OSD duration 1500 ms, `Input_Region: []`, `Keyboard: NONE` in the documented Panel (AC-NOT-12 by reading); no snackbar, banner or notification server (outside v1); announcements go through `Window.announce` in one window |
| tre | `tre:docs/guide/layers.md`, `tre:docs/guide/accessibility.md` (`announce`, `live`) | not applicable: non-dismissible layer plus `live`; timer and queue are the app's; `announce` queue holds 16 and keeps the newest |

Request candidates: tess-ui `Banner` view and a queue limit with priority in `SnackbarHost`; routed through the Orchestrator.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Queue with priority instead of replacing the previous snackbar | several results arrive in a desktop session; none may be lost | none; design choice |
| 10 s with an action; hold on focus | WCAG 2.2 SC 2.2.1; keyboard reaches the action | none; design choice |
| A banner as a first-class surface | MD3 removed the banner component from the current set #needs-verification; the config app needs it | none |
| Snackbar not density scaled | message reads at the same size at every density | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- [Material Components Android: Snackbar](https://github.com/material-components/material-components-android/blob/master/docs/components/Snackbar.md): transient, bottom, one at a time, optional action and close, `colorSurfaceInverse`, `shapeAppearanceCornerExtraSmall`, 6 dp elevation, 8 dp margin, `textAppearanceBodyMedium`, TalkBack reads the text. Verified 2026-11-21.
- [Material Components Android: Banner](https://github.com/material-components/material-components-android/blob/master/docs/components/Banner.md): "yet to be completed". The m3.material.io banner and snackbar duration guidance is unreadable by tools #needs-verification.
- [WCAG 2.2 SC 4.1.3 Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), [SC 2.2.1 Timing Adjustable](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html); [WAI-ARIA APG alert pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alert/), [alertdialog](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/).
- Durations 4 s and 10 s, queue limit 5 and the 2 s merge are design choices #needs-verification-as-design-choice.
- Code: `tess-ui:docs/components/snackbars.md`; `tre:docs/guide/accessibility.md`; `shell-vault:40 Specifications/Modules/Volume OSD Module.md`; `shell-vault:10 Vision/V1 Scope.md`; [[Gaps and Contradictions]].
