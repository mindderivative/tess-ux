---
title: Adoption tre
type: adoption
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adoption, tre, engine]
related: ["[[70 Adoption]]", "[[Audit Template]]", "[[17 Conformance]]", "[[Test Method]]", "[[80 Requests]]", "[[UXREQ-001 Two-axis scroll view with the specified scrollbar]]", "[[UXREQ-002 Virtual list keys and scroll to index]]", "[[Scrollbar and Scroll Container]]", "[[Accessibility Tree]]", "[[Terminal]]", "[[Drag and Drop]]", "[[Adoption Libraries]]"]
depends_on: ["[[17 Conformance]]", "[[Test Method]]"]
---

# Adoption tre

> [!info] Summary
> What the engine tre (tess-re) must still provide for the specification, read from every `tre` row of the "Status in code" tables and checked against tre `origin/main` at commit `d7e6941a` (the tag `v0.6.10` plus four commits: CI, documentation and an AT-SPI naming fix). 17 findings remain open (TRE-001 to TRE-017), grouped into 8 candidate requests (2 already approved as UXREQ-001 and UXREQ-002; the Wayland file drop is external and has none); 5 items of the review list are dropped as fixed, by design or not an engine matter. This is a reading of source and documentation; no test was run and no acceptance criterion is recorded as `pass` or `fail` by this note. The audit proper follows [[Audit Template]].

## Method

1. Every `tre` row of every component, pattern, foundation and chapter note was read (about 160 rows). Rows that say "not applicable by design" or "mechanism only" with no failing criterion are not findings: the engine is a renderer, and tokens, state layers, components and roles of colour belong to the toolkit ([[Colour Roles]], [[State Layers]]).
2. Each claim in a row that names a missing engine property was checked against `tre:` source and documentation at `origin/main` (`git show origin/main:<path>`, search for the symbol or constant). Constants: `tre:crates/engine-core/src/node.rs` (`SCROLLBAR_THICKNESS` 4, `SCROLLBAR_MARGIN` 2, `SCROLLBAR_MIN_LENGTH` 32, `SCROLLBAR_GRAB_SLOP` 6), `tre:crates/engine-core/src/tree/scroll.rs` (`KEY_SCROLL_LINE` 40, `scroll_by_key`, `scroll_view_for_key`, `scroll_into_view`), `tre:crates/engine-core/src/tree/dispatch.rs` (wheel `y * 20.0`), `tre:crates/engine-render/src/lib.rs` (`DEFAULT_SCROLLBAR_FILL` `#CAC4D0` alpha `0x8C`, 55 percent), `tre:crates/engine-py/src/node_props.rs` (`ROLES`, 24 entries).
3. Findings are grouped so that each group can become one request note in [[80 Requests]] with one owner (tess-re) and one consumer test.

Severity (this note only):

| Severity | Meaning |
|---|---|
| high | a MUST criterion cannot pass in any project without engine work, or a WCAG 2.2 failure follows (keyboard trap, no keyboard path, no AT information) |
| medium | the criterion fails today; the toolkit can approximate it with application code, at a cost or with a known gap |
| low | a SHOULD criterion, a documented fallback exists (the criterion names it), or the effect is cosmetic |

## Open findings

