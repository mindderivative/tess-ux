---
title: ADR-0003 Scrollbar rule
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0003 Scrollbar rule

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-04 in [[Open Questions]].

## Context

tess-ui styles only the colour; tre draws a 4 px thumb without track or auto-hide; one axis per scroll view; the shell has no scrollbar. Owner feedback F6.

## Options

1. Both axes, visible when content overflows, no auto-hide by default on desktop, width and hit area as tokens, track-less thumb allowed (recommended)
2. Platform-native bars
3. Engine default as is

## Decision

Every scroll container shows a scrollbar for each axis whose content overflows. No auto-hide by default on desktop. Thickness, hit area, margin and minimum thumb length are tokens in [[Scrollbar and Scroll Container]]. A track-less thumb is allowed. Container with two overflowing axes shows two thumbs that do not overlap.

## Consequences

tre needs two-axis scrolling or nesting; virtual lists need key handling. Requests go through the Orchestrator.

## Affected notes

- [[Scrollbar and Scroll Container]]
- [[10 Layout Overflow and Scrolling]]
