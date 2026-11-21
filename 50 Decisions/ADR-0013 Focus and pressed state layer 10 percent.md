---
title: ADR-0013 Focus and pressed state layer 10 percent
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[ADR-0009 State layer percentages]]"]
---

# ADR-0013 Focus and pressed state layer 10 percent

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-22 in [[Open Questions]]. Amends [[ADR-0009 State layer percentages]].

## Context

[[ADR-0009 State layer percentages]] sets focus and pressed at 10 percent. The older Material Web token set (`v0_192`) has 12 percent; the latest set has 10. Evidence: [[State Layers]], [[MD3 Verification Status]].

## Options

1. 10 percent, following the latest token set (recommended)
2. 12 percent, following the older set

## Decision

Focus and pressed state layers are 10 percent. Hover stays 8, dragged 16, disabled content 38 and disabled container 12 percent. Adoption of state layers by tess-shell stays undecided (OQ-23); the shell audit records it as a gap and the Orchestrator asks the owner.

## Consequences

No change in tess-ui, which already uses 10.

## Affected notes

- [[State Layers]]
- [[Focus Ring]]
