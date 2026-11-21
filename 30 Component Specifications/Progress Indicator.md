---
title: Progress Indicator
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, communication, progress]
related: ["[[Linear Progress Indicator]]", "[[Circular Progress Indicator]]", "[[Loading Indicator]]", "[[Progress Bar]]", "[[Loading States]]", "[[Notifications]]", "[[Button]]", "[[Snackbar]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Tooltip]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[Spacing and Density]]"]
---

# Progress Indicator

> [!info] Summary
> A read-only indicator of how far a process has come (determinate) or that it is still working (indeterminate), drawn as a line (linear) or a ring (circular). Counterpart: Material Design 3 [Progress indicators](https://m3.material.io/components/progress-indicators/overview). This note covers tess-ui `LinearProgress` and `CircularProgress` and the tess-shell `ProgressBar` module. Source of truth in code: see Status in code.

## Purpose

Show the user that work is under way and, when known, how much is done, so the user can wait, cancel or move on. It never takes input.

## When to use and not

- Use when: an operation takes longer than about 1 s and the user can do nothing useful meanwhile (determinate: the share is known, such as a download; indeterminate: it is not); a button or a region is busy ([[Loading States]]).
- Do not use when: the user sets a value (use a Slider, specified later); the value is a gauge, not progress (battery or volume level: a determinate bar may draw it, but its accessible role stays `meter`-like #needs-verification, see Accessibility); the wait is under 1 s (show nothing, see Rules); a message is needed (use [[Snackbar]] or [[Banner]]).

## Anatomy

1. Active indicator: the bar or the arc that fills (`primary`).
2. Track: the line or ring behind it (`surface_container_highest` for the bar; none for the ring unless the caller names a track role).
3. Stop indicator (linear, optional): a 4 dp dot at the end of the track.
4. Gap: 4 dp between the active indicator and the track in a ring with a track.
5. Label (accessible name only): never drawn; a percentage text beside the indicator is the caller's own text.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Linear determinate | a known share of a long task | bar fills from the start edge; value 0 to 1 |
| Linear indeterminate | an unknown wait over a wide region | a bar sweeps along the track; a 40 percent bar in the one-bar form |
| Circular determinate | a known share in a small space | arc from 12 o'clock clockwise |
| Circular indeterminate | an unknown wait in a small space or on a control | arc rotates and lengthens and shortens |
| Buffer (linear, optional) | media loading beyond the played part | a second bar at 38 percent opacity of `primary` behind the value |

Expressive shapes (wavy bars and rings, thick tracks, the morphing loading indicator) are not in the baseline of [[ADR-0006 MD3 baseline with named Expressive adoptions]]. tess-ui ships them (`Wavy`, `Thickness`, `LoadingIndicator`); using one needs a named adoption entry in [[Deviations from MD3]]. They are not graded here.

## States

A progress indicator has no hover, focus, pressed, selected or dragged state: it takes no focus and no pointer events.

| State | Visual change | Token values |
|---|---|---|
| Determinate | active indicator length or arc equals the value | `primary` on track |
| Indeterminate | moving indicator (or a still bar and arc under reduced motion) | `primary` on track |
| Complete (value 1) | full track; the caller removes the indicator or replaces it with the result | none |
| Disabled (owner is disabled) | active indicator `on_surface` at 38 percent, track `on_surface` at 12 percent | [[State Layers]] |
| Error (the task failed) | the indicator is removed and an error state shown; the indicator does not turn red | see [[Error States]] |

## Tokens used

Colour: `primary` (active indicator and stop indicator), `surface_container_highest` (linear track; Material Web latest). Shape: `full` for the active indicator's ends and the track (Material Web latest sets `corner-none` for the baseline linear and circular tokens and `corner-full` for the newer progress-indicator tokens; Tesserae uses `full`, a rounded end, as the 2023 specification does #needs-verification). Motion: determinate change `medium1` (250 ms) with `standard`; indeterminate cycles in the table of Motion. See [[Colour Roles]], [[Shape]], [[Motion]].

| Token | Value | Source |
|---|---|---|
| `md.comp.linear-progress-indicator.active-indicator-height` and `track-height` | 4 dp | [latest `_md-comp-linear-progress-indicator.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-linear-progress-indicator.scss) |
| `md.comp.progress-indicator.track-active-indicator-space` | 4 dp | [latest `_md-comp-progress-indicator-linear.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-progress-indicator-linear.scss) |
| `md.comp.progress-indicator.stop-indicator-size` | 4 dp | same |
| `md.comp.circular-progress-indicator.active-indicator-width` | 4 dp | [latest `_md-comp-circular-progress-indicator.scss`](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-circular-progress-indicator.scss) |
| `md.comp.circular-progress-indicator.size` | 40 dp | same |
| linear and circular colour | `primary`; linear track `surface_container_highest` | same |

## Sizing and density

The indicator itself is not a control, so its thickness is fixed. Its length (bar) and size (ring) scale with the density of what it sits in, so a spinner inside a button or a row fits.

| Level | Bar thickness | Bar default width | Ring size (diameter) | Ring stroke |
|---|---|---|---|---|
| default | 4 | 240 (or the width of its container) | 40 | 4 |
| compact | 4 | 240 | 24 | 3 |
| dense | 4 | 160 | 16 | 2 |

- Bar thickness 4 dp at every level (MD3 value); a thick 8 dp bar needs a named adoption (Expressive).
- The ring sizes for compact and dense are Tesserae design choices #needs-verification-as-design-choice: they let a ring sit inside a 32 or 28 dp button without changing its height ([[Button]], loading). A ring never exceeds the control's height minus 8 dp.
- The shell `ProgressBar` is 160 by 8 dp by default (a pill). MD3 has 4 dp; the shell keeps 8 dp because a 4 dp bar on a 1080p bar surface is hard to read #needs-verification-as-design-choice.
- The indicator has no hit area of its own; it is never a pointer target.

## Layout and overflow

- A bar fills the width its container gives it, or the caller's width; it never wraps and it keeps its thickness when the width shrinks. Minimum useful width 48 dp; below it the caller shows the ring.
- A ring keeps a square box; it is centred in the space given and never clipped by the box (stroke inside the box).
- A bar inside a row is vertically centred in the row; a ring beside text is centred on the text line box within 1 px (see [[10 Layout Overflow and Scrolling]]).
- Right-to-left: a linear bar fills from the end edge.
- A ring over content (a buffering ring on a picture) is centred on the content, and the content below does not shift.

## Behaviour

- Pointer, keyboard, touch: none. The indicator is hit-test transparent and not in the Tab order. A cancel action is a separate [[Button]] beside it.
- Value changes: determinate eases to the new value over 250 ms (`medium1`, `standard`); a value that goes backwards snaps (no reverse animation) so the bar never appears to unfill slowly.
- Switching from indeterminate to determinate settles to the determinate look without a jump larger than 1 px; the reverse restarts the sweep from the start.
- Show and hide rule (design choice #needs-verification-as-design-choice): an indicator that appears for an operation expected under 1 s is delayed by 300 ms and not shown if the operation ends first; once shown, it stays at least 500 ms so it does not flash.

## Tooltip and overlay behaviour

The indicator carries no tooltip ([[ADR-0004 Tooltip rule]]). A control that shows a ring in place of its icon keeps its own tooltip. The indicator opens no overlay.

## Motion

| Animation | Timing | Source |
|---|---|---|
| Determinate fill | 250 ms `medium1`, `standard` | tess-ui `controls.py` |
| Linear indeterminate sweep (one bar) | 1500 ms per crossing, `standard` | tess-ui (`SWEEP_MS`), MD3 value #needs-verification |
| Linear indeterminate two-bar sweep | 1900 ms per bar, second bar 650 ms behind | tess-ui (`TWO_BARS`), approximates MD3 #needs-verification |
| Circular indeterminate turn | 1568 ms per turn, arc length changes over 666 ms | tess-ui (`TURN_MS`, `ARC_MS`) |

Reduced motion. When the OS preference is on ([[Motion]], rule 4; [[14 Accessibility Basics]]), an indeterminate indicator is drawn still, with no movement: a linear bar is a bar of 40 percent of the track width, centred; a ring is an arc of 25 percent of the circle (90 degrees) at 12 o'clock. It stays exposed as busy. This note takes the stricter of the two options that [[Motion]] rule 4 permits (animation may continue when it is the only sign of activity): the baseline is still, because the busy state is also exposed to assistive technology and a moving element lasting over 5 s with no stop control fails [WCAG 2.2.2](https://www.w3.org/TR/WCAG22/#pause-stop-hide) unless the essential-activity exception applies. A project may keep the motion only by a named entry in [[Deviations from MD3]]. A determinate change under reduced motion draws the new value on the next frame.

The cycle never flashes more than 3 times a second ([WCAG 2.3.1](https://www.w3.org/TR/WCAG22/#three-flashes-or-below-threshold)).

## Accessibility

- Role: `progressbar` ([WAI-ARIA progressbar](https://www.w3.org/TR/wai-aria-1.2/#progressbar)), with `value_min`, `value_max` and `value` for determinate; text `value_text` as a percentage ("40%"). A gauge such as battery level is not progress: it uses the project's `meter` equivalent if the engine has one, else `progressbar` with the name stating the quantity ("Battery, 80%") #needs-verification.
- Indeterminate: no `value`; the node is `busy`; `value_text` is absent.
- Name: required (AC-PRG-6). The label states the process ("Downloading update"), never "progress". An indicator inside a busy button takes the button's name and sets the button `busy` ([[Button]]).
- Announcements: no announcement per tick; a determinate indicator is not a live region. The end of the process is announced once, politely, by the caller ([[Notifications]], [[Accessibility Rules]] AR-26). Assertive is never used for progress.
- Contrast: active indicator against the track and against the surface at least 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)). `primary` on `surface` is 6.1 to 1 in light (computed for this note from #6750A4 on #FEF7FF); the 38 percent buffer bar is decorative.
- Colour is not the only cue: the length or the motion carries the state.

## Dark and light

Roles only. The track `surface_container_highest` is lighter than the surface in dark and darker in light; the active indicator keeps at least 3 to 1 against the track in both. High contrast replaces the track fill with an `outline` stroke of 1 dp.

## Defaults

`primary`, track `surface_container_highest` for the bar and none for the ring, bar 4 dp by 240 dp, ring 40 dp with 4 dp stroke at `default` density (tess-ui ring box is 48 dp, see Deviations), stop indicator off, buffer off, indeterminate when no value is given, still under reduced motion.

## Acceptance criteria

- [ ] AC-PRG-1 (geometry check): at default density a linear indicator is 4 dp thick and a ring is 40 dp across with a 4 dp stroke; at compact the ring is 24 dp with a 3 dp stroke and at dense 16 dp with 2 dp (bar thickness stays 4). Pass: equal within 0.5 dp at scale 1.0 and 2.0 (tess-ui ring box 48 dp fails).
- [ ] AC-PRG-2 (pixel check): a determinate linear indicator at value 0.4 in a 240 dp track paints the active bar 96 dp long (within 1 px) from the start edge with rounded ends, the track behind in `surface_container_highest`; value 0 paints no bar and value 1 paints the full track length. Pass: edge columns equal.
- [ ] AC-PRG-3 (pixel check): a determinate ring at value 0.25 paints an arc from 12 o'clock to 3 o'clock; with a track, the gap between the arc end and the track start is 4 dp. Pass: sampled angles within 3 degrees; gap within 1 px.
- [ ] AC-PRG-4 (scripted input): set the value 0.2, then 0.8: the painted length reaches 0.8 no earlier than 250 ms and no later than 250 ms plus 2 frames; set 0.8, then 0.3: the bar reaches 0.3 on the next frame. Pass: frame times equal.
- [ ] AC-PRG-5 (scripted input): with reduced motion on, an indeterminate bar and ring are drawn still: two frames 500 ms apart are pixel-identical, the bar is 40 percent of the track and centred, the ring arc is 90 degrees at 12 o'clock. With reduced motion off the frames differ. Pass: frame diff 0 and nonzero respectively.
- [ ] AC-PRG-6 (AT tree assertion): determinate: role `progressbar`, non-empty name, `value_min` 0, `value_max` 1 (or the project range), `value` equal to the value, `value_text` "40%" for 0.4, not busy. Indeterminate: role `progressbar`, non-empty name, busy true, no value. Pass: all equal.
- [ ] AC-PRG-7 (scripted input): a value change produces zero announcements; the end of the process produces exactly one polite announcement from the caller. Pass: the announce queue length equals 0 during, 1 after.
- [ ] AC-PRG-8 (contrast script): `primary` against `surface_container_highest`, and against `surface`, at least 3 to 1 in light, dark and high contrast. Pass: no ratio below 3.
- [ ] AC-PRG-9 (scripted input): a pointer press and the Tab key pass through the indicator: it takes no focus, no event handler runs, and the element beneath receives the press. Pass: the Tab sequence excludes it and the lower element's event count is 1.
- [ ] AC-PRG-10 (scripted input): an operation that ends within 200 ms shows no indicator; one that runs 3 s shows it from 300 ms (within 2 frames) and keeps it at least 500 ms after it was shown. Pass: visibility times equal.
- [ ] AC-PRG-11 (token test): the shell `ProgressBar` track and fill use role colours `surface_container_highest` and `primary` (no `outline` for the track), the fill width equals clamp((value minus min) over (max minus min), 0, 1) of the track width and stays inside the track. Pass: values equal; fill at most the track width for any input.
- [ ] AC-PRG-12 (scripted input): switching from indeterminate to determinate and back leaves no frame in which the bar exceeds the track or jumps by more than 1 px. Pass: max frame-to-frame jump at most 1 px apart from the intended motion.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`Indicator`, `LinearProgress`, `CircularProgress`, `LoadingIndicator`), `tess-ui:src/tess_ui/widgets/progress.py`, `tess-ui:docs/components/progress-indicators.md` | partly meets: bar 4 dp with `surface_container_highest` track and `primary`, ring 4 dp stroke, determinate eases over `medium1`, role `progressbar` with `value_text` percent and `busy` for no value, reduced motion gives a still 40 percent bar and a still arc (AC-PRG-2, AC-PRG-4, AC-PRG-5 bar, AC-PRG-6 meet by reading, unrun); the ring box is 48 dp and has no density scaling (AC-PRG-1 fails); no delay-to-show rule (AC-PRG-10 fails); the reduced-motion ring arc length is not specified in code (AC-PRG-5 ring unmeasured); the wave and thickness amplitudes are written from memory of the spec per the code comment and `Wavy` is not graded |
| tess-shell | `tess-shell:src/tess_shell/shipped/ProgressBar/ProgressBar_Module.tdl`, `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl` | partly meets: determinate linear only, 160 by 8 pill, role PROGRESSBAR with `value`, `value_min`, `value_max`, fill eases with the medium duration and not under reduced motion (AC-PRG-4 meets by reading, AC-PRG-6 meets for determinate); the track is `$color.outline`, not `surface_container_highest` (AC-PRG-11 fails); no indeterminate, no ring (AC-PRG-5, AC-PRG-6 indeterminate, AC-PRG-1 ring: absent); no `value_text`; the label is the caller's |
| tre | `tre:docs/reference/node.md` (`busy`), `tre:crates/engine-core` path trim animation (`tre:docs/guide/animation.md`) | not applicable: the engine has no progress node; it provides `progressbar` role, `value`, `busy`, path trim and animation |

Evidence: [[Gaps and Contradictions]] (no indeterminate or circular progress in the shell; ProgressBar indeterminate not in v1).

## Source of truth in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`LinearProgress`, `CircularProgress`) | exists |
| tess-ui | `tess-ui:src/tess_ui/controls.py` (`LoadingIndicator`) | exists; Expressive, not graded |
| tess-shell | `tess-shell:src/tess_shell/shipped/ProgressBar/ProgressBar_Module.tdl` | partial: linear determinate only |
| tre | path node with `trim_start` and `trim_end`, `tre:docs/guide/animation.md` | mechanism only |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Ring sizes 24 dp (compact) and 16 dp (dense) | a ring inside a 32 or 28 dp control must fit without changing its height | [[ADR-0002 Desktop density levels and target sizes]] |
| Shell `ProgressBar` default 8 dp thick (MD3 4 dp) | legibility on a shell bar; kept as a shell choice #needs-verification | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Indeterminate indicators are still under reduced motion | the busy state is also exposed to assistive technology; the baseline takes the stricter rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Delay-to-show 300 ms and minimum visible time 500 ms | avoids flashing indicators on short operations on a desktop | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Expressive wavy, thick and morphing variants excluded | baseline is the 2022 system; adoption by name only | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| tess-ui ring box 48 dp (Material Web latest and Android: 40 dp) | the older MD3 spec size; the vault takes the latest token value | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- [Material Web linear progress tokens (latest)](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-linear-progress-indicator.scss): active indicator height 4 px, track height 4 px, colours `primary`, `surface-container-highest`, shapes `corner-none`. Verified 2026-11-21.
- [Material Web circular progress tokens (latest)](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-circular-progress-indicator.scss): width 4 px, size 40 px. [progress-indicator-linear](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-progress-indicator-linear.scss): track and active indicator space 4 px, stop indicator 4 px, thick 8 px, wave amplitude 3 px and wavelength 40 px (Expressive). [progress-indicator](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-progress-indicator.scss): track colour `secondary-container`, shapes `corner-full` (a newer set that conflicts with the linear and circular files: #needs-verification).
- [Material Components Android progress indicators](https://github.com/material-components/material-components-android/blob/master/docs/components/ProgressIndicator.md): track thickness 4 dp, gap 4 dp, spinner size 40 dp, `showDelay`, corner radius 50 percent.
- [WAI-ARIA 1.2 progressbar](https://www.w3.org/TR/wai-aria-1.2/#progressbar); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.2.2, 2.3.1, 4.1.3.
- The 38 percent buffer opacity (alpha 96 of 255 is 0.376) and the 1500, 1900 and 1568 ms cycles are tess-ui values; the m3.material.io page could not be fetched #needs-verification.
