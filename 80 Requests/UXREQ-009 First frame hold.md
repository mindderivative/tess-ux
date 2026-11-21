---
title: UXREQ-009 First frame hold
type: request
status: proposed
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, theme]
related: ["[[Theme Following the System]]", "[[ADR-0005 Theme follows the system]]", "[[Application Window]]", "[[Window]]", "[[Adoption tre]]", "[[Adoption tess-ui]]", "[[ADR-0020 The engine never blocks the design]]"]
depends_on: []
---

# UXREQ-009 First frame hold

> [!important] Status
> `proposed`; held by the Orchestrator, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui (finding TUI-060 in [[Adoption tess-ui]]). Not routed until the Orchestrator releases it.
>
> Progress, 2026-11-22: delivered for windows in tre 0.6.11 (PR 334: `Window(first_present=..., background=...)` and `window.ready()`). Layer and popup surfaces follow in tre's `feat/first-present-layers`; the request stays open for them.

## Principle

[[ADR-0020 The engine never blocks the design]]: the hold is a window property plus one call, settable from Python, with no per-frame Python.

## Need

[[ADR-0005 Theme follows the system]] requires that the scheme is resolved before the first frame. On macOS and Windows the platform appearance is answered after the window opens, so the application starts in one scheme and flips: a visible flash (owner feedback F1). On Linux the appearance is read at construction and no flash occurs. macOS and Windows are untested. The toolkit cannot hold the first present itself; the engine presents the first frame as soon as the window is mapped.

## Request

A window feature that defers the first present until the application calls `ready()` on the window or N ms pass, whichever comes first (property on the window, for example `first_frame_hold_ms`, default 0, so no existing window changes). Until then the window shows nothing (not mapped, or a single uniform colour the application sets); after `ready()` or the timeout the first present is the application's current tree. A window with the hold off behaves as today.

## Acceptance

[[Theme Following the System]] AC-TH-1, AC-TH-2, AC-TH-7 and AC-TH-8: with a platform stub that answers dark after 500 ms and a hold of 1000 ms, no frame is presented before the answer and the first presented frame is dark; with a stub that never answers, the first frame is presented at the hold time (200 ms in tess-ui). A tre-level test passes when the first present time equals the `ready()` call or the timeout, and the hold is ignored when it is 0.

## Out of scope

Reading the platform appearance (tess-ui, `tess-ui:src/tess_ui/follow.py`); the choice of the default scheme while the platform is silent (ADR-0005).

Back to [[80 Requests]].
