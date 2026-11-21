---
title: Navigation Drawer
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, navigation, drawer, modal, landmark]
related: ["[[Navigation Rail]]", "[[Side Sheet]]", "[[Scrim]]", "[[Dialog]]", "[[List]]", "[[List Item]]", "[[Tree]]", "[[Divider]]", "[[Badge]]", "[[Icon Button]]", "[[Top App Bar]]", "[[Routed View]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Scrim]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
---

# Navigation Drawer

> [!info] Summary
> A navigation drawer is a vertical list of destinations (icon, label, optional badge), grouped by headings and dividers: standard (permanent, beside the content) or modal (over the content on a scrim, from the start edge). Material Design 3 counterpart: [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview). Source of truth in code: see Status in code. No app or example uses it today.

## Purpose

Show every top-level destination of an application at once, with names, so the user knows where they are and can go anywhere in one step.

## When to use and not

- Use when: an app has more than seven top-level destinations, or destinations need section headings and long labels; the window is large enough to keep a permanent column (standard), or the window is compact and the destinations open on demand (modal).
- Do not use when: there are three to seven destinations and the window is medium or expanded ([[Navigation Rail]]); the content is supporting detail ([[Side Sheet]]); the choices are commands ([[Menu]]); the hierarchy is deep and user-built ([[Tree]]); the items are data rows ([[List]]).
- A drawer holds destinations, not actions: pressing a destination changes where the user is. Actions go in the header or footer slot as [[Button]] or [[Icon Button]] instances.
- Only one navigation region is shown at a time: a drawer and a rail are not shown together ([[Navigation Rail]] rule 3 below).

## Anatomy

1. Scrim (modal only): the whole window ([[Scrim]]).
2. Container: a full-height column.
3. Header slot (optional): a title, an account, a search field.
4. Section heading (optional): `title_small`, `on_surface_variant`.
5. Divider (optional): 1 dp, `outline`.
6. Destination (several): active indicator pill, icon 24 dp, label, optional badge at the end.
7. Footer slot (optional).
8. Scrollbar thumb on the destination column when it overflows.
9. State layer and focus ring on the focused or hovered destination.

## Variants

| Variant | Container | Elevation | Shape | Scrim | Layout effect |
|---|---|---|---|---|---|
| Standard | `surface` | level 0 | `none` at the content edge | none | inline; takes its width from the content while open |
| Modal | `surface_container_low` | level 1 | `large` (16 dp) on the end corners (`corner-large-end`) | `scrim` at 0.32 | over the content; takes no room |

Material Web [navigation-drawer tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-drawer.scss): container width 360 px, active indicator 336 by 56 px (the indicator is inset 12 px each side), indicator shape `corner-full`, standard container `surface` level 0, modal container `surface-container-low` level 1, container shape `corner-large-end`, bottom container shape `corner-large-top`, headline `title-small` in `on-surface-variant`, label `label-large`, icon 24 px, divider `outline`.

## States

State layer colour and content colours follow the Material Web tokens (above): active destination `on_secondary_container`; inactive destination content `on_surface_variant`, and `on_surface` on hover, focus and pressed (state layer `on_surface`, pressed layer `on_secondary_container`). Opacities: hover 8, focus 10, pressed 10 percent ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]], [[State Layers]]).

| State | Visual change | Token values |
|---|---|---|
| Rest, inactive | transparent pill; icon and label `on_surface_variant` | roles |
| Rest, active (selected) | pill `secondary_container`; icon and label `on_secondary_container`; label weight prominent (700) | `active-indicator-color`, `active-label-text-weight` |
| Hover | state layer 8 percent over the pill; inactive content `on_surface` | `on_surface` at 0.08 |
| Focus (keyboard) | state layer 10 percent; ring 3 dp, 2 dp offset, `secondary` (drawn inside the destination: inward offset, because the pill is inset 12 dp from the container edge) | [[Focus Ring]] |
| Pressed | state layer 10 percent; ripple | pressed layer `on_secondary_container` at 0.10 |
| Disabled | icon, label, badge `on_surface` at 38 percent; no state layer, no focus, no press | [[State Layers]] |
| Closed | standard: zero width, not in the focus order; modal: no layer | not applicable |
| Empty | a drawer with no destination is not drawn | not applicable |
| Loading | destinations appear when they are known; the header stays | not applicable |

## Tokens used

