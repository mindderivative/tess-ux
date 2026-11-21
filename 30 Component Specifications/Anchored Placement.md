---
title: Anchored Placement
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, layout, engine, overlay]
related: ["[[Popup]]", "[[Popup Window]]", "[[Tooltip]]", "[[Menu]]", "[[Dialog]]", "[[Box]]", "[[12 Overlays]]", "[[10 Layout Overflow and Scrolling]]", "[[Focus Ring]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[12 Overlays]]"]
aliases: ["Absolute and anchored positioning"]
---

# Anchored Placement

> [!info] Summary
> Anchored placement puts a node against another node: a badge on the corner of a button, a label beside a field, a marker on a chart point (an ordinary node with `anchor`), or a menu below its button (a layer with `show_layer`). MD3 uses it for [badges](https://m3.material.io/components/badges/overview) and menus. This note states the placement rules the UX relies on and the differences between the two mechanisms.

## Purpose

Place one element relative to another with no tuned coordinates and no lag through scroll and transforms.

## When to use and not

- Use when: a badge, marker or label belongs to a distant element and must clip and order with its neighbours (anchored node); a menu, tooltip or dialog floats over the window (layer).
- Do not use when: the element is a bar or panel at a screen edge ([[Layer Window]]); a popup that hangs off a bar surface ([[Popup Window]]); a normal flow layout works ([[FlexBox]]).

## Anatomy

1. Anchor: the node placed against (its box through its transform).
2. Placed node: ordinary child of its own parent (clipped by `clip_children`, ordered by `z_index`, in the parent's Tab order, events bubble to the parent) or a layer.
3. Placement: `below` (default), `above`, `start`, `end` (outside the anchor, aligned to its start edge), or a point `top_start`, `top_end`, `bottom_start`, `bottom_end`, `center` (the node's centre on that point).
4. Offset `(dx, dy)` in the anchor's coordinates (+x toward the end, +y down; scaled with the anchor).
5. Flip and shift (layers only): when the preferred side lacks room and the opposite has more, the layer flips, then shifts to stay inside the window; points never flip or shift.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Anchored node | badge, marker, label | `anchor`, `placement`, `offset` on a node; never flipped or shifted; follows scroll and transforms |
| Layer | menu, tooltip, dialog, snackbar | `show_layer(anchor, placement, flip, offset)`; escapes ancestors' clipping; own Tab scope; dismissal rules |
| Insets | scrim, strip | `position: absolute` with `left`, `right`, `top`, `bottom` or `inset` against the parent |

## States

Not applicable: placement has no visual states; a layer reports `layer_placement` (the side it landed on) so a menu can grow upward or an arrow can point the right way.

## Tokens used

Offsets and gaps use the spacing steps ([[Spacing and Density]]): a badge sits 2 or 4 dp inside the corner, a tooltip 4 dp from its trigger #needs-verification (design choices); badge sizes 6 dp (dot) and 16 dp ([[Circle]]). Corner values: [[Shape]].

## Sizing and density

Not applicable: placement does not change sizes. A badge's hit area belongs to its control.

## Layout and overflow

- An anchored node is laid out after the layout in the same pass and follows the anchor with no lag, through scrolling and transforms above either.
- It never flips or shifts to fit: it can lie partly outside the window. A layer flips and shifts, and stays inside the window.
- Clipping: an anchored node is clipped by the parent's `clip_children`; a layer is not.
- Cycles: a node cannot be anchored to itself or a node inside it (`ValueError`); two nodes anchored to each other are put back in the flow with a warning; chains work.
- If the anchor is removed the node stays where it was.
- Insets are measured from the parent's edge, not its padding; both edges of an axis with `auto` size stretch the node; a set size wins over the second inset.

## Behaviour

- Pointer, keyboard, touch: those of the placed element. A layer dismisses on an outside press (not delivered to what lies under) and on Escape; a press inside never dismisses layers below; a submenu is a layer anchored to its item with `placement: end`.
- Focus: a modal layer moves focus to its first focusable node, Tab stays inside, and closing returns focus to the opener.

## Tooltip and overlay behaviour

A tooltip is a layer anchored to its trigger with `placement` above or below and `dismissible: false`, shown on hover after 500 ms and on keyboard focus at once ([[ADR-0004 Tooltip rule]], [[Tooltip]]); it never covers the focused trigger ([[14 Accessibility Basics]]).

## Motion

Placement is applied at every layout, with no animation; an entry animation belongs to the placed element ([[Motion]]).

## Accessibility

An anchored node keeps its place in the parent's Tab and accessibility order, which may differ from its visual place: a badge's meaning goes in the name of the control it decorates ("Inbox, 3 unread"), not only in the badge ([[Accessibility Tree]]). A layer is its own Tab scope and a modal one has role `dialog`.

## Dark and light

Not applicable.

## Defaults

`placement` below, `offset` (0, 0), `flip` true for layers, `dismissible` true, `modal` false.

## Acceptance criteria

- [ ] AC-ANC-1 (geometry check): a 16 by 16 node anchored to a 40 by 40 button with `placement: top_end` and `offset: (-2, 2)` has its centre at the button's top-end corner moved by (-2, +2) dp, within 1 dp.
- [ ] AC-ANC-2 (geometry check): after the button scrolls 100 dp or scales by 2, the anchored node keeps the same relation to the button within 1 dp in the same frame.
- [ ] AC-ANC-3 (geometry check): a layer anchored `below` a button within 20 dp of the window bottom lands `above` (`layer_placement` above) when more room exists above, and is shifted inside the window horizontally when it would overflow by 30 dp.
- [ ] AC-ANC-4 (geometry check): a point placement (`top_end`) with the anchor at the window edge is not flipped or shifted.
- [ ] AC-ANC-5 (scripted input): anchoring a node to itself raises `ValueError`; two nodes anchored to each other are returned to the flow and a warning is logged.
- [ ] AC-ANC-6 (scripted input): an outside press dismisses a dismissible layer and is not delivered to the node under it; a press inside a layer does not dismiss the layer below.
- [ ] AC-ANC-7 (pixel check): an anchored badge inside a `clip_children` parent is clipped at the parent's rounded edge; the same node as a layer is not clipped.
- [ ] AC-ANC-8 (scripted input): Escape closes the topmost dismissible layer only, and focus returns to the opener.
- [ ] AC-ANC-9 (AT tree assertion): a badge count appears in the accessible name or description of its control.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/composed.py` (anchor and placement for anchored nodes and tooltip layers), `tess-ui:src/tess_ui/overlays.py` (`show_layer`) | partly meets: uses both mechanisms; badge name rule (AC-ANC-9) not verified; dismissal on scroll and activation of tooltips is open in [[Tooltip]] |
| tess-shell | `tess-shell:src/tess_shell/surfaces/popup.py` (`placement` helper for popups) | not applicable to `anchor`: bars use popup windows ([[Popup Window]]) |
| tre | `tre:docs/guide/nodes-and-layout.md` (Anchored layout), `tre:docs/guide/layers.md`, `tre:crates/engine-core/src/overlay.rs` | meets AC-ANC-1 to 8 by documented behaviour (0.5.7 for anchors, points and offset) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Overlays clipped to the window, not to the control | desktop windows | [[ADR-0004 Tooltip rule]] |
| Tooltips and menus placed by the engine's flip and shift rule | MD3 gives no algorithm | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tre:docs/guide/nodes-and-layout.md` (Absolute positioning, Anchored layout), `tre:docs/guide/layers.md`, `tre:docs/reference/properties.md` (Size and position), `tre:crates/engine-core/src/overlay.rs`.
- MD3 badges and menus (JavaScript apps #needs-verification): https://m3.material.io/components/badges/overview, https://m3.material.io/components/menus/overview.
- WCAG 2.2 SC 2.4.11 Focus Not Obscured: https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum.
