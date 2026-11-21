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

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| image | height | - | N/A: no natural size in the engine; the owner sets `Height`, or `Fit: NONE` uses the pixel size | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| image | padding | - | N/A: the pixels fill the whole box; there is no content inset | N/A: same as default | N/A: same as default | tess-shell:src/tess_shell/binder/shapes.py | tess-ui: yes (style padding); tess-shell: n/a: the Bitmap has no Padding key and the pixels fill the box; tre: yes (padding) |
| image | margin | - | N/A: the parent container sets the outer space | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| image | gap | - | N/A: the block has no children | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: an Image has no children; tess-shell: n/a: the block has no children and no Spacing key; tre: n/a: the image has no children |
| image | border width | - | N/A: the block draws no border; a frame is a parent Box | N/A: same as default | N/A: same as default | tess-shell:src/tess_shell/binder/shapes.py | tess-ui: yes (style border_width); tess-shell: n/a: the Bitmap has no border key, the frame is the parent Box; tre: yes (stroke_width) |
| image | border color | - | N/A: the block draws no border; a frame is a parent Box | N/A: same as default | N/A: same as default | tess-shell:src/tess_shell/binder/shapes.py | tess-ui: yes (style border_color); tess-shell: n/a: the Bitmap has no border key, the frame is the parent Box; tre: yes (stroke_color) |
| clipping parent, cover art | corner radius | `shape.small` | 8 | 8 | 8 | [[Shape]] | tess-ui: yes (style corner_radius of the Image or its parent); tess-shell: yes (Corner_Radius of the parent Box with Clip_Children); tre: yes (corner_radius clips the image to the rounded box) |
| clipping parent, avatar | corner radius | `shape.full` | 9999 | 9999 | 9999 | [[Shape]] | tess-ui: yes (style corner_radius of the Image or its parent); tess-shell: yes (Corner_Radius of the parent Box with Clip_Children); tre: yes (corner_radius clips the image to the rounded box) |
| image | font | - | N/A: the block draws no text | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: an Image draws no text; tess-shell: n/a: the block draws no text; tre: n/a: the image draws no text |
| image | icon size | - | N/A: an image is not an icon; icons are Path blocks | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: an Image is not an icon; tess-shell: n/a: a Bitmap is not an icon; tre: n/a: an image is not an icon |
| image | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: no hook (the Bitmap has no Elevation or Shadows key, a parent Box carries the shadow); tre: yes (shadows) |

The radius rows belong to the clipping parent, which sets `Clip_Children`; a Bitmap has no radius of its own. Source images need at least twice the box pixels at scale 2.0.

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
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py`, `tess-shell:src/tess_shell/binder/shapes.py` (`bitmap`), `tess-shell:src/tess_shell/binder/images.py` | meets: `Source`, `Fit` (FILL, CONTAIN, COVER, NONE); decoding done by the shell; animated gif and tint not built. Settable: the Bitmap has no `Elevation` or `Shadows` key, so the elevation default cannot be changed on the block (project request) |
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
