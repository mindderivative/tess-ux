---
title: Hooks Needed
type: research
status: research
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [research, settable, tre, tess-ui, tess-shell, adr-0020]
related: ["[[Settable Properties Reference]]", "[[Defaults Matrix]]", "[[Scrollbar and Scroll Container]]"]
depends_on: []
---

# Hooks Needed

What each project must expose so that every default of the [[Defaults Matrix]] is settable from Python without touching the engine (ADR-0020, the owner principle that the engine never blocks the design). Collected from the `Settable` column of the component notes and from the tre audit of its own hardcoded visuals (tess-re, 2026-11-21, approved by the owner, being built for tre 0.6.11 with the specification values as defaults). Requests to tre are filed in `80 Requests`; requests to tess-ui and tess-shell go through the Orchestrator.

State as of 2026-11-22. P13 (state layer hooks) and P14 (focus outline) of the tre audit are approved as UXREQ-010 and UXREQ-008. The component notes were written against tre 0.6.10; on tre 0.6.11 the `both` scroll view (PR 326) already takes `scrollbar_width`, `scrollbar_hit_width`, `scrollbar_margin`, `scrollbar_min_length`, `scrollbar_gutter`, `scrollbar_corner`, `scrollbar_fill` and the three opacities, with the specification defaults (thumb 8, hit 12, margin 2, minimum 32, rest 0.70, hover 0.80, drag 1.00, wheel 40). One-axis scroll views keep the legacy 4 px thumb until properties are set.

## tre

| Hook | Today | Unlocks | Request |
|---|---|---|---|
| Scrollbar radius, track fill, per-state colours | hardcoded (pill on `both`, 2 px one-axis; no track) | AC-SCB-22, AC-SCB-23 | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] |
| Scrollbar side (vertical left or right, horizontal top or bottom, RTL), show policy, fade time and easing, arrow buttons, lane-click mode, page repeat timing | hardcoded | AC-SCB-26, AC-SCB-27, AC-SCB-28 | UXREQ-001 |
| Wheel notch, key line, page fraction, smooth scroll time | hardcoded (40 px, 40 px, 0.9, instant) | AC-SCB-24 | UXREQ-001, [[UXREQ-002 Virtual list keys and scroll to index]] |
| Virtual list takes every `scrollbar_*` property | rejected on non-scroll views | AC-SCB-22 to AC-SCB-30 for lists and trees | UXREQ-002 |
| Snap timing and curve (`snap_settle_ms`, `snap_duration_ms`, `snap_easing`); snap per axis on a `both` view | hardcoded 120 ms, 200 ms, bezier(0.2, 0, 0, 1); snap on the main axis only | scroll snap rules | UXREQ-001 |
| Fling constants | hardcoded (tau 0.35, stop 30, minimum 150) | touch scrolling feel | UXREQ-001 |
| Text nodes hit-testable (pointer enter, leave on plain text) | a plain `text` never claims a hit | AC-TIP-1 for a tooltip on a label | tre P2, approved |
| Static text selection colour (`selection_fill` on `text` as on `text_input`), terminal font family, line height, cursor shape and blink, bold weight, dim opacity, underline geometry, palette defaults | hardcoded | [[Text Selection]], [[Terminal]] | to be filed |
| Gesture thresholds (long press 500 ms, tap 300 ms, double tap 300 ms and 30 px, swipe 600 px/s and 40 px, multi-click 500 ms and 4 px) | hardcoded except `touch_slop` | [[11 Interaction]] timings | to be filed |
| Vertical alignment of text and text input, letter spacing and line height on `text_input` | missing | [[Text Field]], F7 | UXREQ-005 |
| Accessibility set size and position, mixed, orientation, modal; roles | missing | [[14 Accessibility Basics]] | UXREQ-003, UXREQ-004 |
| Terminal escape chord, history scrollbar | missing | [[Terminal]] | UXREQ-006 |
| Layer placement policy: viewport margin, flip threshold | hardcoded margin 0, slack 0 | [[Anchored Placement]] | to be filed |
| First-frame hold (the first present is deferred until the application is ready) | missing | ADR-0005 | UXREQ-009 (held) |
| Declarative state layers: colour, opacity per state (hover, focus, pressed, dragged), fade, shape, disabled scheme (tre audit P13) | tre draws none; tess-ui constants, tess-shell opacity literals | [[State Layers]], every control | [[UXREQ-010 State layer hooks]] (approved) |
| Outline outside the border box (width, offset, colour) for focus rings (tre audit P14) | `stroke_*` draws inside the box; the ring is a shadow with spread | [[Focus Ring]], AC-FOC-2, AC-FOC-5 | [[UXREQ-008 Outline property for focus rings]] (approved) |
| Default colours that follow a scheme (scrollbar `#CAC4D0`, text black, terminal palette) | light-scheme literals | dark by default | to be filed |

