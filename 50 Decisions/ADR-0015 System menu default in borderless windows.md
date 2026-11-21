---
title: ADR-0015 System menu default in borderless windows
type: adr
status: accepted
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [adr]
related: ["[[Window]]", "[[Title Bar]]"]
depends_on: []
---

# ADR-0015 System menu default in borderless windows

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-21. The owner can overturn it. Raised in the Phase 2 review (decision 2).

## Context

A borderless window loses the window manager's title bar and its system menu, which is the keyboard route to move, resize, minimise and close. tess-ui's `system_menu` is off by default. Evidence: [[Window]], [[Title Bar]].

## Options

1. System menu on by default in borderless windows (recommended)
2. Off by default

## Decision

In a borderless window the system menu is on by default and opens from the title bar icon, a secondary click on the title bar and Alt+Space. A project may turn it off in its own decision record.

## Consequences

tess-ui changes its default.

## Affected notes

- [[Window]]
- [[Title Bar]]
