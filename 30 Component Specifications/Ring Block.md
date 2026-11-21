---
title: Ring Block
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, shape, primitive]
related: ["[[Circle]]", "[[Path Block]]", "[[Rectangle Block]]", "[[Shape]]", "[[Colour Roles]]", "[[Motion]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Shape]]", "[[Colour Roles]]"]
aliases: ["Ring", "Ring block"]
---

# Ring Block

> [!info] Summary
> A Ring is a Circle with no fill: a stroked circle whose thickness is `Border_Width`, used for outlines, radio rings and static progress rings. The MD3 counterpart for an animated ring is the circular [progress indicator](https://m3.material.io/components/progress-indicators/overview), which the [[Path Block]] with `Trim_End` builds. Source of truth in code: see Status in code.

## Purpose

Draw a circular outline without fill.

## When to use and not

- Use when: an unfilled circular outline is needed.
- Do not use when: a disc is needed ([[Circle]]); a partial arc or spinner is needed ([[Path Block]] with `Trim_Start` and `Trim_End`).

## Anatomy

1. Stroke: `Border_Width` thick, `Border_Color`, centred on the circle of the given diameter.
2. Hollow centre: transparent and, with hit shape painted, not hit.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Outline | radio or marker | `Border_Width` 2 dp |
| Heavy | emphasis | `Border_Width` 4 dp |

## States

Not applicable: no states of its own; `Border_Color` and `Opacity` change by `Transition`.

## Tokens used

`Border_Color` a role ([[Colour Roles]]); thickness a literal number of dp chosen by the owner (2 is the engine default of the shell); no radius.

## Sizing and density

Not applicable: `Diameter` set by the owner, independent of density. A 2 dp stroke is below the 24 dp target rule only as paint; the pointer target is the owner's.

## Layout and overflow

- Box is `Diameter` square; the stroke is centred on the outline, so half of it lies outside the nominal diameter in the engine path; the owner adds `Margin` of half the thickness when the outer size must equal the diameter #needs-verification.
- No clip, no scroll.
- Hit testing: painted shape: the stroke takes events, the hollow centre passes through.

## Behaviour

No events unless a handler is set; not focusable.

## Tooltip and overlay behaviour

Not applicable.

## Motion

`Transition` on `Border_Color`, `Opacity`. An animated spinner uses [[Path Block]] trim, not a Ring. Reduced motion: immediate change.

## Accessibility

Role none, hidden from AT unless `Label` is set. A ring that conveys progress takes the role `PROGRESSBAR` with `Value`, `Value_Min`, `Value_Max` on the owning element, never on the Ring alone. Contrast of the stroke 3 to 1 against its background when it carries meaning (WCAG 2.2 SC 1.4.11).

## Dark and light

Roles per scheme.

## Defaults

`Diameter` required, `Border_Width` 2, no fill (always transparent), hit shape painted.

## Acceptance criteria

- [ ] AC-BLK-RNG-1 (pixel check): a Ring with `Diameter` 24 and `Border_Width` 2 paints a stroke of 2 dp and the centre pixel is background.
- [ ] AC-BLK-RNG-2 (scripted input): a click at the centre passes to the node behind; a click on the stroke is delivered to the Ring.
- [ ] AC-BLK-RNG-3 (token test): a `Fill` key on a Ring is rejected by the schema; `Border_Color` resolves to a role.
- [ ] AC-BLK-RNG-4 (AT tree assertion): a Ring without `Label` is absent from the tree.
- [ ] AC-BLK-RNG-5 (geometry check): at scale 2.0 the stroke is 4 px; stroke width in dp does not change with the view box.
- [ ] AC-BLK-RNG-6 (contrast script): a meaningful Ring stroke has at least 3 to 1 against its background in light and dark.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` (`Ring`: path, fixed transparent fill, `stroke_width` default 2, hit shape painted) | meets |
| tess-ui | none | absent |
| tre | `tre:docs/reference/paint.md` | meets |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A static ring block; MD3 only has the animated circular progress | block set of the shell | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tess-shell:src/tess_shell/binder/tables.py`, `tess-shell:src/tess_shell/schema/blocks.py`.
- `tre:docs/reference/paint.md` (stroke, `hit_shape`).
- MD3 progress indicators (Material Web `docs/components/progress.md` verified to describe linear and circular types): https://github.com/material-components/material-web/blob/main/docs/components/progress.md. WCAG 2.2 SC 1.4.11: https://www.w3.org/TR/WCAG22/.
