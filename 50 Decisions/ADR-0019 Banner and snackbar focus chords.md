---
title: ADR-0019 Banner and snackbar focus chords
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Banner]]", "[[Snackbar]]"]
depends_on: []
---

# ADR-0019 Banner and snackbar focus chords

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Raised in the Phase 2 review (decision 7).

## Context

A snackbar or banner that appears while the user types is not reachable by Tab without scanning the whole window. Evidence: [[Banner]], [[Snackbar]].

## Options

1. Alt+Shift+B moves focus to the banner, Alt+Shift+N to the snackbar (recommended)
2. No chord, Tab order only

## Decision

Proposed defaults: Alt+Shift+B moves focus to the current banner and Alt+Shift+N to the current snackbar. Both are proposed defaults: a collision check against the shell's shortcut map and each application's own map is required before a project adopts them, and the chord table of [[11 Interaction]] lists them as proposed.

## Consequences

Projects run the collision check and record the result.

## Affected notes

- [[Banner]]
- [[Snackbar]]
- [[11 Interaction]]
