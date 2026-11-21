---
title: Box
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, layout, primitive]
related: ["[[FlexBox]]", "[[Grid]]", "[[Spacer]]", "[[ScrollBox]]", "[[Rectangle Block]]", "[[Panel and Surface]]", "[[Scrollbar and Scroll Container]]", "[[10 Layout Overflow and Scrolling]]", "[[07 Spacing and Density Rules]]", "[[Spacing and Density]]", "[[Shape]]", "[[Colour Roles]]", "[[Elevation]]", "[[14 Accessibility Basics]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]"]
aliases: ["Box block"]
---

# Box

> [!info] Summary
> A Box is the basic container block: it holds children in one shared cell, paints an optional fill, border, corner radius and shadow, and has no role. Material Design 3 has no container primitive; the nearest counterparts are the Compose `Box` layout and the MD3 surface ([Layout](https://m3.material.io/foundations/layout/overview)). Source of truth in code: see Status in code.

## Purpose

Group, pad, clip and paint a region without implying a stacking direction. A Box is invisible when unstyled and a surface when styled ([[Panel and Surface]] is the styled use).

## When to use and not

- Use when: children overlap or one child fills the Box (a badge over an icon, a background behind content, a clipped viewport).
- Do not use when: children stack along one axis (use [[FlexBox]]); children align in rows and columns (use [[Grid]]); content scrolls (use [[ScrollBox]]); a plain rectangle without children is needed (use [[Rectangle Block]]).

## Anatomy

1. Box container: the laid-out rectangle with padding.
2. Paint layer: fill, border (drawn inside the box, no layout change in the engine), corner radius, shadows.
3. Children: all placed in cell (1, 1) of a one-column, one-row grid, so they overlap and the Box is as large as its largest child unless sized.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Transparent | grouping, padding | no fill, border or shadow |
| Surface | panel body, card | fill from a role, `Corner_Radius` from [[Shape]], optional border and elevation |
| Clipping | viewport, rounded image mask | `Clip_Children: true`; children clip to the rounded box |

## States

Not applicable: a Box has no interaction states of its own. A Box that raises `On_Click` takes its states from the element built on it ([[Button]], [[List Item]]).

| State | Visual change | Token values |
|---|---|---|
| Disabled (`Enabled: false`) | the Box and its subtree are announced disabled; the owning element dims it | defined by the owning element |

## Tokens used

Fill: a role of [[Colour Roles]]; radius: [[Shape]]; shadow: [[Elevation]]; padding and margin: the nine steps of [[Spacing and Density]] (0, 2, 4, 8, 12, 16, 24, 32, 48 dp). A Box carries no literal colour (AR-20 of [[Accessibility Rules]]).

## Sizing and density

Not applicable: a Box has no size of its own and no density-dependent value. Size comes from content, `Width`, `Height`, `Min_*`, `Max_*` or flex growth. Padding uses a spacing step chosen by the owning element and its density level ([[07 Spacing and Density Rules]]).

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | N/A: content-sized: the height comes from the largest child, `Height` or `Min_Height` | N/A: content-sized, same as default | N/A: content-sized, same as default | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| container | margin | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| container | gap | - | N/A: all children share cell (1, 1), so no gap exists between them | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: a Box has no Spacing key, its one grid cell holds every child; tre: yes (gap) |
| container | border width | - | 0 | 0 | 0 | tess-shell:src/tess_shell/schema/blocks.py | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| container | border color | - | N/A: no border by default; a bordered Box takes a colour role from its owner | N/A: same as default | N/A: same as default | tess-shell:src/tess_shell/schema/blocks.py | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| container | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| container | font | - | N/A: a Box draws no text; text belongs to its children | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: a Container draws no text; tess-shell: n/a: a Box draws no text and has no font key; tre: n/a: a box draws no text |
| container | icon size | - | N/A: a Box draws no icon; icons are children | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: a Container draws no icon; tess-shell: n/a: a Box draws no icon and has no icon key; tre: n/a: a box draws no icon |
| container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |

Box values do not change with density; the owning element chooses padding from the nine spacing steps and its density level. A surface Box takes `shape.medium` (12) or another step from [[Shape]]; that choice belongs to [[Panel and Surface]].

## Layout and overflow

- Overflow per axis: clip only when `Clip_Children` is true; otherwise children paint past the Box (an overlay badge needs this). A Box that holds text or controls that may exceed it must either clip, wrap, ellipsise or sit in a [[ScrollBox]] ([[10 Layout Overflow and Scrolling]], overflow rule 1).
- Children that hold text have minimum width 0 so the ellipsis can work (chapter 10, Minimum widths).
- Each child aligns itself with `Align_Self` and the justify key of its cell; nothing stacks automatically.
- A Box never shows a scrollbar; scrolling is a [[ScrollBox]].
- Vertical centring of single-line text is done by the owning control, not by the Box ([[10 Layout Overflow and Scrolling]]).
- Hit testing: a Box is hit inside its rounded corners, also when transparent; `hit_testable=false` makes it transparent to the pointer. A clip does not narrow the hit area in the engine (clipped-away corners still hit).

## Behaviour

- Pointer: raises the pointer events and `On_Click` only when the module sets a handler; a Box is not focusable by default.
- Keyboard: none unless `Focusable` is set by the owning element; then Enter and Space fire `click` (engine rule).
- Touch: none of its own.

## Tooltip and overlay behaviour

Not applicable: a tooltip belongs to a control, never to a container ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]). A Box opens no overlay.

