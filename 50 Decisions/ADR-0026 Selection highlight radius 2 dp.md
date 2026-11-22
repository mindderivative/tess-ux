---
title: ADR-0026 Selection highlight radius 2 dp
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Text Selection]]", "[[Text Field]]"]
depends_on: []
---

# ADR-0026 Selection highlight radius 2 dp

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-22, on tess-shell's approved default. The owner can overturn it.

## Context

[[Text Selection]] fixes the selection fill (`primary` at 30 percent) but gave no corner radius: MD3 and Compose draw the highlight as a square rectangle. tess-shell's selectable Text needs a default, and tre now has a `selection_radius` property (terminal, PR 347).

## Options

1. Radius 2 dp, the shell default (chosen)
2. Square highlight (MD3)

## Decision

The selection highlight of selectable text has a corner radius of 2 dp at every density, with the fill `primary` at 30 percent. It is a design choice and a recorded deviation from MD3. A project may override it per element.

## Consequences

- [[Text Selection]] carries the value in its Dimensions table, the shell default section and a deviation row.
- tess-ui and tess-shell need a hook for the radius on text and text input; tre has `selection_radius` on the terminal only in the 0.6.11 and 0.6.12 notes read so far.

## Affected notes

- [[Text Selection]]
