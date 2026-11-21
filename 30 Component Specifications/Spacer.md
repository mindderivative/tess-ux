---
title: Spacer
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, layout, primitive]
related: ["[[FlexBox]]", "[[Box]]", "[[10 Layout Overflow and Scrolling]]", "[[Spacing and Density]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Spacing and Density]]"]
aliases: ["Spacer Block"]
---

# Spacer

> [!info] Summary
> A Spacer is an empty block that takes the free space along the main axis of a flex container, pushing its siblings apart (for example the clock to the far end of a bar). Compose has a `Spacer`; Material Design 3 defines none. Source of truth in code: see Status in code.

## Purpose

Separate groups inside a [[FlexBox]] without computing gaps: left group, Spacer, right group.

## When to use and not

- Use when: one group must stick to each end of a row or column.
- Do not use when: a fixed gap is needed (use `Spacing` of the [[FlexBox]], a spacing step of [[Spacing and Density]]); a visible divider is needed (use a [[Rectangle Block]] of 1 dp).

## Anatomy

One invisible box with `Flex_Grow` 1.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Flexible | default | `Flex_Grow` 1 takes the free space |
| Weighted | two spacers share space | `Flex_Grow` 2 takes twice as much |
| Fixed | do not use | a fixed gap is a spacing step, not a Spacer |

## States

Not applicable: a Spacer paints nothing and has no states.

## Tokens used

None: no colour, shape or type. Gaps between the Spacer and its siblings come from the container `Spacing`.

## Sizing and density

Not applicable: the size is the free space. A Spacer has no minimum; in a container too small for its other children it collapses to 0 dp and never forces overflow.

## Layout and overflow

- Takes free space on the container main axis only; across the axis it stretches with `Align_Items`.
- It shrinks to 0 before any sibling shrinks below its minimum.
- Never clips, never scrolls. A Spacer in a [[ScrollBox]] content column has no free space and measures 0.

## Behaviour

Not applicable: not hit testable by intent, not focusable, no events. The shell raises pointer events for a Spacer only if a handler is set; none should be.

## Tooltip and overlay behaviour

Not applicable: no tooltip, no overlay.

## Motion

Not applicable: no animation of its own.

## Accessibility

Role none, no name, not focusable. Decorative; `A11y_Hidden` is the default expectation and adds no node to the tree.

## Dark and light

Not applicable: paints nothing.

## Defaults

`Flex_Grow` 1, no size, no paint.

## Acceptance criteria

- [ ] AC-BLK-SPC-1 (geometry check): in a 400 dp wide horizontal FlexBox holding a 100 dp child, a Spacer and a 60 dp child, the second child's right edge equals the container's inner right edge and the Spacer is 240 dp wide, with zero gap.
- [ ] AC-BLK-SPC-2 (geometry check): when the container narrows to 150 dp the Spacer measures 0 dp and the other children keep their sizes (no overlap).
- [ ] AC-BLK-SPC-3 (pixel check): the Spacer region has the same pixels as the container background.
- [ ] AC-BLK-SPC-4 (AT tree assertion): a Spacer exposes no node with a role or a name.
- [ ] AC-BLK-SPC-5 (scripted input): a click on a Spacer region with no handler reaches the container behind it; Tab never lands on it.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` (`Spacer`: tre `box` with default `flex_grow` 1) | meets AC-BLK-SPC-1 and 2 by construction; hit testing: the engine hits an empty box, so AC-BLK-SPC-5 is not verified |
| tess-ui | none | absent: use `Flex: fill` on an empty container |
| tre | `tre:docs/guide/nodes-and-layout.md` (`flex_grow`) | meets: no Spacer kind; a box with `flex_grow` |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Spacer exists as a block; MD3 has none | bars need end-aligned groups | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `shell-vault:41 TDL Reference/Block Reference.md` (Spacer, decided 2026-11-04), `tess-shell:src/tess_shell/binder/tables.py`.
- `tre:docs/guide/nodes-and-layout.md`. Compose `Spacer`: https://developer.android.com/develop/ui/compose/layouts/basics.
