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

State as of 2026-11-22, synchronised with tre 0.6.11 on 2026-11-22. P13 (state layer hooks) and P14 (focus outline) of the tre audit are approved as UXREQ-010 and UXREQ-008. The component notes were written against tre 0.6.10; on tre 0.6.11 the `both` scroll view (PR 326) already takes `scrollbar_width`, `scrollbar_hit_width`, `scrollbar_margin`, `scrollbar_min_length`, `scrollbar_gutter`, `scrollbar_corner`, `scrollbar_fill` and the three opacities, with the specification defaults (thumb 8, hit 12, margin 2, minimum 32, rest 0.70, hover 0.80, drag 1.00, wheel 40). One-axis scroll views keep the legacy 4 px thumb until properties are set.

## tre

### Delivered in tre 0.6.11

Checked in the `v0.6.11` tag (PR titles, `docs/reference/properties.md`, `docs/api/python.md`); the property names below were found there. Delivery does not mean the vault criteria pass: each row still needs its audit.

| Hook | tre PR | Request | Unlocks |
|---|---|---|---|
| Two-axis `scroll_view` with the specified scrollbar | 326 | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] | AC-SCB-01 to AC-SCB-21 |
| Every scrollbar aspect is a property (`scrollbar_*`: radius, side, show policy, track, per-state colours, fade, arrows, lane click, steps, smooth scroll); `virtual_list` shares the scroll view scrollbar | 329 | UXREQ-001, [[UXREQ-002 Virtual list keys and scroll to index]] | AC-SCB-22 to AC-SCB-30 |
| `virtual_list` keys, `scroll_to_index`, `scroll_into_view` | 325 | UXREQ-002 | AC-SCB-14, [[List]], [[Tree]] |
| `hit_testable` on every node (text hit-testable by default); `vertical_align` on `text` and `text_input` | 327 | [[UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input]] | AC-TIP-1 for a label, F7, [[Text Field]] |
| `letter_spacing` and `line_height` on `text_input` (0.6.11) | consolidated in 337 | UXREQ-005 | AC-TYP-2, [[Text Field]] |
| `set_size` and `pos_in_set` (derived for `virtual_list`), `checked` mixed, `orientation`, `modal` and 18 more roles | 328 | [[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]], [[UXREQ-004 Accessibility roles]] | [[14 Accessibility Basics]], [[Accessibility Tree]] |
| `Window` and `App` `scheme` selects the baseline colours of every engine default (the dark-by-default and light-literal defaults are gone) | 330 | tre audit P4 | [[Colour Roles]], AC-COL-11 (98 of 98 roles match, `tools/compare_scheme.py`) |
| `set_defaults` declares the baseline look per node kind | 331 | tre audit P12 | [[Defaults Matrix]] defaults |
| Named easings everywhere an easing is taken; snap and fling timings are properties | 332 | tre audit P7 | [[Motion]], scroll snap |
| Terminal `escape_chord` (and `escape_chord_reverse`) leaves a focused terminal without sending the key to the shell | 333 | [[UXREQ-006 Terminal escape chord and history scrollbar]] (first half) | [[ADR-0018 Terminal escape chord]], [[Terminal]] |
| `Window(first_present=..., background=...)` and `window.ready()` hold the first present for windows | 334 | [[UXREQ-009 First frame hold]] (windows) | [[ADR-0005 Theme follows the system]] |
| `hover_layer`, `pressed_layer`, `focus_layer` (colour, opacity), `focus_layer_any_modality`, `state_layer_ms`, `state_layer_easing`: the engine draws and fades state layers | 335 | [[UXREQ-010 State layer hooks]] | [[State Layers]] (the 16 percent dragged layer is not covered: the engine has no drag state to follow) |
| `outline` and `focus_outline` draw a ring outside the box | 336 | [[UXREQ-008 Outline property for focus rings]] | [[Focus Ring]], AC-FOC-2, AC-FOC-5 |

### Still needed

| Hook | Today | Unlocks | Request |
|---|---|---|---|
| Terminal history scrollbar | not built (the wheel scrolls the history; `docs/guide/text.md` calls it a later item) | [[Terminal]] | UXREQ-006 (second half, open) |
| First-frame hold for layer and popup surfaces | windows only; layers follow in tre's `feat/first-present-layers` | [[ADR-0005 Theme follows the system]] | UXREQ-009 |
| Multi-click window 500 ms and 4 px as properties; a drag start distance property | hardcoded; no drag threshold (absent in the 0.6.11 tag) | [[11 Interaction]] double click and drag rules, [[Drag and Drop]] | to be filed (tess-re 0.6.12 list) |
| `selection_foreground`, `selection_radius` | absent in the 0.6.11 tag; `caret_width` is settable on `text_input` in tre | [[Text Selection]] | to be filed (tess-re 0.6.12 list); tess-re counts `caret_width` as a gap, which in 0.6.11 is a project-layer gap |
| Layer placement viewport margin and flip threshold; popup edge margin | absent in the 0.6.11 tag (margin 0, slack 0) | [[Anchored Placement]], [[Popup Window]] | to be filed (tess-re 0.6.12 list) |
| Per-state state layer timings | in progress in tre | [[State Layers]] | UXREQ-010 follow-up |
| Shadows on a path including holes | in progress in tre | [[Elevation]] for path shapes | tess-re 0.6.12 |
| Static text selection colour (`selection_fill` on `text`), terminal font family, line height, cursor shape and blink, bold weight, dim opacity, underline geometry | hardcoded in the audit; re-check against 0.6.11 | [[Text Selection]], [[Terminal]] | to be filed |
| Gesture thresholds (long press 500 ms, tap 300 ms, double tap 300 ms and 30 px, swipe 600 px/s and 40 px) | hardcoded except `touch_slop` | [[11 Interaction]] timings | to be filed |

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
