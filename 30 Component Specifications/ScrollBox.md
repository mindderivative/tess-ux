---
title: ScrollBox
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, scrolling, overflow, primitive]
related: ["[[Scrollbar and Scroll Container]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0012 Scrollbar thumb opacity and hit area exception]]", "[[10 Layout Overflow and Scrolling]]", "[[List]]", "[[Tree]]", "[[FlexBox]]", "[[Box]]", "[[Accessibility Tree]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Scrollbar and Scroll Container]]", "[[ADR-0003 Scrollbar rule]]"]
aliases: ["ScrollBox Block", "Scroll Box"]
---

# ScrollBox

> [!info] Summary
> A ScrollBox is the block form of a scroll container: a clipped viewport that scrolls its one content child along one axis. The behaviour, scrollbar geometry, keys and tokens are defined once in [[Scrollbar and Scroll Container]]; this note records what the block contributes and where the shell falls short. MD3 has no scroll container component. Source of truth in code: see Status in code.

## Purpose

Give any block content a viewport so that no content is unreachable ([[10 Layout Overflow and Scrolling]], hard rule 3).

## When to use and not

- Use when: content (a [[FlexBox]] column of rows, a long form) can exceed its frame.
- Do not use when: content is shaped by wrapping or ellipsis; the list has more entries than can be built (a virtual list, planned as `VirtualList`); content is discrete pages (a carousel with snap is allowed, a tab view is not a ScrollBox).

## Anatomy

1. Viewport: clips to its bounds.
2. One content child (a [[FlexBox]] or [[Box]]) holding the rest.
3. Scrollbar thumb and gutter: see [[Scrollbar and Scroll Container]].

## Variants

| Variant | Use | Differences |
|---|---|---|
| Vertical | lists, forms | `Orientation: VERTICAL` (default) |
| Horizontal | strips, wide trees | `Orientation: HORIZONTAL`; a plain vertical wheel passes to the outer view |
| Two axes | wide and tall content | the engine has one axis per view; nest a horizontal ScrollBox in a vertical one (visible result must equal AC-SCB-04) |
| Snapping | carousel | `Scroll_Snap` START, CENTER, END (not built in the shell) |

## States

Defined in [[Scrollbar and Scroll Container]] (rest, hover, drag for the thumb; no state of the box itself).

## Tokens used

Scrollbar tokens (thumb 8 dp, hit 12 dp, margin 2 dp, minimum thumb 32 dp, gutter 12 dp, line 40 dp, notch 40 dp) are defined in [[Scrollbar and Scroll Container]]; this block reads them and defines none.

## Sizing and density

Not applicable: scrollbar sizes do not vary with density ([[Scrollbar and Scroll Container]], Tokens used). The viewport size is set by the owner.

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| viewport | height | - | N/A: the owner sets the viewport size; content beyond it scrolls | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| viewport | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]] | tess-ui: yes (style padding, applied to the content box); tess-shell: via Padding on the content child Box; tre: via padding on the content child (the scroll view ignores its own) |
| content gutter | padding | `scrollbar.gutter` | 0 12 0 0 | 0 12 0 0 | 0 12 0 0 | [[Scrollbar and Scroll Container]] | tess-ui: yes (style padding, applied to the content box); tess-shell: via Padding on the content child Box; tre: via padding on the content child (the scroll view ignores its own) |
| viewport | margin | - | N/A: the parent container sets the outer space | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| viewport | gap | - | N/A: the block has one content child; gaps belong to that child | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style gap, applied to the content box); tess-shell: n/a: one content child and no Spacing key on the ScrollBox; tre: n/a: the scroll view holds one content child |
| thumb | margin | `scrollbar.margin` | 2 | 2 | 2 | [[Scrollbar and Scroll Container]] | tess-ui: no hook; tess-shell: no hook; tre: hardcoded in tre (SCROLLBAR_MARGIN 2.0 in engine-core/src/node.rs) |
| thumb, across the axis | min width | `scrollbar.thumb.thickness` | 8 | 8 | 8 | [[Scrollbar and Scroll Container]] | tess-ui: no hook; tess-shell: no hook; tre: yes (scrollbar_width, default SCROLLBAR_THICKNESS 4.0) |
| thumb, along the axis | min height | `scrollbar.thumb.min_length` | 32 | 32 | 32 | [[Scrollbar and Scroll Container]] | tess-ui: no hook; tess-shell: no hook; tre: hardcoded in tre (SCROLLBAR_MIN_LENGTH 32.0 in engine-core/src/node.rs) |
| hit area | min width | `scrollbar.hit.thickness` | 12 | 12 | 12 | [[ADR-0012 Scrollbar thumb opacity and hit area exception]] | tess-ui: no hook; tess-shell: no hook; tre: hardcoded in tre (SCROLLBAR_GRAB_SLOP 6.0 in engine-core/src/node.rs) |
| viewport | border width | - | N/A: the viewport draws no border; paint is the content's or a parent's | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style border_width); tess-shell: n/a: the ScrollBox has no border key, a parent Box draws it; tre: yes (stroke_width) |
| viewport | border color | - | N/A: the viewport draws no border; paint is the content's or a parent's | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: yes (style border_color); tess-shell: n/a: the ScrollBox has no border key, a parent Box draws it; tre: yes (stroke_color) |
| viewport | corner radius | - | N/A: the viewport clips to a rectangle; rounding belongs to a parent Box | N/A: same as default | N/A: same as default | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: the ScrollBox has no radius key, a parent Box rounds; tre: yes (corner_radius, the content clips to it) |
| thumb | corner radius | `scrollbar.thumb.radius` | 9999 | 9999 | 9999 | [[Scrollbar and Scroll Container]] | tess-ui: no hook; tess-shell: no hook; tre: hardcoded in tre (SCROLLBAR_THUMB_RADIUS 2.0 in engine-render/src/lib.rs) |
| viewport | font | - | N/A: the block draws no text | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: a ScrollView draws no text; tess-shell: n/a: the block draws no text and has no font key; tre: n/a: the scroll view draws no text |
| viewport | icon size | - | N/A: the block draws no icon | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: a ScrollView draws no icon; tess-shell: n/a: the block draws no icon; tre: n/a: the scroll view draws no icon |
| viewport | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |

