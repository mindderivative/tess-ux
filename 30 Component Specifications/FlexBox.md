---
title: FlexBox
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, layout, primitive]
related: ["[[Box]]", "[[Grid]]", "[[Spacer]]", "[[ScrollBox]]", "[[Form Row]]", "[[10 Layout Overflow and Scrolling]]", "[[07 Spacing and Density Rules]]", "[[Spacing and Density]]", "[[Panel and Surface]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[Spacing and Density]]"]
aliases: ["FlexBox Block"]
---

# FlexBox

> [!info] Summary
> A FlexBox stacks its children along one axis with a gap, wraps them if asked, and aligns them across and along the axis. Material Design 3 has no layout primitive; the counterparts are the Compose `Row` and `Column` and the 4 dp layout grid ([Layout](https://m3.material.io/foundations/layout/overview)). Source of truth in code: see Status in code.

## Purpose

Arrange rows (bars, toolbars, form lines, button groups) and columns (panels, lists of sections) so that gaps, alignment and shrinking follow rules instead of tuned numbers.

## When to use and not

- Use when: children follow each other in one direction, optionally wrapping.
- Do not use when: children must line up across rows (use [[Grid]]); children overlap (use [[Box]]); content must scroll (wrap the FlexBox in a [[ScrollBox]]).

## Anatomy

1. Container: padding, optional paint (as [[Box]]).
2. Main axis: `Flex` HORIZONTAL or VERTICAL.
3. Gap: `Spacing` between children.
4. Children: each with `Flex_Grow`, `Flex_Shrink`, `Align_Self`, `Min_*`, `Max_*`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Horizontal | bars, toolbars, rows | `Flex: HORIZONTAL` (default) |
| Vertical | panels, columns, vertical bars | `Flex: VERTICAL` |
| Wrapping | tag lists, chip rows | `Wrap: true`, lines separated by `Spacing` |

## States

Not applicable: a FlexBox has no states of its own (see [[Box]]).

## Tokens used

`Spacing` and padding use the nine steps of [[Spacing and Density]]; typical choices: 8 dp between related controls, 16 dp between controls, 24 dp between groups ([[07 Spacing and Density Rules]]). Paint as [[Box]].

## Sizing and density

Not applicable: no size of its own. A row of controls gets its height from the tallest child, so the control heights per density (40, 32, 28 dp, [[Spacing and Density]]) set the row height. The gap between adjacent controls is at least `space.1` (2 dp) when each has a 24 dp hit area, and 8 dp at `default` and `compact` and 4 dp at `dense` as the default.

## Layout and overflow

- Shrinking: a child holding text has `Min_Width` 0 and `Flex_Shrink` 1 so it truncates with an ellipsis; icons, switches and buttons keep a fixed minimum equal to their hit area and `Flex_Shrink` 0 ([[10 Layout Overflow and Scrolling]], Minimum widths; AC-LAY-6).
- Cross-axis alignment: `Align_Items` CENTER places single-line children on a common vertical centre; STRETCH fills the cross axis.
- Overflow per axis: the FlexBox does not clip; content beyond it paints outside unless `Clip_Children` is set; a column that can outgrow its parent goes in a [[ScrollBox]].
- Wrap: lines break between children, never inside one; the gap applies on both axes.
- Order follows the children list; `Z_Index` changes paint order only.

## Behaviour

Pointer, keyboard and touch: none of its own. Tab order follows tree order, not visual order after `Z_Index` or wrapping changes; a FlexBox that reorders visually keeps source order equal to reading order (WCAG 2.2 SC 2.4.3).

## Tooltip and overlay behaviour

Not applicable: a container never carries a tooltip ([[ADR-0004 Tooltip rule]]).

## Motion

Not applicable: layout changes are immediate; a child that animates its size uses the `Transition` keys of its own element ([[Motion]]).

## Accessibility

Role none, no name. A FlexBox that groups related controls takes `Role: GROUP` with a `Label` from the owning element (a toolbar, a form section). Reading order equals source order.

## Dark and light

As [[Box]].

## Defaults

`Flex` HORIZONTAL, `Wrap` false, `Spacing` 0, padding 0, `Align_Items` and `Justify_Content` as given by the shell schema (`STRETCH` and `START` in the Block Reference; the engine page does not state its defaults #needs-verification).

## Acceptance criteria

- [ ] AC-BLK-FLX-1 (geometry check): in a horizontal FlexBox of width 200 dp holding a text child of 600 dp natural width, a 24 dp icon and a 40 dp button with gaps of 8 dp, the text child is at most 200 minus 24 minus 40 minus 16 dp wide and the icon and button keep their size (same as AC-LAY-6).
- [ ] AC-BLK-FLX-2 (geometry check): `Spacing` 8 puts exactly 8 dp between the borders of adjacent children on the main axis and 8 dp between wrapped lines; `Spacing` values outside the nine steps fail the AC-DEN-1 lint.
- [ ] AC-BLK-FLX-3 (geometry check): with `Align_Items: CENTER`, the vertical centres of children of 24, 32 and 40 dp height differ by at most 1 px.
- [ ] AC-BLK-FLX-4 (geometry check): with `Flex_Grow` 1 on one child, it takes all free main-axis space and siblings keep their size; with `Flex_Shrink` 0 a child never narrows below its set width.
- [ ] AC-BLK-FLX-5 (geometry check): with `Wrap: true` and children totalling 500 dp in 200 dp, no child is split and no line is wider than 200 dp.
- [ ] AC-BLK-FLX-6 (scripted input): Tab visits focusable children in source order for HORIZONTAL, VERTICAL and wrapped layouts.
- [ ] AC-BLK-FLX-7 (AT tree assertion): a FlexBox with `Role: GROUP` and `Label` exposes `group` with that name; one with no role is absent from the role list.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` (`FlexBox`) | meets: keys `Flex`, `Wrap`, `Align_Items`, `Justify_Content`, `Spacing`, `Padding`; engine defaults unverified |
| tess-ui | `tess-ui:src/tess_ui/views/*_View.tdl` (`Container` with `Flex_Direction`) | partly meets: same engine layout; spacing literals off the scale (value 14 in `Snackbar_Stylesheet.tdl`) fail AC-BLK-FLX-2 |
| tre | `tre:docs/guide/nodes-and-layout.md` (Flex layout), `tre:docs/reference/properties.md` | meets: taffy flexbox with direction, wrap, gap, grow, shrink, basis, min and max, percentage and calc sizes |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Gap defaults 8, 8, 4 dp by density | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| No MD3 counterpart for a layout block | MD3 specifies layout by grid and canonical layouts, not by primitives | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `shell-vault:41 TDL Reference/Block Reference.md` (FlexBox), `tess-shell:src/tess_shell/schema/blocks.py`.
- `tre:docs/guide/nodes-and-layout.md`, `tre:docs/reference/properties.md`.
- MD3 layout page (JavaScript app, not readable by tools #needs-verification): https://m3.material.io/foundations/layout/overview. Compose Row and Column: https://developer.android.com/develop/ui/compose/layouts/basics.
- WCAG 2.2 SC 2.4.3 Focus Order: https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html.
