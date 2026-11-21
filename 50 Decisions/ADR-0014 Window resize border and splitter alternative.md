---
title: ADR-0014 Window resize border and splitter alternative
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Window]]", "[[Splitter]]"]
depends_on: []
---

# ADR-0014 Window resize border and splitter alternative

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Raised in the Phase 2 review (decision 1).

## Context

The 6 dp window resize border is below the 24 dp minimum pointer target of WCAG 2.2 SC 2.5.8, and a splitter resized by dragging needs a single-pointer alternative under SC 2.5.7. Evidence: [[Window]], [[Splitter]], [[Dock]].

## Options

1. Keep 6 dp for the window border with the platform resize path as the equivalent control; double-click collapse and a keyboard path as the dragging alternative for splitters (recommended)
2. Enlarge the border to 24 dp
3. Document the failure

## Decision

The window resize border stays 6 dp: the window manager's keyboard resize and the title bar maximise and restore controls are the equivalent control for SC 2.5.8. A splitter offers three ways to resize: drag, double-click to collapse and restore, and a keyboard path (arrow keys, Enter to collapse and restore, Home and End). The keyboard path is required, not optional.

## Consequences

Splitters without a keyboard path fail AC-SPL; tess-ui's Enter handling is a finding.

## Affected notes

- [[Window]]
- [[Splitter]]
- [[Dock]]
