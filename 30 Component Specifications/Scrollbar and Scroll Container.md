---
title: Scrollbar and Scroll Container
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, scrolling, overflow, owner-feedback]
related: ["[[ADR-0003 Scrollbar rule]]", "[[10 Layout Overflow and Scrolling]]", "[[Owner Feedback 2026-11-20]]", "[[Tree]]", "[[List]]", "[[Form Row]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[State Layers]]", "[[Shape]]", "[[Motion]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0003 Scrollbar rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]"]
---

# Scrollbar and Scroll Container

> [!info] Summary
> A scroll container clips its content and moves it along one or both axes; its scrollbar shows where the viewport sits in the content and lets the pointer drag it. Material Design 3 has no scrollbar component (see Sources), so this note is a Tesserae specification that implements [[ADR-0003 Scrollbar rule]] completely. Source of truth in code: the last section.

## Purpose

Show the user that content continues past the visual frame and give a pointer, a keyboard and a wheel the same, predictable way to reach it. Owner feedback F6 ("no horizontal scroll bars though every panel has content past the visual frame", [[Owner Feedback 2026-11-20]]) is the origin of the rule that every axis with overflow shows its own scrollbar.

## When to use and not

- Use when: a panel, pane, list, tree, form or text area can hold more content than its frame on one or both axes.
- Do not use when: content is fitted by wrapping or by ellipsis (see [[10 Layout Overflow and Scrolling]]); prefer wrapping or ellipsis first, a scrollbar is the fallback and never the cure for a label that could truncate.
- Use a paged or snapped container (Carousel, Tabs) when items are discrete; snap is described below.

## Anatomy

1. Scroll container: a clipping box with a viewport, content and a scroll offset per axis.
2. Thumb: the painted bar whose length is proportional to viewport divided by content.
3. Track: the invisible lane the thumb moves in; track-less by default (nothing painted).
4. Hit area: the pointer-sensitive strip around the thumb and along the lane.
5. Gutter: space reserved at the end edge of an overflowing axis so that content does not sit under the thumb.
6. Corner: the square where two bars would meet; it stays empty.

```mermaid
flowchart LR
  C[Scroll container: clips content] --> V[Vertical bar: right edge]
  C --> H[Horizontal bar: bottom edge]
  V --- K[Corner 12 x 12 dp, empty]
  H --- K
```

## Variants

| Variant | Use | Differences |
|---|---|---|
| Vertical | default for lists, forms, trees | bar on the end side (right in left-to-right) |
| Horizontal | wide trees, tables, code, wide forms | bar on the bottom edge |
| Both axes | trees with long labels, canvases, tables | two thumbs, corner square, see AC-SCB-04 |
| Virtualised | long lists that build only visible rows | same bar; the thumb length uses the estimated total extent; the same keys apply, see Behaviour |
| Snapping | carousels, tab strips, pickers | the offset settles on a snap point, see Motion |

## States

The thumb colour role is `on_surface_variant` ([[Colour Roles]]). The opacities are Tesserae design choices accepted by [[ADR-0012 Scrollbar thumb opacity and hit area exception]] (amending [[ADR-0003 Scrollbar rule]]); the state-layer percentages of [[ADR-0009 State layer percentages]] do not apply, because a thumb is a painted indicator and not a pressable surface. No MD3 value exists for a scrollbar thumb; the contrast check of AC-SCB-09 is the basis of the rest value.

| State | Visual change | Token values |
|---|---|---|
| Rest | thumb visible whenever the axis overflows | `scrollbar.thumb.opacity.rest` 0.60 |
| Hover (pointer inside the hit area) | thumb darker, same size | `scrollbar.thumb.opacity.hover` 0.80 |
| Dragged | thumb at full opacity | `scrollbar.thumb.opacity.drag` 1.00 |
| Focus | none on the thumb; the container shows the [[Focus Ring]] only if it is itself focusable and has no focusable descendant | focus ring tokens |
| Disabled | not applicable; a container that cannot scroll shows no thumb | none |
| No overflow on an axis | no thumb for that axis, no gutter for that axis | none |
| Empty content | no thumb | none |

