---
title: UXREQ-010 State layer hooks
type: request
status: approved
owner: phil
created: 2026-11-22
updated: 2026-11-22
tags: [request, uxreq, state-layers]
related: ["[[State Layers]]", "[[Focus Ring]]", "[[UXREQ-008 Outline property for focus rings]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[ADR-0020 The engine never blocks the design]]"]
depends_on: []
---

# UXREQ-010 State layer hooks

> [!important] Status
> Progress, 2026-11-22: delivered in tre 0.6.11 (PR 335); per-state timings delivered on tre main (PR 338, 0.6.12 unreleased).
>
> `approved` by bot:Orchestrator under the owner's delegation, 2026-11-22 (tre audit item P13). Owner project: tess-re (tre). Consumers: tess-ui and tess-shell.

## Principle

[[ADR-0020 The engine never blocks the design]]: state feedback is declared with node properties settable from Python and from a stylesheet rule, with no per-frame Python.

## Need

[[State Layers]] specifies hover 8, focus 10, pressed 10 and dragged 16 percent, disabled content 38 and container 12 percent ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). tre draws no state layer and has no hover or pressed paint: tess-ui draws them with module constants (`HOVERED` and the others), tess-shell changes opacity literals. Neither project can change the percentages, the tint colour or the fade time from its stylesheet or theme.

## Request

Declarative state-layer properties on any node, evaluated by the engine on pointer and focus state changes: the layer colour (role colour), the opacity per state (hover, focus, pressed, dragged), the fade duration and easing, the layer shape (the node corner radius or a circle of a given size), and the disabled scheme (content and container opacities). Defaults are the specification values. The properties may be set per node and by a rule.

## Acceptance

[[State Layers]] AC-STL-1 to AC-STL-9: a node with the properties set to non-default values renders the layer colour and opacity per state after a scripted pointer or focus change, with no Python callback per frame.

## Out of scope

Ripple (tess-ui shader option); focus ring ([[UXREQ-008 Outline property for focus rings]]).

Back to [[80 Requests]].