| Part | Role or token |
|---|---|
| Container | per Variants |
| Section heading | `title_small`, `on_surface_variant` |
| Destination label | `label_large`; `on_surface_variant` inactive, `on_secondary_container` active |
| Destination icon | 24 dp; same colours as the label |
| Active indicator | `secondary_container`, shape `full` (pill) |
| Badge | `label_large`, `on_surface_variant` inactive, `on_secondary_container` active |
| Divider | 1 dp, `outline` |
| Scrim | `scrim` at 0.32 |

See [[Colour Roles]], [[Typography]], [[Shape]], [[Elevation]], [[Motion]], [[Spacing and Density]].

## Sizing and density

Destination height, paddings and gaps follow the density level ([[ADR-0002 Desktop density levels and target sizes]]). Values are Tesserae choices; default equals MD3 where MD3 gives a value (the 56 dp pill, the 24 dp icon, the 12 dp inset). [[Spacing and Density]] has no drawer row yet (see Deviations).

| Item | default | compact | dense | MD3 or source value |
|---|---|---|---|---|
| Destination (pill) height | 56 | 40 | 32 | 56 (`active-indicator-height`) |
| Panel inset (container edge to pill) | 12 | 8 | 4 | 12 (336 of 360 px indicator; tess-ui 12) |
| Pill padding start | 16 | 12 | 8 | 16 (tess-ui) |
| Pill padding end | 24 | 16 | 8 | 24 (tess-ui) |
| Icon size | 24 | 20 | 20 | 24 (`icon-size`) |
| Icon-to-label gap | 12 | 8 | 4 | 12 (tess-ui); 8, 8, 4 in [[Spacing and Density]] for lists |
| Section heading row height | 56 | 40 | 32 | tess-ui 18 plus 20 plus 18 |
| Heading padding start | 16 | 12 | 8 | 16 (tess-ui) |
| Divider margin (above and below) | 8 | 4 | 4 | not read from a source |
| Width (default) | 360 | 280 | 256 | 360 (`container-width`) |

- Width range: 256 to 360 dp at every density (tess-ui); the indicator width is the container width minus twice the inset.
- Hit area: the full pill (at least 24 dp high at every level; the smallest pill is 32 dp); in a touch context the hit area grows to 48 dp high and the painted pill does not.
- The pill corner is `full` (half its height) at every density.

## Window size class behaviour

Size classes are defined in [[Spacing and Density]] (compact below 600 dp, medium 600 to 839, expanded 840 to 1199, large 1200 to 1599, extra-large 1600 and up); the pane rules are in [[10 Layout Overflow and Scrolling]]. A boundary value belongs to the larger class. Density is independent of the class.

| Width class | Navigation region | Drawer |
|---|---|---|
| compact (below 600) | none permanent; a menu button in the [[Top App Bar]] opens the drawer | modal only |
| medium (600 to 839) | a collapsed [[Navigation Rail]]; the drawer is optional, opened from the rail's menu button | modal only |
| expanded (840 to 1199) | a collapsed rail or a standard drawer, chosen by the project | standard or modal |
| large (1200 to 1599) | a standard drawer by default; a rail is allowed | standard |
| extra-large (1600 and up) | as large; extra width goes to the content pane | standard |

Rules:
1. A standard drawer is shown only where the content pane keeps at least 320 dp ([[10 Layout Overflow and Scrolling]]): window width minus drawer width at least 320 dp. With the default 360 dp drawer this holds from 680 dp; with the dense 256 dp drawer from 576 dp. The class table and this rule both hold; where either fails, the drawer is modal.
2. The class is re-evaluated on each resize. An open standard drawer that no longer fits becomes closed and its opener appears; a modal drawer that is open when the window grows stays modal until it is closed.
3. A rail and a standard drawer are never shown together; a window that switches from one to the other keeps the selected destination and moves focus only if focus was inside the region that left (to the same destination in the other region).
4. The collapse of a standard drawer to a rail is the caller's setting; tess-ui does not switch by itself (see Status in code).

## Dimensions and defaults

