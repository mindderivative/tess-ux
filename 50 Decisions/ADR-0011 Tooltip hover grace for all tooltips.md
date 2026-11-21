---
title: ADR-0011 Tooltip hover grace for all tooltips
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]", "[[ADR-0004 Tooltip rule]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]"]
---

# ADR-0011 Tooltip hover grace for all tooltips

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-19 in [[Open Questions]]. Amends [[ADR-0004 Tooltip rule]].

## Context

[[ADR-0004 Tooltip rule]] dismisses a tooltip on pointer leave of the trigger and grants a 150 ms grace only to rich tooltips. WCAG 2.2 SC 1.4.13 (content on hover or focus) asks that such content is dismissible, hoverable and persistent. Evidence: [[14 Accessibility Basics]], [[Tooltip]].

## Options

1. All tooltips, plain and rich, get the 150 ms grace (recommended)
2. Grace for rich tooltips only, document the exception

## Decision

The pointer moving from the trigger onto the tooltip keeps any tooltip, plain or rich, open; the tooltip closes 150 ms after the pointer has left both the trigger and the tooltip. The rest of ADR-0004 stands: 500 ms show delay, immediate on keyboard focus, dismissal on Escape, scroll of an ancestor, activation or press of the trigger, trigger removal and window focus loss; one tooltip at a time; the tooltip belongs to the control and never to a row, group or container. A tooltip stays open while hovered and is dismissible without moving the pointer (Escape).

## Consequences

Projects implement the grace for plain tooltips; the shell's 200 ms exit delay is within the same order of magnitude but must read 150 ms to pass the test.

## Affected notes

- [[Tooltip]]
- [[12 Overlays]]
- [[14 Accessibility Basics]]
