---
title: Divider
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, containment, divider]
related: ["[[Divider|Menu Separator]]", "[[List]]", "[[List Item]]", "[[Menu]]", "[[Panel and Surface]]", "[[Accordion]]", "[[Banner]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[Shape]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]", "[[Spacing and Density]]"]
---

# Divider

> [!info] Summary
> A 1 dp line that groups and separates content in lists and containers, full width, inset, or inset on both ends, horizontal or vertical. Counterpart: Material Design 3 [Divider](https://m3.material.io/components/divider/overview). Source of truth in code: see Status in code.

## Purpose

Show where one group of content ends and the next begins, and imply a parent and child relationship when inset, with the least visual weight.

## When to use and not

- Use when: unrelated groups sit on the same surface; a list or menu has sections; interactive areas border non-interactive areas.
- Do not use when: spacing alone separates the groups (prefer space: a gap of `space.5` 16 dp or more); a container boundary already exists (a card or panel edge); every row of a dense list would carry one (use row hover and alternate surface instead); the line is a control (a splitter handle is a [[Panel and Surface]] concern, not a divider).

## Anatomy

1. Line: a 1 dp rectangle spanning the cross axis of its container.
2. Inset (optional): empty space of 16 dp at the start (inset) or at both ends (middle inset).

## Variants

| Variant | Use | Geometry |
|---|---|---|
| Full width | separate large unrelated sections; interactive from non-interactive | spans the whole length |
| Inset | separate related items inside a section, aligned with the text start | starts 16 dp from the start edge, runs to the end |
| Middle inset | separate items inside a card or panel | 16 dp clear at both ends |
| Vertical | separate columns, toolbar groups | the same three variants rotated: top and bottom insets |
| Emphasised | a division that must be seen (the line is the only cue, or separates interactive regions) | colour `outline` instead of `outline_variant`, still 1 dp |

## States

A divider is static: no hover, focus, pressed or disabled state, no state layer, never focusable. Its colour does not change when the parent is disabled.

| State | Visual change | Token values |
|---|---|---|
| Rest | line drawn | `outline_variant`, 1 dp |
| High contrast | line colour `outline` | [[Colour Roles]] |

## Tokens used

| Part | Token | Value |
|---|---|---|
| Colour | `md.comp.divider.color` | `outline_variant` (#CAC4D0 light, #49454F dark) |
| Thickness | `md.comp.divider.thickness` | 1 dp |
| Insets | MD3 guidance | 16 dp |

Source: [Material Web divider tokens, latest](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss) (`color` `outline-variant`, `thickness` 1 px, verified 2026-11-21); [Material Components Android Dividers](https://github.com/material-components/material-components-android/blob/master/docs/components/Divider.md) (full width and inset types, default colour `colorOutlineVariant`, 1 dp, heavy divider 8 dp is an Android-only option). Contrast: `outline_variant` is below 3 to 1 against `surface` (1.62 to 1 light, 1.99 to 1 dark, [[Colour Roles]]).

## Sizing and density

The line does not scale with density; the spacing around it does. A divider adds no height of its own beyond its thickness.

| Level | Thickness | Inset (start) | Middle inset (each end) | Space above and below inside a list or menu |
|---|---|---|---|---|
| default | 1 | 16 | 16 | 8 |
| compact | 1 | 16 | 16 | 4 |
| dense | 1 | 16 | 16 | 4 |

- The inset equals the MD3 value at every level so a divider aligns across levels; the project may set the inset to the row padding plus a leading icon box and gap where the divider must align with row text, which is the intent of the inset variant. Row padding and icon gap come from [[Spacing and Density]].
- A divider is not a pointer target and has no 24 dp minimum.
- Thickness at scale factor 1.25 and 1.5 is 1 dp, painted as at least 1 device pixel: the line never disappears and never paints at a fractional blur #needs-verification (engine snapping behaviour).

## Dimensions and defaults

The line has no density-dependent size; only the space around it in a list or menu does ([[Divider#Sizing and density]]). The divider draws no border: the line itself is the fill, so its colour is given under border color.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| line (horizontal) | height | `md.comp.divider.thickness` | 1 | 1 | 1 | MD3 [divider tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss) | tess-ui: via Divider param Thickness (Height rule); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| line (vertical) | min width | `md.comp.divider.thickness` | 1 | 1 | 1 | MD3 [divider tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss) | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| line | min height | - | N/A: a divider is not a pointer target and has no 24 dp minimum | N/A: same as default | N/A: same as default | [[Divider#Sizing and density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| line | padding | - | N/A: the line is a plain rectangle with no content; the insets are margins | N/A: same as default | N/A: same as default | [[Divider#Sizing and density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| line (full width) | margin | - | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Divider#Variants]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| line (inset) | margin | - | 0 0 0 16 | 0 0 0 16 | 0 0 0 16 | MD3 [Android Dividers](https://github.com/material-components/material-components-android/blob/master/docs/components/Divider.md) (16 dp inset); tess-ui `Divider_Stylesheet.tdl` | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| line (middle inset) | margin | - | 0 16 0 16 | 0 16 0 16 | 0 16 0 16 | MD3 [Android Dividers](https://github.com/material-components/material-components-android/blob/master/docs/components/Divider.md); tess-ui `Divider_Stylesheet.tdl` | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| space around the line in a list or menu | gap | `space.3`, `space.2`, `space.2` | 8 | 4 | 4 | design choice, proposed ADR (divider spacing by density); [[Divider#Sizing and density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| line | border width | - | N/A: the divider draws no border; the 1 dp thickness is its height | N/A: same as default | N/A: same as default | MD3 [divider tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss) | tess-ui: via Divider param Thickness (Background fill, no border); tess-shell: n/a: element absent in tess-shell; tre: via height or width of a 1 px box (no border) |
| line (fill) | border color | `outline_variant` | `outline_variant` | `outline_variant` | `outline_variant` | MD3 [divider tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss) (emphasised variant: `outline`) | tess-ui: yes (style Background); tess-shell: n/a: element absent in tess-shell; tre: yes (background) |
| line | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] (MD3 divider tokens define no shape; the line is a rectangle) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| line | font | - | N/A: a divider holds no text | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: the line draws no text or icon; tess-shell: n/a: element absent in tess-shell; tre: n/a: the line draws no text or icon |
| line | icon size | - | N/A: a divider holds no icon | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: the line draws no text or icon; tess-shell: n/a: element absent in tess-shell; tre: n/a: the line draws no text or icon |
| line | elevation | `elevation.level_0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

## Layout and overflow

- A horizontal divider fills the width of its container minus insets; a vertical one fills the height. It needs a container that gives it a cross size: in a container that sizes to content the divider has no length (tess-ui documents this).
- It never wraps, scrolls or truncates. In a scroll container it scrolls with the content ([[Scrollbar and Scroll Container]]).
- In a list the divider sits between rows and takes its own 1 dp of height; a list row height does not change when a divider is present. A divider is not drawn after the last row of a list, nor before the first.
- Two dividers are never adjacent; a divider next to a container edge is dropped.
- Vertical centring does not apply; a vertical divider in a toolbar is centred in the cross axis with its own length (at most the control height minus 8 dp).

## Behaviour

- Pointer, keyboard, touch: none. The divider is hit-test transparent and not in the Tab order. In a menu, a menu separator is a divider that arrow keys skip ([[Divider|Menu Separator]], [[Menu]]).

## Tooltip and overlay behaviour

None: a divider has no tooltip ([[ADR-0004 Tooltip rule]] applies to controls) and opens no overlay. Hover over it falls through to the container.

## Motion

None. A divider appears with its container. Not applicable under reduced motion.

## Accessibility

- Role: `separator` (WAI-ARIA [separator](https://www.w3.org/TR/wai-aria-1.2/#separator), a non-focusable structural separator), with `orientation` vertical for a vertical one (horizontal is the default). It has no name and no value.
- A divider that only decorates (between two paragraphs already separated by headings) is hidden from assistive technology; one that marks a menu or toolbar section stays exposed as `separator`.
- Contrast: a divider that is the only cue separating two regions the user must tell apart uses the emphasised variant (`outline`, 3 to 1 against `surface`, [WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)). A purely decorative `outline_variant` divider is exempt because the structure is also given by spacing, headings or the accessible tree.
- Colour is not the only cue: position and structure carry the grouping.

## Dark and light

Roles only. `outline_variant` is #CAC4D0 on `surface` #FEF7FF light and #49454F on #141218 dark. High contrast switches to `outline`.

## Defaults

Horizontal, full width, 1 dp, `outline_variant`, exposed as `separator`.

## Acceptance criteria

- [ ] AC-DIV-1 (token test): thickness is 1 dp and colour is the role `outline_variant` (emphasised: `outline`); no colour literal. Pass: values equal at scale 1.0, 1.25 and 2.0 (painted at least 1 device pixel).
- [ ] AC-DIV-2 (geometry check): a horizontal full-width divider in a 320 dp container is 320 dp long and 1 dp high; inset starts 16 dp from the start edge and ends at the end edge; middle inset has 16 dp clear at both ends; a vertical divider of each variant has the same insets at top and bottom. Pass: equal within 0.5 dp.
- [ ] AC-DIV-3 (geometry check): in a list of 5 rows with dividers between rows, the dividers are 4 in number, the row heights are unchanged at each density level and no divider precedes the first row or follows the last. Pass: counts and heights equal.
- [ ] AC-DIV-4 (AT tree assertion): a structural divider has role `separator`, no name, and `orientation` vertical when vertical; a decorative one is absent from the tree; a divider is never focusable. Pass: tree walk equal; Tab sequence excludes it.
- [ ] AC-DIV-5 (scripted input): pointer press and hover on a divider reach the element beneath it; arrow keys in a menu skip a menu separator. Pass: the container's event count 1 and focus order equals the item list.
- [ ] AC-DIV-6 (contrast script): the emphasised divider `outline` against each of `surface`, `surface_container` and `surface_container_high` at least 3 to 1 in light, dark and high contrast; `outline_variant` is not tested (decorative). Pass: no ratio below 3.
- [ ] AC-DIV-7 (review): no divider is adjacent to another, to a container edge, or used where a container boundary exists; no row of a list with more than 8 rows carries a divider under every row. Pass: reviewer finds none, name and date recorded.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Divider_View.tdl`, `tess-ui:src/tess_ui/views/Divider_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/structural.py`, `tess-ui:docs/components/dividers.md` | meets in design: 1 dp default `Thickness`, `outline_variant`, variants full, inset (16 start) and middle (16 both), orientation, role `separator` (AC-DIV-1, AC-DIV-2, AC-DIV-4 by reading, unrun); no emphasised variant (AC-DIV-6 not applicable until it exists); not used by any app or example, so the list rules (AC-DIV-3, AC-DIV-7) are unmeasured |
| tess-shell | none as a module; the MenuItem has a `rule` part (menu separator, see [[Divider|Menu Separator]]); no divider module | absent as a component; `tess-shell:docs/guide/modules.md` has no Divider |
| tre | none: a divider is a box of 1 px | not applicable |

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Divider_View.tdl` | exists |
| shell vault | `shell-vault:50 Design System/Standard Modules.md` (menu separator) | design intent for menus only |
| tess-shell | none | absent |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Emphasised variant in `outline` | `outline_variant` is below 3 to 1; a divider that is the only separating cue must pass WCAG 1.4.11 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Space inside lists and menus is 8, 4, 4 dp by density | density levels | [[ADR-0002 Desktop density levels and target sizes]] |
| No heavy 8 dp divider | Android-only option; not in the Material Web tokens | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Insets stay 16 dp at all levels | alignment across levels; MD3 value kept | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- [Material Web divider tokens (latest)](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-divider.scss): `thickness` 1 px, `color` `outline-variant`. Verified 2026-11-21.
- [Material Components Android Dividers](https://github.com/material-components/material-components-android/blob/master/docs/components/Divider.md): full width and inset types, thickness 1 dp default, 8 dp heavy, colour `colorOutlineVariant`, insets 0 dp default.
- [WAI-ARIA 1.2 separator](https://www.w3.org/TR/wai-aria-1.2/#separator); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11.
- The 16 dp inset values come from the tess-ui documentation of the MD3 page (`tess-ui:docs/components/dividers.md`); m3.material.io could not be fetched #needs-verification.
- Contrast figures for `outline_variant` from [[Colour Roles]].
