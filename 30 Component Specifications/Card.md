---
title: Card
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, containment, card]
related: ["[[Panel and Surface]]", "[[Button]]", "[[Icon Button]]", "[[List]]", "[[List Item]]", "[[Carousel]]", "[[Dialog]]", "[[Accordion]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[State Layers]]", "[[Spacing and Density]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
---

# Card

> [!info] Summary
> A card is a surface that holds content and actions about one subject, in three variants (elevated, filled, outlined) with a 12 dp corner. Material Design 3 counterpart: [Cards](https://m3.material.io/components/cards/overview). Source of truth in code: see Status in code. No app or example uses it today.

## Purpose

Group the text, media and actions of one subject (a trip, a file, a device, a recipe) on a surface that separates the group from its neighbours and, when the whole card is pressable, opens that subject.

## When to use and not

- Use when: items are heterogeneous (media, headline, text, actions) and each is a self-contained subject; a collection is browsed as tiles, not scanned as rows.
- Do not use when: items are homogeneous rows to scan and sort (use [[List]] and [[List Item]]); the surface only separates a region of a window (use [[Panel and Surface]]); the content blocks the task ([[Dialog]]); a row expands in place ([[Accordion]]); a horizontal strip of media is scrolled ([[Carousel]]).
- A card does not contain another card. An actionable card does not contain buttons or other focusable controls (MD3 asks to avoid the conflict: two actions on one target; `tess-ui:docs/components/cards.md`). A plain card may hold [[Button]] actions.

## Anatomy

1. Container: elevated, filled or outlined; shape `medium`.
2. Media (optional): picture across the top, clipped to the corner.
3. Headline: `title_large`, `on_surface`.
4. Subhead (optional): `title_small`, `on_surface_variant`.
5. Supporting text (optional): `body_medium`, `on_surface_variant`.
6. Content slot (optional): the caller's own nodes.
7. Actions row (optional): [[Button]] instances, end-aligned, 8 dp gap.
8. State layer (actionable and draggable cards only; [[State Layers]]).
9. Focus ring (actionable cards, keyboard focus; [[Focus Ring]]).

## Variants

| Variant | Container | Outline | Elevation: rest, hover, focus, pressed, dragged (level) | Use |
|---|---|---|---|---|
| Elevated | `surface_container_low` | none | 1, 2, 1, 1, 4 | separation by shadow on a plain `surface` |
| Filled | `surface_container_highest` | none | 0, 1, 0, 0, 3 | separation by tone; the default for dense UI |
| Outlined | `surface` | 1 dp `outline_variant` | 0, 1, 0, 0, 3 | separation by border; the lowest emphasis |

Elevation levels are those of [[Elevation]] (0, 1, 3, 6, 8, 12 dp for levels 0 to 5). Values are the Material Web tokens [elevated](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-elevated-card.scss), [filled](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filled-card.scss) and [outlined](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-outlined-card.scss) (`latest`). The Material Components Android guide gives other dragged elevations (8 dp for filled and outlined, 2 dp for elevated); Tesserae follows the Material Web tokens.

| Kind | Use | Differences |
|---|---|---|
| Plain | information, with optional actions | role `group`, not focusable, no state layer |
| Actionable | the whole card opens one subject | one Tab stop, role `button`, state layers, ripple, Enter and Space activate |
| Selectable | the card is chosen among several | actionable plus `selected`: container `secondary_container` (outlined: border `outline`) |
| Draggable | the card is reordered or moved | dragged state; not built, see Behaviour |

## States

State layer colour `on_surface` (all three variants, [Material Web tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filled-card.scss)); opacities hover 8, focus 10, pressed 10, dragged 16 percent ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]], [[State Layers]]). Precedence: dragged, pressed, focused, hovered.

| State | Visual change | Token values |
|---|---|---|
| Rest | variant container | see Variants |
| Hover (actionable) | state layer 8 percent; elevation per Variants (elevated 2, filled 1, outlined 1) | `on_surface` at 0.08 |
| Hover (plain) | none | not applicable |
| Focus (actionable, keyboard) | state layer 10 percent; ring 3 dp, 2 dp offset, `secondary`; outlined border becomes `on_surface` | [[Focus Ring]] |
| Pressed | state layer 10 percent; ripple; elevation back to the rest level | `on_surface` at 0.10 |
| Dragged | state layer 16 percent; elevation level 4 (elevated) or 3 (filled, outlined) | `on_surface` at 0.16 |
| Selected | container `secondary_container` (elevated, filled); border `outline` (outlined) | Tesserae choice, see Deviations |
| Disabled | container at 38 percent opacity (elevated container `surface`, filled `surface_variant`, outlined container `surface` and border `outline` at 12 percent); content `on_surface` at 38 percent; no state layer, no ripple, no focus | [[State Layers]] disabled scheme; tokens `disabled-container-opacity` 0.38, `disabled-outline-opacity` 0.12 |
| Loading | skeleton content is not specified; the card holds a progress indicator in its content slot | not applicable |
| Empty | a card with no content is not drawn; the caller removes it | not applicable |