| ID | Severity | Finding (verified at `d7e6941a`) | Failing AC ids | Evidence path | Suggested fix | Spec note | UXREQ |
|---|---|---|---|---|---|---|---|
| TRE-001 | high | `scroll_view` scrolls along one `orientation` (`vertical` or `horizontal`); a second axis needs a nested view, which splits wheel, key and scroll-into-view handling. No view shows two thumbs. | AC-SCB-03, AC-SCB-04, AC-SCB-18, AC-LST-08 | `tre:crates/engine-core/src/tree/scroll.rs`, `tre:docs/guide/nodes-and-layout.md` (Scrolling), `tre:docs/reference/properties.md` (`orientation`) | orientation `both`, per-axis offsets and per-axis overflow | [[Scrollbar and Scroll Container]] | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] |
| TRE-002 | medium | Thumb thickness 4 px (spec 8 dp), radius 2, fill `#CAC4D0` at fixed alpha 0x8C (about 0.55; spec 0.70 rest, 0.80 hover, 1.00 dragged); no per-view setting of thickness, margin or colour; no hover or drag opacity. Grab slop is 6 px around a 4 px thumb (a press 8 px from the centre grabs; AC-SCB-06 wants 6 grabs and 8 does not) #needs-verification by test. | AC-SCB-01, AC-SCB-06, AC-SCB-08, AC-SCB-09 | `tre:crates/engine-core/src/node.rs` (constants), `tre:crates/engine-render/src/lib.rs` (`DEFAULT_SCROLLBAR_FILL`) | scrollbar properties per view (thickness, hit thickness, thumb colour, three opacities) with the stated defaults | [[Scrollbar and Scroll Container]] | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] |
| TRE-003 | medium | The thumb overlays content; no 12 dp gutter is reserved at the end edge of an overflowing axis and no corner square exists (search of `scroll.rs` and `node.rs` finds neither). | AC-SCB-04, AC-SCB-16, AC-SCB-15 | `tre:crates/engine-core/src/tree/scroll.rs`, `tre:crates/engine-core/src/node.rs` | reserved gutter per overflowing axis and an empty corner | [[Scrollbar and Scroll Container]] | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] |
| TRE-004 | medium | A wheel notch moves 20 px (two sites: `y * 20.0`, `x * 20.0`; Python binding `WHEEL_LINE_PX` 20); spec 40 dp. Shift plus wheel does not map to the horizontal axis (a horizontal view reads only the `x` delta). Passing the wheel to the parent at an end is met (`can_scroll`). | AC-SCB-11 | `tre:crates/engine-core/src/tree/dispatch.rs` (Scroll arm), `tre:crates/engine-py/src/listeners.rs` | wheel step 40; Shift plus wheel swaps axis | [[Scrollbar and Scroll Container]] | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] |
| TRE-005 | medium | Page Up and Page Down move a full viewport (`now - viewport`); spec viewport minus 10 percent. Arrow line 40 and Home and End are met. | AC-SCB-10, AC-LST-03 | `tre:crates/engine-core/src/tree/scroll.rs` (`scroll_by_key`) | page = viewport minus 10 percent | [[Scrollbar and Scroll Container]] | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] |
| TRE-006 | medium | A press on the lane outside the thumb does nothing (no lane click or page toward the press in `scroll.rs` or `dispatch.rs`). | AC-SCB-13 | `tre:crates/engine-core/src/tree/dispatch.rs`, `tre:crates/engine-core/src/tree/scroll.rs` | page toward the press, stop at the thumb | [[Scrollbar and Scroll Container]] | [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] |
| TRE-007 | high | A focused `virtual_list` handles no keys: `scroll_view_for_key` and `scroll_by_key` match `NodeKind::ScrollView` only. Home, End, Page and arrows do nothing; the wheel and the thumb drag work. | AC-SCB-14, AC-LST-03, AC-LST-07, AC-LAY-11 | `tre:crates/engine-core/src/tree/scroll.rs`, `tre:crates/engine-core/src/tree/dispatch.rs` | key handling with the step values of TRE-004 and TRE-005 | [[List]], [[Tree]], [[Scrollbar and Scroll Container]] | [[UXREQ-002 Virtual list keys and scroll to index]] |
| TRE-008 | high | `scroll_into_view` filters ancestors to `NodeKind::ScrollView`; a `virtual_list` is skipped, so focus (`focus.rs` calls it) and an AT scroll request do not bring a materialised row inside; there is no `scroll_to_index`, so an unmaterialised row cannot be reached. | AC-SCB-14, AC-SCB-19, AC-LST-07, AC-LAY-14, AC-FOC-8, AC-AXT-8 (virtual rows) | `tre:crates/engine-core/src/tree/scroll.rs` (`scroll_into_view`), `tre:crates/engine-core/src/tree/focus.rs` | `scroll_to_index(i, align)`; `scroll_into_view` for materialised rows | [[List]], [[Tree]], [[Accessibility Tree]] | [[UXREQ-002 Virtual list keys and scroll to index]] |
| TRE-009 | high | No set size and no position in set on any node (the access state has `expanded`, `level`, `current`, `selected`, `pressed`, `checked`; no such property). Rows of a virtual list, radios, tabs and carousel items cannot report "2 of 5"; with virtualisation only the engine knows the full count. | AC-AXT-13, AC-LAY-13, AC-RAD-7, AC-CRS-9, AC-LST-07 | `tre:crates/engine-core/src/access.rs`, `tre:crates/engine-py/src/node_props.rs`, `tre:docs/reference/node.md` | `set_size` and `pos_in_set` properties; a virtual list derives both from `item_count` and the row index | [[Accessibility Tree]], [[List]], [[Radio Button]] | proposed (UXREQ-003) |
| TRE-010 | medium | `checked` takes bool or none; no `mixed`. The `pressed` property takes `"mixed"` for a toggle button only, and wins over `checked` where both are set. No `orientation` for a slider (a vertical slider cannot say so). No modal flag (`aria-modal` equivalent) on a dialog. | AC-CHK-8, AC-SLD-12, AC-DTP-8 | `tre:docs/reference/node.md` (`checked`, `pressed`), `tre:crates/engine-core/src/access.rs` | `checked="mixed"`; `orientation` for ranges; `modal` flag mapped to the platform | [[Checkbox]], [[Slider]], [[Date Picker]] | proposed (UXREQ-003) |
| TRE-011 | medium | The role vocabulary is 24 names (`button`, `checkbox`, `radio`, `switch`, `slider`, `progressbar`, `link`, `textbox`, `tab`, `tablist`, `tabpanel`, `menu`, `menuitem`, `dialog`, `alert`, `list`, `listitem`, `tree`, `treeitem`, `heading`, `img`, `group`, `none`, `separator`). Missing and named by an AC: `radiogroup`, `option` and `listbox`, `toolbar`, `navigation`, `complementary`, `region`, `status`, `grid`, `row`, `gridcell`, `columnheader`. Each of these criteria names a fallback (`group`, `list`) except `radiogroup`, `option` and the date grid. | AC-RAD-7, AC-LST-01, AC-DTP-8, AC-TLB-8, AC-NRL-9, AC-NDR-12, AC-SSH-10, AC-STB-9 | `tre:crates/engine-py/src/node_props.rs` (`ROLES`) | add the roles (AccessKit has all of them) | [[Accessibility Tree]] | proposed (UXREQ-004) |
| TRE-012 | medium | `text` has no vertical alignment: the text draws at the top of its box, so single-line text centring is the caller's padding arithmetic; `text_input` has no vertical alignment property either. | AC-TXT-5, AC-TXF-1, AC-TXF-2, AC-C03-3, AC-TLB-2 | `tre:docs/reference/properties.md` (Text), `tre:docs/guide/text.md` | `vertical_align` (start, centre, end) for `text` and `text_input`, centring the line box in the content box | [[Text]], [[Text Field]], [[03 Typography and Text Rules]] | proposed (UXREQ-005) |
| TRE-013 | low | `letter_spacing` and `line_height` exist on `text` only, not on `text_input`, so the tracking of AC-TYP-2 cannot be met for inputs (the AC allows a recorded deviation for a kind that cannot apply it). | AC-TYP-2 | `tre:docs/reference/properties.md`, `tre:docs/guide/text.md` | the two properties on `text_input` | [[Typography]] | proposed (UXREQ-005) |
| TRE-014 | high | A focused `terminal` takes every key; no escape chord leaves it, a keyboard trap (WCAG 2.1.2). Ctrl+Shift+C copy is met. [[ADR-0018 Terminal escape chord]] reserves Ctrl+Shift+Escape (a project may change it). The terminal has no scrollbar (the wheel and history work). | AC-BLK-TRM-3, AC-SCB-02 (terminal) | `tre:docs/guide/text.md` (Terminal), `tre:crates/engine-py/src/terminal.rs` | a settable chord, reserved before the program receives keys, that moves focus to the next focusable node and is not sent to the shell; optional scrollbar over the history | [[Terminal]], [[ADR-0018 Terminal escape chord]] | proposed (UXREQ-006) |
| TRE-015 | medium | No drag session: `capture_pointer` and the docking drag exist, but nothing cancels a drag on Escape (the docking guide cancels only on `undock_panel`), and nothing scrolls a scroll view at its edge during a drag. Both are app code today; whether a captured pointer receives `key_down` is not documented #needs-verification. | AC-DND-4, AC-DND-7, AC-DND-9 | `tre:docs/guide/events-and-input.md`, `tre:docs/guide/docking.md` | an Escape cancel for a captured pointer and dock drags (`pointer_cancel`), and an opt-in edge auto-scroll with the 8 to 32 dp per frame band of the AC | [[Drag and Drop]], [[Drag and Drop Pattern]] | proposed (UXREQ-007) |
| TRE-016 | medium | OS file drag and drop does not work on Wayland (winit 0.30.13 does not implement it); `file_hover`, `file_drop` and `file_hover_cancel` never fire; `simulate` fires them. X11 may report no pointer position. The AC accepts an Open command as the Wayland equivalent. | AC-DNP-11, AC-DND-4 (file) | `tre:docs/guide/events-and-input.md` (Files dragged from the OS), `tre:crates/engine-platform/Cargo.toml` | wait for a winit release (upstream), or the portal route; the toolkit keeps an Open command | [[Drag and Drop]], [[Drag and Drop Pattern]] | none (external; see Questions) |
| TRE-017 | low | No outline outside the border box: `stroke_color` and `stroke_width` draw inside the box, so a focus ring of 3 dp at a 2 dp offset (transparent gap) has to be a shadow with spread (which fills the gap with an opaque colour) or an extra node, and a ring is cut by `clip_children` of an ancestor. | AC-FOC-2, AC-FOC-5, AC-BLK-TRM-7, AC-SCB-15 | `tre:docs/guide/painting.md` (strokes inside, shadows with spread) | an `outline` property (width, offset, colour) following the corner radius, drawn outside the box | [[Focus Ring]] | proposed (UXREQ-008) |

