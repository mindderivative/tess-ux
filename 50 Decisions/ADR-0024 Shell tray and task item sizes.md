---
title: ADR-0024 Shell tray and task item sizes
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Tray Item]]", "[[Task Item]]", "[[Tray Module]]", "[[Tasks Module]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
depends_on: []
---

# ADR-0024 Shell tray and task item sizes

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-22, on the owner principle that the compact level keeps today's sizes.

## Context

The specification gave the tray item and the task item the sizes of the icon button (container 40, 32, 28 dp, icon 24, 20, 20 dp, [[ADR-0002 Desktop density levels and target sizes]]). In the shell they are smaller: a tray item is 24 by 24 dp with an 18 dp icon today, a task item 24 dp high, and the shell bar holds many of them. The owner principle is that the compact level keeps today's sizes.

## Options

1. Tray and task items have their own sizes: 32, 24, 24 dp (default, compact, dense) and icons 20, 18, 18 dp; 24 dp is the pointer minimum (recommended, chosen)
2. Use the icon button sizes 40, 32, 28 (a visible change to every Bar)

## Decision

Tray items and task items are not the icon button. Their height and hit area are 32, 24 and 24 dp at default, compact and dense; their icons are 20, 18 and 18 dp. The compact size equals today's size. 24 dp is the pointer minimum, so the dense level does not go below it. The tray and tasks modules take their row height from these items.

## Consequences

- [[Tray Item]], [[Tray Module]], [[Task Item]] and [[Tasks Module]] carry the sizes in their Sizing tables, Dimensions rows and acceptance criteria (AC-MOD-TRI-2, AC-MOD-TRY-7, AC-MOD-TIT-6, AC-MOD-TSK-7); each records a deviation row.
- tess-shell meets them at compact and dense today (24 by 24); the default level and the icon sizes 20 and 18 are the shell's to build ([[Adoption tess-shell]]).
- Line_Height in the shell is a pixel value; the binder converts it to tre's multiplier. The shell fix is tracked in [[Hooks Needed]].

## Affected notes

- [[Tray Item]]
- [[Tray Module]]
- [[Task Item]]
- [[Tasks Module]]
