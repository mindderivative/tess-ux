---
title: Path Block
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, shape, primitive, icon]
related: ["[[Circle]]", "[[Ring Block]]", "[[Rectangle Block]]", "[[Canvas]]", "[[Iconography]]", "[[Shape]]", "[[Colour Roles]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Iconography]]", "[[Colour Roles]]"]
aliases: ["Path", "Path Node", "Path block"]
---

# Path Block

> [!info] Summary
> A Path draws SVG path data, fitted into its box by a view box, with fill, stroke and a trim of the stroke: icons, custom shapes, progress arcs and spinners. MD3 icons are paths ([Icons](https://m3.material.io/styles/icons/overview)); the progress indicators animate a trimmed stroke ([Progress indicators](https://m3.material.io/components/progress-indicators/overview)). Source of truth in code: see Status in code.

## Purpose

Draw anything that is a vector outline: an icon, a frame corner, a ring segment, a check mark that draws on.

## When to use and not

- Use when: the shape is not a rectangle, circle or ring; an icon from the icon set ([[Iconography]]) needs a `d` and a `viewBox`; a stroke must be trimmed or morphed.
- Do not use when: a plain rectangle ([[Rectangle Block]]), disc ([[Circle]]) or ring ([[Ring Block]]) suffices; imperative drawing is needed ([[Canvas]]).

## Anatomy

1. Data: SVG path commands (M, L, H, V, C, S, Q, T, A, Z).
2. View box: `[min_x, min_y, width, height]` fitted uniformly and centred into the box.
3. Fill and stroke (`Border_Width` is the stroke; stroke width stays in pixels however the view box scales; round caps and joins).
4. Trim: `Trim_Start`, `Trim_End` from 0.0 to 1.0 by length over all sub-paths.
5. Hit shape: `PAINTED` or `BOX`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Icon | glyph from the icon set | filled, `view_box` 24 by 24, size 24 dp (20 dp at compact and dense) |
| Stroke | drawn line, arc | no fill, stroke 2 to 4 dp |
| Trimmed | progress or spinner | `Trim_End` animated 0 to 1 |

## States

Not applicable: no states of its own; the owning element changes `Fill` or `Border_Color` through `Transition`.

## Tokens used

Fill and stroke: roles ([[Colour Roles]]; an icon takes `on_surface` or the role of its control); icon sizes: 24 dp, 20 dp ([[Spacing and Density]]); motion: [[Motion]].

## Sizing and density

| Value | default | compact | dense |
|---|---|---|---|
| Icon size (box) | 24 | 20 | 20 |
| Hit area of an icon alone | 24 (touch 48) | 24 | 24 |

Icon sizes follow the Icon Button values of [[Spacing and Density]]. The hit area belongs to the control around the icon.

## Layout and overflow

- The path is fitted into the content box (box minus padding) and centred; it does not stretch.
- Ink outside the box: strokes are centred on the outline, so a stroke touching the view-box edge is clipped by the node bounds only if a parent clips.
- Never wraps, never scrolls. A path in a flex row has `Flex_Shrink` 0.
- Hit testing: default in the shell is `PAINTED` (fill region and stroke); the engine default is `BOX`. A click in the empty middle of a ring or a notch passes through with `PAINTED`.

## Behaviour

Pointer events if a handler is set; not focusable. Icons inside a button are `hit_testable` false so the button receives the click.

## Tooltip and overlay behaviour

Not applicable: an icon alone carries no tooltip; its control does ([[ADR-0004 Tooltip rule]]).

## Motion

- `Trim_End` 0 to 1 over 1000 ms draws a line on; moving both ends together makes an indeterminate spinner; `Data` morphs between shapes with the engine's `resample`, `structure` or `strict` modes ([[Motion]]).
- Reduced motion: a determinate trim jumps to its value; a spinner that conveys activity may keep moving at low amplitude, others stop ([[14 Accessibility Basics]]).

## Accessibility

Role none; hidden from AT unless `Label` is set. An icon that is the only content of a control names the control, not the Path ([[Icon Button]]). A decorative icon beside a label is `A11y_Hidden`. Contrast of a meaningful icon at least 3 to 1 (WCAG 2.2 SC 1.4.11).

## Dark and light

Roles per scheme; an icon uses `Foreground`/`Color` roles so it follows the theme.

## Defaults

`Data` required, hit shape painted (shell), no fill, no stroke (a path with neither takes no events), `Trim_Start` 0, `Trim_End` 1.

## Acceptance criteria

- [ ] AC-BLK-PTH-1 (geometry check): a 24 by 24 dp Path with `View_Box [0, 0, 24, 24]` and data touching the view-box edges paints inside the 24 by 24 box, centred, at scale 1.0 and 2.0.
- [ ] AC-BLK-PTH-2 (pixel check): `Trim_End: 0.5` on a stroked line paints half of its length (within 1 dp); `Trim_Start: 0.25, Trim_End: 0.75` paints the middle half.
- [ ] AC-BLK-PTH-3 (scripted input): with `Hit_Shape: PAINTED`, a click in the hollow of a ring path reaches the node behind and a click on its stroke is delivered; with `BOX` both are delivered.
- [ ] AC-BLK-PTH-4 (token test): fill and stroke colours resolve to role names.
- [ ] AC-BLK-PTH-5 (AT tree assertion): a Path without `Label` is absent from the tree; with `Label` it has that name.
- [ ] AC-BLK-PTH-6 (pixel check): under the reduced-motion preference an animated trim jumps to the final value in the first frame.
- [ ] AC-BLK-PTH-7 (geometry check): stroke width 2 stays 2 dp when the view box is 24 by 24 in a 48 dp box (not 4 dp).

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` (`Path`: `Data`, `View_Box`, `Trim_Start`, `Trim_End`, `Hit_Shape`, fill and border keys) | meets; reduced motion for trim is the module's job (AC-BLK-PTH-6 not verified) |
| tess-ui | `tess-ui:src/tess_ui/widgets/media.py` (`icon`, edges of the node graph use `path`) | partly meets: path edges exist; no named icon lookup |
| tre | `tre:docs/reference/paint.md` (Paths, hit testing, morphing), `tre:crates/engine-core/src/path.rs` | meets: `hit_shape` since 0.5.9, trim, morph |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Icon sizes 24, 20, 20 dp by density (MD3 24 dp) | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Icon set and its deviation | see the ADR | [[ADR-0007 Icon set and Material Symbols deviation]] |

## Sources

- `tess-shell:src/tess_shell/schema/blocks.py`, `shell-vault:41 TDL Reference/Block Reference.md` (Shapes, Path).
- `tre:docs/reference/paint.md`, `tre:docs/guide/painting.md` (Paths), `tre:docs/guide/animation.md` (Morphing paths).
- MD3 icons and progress (JavaScript apps #needs-verification): https://m3.material.io/styles/icons/overview, https://m3.material.io/components/progress-indicators/overview. Material Web progress: https://github.com/material-components/material-web/blob/main/docs/components/progress.md.
- WCAG 2.2 SC 1.1.1 and 1.4.11: https://www.w3.org/TR/WCAG22/.
