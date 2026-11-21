---
title: UXREQ-003 Accessibility set size, position, mixed, orientation and modal
type: request
status: approved
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, accessibility]
related: ["[[Accessibility Tree]]", "[[List]]", "[[Radio Button]]", "[[Checkbox]]", "[[Slider]]", "[[Date Picker]]", "[[Carousel]]", "[[Adoption tre]]", "[[ADR-0020 The engine never blocks the design]]", "[[UXREQ-004 Accessibility roles]]"]
depends_on: []
---

# UXREQ-003 Accessibility set size, position, mixed, orientation and modal

> [!important] Status
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-21. Owner project: tess-re (tre). Consumer: tess-ui (and later tess-shell). Routed through bot:Orchestrator. Findings: TRE-009 and TRE-010 in [[Adoption tre]].

## Principle

[[ADR-0020 The engine never blocks the design]]: each hook below is settable from Python by a property or a declarative hook, with no per-frame Python. The toolkit sets the values; the engine only carries them to the platform accessibility tree.

## Need

The engine's access state has `expanded`, `level`, `current`, `selected`, `pressed` and `checked`, and nothing else for position or grouping state (`tre:crates/engine-core/src/access.rs`, `tre:docs/reference/node.md`). Rows of a virtual list, radios, tabs and carousel items cannot report "2 of 5"; with virtualisation only the engine knows the full count, because only some rows exist. `checked` takes a boolean or none, so a parent checkbox cannot be mixed; `pressed` takes `"mixed"` for a toggle button only and wins over `checked` where both are set. A slider cannot say that it is vertical. A dialog cannot say that it is modal. The criteria below stay `fail` with this request as the issue link until the hooks exist.

## Request

- `set_size` and `pos_in_set` properties on any node, mapped to the platform position and set size. For a `virtual_list` the engine derives both from `item_count` and the row index, so the toolkit does not set them on each row; a row that sets them explicitly overrides the derived value.
- `checked` accepts `"mixed"` (as well as true, false and none) and exposes it as the mixed state; `mixed` and `pressed` do not conflict (an explicit rule when both are set).
- `orientation` (`horizontal` or `vertical`) for range nodes (`slider`, `progressbar`, `separator`), exposed to the platform.
- `modal` flag on a node (the `aria-modal` equivalent), mapped to the platform modal state; a modal layer sets it by default and the toolkit can override it.

## Acceptance

[[Accessibility Tree]] AC-AXT-13; [[List]] AC-LST-07; [[Radio Button]] AC-RAD-7; [[Carousel]] AC-CRS-9; [[Checkbox]] AC-CHK-8; [[Slider]] AC-SLD-12; [[Date Picker]] AC-DTP-8; AC-LAY-13. A tre-level test passes when the accessibility tree of a virtual list of 10000 rows shows the row at index 1 with position 2 and set size 10000 while about 20 rows exist, a checkbox with `checked="mixed"` reads as mixed, a vertical slider reads as vertical, and a node with the modal flag reads as modal.

## Out of scope

Roles ([[UXREQ-004 Accessibility roles]]); which nodes the toolkit marks modal or mixed (tess-ui code).

Back to [[80 Requests]].