Scrollbar values do not change with density; they are copied from [[Scrollbar and Scroll Container]], which owns them. The gutter row is for a vertical bar and applies only while the axis overflows (a horizontal bar reserves 12 at the bottom). A touch context sets the hit thickness to 48.

## Layout and overflow

- Overflow: clip, with scroll on its own axis; the bar shows exactly when content exceeds the viewport on that axis (AC-SCB-02).
- The content child has its cross-axis size equal to the viewport minus the gutter when the axis overflows.
- Nested ScrollBoxes chain: an inner one at its end, or not able to move that way, passes wheel and keys outward.
- The focus ring of a child is not clipped by the viewport (the child scrolls into view with ring and gutter inside).
- Hit testing: the viewport hits within its box; content outside the viewport is not hit.

## Behaviour

Defined in [[Scrollbar and Scroll Container]]: arrows 40 dp, Page keys one viewport minus 10 percent, Home and End, wheel 40 dp per notch, Shift plus wheel for the horizontal axis; keyboard scroll jumps. `Scroll_Offset` is settable and animatable and clamps to the content range at once.

## Tooltip and overlay behaviour

A scrolling ancestor dismisses an open tooltip inside it ([[ADR-0004 Tooltip rule]]); the ScrollBox itself has no tooltip.

## Motion

Wheel and key scrolls jump; programmatic offset changes animate with `easing-standard`; snap settles 120 ms after the last input over about 200 ms; reduced motion: 0 ms ([[Scrollbar and Scroll Container]], Motion).

## Accessibility

A ScrollBox with overflow and no focusable descendant is a Tab stop with a name so that arrows scroll it; assistive `scroll_into_view` requests are honoured by the engine; focus on a descendant scrolls it into view ([[14 Accessibility Basics]], [[Accessibility Tree]]).

## Dark and light

Roles per scheme; see [[Scrollbar and Scroll Container]].

## Defaults

`Orientation` VERTICAL, `Scroll_Offset` 0, no snap, bar visible on overflow, no auto-hide.

## Acceptance criteria

The criteria AC-SCB-01 to AC-SCB-21 of [[Scrollbar and Scroll Container]] apply to every ScrollBox and are not repeated. The block adds:

- [ ] AC-BLK-SBX-1 (scripted input): `Scroll_Offset` set to 10000 on content of 1000 dp in a 400 dp viewport reads back 600 at once and the view shows the end.
- [ ] AC-BLK-SBX-2 (geometry check): the ScrollBox accepts one content child; a second child is a schema error, not a silent drop.
- [ ] AC-BLK-SBX-3 (scripted input): with `Orientation: HORIZONTAL` inside a vertical ScrollBox, a plain wheel scrolls the outer box and Shift plus wheel the inner one.
- [ ] AC-BLK-SBX-4 (AT tree assertion): a ScrollBox with overflow and no focusable descendant is reachable by Tab and exposes a name.
- [ ] AC-BLK-SBX-5 (scripted input): `On_Scroll` fires once per frame with the old and new offsets, for wheel, key, focus and programmatic changes.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (`ScrollBox`: `Orientation`, `Scroll_Offset`; `Scroll_Snap` and `On_Scroll` not built), `tess-shell:src/tess_shell/binder/tables.py` | partly meets: wheel scrolling and engine keys; no scrollbar of either axis: fails AC-SCB-02 to 09, 12, 13 and AC-BLK-SBX-5; AC-BLK-SBX-2 not verified. Settable: no key reaches the thumb margin, thickness, minimum length, hit area or radius (project request) |
| tess-ui | `tess-ui:src/tess_ui/scrolling.py` (`ScrollView`) | partly meets: see [[Scrollbar and Scroll Container]]. Settable: `_scroll_props` sets only `scrollbar_fill` (role `outline`), so the thumb margin, thickness, minimum length, hit area and radius have no hook (project request) |
| tre | `tre:crates/engine-core/src/tree/scroll.rs`, `tre:docs/guide/nodes-and-layout.md` (Scrolling) | partly meets: see [[Scrollbar and Scroll Container]]: thumb 4 px, wheel 20 px, Page keys a full viewport. Settable: only the thumb thickness (`scrollbar_width`) and colour (`scrollbar_fill`) are properties, the margin, minimum length, grab slop and radius are hardcoded (engine request) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Visible scrollbar on both axes when content overflows | owner feedback F6 | [[ADR-0003 Scrollbar rule]] |
| Thumb opacity states and 12 dp hit area | accepted exception | [[ADR-0012 Scrollbar thumb opacity and hit area exception]] |

## Sources

- `shell-vault:41 TDL Reference/Block Reference.md` (ScrollBox, decided 2026-11-01, R3), `tess-shell:src/tess_shell/schema/blocks.py`.
- `tre:docs/guide/nodes-and-layout.md`, `tre:docs/reference/properties.md` (Scroll view).
- Sources of [[Scrollbar and Scroll Container]]. WCAG 2.2 SC 2.1.1: https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html.