## Dropped from the review list

| Item | Why dropped | Evidence |
|---|---|---|
| Tooltip timers absent | the engine has timers: `window.after(ms, fn)` and `window.every(ms, fn)` return a handle; the specification of the delay (500 ms) and the grace (150 ms, [[ADR-0011 Tooltip hover grace for all tooltips]]) is toolkit code with them. The statement "no timer primitive" in [[Clock Module]] and [[Tooltip]] is wrong; the owners of those notes correct it (not done by this note). The tooltip itself (hover rules, placement, content) stays the toolkit's by design. | `tre:docs/reference/window.md` (timers), `tre:docs/guide/layers.md` (Tooltips and snackbars) |
| Scrim | by design: a modal layer blocks input and draws nothing; the scrim is a window-sized `box` in the layer, as the guide shows (fill `(0,0,0,82)` is the example, the specified value is `scrim` at 0.32). AC-SCR-1 to AC-SCR-8 are toolkit criteria. | `tre:docs/guide/layers.md` (Building one), `tre:docs/reference/layers.md` |
| Popup window limits | platform facts, not gaps: the size is fixed for the popup's life, only `input_region` can be changed through `set`, a keyboard-exclusive panel cannot be a popup, and the grab-popup click-away recipe is sway-only (a transparent `LayerWindow` is the portable recipe). Recorded for the shell; no request. | `tre:docs/reference/layer-window.md`, `tre:LOG.md` (TRE-REQ-024 correction) |
| Layer clipping | by design: a layer escapes the ancestors' `clip_children` and is clipped to the host window; in a layer-surface host a tooltip that does not fit uses the popup-window route (AC-TIP-16). | `tre:docs/guide/layers.md`, [[Tooltip]] |
| Multiline Tab (request T-048) | fixed: `tab_navigates` (0.6.8) makes Tab and Shift+Tab leave a multiline `text_input`; default `False` keeps indentation. AC-MOD-TED-4 and AC-TXF-8 can pass by setting it; the Status in code row of [[Text Editor]] still names T-048 and needs the same update (not done by this note). | `tre:docs/guide/text.md` (`tab_navigates`) |

