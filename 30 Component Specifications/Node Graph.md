---
title: Node Graph
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, widget, graph, tesserae-specific]
related: ["[[Path Block]]", "[[Panel and Surface]]", "[[Focus Ring]]", "[[State Layers]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[Spacing and Density]]", "[[Drag and Drop]]", "[[Text Selection]]", "[[Accessibility Tree]]", "[[Scrollbar and Scroll Container]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Colour Roles]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[14 Accessibility Basics]]"]
---

# Node Graph

> [!info] Summary
> A Node Graph is a pannable, zoomable canvas of titled boxes (graph nodes) joined by curved edges, for tools such as pipelines. Material Design 3 has no node graph; the spec rests on the MD3 surface and card patterns, WAI-ARIA APG and the project code. Source of truth in code: see Status in code.

## Purpose

Show and rearrange a small directed graph (tens of nodes) with the pointer and the keyboard.

## When to use and not

- Use when: relations between items are the content and positions carry meaning to the user.
- Do not use when: items are a hierarchy ([[Tree]]) or a flat set ([[List]]); the graph holds hundreds of nodes (the widget builds every node, it does not virtualise).

## Anatomy

1. Viewport: clipped area, `surface_container_low`, optional border.
2. Content layer: holds nodes and edges, translated by the offset and scaled by the zoom.
3. Graph node: card with a title bar (32 dp, `surface_container_highest`, `title_small` label) and a body for content.
4. Edge: curve from the right side of the source node to the left side of the target; optional arrowhead.
5. Selection mark: 2 dp `primary` border on the chosen node.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Plain | view and move | no snap |
| Snapped | alignment | `Snap` N dp: moved nodes land on multiples of N |
| With arrows | directed graph | `Arrows: true` draws an open arrowhead 9 by 10 dp at the target end |

## States

State layer percentages follow [[ADR-0009 State layer percentages]] and [[ADR-0013 Focus and pressed state layer 10 percent]].

| State | Visual change | Token values |
|---|---|---|
| Node rest | card `surface_container_high`, border `outline_variant` 1 dp | radius `medium` 12 dp |
| Node hover | cursor `grab`; state layer `on_surface` 8 percent | [[State Layers]] |
| Node focused (keyboard) | [[Focus Ring]] outside the node (nodes are not clipped) | ring 3 dp, offset 2 dp, `secondary` |
| Node selected | border 2 dp `primary`; exposed as selected | role `primary` |
| Node dragged | cursor `grabbing`; dragged state layer | `on_surface` 16 percent |
| Edge | stroke 2 dp `outline`, not hit-testable | role `outline` |
| Empty graph | viewport only; the owner shows an empty-state hint | none |

## Tokens used

Viewport `surface_container_low`; node `surface_container_high`; title `surface_container_highest`, text `on_surface`; selection `primary`; edge `outline`; border `outline_variant` ([[Colour Roles]]); radius `medium` ([[Shape]]); title type `title_small` ([[Typography]]); spacing: title padding 12 dp left and right ([[Spacing and Density]]).

## Sizing and density

| Value | default | compact | dense |
|---|---|---|---|
| Title bar height | 32 | 28 | 24 |
| Title padding x | 12 | 8 | 8 |
| Keyboard step without snap | 8 | 8 | 8 |
| Zoom range | 0.25 to 4.0 | same | same |

Only the first row differs by density in this spec; the code has a fixed 32 dp. Node size is set by the author (140 by 80 dp in the documentation example). Edge stroke 2 dp. Zoom step 1.1 per wheel notch. Hit area of a node is its whole box (at least 24 dp each side: nodes smaller than 24 dp are not allowed).

## Layout and overflow

