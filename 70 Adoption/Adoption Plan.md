---
title: Adoption Plan
type: adoption
status: draft
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adoption, plan]
related: ["[[Adoption tess-ui]]", "[[Adoption tess-shell]]", "[[Adoption tre]]", "[[Adoption Libraries]]", "[[17 Conformance]]", "[[Audit Template]]", "[[80 Requests]]", "[[ADR-0020 The engine never blocks the design]]", "[[UXREQ-001 Two-axis scroll view with the specified scrollbar]]", "[[UXREQ-002 Virtual list keys and scroll to index]]", "[[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]]", "[[UXREQ-004 Accessibility roles]]", "[[UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input]]", "[[UXREQ-006 Terminal escape chord and history scrollbar]]", "[[UXREQ-007 Drag cancel by Escape and edge auto-scroll]]", "[[UXREQ-008 Outline property for focus rings]]", "[[UXREQ-009 First frame hold]]"]
depends_on: []
---

# Adoption Plan

How the specifications reach the projects. Each project has an audit worklist derived from the Status in code tables of the notes and checked against the project's `origin/main`; the Orchestrator routes the worklists to the project bots. This note orders the work across projects.

## Worklists

| Project | Note | Findings | P0 | P1 | P2 | Method |
|---|---|---|---|---|---|---|
| tess-ui | [[Adoption tess-ui]] | 69 | 8 | 39 | 22 | desk audit against `origin/main`, nothing run |
| tess-shell | [[Adoption tess-shell]] | 59 open, 1 fixed | 3 | 31 | 25 | desk audit against `origin/main`, nothing run |
| tre | [[Adoption tre]] | 17 | 5 high | 10 medium | 2 low | desk audit, severities high, medium, low |
| tess-dl, tess-el, tess-utils | [[Adoption Libraries]] | 9 | 0 | 1 medium | 1 low | nothing applies to tess-dl and tess-el |

Severity: P0 blocks use (an owner-feedback item still failing, a keyboard trap, content unreachable, a missing name on a core control), P1 breaks a MUST criterion, P2 polish. Counts come from the notes' summary tables and may move as findings are verified. No criterion is reported as passing: nothing was run.

## Order of work

1. P0 in tess-ui (the owner-feedback items): theme with no seed and first-frame flash (TUI-001, TUI-060; the hold of the first frame needs a tre hook, UXREQ-009), tree indent and chevron gap (TUI-002, TUI-003), tooltip scope and dismissal (TUI-010, TUI-011), two-axis scrolling (TUI-020, needs the tre hook of UXREQ-001), icon-only FAB name (TUI-050).
2. The tre hooks that the P0 and P1 items need: [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] and [[UXREQ-002 Virtual list keys and scroll to index]] (approved), then set size and position, roles, the terminal escape chord and the vertical alignment of text (TRE-009, TRE-014 and UXREQ-003 to UXREQ-006, approved; UXREQ-007 to UXREQ-009, proposed and held; see [[Adoption tre]]).
3. P0 in tess-shell: build `Auto_Hide`, `Auto_Hide_Delay` and the Shortcut Mode reveal together (TSH-010, [[ADR-0021 Shortcut Mode reveals a hidden Bar]]), pressed menu item contrast (TSH-040), the clock colour on the light scheme (TSH-041).
4. P1 by theme across tess-ui and tess-shell: density (ADR-0002), tooltips (ADR-0004, ADR-0011), state layers (ADR-0009, shell adoption undecided: OQ-23), roles and names, keyboard paths, state feedback.
5. A contrast script in a shared library (LIB-004 in [[Adoption Libraries]]) so that every project runs the contrast acceptance criteria the same way.
6. P2 last; components that no application uses are audited when an application adopts them.

## Engine hooks needed

Under [[ADR-0020 The engine never blocks the design]] the engine offers a hook for every value the specification needs, settable from Python with no per-frame Python. The table of what each hook unlocks is in [[Adoption tre]].

- [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] (approved)
- [[UXREQ-002 Virtual list keys and scroll to index]] (approved)
- [[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]] (approved)
- [[UXREQ-004 Accessibility roles]] (approved)
- [[UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input]] (approved)
- [[UXREQ-006 Terminal escape chord and history scrollbar]] (approved)
- [[UXREQ-007 Drag cancel by Escape and edge auto-scroll]] (proposed, held)
- [[UXREQ-008 Outline property for focus rings]] (approved)
- [[UXREQ-009 First frame hold]] (proposed, held)

## Findings outside the worklists

- The shell `accent` colour on `surface` measures 4.38 to 1 in the dark scheme, below the 4.5 limit for text ([[Colour Roles]]); it passes for non-text use. Audit item for the shell: do not use `accent` for text.
- The scrollbar thumb rest opacity was raised to 0.70 (OQ-32, [[ADR-0012 Scrollbar thumb opacity and hit area exception]]): at 0.60 it measured 2.76 to 1 over `surface_dim` in the light scheme; at 0.70 the minimum over every surface role is 3.40 to 1. UXREQ-001 carries the value.

## How an audit is run

[[17 Conformance]] defines the unit (the criterion id), the result values and the report format; [[Audit Template]] is the table. The vault lint ([[Vault Lint]]) checks the notes themselves, not the projects.

Back to [[70 Adoption]].
