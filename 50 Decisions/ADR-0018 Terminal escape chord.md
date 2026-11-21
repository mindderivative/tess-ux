---
title: ADR-0018 Terminal escape chord
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Terminal]]"]
depends_on: []
---

# ADR-0018 Terminal escape chord

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Raised in the Phase 2 review (decision 6).

## Context

The terminal block passes every key to the program, so a keyboard user cannot leave it: a keyboard trap under WCAG 2.1.2. Evidence: [[Terminal]].

## Options

1. Reserve an escape chord that moves focus out of the terminal (recommended)
2. Document the trap

## Decision

A terminal block reserves one chord, Ctrl+Shift+Escape, that moves focus to the next focusable element outside the terminal; the chord is shown in the block's description and is not sent to the program. A project may change the chord and must keep one. Proposed default: the shell's shortcut map needs a collision check.

## Consequences

The engine or framework must reserve the chord before the program receives keys.

## Affected notes

- [[Terminal]]
- [[11 Interaction]]
