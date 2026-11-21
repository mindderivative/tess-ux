---
title: Image
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, content, image]
related: ["[[Image|Image Node]]", "[[SVG]]", "[[Video Player]]", "[[Icon Button]]", "[[Iconography]]", "[[Iconography#Fallback icon|Empty and Error States]]", "[[Loading States]]", "[[Error States]]", "[[Panel and Surface]]", "[[Colour Roles]]", "[[Shape]]", "[[Motion]]", "[[Spacing and Density]]", "[[Scrim]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0007 Icon set and Material Symbols deviation]]"]
depends_on: ["[[Shape]]", "[[Colour Roles]]", "[[Iconography]]"]
---

# Image

> [!info] Summary
> A raster picture (PNG, JPEG, GIF, WebP) fitted into a box, clipped to a shape, with a placeholder while it loads and an error image when it cannot. Material Design 3 has no image component; the spec rests on the MD3 [shape scale](https://m3.material.io/styles/shape/corner-radius-scale), the media area of cards and WAI-ARIA image rules. Source of truth in code: see Status in code.

## Purpose

Show content pictures (a photo, an avatar, a thumbnail, an album cover) predictably: the box size is known before the file is read, the picture never distorts silently, loading and failure are visible, and assistive technology gets the right text.

## When to use and not

- Use when: the picture is content or an identity mark loaded from a file or bytes (raster).
- Do not use when: the graphic is a vector icon or illustration that must follow the theme colour (use [[SVG]] or an icon, [[Iconography]]); the pictures are video frames with controls (use [[Video Player]]); the picture is a background texture of a surface (use the surface fill, [[Panel and Surface]]).

## Anatomy

1. Box: the fixed rectangle that owns the layout size.
2. Picture: the decoded pixels, fitted into the box by the fit mode.
3. Clip shape: a corner radius from [[Shape]] (or a circle) that masks the picture.
4. Placeholder: shown while there is no source or the picture is loading.
5. Error image: shown when the file cannot be read or decoded.
6. Scrim (optional, text on picture): a `scrim` layer at 60 percent behind overlaid text ([[Scrim]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Rectangular | photos, thumbnails | radius `none` or a token (`extra_small` 4, `small` 8, `medium` 12) |
| Rounded card media | the media area of a card | radius `medium` 12 on the outer corners only (`extra_small_top`-style shorthand: top corners) |
| Avatar | a person or an account | square box, radius `full`, so the clip is a circle |
| Pill | a wide banner image | radius `full` on a non-square box clips to a pill |
| Decorative | a picture with no information | no accessible name, hidden from assistive technology |
| Informative | a picture that carries information | has an alt text (accessible name) |

Clipping shapes. The baseline clip is a corner radius: any token of the scale `none` 0, `extra_small` 4, `small` 8, `medium` 12, `large` 16, `extra_large` 28, `full`, or a different radius on each corner. `full` is clamped to half the shorter side (a circle on a square, a pill otherwise) ([[Shape]], rule 2). Clipping to a path or a polygon (the Expressive shape set) is not in the baseline; the engine can mask a node with a circle, a rounded rectangle or a path, but no toolkit style passes one on, so a path mask needs a named adoption and a request.

## States

| State | Visual change | Token values |
|---|---|---|
| Empty (no source) | placeholder drawn | container `surface_container_highest`, icon `image` in `on_surface_variant` |
| Loading | placeholder stays; no spinner for a local file | as Empty |
| Loaded | picture fades in over 200 ms | see Motion |
| Error | error image: icon `image-broken-variant` centred on `surface_container_highest`, in `on_surface_variant` | [[Iconography]] |
| Pressed / hover / focus | only when the image is interactive (a click handler): the state layer and focus ring of the owning control apply; a plain image has none | [[State Layers]], [[Focus Ring]] |
| Disabled | not applicable: a picture has no disabled state; an interactive image shows its owner's state | |

An error is not shown by colour only: the broken-picture glyph differs from the placeholder glyph.

## Tokens used

Colour: `surface_container_highest` for placeholder and error backgrounds, `on_surface_variant` for their glyphs ([[Colour Roles]]). Shape: the corner scale ([[Shape]]). Motion: `short4` 200 ms with `standard` for the fade-in ([[Motion]]). Spacing: none; the box size is set by the owner. Glyph names: Pictogrammers Material Design Icons ([[ADR-0007 Icon set and Material Symbols deviation]]): `image-outline` for the placeholder, `image-broken-variant` for the error. The shell vault says `image-missing`, a name not in the mdi set; code uses `mdi:image-broken-variant` (`tess-shell:src/tess_shell/model/icons.py`) ([[Gaps and Contradictions]]).

## Sizing and density

The picture size is content, set by the owner; density does not change it. Defaults when the owner sets none: 96 by 96 dp (the shell) and the file's pixel size divided by the scale factor, capped to the container, in tess-ui #needs-verification. Avatar sizes follow the control heights so an avatar in a row fits: 40, 32 and 24 dp at default, compact and dense for a row avatar; 96 dp for a profile picture.

| Level | Row avatar (inside a list row) | Thumbnail in a row | Placeholder and error glyph |
|---|---|---|---|
| default | 40 | 40 | 50 percent of the box, at most 48 dp |
| compact | 32 | 32 | 50 percent, at most 32 dp |
| dense | 24 | 24 | 50 percent, at most 20 dp |

- An interactive image has a hit area of at least 24 dp by 24 dp at every level, 48 dp in a touch context ([[ADR-0002 Desktop density levels and target sizes]]); a plain image has none.
- Limits: a side above 4096 pixels is refused with one warning in the shell; the engine accepts a side up to 8192 pixels (`tre:docs/reference/properties.md`, image). The spec takes 4096 as the toolkit limit.

## Layout and overflow

- The box size is fixed before loading: loading and the error state never change the layout size (a layout-stability rule: the content around it does not shift).
- Fit modes: `contain` shows the whole picture inside the box, letterboxed in the box's background; `cover` fills the box and crops the overflow, centred on the picture's centre; `fill` stretches to the box and distorts when the ratios differ; `none` (shell) draws at the picture's own size, clipped to the box. Default `contain`: it never crops content silently. A photo thumbnail uses `cover` by an explicit choice. `fill` is for decorative use only (distortion changes meaning).
- The picture is turned upright by its EXIF orientation before fitting (tess-ui does).
- The clip applies after fitting: the picture's corners outside the radius show the box background, not the picture.
- An overlay text on a picture sits on a `scrim` at 60 percent so it keeps 4.5 to 1 (black at 60 percent over white gives #666666, 5.7 to 1 against white text, computed for this note).
- The box never scrolls its own content; a picture bigger than the available space is scaled by the fit mode, never clipped by a scrollbar. A scroll container around it is [[Scrollbar and Scroll Container]]'s concern.
- An animated GIF shows its first frame; no autoplay (an animation of over 5 s needs a pause control, [WCAG 2.2.2](https://www.w3.org/TR/WCAG22/#pause-stop-hide)).

## Behaviour

- Pointer: a plain image takes no pointer events. An image with a click handler is an interactive control and gets the pointer, focus and keyboard rules of [[Icon Button]] (Enter and Space activate it).
- Keyboard: a plain image is not in the Tab order.
- Touch: as pointer; an interactive image has a 48 dp hit area in a touch context.
- Loading: decoding runs off the UI thread; the placeholder shows until the pixels are ready; a changed source keeps the old picture until the new one is ready, then fades to it (no flash of the placeholder). A failed reload shows the error image and one log warning per path, not one per frame.
- Pixels are cached by path and modification time; a changed file reloads on the next show.
- Paths: a source path is relative to the file that names it and stays inside that directory; an absolute path or one that leaves it is refused (tess-ui).

## Tooltip and overlay behaviour

A plain image has no tooltip. An interactive image carries a tooltip on the image itself ([[ADR-0004 Tooltip rule]]) whose text repeats or adds to its name; never on a parent. An image never opens an overlay by itself.

## Motion

| Animation | Duration | Easing |
|---|---|---|
| Fade in on load | 200 ms (`short4`) | `standard` |
| Cross-fade when the source changes | 200 ms (`short4`) | `standard` |
| Placeholder to error | none (immediate) | |

Reduced motion: the picture appears in one frame; no cross-fade ([[Motion]], rule 4). A first load that was ready before the first paint has no fade.

## Accessibility

- Role: `img` for an informative image; none (hidden) for a decorative one ([WAI-ARIA img](https://www.w3.org/TR/wai-aria-1.2/#img)). An interactive image has role `button` (or `link`) and the name of its action, not a description of the picture.
- Name: the alt text states what the picture shows or what it does, in about 80 characters or fewer, without "image of". It is required for an informative image; without it the picture is decorative and hidden ([WCAG 1.1.1](https://www.w3.org/TR/WCAG22/#non-text-content)). An avatar names the person ("Ada Lovelace"). An informative image whose alt is missing fails AC-IMG-5 in review.
- Error: when an informative image fails to load its accessible name stays the alt text and its description becomes "Could not load the image" so the loss is not silent; a decorative image that fails exposes nothing.
- Announcements: none. Loading and failure are not live events; a failure the user must handle is reported by the owner ([[Error States]]).
- Contrast: placeholder and error glyph against their background at least 3 to 1 ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); overlaid text 4.5 to 1.
- Images are not inverted or tinted in dark theme.

## Dark and light

The picture is the same in both themes. The placeholder and error colours are roles and follow the scheme. The raster `error.png` that the shell ships cannot follow the theme (a light-theme picture on a dark bar); the spec replaces it with the themed glyph.

## Defaults

Fit `contain`, radius `none`, decorative (hidden) without an alt, placeholder icon `image-outline` on `surface_container_highest`, error glyph `image-broken-variant`, fade-in 200 ms, first frame of an animated GIF, side limit 4096 pixels.

## Acceptance criteria

- [ ] AC-IMG-1 (geometry check): the box size is the owner's size before the picture is read and does not change in the states empty, loading, loaded and error (bounds equal at each); with no owner size the shell default is 96 by 96 dp. Pass: bounds identical in all four states within 0.5 dp.
- [ ] AC-IMG-2 (pixel check): for a 200 by 100 picture in a 100 by 100 dp box: `contain` draws 100 by 50 dp centred with the box background above and below, `cover` draws the middle 100 by 100 dp of the picture with no letterbox, `fill` draws 100 by 100 dp stretched. Pass: sampled pixels at the letterbox and at the picture's centre match within 2 levels.
- [ ] AC-IMG-3 (pixel check): in a 64 by 64 dp box with radius `full` the pixel at (1,1) from a corner is the box background and the pixel at the centre of an edge is the picture; with radius `medium` the corner arc has radius 12 dp (within 1 px); with per-corner radii only the named corners are round. Pass: pixels equal at scale 1.0 and 2.0 (as AC-SHP-3).
- [ ] AC-IMG-4 (scripted input): with no source the placeholder shows (`surface_container_highest` with the `image-outline` glyph); with a missing file the error image shows (the `image-broken-variant` glyph, different pixels from the placeholder) and exactly one warning is logged for repeated renders; a valid file replaces the placeholder with the picture. Pass: pixel and log-count equal.
- [ ] AC-IMG-5 (AT tree assertion): an informative image has role `img` and a non-empty name; a decorative image is absent from the tree; an interactive image has role `button` and the action's name; a failed informative image has description "Could not load the image". Pass: tree walk equals the expected list.
- [ ] AC-IMG-6 (scripted input): with reduced motion off the picture reaches full opacity in 200 ms (within 2 frames); with it on, in the first frame after it is ready. Pass: frame counts equal.
- [ ] AC-IMG-7 (scripted input): replacing the source of a loaded image keeps the old picture until the new pixels are ready, then cross-fades; the placeholder does not appear in between. Pass: no frame shows the placeholder pixels.
- [ ] AC-IMG-8 (scripted input): a file with a side of 4097 pixels shows the error image and one warning; a JPEG with EXIF orientation 6 is drawn upright; an animated GIF draws its first frame and no later frame in 3 s. Pass: pixels and counts equal.
- [ ] AC-IMG-9 (scripted input): a path that is absolute or leaves the view directory is refused with a message naming the widget and the path, and the view does not draw a picture from it. Pass: error raised, no picture.
- [ ] AC-IMG-10 (contrast script): the placeholder and error glyph (`on_surface_variant`) against `surface_container_highest` at least 3 to 1 in light, dark and high contrast; overlaid white text on a 60 percent `scrim` over a white picture at least 4.5 to 1. Pass: no ratio below the limit.
- [ ] AC-IMG-11 (geometry check): an interactive image has a hit area of at least 24 by 24 dp (48 in a touch context), takes Tab focus, shows the ring of [[Focus Ring]] and activates on Enter and Space; a plain image is not in the Tab sequence. Pass: bounds and sequence equal.
- [ ] AC-IMG-12 (review): every informative image in a view has an alt text of 80 characters or fewer, not starting with "image of"; every avatar is named; every decorative image has none. Pass: reviewer finds no violation, name and date recorded.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/widgets/media.py` (`image`), `tess-ui:docs/components/images.md`; the TDL `Image` is the engine node | partly meets: PNG, JPEG, GIF, WebP decoded with EXIF orientation, `cover` default in the view and `fill` default in the Python widget (AC-IMG-2 fails on the default; the two defaults disagree), `Corner_Radius` token or `full` clips (AC-IMG-3 meets by reading), `Alt` makes it `img` and absent `Alt` hides it (AC-IMG-5 meets for decorative and informative), relative-path rule (AC-IMG-9 meets by reading); no placeholder, no error image, a missing file stops the view opening (AC-IMG-4 fails), no fade (AC-IMG-6 fails), no side limit stated (AC-IMG-8 unmeasured), no path mask other than the radius |
| tess-shell | `tess-shell:src/tess_shell/shipped/Image/Image_Module.tdl`, `tess-shell:src/tess_shell/shipped/Images/error.png`, `tess-shell:docs/guide/modules.md` (Image) | partly meets: 96 by 96 default, `Fit` CONTAIN default, COVER, FILL, NONE, first frame of a GIF, 4096 by 4096 limit with the error image and one warning, hidden unless the call has a `Label` (AC-IMG-1 meets by reading, AC-IMG-5 meets for decorative, AC-IMG-8 meets by reading); `Placeholder` shows only while there is no `Source`, not while loading and not on failure (AC-IMG-4 fails partly); the error image is a fixed raster, not the themed glyph (AC-IMG-10 unmeasured); no fade (AC-IMG-6 fails); no clip shape beyond the stylesheet radius |
| tre | `tre:docs/reference/properties.md` (Image: `rgba`, `pixel_width`, `pixel_height`, `fit`), `tre:crates/engine-render/src/image_cache.rs` | not applicable as a component: the node draws straight-alpha RGBA8 pixels with `fill`, `contain` or `cover`; it decodes no format and has no placeholder |

Evidence: [[Gaps and Contradictions]] (Image clip to any shape except circle through the `avatar` class; fallback icon name differs between vault and code).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/widgets/media.py` | exists, partial |
| tess-shell | `tess-shell:src/tess_shell/shipped/Image/Image_Module.tdl` | exists, partial |
| shell vault | `shell-vault:50 Design System/Standard Modules.md`, `shell-vault:40 Specifications/Modules/Media Module.md` | design intent |
| tre | the [[Image|Image Node]] | mechanism |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| An Image element is specified at all | MD3 has no image component; the spec uses the shape scale and card media rules | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Default fit `contain` (tess-ui view default is `cover`) | cropping loses content silently; cropping is an explicit choice | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Themed glyph error image instead of the shell's raster `error.png` | the glyph follows light, dark and high contrast | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Clip shapes limited to the corner scale | path masks are an Expressive shape set | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Tooltip only on an interactive image | tooltips belong to controls | [[ADR-0004 Tooltip rule]] |

## Sources

- [Material Web shape tokens (v0_192)](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-shape.scss): corner scale 0, 4, 8, 12, 16, 28, full. The card media corner (12 dp outer corners) from [elevated card](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-elevated-card.scss) `corner-medium`. Verified 2026-11-21.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.1.1, 1.4.3, 1.4.11, 2.2.2; [WAI-ARIA 1.2 img](https://www.w3.org/TR/wai-aria-1.2/#img); [WAI image tutorial](https://www.w3.org/WAI/tutorials/images/) for informative versus decorative.
- Code: `tess-ui:docs/components/images.md`, `tess-shell:src/tess_shell/shipped/Image/Image_Module.tdl`, `tre:docs/reference/properties.md`.
- MD3 does not publish an image component; the avatar glyph sizes, row avatar sizes, 200 ms fade and 4096 limit are Tesserae choices #needs-verification-as-design-choice.