## Tokens used

Colour from [[Colour Roles]], radius from [[Shape]], density and targets from [[Spacing and Density]]. The scrollbar tokens are defined here once; other notes link to this table.

| Token | Value | Notes |
|---|---|---|
| `scrollbar.thumb.thickness` | 8 dp | painted size across the axis; #needs-verification (design choice) |
| `scrollbar.hit.thickness` | 12 dp | pointer-sensitive size across the axis, centred on the thumb (8 dp thumb plus 2 dp margin each side) |
| `scrollbar.margin` | 2 dp | between thumb and container edge, and between thumb end and lane end |
| `scrollbar.thumb.min_length` | 32 dp | along the axis |
| `scrollbar.thumb.radius` | `full` (4 dp at 8 dp thickness) | [[Shape]] |
| `scrollbar.thumb.color` | role `on_surface_variant` | |
| `scrollbar.thumb.opacity.rest` / `.hover` / `.drag` | 0.60 / 0.80 / 1.00 | accepted by [[ADR-0012 Scrollbar thumb opacity and hit area exception]]; contrast of the rest value: AC-SCB-09 |
| `scrollbar.track.color` | none (transparent) | a track-less thumb is allowed by [[ADR-0003 Scrollbar rule]] |
| `scrollbar.gutter` | 12 dp (equals `scrollbar.hit.thickness`) | reserved at the end edge of an axis that overflows; #needs-verification (design choice) |
| `scrollbar.corner` | 12 dp square, empty | where both axes overflow |
| `scroll.key.line` | 40 dp | arrow keys |
| `scroll.key.page` | viewport extent minus 10 percent | Page Up, Page Down, track click |
| `scroll.wheel.notch` | 40 dp per notch | #needs-verification (design choice); the engine moves 20 dp per notch today |
| `scroll.snap.settle` / `.duration` | 120 ms / 200 ms | engine values, kept |

The values do not change with density: the bar is a pointer target of its own and the 8 dp thumb with 12 dp hit area is the same at `default`, `compact` and `dense` ([[Spacing and Density]]). Touch contexts (ADR-0002, 48 dp targets) set `scrollbar.hit.thickness` to 48 dp.

## Sizing and density

- Thumb 8 dp across the axis, hit strip 12 dp, minimum thumb length 32 dp (a 24 dp minimum target length is met on the long side).
- The 12 dp hit thickness is below the 24 dp minimum pointer target of WCAG 2.2 SC 2.5.8. The note relies on the equivalent-control exception of that criterion, accepted by [[ADR-0012 Scrollbar thumb opacity and hit area exception]]: every scroll container offers keyboard scrolling (arrows, Page Up, Page Down, Home, End) and wheel scrolling, so the thumb is never the only way to scroll. A container that cannot be scrolled by keyboard does not qualify and must use a 24 dp hit thickness (AC-SCB-21).
- Thumb length along an axis = max(`scrollbar.thumb.min_length`, lane x viewport / content), where lane = viewport extent - 2 x `scrollbar.margin` (minus `scrollbar.corner` when the other axis also overflows).

## Layout and overflow

- A container shows the bar of an axis if and only if content extent exceeds viewport extent on that axis (F6). Overflow is measured, not assumed from the content type.
- Content stays inside the frame: the container clips to its bounds and corner radius; nothing is drawn past the frame.
- Both axes: two thumbs. The vertical lane ends `scrollbar.corner` above the bottom edge and the horizontal lane ends `scrollbar.corner` left of the right edge, so the two thumbs never overlap. The corner square is empty.
- The gutter: when an axis overflows, content end padding on the cross axis is at least `scrollbar.gutter`, so that a label or control is not covered by the thumb. A vertical thumb sits in the right gutter, a horizontal one in the bottom gutter.
- Ellipsis and wrapping come first: a label that can truncate truncates (see [[Tree Node]], [[List Item]]); only content that cannot shrink (a long unbroken code line, a wide table) makes a horizontal bar.
- A scroll container nested in another passes on the wheel and keys it cannot use (scroll chaining).

