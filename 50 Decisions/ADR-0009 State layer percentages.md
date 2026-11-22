---
title: ADR-0009 State layer percentages
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0009 State layer percentages

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-05 in [[Open Questions]].

> [!note] Amended
> The 10 percent focus and pressed values are confirmed by [[ADR-0013 Focus and pressed state layer 10 percent]], 2026-11-21.

## Context

tess-ui implements MD3 state layers; the shell uses opacity literals (hover 0.85, pressed 0.7, disabled 0.5); tre draws none.

## Options

1. Adopt the MD3 percentages as the specification rule (recommended)
2. Document the shell literals as the rule

## Decision

Specification rule: hover 8, focus 10, pressed 10, dragged 16 percent; disabled content 38 and container 12 percent; focus ring 3 dp wide, 2 dp offset, role `secondary`, keyboard focus only. Adoption by tess-shell: decided yes by the owner on 2026-11-22 (his item 22, 'Adopt the MD3 state layers in the shell'); recorded in OQ-23.

## Consequences

The owner decided on 2026-11-22 that the shell adopts the state layers; tess-shell implements them (the fades wait for tre 0.6.12, TSH-020, TSH-022).

## Affected notes

- [[State Layers]]
- [[Focus Ring]]
- [[Deviations from MD3]]