## Tokens used

| Part | Role or token |
|---|---|
| Container | per Variants; shape `medium` (12 dp) |
| Headline | `title_large`, `on_surface` |
| Subhead | `title_small`, `on_surface_variant` |
| Supporting text | `body_medium`, `on_surface_variant` |
| Icon (in content) | 24 dp, `primary` (Material Web `icon-size` 24 px, `icon-color` `primary`) |
| Outline | 1 dp (`outline-width` 1 px); `outline_variant` at rest |
| Shadow | role `shadow`, level per state |

See [[Colour Roles]], [[Typography]], [[Shape]], [[Elevation]], [[Motion]], [[Spacing and Density]]. The typography roles come from tess-ui; the Material Web card tokens carry no text roles #needs-verification.

## Sizing and density

Card padding and gaps follow the density level ([[ADR-0002 Desktop density levels and target sizes]]). The corner (12 dp), the outline (1 dp) and media corners do not change with density. Values below are Tesserae choices; [[Spacing and Density]] has no card row yet (see Deviations).

| Item | default | compact | dense | MD3 or source value |
|---|---|---|---|---|
| Body padding | 16 | 12 | 8 | 16 (tess-ui; Android sample padding 16 dp) |
| Gap between headline, subhead, text | 4 | 4 | 2 | 4 (tess-ui) |
| Actions row padding top | 8 | 8 | 4 | no MD3 value read |
| Gap between actions | 8 | 8 | 4 | 8 (tess-ui) |
| Action button height | 40 | 32 | 28 | [[Spacing and Density]] |
| Media height (default) | 160 | 120 | 96 | 160 (tess-ui `Media_Height`) |