## Behaviour

- Pointer:
  - Wheel: one notch moves `scroll.wheel.notch`; vertical wheel moves the vertical axis; Shift plus wheel, or a sideways wheel or trackpad, moves the horizontal axis. Over a container that cannot move that way the wheel goes to the container outside it.
  - Drag: pressing inside the hit area of the thumb grabs it; the offset follows the pointer linearly, offset = start offset + pointer delta x (content - viewport) / (lane - thumb length); the drag continues while the pointer is outside the gutter and ends on release.
  - Click on the lane outside the thumb: scrolls by `scroll.key.page` toward the click, repeating while pressed with a 400 ms first delay and a 100 ms repeat #needs-verification (design choice).
  - Hover over the hit area switches the thumb to the hover opacity.
- Keyboard (any container that has focus or contains the focused node; a container with overflow and no focusable descendant is itself a Tab stop):

| Key | Vertical axis | Horizontal axis |
|---|---|---|
| Up, Down | one line, 40 dp | none |
| Left, Right | none | one line, 40 dp |
| Page Up, Page Down | viewport extent minus 10 percent | none |
| Home, End | offset 0, offset max | offset 0, offset max when the container is horizontal only |
| Shift plus Page Up, Page Down | none | viewport extent minus 10 percent |

  Keys the focused node uses itself are not scrolled (a text input keeps its arrows and Home, End). Ctrl, Alt and Meta combinations are shortcuts and never scroll. Keyboard scrolls jump, they do not ease.
- Virtualised lists and trees: the same keys, and moving the focus to a row scrolls it into view by the least distance that shows it; Home and End move focus and offset to the first and last row. The thumb is draggable. A virtualised container whose rows are not scrollable by key violates [[ADR-0003 Scrollbar rule]].
- Focus: moving focus into a child scrolls it into view by the least distance that shows it, with `scrollbar.gutter` and the [[Focus Ring]] outset (3 dp ring plus 2 dp offset) inside the viewport.
- Touch: drag pans the content with fling; the bar is shown while content overflows and is not the touch handle.
- Snap (`scroll_snap` start, center or end): after the last input the offset settles on the nearest snap point within `scroll.snap.settle` and animates `scroll.snap.duration`; programmatic offsets are not snapped; the default is no snap.

## Tooltip and overlay behaviour

The scrollbar has no tooltip. A scroll offset indicator tooltip ("page 3 of 9") is not specified. A scrolling ancestor dismisses any open tooltip inside it ([[ADR-0004 Tooltip rule]]).

## Motion

- Wheel and key scrolls jump; thumb opacity changes use `short2` 100 ms ([[Motion]]); no fade in or out of the bar (no auto-hide).
- Snap settles over 200 ms with `easing-standard` cubic-bezier(0.2, 0, 0, 1); under reduced motion the settle is 0 ms.

## Accessibility

- A container with overflow and no focusable descendant is a Tab stop with an accessible name (its pane label) so that arrows scroll it ([[14 Accessibility Basics]]).
- Assistive technology can request that a node scroll into view and the container honours it.
- The thumb is not a separate focus stop and is hidden from the accessibility tree; its position equals the container offset. Whether to expose a `scrollbar` role with value is #needs-verification.
- Thumb contrast: the thumb at rest needs 3 to 1 against the container colour for WCAG 2.2 SC 1.4.11 non-text contrast when it is the only cue for hidden content. Calculation for the baseline scheme (`on_surface_variant` over `surface`): at 0.38 the ratio is 2.57 to 1 in dark and 1.94 to 1 in light; at 0.60 it is 4.61 and 3.11; at 1.00 the full role colour applies. [[ADR-0012 Scrollbar thumb opacity and hit area exception]] sets the rest opacity to 0.60 for that reason. The figures were computed while drafting this note and are not yet from a shipped contrast script.
- Target size: see Sizing; the 12 dp hit thickness relies on the equivalent-control exception of WCAG 2.2 SC 2.5.8 (ADR-0012), tested by AC-SCB-21.

## Dark and light

