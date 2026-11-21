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

## Context

tess-ui implements MD3 state layers; the shell uses opacity literals (hover 0.85, pressed 0.7, disabled 0.5); tre draws none.

## Options

1. Adopt the MD3 percentages as the specification rule (recommended)
2. Document the shell literals as the rule

## Decision

Specification rule: hover 8, focus 10, pressed 10, dragged 16 percent; disabled content 38 and container 12 percent; focus ring 3 dp wide, 2 dp offset, role `secondary`, keyboard focus only. Adoption by tess-shell is not decided: the shell audit records it as a deviation and gap, and the Orchestrator asks the owner when the audit is due.

## Consequences

tess-shell status is `absent` until the owner decides.

## Affected notes

- [[State Layers]]
- [[Focus Ring]]
- [[Deviations from MD3]]