- Minimum width: 120 dp (the wrapping minimum of [[10 Layout Overflow and Scrolling]]). Maximum width: none; the parent decides. Height: the content height; a card never has a fixed height unless the caller sets one, and then it scrolls its content per Layout and overflow.
- Hit area: an actionable card's hit area is the whole container (at least 24 by 24 dp at every level; 48 by 48 dp in a touch context).
- Margin between cards in a collection: `space.4` (8 dp) at compact and dense, `space.5` (16 dp) at default. Android advises 8 dp margins on mobile ([Card guide](https://github.com/material-components/material-components-android/blob/master/docs/components/Card.md)).

## Layout and overflow

- The container clips its children to the 12 dp corner, so media and the state layer follow the shape ([[Shape]]).
- Headline: wraps to at most two lines, then ends with an ellipsis; subhead: one line, ellipsis; supporting text: wraps without a line limit. The accessible name stays the full headline ([[10 Layout Overflow and Scrolling]], AC-LAY-13).
- Vertical centring: not applicable to multi-line text; the media top edge is flush with the container top, the body starts after it.
- A card taller than its parent's viewport scrolls with its parent ([[Scrollbar and Scroll Container]], [[ADR-0003 Scrollbar rule]]); a card never has its own scrollbar unless the caller gives its content slot a scroll container.
- Actions that do not fit on one row wrap to a second row; none is clipped.
- Space runs out: below 120 dp the parent switches the layout (one column) rather than squeezing the card.

## Behaviour

- Pointer: an actionable card activates on release inside it; the hover state layer and the lift show on enter; a press on a plain card does nothing. A press on a button inside a plain card runs that button only.
- Keyboard: a plain card takes no focus; its buttons take Tab stops in reading order. An actionable card is one Tab stop; Enter and Space activate it; Shift+Tab leaves it. A selectable card toggles `selected` with Space and activates with Enter (the caller decides what `selected` means).
- Touch: same as pointer; the hit area is 48 by 48 dp at least in a touch context.
- Drag and swipe: MD3 draws a dragged state and supports swipe to dismiss ([Android guide](https://github.com/material-components/material-components-android/blob/master/docs/components/Card.md), draggable and swipe sections). Tesserae specifies the dragged state (state layer 16 percent, elevation as in Variants) for a card the caller makes draggable; a draggable card also offers the same move by keyboard (a Move action reachable from the keyboard) because pointer drag alone fails WCAG 2.2 SC 2.5.7 Dragging Movements.

## Tooltip and overlay behaviour

A card shows no tooltip of its own: the control is the card only when it is actionable, and then its headline is its visible name. A truncated headline shows a tooltip with the full text on the headline node, not on the card ([[ADR-0004 Tooltip rule]], AC-LAY-5). Buttons and icon buttons in the card carry their own tooltips ([[Button]], [[Icon Button]]). A card opens a [[Dialog]] or a screen when activated; focus returns to the card when that closes.

## Motion

Background and border colour: 150 ms (`short3`, `standard`); elevation: 200 ms (`short4`, `standard`) ([[Motion]], tess-ui transitions Elevation 200, Background 150). Ripple on press ([[State Layers]]). With reduced motion on, the end state is drawn on the next frame. A drag moves the card with the pointer with no easing.

## Accessibility

- Role: plain `group` named by the headline; actionable `button` named by the headline (supporting text as description); selectable adds `selected`. A collection of cards sits in a `list` with each card as `listitem` when the order matters.
- Name: the visible headline; when absent, the first non-empty text; a media-only card needs an explicit label (a picture alone is not a name).
- Images in media carry a text alternative or are marked decorative ([[Accessibility Rules]] AR-5).
- Keys: see Behaviour. Announcement: role, name and, for selectable, the selected state.
- Contrast: `on_surface` and `on_surface_variant` on each container at least 4.5:1 in light and dark ([[Colour Roles]]); the focus ring at least 3:1 against the surface. An actionable outlined card draws its border in `outline_variant`, which measures below 3:1 against `surface` ([[Colour Roles]]); the identity of the control is carried by the ring on focus and the state layer on hover, so a reviewer checks WCAG 2.2 SC 1.4.11 for the actionable outlined case (AC-CRD-14).
- Targets: see Sizing and density.

## Dark and light

All colours are roles and follow the theme ([[Theme Following the System]], [[ADR-0005 Theme follows the system]]). Elevation shadows are the same geometry in both; the tonal container (`surface_container_low`, `surface_container_highest`) carries the separation in dark. The media is theme-independent.

## Defaults

| Setting | Default |
|---|---|
| Variant | elevated |
| Kind | plain |
| Corner | 12 dp |
| Density | the project's level (padding 16, 12 or 8) |
| Media height | 160 dp at default density |
| Selected, disabled | off |

## Acceptance criteria

- [ ] AC-CRD-1 (token test): the variants resolve to container `surface_container_low` (elevated), `surface_container_highest` (filled), `surface` (outlined), corner 12 dp for all three, outline 1 dp `outline_variant` for outlined only, rest elevation level 1, 0, 0. Pass: exact equality of role names and values.
- [ ] AC-CRD-2 (token test): elevation by state: elevated 1, 2, 1, 1, 4; filled and outlined 0, 1, 0, 0, 3 for rest, hover, focus, pressed, dragged, on an actionable card; a plain card stays at its rest level on hover. Pass: 15 of 15.
- [ ] AC-CRD-3 (pixel check): on an actionable card the state layer over the container equals `on_surface` blended at 0.08 on hover, 0.10 with keyboard focus, 0.10 pressed, 0.16 dragged (within 1 level per channel); a plain card shows none.
- [ ] AC-CRD-4 (token test): headline `title_large` `on_surface`, subhead `title_small` `on_surface_variant`, supporting text `body_medium` `on_surface_variant`.
- [ ] AC-CRD-5 (geometry check): at each density level body padding is 16, 12, 8 dp, the gap between headline, subhead and text is 4, 4, 2 dp, the gap between actions is 8, 8, 4 dp (scale factors 1.0 and 2.0).
- [ ] AC-CRD-6 (geometry check): media is flush with the top, left and right container edges, has the set height (default 160, 120, 96 dp) and no ink lies outside the 12 dp corner.
- [ ] AC-CRD-7 (layout test): a headline of 100 characters in a 200 dp wide card wraps to two lines and ends with `…`; the accessible name is the full headline; a card narrower than 120 dp is refused or switches layout.
- [ ] AC-CRD-8 (scripted input): an actionable card is exactly one Tab stop; Enter and Space each fire its handler once; a plain card has no Tab stop; a disabled actionable card has no Tab stop and fires nothing on click, Enter or Space.
- [ ] AC-CRD-9 (scripted input): a selectable card toggles `selected` on Space and the container changes to `secondary_container` (outlined: border `outline`) within one frame; the handler receives the new value.
- [ ] AC-CRD-10 (AT tree assertion): a plain card has role `group`; an actionable card role `button`; both are named by the headline; a selectable card reports `selected`; a media-only card without a label is reported as a failure.
- [ ] AC-CRD-11 (contrast script): `on_surface` and `on_surface_variant` on each of the three containers at least 4.5:1 in light and dark; the focus ring at least 3:1 against the card's surrounding surface.
- [ ] AC-CRD-12 (token test): the disabled state draws the container at 0.38 opacity (outlined: border `outline` at 0.12), content `on_surface` at 0.38, no state layer.
- [ ] AC-CRD-13 (scripted frame capture): an elevation change completes between 200 ms and 233 ms after hover at 60 Hz; a colour change between 150 ms and 183 ms; with reduced motion on both are complete on the next frame.
- [ ] AC-CRD-14 (review): an actionable outlined card is identifiable without the border colour alone (ring on focus, state layer on hover, name and role); a reviewer confirms WCAG 2.2 SC 1.4.11 is met or the border uses `outline`.
- [ ] AC-CRD-15 (scripted input): a draggable card shows the dragged state on drag start (state layer 0.16, elevation per Variants) and offers a keyboard move action; pass: the same move completes with no pointer.
- [ ] AC-CRD-16 (scripted input): an actionable card does not contain a focusable descendant; a build with a Button inside an actionable card is reported (lint).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Card_View.tdl`, `tess-ui:src/tess_ui/views/Card_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/structural.py` (`card`), `tess-ui:docs/components/cards.md`, tests `tess-ui:tests/test_card.py` | Partly meets. Meets AC-CRD-1 (three variants, 12 px corners, tested), AC-CRD-4 (types set in the view), AC-CRD-6 (media clipped, 160 px), AC-CRD-8 and AC-CRD-10 in part (plain `group`, actionable `button`, selected reported, tested; selectable Space not verified). Elevated hover lift to 2 for actionable only: AC-CRD-2 fails for filled and outlined (no hover elevation 1) and for focus and pressed (not tested), and no dragged elevation. Padding 16 and gap 4 are fixed: AC-CRD-5 fails at compact and dense. Selected uses `secondary_container`; disabled is "dimmed", values not verified against AC-CRD-12. No dragged state, no drag, no swipe: AC-CRD-15 fails (stated "not built" in the docs). Transitions are literals 150 and 200 ms equal to `short3` and `short4` (`AC-MOT-6` allow-list). Not used by any app or example |
| tess-shell | none | Absent. The shell draws no card; its tooltip card and Volume OSD card are Panel content ([[Volume OSD]]) |
| tre | none | Not applicable: the engine has no card node; a card is a `box` with `corner_radius`, `fill` and `shadow` properties |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Padding, gaps and media height scale with the three density levels | desktop information density; MD3 gives one touch size | [[ADR-0002 Desktop density levels and target sizes]] |
| Selected container `secondary_container` (outlined: border `outline`) | MD3 defines a checkable card in Android (checked icon) but the Material Web card tokens have no selected state; Tesserae uses the tonal selected pattern of other components #needs-verification | [[Deviations from MD3]] |
| Draggable card must also be movable by keyboard | WCAG 2.2 SC 2.5.7 Dragging Movements; MD3 shows only the pointer drag | [[Accessibility Rules]] |
| Hover on a plain card has no feedback | a card that cannot be pressed must not look pressable; MD3 tokens define hover for an interactive card | [[Deviations from MD3]] |
| Dragged elevation taken from Material Web tokens, not from the Android guide | the sources differ; one value is testable | [[Deviations from MD3]] |

## Sources

- Material Web card tokens (container colours `surface-container-low`, `surface-container-highest`, `surface`; shape `corner-medium`; elevations rest, hover, focus, pressed, dragged; disabled opacities 0.38 and 0.12; outline 1 px `outline-variant`; icon 24 px `primary`; state layers `on-surface`), verified 2026-11-21: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-elevated-card.scss, `_md-comp-filled-card.scss`, `_md-comp-outlined-card.scss` (same folder).
- Material Components Android Card guide (three types, checkable, draggable with accessibility delegate, swipe to dismiss, 8 dp margin advice, 16 dp padding in the sample): https://github.com/material-components/material-components-android/blob/master/docs/components/Card.md
- Compose Material 3 card, for cross-reference only: https://developer.android.com/develop/ui/compose/components/card
- WCAG 2.2 SC 2.5.7 Dragging Movements: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html; SC 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- tess-ui card documentation: `tess-ui:docs/components/cards.md`, `tess-ui:COMPONENT_LIST.md` (Cards).
- Not verified: the MD3 specification page (https://m3.material.io/components/cards/specs is a script-rendered app); card headline and subhead type roles #needs-verification; selected-card styling #needs-verification.
