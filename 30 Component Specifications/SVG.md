---
title: SVG
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, content, svg, block]
related: ["[[SVG|SVG Block]]", "[[SVG|SVG Node]]", "[[Path Node]]", "[[SVG|Animated Icon]]", "[[Image]]", "[[Iconography]]", "[[Icon Button]]", "[[Colour Roles]]", "[[Motion]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0007 Icon set and Material Symbols deviation]]"]
depends_on: ["[[Iconography]]", "[[Colour Roles]]", "[[Motion]]"]
---

# SVG

> [!info] Summary
> A vector document drawn as one scene, scaled to fit its box and centred, whose `currentColor` follows the theme. Material Design 3 uses SVG for icons and illustrations but has no SVG component: the counterpart is [Icons](https://m3.material.io/styles/icons/overview). The block is the author-facing element; the engine node is [[SVG|SVG Node]] and the shell block is [[SVG|SVG Block]]. Source of truth in code: see Status in code.

## Purpose

Draw icons, logos and illustrations that stay sharp at any size and any scale factor and take their colour from the theme, so light, dark and high contrast need no second asset.

## When to use and not

- Use when: the graphic is vector (an icon, a logo, an illustration) and a monochrome part should follow the theme.
- Do not use when: the graphic is a photograph or other raster (use [[Image]]); an icon from the shipped icon set is enough (use the icon facility, [[Iconography]]; an icon name is simpler than an SVG file); a simple progress or custom shape is drawn at run time (use [[Path Node]]).

## Anatomy

1. Box: the layout rectangle with the owner's width and height.
2. Document: the parsed SVG scene (shapes, gradients, clips, masks, text, embedded raster images).
3. Viewport fit: the document's viewBox scaled uniformly (`meet`) and centred in the box.
4. Current colour: the colour that `currentColor` resolves to inside the document.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Themed monochrome | icons, simple logos | fills and strokes use `currentColor`; the colour is the owner's `Foreground` role |
| Multicolour | illustrations, brand logos | fixed colours in the document; not themed |
| Animated | an animated icon or spinner | the document carries SMIL animation, sampled by the `svg_time` property ([[SVG|Animated Icon]]) |
| Informative | the graphic carries meaning | has an alt text |
| Decorative | the graphic only decorates | hidden from assistive technology |

## States

A plain SVG has no interaction states. When it is an interactive control (an icon with a click handler) it uses the states of [[Icon Button]]; the document does not draw them.

| State | Visual change | Token values |
|---|---|---|
| Rest | document drawn, `currentColor` = the owner's colour role (default `on_surface`) | role |
| Disabled (owner disabled) | `currentColor` becomes `on_surface` at 38 percent | [[State Layers]] |
| Error (parse or file failure) | the document is not drawn; the view fails to open with the widget name and file, or the error glyph shows (see Behaviour) | |
| Loading | not applicable: a local document is parsed before the first frame | |

## Tokens used

Colour: the owner's `Foreground` role for `currentColor` (default `on_surface`; `primary` for an accent logo; `on_surface_variant` for a quiet icon), see [[Colour Roles]]. Fixed colours inside a multicolour document are the document's own and are not roles. Motion: SMIL timing is the document's; reduced motion rule below ([[Motion]]). Sizes: [[Iconography]] (24 dp viewBox for icons; sizes 24, 20, 20 by density).

## Sizing and density

The box is set by the owner. For an icon the size follows the icon sizes of [[Iconography]] and the density of its container.

| Level | Icon box | Notes |
|---|---|---|
| default | 24 dp | MD3 icon size |
| compact | 20 dp | as [[Icon Button]] icon |
| dense | 20 dp | as [[Icon Button]] icon |

- An illustration or logo has the owner's size; with no size given, the document's own width and height (shell: #needs-verification) apply, capped to the container.
- An interactive SVG has a hit area of at least 24 by 24 dp (48 in a touch context); a plain one has none.
- Stroke widths inside the document scale with the box, so a 24 dp icon at 20 dp has strokes 20/24 as wide; a project that needs a constant stroke supplies a path with non-scaling stroke #needs-verification.

## Layout and overflow

- The document is fitted uniformly into the box (`xMidYMid meet`): no distortion; a box with a different ratio leaves empty bands, centred. There is no `Fit` option (tess-shell); a different crop needs a different viewBox.
- The box clips the document: shapes outside the viewBox are not drawn.
- A box with only a width or only a height takes the other from the document's ratio.
- The SVG is vertically centred with adjacent text by the layout of its container; an icon beside a text line is centred on the text's line box within 1 px.
- Documents are limited to 2 MB of text and 10 000 path segments in total #needs-verification-as-design-choice, so a hostile or accidental document cannot stall the UI thread.

## Behaviour

- Pointer, keyboard, touch: none for a plain SVG; it is hit-test transparent unless it has a handler.
- Parsing: the shell or toolkit reads the file once and gives the document to the engine; a changed `Source` re-parses; a `.svgz` (gzip) is accepted.
- Failure: a missing file or a document that is not SVG is an error naming the widget and the file position; the shell raises it at load and the view does not open (tess-ui) or the module is replaced by the error glyph (spec). The spec requires a visible failure: the themed `image-broken-variant` glyph in `on_surface_variant` and one logged error per file.
- Security: scripts, event attributes and external references (a link to a file or a URL outside the document's directory) are not executed or fetched; an embedded raster image comes only from a `data:` URL or from a file next to the document. A reference that is refused draws nothing and logs one warning.
- Supported subset: the engine draws one blur or drop shadow filter at most and no blend modes; other filters are dropped (`tre:docs/reference/paint.md`). An icon that depends on a dropped filter may render differently and is rejected at authoring time ([[Iconography]]).

## Tooltip and overlay behaviour

A plain SVG has no tooltip. An interactive SVG carries a tooltip on itself ([[ADR-0004 Tooltip rule]]) and is an icon button in effect. An SVG opens no overlay.

## Motion

Static documents have no motion. A SMIL animation is sampled by `svg_time` seconds into the animation (`tre:docs/reference/paint.md`, SMIL animation); nothing advances it on its own, so the owner drives it with an animation of `svg_time`. Animation of a looping document must not exceed 3 flashes per second. Reduced motion: an animated SVG draws its first frame (`svg_time` 0) or a stated rest frame and does not advance; an animation that conveys activity follows the [[Progress Indicator]] rule (still form) ([[Motion]], rule 4). An animation longer than 5 s that starts automatically has a pause control or does not start.

## Accessibility

- Role: `img` for an informative SVG; hidden for a decorative one. An interactive SVG is a `button` or `link` with the action's name.
- Name: the alt text states what the graphic shows or means ("Tesserae logo"); for an icon inside a control the control's name is used and the icon is hidden. A `title` element inside the document is not used as the name (the document is opaque to the tree).
- Without an alt text the graphic is decorative and hidden (tess-ui, tess-shell: hidden unless a `Label` is set).
- Announcements: none.
- Contrast: monochrome content in `currentColor` at least 3 to 1 against the background for non-text, 4.5 to 1 if it contains text drawn as glyphs ([WCAG 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum), 1.4.11). A multicolour document does not change with the theme, so the author checks it against both schemes.
- Fixed colours are not the only carrier of state.

## Dark and light

A monochrome document in `currentColor` follows the scheme through the owner's role. A multicolour document is the same in both schemes. High contrast: the owner uses `on_surface` for `currentColor`.

## Defaults

Fitted `meet`, centred; `currentColor` = `on_surface`; decorative (hidden) without an alt; icon box 24 dp at default density.

## Acceptance criteria

- [ ] AC-SVG-1 (pixel check): a document of one circle with `fill="currentColor"` drawn with the owner's `Foreground` set to `primary` in the light scheme and again in the dark scheme paints the pixel at the circle's centre in the respective `primary` hex (#6750A4, #D0BCFF) within 2 levels. Pass: both equal.
- [ ] AC-SVG-2 (geometry check): a 100 by 50 viewBox document in a 100 by 100 dp box is drawn 100 by 50 dp and centred (25 dp bands above and below); a 50 by 100 viewBox is drawn 50 by 100 dp, centred horizontally; only width given: height follows the ratio. Pass: bounds equal within 0.5 dp at scale 1.0 and 2.0.
- [ ] AC-SVG-3 (pixel check): the same document drawn at 24 dp and at 48 dp (or scale 2.0) has crisp edges at both sizes: the rendered shape equals the vector rasterised at that size (difference at most 2 levels per sampled edge pixel), no bitmap scaling. Pass: sampled pixels equal.
- [ ] AC-SVG-4 (AT tree assertion): an informative SVG has role `img` and a non-empty name; a decorative one is absent from the tree; an interactive one has the role and name of its action; no `title` text from the document is used as the name. Pass: tree walk equals the expected list.
- [ ] AC-SVG-5 (scripted input): a missing file and a non-SVG document each produce one error that names the widget and the file, the themed error glyph (or a failed open) and exactly one log entry however many frames are drawn. Pass: error text, pixel and log count equal.
- [ ] AC-SVG-6 (scripted input): a document with a `<script>` element, an `onclick` attribute and an `<image href>` to a path outside its directory draws without running the script, without firing the handler and without reading the outside file (checked with a file-access probe); a `data:` image and a neighbouring file image draw. Pass: probe count 0 for the outside file; the allowed images draw.
- [ ] AC-SVG-7 (scripted input): a SMIL document with `svg_time` 0 draws its first frame; with reduced motion on, an owner animation of `svg_time` does not advance it (two frames 1 s apart are identical); with reduced motion off it advances. Pass: frame diff 0 and nonzero respectively.
- [ ] AC-SVG-8 (contrast script): `currentColor` roles used for icons (`on_surface`, `on_surface_variant`, `primary`) against `surface` and `surface_container` at least 3 to 1 in light, dark and high contrast (`on_surface_variant` on dark `surface` passes: #CAC4D0 on #141218). Pass: no ratio below 3.
- [ ] AC-SVG-9 (scripted input): a document over 2 MB, or with more than 10 000 path segments, is refused with the error glyph and one log entry in under 100 ms of parse time; a normal 5 KB icon parses in under 16 ms. Pass: times and outcomes equal (limits #needs-verification-as-design-choice).
- [ ] AC-SVG-10 (geometry check): an icon SVG has a box of 24, 20 and 20 dp at default, compact and dense; an interactive SVG has a hit area of at least 24 by 24 dp (48 in touch context) and takes Tab focus with the ring of [[Focus Ring]]. Pass: bounds equal and sequence equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/widgets/media.py` (`svg`), `tess-ui:src/tess_ui/spec/svg.py`, `tess-ui:docs/components/svg.md` | partly meets: whole document drawn, scaled to fit and centred, `Foreground` is `currentColor` (AC-SVG-1, AC-SVG-2 meet by reading), `Src` or `Content`, `.svgz`, raster `<image>` from `data:` URLs or neighbouring files decoded by the toolkit (AC-SVG-6 partly: scripts are ignored by the engine #needs-verification), `Alt` gives `img`, none hides (AC-SVG-4 meets by reading), a missing file stops the view opening with the widget name (AC-SVG-5 partly: no error glyph); no size limit (AC-SVG-9 fails); no reduced-motion handling of `svg_time` in the widget code read (AC-SVG-7 unmeasured) |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` (the [[SVG|SVG Block]]), `shell-vault:41 TDL Reference/Block Reference.md` | partly meets: `Source` or `Icon`, `Color` or `Foreground` for `currentColor`, uniform fit and centred, hidden unless `Label` (AC-SVG-1, AC-SVG-2, AC-SVG-4 meet by reading); an unknown icon is an error at its value name (AC-SVG-5 partly); `svg_images` is not exposed, so an embedded raster does not draw (AC-SVG-6: not applicable until exposed); default size from the document is #needs-verification; no reduced-motion rule for animation (AC-SVG-7 unmeasured) |
| tre | `tre:docs/reference/paint.md` (SVG documents), `tre:crates/engine-core/src/svg.rs`, `tre:crates/engine-core/src/svg_smil.rs` | not applicable as a component: the [[SVG|SVG Node]] parses and draws the scene, supports `svg_time` sampling and one blur or drop shadow filter only |

Evidence: [[Gaps and Contradictions]] (SVG node drops all filters except one blur or drop shadow; icon facility has no named lookup or size tokens).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/widgets/media.py`, `tess-ui:src/tess_ui/spec/svg.py` | exists, partial |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` | exists as the SVG block |
| tre | the [[SVG|SVG Node]] | mechanism |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| An SVG element is specified; MD3 specifies icons and no SVG component | the stack draws icons and illustrations as SVG documents | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Icons come from Material Design Icons (Pictogrammers), not Material Symbols; no variable axes (weight, fill, grade, optical size) | the stack ships that set | [[ADR-0007 Icon set and Material Symbols deviation]] |
| Reduced motion draws an animated SVG's first frame | MD3 does not specify; the vault baseline is no non-essential motion | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| No scripts, no external references, size limits | a desktop shell reads untrusted files | [[ADR-0001 MD3 role names are the specification vocabulary]] (roles only; safety rule is Tesserae's) |

## Sources

- [Material Symbols and icons guidance](https://developers.google.com/fonts/docs/material_symbols) for sizes (24 dp default, 20 and 40 and 48 optical sizes) and the variable axes; m3.material.io icon page not readable #needs-verification.
- [SVG 1.1 specification](https://www.w3.org/TR/SVG11/): `viewBox` and `preserveAspectRatio` (`xMidYMid meet`), `currentColor`.
- [WAI-ARIA 1.2 img](https://www.w3.org/TR/wai-aria-1.2/#img); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.1.1, 1.4.3, 1.4.11, 2.2.2, 2.3.1.
- Code and engine docs: `tess-ui:docs/components/svg.md`, `tre:docs/reference/paint.md` (SVG documents, SMIL animation, `svg_time`), `shell-vault:41 TDL Reference/Block Reference.md` (SVG).
- Size limits for documents and the 24, 20, 20 icon sizes are Tesserae choices.
