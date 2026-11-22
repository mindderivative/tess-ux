---
title: ADR-0021 Shortcut Mode reveals a hidden Bar
type: adr
status: accepted
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adr]
related: ["[[Auto Hide]]", "[[Bar]]", "[[Accessibility Rules]]"]
depends_on: []
---

# ADR-0021 Shortcut Mode reveals a hidden Bar

> [!important] Status
> `accepted`: decided by the owner on 2026-11-21 (item 20 of the Orchestrator's list), recorded by bot:Orchestrator. It amends the owner's decision of 2026-10-27 that no key reveals a Bar. Closes OQ-25.

## Context

The owner decided on 2026-10-27 that no key reveals an auto-hidden Bar (`Reveal_Key` was removed). The accessibility rule AR-9 ([[Accessibility Rules]]) requires that everything reachable by pointer is reachable by keyboard, and a hidden Bar was reachable by pointer only. The two rules collided; [[Auto Hide]] and [[Bar]] recorded the conflict as OQ-25.

## Options

1. Shortcut Mode reveals a hidden Bar: a keyboard path with no always-on key (recommended; chosen)
2. A dedicated reveal key
3. A Bar that never hides

## Decision

A hidden Bar is revealed by Shortcut Mode. Entering Shortcut Mode shows every hidden Bar and keeps it visible while the mode is active. Focus does not jump to the Bar: it starts where the shell's focus rule 4 puts it (the Frame, or the surface the developer set as the default focus; when there is no Frame and no default, the first revealed surface in `Tab_Index` order), and `Next_Focus` and `Previous_Focus` move it through the Frame's panels, peeks, bars and strips in `Tab_Index` order, so the Bar is reached with `Next_Focus` (`shell-vault:40 Specifications/Integration/Focus and Keyboard.md`, rule 4 and rule 5). Leaving Shortcut Mode, or pressing Escape, hides the Bar again according to `Auto_Hide` and `Auto_Hide_Delay`. There is no always-on reveal key: plain keys still do not reveal a Bar, so the decision of 2026-10-27 holds for plain keys. A Bar that holds keyboard focus is not hidden while it holds it.

## Consequences

- AR-9 passes for the Bar through Shortcut Mode; AC-AHD-9 is no longer proposed or dependent on a decision.
- The shell must build `Auto_Hide`, `Auto_Hide_Delay` and the Shortcut Mode reveal together (TSH-010, TSH-050 in [[Adoption tess-shell]]).
- The same rule applies to a hidden Panel: Shortcut Mode reveals it ([[Panel and Surface]]).

## Affected notes

- [[Auto Hide]]
- [[Bar]]
- [[Panel and Surface]]
- [[Accessibility Rules]]
- [[Adoption tess-shell]]
