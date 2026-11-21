---
title: UXREQ-007 Drag cancel by Escape and edge auto-scroll
type: request
status: proposed
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, drag-and-drop]
related: ["[[Drag and Drop]]", "[[Drag and Drop Pattern]]", "[[Dock]]", "[[Scrollbar and Scroll Container]]", "[[Adoption tre]]", "[[ADR-0020 The engine never blocks the design]]"]
depends_on: []
---

# UXREQ-007 Drag cancel by Escape and edge auto-scroll

> [!important] Status
> `proposed`; held by the Orchestrator, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui. Finding: TRE-015 in [[Adoption tre]]. Not routed until the Orchestrator releases it.

## Principle

[[ADR-0020 The engine never blocks the design]]: cancel and auto-scroll are an event and properties settable from Python (the band and the speed are values, not callbacks), with no per-frame Python.

## Need

The engine has `capture_pointer` and the docking drag, but nothing cancels a drag on Escape (the docking guide cancels only through `undock_panel`), and nothing scrolls a scroll view at its edge during a drag (`tre:docs/guide/events-and-input.md`, `tre:docs/guide/docking.md`). Whether a node that holds a captured pointer receives `key_down` is not documented #needs-verification. Both rules are app code today, which cannot be reliable for dock drags, where the engine owns the gesture.

## Request

- Escape during a captured-pointer gesture or a dock drag ends it with a `pointer_cancel` event (no release, no drop), restores the dock state and raises no move; the event reaches the node that holds the capture.
- Opt-in edge auto-scroll for a scroll view during a captured-pointer gesture: a band (default 24 dp from the edge) and a speed that rises from 8 dp per frame at 60 Hz at the inner edge of the band to 32 dp per frame at the edge, settable per view; it stops one frame after the pointer leaves the band or the gesture ends.

## Acceptance

[[Drag and Drop]] AC-DND-7; [[Drag and Drop Pattern]] AC-DNP-4 and AC-DNP-9; [[Dock]] AC-DCK-6. A tre-level test passes when Escape during a dock tab drag leaves the panel in its zone with zero move events, and a pointer held 10 dp from the bottom edge of an auto-scroll view moves its offset by a value in the 8 to 32 dp per frame band each frame and by zero one frame after it leaves.

## Out of scope

The drag image, the drop indicator and the data (tess-ui code); file drops from the OS (TRE-016, upstream).

Back to [[80 Requests]].
