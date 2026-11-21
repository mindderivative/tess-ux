---
title: ADR-0002 Desktop density levels and target sizes
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0002 Desktop density levels and target sizes

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-03 in [[Open Questions]].

## Context

No project has a density scale; tess-ui has `Compact` on `Tree` only (rows 40 px against 56) and the shell hard-codes control heights. Owner feedback F3 and F4 (tree gaps too large). MD3 sizes target touch.

## Options

1. Three levels default, compact, dense with a minimum pointer target of 24 dp and 48 dp in touch contexts (recommended)
2. MD3 sizes only
3. One compact desktop size

## Decision

Three density levels: `default`, `compact`, `dense`. Minimum pointer target 24 dp (WCAG 2.2 SC 2.5.8), 48 dp in touch contexts. Values are the canonical tables in [[Spacing and Density]]. A level is chosen per project or per container; each project sets its default in its own decision record.

## Consequences

Every component note carries sizes per level. The config app and the shell choose their default level in project ADRs.

## Affected notes

- [[Spacing and Density]]
- [[07 Spacing and Density Rules]]
