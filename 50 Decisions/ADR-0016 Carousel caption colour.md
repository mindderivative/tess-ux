---
title: ADR-0016 Carousel caption colour
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Carousel]]", "[[Scrim]]"]
depends_on: []
---

# ADR-0016 Carousel caption colour

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Raised in the Phase 2 review (decision 3).

## Context

A carousel caption over an image needs readable text on any image. A literal white text colour breaks the rule that every colour is a role, and the tess-ui band at `scrim` 32 percent gives 2.2 to 1 against white. Evidence: [[Carousel]], [[Scrim]].

## Options

1. Caption text `on_scrim` over a `scrim` band at 0.60 opacity (5.7 to 1) (recommended)
2. Literal white text
3. A per-image computed colour

## Decision

The caption text uses the colour role `on_scrim` and the band behind it is the `scrim` role at 0.60 opacity. No literal colours.

## Consequences

tess-ui's carousel changes the band opacity and the text role.

## Affected notes

- [[Carousel]]
- [[Scrim]]
