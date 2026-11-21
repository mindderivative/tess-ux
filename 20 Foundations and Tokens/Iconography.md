---
title: Iconography
type: foundation
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [foundation, icons, tokens]
related: ["[[Spacing and Density]]", "[[Colour Roles]]", "[[State Layers]]", "[[Icon Button]]", "[[Button]]", "[[Tree Node]]", "[[List Item]]", "[[ADR-0007 Icon set and Material Symbols deviation]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[14 Accessibility Basics]]", "[[Existing Tokens]]", "[[Gaps and Contradictions]]"]
depends_on: ["[[ADR-0007 Icon set and Material Symbols deviation]]", "[[Spacing and Density]]"]
---

# Iconography

> [!info] Summary
> Icon sizes per density level, the icon set (Material Design Icons through tess-icons) and its deviation from Material Symbols, the 24 unit view box, tinting by colour role and the fallback icon. MD3 counterpart: [Material Symbols](https://fonts.google.com/icons) and the 24 dp icon.

Decision: [[ADR-0007 Icon set and Material Symbols deviation]].

## Icon sizes

An icon is drawn in a square of the stated size; the view box is scaled to it.

| Use | default | compact | dense | MD3 value |
|---|---|---|---|---|
| Icon button icon | 24 | 20 | 20 | 24 (`md.comp.icon-button.icon.size`) |
| Leading and trailing icon in a list row, menu item or tree row | 24 | 20 | 20 | 24 (`md.comp.menu-item` list item leading icon size 24) |
| Icon next to a button label | 18 | 18 | 16 | 18 (`md.comp.filled-button.with-icon.icon.size`) |
| Text field leading and trailing icon | 24 | 20 | 20 | 24 (`md.comp.filled-text-field.leading-icon.size`) |
| Tree chevron glyph | equals the chevron box: 24 | 20 | 16 | no MD3 tree |
| Inline icon in a status bar or badge row | 16 | 16 | 16 | not specified #needs-verification |

The first row is binding from [[Spacing and Density]]. Rows two to four and six are Tesserae choices that follow the density rows so that an icon fits its row (default 24 in 40 leaves 8; compact 20 in 32 leaves 6; dense 20 in a 24 dp list or tree row leaves 2 and in a 28 dp menu item leaves 4, accepted: the icon box is the painted size and the row is the hit area). Standalone icons (empty states, dialog icons) are 24 dp unless a component note states another size. Icons have one size within a row; icon and label centre on the same horizontal axis (AC-ICO-6).

Sizes are dp, equal to px at scale factor 1.0 ([[Spacing and Density]]).

## Icon set

| Property | Value |
|---|---|
| Set | Material Design Icons (Pictogrammers) through tess-icons: 7447 icons, view box 24 by 24 (the shell vault records Apache 2.0; the Pictogrammers licence file names the Pictogrammers Free License, check before shipping) #needs-verification |
| Line set (optional) | Material line icons, 1218 icons, 24 by 24, in tess-icons; used only where an animated or line style is chosen by project ADR |
| Material Symbols | not used; the Symbols subset in tess-ui (view box `0 -960 960 960`) is a legacy set |
| View box | every icon of the standard set is 24 by 24 (`0 0 24 24`) and scales uniformly to the icon size; a set with another view box is normalised to 24 at import |
| Format | vector path data; colour from `currentColor` mapped to a colour role |

The icon's visible glyph occupies the live area of the 24 grid (MDI keeps 2 units of padding in most glyphs, #needs-verification as a Pictogrammers rule); the box is not trimmed, so padding in the glyph counts towards the stated icon size.

## Deviation from Material Symbols

Material Symbols are a variable font with four axes: fill 0 to 1, weight 100 to 700, grade -50 to 200 and optical size 20 to 48 (Google Fonts CSS API: `opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200`). Material Design Icons are static paths with one weight, one fill style per icon (filled or outline variants are separate icons) and no optical size.

Consequences, recorded as the deviation:
- No weight axis: stroke weight is fixed and does not follow text weight.
- No fill axis: a selected state uses a separate filled icon name or a colour change, not a fill animation.
- No grade axis: dark mode does not reduce glare through grade.
- No optical size axis: a 20 dp icon is the 24 grid scaled by 20/24, so its strokes are 17 percent thinner than at 24. The 20 dp size at compact and dense is accepted; the 16 dp size is allowed only for rows where nothing else fits.

Reason: tess-icons, the shell and the config app are built on Material Design Icons; the engine draws paths (`tre:docs/reference/paint.md`) and has no variable-font axes. ADR: [[ADR-0007 Icon set and Material Symbols deviation]].

## Tinting by colour role

- An icon takes its colour from a role, never a literal: the engine path takes `fill` or `stroke_color`, and the set body uses `currentColor` that the consumer maps (`tess-icons:icon-sets/Material-Design-Icons/material-design-icons.json`).
- Default role: the content colour of the parent: `on_surface` for primary actions, `on_surface_variant` for secondary or decorative icons in lists and trees, `on_primary` on a filled primary button, `on_secondary_container` on a tonal control. The component note names the role per part.
- State: the icon takes the state of its control (disabled: content colour at 38 percent, [[State Layers]]); a state layer is drawn behind the icon, not over it.
- Contrast: an icon that carries information has at least 3 to 1 against its background (WCAG 2.2 SC 1.4.11); a decorative icon is exempt but follows the same roles.
- Multicolour images (application icons, thumbnails, album art) are not icons in this sense and are not tinted. They are bitmaps or SVG with their own colours, drawn at the size of the slot.

## Fallback icon

A name that resolves to no icon shows `mdi:image-broken-variant` (24 by 24, tinted by the same role as the missing icon) and logs one warning naming the missing icon once per name (`tess-shell:src/tess_shell/model/icons.py` `FALLBACK`). The shell vault text that says `image-missing` is stale; the code and the Block Reference say `image-broken-variant` ([[Gaps and Contradictions]]). A blank slot is a defect.

## Accessibility

- A decorative icon (next to a text label that says the same) is hidden from the accessibility tree.
- An icon-only control has an accessible name and a tooltip with the same text on the control ([[Icon Button]], [[ADR-0004 Tooltip rule]]).
- An icon never is the only carrier of a state (error, warning): text or a second cue accompanies it.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/icons.py` (Symbols 0 -960 960 960, MDI 0 0 24 24), `tess-ui:src/tess_ui/views/IconButton_Stylesheet.tdl` line 52, `Button_Stylesheet.tdl` line 162 | partly meets: two sets with different view boxes (fails AC-ICO-2 for the Symbols subset); icon button icon is 24 and 20 for size xs but no density levels (fails AC-ICO-1 at compact, dense); Button size s icon is 18 (meets for default). Icon colour from roles meets AC-ICO-3 |
| tess-shell | `tess-shell:src/tess_shell/shipped/Icons/mdi.json`, `tess-shell:src/tess_shell/model/icons.py` | partly meets: mdi 24 view box, fallback `mdi:image-broken-variant` with one warning (meets AC-ICO-4, AC-ICO-5); Icon default size 16 and MenuItem icon 16 are literals (fail AC-ICO-1 at default, where list and menu icons are 24) |
| tre | `tre:docs/reference/paint.md`, `tess-icons` | not applicable: the engine draws paths and has no icon size default; the 24 by 24 view box comes from tess-icons |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Material Design Icons instead of Material Symbols; no weight, fill, grade, optical size axes | existing icon set in all projects, engine draws static paths | [[ADR-0007 Icon set and Material Symbols deviation]] |
| 20 dp icon at compact and dense (also in the 24 dp dense list and tree row, which leaves 2 dp above and below), 16 dp only where nothing else fits | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| Fallback icon is a broken-image glyph | MD3 states no fallback; a visible glyph exposes the missing name | [[ADR-0007 Icon set and Material Symbols deviation]] |

## Acceptance criteria

- [ ] AC-ICO-1 (geometry check): at each density level the icon button icon is 24, 20 and 20 dp; the list, menu and tree leading icon 24, 20 and 20 dp; the button label icon 18, 18 and 16 dp. Pass: painted icon bounds equal the stated size.
- [ ] AC-ICO-2 (token test): every icon in the standard set has view box width 24 and height 24 (a script over the set JSON); a set with another view box is converted at import.
- [ ] AC-ICO-3 (token test): no icon literal colour in a stylesheet; every icon fill resolves to a colour role; a theme switch from light to dark changes every icon colour (pixel check on a test sheet).
- [ ] AC-ICO-4 (scripted input): resolving an unknown icon name draws the glyph of `mdi:image-broken-variant` at the requested size and logs one warning; a second resolution of the same name logs none.
- [ ] AC-ICO-5 (pixel check): the fallback glyph pixels equal the tint role colour of the slot, not a literal.
- [ ] AC-ICO-6 (geometry check): in a row, the icon centre and the label line box centre have the same vertical coordinate within 1 px.
- [ ] AC-ICO-7 (AT tree assertion): an icon-only button exposes an accessible name; a decorative icon is absent from the tree.
- [ ] AC-ICO-8 (pixel check): a disabled icon's pixels equal `on_surface` at 38 percent over the container (see AC-STL-5).

## Sources

- Material Symbols axes (fill, weight, grade, optical size) and CSS ranges `opsz 20..48, wght 100..700, FILL 0..1, GRAD -50..200`: https://developers.google.com/fonts/docs/material_symbols (verified 2026-11-21).
- Icon size 24 px: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-icon.scss and `_md-comp-icon-button.scss` (verified); filled button icon 18 px: `_md-comp-filled-button.scss` (verified); text field icon 24 px: `_md-comp-filled-text-field.scss` (verified); menu list item icon 24 px: `_md-comp-menu-item.scss` (verified).
- MDI license and grid: https://pictogrammers.com/docs/library/mdi/ (not read in full #needs-verification for the live-area statement).
- WCAG 2.2 SC 1.4.11: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html (verified).
- Project facts: [[Existing Tokens]], [[Gaps and Contradictions]].
