---
title: Carousel
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, containment, carousel, scrolling]
related: ["[[Card]]", "[[List]]", "[[ScrollBox|Scroll View]]", "[[Scrollbar and Scroll Container#Behaviour|Scroll Behaviour]]", "[[Scrollbar and Scroll Container]]", "[[Icon Button]]", "[[Tooltip]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0012 Scrollbar thumb opacity and hit area exception]]"]
depends_on: ["[[Scrollbar and Scroll Container]]", "[[Shape]]", "[[Motion]]", "[[ADR-0003 Scrollbar rule]]"]
---

# Carousel

> [!info] Summary
> A carousel is a horizontally scrolling strip of rounded visual items that settles with an item lined up; item sizes follow one of four layouts (uncontained, multi-browse, hero, centre hero). Material Design 3 counterpart: [Carousel](https://m3.material.io/components/carousel/overview). Source of truth in code: see Status in code. No app or example uses it today.

## Purpose

Let a user browse a collection of visual items (photos, albums, previews) in one row, seeing several at once and choosing one.

## When to use and not

- Use when: the items are mainly pictures with a short caption and the collection is browsed, not scanned.
- Do not use when: items are text rows to scan, sort or select by keyboard type-ahead ([[List]]); items carry actions and detail ([[Card]] in a wrapping grid); the collection must be fully visible at once (a grid); content is a few steps of a flow (a page or tabs).
- A carousel never advances by itself by default. Auto-advance is an opt-in that follows WCAG 2.2 SC 2.2.2 and [[Motion]] rule 4 (see Behaviour).

## Anatomy

1. Container: a horizontal scroll container ([[ScrollBox|Scroll View]]) of the set width and height; it clips its items.
2. Item (several): a rounded container with an image filling it.
3. Caption band (optional): a band at the item bottom with the title and, optionally, supporting text.
4. Title: `title_medium`, one line, ellipsis.
5. Supporting text (optional): `body_small`, one line, ellipsis.
6. Scrollbar thumb along the bottom ([[ADR-0003 Scrollbar rule]]).
7. State layer and focus ring on the focused or pressed item.

MD3 names the sizes large, medium and small item ([Android guide](https://github.com/material-components/material-components-android/blob/master/docs/components/Carousel.md)); Tesserae uses the same names.

## Variants

| Variant | Item sizes | Alignment (snap) | Use |
|---|---|---|---|
| Uncontained | every item the set item width; the last item is cut by the container edge | start | items with a fixed aspect ratio |
| Multi-browse | large item, then a medium item, then small items | start | many small thumbnails with one featured |
| Hero | one large item and a small item that peeks | start | media with one subject at a time |
| Centre hero | one large item in the middle, small items on both sides | centre | a focused choice with neighbours |
| Full-screen | one edge-to-edge item | not specified | not built; see Deviations |

The first four are MD3 layouts (Android guide above, Layouts of carousel). In the Android implementation a large item is at most twice as wide as the carousel is tall. Desktop sizes are in Sizing and density.

## States

State layer colour `on_surface` on the item; percentages hover 8, focus 10, pressed 10 ([[State Layers]], [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). Material Web carousel-item tokens: elevation level 0 at rest, 1 on hover, 0 on focus and pressed ([md-comp-carousel-item](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-carousel-item.scss)).

| State | Visual change | Token values |
|---|---|---|
| Rest | item container `surface`, image fills it | shape `extra_large` (28 dp) |
| Hover | state layer 8 percent; elevation level 1 | `on_surface` at 0.08 |
| Focus (keyboard) | state layer 10 percent; ring 3 dp, 2 dp offset, `secondary`; the item is scrolled fully into view | [[Focus Ring]] |
| Pressed | state layer 10 percent; ripple; elevation 0 | `on_surface` at 0.10 |
| Selected (the chosen item) | the chosen item reports `selected`; a visual mark is the caller's (a check or ring) | not specified in MD3 |
| Dragging (the strip) | the strip follows the pointer; no state layer | not applicable |
| Disabled item | image and caption at 38 percent opacity, no state layer, no focus | [[State Layers]] |
| Empty | a carousel with no items shows nothing and is not focusable | not applicable |
| Loading | items without an image show the `surface_container_highest` fill | [[Colour Roles]] |

## Tokens used

| Part | Role or token |
|---|---|
| Item container | `surface` (Material Web `container-color`), shape `extra_large` (28 dp, `corner-extra-large`) |
| Item fill when no image | `surface_container_highest` |
| Caption band | `scrim` at 0.60 opacity ([[ADR-0016 Carousel caption colour]]) |
| Title, supporting text | `title_medium`, `body_small`; colour `on_scrim` (supporting text at 80 percent of `on_scrim`) over the band |
| Outline (optional) | 1 dp `outline` (`with-outline-outline-width` 1 px) |
| Focus ring | `secondary` ([[Focus Ring]]) |

See [[Colour Roles]], [[Typography]], [[Shape]], [[Elevation]], [[Motion]], [[Spacing and Density]]. The caption text colour is the role `on_scrim` ([[ADR-0016 Carousel caption colour]]); there is no colour literal. The contrast figures below assume `on_scrim` resolves to white (the scheme value is defined in [[Colour Roles]]).

## Sizing and density

Item height is set by the caller (default 200 dp at default density, 160 and 128 at compact and dense). The gap between items, the caption band and the container padding follow the density level ([[ADR-0002 Desktop density levels and target sizes]]); the corner does not.

| Item | default | compact | dense | MD3 or source value |
|---|---|---|---|---|
| Gap between items | 8 | 8 | 4 | 8 (tess-ui); MD3 item gap #needs-verification |
| Caption band height | 64 | 56 | 48 | 64 (tess-ui) |
| Caption padding horizontal | 16 | 12 | 8 | 16 (tess-ui) |
| Item corner | 28 | 28 | 28 | 28 (`corner-extra-large`) |
| Small item width | 56 | 48 | 40 | 56 (tess-ui); MD3 small item 40 to 56 dp #needs-verification |
| Carousel height (default) | 200 | 160 | 128 | 200 (tess-ui) |
| Peek in hero layouts | 56 + gap | 48 + gap | 40 + gap | tess-ui |

Layouts for a carousel of width W (tess-ui formulas, adopted as the spec at default density): uncontained item width = set item width (default 200 dp); multi-browse: large 0.55 W, medium 0.28 W, then small items; hero: item width W − small width − gap; centre hero: item width W − 2 × small width − 2 × gap, with padding of small width plus gap at both ends. A large item is never wider than twice the carousel height.

- Hit area: the whole item, at least 24 by 24 dp at every level (a small item is 40 dp wide at the narrowest, 56 dp wide at default).
- Minimum carousel width: 120 dp; narrower, the parent uses a single [[Card]] or a vertical list ([[10 Layout Overflow and Scrolling]]).

## Layout and overflow

- A carousel is a scroll container on the horizontal axis: it shows a scrollbar thumb whenever the items overflow ([[ADR-0003 Scrollbar rule]], thumb opacity per [[ADR-0012 Scrollbar thumb opacity and hit area exception]]); no auto-hide. Vertical overflow does not occur: the height is set.
- Items are clipped to the 28 dp corner; the image uses cover fit and centre crop. The caption sits at the bottom edge of the item and is clipped with it.
- Title and supporting text are one line each with an end ellipsis ([[10 Layout Overflow and Scrolling]]); the full text is the accessible name and the tooltip text. Single-line text is vertically centred in the band (space above and below differ by at most 1 px).
- The scroll range reaches both ends: the first item can align at the start and the last item at the end (or the centre in the centre-hero layout) (AC-LAY-8).
- Space runs out: items keep their widths and the strip scrolls; the strip never squeezes items below the small item width.

## Behaviour

- Pointer: wheel scrolls the strip horizontally (a vertical wheel turn scrolls sideways when the strip cannot scroll vertically; Shift plus wheel always); dragging the strip scrolls it with momentum; dragging the thumb scrolls it. On release the strip settles with an item at the start (centre in centre hero) (snap, [[Scrollbar and Scroll Container#Behaviour|Scroll Behaviour]]). A press on an item chooses it.
- Keyboard: the carousel is one group; Left and Right Arrow move focus to the previous and next item and scroll it fully into view (AC-LAY-14); Home and End move to the first and last item; Enter and Space choose the focused item; Tab leaves the carousel to the next control (the focus group is one Tab stop; Shift+Tab enters on the last focused item). A carousel never traps focus.
- Touch: swipe scrolls with momentum and settles on snap; a tap chooses; hit areas are 48 by 48 dp at least in a touch context.
- Auto-advance (opt-in): off by default. When on, it pauses while the pointer is over the carousel or focus is inside it, offers a visible pause and play control ([[Icon Button]]), and does not start under reduced motion (WCAG 2.2 SC 2.2.2 Pause, Stop, Hide; [[Motion]] rule 4; APG carousel pattern).
- The caller owns what choosing does (open, select, play); the carousel reports the chosen value.

## Tooltip and overlay behaviour

The tooltip belongs to the item, which is the control: when a title or supporting text is truncated, hovering the item for 500 ms or focusing it by keyboard shows a plain tooltip with the full text, kept open over the pointer move onto it for 150 ms ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]], [[Tooltip]]). The tooltip is dismissed on scroll of the strip, on press and on Escape. A carousel opens no overlay itself; the caller's action may (a [[Dialog]], a screen). Previous and next buttons, if the caller adds them, carry tooltips per [[Icon Button]].

## Motion

Scrolling and settling: the scroll offset eases to the snap point; the tre engine settles 120 ms after the last wheel event and then animates 200 ms (`short4`) ([[Scrollbar and Scroll Container#Behaviour|Scroll Behaviour]], `tre:docs/guide/nodes-and-layout.md`). State changes: 150 ms colour, 200 ms elevation ([[Motion]]). MD3 sizes items continuously as they scroll (a large item shrinks as it leaves); this change of size while scrolling is optional in Tesserae and not built. With reduced motion on, settling and state changes complete on the next frame and no auto-advance runs.

## Accessibility

- Role: container `list` named by its label (for example the collection name), each item `listitem` with the title as name; the whole carousel is a group of one set. A `listitem` without a `list` parent is invalid (AC-CRS-9). APG describes a carousel as a group with role description "carousel" and slides as groups ([APG carousel pattern](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/)); tre has no role description property, so the list form carries the semantics #needs-verification.
- Name: item name is the title; an item without a title needs a label. Position is announced as "n of m" through set size and position (AC-LAY-13).
- Keys: see Behaviour. Escape does nothing in a carousel (no overlay).
- Contrast: the caption text on the band is at least 4.5:1 against the worst-case image under the band, a white pixel field (see below); the focus ring at least 3:1.
- Caption legibility ([[ADR-0016 Carousel caption colour]]): `on_scrim` text (white) on a `scrim` band (black) at alpha a over a white image has contrast 1.05 / (L + 0.05), with L the luminance of the darkened white; 4.5:1 needs L at most 0.183, hence a at least 0.535. At a = 0.60 the band over white is sRGB 102 (0.40 of 255), L = 0.1329, and the contrast is 1.05 / 0.1829 = 5.74:1 (recomputed 2026-11-21, 5.7:1 as in the ADR). The 0.32 band of tess-ui gives 2.2:1 over white and fails.
- Auto-advance, when on, is controllable (SC 2.2.2); content moving under reduced motion is stopped.
- Images carry a text alternative through the title; a purely decorative image is hidden from assistive technology ([[Accessibility Rules]] AR-5).

## Dark and light

The item container, the fill when no image, the state layer and the ring follow the theme ([[Theme Following the System]]). The image and the caption (`on_scrim` on a `scrim` band at 0.60) are the same in both themes.

## Defaults

| Setting | Default |
|---|---|
| Variant | uncontained |
| Width, height | 360 dp by 200 dp (tess-ui) |
| Item width (uncontained) | 200 dp |
| Gap, corner | 8 dp, 28 dp |
| Snap | start (centre for centre hero) |
| Auto-advance | off |
| Scrollbar | shown when items overflow |

## Acceptance criteria

- [ ] AC-CRS-1 (token test): item container `surface`, shape `extra_large` 28 dp at every density; image fill when no image `surface_container_highest`; caption band `scrim` at 0.60.
- [ ] AC-CRS-2 (geometry check): for width 360 dp and height 200 dp at default density: uncontained items are 200 dp wide, 8 dp apart; multi-browse items are 198 dp (0.55 W), 100.8 dp (0.28 W) and 56 dp wide in order; hero items are 296 dp wide (W − 56 − 8); centre-hero items are 232 dp wide (W − 112 − 16) with 64 dp padding at both ends (±0.5 dp).
- [ ] AC-CRS-3 (geometry check): at compact and dense the gap is 8 and 4 dp, the caption band 56 and 48 dp, the small item 48 and 40 dp (scale factors 1.0 and 2.0).
- [ ] AC-CRS-4 (scripted input): after a wheel turn of any size and 400 ms of rest, an item's start edge (centre in centre hero) is at the container start (centre) within 1 dp; a turn too small to move one item returns to the first item.
- [ ] AC-CRS-5 (scripted input): focus the first item; Right Arrow x5 moves focus to item 6 and the item lies fully inside the viewport with its ring (5 dp beyond the border box) visible; End focuses the last item and Home the first; Enter and Space on a focused item deliver its value once.
- [ ] AC-CRS-6 (scripted input): Tab from the control before the carousel lands on the carousel once; one more Tab leaves it; Shift+Tab returns to the last focused item; no key sequence traps focus.
- [ ] AC-CRS-7 (geometry check): a carousel with content wider than its width shows a horizontal thumb meeting [[Scrollbar and Scroll Container]] dimensions at 60, 80 and 100 percent opacity for rest, hover and drag; with content that fits, no thumb shows.
- [ ] AC-CRS-8 (geometry check): a title of 60 characters in a 160 dp wide item shows one line ending in `…`, the accessible name and the tooltip text are the full title, and hovering 500 ms (or keyboard focus) shows the tooltip with the item as trigger.
- [ ] AC-CRS-9 (AT tree assertion): the container has role `list` and a non-empty name, each item has role `listitem` with the title as name and set size and position, no `listitem` lacks a `list` ancestor.
- [ ] AC-CRS-10 (contrast script): the caption text role is `on_scrim` and the band role is `scrim` at 0.60 ([[ADR-0016 Carousel caption colour]]); `on_scrim` text over a white image under the band measures at least 5.7:1 (computed 5.74:1) and in no case below 4.5:1; the focus ring at least 3:1 against the image edge sample. Pass: measured ratios and zero colour literals in the caption.
- [ ] AC-CRS-11 (token test): state layers on an item: hover 0.08, focus 0.10, pressed 0.10 of `on_surface`; elevation 1 on hover, 0 at rest, focus and pressed.
- [ ] AC-CRS-12 (pixel check): the settle animation after a wheel turn ends at most 400 ms after the last event; with reduced motion the end state is drawn on the next frame and an enabled auto-advance does not start.
- [ ] AC-CRS-13 (scripted input): with auto-advance enabled, the carousel stops advancing while the pointer is over it and while focus is inside it, and a pause control is reachable by keyboard.
- [ ] AC-CRS-14 (scripted input): a disabled item takes no focus and no press and is drawn at 38 percent opacity.
- [ ] AC-CRS-15 (review): the carousel is used only for visual items; no item is reachable only by drag (the scrollbar, keyboard and wheel reach every item).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Carousel_View.tdl`, `tess-ui:src/tess_ui/views/Carousel_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/containment.py` (`carousel`, `carousel_layout`), `tess-ui:docs/components/carousel.md`, tests `tess-ui:tests/test_carousel.py` | Partly meets. Meets AC-CRS-1 in part (28 px corners, `surface_container_highest` fill; the item container is `surface_container_highest`, not `surface`; caption band `scrim@32%`, not 0.60), AC-CRS-2 (formulas as in the spec, tested at the layout level), AC-CRS-4 in part (snap start or centre, tested; the engine settles 120 ms then 200 ms), AC-CRS-5 in part (items focusable, horizontal focus group; Home and End not verified). Fails AC-CRS-3 (gap fixed 8, no density), AC-CRS-9 (container role `group`, items `listitem` with no `list` parent), AC-CRS-10 (caption `#FFFFFF` on a 32 percent band: 2.2:1 over white), AC-CRS-11 (no hover elevation; state layer and focus ring come from the shared mechanism and are not asserted), AC-CRS-13 (no auto-advance exists, so not applicable until built). Size change while scrolling, parallax, dot indicators, full-screen and autoplay are not built. `COMPONENT_LIST.md` still labels Carousel "Python only" though a TDL view ships ([[Gaps and Contradictions]]). Not used by any app or example |
| tess-shell | none | Absent. No shipped module scrolls a strip of visual items |
| tre | `tre:docs/guide/nodes-and-layout.md` (Scrolling, Snapping), `tre:crates/engine-core/src/tree/scroll.rs` | Mechanism only: `scroll_snap` start, centre, end, `snap_align` per child, always mandatory; scroll chaining to the outer view; no proximity mode; one-axis scroll view; no role description property |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Caption band `scrim` at 0.60 with caption text `on_scrim` | the image does not follow the theme, so no role pair under the image guarantees 4.5:1; the band at 0.60 gives 5.7:1 over a white image; no colour literal remains | [[ADR-0016 Carousel caption colour]] |
| Scrollbar thumb shown whenever items overflow | owner rule for every scroll container | [[ADR-0003 Scrollbar rule]] |
| Gap, caption band and small item width scale with density | desktop information density | [[ADR-0002 Desktop density levels and target sizes]] |
| Items do not resize continuously while scrolling (not built) | engine has no per-item size animation tied to scroll; MD3 describes the effect | [[Deviations from MD3]] |
| Full-screen layout not specified | no desktop use case; touch layout | [[Deviations from MD3]] |
| No auto-advance by default; opt-in with pause | WCAG 2.2 SC 2.2.2 and reduced-motion rule | [[Motion]] |
| Arrow keys, Home and End move between items | desktop keyboard-first use; MD3 documents no keyboard model | [[14 Accessibility Basics]] |

## Sources

- Material Web carousel item tokens (container `surface`, shape `corner-extra-large`, hover elevation level 1, state layers `on-surface`, outline 1 px `outline`, disabled opacity 0.38), verified 2026-11-21: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-carousel-item.scss
- Material Components Android Carousel guide (four layouts, large item at most twice the carousel height, snap helper, extra-large item shape): https://github.com/material-components/material-components-android/blob/master/docs/components/Carousel.md
- WAI-ARIA Authoring Practices carousel pattern (previous and next controls, rotation control, pause on hover and focus): https://www.w3.org/WAI/ARIA/apg/patterns/carousel/
- WCAG 2.2 SC 2.2.2 Pause, Stop, Hide: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html
- tess-ui carousel documentation: `tess-ui:docs/components/carousel.md`; engine snapping: `tre:docs/guide/nodes-and-layout.md`.
- Not verified: MD3 item gap (8 dp) and small item width range (40 to 56 dp) on the specification page, which is a script-rendered app #needs-verification; the role description and the `list` mapping in tre #needs-verification.
