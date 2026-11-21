---
title: UXREQ-008 Outline property for focus rings
type: request
status: proposed
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, focus]
related: ["[[Focus Ring]]", "[[Scrollbar and Scroll Container]]", "[[Terminal]]", "[[Adoption tre]]", "[[ADR-0020 The engine never blocks the design]]"]
depends_on: []
---

# UXREQ-008 Outline property for focus rings

> [!important] Status
> `proposed`; held by the Orchestrator, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui and tess-shell. Finding: TRE-017 in [[Adoption tre]]. Not routed until the Orchestrator releases it.

## Principle

[[ADR-0020 The engine never blocks the design]]: the outline is a node property (width, offset, colour) settable from Python and from a stylesheet rule, with no per-frame Python.

## Need

`stroke_color` and `stroke_width` draw inside the border box, so the focus ring of [[Focus Ring]] (3 dp wide, 2 dp offset, with a transparent gap) has to be a shadow with spread, which fills the gap with an opaque colour, or an extra node; and a ring is cut by `clip_children` of an ancestor (`tre:docs/guide/painting.md`, strokes inside, shadows with spread). The tess-shell ring today is a 2 px spread with no offset.

## Request

An `outline` property on any node: width, offset (may be negative for the inward variant) and colour, drawn outside the border box and following the corner radius plus the offset, with a transparent gap. The outline does not affect layout or hit testing, and its paint is not clipped by `clip_children` of the node itself (the clip of an ancestor still applies, so the toolkit keeps scroll padding for the ring).

## Acceptance

[[Focus Ring]] AC-FOC-2 and AC-FOC-5; [[Terminal]] AC-BLK-TRM-7; [[Scrollbar and Scroll Container]] AC-SCB-15. A tre-level test passes when a box with `outline` of width 3, offset 2 and a corner radius of 8 renders a ring whose inner edge is 2 dp and whose outer edge is 5 dp outside the border box on all four sides, with a corner radius of 10 and fully transparent pixels in the gap.

## Out of scope

When the ring is shown (focus-visible logic, toolkit code); animation of the ring.

Back to [[80 Requests]].