Colours are roles and follow the scheme ([[Theme Following the System]]). No hex value is fixed in the container; only the opacity tokens are.

## Defaults

Both axes enabled, thumb visible whenever overflow exists, no auto-hide, no track, no snap, vertical wheel to vertical axis, hit 12 dp, gutter 12 dp.

## Acceptance criteria

- [ ] AC-SCB-01: Token test. The scrollbar token set exists with `scrollbar.thumb.thickness` 8, `scrollbar.hit.thickness` 12, `scrollbar.margin` 2, `scrollbar.thumb.min_length` 32, `scrollbar.gutter` 12, `scroll.key.line` 40. Passes when every value is equal to the table.
- [ ] AC-SCB-02: Geometry check (F6, vertical). A container whose content height exceeds its viewport shows a vertical thumb; one whose content fits shows none. Passes when the thumb rectangle exists if and only if content height > viewport height, for 10 heights around the boundary.
- [ ] AC-SCB-03: Geometry check (F6, horizontal). The same for width and a horizontal thumb. Passes when every axis follows its own overflow independently of the other axis.
- [ ] AC-SCB-04: Geometry check (F6, two axes). With overflow on both axes the two thumb rectangles do not intersect, the vertical lane ends 12 dp above the bottom edge, the horizontal lane 12 dp left of the right edge, and the 12 by 12 dp corner is background colour. Passes when intersection area is 0 and corner pixels equal the container surface.
- [ ] AC-SCB-05: Geometry check. Thumb length = max(32, lane x viewport / content) within 1 dp, for content/viewport ratios 1.01, 2, 10 and 1000 on a 400 dp viewport.
- [ ] AC-SCB-06: Scripted input. A press at 6 dp from the thumb centre across the axis (inside the 12 dp hit strip) grabs the thumb; a press at 8 dp does not. Passes when the drag moves the offset in the first case and not in the second.
- [ ] AC-SCB-07: Pixel check. After 10 s of no input the thumb is painted with the rest opacity, and no frame between has a lower thumb alpha (no auto-hide).
- [ ] AC-SCB-08: Pixel check and token test. Thumb alpha is 0.60 at rest, 0.80 under the pointer, 1.00 while dragged, role `on_surface_variant`, in light and dark.
- [ ] AC-SCB-09: Contrast script. For the baseline light and dark schemes, the thumb composited at the rest opacity 0.60 over the container colour reaches at least 3 to 1. Passes at 3.0 or higher (computed 4.61 dark, 3.11 light); a rest opacity of 0.38 fails (2.57 and 1.94).
- [ ] AC-SCB-10: Scripted input. With focus in a container with 1000 dp of overflow and a 400 dp viewport: Down moves the offset by 40, Page Down by 360, End to 600, Home to 0, Right on a vertical-only container by 0.
- [ ] AC-SCB-11: Scripted input. A wheel notch moves 40 dp; Shift plus wheel moves the horizontal offset 40 dp; a wheel over an inner container already at its end moves the outer container.
- [ ] AC-SCB-12: Scripted input. Dragging the thumb by d dp changes the offset by d x (content - viewport) / (lane - thumb) within 1 dp, also when the pointer leaves the gutter during the drag.
- [ ] AC-SCB-13: Scripted input. A press on the lane 100 dp past the thumb scrolls one page (viewport minus 10 percent) toward the press and stops when the thumb reaches the press point.
- [ ] AC-SCB-14: Scripted input on a virtualised list of 100000 rows. End moves focus and offset to the last row, Home to the first, Page Down moves focus by a page, and the focused row is fully inside the viewport after each key.
- [ ] AC-SCB-15: Geometry check. After Tab moves focus to an off-screen control, the control and its 3 dp focus ring plus 2 dp offset lie inside the viewport minus the gutter.
- [ ] AC-SCB-16: Geometry check. With a vertical thumb shown, no content (text or control) in the container has its end edge within the 12 dp gutter.
- [ ] AC-SCB-17: Scripted input. With `scroll_snap: start`, 120 ms after the last input the offset equals the nearest snap point after a 200 ms animation (0 ms under reduced motion); without `scroll_snap` no settle occurs.
- [ ] AC-SCB-18: Config-app sweep (F6). For every scroll container of the configuration window at 800 by 600 and 1920 by 1080, each axis with content extent greater than viewport extent shows its bar. Passes when no container has overflow on an axis without a bar.
- [ ] AC-SCB-19: AT tree assertion. A scroll request from assistive technology for an off-screen node brings it inside the viewport, and an overflowing container with no focusable descendant is reachable by Tab.
- [ ] AC-SCB-20: Pixel check. Content is clipped to the container bounds and its corner radius; no pixel of the content lies outside the frame.
- [ ] AC-SCB-21: Scripted input and token test. The equivalent-control exception holds: every scroll container with `scrollbar.hit.thickness` below 24 dp responds to Up, Down, Page Up, Page Down, Home and End when focused and to the wheel when hovered (AC-SCB-10, AC-SCB-11). Pass: a container that fails either test uses `scrollbar.hit.thickness` of at least 24 dp.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/scrolling.py`, `tess-ui:docs/guide/layout.md` (Scrolling), `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` | partly meets: `ScrollView` scrolls one axis (`Orientation`, vertical default), the keys and wheel come from the engine; two-way scrolling is planned on branch `feat/scrollview-two-way` (status of the branch not verified); bar colour is `outline` and not `on_surface_variant`; size is engine-owned. Fails AC-SCB-01, 03 (config app uses vertical scroll views only), 04, 08, 09, 11, 13, 16, 18; AC-SCB-07 is not verified |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (`ScrollBox`) | partly meets: wheel and the List keys only; no scrollbar of either axis (absent: AC-SCB-02 to 09, 12, 13) |
| tre | `tre:crates/engine-core/src/tree/scroll.rs`, `tre:crates/engine-core/src/node.rs` (lines near 510 to 530), `tre:docs/guide/nodes-and-layout.md` | partly meets: `scroll_view` is one axis (nest a horizontal view in a vertical one for two axes); thumb 4 px (spec 8), margin 2 (meets), min length 32 (meets), grab slop 6 px, radius 2, fill `#CAC4D0` at 55 percent, no track, no auto-hide (meets); arrow line 40 (meets), Page Up and Page Down a full viewport (spec viewport minus 10 percent: fails AC-SCB-10), Home and End (meets); wheel notch 20 px (spec 40: fails AC-SCB-11); no click on the lane (fails AC-SCB-13); `virtual_list` has a draggable vertical thumb and no key handling and `scroll_into_view` skips it (fails AC-SCB-14); snap 120 ms plus 200 ms (meets) |