Also read and confirmed as not open: `active_descendant` exists since 0.6.10 (TRE-REQ-023; the documentation still says "unreleased", a stale word, see Questions); `LayerWindow` content size exists (TRE-REQ-022, `size=("content", ...)`); the accessibility tree, `announce` queue of 16, `live` regions and `describedby` and `controls` meet the criteria of [[Accessibility Tree]] that are not listed above.

## Counts

| Severity | Findings |
|---|---|
| high | 5 (TRE-001, TRE-007, TRE-008, TRE-009, TRE-014) |
| medium | 10 (TRE-002 to TRE-006, TRE-010, TRE-011, TRE-012, TRE-015, TRE-016) |
| low | 2 (TRE-013, TRE-017) |
| open total | 17 |
| dropped | 5 |

## Proposed request notes

Titles only; not created here. A request is approved by the Orchestrator under the owner's delegation ([[80 Requests]]).

| Proposed | Title | Findings | Status |
|---|---|---|---|
| UXREQ-001 | Two-axis scroll view with the specified scrollbar | TRE-001 to TRE-006 | exists, approved |
| UXREQ-002 | Virtual list keys and scroll to index | TRE-007, TRE-008 | exists, approved |
| UXREQ-003 | Accessibility set size, position, mixed, orientation and modal | TRE-009, TRE-010 | proposed |
| UXREQ-004 | Accessibility roles: radiogroup, option, listbox, toolbar, navigation, complementary, region, status, grid | TRE-011 | proposed |
| UXREQ-005 | Vertical alignment of text and text input, tracking and line height on text input | TRE-012, TRE-013 | proposed |
| UXREQ-006 | Terminal escape chord and history scrollbar | TRE-014 | proposed |
| UXREQ-007 | Drag cancel by Escape and edge auto-scroll | TRE-015 | proposed |
| UXREQ-008 | Outline property for focus rings | TRE-017 | proposed |
| (none) | OS file drop on Wayland | TRE-016 | external, upstream winit |

