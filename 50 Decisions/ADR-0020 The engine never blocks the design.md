---
title: ADR-0020 The engine never blocks the design
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr, principle]
related: ["[[01 Principles and Scope]]", "[[17 Conformance]]"]
depends_on: []
---

# ADR-0020 The engine never blocks the design

> [!important] Status
> `accepted`: owner principle of 2026-11-21, recorded by bot:Orchestrator under the owner's delegation. The owner can overturn it.

## Context

The audits found many criteria that tre cannot meet today because the engine hardcodes a visual value or lacks a hook: the scrollbar thumb size and colour, focus ring placement, text alignment, roles. The specifications must not bend to those limits, and a project must not have to write a deviation for something only the engine can change. Evidence: [[Adoption tre]], [[Adoption tess-ui]].

## Options

1. The engine never blocks the design: every visual element and parameter is adjustable from Python, and an engine limit is a request, never a specification exception (recommended; the owner's principle)
2. Specification values yield to engine limits and are recorded as deviations

## Decision

Tre must never block a design change. Every visual element and parameter of tre is adjustable from Python through properties, tokens or declarative hooks (a rule the engine evaluates), with no per-frame Python. tess-ui and tess-shell own the look. A specification value is always reachable from the project layer; where the engine hardcodes it, that is an engine request in `80 Requests`, never an exception to the specification.

## Consequences

- Adoption notes say 'needs a tre hook' with a UXREQ number instead of 'blocked on tre', and list the hooks needed ([[Adoption tre]], section Engine hooks needed).
- A criterion that fails because of an engine limit stays `fail` with the UXREQ id as its issue link ([[17 Conformance]], AC-CON-15); a project does not write a deviation ADR for it.
- Each default in the Defaults Matrix records whether it is settable from Python in tess-ui, tess-shell and tre.
- tess-re audits the hardcoded visuals of tre and proposes properties; the requests carry them.

## Affected notes

- [[01 Principles and Scope]]
- [[17 Conformance]]
- [[Adoption tre]]
- Defaults Matrix
