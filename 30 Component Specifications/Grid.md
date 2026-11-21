---
title: Grid
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, layout, primitive, planned]
related: ["[[Box]]", "[[FlexBox]]", "[[Form Row]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Spacing and Density]]"]
---

# Grid

> [!info] Summary
> A Grid lays children out in rows and columns so edges line up across rows (forms of label and field, tiles). Material Design 3 describes a responsive layout grid of columns, margins and gutters ([Layout](https://m3.material.io/foundations/layout/understanding-layout/overview)). The Tesserae shell decided a Grid block but does not build it yet; the engine supports grid layout. Source of truth in code: see Status in code.

## Purpose

Align label and field columns in settings forms, tile galleries and dashboards, where [[FlexBox]] rows cannot line up.

## When to use and not

- Use when: cells align on both axes.
- Do not use when: items follow one axis ([[FlexBox]]); children overlap ([[Box]]).

## Anatomy

1. Container with padding.
2. Tracks: columns and rows sized by length, `AUTO`, `EXPAND` (a share of free space) or `minmax`.
3. Gaps: `Column_Spacing`, `Row_Spacing`.
4. Cells: children placed in order, or by `Grid_Column` and `Grid_Row`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Form grid | label and field | two columns: `AUTO` and `EXPAND`; row gap 8 dp, column gap 12 dp |
| Tile grid | gallery | `repeat(auto_fill, minmax(96, 1fr))` in the engine; gap 8 dp |

## States

Not applicable: a Grid has no states.

## Tokens used

Gaps and padding from [[Spacing and Density]]: form grid column gap 12 dp (`space.4`) and row gap 8 dp (`space.3`) at `default`; 8 and 4 dp at `compact` and `dense`. These are Tesserae choices, not MD3 values; MD3 gutters are 16 or 24 dp for touch layouts #needs-verification.

## Sizing and density

| Value | default | compact | dense |
|---|---|---|---|
| Form grid row gap | 8 | 8 | 4 |
| Form grid column gap | 12 | 8 | 8 |
| Row minimum height | row height of the owning element (40) | 32 | 24 or 28 |

Row heights come from the controls in the cells ([[Spacing and Density]]).

## Layout and overflow

- A track of `AUTO` sizes to its widest cell; a text cell has minimum width 0 in an `EXPAND` track so it truncates ([[10 Layout Overflow and Scrolling]]).
- The Grid does not clip; content wider than the sum of fixed tracks overflows, so a Grid in a pane that can be narrower than its tracks goes in a [[ScrollBox]].
- Named lines and template areas are not supported by the engine.
- Percent-plus-pixel sizes inside a grid are taken of the Grid container, not the cell (engine limit).

## Behaviour

None of its own. Tab order is children order (row by row for `Auto_Flow: ROW`), which equals reading order only if children are in reading order.

## Tooltip and overlay behaviour

Not applicable: containers carry no tooltip ([[ADR-0004 Tooltip rule]]).

## Motion

Not applicable.

## Accessibility

Role none; a Grid used as a data table needs `table`, `row`, `cell` roles, which the shell role list lacks (candidate request). A form grid is announced by its rows ([[Form Row]]).

## Dark and light

As [[Box]].

## Defaults

One `EXPAND` track, gaps 0, `Auto_Flow` ROW, items STRETCH.

## Acceptance criteria

- [ ] AC-BLK-GRD-1 (geometry check): in a form grid with columns `AUTO` and `EXPAND` and three rows, all field left edges are equal and each equals the widest label width plus the column gap.
- [ ] AC-BLK-GRD-2 (geometry check): `Column_Spacing` 12 and `Row_Spacing` 8 give exactly those distances between adjacent cell borders.
- [ ] AC-BLK-GRD-3 (geometry check): a text cell of 600 dp natural width in an `EXPAND` track of 200 dp is at most 200 dp wide.
- [ ] AC-BLK-GRD-4 (geometry check): `Grid_Column: 1/3` spans two tracks including the gap between them.
- [ ] AC-BLK-GRD-5 (scripted input): Tab order follows row-major children order.
- [ ] AC-BLK-GRD-6 (review): a Grid block exists in the shell schema and block table, or the planned status stays recorded here. Pass: schema and this note agree.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (13 blocks, no Grid), `shell-vault:41 TDL Reference/Block Reference.md` (Grid decided, R11 lists it as v1) | absent: fails AC-BLK-GRD-1 to 6 |
| tess-ui | `tess-ui:src/tess_ui/views/*_View.tdl` | absent as a widget; layouts use flex only |
| tre | `tre:docs/guide/nodes-and-layout.md` (Grid layout), `tre:crates/engine-py/src/grid.rs` | partly meets: tracks, `fr`, `minmax`, `repeat`, spans, gaps; no named lines or template areas |

Note: the shell implements `Box` as a one-cell grid internally, so the engine path is in use.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Row and column gaps 12 and 8 dp at default (MD3 gutters 16 or 24 dp, touch layouts) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Grid is a container block, not a page layout grid | MD3 grid is a page-level concept (columns by window size class); page panes are specified in chapter 10 | [[ADR-0010 Document structure of the specifications]] |

## Sources

- `shell-vault:41 TDL Reference/Block Reference.md` (Grid), `tess-shell:src/tess_shell/schema/blocks.py`.
- `tre:docs/guide/nodes-and-layout.md`, `tre:docs/reference/properties.md` (Grid layout).
- MD3 layout (JavaScript app, not readable by tools #needs-verification): https://m3.material.io/foundations/layout/understanding-layout/overview.