- Overflow: the viewport clips; the content is reached by panning (drag the background, space-drag, arrow keys) and zooming, and the canvas shows no scrollbars ([[ADR-0017 Node Graph pans instead of scrolling]]). This is a recorded deviation from [[ADR-0003 Scrollbar rule]] with this reason: the canvas has no content extent, so there is nothing for a thumb to show. The viewport must still give a cue when nodes lie outside it (candidate: edge indicators or a minimap, not built).
- `Fit: true` pans and zooms on open so every node shows, never beyond actual size (zoom 1.0), with 24 dp padding.
- A node label that exceeds the title width truncates with an ellipsis ([[10 Layout Overflow and Scrolling]]); today the title text does not truncate #needs-verification.
- Edges are drawn in a 20000 by 20000 unit space centred on the origin; nodes beyond about 10000 units from the origin lose their edges (engine and widget limit).

## Behaviour

- Pointer: drag the background pans (the pointer is captured); the wheel zooms about the pointer, keeping the graph point under the pointer fixed; drag a node moves it at the current zoom (delta divided by zoom), edges follow; pressing a node selects it, pressing the background clears the selection.
- Keyboard: Tab focuses nodes in tree order; arrow keys on a focused node move it one `Snap` square or 8 dp; Enter and Space activate nothing. Keyboard pan and zoom are required ([[ADR-0017 Node Graph pans instead of scrolling]]): arrow keys on the focused viewport pan it, plus and minus (with Ctrl) zoom, Home fits to view; the spec also requires Escape to clear the selection. These are not built (fail AC-NGR-5 to 7).
- Dragging alternative: moving a node by arrow keys satisfies WCAG 2.2 SC 2.5.7 for node moves; panning by drag has the keyboard pan as its alternative (AC-NGR-6, AC-NGR-7), not built today.
- Touch: not specified; pinch zoom is not built.

## Tooltip and overlay behaviour

Not applicable on the viewport. A node with truncated title shows the full label in a tooltip on the title text, not on the node ([[ADR-0004 Tooltip rule]]).

## Motion

Pan, zoom and node moves are direct manipulation and follow the pointer with no easing. `Fit` and `fit_to_view` jump; a 200 ms ease with `easing-standard` is allowed, and is immediate under reduced motion ([[Motion]]).

## Accessibility

- The viewport has role `group` and the name "Node graph" (the owner may supply a better one); each node has role `group`, the label as name, and `selected` when chosen.
- Edges are hidden from assistive technology, so the relations are not exposed: this fails the requirement that every edge is available as text. The spec requires that the relations are reachable, for example each node's description lists its successors ("Connects to Clean"), or `describedby` and `controls` link nodes (engine support since 0.5.6).
- Selection and moves are announced politely ("Load moved to 40, 40" optional; not required).
- Focus ring and contrast: node border `outline_variant` against `surface_container_low` is below 3 to 1 in the baseline schemes #needs-verification; the 1 dp border is decoration, node text contrast is the check (4.5 to 1).

## Dark and light

Roles per scheme; edges and borders keep 3 to 1 against the viewport where they carry information (selection border, edges).

## Defaults

Offset (0, 0), zoom 1.0, `Snap` 0, `Arrows` false, `Fit` false, nothing selected.

## Acceptance criteria

