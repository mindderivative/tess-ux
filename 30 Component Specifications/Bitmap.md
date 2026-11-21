---
title: Bitmap
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, image, primitive]
related: ["[[Path Block]]", "[[Rectangle Block]]", "[[Iconography]]", "[[Shape]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Tree]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[14 Accessibility Basics]]"]
aliases: ["Bitmap block"]
---

# Bitmap

> [!info] Summary
> A Bitmap shows decoded raster pixels from a file, fitted into its box (album art, photographs, avatars). MD3 has no image block; images in components follow [Shape](https://m3.material.io/styles/shape/overview) for corners. Source of truth in code: see Status in code.

## Purpose

Show a raster image that is not an icon, with a defined fit and an accessible alternative.

## When to use and not

- Use when: the content is a photograph, cover art or screenshot.
- Do not use when: the image is an icon or logo that must follow the theme (use an SVG or [[Path Block]], see [[Iconography]]); a flat colour is needed ([[Rectangle Block]]).

## Anatomy

1. Pixels: decoded by the shell, handed to the engine as RGBA8.
2. Fit: `FILL` (stretch), `CONTAIN` (letterbox), `COVER` (crop), `NONE` (pixel size).
3. Optional mask or radius by a parent that clips ([[Shape]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Contain | cover art whole | `Fit: CONTAIN` (default), empty bars show the parent colour |
| Cover | avatar, banner | `Fit: COVER`, crops |
| Native size | pixel-exact art | `Fit: NONE`, box sized by pixels |

## States

Not applicable: a Bitmap has no states; `Opacity` fades it.

## Tokens used

Corner radius from [[Shape]] on the clipping parent (cover art 8 dp, avatar `full`); no colour of its own.

## Sizing and density

Not applicable: size is set by the owner; image pixels are decoded to at most 8192 by 8192 (engine limit). For a 2.0 scale factor the source should have at least twice the box pixels, otherwise it is upscaled (blurred).

## Layout and overflow

- Fit decides overflow: `CONTAIN` never overflows, `COVER` crops to the box, `FILL` distorts, `NONE` may exceed the box and is clipped by the parent only if it clips.
- The engine has no natural size for an image: width and height are set, or the pixel size is used with `Fit: NONE`.
- No wrapping, no scrolling.
- Hit testing: any image is hit-testable as its box.

## Behaviour

Pointer events if a handler is set; not focusable.

## Tooltip and overlay behaviour

Not applicable: an image carries no tooltip; a control around it does.

## Motion

`Opacity` by `Transition`; cross-fade of changed artwork is 200 ms `easing-standard` ([[Motion]]) #needs-verification (design choice); reduced motion: immediate. Video is the same node with frames set; not specified.

## Accessibility

- Role none and hidden from AT unless `Label` is set (shell default). An informative image has a `Label` that states its content in words (WCAG 2.2 SC 1.1.1); a decorative image stays hidden.
- Text embedded in an image is not allowed for information; the same text is in the name or the description.

## Dark and light

No change; a bitmap is not recoloured. A transparent image sits on a role colour that keeps 3 to 1 contrast for its meaningful parts.

## Defaults

`Source` required, `Fit` CONTAIN, hidden from AT, opacity 1.

## Acceptance criteria

- [ ] AC-BLK-BMP-1 (pixel check): a 100 by 50 px image in a 100 by 100 dp Bitmap with `Fit: CONTAIN` paints 100 by 50 dp centred with 25 dp bars; with `COVER` it fills 100 by 100 with the sides cropped; with `FILL` it fills 100 by 100 stretched.
- [ ] AC-BLK-BMP-2 (geometry check): `Fit: NONE` lays out the box at the image pixel size.
- [ ] AC-BLK-BMP-3 (AT tree assertion): a Bitmap with `Label` exposes role `img` or equivalent with that name; one without is absent.
- [ ] AC-BLK-BMP-4 (scripted input): a file larger than 8192 px on a side is rejected with an error that names the file and the limit.
- [ ] AC-BLK-BMP-5 (pixel check): a Bitmap inside a parent with `Clip_Children` and radius 8 has no ink outside the rounded corner.
- [ ] AC-BLK-BMP-6 (review): every informative Bitmap in a module has a `Label`; a reviewer finds none without one.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py`, `tess-shell:src/tess_shell/binder/shapes.py` (`bitmap`), `tess-shell:src/tess_shell/binder/images.py` | meets: `Source`, `Fit` (FILL, CONTAIN, COVER, NONE); decoding done by the shell; animated gif and tint not built |
| tess-ui | `tess-ui:src/tess_ui/widgets/media.py` (`image`) | partly meets: image widget with fit, accessibility `Label` optional |
| tre | `tre:docs/guide/painting.md` (Images) | meets: `image` kind, RGBA8 only, `fit` fill, contain, cover |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Image block with four fit modes | shell block set; MD3 has no image primitive | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tess-shell:src/tess_shell/schema/blocks.py`, `shell-vault:41 TDL Reference/Block Reference.md` (Bitmap).
- `tre:docs/guide/painting.md`, `tre:docs/reference/properties.md` (Image).
- WCAG 2.2 SC 1.1.1 Non-text Content: https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html.
- MD3 shape (JavaScript app #needs-verification): https://m3.material.io/styles/shape/overview.
