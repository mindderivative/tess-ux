---
title: Adoption Plan
type: adoption
status: draft
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [adoption, plan]
related: ["[[Adoption tess-ui]]", "[[Adoption tess-shell]]", "[[Adoption tre]]", "[[Adoption Libraries]]", "[[17 Conformance]]", "[[Audit Template]]"]
depends_on: []
---

# Adoption Plan

How the specifications reach the projects. Each project has an audit worklist derived from the Status in code tables of the notes and checked against the project's `origin/main`; the Orchestrator routes the worklists to the project bots. This note orders the work across projects.

## Worklists

| Project | Note | Findings | P0 | P1 | P2 | Method |
|---|---|---|---|---|---|---|
| tess-ui | [[Adoption tess-ui]] | 69 | 8 | 39 | 22 | desk audit against `origin/main`, nothing run |
| tess-shell | [[Adoption tess-shell]] | 60 | 3 | 35 | 22 | desk audit against `origin/main`, nothing run |
| tre | [[Adoption tre]] | 17 | 5 high | 10 medium | 2 low | desk audit, severities high, medium, low |
| tess-dl, tess-el, tess-utils | [[Adoption Libraries]] | 9 | 0 | 1 medium | 1 low | nothing applies to tess-dl and tess-el |

Severity: P0 blocks use (an owner-feedback item still failing, a keyboard trap, content unreachable, a missing name on a core control), P1 breaks a MUST criterion, P2 polish. Counts come from the notes' summary tables and may move as findings are verified. No criterion is reported as passing: nothing was run.

## Order of work

1. P0 in tess-ui (the owner-feedback items): theme with no seed and first-frame flash (TUI-001, TUI-060), tree indent and chevron gap (TUI-002, TUI-003), tooltip scope and dismissal (TUI-010, TUI-011), two-axis scrolling (TUI-020, depends on UXREQ-001), icon-only FAB name (TUI-050).
2. tre requests that unblock the P0 items: [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] and [[UXREQ-002 Virtual list keys and scroll to index]] (approved), then set size and position, roles, the terminal escape chord and the vertical alignment of text (TRE-009, TRE-014 and the proposed UXREQ-003 to UXREQ-008 in [[Adoption tre]]).
3. P0 in tess-shell: the Bar auto-hide conflict (TSH-010, owner decision OQ-25), pressed menu item contrast (TSH-040), the clock colour on the light scheme (TSH-041).
4. P1 by theme across tess-ui and tess-shell: density (ADR-0002), tooltips (ADR-0004, ADR-0011), state layers (ADR-0009, shell adoption undecided: OQ-23), roles and names, keyboard paths, state feedback.
5. A contrast script in a shared library (LIB-004 in [[Adoption Libraries]]) so that every project runs the contrast acceptance criteria the same way.
6. P2 last; components that no application uses are audited when an application adopts them.

## Findings outside the worklists

- The shell `accent` colour on `surface` measures 4.38 to 1 in the dark scheme, below the 4.5 limit for text ([[Colour Roles]]); it passes for non-text use. Audit item for the shell: do not use `accent` for text.
- The scrollbar thumb at the accepted 0.60 rest opacity measures 3.11 to 1 over `surface` in the light scheme but 2.76 to 2.93 over `surface_dim`, `surface_container_high` and `surface_container_highest` ([[Open Questions]] OQ-32).

## How an audit is run

[[17 Conformance]] defines the unit (the criterion id), the result values and the report format; [[Audit Template]] is the table. The vault lint ([[Vault Lint]]) checks the notes themselves, not the projects.

Back to [[70 Adoption]].
