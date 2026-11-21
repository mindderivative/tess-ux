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

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| ring | height | - | N/A: `Diameter` is required and has no default; the owner sets it | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Diameter); tre: yes (width, height) |
| ring | padding | - | N/A: the block has no children | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: the block has no children and no Padding key; tre: n/a: the path has no children to inset |
| ring | margin | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | tess-shell:src/tess_shell/binder/tables.py | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Margin); tre: yes (margin) |
| ring | gap | - | N/A: the block has no children | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: the block has no children and no Spacing key; tre: n/a: the path has no children |
| ring | min width | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Width); tre: yes (min_width) |
| ring | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Height); tre: yes (min_height) |
| outline | border width | - | 2 | 2 | 2 | [[Ring Block]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: yes (stroke_width of the path) |
| heavy | border width | - | 4 | 4 | 4 | [[Ring Block]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: yes (stroke_width of the path) |
| ring | border color | - | N/A: the owner supplies the role; the block has no default stroke colour | N/A: same as default | N/A: same as default | tess-shell:src/tess_shell/binder/tables.py | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color); tre: yes (stroke_color of the path) |
| ring | corner radius | `shape.full` | 9999 | 9999 | 9999 | [[Shape]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: the roundness is the Diameter path, there is no radius key; tre: n/a: a path has no box and ignores corner_radius |
| ring | font | - | N/A: the block draws no text | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: the block draws no text; tre: n/a: the path draws no text |
| ring | icon size | - | N/A: the block draws no icon | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: the block draws no icon; tre: n/a: the path draws no icon |
| ring | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook (the Ring has no Elevation or Shadows key); tre: yes (shadows) |

Stroke thickness does not change with density. The 24 dp minimum is the owner's hit area (48 in touch contexts), not the painted size.

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
