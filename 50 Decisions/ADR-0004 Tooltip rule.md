---
title: ADR-0004 Tooltip rule
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0004 Tooltip rule

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-06 in [[Open Questions]].

## Context

tess-ui shows a tooltip after 500 ms and on keyboard focus; the engine has no tooltip primitive or timers; the config app put tooltips on whole rows. Owner feedback F2, F8, F9.

## Options

1. Tooltip on the control, MD3 timing, defined dismissal, keyboard-reachable rich tooltips (recommended)
2. Row-level tooltips where the row is the control

## Decision

The tooltip belongs to the control, never to a row or group. 500 ms hover delay, immediate on keyboard focus. Dismiss on pointer leave, Escape, scroll of an ancestor, press or activation, trigger removal and window focus loss. One tooltip at a time. Always an opaque container. Rich tooltips are reachable by keyboard. Details and tests: [[Tooltip]].

## Consequences

tess-ui must dismiss on scroll and activation; the config app and any form pattern attach tooltips to labels and controls only.

## Affected notes

- [[Tooltip]]
- [[12 Overlays]]
- [[Form Row]]
