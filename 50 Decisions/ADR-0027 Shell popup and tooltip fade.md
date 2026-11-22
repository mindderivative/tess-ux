---
title: ADR-0027 Shell popup and tooltip fade
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Popup]]", "[[Tooltip]]", "[[Popup Window]]", "[[Motion]]", "[[Accessibility Rules]]"]
depends_on: []
---

# ADR-0027 Shell popup and tooltip fade

> [!important] Status
> `accepted`: accepted by bot:Orchestrator under the owner's delegation, 2026-11-22, on tess-shell's shipped decision (PR 178, schema 1.42; reported, not re-checked). The owner can overturn it.

## Context

[[Popup]] and [[Tooltip]] require no animation and recommend at most 100 ms ([[Motion]] `short2`). tess-shell shipped a setting for popups and tooltips with a longer default and rules for dismissal and the keyboard grab.

## Options

1. `Animation: FADE or NONE`, `Duration` default 200 ms, no slide (chosen)
2. No setting, popups always instant (the specification's minimum)
3. Fade and slide

## Decision

- `Animation` is `FADE` or `NONE`; `SLIDE` is refused with an error: a compositor places the popup and a slide would move it off its placement.
- `Duration` defaults to 200 ms (`short4`), a design choice above the 100 ms recommendation; a project may set it.
- With reduced motion the popup opens and closes instantly.
- A popup that is dismissed (Escape, outside press, opener removed) closes at once, with no fade-out.
- A popup that holds the keyboard grab keeps it during a fade-out and releases it no later than the end of it (shell measurement on a private KWin: released 1 ms after close, not re-checked).

## Consequences

- [[Popup]], [[Tooltip]] and [[Popup Window]] carry a deviation row and the motion note; [[Popup]] gets AC-POP-17.
- tess-ui is not affected: its popups are layers and keep the 100 ms recommendation unless it adopts the same setting.

## Affected notes

- [[Popup]]
- [[Tooltip]]
- [[Popup Window]]
