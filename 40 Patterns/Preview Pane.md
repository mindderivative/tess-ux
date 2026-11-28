---
title: Preview Pane
type: pattern
status: draft
owner: phil
created: 2026-11-27
updated: 2026-11-27
tags: [pattern, preview, accessibility]
related: ["[[40 Patterns]]", "[[Config App Layout]]", "[[Error States]]", "[[Colour Roles]]", "[[Accessibility Tree]]", "[[14 Accessibility Basics]]", "[[Keyboard Navigation]]"]
depends_on: ["[[Colour Roles]]", "[[14 Accessibility Basics]]"]
---

# Preview Pane

> [!info] Summary
> A Preview Pane shows a picture of something the user is editing (a shell, a theme, a layout) next to the editor, redrawn as the data changes. The picture is not a control: it takes no clicks and holds no focus, it is drawn with its own colour scheme, and assistive technology sees one region with a text alternative. Status in code: in progress (decided by the owner for the config app on 2026-11-27, [[Config App Layout]]; not built or re-checked). Material Design 3 has no preview pane.

## Problem

An editor of declarative data (a shell file) makes the user imagine the result. A live picture closes the loop, but a picture drawn with the application's own tokens misleads (the preview's theme is the edited data's, not the application's), a picture that answers clicks is mistaken for the real thing, and a picture that goes blank on a half-typed file hides the last thing the user could see.

## Purpose

One rule set for any pane that renders a model for looking only, so a project does not invent a different one per tool.

## When to use and not

- Use when: the user edits data whose result is visual and the result can be drawn from the data without running it.
- Do not use when: the picture must be operated (that is the real application, not a preview); the data has no visual result; a thumbnail in a list or dialog is enough ([[Icon Picker]], file preview in the File Dialog).

## Rules

1. Non-interactive. The preview takes no pointer input and no keyboard focus: no node inside it is a Tab stop, a pointer press on it does nothing, and it never starts a drag, a tooltip or a hover state. The pane itself is not a Tab stop of its own; it is reached by F6 only to let a user hear its description (rule 4) and shows the focus ring around the pane then ([[Focus Ring]], [[Keyboard Navigation]]).
2. Own colour scheme. The picture is drawn with the scheme of the edited data (the shell's theme), never with the application's scheme, and the application's scheme never leaks into it. The pane frame (border, padding, background around the picture) uses the application's roles. Switching the application between light and dark does not change the picture.
3. One region in the accessibility tree. The pane is one node with role `img` (or `group` named and described when the picture has several named parts), an accessible name ("Shell preview") and a description in words that summarises the picture ("Top bar with 3 modules, desktop with 2 panels"). The nodes inside the picture are hidden from assistive technology. The description changes when the picture changes, and a change is not announced unless the user asked for the preview ([[14 Accessibility Basics]]).
4. Stale and error state. When the data cannot be drawn (a syntax error, a missing file), the pane keeps the last good picture, dims it (the picture at 38 percent opacity, matching disabled content) and shows over it the message "Preview unavailable: see Problems" with an icon. The message is text, never colour alone. When there never was a good picture, the pane shows the message on the pane background. The description says "Preview unavailable" in that state. The message goes away in the first frame after a draw succeeds.
5. Debounce. A change to the data redraws the picture after 300 ms with no further change (the same debounce as selection announcements); a redraw in progress is replaced by the newer one, never queued. The redraw never blocks typing: the editor stays responsive while a draw runs.
6. Size. The picture scales to fit the pane (keeping aspect ratio) with no scrollbars unless the pane is told to show 1:1; the pane has a minimum size below which it shows the message "Make the pane larger to see the preview" instead of an unreadable picture.
7. Sync with the editor (selection in the data highlights the part in the picture, and the reverse) is not part of this version: the preview is a one-way picture. A later version adds it with its own criteria.
8. Reduced motion: a redraw replaces the picture in one frame with no cross-fade ([[Motion]]).

## States

| State | What the user sees | Description (AT) |
|---|---|---|
| Empty | message on the pane background: "Nothing to preview" | "Preview empty" |
| Current | the picture | the summary |
| Redrawing | the previous picture until the new one is ready | unchanged |
| Stale | last good picture dimmed with the message | "Preview unavailable" |
| Too small | the size message | "Preview too small" |

## Acceptance criteria

- [ ] AC-PRV-1 (scripted input): a pointer press, a wheel event and a key sent to the picture area change nothing (no event reaches the preview's content, no state changes); Tab never lands inside the picture. Pass: zero state changes and focus order unchanged.
- [ ] AC-PRV-2 (pixel check): with the application in light and in dark, the picture pixels at five sampled points are identical; the frame pixels follow the application's scheme. Pass: picture samples equal across schemes, frame samples differ.
- [ ] AC-PRV-3 (AT tree assertion): the pane is one node with role `img` or a described `group`, a non-empty name and a non-empty description; nodes inside the picture are hidden. Pass: node count of the pane subtree visible to AT is 1.
- [ ] AC-PRV-4 (scripted input): after a change that makes the data undrawable, the last good picture remains, dimmed to 38 percent, with the text "Preview unavailable: see Problems" over it, and the description reads "Preview unavailable"; fixing the data restores the picture and removes the message within one frame of the draw. Pass: states equal.
- [ ] AC-PRV-5 (scripted input): twenty changes 50 ms apart cause one redraw 300 ms after the last (on a fake clock); a change during a redraw cancels it and starts a new one; typing in the editor is never blocked (key to glyph within one frame during a draw). Pass: draw count 1 and timings equal.
- [ ] AC-PRV-6 (geometry check): the picture fits the pane keeping aspect ratio at three pane sizes with no scrollbar; below the minimum the size message shows. Pass: bounds equal.
- [ ] AC-PRV-7 (scripted input): with reduced motion on, a redraw changes the picture in one frame without a cross-fade. Pass: frame count 1.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | the config app View pane, in progress | not built, not re-checked |
| tess-shell | not applicable | not applicable |
| tre | not applicable | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | a live picture of edited data | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- WCAG 2.2 SC 1.1.1 Non-text Content (text alternative), SC 1.4.1 Use of Color, SC 4.1.2 Name, Role, Value.
- WAI-ARIA 1.2, role `img`.
- Owner decision for the config app, 2026-11-27, relayed by the Orchestrator (a decision, not a verified claim).
