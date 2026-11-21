---
title: Canvas
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, drawing, primitive, post-v1]
related: ["[[Path Block]]", "[[Box]]", "[[Rectangle Block]]", "[[Colour Roles]]", "[[14 Accessibility Basics]]", "[[Accessibility Tree]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Colour Roles]]", "[[14 Accessibility Basics]]"]
aliases: ["Canvas node"]
---

# Canvas

> [!info] Summary
> A Canvas draws with code: a module's `draw` callback receives a painter and draws rectangles, circles and bezier strokes (charts, meters, waveforms). It has no MD3 counterpart. It is post-v1 in the shell and needs a module with its own Python. Source of truth in code: see Status in code.

## Purpose

Draw content that blocks and paths cannot express (data plots), with the accessibility and colour rules of every other block.

## When to use and not

- Use when: the picture is data driven and redrawn on change.
- Do not use when: blocks suffice ([[Box]], [[Rectangle Block]], [[Path Block]]); the drawing is a static icon ([[Path Block]]); the content is text (a Text block).

## Anatomy

1. Box with padding; painter coordinates start at the content box corner.
2. `draw` callback: runs when created, when set and on `redraw()`, never on its own.
3. Hit shape: the whole box, or a circle or path set from the painter.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Chart | data plot | roles for series, a text alternative |
| Meter | gauge | exposes `value` through its owner |

## States

Not applicable: states are drawn by the module's callback from its own state.

## Tokens used

Every colour the callback draws comes from a role ([[Colour Roles]]), resolved by the module when it draws; a literal colour is a defect. The canvas does not redraw when the scheme changes unless the module calls `redraw()` on the scheme event ([[Theme Following the System]]).

## Sizing and density

Not applicable: size is set by the owner. A canvas element that is a pointer target (a chart point) has a hit area of at least 24 dp (48 dp in touch contexts, [[Spacing and Density]]).

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| canvas | height | - | N/A: the owner sets the size; the painter draws inside it | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| canvas | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding, painter coordinates start at it) |
| canvas | margin | - | N/A: the parent container sets the outer space | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| canvas | gap | - | N/A: the painter callback places every shape; the block lays out nothing | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: the painter places every shape; tess-shell: n/a: element absent in tess-shell; tre: n/a: the painter places every shape |
| data point target | min width | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| data point target | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| canvas | border width | - | N/A: the block draws no border; the callback paints what it needs | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (stroke_width) |
| canvas | border color | - | N/A: the block draws no border; the callback paints what it needs | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (stroke_color) |
| canvas | corner radius | - | N/A: the painter clips to the rectangular box | N/A: same as default | N/A: same as default | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| canvas | font | - | N/A: the engine canvas has no text drawing call | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: the engine canvas has no text drawing call; tess-shell: n/a: element absent in tess-shell; tre: n/a: the engine canvas has no text drawing call |
| canvas | icon size | - | N/A: the block draws no icon; the callback may draw paths | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: the canvas draws no icon; tess-shell: n/a: element absent in tess-shell; tre: n/a: the canvas draws no icon |
| canvas | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

The 24 dp minimum applies to a chart point that is a pointer target (48 in touch contexts).

## Layout and overflow

- The painter clips to the box; nothing paints outside it.
- No wrapping or scrolling; a large drawing goes in a [[ScrollBox]] or is scaled by its owner.
- Hit testing: the whole box unless narrowed by `set_hit_test_circle` or `set_hit_test_path`.

## Behaviour

Pointer events if handlers are set; keyboard only if the module makes it focusable and implements the keys; a chart whose data points can be selected by pointer must offer the same selection by keyboard (WCAG 2.2 SC 2.1.1).

## Tooltip and overlay behaviour

Not applicable on the canvas as a whole; a hover value on a data point is a tooltip from a control, never drawn in the canvas ([[ADR-0004 Tooltip rule]]).

## Motion

Animation is the callback's: it redraws per frame only while something changes; reduced motion stops decorative animation ([[14 Accessibility Basics]]).

## Accessibility

Role none and hidden from AT unless `Label` is set; a canvas that conveys data has `Label` and `Description` giving the summary, and the data is available as text or a table next to it (WCAG 2.2 SC 1.1.1). Colour is not the only carrier (SC 1.4.1); non-text contrast 3 to 1 (SC 1.4.11).

## Dark and light

The callback draws from roles and redraws on a scheme change.

## Defaults

No `draw`, nothing painted, role none, hidden from AT, hit box.

## Acceptance criteria

- [ ] AC-BLK-CNV-1 (pixel check): a callback that fills a 200 by 100 dp rectangle in a 100 by 100 canvas leaves no ink outside the canvas box.
- [ ] AC-BLK-CNV-2 (scripted input): `draw` runs once at creation and once per `redraw()`, and zero times in 60 idle frames.
- [ ] AC-BLK-CNV-3 (token test): a scheme change followed by the module's redraw repaints series with the new role colours; the colours before and after differ by role resolution, and no literal remains in the callback source (static check).
- [ ] AC-BLK-CNV-4 (AT tree assertion): a data canvas exposes a name and a description; a decorative canvas is absent.
- [ ] AC-BLK-CNV-5 (scripted input): with `set_hit_test_circle`, a click outside the circle reaches the node behind.
- [ ] AC-BLK-CNV-6 (review): every pointer-only interaction on a canvas has a keyboard equivalent.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `shell-vault:41 TDL Reference/Block Reference.md` (Canvas, post-v1); no `Canvas` in `tess-shell:src/tess_shell/schema/blocks.py` | absent: fails all AC-BLK-CNV |
| tess-ui | `tess-ui:docs/guide/effects.md` | not verified |
| tre | `tre:docs/reference/painter.md`, `tre:crates/engine-core/src/canvas.rs`, `tre:docs/guide/painting.md` (Canvas) | meets: `fill_rect`, `fill_circle`, `stroke_path`, hit test narrowing; no text drawing call |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Imperative drawing block | MD3 has none; charts are app specific | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `shell-vault:41 TDL Reference/Block Reference.md` (Canvas), `tre:docs/reference/painter.md`, `tre:docs/guide/painting.md`.
- WCAG 2.2 SC 1.1.1, 1.4.1, 1.4.11, 2.1.1: https://www.w3.org/TR/WCAG22/.
