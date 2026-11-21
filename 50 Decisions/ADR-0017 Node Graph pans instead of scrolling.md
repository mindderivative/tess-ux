---
title: ADR-0017 Node Graph pans instead of scrolling
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[ADR-0003 Scrollbar rule]]"]
depends_on: []
---

# ADR-0017 Node Graph pans instead of scrolling

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Raised in the Phase 2 review (decision 4).

## Context

[[ADR-0003 Scrollbar rule]] requires scrollbars wherever content overflows. A node graph canvas is unbounded: there is no content extent to show. Evidence: [[Node Graph]].

## Options

1. The canvas pans and zooms; no scrollbars; a deviation from ADR-0003 (recommended)
2. Bounded canvas with scrollbars

## Decision

The Node Graph canvas pans (drag, space-drag, arrow keys) and zooms; it shows no scrollbars. This is a recorded deviation from ADR-0003 with this reason: the canvas has no content extent. Keyboard pan and zoom are required.

## Consequences

[[Deviations from MD3]] gains a row; tess-ui must add keyboard pan and zoom.

## Affected notes

- [[Node Graph]]
- [[Scrollbar and Scroll Container]]