## Questions for the tre bot

1. TRE-002: with `SCROLLBAR_GRAB_SLOP` 6 around a 4 px thumb, does a press 8 px from the thumb centre across the axis grab the thumb? AC-SCB-06 wants no grab at 8 dp.
2. TRE-015: does a node that holds `capture_pointer` receive `key_down` (Escape) while the pointer is captured, so that a toolkit can cancel a drag itself? If yes, is the request only for dock drags?
3. TRE-016: is a Wayland file drop planned (winit upgrade, `wl_data_device` directly, or the portal)? If not, we keep the Open command as the only route and record AC-DNP-11 as a declared deviation on Wayland.
4. TRE-014: where would a reserved chord be best placed (a `terminal` property, or a window-level key filter before the terminal)? Is Ctrl+Shift+Escape free in the engine's key handling?
5. TRE-009: for a `virtual_list`, can the engine give `pos_in_set` and `set_size` from `item_count` and the row index without the toolkit setting them on each row?
6. TRE-011: the 24-role table says `M93 role vocabulary`; is the limit a decision or only the first set? AccessKit offers every role in TRE-011.
7. The accessibility guide still reads "Active descendant (unreleased)" although the tag `v0.6.10` carries it (LOG.md says so): is the word stale?
8. TRE-017: would an `outline` property sit well with the engine's paint model, or is a second `box` node the intended recipe for a focus ring?
9. Is a `mixed` value for `checked` preferred to extending `pressed`, given that `pressed` wins over `checked` where both are set?

Back to [[70 Adoption]].
