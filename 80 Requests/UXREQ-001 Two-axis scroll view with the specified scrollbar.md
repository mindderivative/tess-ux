---
title: UXREQ-001 Two-axis scroll view with the specified scrollbar
type: request
status: approved
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [request, uxreq]
related: ["[[Scrollbar and Scroll Container]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0012 Scrollbar thumb opacity and hit area exception]]", "[[UXREQ-002 Virtual list keys and scroll to index]]"]
depends_on: []
---

# UXREQ-001 Two-axis scroll view with the specified scrollbar

> [!important] Status
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui (and later tess-shell). Routed through bot:Orchestrator.

## Need

Owner feedback F6 (config-app demo, 2026-11-20, [[Owner Feedback 2026-11-20]]): no horizontal scrollbars although every panel has content past the visual frame. [[ADR-0003 Scrollbar rule]] requires a scrollbar for every axis whose content overflows. tre 0.6.10 offers one axis per scroll view (`ScrollViewState::new(horizontal)`, `tre:crates/engine-core/src/node.rs`); the only way to get two axes is to nest a horizontal view inside a vertical one, which splits wheel, key and scroll-into-view handling and leaves no corner rule. tess-ui's `ScrollView` has one `Orientation` and a planned two-way view depends on this.

## Request

An opt-in two-axis scroll view whose behaviour matches [[Scrollbar and Scroll Container]]:

- Orientation `both` (existing values keep their behaviour, so no existing view changes).
- Scrollbar tokens (settable per view, defaults as listed): thumb thickness 8 dp, hit thickness 12 dp, margin 2 dp, minimum thumb length 32 dp, thumb radius half the thickness, thumb colour supplied by the caller, opacity 0.60 at rest, 0.80 on hover, 1.00 while dragged ([[ADR-0012 Scrollbar thumb opacity and hit area exception]]), no track, no auto-hide.
- Gutter: 12 dp reserved at the end edge of an axis that overflows, none for an axis that does not.
- Corner: a 12 dp square, empty, where both axes overflow; the two thumbs never overlap.
- Wheel: 40 dp per notch (today 20), Shift plus wheel scrolls horizontally, a wheel over a view already at its end passes to the parent view.
- Click on the lane outside the thumb scrolls one page (viewport minus 10 percent) toward the click.
- Drag: the offset follows the pointer linearly: offset = start offset + pointer delta x (content - viewport) / (lane - thumb length); the drag continues while the pointer leaves the gutter and ends on release.
- Keys for a focused view: Up and Down 40 dp, Left and Right 40 dp, Page Up and Page Down one page, Home and End to the start and end of the vertical axis, Ctrl plus Home and End for the horizontal axis (key mapping to be confirmed in the interaction chapter when it is written).
- `scroll_into_view` per axis: a focused descendant is brought inside the viewport on both axes with the smallest movement.
- A scroll event reports both offsets (x and y) and the viewport and content sizes.

## Acceptance

[[Scrollbar and Scroll Container]]: AC-SCB-01 to AC-SCB-21, in particular AC-SCB-02 to AC-SCB-13 (geometry, thumb length, drag, lane click, keys, wheel) and AC-SCB-20 (clipping). A tre-level test passes when a view with 1000 by 800 dp content in a 400 by 300 dp viewport shows two thumbs without overlap, each drag moves only its own axis, and the keys above move the offsets by the stated amounts.

## Out of scope

Overscroll, rubber band, proximity snap, kinetic wheel inertia (OS-provided), touch behaviour.

Back to [[80 Requests]].
