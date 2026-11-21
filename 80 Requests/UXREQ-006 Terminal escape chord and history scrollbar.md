---
title: UXREQ-006 Terminal escape chord and history scrollbar
type: request
status: approved
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, terminal]
related: ["[[Terminal]]", "[[ADR-0018 Terminal escape chord]]", "[[Scrollbar and Scroll Container]]", "[[UXREQ-001 Two-axis scroll view with the specified scrollbar]]", "[[Adoption tre]]", "[[ADR-0020 The engine never blocks the design]]"]
depends_on: []
---

# UXREQ-006 Terminal escape chord and history scrollbar

> [!important] Status
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui and tess-shell. Routed through bot:Orchestrator. Finding: TRE-014 in [[Adoption tre]].
>
> Progress, 2026-11-22: the escape chord is delivered in tre 0.6.11 (PR 333: `escape_chord`, `escape_chord_reverse`). The second half, the terminal history scrollbar, is NOT built in tre 0.6.11 (`docs/guide/text.md`: the wheel scrolls the history, a scrollbar is a later item); it stays open.

## Principle

[[ADR-0020 The engine never blocks the design]]: the chord and the scrollbar are properties of the `terminal` node settable from Python, with no per-frame Python. The chord filter runs in the engine's key path, not in a Python callback.

## Need

A focused `terminal` takes every key, so no chord leaves it: a keyboard trap (WCAG 2.1.2). [[ADR-0018 Terminal escape chord]] reserves Ctrl+Shift+Escape (a project may change it). Ctrl+Shift+C copy already works. The terminal has no scrollbar over its history although the wheel and the history work (`tre:docs/guide/text.md`, Terminal; `tre:crates/engine-py/src/terminal.rs`), so AC-SCB-02 fails for it.

## Request

- A settable chord property on `terminal` (default Ctrl+Shift+Escape, the empty value disables it). The chord is matched before the key reaches the program, is not sent to the shell, and moves focus to the next focusable node outside the terminal.
- An opt-in scrollbar over the history (the scrollback and the visible rows as content), using the scrollbar tokens, thumb states and lane behaviour of [[UXREQ-001 Two-axis scroll view with the specified scrollbar]].

## Acceptance

[[Terminal]] AC-BLK-TRM-3; [[Scrollbar and Scroll Container]] AC-SCB-02 (terminal). A tre-level test passes when, with focus in a terminal, Tab reaches the program and the chord moves focus to the next node outside it without sending a byte, and a terminal with 500 lines of history in 24 visible rows shows a thumb whose length follows AC-SCB-05.

## Out of scope

Which chord a project chooses (ADR-0018 records the default and the change rule); selection and copy rules.

Back to [[80 Requests]].