Evidence: F6 in [[Owner Feedback 2026-11-20]]; the engine thumb of 4 px is the likely cause of the thin bar the owner saw.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| MD3 has no scrollbar component; Tesserae specifies one | desktop content overflows on two axes and needs a visible indicator | [[ADR-0003 Scrollbar rule]] |
| No auto-hide by default | desktop users need a permanent cue that content continues | [[ADR-0003 Scrollbar rule]] |
| Track-less thumb with opacity states instead of state layers | a thumb is an indicator, not a surface | [[ADR-0003 Scrollbar rule]] |

## Sources

- Material Web repository: no scrollbar component or token in `tokens/`, `docs/components/` (tree listing of https://github.com/material-components/material-web read 2026-11-21); the engine source comment says the same (`tre:crates/engine-core/src/node.rs`). The m3.material.io pages are a JavaScript application and were not read. #needs-verification (that no scrollbar guidance exists on https://m3.material.io).
- WCAG 2.2 SC 2.5.8 and its exceptions: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html (Spacing, Equivalent, Inline, User Agent Control, Essential).
- Engine values: `tre:crates/engine-core/src/tree/scroll.rs` (`KEY_SCROLL_LINE` 40, snap 120 and 200 ms), `tre:crates/engine-core/src/tree/dispatch.rs` (wheel line 20 px), `tre:docs/guide/nodes-and-layout.md` (Scrolling, Keyboard scrolling, Snapping).
