---
title: ADR-0012 Scrollbar thumb opacity and hit area exception
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]", "[[ADR-0003 Scrollbar rule]]"]
depends_on: ["[[ADR-0003 Scrollbar rule]]"]
---

# ADR-0012 Scrollbar thumb opacity and hit area exception

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-20 and OQ-21 in [[Open Questions]]. Amends [[ADR-0003 Scrollbar rule]].

> [!note] Amended
> 2026-11-22 (OQ-32, accepted by bot:Orchestrator under the owner's delegation): the rest opacity is 0.70, not 0.60. At 0.60 the thumb measures 2.76 to 1 over `surface_dim` in the light scheme; the smallest opacity that reaches 3.0 on every container is 0.65, and 0.70 is used for margin.

## Context

[[ADR-0003 Scrollbar rule]] proposed a thumb at 38 percent opacity at rest and a 12 dp hit area. The rest opacity gives 2.57 to 1 in dark and 1.94 to 1 in light against the surface, below the 3 to 1 non-text contrast of WCAG 1.4.11. The 12 dp hit area is below the 24 dp target of WCAG 2.5.8. Evidence: [[Scrollbar and Scroll Container]].

## Options

1. Thumb 70 percent at rest (amended from 60 by OQ-32), 80 hover, 100 dragged; keep 12 dp with the keyboard and wheel path as the equivalent control exception (recommended)
2. Enlarge the hit area to 24 dp
3. Keep 38 percent and document the failure

## Decision

The scrollbar thumb opacity is 70 percent at rest (5.85 to 1 dark and 3.96 to 1 light over `surface`; at least 3.40 to 1 over every surface role in all schemes; role `on_surface_variant`), 80 percent on hover and 100 percent while dragged. The hit area stays 12 dp. WCAG 2.5.8 is met through the equivalent-control exception: every scroll container offers keyboard scrolling (arrows, Page, Home, End) and wheel scrolling, so the thumb is not the only way to scroll. The note [[Scrollbar and Scroll Container]] documents the exception.

## Consequences

Projects set the thumb colour to `on_surface_variant` at the three opacities. Containers that cannot scroll by keyboard do not qualify for the exception.

## Affected notes

- [[Scrollbar and Scroll Container]]
- [[Spacing and Density]]
