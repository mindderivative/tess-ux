---
title: UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input
type: request
status: approved
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, text]
related: ["[[Text]]", "[[Text Field]]", "[[Typography]]", "[[03 Typography and Text Rules]]", "[[Owner Feedback 2026-11-20]]", "[[Adoption tre]]", "[[ADR-0020 The engine never blocks the design]]"]
depends_on: []
---

# UXREQ-005 Vertical alignment of text and text input, tracking and line height on text input

> [!important] Status
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui (and later tess-shell). Routed through bot:Orchestrator. Findings: TRE-012 and TRE-013 in [[Adoption tre]].

## Principle

[[ADR-0020 The engine never blocks the design]]: the alignment, the tracking and the line height are node properties settable from Python (and from a stylesheet rule), with no per-frame Python.

## Need

Owner feedback F7 ([[Owner Feedback 2026-11-20]]): single-line field text sat at the top of its box. A `text` node draws at the top of its box and a `text_input` has no vertical alignment property (`tre:docs/reference/properties.md`, `tre:docs/guide/text.md`), so centring is the caller's padding arithmetic, correct for one line box height only. `letter_spacing` and `line_height` exist on `text` and not on `text_input`, so the tracking of AC-TYP-2 cannot be applied to inputs.

## Request

- `vertical_align` (`start`, `center`, `end`; default `start`, so no existing node changes) for `text` and `text_input`, placing the line box (or the block of lines) in the content box of the node.
- `letter_spacing` and `line_height` on `text_input`, with the semantics they have on `text` (the caret, selection and scroll follow the spaced glyphs).

## Acceptance

[[Text]] AC-TXT-5; [[Text Field]] AC-TXF-1 and AC-TXF-2; AC-C03-3; AC-TLB-2; [[Typography]] AC-TYP-2. A tre-level test passes when a single-line `text_input` of height 40, 32 and 28 dp with `vertical_align="center"` shows equal space above and below the line box within 0.5 dp, and a `text_input` with `letter_spacing` set draws, positions its caret and selects with the spaced advances.

## Out of scope

Multi-line baseline alignment across siblings (cross-axis alignment already exists in layout); which alignment tess-ui chooses per component.

Back to [[80 Requests]].
