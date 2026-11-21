---
title: UXREQ-002 Virtual list keys and scroll to index
type: request
status: approved
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [request, uxreq]
related: ["[[Scrollbar and Scroll Container]]", "[[List]]", "[[Tree]]", "[[ADR-0020 The engine never blocks the design]]", "[[UXREQ-001 Two-axis scroll view with the specified scrollbar]]"]
depends_on: []
---

# UXREQ-002 Virtual list keys and scroll to index

> [!important] Status
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui. Routed through bot:Orchestrator.

## Principle

[[ADR-0020 The engine never blocks the design]]: the key steps, the wheel step and `scroll_to_index` are properties and calls settable from Python, with no per-frame Python.

## Need

Large lists and trees must be virtualised and still meet the keyboard rules of [[Scrollbar and Scroll Container]], [[List]] and [[Tree]]. In tre 0.6.10 the `virtual_list` has a draggable vertical thumb but handles no keys: Home, End, Page Up, Page Down and the arrows do nothing, and `scroll_into_view` skips it because it considers scroll views only (`tre:crates/engine-core/src/tree/scroll.rs`, `tree/dispatch.rs`). The docs say it scrolls by wheel only (`tre:docs/guide/nodes-and-layout.md`). A virtualised list therefore fails AC-SCB-10, AC-SCB-14 and the list and tree keyboard criteria.

## Request

- Keys on a focused `virtual_list`: Up and Down move `key_scroll_step` (default 40 dp), Page Up and Page Down move one page (`key_page_overlap`, default viewport minus 10 percent), Home and End go to the first and last row; the same properties and defaults as [[UXREQ-001 Two-axis scroll view with the specified scrollbar]].
- `scroll_to_index(i, align)` with `align` one of start, center, end, nearest; unmaterialised rows are materialised so the call works for any index in range.
- `scroll_into_view` works for a focused descendant that is a materialised row, with the `nearest` rule.
- Wheel step `wheel_step`, default 40 dp per notch (tre hardcodes 20 px today), settable per list and as a project default, as in UXREQ-001.
- The thumb of a virtual list takes every scrollbar property of the Settable property set of UXREQ-001, with the same defaults (AC-SCB-22 to AC-SCB-30).

## Acceptance

[[Scrollbar and Scroll Container]] AC-SCB-10, AC-SCB-11, AC-SCB-14; [[List]] and [[Tree]] keyboard criteria. A tre-level test passes when, in a virtual list of 10000 rows with a 400 dp viewport and 40 dp rows, End scrolls to the last row, Page Down moves 360 dp, `scroll_to_index(5000, "center")` centres row 5000, and focusing a materialised row outside the viewport scrolls it into view.

## Out of scope

Row selection, typeahead and expansion (framework code in tess-ui); horizontal virtualisation.

Back to [[80 Requests]].
