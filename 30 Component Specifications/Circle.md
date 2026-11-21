---
title: Circle
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, shape, primitive]
related: ["[[Ring Block]]", "[[Rectangle Block]]", "[[Path Block]]", "[[Shape]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Shape]]", "[[Colour Roles]]"]
aliases: ["Circle block"]
---

# Circle

> [!info] Summary
> A Circle is a childless block that paints a filled disc of a given diameter, with an optional border: status dots, avatars' backgrounds, radio dots. No MD3 counterpart as a block ([Shape](https://m3.material.io/styles/shape/overview), corner `full`). Source of truth in code: see Status in code.

## Purpose

Draw a disc whose size comes from `Diameter`.

## When to use and not

- Use when: a dot, a badge disc or a round indicator is needed.
- Do not use when: only an outline is needed ([[Ring Block]]); a rounded rectangle with radius `full` is needed (use [[Rectangle Block]] with `Corner_Radius` equal to half the shorter side); children are needed ([[Box]]).

## Anatomy

1. Disc fill (`Fill`).
2. Border (`Border_Width`, `Border_Color`), centred on the outline in the engine path stroke.
3. Diameter: one number; `Width` and `Height` are not keys.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Dot | status marker | `Diameter` 8 dp |
| Badge | counter background | `Diameter` 16 dp |
| Large | avatar background | `Diameter` 40 dp |

Sizes are Tesserae choices; MD3 badges are 6 dp (small) and 16 dp (large) in Material Web `md-badge`-like tokens #needs-verification.

## States

Not applicable: no states of its own; `Fill` changes through `Transition` keys.

## Tokens used

Fill and border roles ([[Colour Roles]]); no radius (a circle). Diameter from a size the owning element sets; spacing steps from [[Spacing and Density]].

## Sizing and density

Not applicable: the diameter is set by the owner and does not scale with density. A Circle that is a pointer target has a hit area of 24 dp at least (48 dp in touch contexts), larger than a dot painted at 8 dp: the owner adds a transparent [[Box]] hit area.

## Layout and overflow

- A square box of `Diameter`; in a flex container `Flex_Shrink` 0 keeps it round.
- Never clips, never scrolls.
- Hit testing: the block is a path with hit shape `PAINTED`: only the disc (and border) takes pointer events; the corners of its box pass through.

## Behaviour

Pointer events only if a handler is set; not focusable.

## Tooltip and overlay behaviour

Not applicable: decorative; a status dot that carries meaning belongs to a control that has the tooltip ([[ADR-0004 Tooltip rule]]).

## Motion

`Transition` on `Fill`, `Opacity`; reduced motion makes it immediate. A pulsing dot is not specified.

## Accessibility

Role none, hidden from assistive technology unless `Label` is set. A dot that is the only carrier of a state (online) has a `Label` and a second cue (text or shape), never colour alone (WCAG 2.2 SC 1.4.1); contrast of the disc against its background at least 3 to 1 when it carries meaning (SC 1.4.11).

## Dark and light

Roles per scheme.

## Defaults

`Diameter` required, no fill, no border, hit shape painted, hidden from AT.

## Acceptance criteria

- [ ] AC-BLK-CIR-1 (geometry check): a Circle with `Diameter: 16` lays out 16 by 16 dp and is round: the disc pixels at the four box corners are background.
- [ ] AC-BLK-CIR-2 (scripted input): a click at the box corner passes to the node behind; a click at the centre is delivered to the Circle.
- [ ] AC-BLK-CIR-3 (token test): `Fill` and `Border_Color` resolve to role names; zero literals.
- [ ] AC-BLK-CIR-4 (AT tree assertion): a Circle without `Label` is absent from the tree; a meaningful dot has a name and an adjacent text cue.
- [ ] AC-BLK-CIR-5 (contrast script): a meaningful Circle against its background has at least 3 to 1 in light and dark.
- [ ] AC-BLK-CIR-6 (token test): `Width` and `Height` keys are rejected on a Circle by the schema (only `Diameter`).

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py`, `tess-shell:src/tess_shell/binder/shapes.py` (`circle_data`) | meets: tre `path`, `Diameter` required, hit shape painted by default |
| tess-ui | none (`Rect` with `Corner_Radius` equal to half) | absent as a block |
| tre | `tre:docs/reference/paint.md` (hit testing a path, `hit_shape` since 0.5.9) | meets |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Disc as a block | no MD3 block; shape scale has `full` only as a corner value | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/shapes.py`, `shell-vault:41 TDL Reference/Block Reference.md`.
- `tre:docs/reference/paint.md`.
- MD3 shape (JavaScript app #needs-verification): https://m3.material.io/styles/shape/overview. WCAG 2.2 SC 1.4.1, 1.4.11: https://www.w3.org/TR/WCAG22/.
