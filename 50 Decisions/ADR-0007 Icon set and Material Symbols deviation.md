---
title: ADR-0007 Icon set and Material Symbols deviation
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0007 Icon set and Material Symbols deviation

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-09 in [[Open Questions]].

## Context

tess-icons holds Pictogrammers Material Design Icons and Line MD, not Material Symbols; tre draws paths only; tess-ui carries two sets with different view boxes.

## Options

1. Keep Material Design Icons and record the deviation (recommended)
2. Move to Material Symbols

## Decision

The icon rules (sizes, tinting by colour role, fallback, 24 view box) are independent of the set. The set stays Material Design Icons; the missing weight, fill, grade and optical-size axes are a recorded deviation.

## Consequences

Icon notes link the deviation; a later change of set needs a new ADR.

## Affected notes

- [[Iconography]]
- [[Deviations from MD3]]