Values agree with Sizing and density above; compact and dense values are Tesserae choices #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | N/A: a full-height column, the height is the region height | N/A: same as the default level | N/A: same as the default level | [[Navigation Drawer]] Anatomy | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | min width | - | 256 | 256 | 256 | tess-ui:src/tess_ui/views/NavigationDrawer_Stylesheet.tdl (range 256 to 360); container width 360 default, 280 compact, 256 dense, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| container | padding | - | N/A: the pill inset is the destination margin; the column adds no padding of its own | N/A: same as the default level | N/A: same as the default level | [[Navigation Drawer]] Sizing and density | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container | margin | - | N/A: the content region sets the outer space | N/A: same as the default level | N/A: same as the default level | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| container | gap | - | N/A: destinations stack edge to edge; each pill carries its own height | N/A: same as the default level | N/A: same as the default level | [[Navigation Drawer]] Sizing and density | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| container | border width | - | 0 | 0 | 0 | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-drawer.scss | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| container | border color | - | N/A: the container draws no border; the standard drawer meets the content at a change of colour | N/A: same as the default level | N/A: same as the default level | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-drawer.scss | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container, standard | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| container, modal | corner radius | `shape.large` | 16 | 16 | 16 | [[Shape]], end corners only | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| container, standard | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| container, modal | elevation | `elevation.level1` | 1 | 1 | 1 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| destination | height | - | 56 | 40 | 32 | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-drawer.scss, design choice, proposed ADR: navigation region sizes per density | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| destination | min height | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| destination | padding | - | 0 24 0 16 | 0 16 0 12 | 0 8 0 8 | tess-ui:src/tess_ui/views/NavigationDrawerItem_Stylesheet.tdl, design choice, proposed ADR: navigation region sizes per density | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| destination | margin | `space.4`, `space.3`, `space.2` | 0 12 0 12 | 0 8 0 8 | 0 4 0 4 | tess-ui:src/tess_ui/views/NavigationDrawerPanel_Stylesheet.tdl (12), design choice, proposed ADR: navigation region sizes per density | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| destination | gap | `density.icon_label_gap` | 12 | 8 | 4 | tess-ui (12), [[Spacing and Density]] (8, 8, 4 for lists), design choice, proposed ADR: navigation region sizes per density | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| destination | corner radius | `shape.full` | 28 | 20 | 16 | [[Shape]] (half the height) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| destination | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| destination | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Iconography]], [[Spacing and Density]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| destination | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| section heading | height | - | 56 | 40 | 32 | tess-ui (18 plus 20 plus 18), design choice, proposed ADR: navigation region sizes per density, [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| section heading | padding | - | 0 0 0 16 | 0 0 0 12 | 0 0 0 8 | tess-ui (16), design choice, proposed ADR: navigation region sizes per density, [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| section heading | font | `title_small` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| divider | height | - | 1 | 1 | 1 | [[Divider]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| divider | margin | `space.3`, `space.2` | 8 0 8 0 | 4 0 4 0 | 4 0 4 0 | design choice, proposed ADR: navigation region sizes per density, [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| divider | border color | `outline` | `outline` | `outline` | `outline` | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-drawer.scss | tess-ui: yes (style background); tess-shell: n/a: element absent in tess-shell; tre: yes (background) |

## Layout and overflow

- The destination column scrolls vertically when destinations do not fit, with a visible scrollbar thumb ([[ADR-0003 Scrollbar rule]]); the header and the footer slot stay fixed. A focused destination scrolls into view with its ring visible (AC-LAY-14).
- Labels are one line with an end ellipsis; the badge is never truncated and keeps its width; the label shrinks first ([[10 Layout Overflow and Scrolling]], AC-LAY-6). The full label is the accessible name and the tooltip text. Vertically centred: the icon, label and badge are centred in the pill height (space above and below differ by at most 1 px, AC-LAY-2).
- Section headings are one line with ellipsis; a heading is not focusable and not a link.
- The drawer is full height of its region; a modal drawer is never taller than the window.
- Space runs out: below 256 dp the drawer is not allowed (the width is clamped).

## Behaviour

- Pointer: a press on a destination chooses it; a press on the scrim closes a modal drawer and is consumed ([[Scrim]] rule 4); a press inside the drawer never closes it except on a destination. Hover shows the state layer.
- Keyboard, destinations: the destination list is one Tab stop; focus enters on the selected destination, else the first enabled one. Up and Down Arrow move focus to the previous and next enabled destination (no wrap; headings, dividers and disabled destinations are skipped); Home and End move to the first and last. Enter and Space choose the focused destination. Selection does not follow focus: moving focus never changes the screen. Tab leaves the list to the next control (footer, then main content); Shift+Tab goes back to the header controls.
- Keyboard, modal: on open, focus moves to the selected destination (else the first enabled one). Tab and Shift+Tab cycle inside the drawer only. Escape closes a dismissible drawer and returns focus to the control that opened it. Choosing a destination chooses it, closes the drawer, then focus returns to the opener and the routed view may move focus into the new screen ([[Routed View]]). A modal drawer that is not dismissible still closes on a destination.
- Standard drawer toggle: the opener button reports `expanded`; closing the drawer while focus is inside moves focus to the opener.
- Touch: a swipe from the start edge opens a modal drawer and a swipe toward the edge closes it (MD3); the same actions are reachable by button and keyboard; hit areas are 48 dp high in a touch context.
- A modal drawer closes any open [[Popup]] and removes any tooltip when it opens ([[12 Overlays]]).

