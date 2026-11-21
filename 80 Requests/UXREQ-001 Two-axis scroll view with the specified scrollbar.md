---
title: UXREQ-001 Two-axis scroll view with the specified scrollbar
type: request
status: approved
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [request, uxreq]
related: ["[[Scrollbar and Scroll Container]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0012 Scrollbar thumb opacity and hit area exception]]", "[[ADR-0020 The engine never blocks the design]]", "[[UXREQ-002 Virtual list keys and scroll to index]]"]
depends_on: []
---

# UXREQ-001 Two-axis scroll view with the specified scrollbar

> [!important] Status
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui (and later tess-shell). Routed through bot:Orchestrator.

## Principle

[[ADR-0020 The engine never blocks the design]]: every token below is settable from Python by a property or a declarative hook (a stylesheet rule), with no per-frame Python. A value the engine hardcodes today (thumb 4 px, fill alpha 0x8C, wheel 20 px) is the reason for this request, not an exception to the specification.

## Need

Owner feedback F6 (config-app demo, 2026-11-20, [[Owner Feedback 2026-11-20]]): no horizontal scrollbars although every panel has content past the visual frame. [[ADR-0003 Scrollbar rule]] requires a scrollbar for every axis whose content overflows. tre 0.6.10 offers one axis per scroll view (`ScrollViewState::new(horizontal)`, `tre:crates/engine-core/src/node.rs`); the only way to get two axes is to nest a horizontal view inside a vertical one, which splits wheel, key and scroll-into-view handling and leaves no corner rule. tess-ui's `ScrollView` has one `Orientation` and a planned two-way view depends on this.

## Request

An opt-in two-axis scroll view whose behaviour matches [[Scrollbar and Scroll Container]]:

- Orientation `both` (existing values keep their behaviour, so no existing view changes).
- Scrollbar tokens: every property of the Settable property set below, settable per view and as a project default; defaults: thumb thickness 8 dp, hit thickness 12 dp, margin 2 dp, minimum thumb length 32 dp, thumb radius half the thickness, thumb colour supplied by the caller, opacity 0.70 at rest, 0.80 on hover, 1.00 while dragged ([[ADR-0012 Scrollbar thumb opacity and hit area exception]]), no track, no auto-hide.
- Gutter: 12 dp reserved at the end edge of an axis that overflows, none for an axis that does not.
- Corner: a 12 dp square, empty, where both axes overflow; the two thumbs never overlap.
- Wheel: 40 dp per notch (today 20, settable as `wheel_step`), Shift plus wheel scrolls horizontally, a wheel over a view already at its end passes to the parent view.
- Click on the lane outside the thumb scrolls one page (viewport minus 10 percent) toward the click.
- Drag: the offset follows the pointer linearly: offset = start offset + pointer delta x (content - viewport) / (lane - thumb length); the drag continues while the pointer leaves the gutter and ends on release.
- Keys for a focused view: Up and Down 40 dp, Left and Right 40 dp, Page Up and Page Down one page, Home and End to the start and end of the vertical axis, Ctrl plus Home and End for the horizontal axis (key mapping to be confirmed in the interaction chapter when it is written).
- `scroll_into_view` per axis: a focused descendant is brought inside the viewport on both axes with the smallest movement.
- A scroll event reports both offsets (x and y) and the viewport and content sizes.

## Settable property set

The hook set is the table `Properties a project can set` in [[Scrollbar and Scroll Container]] (35 rows, tokens and defaults there). Each is a tre node property with a Python setter and a stylesheet key, settable per view and as a project default, no per-frame Python. Engine status today comes from `Settable Properties Reference` (tre 0.6.10):

| Property group | tre property | Status today | New tre property |
|---|---|---|---|
| Thumb thickness | `scrollbar_width` | settable (default 4 hardcoded) | no |
| Thumb colour, rest (with alpha) | `scrollbar_fill` | settable (default `#CAC4D0` at 55 percent hardcoded) | no |
| Thumb colour hover and drag; opacity states 0.70, 0.80, 1.00 | `scrollbar_fill_hover`, `scrollbar_fill_drag`, `scrollbar_opacity_*` | absent (one fill) | yes |
| Shape and radius | `scrollbar_shape`, `scrollbar_radius` | hardcoded (radius 2 px) | yes |
| Minimum length, margin | `scrollbar_min_length`, `scrollbar_margin` | hardcoded (32 and 2 px) | yes |
| Hit area | `scrollbar_hit_slop` | hardcoded (grab slop 6 px) | yes |
| Track colour and visibility | `scrollbar_track` | absent (no track) | yes |
| Wheel notch | `wheel_step` | hardcoded (20 px, `tre:crates/engine-py/src/listeners.rs`) | yes |
| Key line step | `key_scroll_step` | hardcoded (40 px) | yes |
| Key page step | `key_page_overlap` | hardcoded (full viewport) | yes |
| Smooth-scroll duration and curve | `scroll_smooth_duration`, `scroll_smooth_easing` | absent | yes |
| Snap settle and duration | `scroll_snap_settle`, `scroll_snap_duration` | hardcoded (120, 200 ms); `scroll_snap` and `snap_align` settable | yes |
| Fade, auto-hide delay, hover delay, lane repeat | `scrollbar_fade_duration`, `scrollbar_autohide_delay`, `scrollbar_hover_delay` | absent | yes |
| Gutter reserved and width, corner | `scrollbar_gutter_reserve`, `scrollbar_gutter`, `scrollbar_corner` | absent (thumb overlays content) | yes |
| Side vertical and horizontal, RTL | `scrollbar_side_vertical`, `scrollbar_side_horizontal`, `scrollbar_rtl` | absent | yes |
| Show policy | `scrollbar_visibility` (always, overflow, auto-hide, never) | absent (always on overflow) | yes |
| Arrow buttons and size | `scrollbar_arrows`, `scrollbar_arrow_size` | absent | yes |
| Lane click | `scrollbar_lane_click` (page, jump) | absent (no lane click) | yes |
| Per-element override | the same keys on a single view | the existing settable keys already work per view; new keys follow the same rule | follows the rows |

Defaults equal the spec values (thumb 8, hit 12, margin 2, minimum length 32, gutter 12, corner 12, opacities 0.70, 0.80, 1.00, wheel 40, keys 40, page viewport minus 10 percent, visibility overflow, arrows off, lane click page, side end and bottom). A property left unset behaves as the default. Acceptance: AC-SCB-22 to AC-SCB-30.

## Acceptance

[[Scrollbar and Scroll Container]]: AC-SCB-01 to AC-SCB-21, in particular AC-SCB-02 to AC-SCB-13 (geometry, thumb length, drag, lane click, keys, wheel) and AC-SCB-20 (clipping). A tre-level test passes when a view with 1000 by 800 dp content in a 400 by 300 dp viewport shows two thumbs without overlap, each drag moves only its own axis, and the keys above move the offsets by the stated amounts.

## Out of scope

Overscroll, rubber band, proximity snap, kinetic wheel inertia (OS-provided), touch behaviour.

Back to [[80 Requests]].
