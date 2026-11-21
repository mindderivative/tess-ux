---
title: ADR-0006 MD3 baseline with named Expressive adoptions
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0006 MD3 baseline with named Expressive adoptions

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-08 in [[Open Questions]].

## Context

tess-ui mixes the 2022 baseline with Expressive sizes (button sizes, shapes).

## Options

1. Baseline MD3 with named Expressive adoptions recorded as deviations (recommended)
2. Full Expressive

## Decision

The baseline is MD3 (2022 role, type and shape scales). Each Expressive element adopted is named in the note that uses it and listed in [[Deviations from MD3]] with its reason.

## Consequences

No silent Expressive values in notes.

## Affected notes

- [[Deviations from MD3]]
- [[Shape]]
