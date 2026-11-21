---
title: ADR-0001 MD3 role names are the specification vocabulary
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0001 MD3 role names are the specification vocabulary

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-02 in [[Open Questions]].

## Context

Tesserae has two token vocabularies: tess-ui uses the 49 Material Design 3 roles, tess-shell uses 12 flat roles (surface, surface_raised, on_surface, on_surface_muted, primary, on_primary, accent, error, warning, success, outline, scrim). The shell never imports tess-ui (shell ADR-0006), so code cannot share tokens. Evidence: [[Existing Tokens]].

## Options

1. Specification uses MD3 role names; each project keeps its own code and documents a mapping (recommended)
2. Two vocabularies in the specification
3. The shell adopts the MD3 roles in code

## Decision

The specification names colours, type, shape, elevation and motion tokens with MD3 role names only. Each project documents how its names map to them; the shell's 12 roles are listed as a mapping in [[Colour Roles]]. Roles without an MD3 counterpart (warning, success) are recorded as extensions, not as a second vocabulary.

## Consequences

Notes stay project-neutral. The shell keeps its code; an audit checks the mapping, not the names.

## Affected notes

- [[Colour Roles]]
- [[Existing Tokens]]