## Tooltip and overlay behaviour

A destination shows a plain tooltip only when its label is truncated: the tooltip carries the full label and its trigger is the destination (the control), after 500 ms of hover or at once on keyboard focus, with a 150 ms grace over the pointer move onto it ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]], [[Tooltip]]). Headings and dividers have none. The modal drawer is a modal layer: one scrim under the topmost modal, above every non-modal overlay ([[12 Overlays]], [[Scrim]]); a [[Dialog]] opened from it closes it first. A standard drawer is page layout, not a layer, and draws no scrim.

## Motion

- Standard: the width eases between 0 and its value in 250 ms (`medium1`) with `standard` easing (tess-ui `Transition { Width: 250 }`); content keeps its final width and is clipped while the width changes.
- Modal: the scrim fades in 500 ms and out 150 ms, linear ([[Scrim]]); the drawer slides in from the start edge over 400 ms (`medium4`) with `emphasized_decelerate` and out over 200 ms (`short4`) with `emphasized_accelerate` (Tesserae choice; MD3 slide durations are not published as tokens #needs-verification).
- Destination selection: the pill colour changes in 150 ms (`short3`, `standard`).
- Reduced motion: every change above completes on the next frame ([[Motion]] rule 4).

## Accessibility

- Role: the destination list is a landmark `navigation` named "Navigation" (or the app's label); each destination is a `link` named by its label with `current` set to `page` when it is the destination of the screen showing (`true` or `location` for non-page destinations). A modal drawer's layer is a `dialog` named "Navigation" that contains the `navigation`. A heading is a `heading` (or a labelled group) and a divider a `separator`. tre has no `navigation` role: the engine's `group` named "Navigation" stands in until it does (candidate request in the summary).
- Name: the visible label (AR-3); a badge is read as part of the name ("Inbox, 24"); the heading text names its group.
- Keys: see Behaviour. A visible control reaches every drawer action (open button, close).
- Modal: content beneath is inert while open #needs-verification (engine tree); Escape and the scrim are the exit (WCAG 2.2 SC 2.1.2).
- Contrast: `on_surface_variant` on `surface` and on `surface_container_low`, `on_secondary_container` on `secondary_container`, `on_surface_variant` on `surface_container_low` each at least 4.5:1 in light and dark; the pill against the surface needs no 3:1 because the label carries the state; the ring 3:1 ([[Colour Roles]]).
- Announcement: choosing a destination announces the new page through the routed view; opening a modal drawer announces role and name.

## Dark and light

All colours are roles and follow the theme ([[Theme Following the System]]). The standard drawer is `surface` in both; the modal drawer `surface_container_low` with level 1 shadow is lighter than `surface` in dark. The scrim is `scrim` at 0.32 in both. A frosted variant exists in tess-ui (the container at 72 percent with a 20 dp backdrop blur); it is a project effect, not a MD3 surface, and it changes no contrast rule: the text contrast is measured against the worst content blurred beneath.

## Defaults

| Setting | Default |
|---|---|
| Form | standard where the window is large and the pane rule holds, else modal |
| Width | 360 dp (256 to 360) at default density |
| Open state | standard: open; modal: closed |
| Destination height | 56 dp at default, 40 compact, 32 dense |
| Dismissible (modal) | yes (Escape, scrim press) |
| Scrim | `scrim` at 0.32 |
| Selection follows focus | no |

## Acceptance criteria

- [ ] AC-NDR-1 (token test): standard container `surface`, level 0; modal container `surface_container_low`, level 1, corner 16 dp on the end corners and 0 on the others; active indicator `secondary_container` with half-height corners.
- [ ] AC-NDR-2 (token test): destination label `label_large`, icon 24 dp (20 at compact and dense); inactive colours `on_surface_variant`, active `on_secondary_container` (icon, label, badge); active label weight 700; heading `title_small` in `on_surface_variant`; divider 1 dp `outline`.
- [ ] AC-NDR-3 (geometry check): at each density a destination pill is 56, 40, 32 dp high, the pill is inset 12, 8, 4 dp from the container edge (width 336 in a 360 dp container at default), padding start 16, 12, 8 and end 24, 16, 8, icon-to-label gap 12, 8, 4 (scale factors 1.0 and 2.0).
- [ ] AC-NDR-4 (token test): width requests of 100, 300, 900 dp give 256, 300, 360 dp.
- [ ] AC-NDR-5 (geometry check): at window widths 599, 600, 679, 680, 839, 840, 1199, 1200 dp with a 360 dp drawer and a default project policy, a standard drawer is shown only where the class table allows it and window width minus drawer width is at least 320 dp; elsewhere the drawer is modal.
- [ ] AC-NDR-6 (geometry check): resizing across 680 dp with a standard drawer open closes it and shows its opener in the same frame; no frame has the content pane below 320 dp.
- [ ] AC-NDR-7 (scripted input): focus enters the destination list on the selected destination; Down x3 moves focus three enabled destinations, skipping headings, dividers and disabled ones; Up returns; Home and End reach the first and last; no wrap; the selected destination does not change while focus moves; Enter and Space each choose the focused destination once.
- [ ] AC-NDR-8 (scripted input): from the control before the drawer, Tab lands in the list once and a second Tab leaves it; Shift+Tab returns to the last focused destination.
- [ ] AC-NDR-9 (scripted input): modal open moves focus to the selected destination within one frame; Tab x30 and Shift+Tab x30 keep focus inside the drawer (60 of 60); Escape closes it and focus is on the opener within one frame; a press on the scrim closes it and the control under the press receives no event; a press inside does not close it.
- [ ] AC-NDR-10 (scripted input): choosing a destination in the modal drawer writes the choice once, closes the drawer, and focus is on the opener; a non-dismissible drawer ignores Escape and the scrim but closes on a destination.
- [ ] AC-NDR-11 (pixel check): while a modal drawer is open, a window pixel outside the drawer equals the underlying pixel blended with `scrim` at 0.32 (within 1 level per channel) at the four window corners; a standard drawer draws no scrim.
- [ ] AC-NDR-12 (AT tree assertion): the list has role `navigation` (or `group` where the engine lacks it) with a non-empty name; each destination has role `link`, its label as name, and `current` page on the selected one only; a modal drawer's layer has role `dialog`; headings are `heading` and dividers `separator`.
- [ ] AC-NDR-13 (geometry check): a label of 80 characters in a 256 dp drawer shows one line ending in `…`, the badge keeps its full width, the accessible name is the full label, and hover for 500 ms shows a tooltip whose trigger is the destination; a short label shows no tooltip.
- [ ] AC-NDR-14 (scripted input): 30 destinations in a 400 dp high drawer scroll with a visible thumb; the header and footer stay fixed; focusing the last destination by keyboard scrolls it fully into view with its ring.
- [ ] AC-NDR-15 (token test): state layers on a destination: hover 0.08, focus 0.10, pressed 0.10; a disabled destination shows none and is skipped by Tab and the arrows.
- [ ] AC-NDR-16 (pixel check): standard width reaches target 250 ms to 283 ms after the toggle at 60 Hz; scrim 0.32 reached 500 to 533 ms after a modal open and 0 at 150 to 183 ms after close; with reduced motion all end states appear on the next frame.
- [ ] AC-NDR-17 (contrast script): the five pairs listed under Accessibility measure at least 4.5:1 in light and dark; the focus ring at least 3:1 against `secondary_container` and against the drawer container.
- [ ] AC-NDR-18 (scripted input): opening a modal drawer closes an open popup and removes a visible tooltip within one frame; the opener reports `expanded` equal to the drawer state.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/NavigationDrawer_View.tdl`, `NavigationDrawerModal_View.tdl`, `NavigationDrawerPanel_View.tdl`, `NavigationDrawerItem_View.tdl`, `NavigationDrawerScreens_View.tdl` and the matching `_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py` (`navigation_drawer`), `tess-ui:docs/components/navigation-drawer.md`, tests `tess-ui:tests/test_navigation_drawer.py` | Partly meets. Meets AC-NDR-1 (standard `surface`; modal `surface_container_low`, level 1, 16 px corners on the right, tested), AC-NDR-2 in part (56 px pill, 24 px icon, 28 px corners, `label_large`, selected `secondary_container`, tested; heading `title_small`; label weight is not prominent when active), AC-NDR-4 (width held 256 to 360, tested), AC-NDR-9 and AC-NDR-10 in part (modal layer: Escape, scrim press, Tab inside, focus return; a destination closes it, tested), AC-NDR-12 in part (destinations are `link` with `current` page, tested; list is `group` named Navigation; modal layer is `dialog` named Navigation; no `navigation` role in the engine), AC-NDR-14 (a long list scrolls, tested). Fails AC-NDR-3 (no density levels: 56 px at every setting), AC-NDR-5 and AC-NDR-6 (no size-class switching or collapse to a rail; the caller chooses), AC-NDR-7 (arrow keys move focus and also choose the destination: `On_Focus_Enter` writes `Selected`; no Home and End, not verified), AC-NDR-11 (scrim is a baked-in colour, AC-SCR-3 fails), AC-NDR-16 (the modal drawer does not slide in, stated "not built"), AC-NDR-18 (opener `expanded` not set). Frosted variant is a tess-ui addition. Not used by any app or example |
| tess-shell | none | Absent. The shell has no navigation drawer; its destinations are Workspaces ([[Workspaces Module]]) and the Launcher ([[Popup]]); a drawer would be a Panel with exclusive keyboard (not a promise) |
| tre | `tre:docs/reference/layers.md`, `tre:docs/reference/node.md` | Mechanism only: modal layer with blocked input, first-focusable focus, Tab inside, `dismiss` on outside press and Escape, no scrim, no slide; `current` state exists; roles `navigation`, `complementary`, `region` do not exist |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Destination height, paddings and width per density level (56, 40, 32 dp) | desktop information density; MD3 gives the 56 dp touch size | [[ADR-0002 Desktop density levels and target sizes]] |
| Scrim 0.32 for the modal drawer; the Material Web drawer token is 0.4 with colour `neutral-variant20` | one scrim value and role for every modal surface | [[Scrim]] |
| Selection does not follow focus; Enter or Space chooses | a screen change per arrow press is disruptive; WAI-ARIA APG tabs allow selection to follow focus only when the panel loads instantly | [[14 Accessibility Basics]] |
| Standard and modal choice follows window size class and the 320 dp pane minimum | desktop layout chapter; MD3 and Android advise standard on tablet and desktop, modal on mobile | [[10 Layout Overflow and Scrolling]] |
| Home, End, Arrow keys and Escape specified | desktop keyboard-first use; MD3 documents no keyboard model (Android advises an Escape handler) | [[14 Accessibility Basics]] |
| Modal drawer swipe and edge gestures also reachable by keyboard | WCAG 2.2 SC 2.5.7 | [[Accessibility Rules]] |
| Frosted variant (72 percent container, 20 dp blur) | tess-ui effect; not an MD3 surface; kept as a named project effect | [[Deviations from MD3]] |
| Slide timings (400 ms in, 200 ms out) | not published as tokens; Tesserae choice | [[Deviations from MD3]] |

## Sources

- Material Web navigation drawer tokens (container width 360 px, indicator 336 by 56 px, `corner-full` indicator, standard `surface` level 0, modal `surface-container-low` level 1, `corner-large-end`, headline `title-small` `on-surface-variant`, label `label-large`, icon 24 px, divider `outline`, active and inactive colours, hover 8, focus 10, pressed 10 percent, drawer scrim opacity 0.4), verified 2026-11-21: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-drawer.scss
- Material Components Android Navigation Drawer guide (standard on tablet and desktop, modal blocks interaction with a scrim, Escape handler advice, 48 dp open and close targets, item icon 24 dp, corner 16 dp): https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationDrawer.md
- WAI-ARIA APG navigation landmark and landmark regions (links, current page, unique labels): https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/navigation.html, https://www.w3.org/WAI/ARIA/apg/practices/landmark-regions/
- APG modal dialog pattern: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- WCAG 2.2 SC 2.1.2 No Keyboard Trap, SC 2.5.7 Dragging Movements, SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/
- tess-ui documentation: `tess-ui:docs/components/navigation-drawer.md`; window size classes: `tess-ui:src/tess_ui/tokens.py`.
- Not verified: MD3 specification page values (item padding start 16 and end 24, section heading spacing, slide durations) #needs-verification; engine tree inertness under a modal layer #needs-verification.
