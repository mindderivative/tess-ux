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
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (`ScrollBox`: `Orientation`, `Scroll_Offset`; `Scroll_Snap` and `On_Scroll` not built), `tess-shell:src/tess_shell/binder/tables.py` | partly meets: wheel scrolling and engine keys; no scrollbar of either axis: fails AC-SCB-02 to 09, 12, 13 and AC-BLK-SBX-5; AC-BLK-SBX-2 not verified |
| tess-ui | `tess-ui:src/tess_ui/scrolling.py` (`ScrollView`) | partly meets: see [[Scrollbar and Scroll Container]] |
| tre | `tre:crates/engine-core/src/tree/scroll.rs`, `tre:docs/guide/nodes-and-layout.md` (Scrolling) | partly meets: see [[Scrollbar and Scroll Container]]: thumb 4 px, wheel 20 px, Page keys a full viewport |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Visible scrollbar on both axes when content overflows | owner feedback F6 | [[ADR-0003 Scrollbar rule]] |
| Thumb opacity states and 12 dp hit area | accepted exception | [[ADR-0012 Scrollbar thumb opacity and hit area exception]] |

## Sources

- `shell-vault:41 TDL Reference/Block Reference.md` (ScrollBox, decided 2026-11-01, R3), `tess-shell:src/tess_shell/schema/blocks.py`.
- `tre:docs/guide/nodes-and-layout.md`, `tre:docs/reference/properties.md` (Scroll view).
- Sources of [[Scrollbar and Scroll Container]]. WCAG 2.2 SC 2.1.1: https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html.
