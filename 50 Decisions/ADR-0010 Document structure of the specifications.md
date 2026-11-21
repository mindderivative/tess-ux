---
title: ADR-0010 Document structure of the specifications
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Open Questions]]"]
depends_on: []
---

# ADR-0010 Document structure of the specifications

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Question: OQ-11 in [[Open Questions]].

## Context

The vault holds two specifications and needs a stable structure and order. The owner-feedback slice goes first.

## Options

1. Chapters in `10`, tokens in `20`, one note per element in `30`, patterns in `40`; owner-feedback slice first, then the families of [[Plan]] (recommended)
2. Strict family order with no slice

## Decision

Structure as in the vault guide and [[Plan]]. Phase 1 writes the owner-feedback slice: chapters 01, 02, 07, 10, 12, 14, the foundations they need, and the component notes for Tooltip, Scrollbar, Tree, List, Text Field, Switch, Icon Button, Button, Accordion, Form Row, Dialog, Menu, Popup, Panel and Surface.

## Consequences

Remaining families follow the order in [[Plan]].

## Affected notes

- [[Plan]]
- [[Inventory]]
