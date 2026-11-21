---
title: Rectangle Block
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, shape, primitive]
related: ["[[Box]]", "[[Circle]]", "[[Ring Block]]", "[[Path Block]]", "[[Shape]]", "[[Colour Roles]]", "[[Elevation]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Shape]]", "[[Colour Roles]]"]
aliases: ["Rectangle"]
---

# Rectangle Block

> [!info] Summary
> A Rectangle is a childless block that paints a filled, optionally bordered and rounded rectangle: dividers, swatches, progress tracks, backgrounds. MD3 has no shape primitive; the corner values come from the [Shape](https://m3.material.io/styles/shape/overview) scale. Source of truth in code: see Status in code.

## Purpose

Draw a plain shape whose size may be `AUTO` or `EXPAND`, which a path cannot take.

## When to use and not

- Use when: a divider (1 dp), a coloured bar, a track or a swatch is needed.
- Do not use when: children are needed (use [[Box]]); a circle or ring is needed ([[Circle]], [[Ring Block]]); a non-rectangular outline is needed ([[Path Block]]).

## Anatomy

1. Fill (`Fill`, a role).
2. Border (`Border_Width`, `Border_Color`), drawn inside the box.
3. Corner radius: one number or four (top-left, clockwise), from [[Shape]].
4. Optional shadow (`Elevation`, `Shadows`).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Divider | separate regions | height or width 1 dp, fill `outline_variant` |
| Track | progress or slider track | fill `surface_container_highest`, radius `full` |
| Swatch | colour preview | fill any role, border `outline` 1 dp |

## States

Not applicable: a Rectangle has no states. A Rectangle used as an indicator changes `Fill` through `Transition` keys at the direction of the owning element.

## Tokens used

Fill and border: [[Colour Roles]]; radius: [[Shape]] (0, 4, 8, 12, 16, 28 dp, `full`); shadows: [[Elevation]]. A literal colour is not allowed in a block.

## Sizing and density

Not applicable: no intrinsic size; set `Width` and `Height`. A divider is 1 dp thick at every density level; a Rectangle that is a pointer target takes the hit area of its element (24 dp, 48 dp in touch contexts, [[Spacing and Density]]).

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| rectangle | height | - | N/A: no intrinsic size; the owner sets `Width` and `Height` (`AUTO` or `EXPAND`) | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| divider | height | - | 1 | 1 | 1 | [[Rectangle Block]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| rectangle | padding | - | N/A: the block has no children to inset | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: a Rect has no children to inset; tess-shell: n/a: the block has no children and no Padding key; tre: n/a: the box has no children to inset |
| rectangle | margin | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | tess-shell:src/tess_shell/binder/tables.py | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| rectangle | gap | - | N/A: the block has no children | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: a Rect has no children; tess-shell: n/a: the block has no children and no Spacing key; tre: n/a: the box has no children |
| rectangle | border width | - | 0 | 0 | 0 | tess-shell:src/tess_shell/binder/tables.py | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| rectangle | border color | - | N/A: no border by default; `Border_Color` takes a role | N/A: same as default | N/A: same as default | tess-shell:src/tess_shell/binder/tables.py | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| swatch | border width | - | 1 | 1 | 1 | [[Rectangle Block]] | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| swatch | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| rectangle | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| track | corner radius | `shape.full` | 9999 | 9999 | 9999 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| rectangle | font | - | N/A: the block draws no text | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: a Rect draws no text; tess-shell: n/a: the block draws no text and has no font key; tre: n/a: the box draws no text |
| rectangle | icon size | - | N/A: the block draws no icon | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: a Rect draws no icon; tess-shell: n/a: the block draws no icon and has no icon key; tre: n/a: the box draws no icon |
| rectangle | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |

The divider is 1 dp at every density; its fill is `outline_variant` and a track fills with `surface_container_highest`.

## Layout and overflow

- No children, no padding. Never clips anything; the shape itself is clipped to nothing.
- A Rectangle in a flex container shrinks per `Flex_Shrink`; a divider sets `Flex_Shrink` 0 and a fixed thickness.
- Hit testing: the block is a rounded box, so it is hit over its whole rounded rectangle also when its fill is transparent. The `Hit_Shape` key of [[Path Block]] is not offered; a Rectangle that must let clicks through sets `hit_testable` false through its element.

## Behaviour

Pointer events and `On_Click` only if a handler is set; not focusable.

## Tooltip and overlay behaviour

Not applicable: decorative.

## Motion

`Transition` on `Fill`, `Border_Color`, `Opacity` with duration and easing from [[Motion]]; reduced motion makes it immediate.

## Accessibility

Role none; hidden from assistive technology unless `Label` is set; a Rectangle that carries meaning alone (a colour swatch) has a `Label` naming the colour in words and never relies on colour alone (WCAG 2.2 SC 1.4.1). A divider is `A11y_Hidden`, or `Role: SEPARATOR` where the divider separates focusable groups.

## Dark and light

Roles resolve per scheme; a divider keeps 3 to 1 non-text contrast only when it is the only cue for a boundary, otherwise it is decorative (WCAG 2.2 SC 1.4.11).

## Defaults

Transparent fill, no border, radius 0, no shadow, role none, hidden from AT.

## Acceptance criteria

- [ ] AC-BLK-RCT-1 (pixel check): a Rectangle of 100 by 40 dp with `Fill: primary` and radius 12 paints the role colour inside and nothing outside; the corner pixels at (0, 0) are background.
- [ ] AC-BLK-RCT-2 (geometry check): `Border_Width` 2 draws inside the box: the laid-out size is unchanged and the border pixels lie within the box.
- [ ] AC-BLK-RCT-3 (geometry check): a divider with height 1 is exactly 1 dp (2 px at scale 2.0) at each density level.
- [ ] AC-BLK-RCT-4 (token test): `Fill`, `Border_Color` and every radius in shipped styles resolve to role or [[Shape]] names; zero literals.
- [ ] AC-BLK-RCT-5 (AT tree assertion): a Rectangle without `Label` is absent from the tree; with `Label: "Accent colour blue"` it is exposed with role `img` or `none` and that name.
- [ ] AC-BLK-RCT-6 (scripted input): a click in the clipped-away corner of a 12 dp radius reaches the node behind; a click inside the rounded area is delivered to the Rectangle.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` (`Rectangle`: tre `box`, keys `Fill`, `Border_*`, `Corner_Radius`, `Margin`, `Opacity`, `Elevation`, `Shadows`) | meets AC-BLK-RCT-1 to 4; `Hit_Shape` not offered, so the shape hit default is the box (the Block Reference says painted; fails that statement, AC-BLK-RCT-6 holds for rounded corners) |
| tess-ui | `tess-ui:src/tess_ui/views/*_View.tdl` (`Rect`) | partly meets: roles for fill, radius names |
| tre | `tre:docs/reference/paint.md` (boxes, corner radius), `tre:docs/reference/node.md` (`hit_testable`) | meets |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Shape primitive with no MD3 counterpart | Tesserae shell blocks draw dividers and tracks | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tess-shell:src/tess_shell/binder/tables.py`, `shell-vault:41 TDL Reference/Block Reference.md` (Shapes).
- `tre:docs/guide/painting.md` (Boxes), `tre:docs/reference/node.md`.
- MD3 shape (JavaScript app #needs-verification): https://m3.material.io/styles/shape/overview.
- WCAG 2.2 SC 1.4.1 and 1.4.11: https://www.w3.org/TR/WCAG22/.
