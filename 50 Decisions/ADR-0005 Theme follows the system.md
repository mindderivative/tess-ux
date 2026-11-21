---
title: ADR-0005 Theme follows the system
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0005 Theme follows the system

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-07 in [[Open Questions]].

## Context

tess-ui follows the OS but macOS and Windows answer after the window opens (flash); an App without a seed ignores dark; the shell defaults to dark. Owner feedback F1.

## Options

1. Follow the system by default, persistent override, no first-frame flash (recommended)
2. Always dark default for the shell

## Decision

Themes follow the system by default. The user may override with system, light or dark and the override persists. The scheme is resolved before the first frame. Every surface uses colour roles. An app without a seed uses the baseline scheme and still follows light and dark.

## Consequences

Projects whose platform answers late delay the first frame or draw a neutral surface until resolved.

## Affected notes

- [[Theme Following the System]]
- [[02 Colour and Theming]]