## tess-ui

| Hook | Today | Notes affected |
|---|---|---|
| Focus ring width and offset (`RING_WIDTH`, `RING_OFFSET`) | module constants | [[Focus Ring]] and every focusable control |
| State layer opacities, ripple timings, state layer size | module constants (`HOVERED` and the others, `PRESS_GROW_MS` and the others, `STATE_LAYER_SIZE`) | [[State Layers]] |
| Tooltip metrics: delay, width, padding, radius, font, elevation | literals in the tooltip code | [[Tooltip]] |
| Control widgets drawn in Python from class constants: Checkbox, Radio Button, Switch, Slider, Spin Box, Time Picker dial (sizes, borders, radii, state layer) | no stylesheet route | [[Checkbox]], [[Radio Button]], [[Switch]], [[Slider]], [[Spin Box]], [[Time Picker]] |
| Docking: handle span and grip, minimum zone and split, tab height and padding, close size, drop highlight width and alpha | module constants | [[Splitter]], [[Dock]], [[Dock Panel]] |
| Title bar: icon size, button width, glyph size | literals | [[Title Bar]] |
| Window frame: gap, corner radius | fixed root style | [[Window]] |
| Scrollbar thickness, margin, minimum length, hit slop, radius and the rest of the property set | only the colour is passed | [[Scrollbar and Scroll Container]] |
| Text field line height and letter spacing | popped before the engine call | [[Text Field]] |
| Progress indicator style keys, stop indicator, ring gap; snackbar inline minimums; image placeholder and error glyph; video player inline sizes; node graph style keys (title height, selected border, edge width, corner radius) | inline in views or fixed | [[Progress Indicator]], [[Snackbar]], [[Image]], [[Video Player]], [[Node Graph]] |
| Inline view styles that beat stylesheet rules (file dialog, colour picker, font list, icon picker, list editor row and gap) | inline `Style` in the shipped views | [[File Dialog]], [[Colour Picker]], [[Font List]], [[Icon Picker]], [[List Editor]] |
| Anchored layers: viewport margin, gap and offset, flip threshold; drag start distance; caret width, selection fill, selection text colour and radius | no key | [[Anchored Placement]], [[Drag and Drop]], [[Text Selection]] |

## tess-shell

| Hook | Today | Notes affected |
|---|---|---|
| `Letter_Spacing` on Text, Marquee and TextField (tracking of the type roles) | no key | every module with a type role |
| `Line_Height` on TextField | no key | [[Text Field]] |
| Bar `Padding`, `Border_Width`, `Border_Color`, `Corner_Radius`; Frame `Min_Height` per side, `Elevation` | not built | [[Bar]], [[Frame]] |
| Peek: handle size and radius, tab minimum size, handle minimum size | painter constants | [[Peek]] |
| Panel and Popup `Padding` and `Margin` | not built (routed through the content block) | [[Panel and Surface]], [[Popup]] |
| Panel and Frame `Min_Width`, `Min_Height`; Popup `Edge_Margin`; `Drag_Threshold` | no key | [[Layer Window]], [[Popup Window]], [[Drag and Drop]] |
| `Caret_Width`, `Selection_Fill`, `Selection_Foreground`, `Selection_Radius` | no key | [[Text Selection]] |
| `Elevation` and `Shadows` on Circle, Ring, Path, Bitmap; `Padding` on Path; SVG `Padding`, `Border_*`, `Corner_Radius`, `Elevation` | no key | [[Circle]], [[Ring Block]], [[Path Block]], [[Bitmap]], [[SVG]] |
| Scrollbar keys on ScrollBox (the box has no scrollbar) | none | [[ScrollBox]] |
| State layer key set (hover, focus, pressed percentages) | opacity changes only; adoption is OQ-23 | [[State Layers]] |
| Image placeholder size and themed error glyph | fixed in the module | [[Image]] |

Back to [[90 Research]].
