---
title: 80 Requests
type: index
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [index]
related: []
depends_on: []
---

# 80 Requests

Request notes `UXREQ-###` for things a project lacks, routed through the Orchestrator. A request names the hook the engine (tre) or toolkit needs; under [[ADR-0020 The engine never blocks the design]] every hook is settable from Python, with no per-frame Python. The table of hooks by what they unlock is in [[Adoption tre]], section Engine hooks needed.

## Notes

| Request | Owner project | Status |
|---|---|---|
| [[UXREQ-001 Two-axis scroll view with the specified scrollbar]] | tess-re | approved |
| [[UXREQ-002 Virtual list keys and scroll to index]] | tess-re | approved |
| [[UXREQ-003 Accessibility set size, position, mixed, orientation and modal]] | tess-re | approved |
| [[UXREQ-004 Accessibility roles]] | tess-re | approved |
| [[UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input]] | tess-re | approved |
| [[UXREQ-006 Terminal escape chord and history scrollbar]] | tess-re | approved |
| [[UXREQ-007 Drag cancel by Escape and edge auto-scroll]] | tess-re | proposed, held by the Orchestrator |
| [[UXREQ-008 Outline property for focus rings]] | tess-re | approved |
| [[UXREQ-009 First frame hold]] | tess-re | proposed, held by the Orchestrator |
| [[UXREQ-010 State layer hooks]] | tess-re | approved |

The OS file drop on Wayland (TRE-016) has no request: it is held, an upstream matter ([[Adoption tre]]).

Back to [[Index]].