- [ ] AC-NGR-1 (geometry check): `Fit: true` with nodes spanning 800 by 400 dp in a 640 by 360 viewport sets zoom at most 1.0, every node lies inside the viewport with at least 24 dp padding, and zoom never exceeds 1.0 for a small graph.
- [ ] AC-NGR-2 (scripted input): one wheel notch changes zoom by a factor 1.1 within the range 0.25 to 4.0 and the graph point under the pointer stays within 1 px of the pointer.
- [ ] AC-NGR-3 (scripted input): dragging a node by 100 px at zoom 2.0 moves its position by 50 graph units; with `Snap: 20` the final position is a multiple of 20.
- [ ] AC-NGR-4 (geometry check): after a node move every edge end lies at the right middle of its source and the left middle of its target within 1 dp.
- [ ] AC-NGR-5 (scripted input): Escape with a selected node clears the selection.
- [ ] AC-NGR-6 (scripted input): Ctrl+plus and Ctrl+minus zoom by 1.1 steps; arrow keys on the focused viewport pan by 40 dp; Home fits to view; the pan and zoom keys are required ([[ADR-0017 Node Graph pans instead of scrolling]]). Pass: offset and zoom after each key.
- [ ] AC-NGR-7 (scripted input): every action available by background drag or space-drag (pan) and by wheel (zoom) is available by keyboard (WCAG 2.2 SC 2.5.7; [[ADR-0017 Node Graph pans instead of scrolling]]). Pass: offset and zoom reached by keys equal those reached by drag and wheel.
- [ ] AC-NGR-8 (AT tree assertion): each node exposes role `group`, its label as name and `selected` true when chosen; for each edge the source node's description or `controls` names the target.
- [ ] AC-NGR-9 (pixel check): the focused node shows the focus ring completely, not clipped by the viewport interior except at the viewport edge; selected node border is 2 dp `primary`.
- [ ] AC-NGR-10 (token test): all colours resolve to role names listed in Tokens used; zero literals.
- [ ] AC-NGR-11 (pixel check): a node whose label is wider than its title bar shows an ellipsis at the end of the label with no ink beyond the title padding.
- [ ] AC-NGR-12 (scripted input): a press on the background sets the selection to none and a press on a node chooses exactly that node (the `Selected` signal).
- [ ] AC-NGR-13 (geometry check): the node graph viewport draws no scrollbar and no scrollbar node at any zoom and offset, including when nodes lie outside the viewport (the recorded deviation from [[ADR-0003 Scrollbar rule]], [[ADR-0017 Node Graph pans instead of scrolling]]). Pass: zero scrollbar nodes in the viewport subtree in five zoom and offset cases.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/widgets/media.py` (`node_graph`, `graph_node`), `tess-ui:src/tess_ui/spec/builtin_widgets.py`, `tess-ui:docs/components/node-graph.md` | partly meets: pan, wheel zoom 0.25 to 4.0 with step 1.1, node drag with snap, arrow keys 8 dp or one snap square, edges with optional arrowheads, selection border `primary` and `selected` state, `fit_to_view`, nodes not clipped so the ring shows. Fails AC-NGR-5, 6, 7 (no Escape, no keyboard zoom or pan), 8 (edges hidden, no relation text), 11 (no ellipsis, not verified); not built per the docs: ports and dragging to connect, edge labels, multi-select, minimap, undo, virtualisation. No use found in apps or examples |
| tess-shell | none | not applicable |
| tre | `tre:docs/guide/painting.md` (Paths), `tre:docs/reference/node.md` (`transform`, `capture_pointer`) | not applicable: the widget is built from boxes, paths and transforms |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element with no MD3 counterpart, built from MD3 surface roles | tools need it | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Panning and zooming replace scrollbars on the canvas; no scrollbar is shown | the canvas has no content extent, so there is no extent to show (deviation from ADR-0003, keyboard pan and zoom required) | [[ADR-0017 Node Graph pans instead of scrolling]] |
| Dragged state layer 16 percent | MD3 dragged state | [[ADR-0009 State layer percentages]] |

## Sources

- `tess-ui:docs/components/node-graph.md`, `tess-ui:src/tess_ui/widgets/media.py`.
- WCAG 2.2 SC 2.5.7 Dragging Movements: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html (verified: all functionality that uses dragging can be achieved by a single pointer without dragging). SC 1.4.11, 1.4.3, 2.1.1: https://www.w3.org/TR/WCAG22/.
- WAI-ARIA 1.2 `group`, `aria-describedby`, `aria-controls`: https://www.w3.org/TR/wai-aria-1.2/.
- MD3 has no node graph (stated in `tess-ui:docs/components/node-graph.md`; MD3 pages are not readable by tools #needs-verification).
