---
title: ADR-0023 Text Field label placement by density
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Text Field]]", "[[Form Row]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
depends_on: []
---

# ADR-0023 Text Field label placement by density

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-22. The owner can overturn it. Raised by the tess-ui bot.

## Context

[[ADR-0002 Desktop density levels and target sizes]] fixes single-line container heights at 40, 32 and 28 dp. The MD3 floating label needs the container to hold the 12 dp label line above the input line (MD3's own field is 56 dp). At 32 and 28 dp a floating label cannot sit inside the container. [[Text Field]] had to say where the label goes and whether the container height includes it.

## Options

1. At compact and dense the label is external, above the field, outside the container height; at default density the MD3 floating label stays available with a 56 dp container; the accessible name is always the label (recommended)
2. Label only as placeholder (it disappears on input: weak for accessibility)
3. A floating label whose container grows with it (breaks ADR-0002 heights)

## Decision

Option 1. External label above the container at every density, and the only placement at compact and dense; the floating label variant exists at default density only, with a 56 dp container. The single-line container height (40, 32, 28 dp) never includes an external label. The label to container gap is 4, 4 and 2 dp (a design choice of this decision) and the label type is `body_small` 12/16. The accessible name is always the `Label` property; a placeholder is a hint. An application that asks for the floating variant at compact or dense gets the external label.

## Consequences

- [[Text Field]] gains two variants, a placement section, Dimensions rows and AC-TXF-17 to AC-TXF-19; AC-TXF-3 states that an external label does not change the container height.
- tess-ui adds an external label variant for compact and dense, and a density-dependent container height ([[Adoption tess-ui]]).
- A field in a [[Form Row]] normally has no label of its own: the row label names it.

## Affected notes

- [[Text Field]]
- [[Form Row]]