## Motion

`Transition` keys animate `Background`, `Opacity` and the border over `Duration` with `Easing`; durations come from [[Motion]]. Under the reduced-motion preference the change is immediate.

## Accessibility

- Role none, not focusable, no name: a container with a role of its own takes it from its element (`LIST`, `MENU`).
- A purely decorative Box needs nothing; one that carries meaning is named by the element that owns it.
- `A11y_Hidden` hides a decorative subtree from assistive technology.

## Dark and light

Colours are roles and follow the scheme ([[Theme Following the System]]); no hex value in a Box.

## Defaults

Padding 0, margin 0, no fill, no border, `Clip_Children` false, role none, all children in cell (1, 1).

## Acceptance criteria

- [ ] AC-BLK-BOX-1 (geometry check): two children in a Box with no size share one cell. Passes when both children have the same layout origin and the Box size equals the larger child plus padding.
- [ ] AC-BLK-BOX-2 (geometry check): padding of 0, 4, 8, 12, 16, 24, 32 and 48 dp insets the children by exactly that value on every side; a padding outside the nine steps is rejected by the stylesheet lint of AC-DEN-1 in [[Spacing and Density]].
- [ ] AC-BLK-BOX-3 (pixel check): with `Clip_Children: true` and `Corner_Radius` 12, no child pixel lies outside the rounded box; with `Clip_Children: false` a child positioned 8 dp past the edge paints.
- [ ] AC-BLK-BOX-4 (scripted input): a click at a point inside a transparent Box raises its `On_Click`; a click in the clipped-away corner of a 12 dp radius lands on what is behind; with `hit_testable=false` the click reaches the sibling below.
- [ ] AC-BLK-BOX-5 (AT tree assertion): an unstyled Box exposes role none and no name; a Box with `A11y_Hidden` is absent from the tree with its subtree.
- [ ] AC-BLK-BOX-6 (token test): every colour of a Box in the shipped themes resolves to a role name; no literal colour exists in a Box style. Passes at zero literals.
- [ ] AC-BLK-BOX-7 (pixel check): the border is drawn inside the box: a 2 dp border leaves the laid-out size unchanged in the engine and the shell reserves 2 dp of content inset (content never under the border).

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py` (`Box`) | meets: a tre `box` with `display: grid`, one `1fr` cell, children in cell (1, 1); keys `Padding`, `Clip_Children`, style keys per `BOX_STYLE`. AC-BLK-BOX-7 not verified (border inset mapping marked #needs-verification in `shell-vault:41 TDL Reference/Block Reference.md`) |
| tess-ui | `tess-ui:src/tess_ui/views/*_View.tdl` (`Container`) | partly meets: `Container` is a flex box, not a one-cell grid; overlap uses `position: absolute`. Spacing literals include 14 (fails AC-DEN-1) |
| tre | `tre:docs/reference/properties.md` (kind `box`), `tre:docs/guide/nodes-and-layout.md` | meets: box kind with fill, stroke, radius, shadows, `clip_children`; hit inside rounded corners; hit test ignores clip and mask |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Container primitive with no MD3 counterpart; padding steps are the Tesserae scale (2 dp half step) | MD3 defines no container block or spacing tokens | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Children share one cell instead of stacking | Tesserae block set decision R1 (shell vault); stacking is [[FlexBox]] | [[ADR-0010 Document structure of the specifications]] |

## Sources

- Block table and keys: `tess-shell:src/tess_shell/schema/blocks.py`, `shell-vault:41 TDL Reference/Block Reference.md` (Box, decision R1).
- Engine: `tre:docs/guide/nodes-and-layout.md`, `tre:docs/reference/properties.md`, `tre:docs/reference/node.md` (`hit_testable`), `tre:docs/reference/paint.md` (masks ignore hit test).
- Material layout overview (page is a JavaScript app, not readable by tools; MD3 statement #needs-verification): https://m3.material.io/foundations/layout/overview. Compose layout basics: https://developer.android.com/develop/ui/compose/layouts/basics.
- WAI-ARIA 1.2 role `none`/`presentation`: https://www.w3.org/TR/wai-aria-1.2/.
