---
title: Navigation Rail
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, navigation, rail, landmark]
related: ["[[Navigation Drawer]]", "[[Side Sheet]]", "[[Icon Button]]", "[[Floating Action Button]]", "[[Badge]]", "[[Tooltip]]", "[[Routed View]]", "[[Top App Bar]]", "[[Dock]]", "[[Bar#Variants|Vertical Bar]]", "[[Workspaces Module]]", "[[Frame#Anatomy|Frame Strip]]", "[[Scrollbar and Scroll Container]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# Navigation Rail

> [!info] Summary
> A navigation rail is a narrow column of three to seven top-level destinations at the window edge, each an icon in a pill with a label under it; the expanded form widens it to 220 dp or more with the label beside the icon. Material Design 3 counterpart: [Navigation rail](https://m3.material.io/components/navigation-rail/overview). Source of truth in code: see Status in code. The plain rail is not used by any app; the screens rail is used by two examples.

## Purpose

Switch between the few top-level destinations of an application with one press, keep the current one visible, and use little width.

## When to use and not

- Use when: the app has three to seven top-level destinations of equal importance; the window is medium or wider (see Window size class behaviour); a vertical column beside the content suits the layout.
- Do not use when: there are more than seven destinations or they need section headings ([[Navigation Drawer]]); the window is compact (a modal drawer opens from the [[Top App Bar]]); the items are commands ([[Menu]]); the items switch content inside one view (tabs); the control is a toolbar of tools ([[Icon Button]] in a toolbar).
- The shell's [[Dock]], [[Bar#Variants|Vertical Bar]] and [[Frame#Anatomy|Frame Strip]] are shell surfaces with their own specifications; they are not instances of this element. [[Workspaces Module]] is a shell module that lists workspaces.

## Anatomy

1. Container: a full-height column, `surface`, width 80 dp (collapsed).
2. Header slot (optional): a menu [[Icon Button]] or a [[Floating Action Button]].
3. Destination (3 to 7): icon 24 dp in an active-indicator pill, label under it.
4. Active indicator: the pill, 56 by 32 dp (collapsed), `secondary_container` when the destination is active.
5. Badge (optional): dot or count on the icon ([[Badge]]).
6. Label: `label_medium`.
7. Footer slot (optional).
8. State layer over the pill; focus ring on the focused destination.

Expanded form: the label sits beside the icon inside a 56 dp high pill (anatomy 3 to 6 rearranged).

## Variants

| Variant | Width | Destination layout | Use |
|---|---|---|---|
| Collapsed | 80 dp (96 dp in Expressive, not adopted) | pill 56 by 32 over the label | default; medium windows and up |
| Expanded | 220 dp (220 to 360 in the Material Web token) | pill 56 high, icon and label side by side | wide windows where labels need room; non-modal; replaces the standard drawer for few destinations |
| Screens rail | as collapsed or expanded | destinations are the app's screens | an app with routed screens ([[Routed View]]) |

Destination alignment inside the column: top (default), centre or bottom (Android `menuGravity`, [Navigation rail guide](https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationRail.md)); expanded rails align top.

The expanded rail is a named Expressive adoption ([[ADR-0006 MD3 baseline with named Expressive adoptions]]; the Android guide describes it as an M3 Expressive element that replaces the navigation drawer). Tesserae adopts it as the wider state of the same region: the baseline is the 2022 rail (80 dp, indicator 56 by 32, active label `on_surface`, as in the Material Web `navigation-rail` tokens); the Expressive collapsed width of 96 dp, item height 64 dp and active label colour `secondary` are not adopted.

## States

State layer colour: `on_surface` for hover, focus and pressed of the inactive and active destination, as in the [navigation-rail tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-rail.scss); the indicator pill holds the active destination. Opacities hover 8, focus 10, pressed 10 percent ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]], [[State Layers]]).

| State | Visual change | Token values |
|---|---|---|
| Rest, inactive | transparent pill; icon and label `on_surface_variant` | `inactive-icon-color`, `inactive-label-text-color` |
| Rest, active | pill `secondary_container`; icon `on_secondary_container`; label `on_surface`, weight prominent (700) | `active-indicator-color`, `active-icon-color`, `active-label-text-color` |
| Hover | state layer 8 percent over the pill; inactive icon and label `on_surface` | `on_surface` at 0.08 |
| Focus (keyboard) | state layer 10 percent; ring 3 dp, 2 dp offset, `secondary`, around the whole destination (pill and label) | [[Focus Ring]] |
| Pressed | state layer 10 percent; ripple | `on_surface` at 0.10 |
| Disabled | icon, label, badge `on_surface` at 38 percent; no state layer, no focus, no press | [[State Layers]] |
| Badge | dot 6 dp, count or text in a 16 dp high pill, `error` with `on_error` text (`label_small`) | `badge-size` 6 px, `large-badge-size` 16 px |
| Empty | a rail with no destination is not drawn | not applicable |
| Loading | not applicable: destinations are known at build time | not applicable |

## Tokens used

| Part | Role or token |
|---|---|
| Container | `surface`, level 0, shape `none` |
| Active indicator | `secondary_container`, shape `full` |
| Icon | 24 dp; `on_surface_variant` inactive, `on_secondary_container` active |
| Label | `label_medium` (collapsed), `label_large` (expanded); `on_surface_variant` inactive, `on_surface` active (collapsed) |
| Expanded label (active) | `on_secondary_container` (tess-ui); the Material Web horizontal item tokens carry no colours of their own #needs-verification |
| Badge | `error`, `on_error`; dot 6 dp, large 16 dp |
| Focus ring | `secondary` |

See [[Colour Roles]], [[Typography]], [[Shape]], [[Elevation]], [[Motion]], [[Spacing and Density]].

## Sizing and density

Rail width, pill size and spacing follow the density level ([[ADR-0002 Desktop density levels and target sizes]]). Values are Tesserae choices ([[Spacing and Density]] has no rail row yet; see Deviations).

| Item | default | compact | dense | MD3 or source value |
|---|---|---|---|---|
| Container width (collapsed) | 80 | 72 | 64 | 80 (`container-width`) |
| Pill (collapsed) width by height | 56 by 32 | 48 by 28 | 40 by 24 | 56 by 32 (`active-indicator-width`, `-height`) |
| Icon size | 24 | 20 | 20 | 24 (`icon-size`) |
| Icon-to-label gap (collapsed) | 4 | 4 | 2 | 4 (`item.vertical.icon-label-space`) |
| Destination height (pill plus gap plus label line 16) | 52 | 48 | 42 | derived |
| Gap between destinations | 12 | 8 | 4 | tess-ui 12; MD3 collapsed item vertical space 4 plus 64 dp item (Expressive) |
| Space above the first destination | 44 | 24 | 12 | 44 (`top-space`, tess-ui) |
| Space below the last destination | 56 | 32 | 16 | tess-ui |
| Expanded width | 220 | 220 | 220 | 220 minimum (`container-width-minimum`) |
| Expanded pill height | 56 | 40 | 32 | 56 (`item-horizontal.active-indicator-height`) |
| Expanded pill padding start, end | 16, 24 | 12, 16 | 8, 8 | 16 (token), tess-ui |
| Expanded rail side padding | 20 | 12 | 8 | 20 (tess-ui; Android `expandedMarginHorizontal` 20) |
| Expanded icon-to-label gap | 8 | 8 | 4 | 8 (`item-horizontal.icon-label-space`) |

- The hit area of a destination is its whole box: the rail width by the destination height (at least 64 by 42 dp at the densest); in a touch context the hit area grows to 48 dp in each axis if smaller, without changing the painted size.
- Expanded width range: 220 to 360 dp (Material Web `container-width-maximum` 360 px).
- Destination count: three to seven (tess-ui documentation and MD3 guidance #needs-verification); fewer than three or more than seven is a use-the-drawer signal (AC-NRL-12).

## Window size class behaviour

Size classes are those of [[Spacing and Density]]; pane rules are in [[10 Layout Overflow and Scrolling]]. The full table of the navigation region by class is in [[Navigation Drawer]] (Window size class behaviour); the rail's rows are:

| Width class | Rail |
|---|---|
| compact (below 600) | not shown; destinations open in a modal [[Navigation Drawer]] from a menu button |
| medium (600 to 839) | collapsed rail shown, permanent |
| expanded (840 to 1199) | collapsed rail, or expanded rail if the project chooses it and the content keeps 320 dp |
| large (1200 to 1599), extra-large (1600 and up) | collapsed or expanded rail by project policy; a standard drawer is the alternative |

Rules:
1. A boundary value belongs to the larger class; the class is re-evaluated on each resize.
2. An expanded rail is shown only where the window width minus the rail width keeps the content pane at least 320 dp; otherwise it collapses to the collapsed rail in place.
3. A rail and a standard drawer are never shown together; switching moves the selection to the same destination in the other region and moves focus only if focus was inside the region that left.
4. Collapsing or expanding the rail keeps the selected destination and the focused destination (focus stays on the same item).
5. At compact width the rail is removed from layout and its destinations are reachable from the drawer; no destination becomes unreachable (AC-LAY-1).

## Layout and overflow

- The destination column scrolls vertically when the destinations do not fit the height (a small window height class), with a visible scrollbar thumb inside the rail width ([[ADR-0003 Scrollbar rule]]); the header and footer slots stay fixed. A focused destination scrolls into view with its ring visible (AC-LAY-14). At the compact height class (below 480 dp) the top space reduces to the dense value.
- Collapsed labels are one line, centred under the icon, with an end ellipsis when wider than the rail minus 8 dp on each side; the full label is the accessible name and the tooltip text (a destination is the control). Expanded labels are one line with an end ellipsis; the badge never truncates.
- Vertical centring: in the expanded pill the icon and label are centred in the pill height (space above and below differ by at most 1 px, AC-LAY-2).
- The rail is full height of its region; a rail never overlaps the content.
- Space runs out: the rail never narrows below 64 dp (the dense width).

## Behaviour

- Pointer: a press on a destination chooses it (activation on release inside it); hover shows the state layer; a press on the active destination keeps it active and does nothing else.
- Keyboard: header controls come first in the Tab order, then the destination list as one Tab stop, then footer controls. Focus enters the list on the selected destination (else the first enabled one). Up and Down Arrow move focus to the previous and next enabled destination (no wrap; disabled destinations are skipped); Home and End move to the first and last; Enter and Space choose the focused destination. Selection does not follow focus: moving focus never changes the screen. Tab leaves the list; Shift+Tab returns to the last focused destination.
- Touch: tap chooses; the hit area is 48 dp in each axis at least in a touch context.
- The screens rail follows the screen showing: the selected destination equals the current screen, and choosing a destination navigates to its screen ([[Routed View]]). Focus then moves into the new screen as the routed view specifies; the rail keeps its Tab stop on the selected destination.
- Expand and collapse: the menu button in the header toggles the form where the project offers both; the button reports `expanded`.

## Tooltip and overlay behaviour

A collapsed destination shows its label permanently, so it needs no tooltip; a plain tooltip with the full label appears only when the label is truncated, on the destination (the control) after 500 ms of hover and at once on keyboard focus, with a 150 ms grace ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]], [[Tooltip]]). Header icon buttons carry their tooltips ([[Icon Button]]). The rail opens no overlay; a modal drawer opened from its menu button covers the rail ([[Navigation Drawer]]). The rail is page layout, never a layer, and draws no scrim.

## Motion

- Selection: the pill background changes in 150 ms (`short3`, `standard`). MD3 Expressive lets the pill grow from the icon; Tesserae fades it in (tess-ui) and does not adopt the growth.
- Expand and collapse: width eases in 250 ms (`medium1`, `standard`); labels change layout on the final frame, not mid-way, so no text reflows during the animation.
- Reduced motion: every change completes on the next frame ([[Motion]] rule 4).

## Accessibility

- Role: the rail is a landmark `navigation` named "Navigation" (or the app's label; a second navigation landmark on the page needs a different name, APG); each destination is a `link` named by its label with `current` set to `page` on the destination of the screen showing. The engine has no `navigation` role: `group` named "Navigation" stands in until it does ([[Accessibility Rules]] AR-2; candidate request in the summary).
- Name: the visible label (AR-3). A badge is read after the label ("Inbox, 3 new"); a dot badge is read as "new" #needs-verification.
- Keys: see Behaviour. Every destination is reachable by keyboard (AR-9).
- Contrast: `on_surface_variant` on `surface`, `on_surface` on `surface`, `on_secondary_container` on `secondary_container` each at least 4.5:1 in light and dark; `on_error` on `error` at least 4.5:1; ring 3:1 ([[Colour Roles]]).
- Announcement: choosing a destination announces the new page through the routed view; the active destination is announced as current.

## Dark and light

All colours are roles ([[Theme Following the System]]). The container is `surface` in both; the active pill `secondary_container` and its icon `on_secondary_container` change with the scheme. A frosted variant (container at 72 percent, 20 dp backdrop blur) exists in tess-ui; it is a project effect, not a MD3 surface.

## Defaults

| Setting | Default |
|---|---|
| Form | collapsed |
| Width | 80 dp at default density (72, 64) |
| Alignment | top |
| Destination label | always shown |
| Selection follows focus | no |
| Expanded width | 220 dp |

## Acceptance criteria

- [ ] AC-NRL-1 (token test): container `surface`, level 0, shape 0 dp; indicator `secondary_container` with half-height corners (16 dp at 32 dp high, 28 dp at 56 dp high); icon 24 dp at default.
- [ ] AC-NRL-2 (token test): label `label_medium` (collapsed) or `label_large` (expanded); inactive icon and label `on_surface_variant`; active icon `on_secondary_container` and active label `on_surface` (collapsed); badge `error` with `on_error`.
- [ ] AC-NRL-3 (geometry check): at default, compact and dense, the collapsed rail is 80, 72, 64 dp wide, the pill 56 by 32, 48 by 28, 40 by 24, the first destination starts 44, 24, 12 dp from the top, destinations are 12, 8, 4 dp apart, the icon-to-label gap is 4, 4, 2 dp (scale factors 1.0 and 2.0).
- [ ] AC-NRL-4 (geometry check): the expanded rail is 220 dp wide (width requests 100, 300, 900 give 220, 300, 360), the pill is 56, 40, 32 dp high at the three levels, side padding 20, 12, 8 dp, icon-to-label gap 8, 8, 4 dp.
- [ ] AC-NRL-5 (geometry check): at window widths 599, 600, 839, 840, 1199, 1200 dp the rail is absent at 599, collapsed at 600 and 839, and follows the project policy from 840; an expanded rail at 840 dp with a 220 dp width leaves the content pane at least 320 dp or collapses.
- [ ] AC-NRL-6 (geometry check): resizing across 600 dp with the rail showing removes it at 599 and shows the modal drawer's opener; every destination stays reachable; resizing across the expanded boundary keeps the selection and the focused destination.
- [ ] AC-NRL-7 (scripted input): focus enters the destination list on the selected destination; Down x3 moves focus three enabled destinations, skipping disabled ones; Home and End reach the first and last; no wrap; the selection does not change while focus moves; Enter and Space each choose the focused destination once.
- [ ] AC-NRL-8 (scripted input): Tab order is header controls, then the list once, then footer controls; Shift+Tab reverses; a disabled destination takes no focus, no press and no key.
- [ ] AC-NRL-9 (AT tree assertion): the container has role `navigation` (or `group` where the engine lacks it) with a non-empty name; each destination is a `link` named by its label; `current` is page on exactly the selected one; a badge count is part of the name.
- [ ] AC-NRL-10 (geometry check): a collapsed label of 20 characters ends in `…` within the rail width minus 8 dp each side; the accessible name and the tooltip text are the full label; hovering 500 ms shows a tooltip whose trigger is the destination; a short label shows none.
- [ ] AC-NRL-11 (token test): state layers on a destination: hover 0.08, focus 0.10, pressed 0.10 of `on_surface`; a disabled destination shows none.
- [ ] AC-NRL-12 (review): a rail holds three to seven destinations; a build with fewer than three or more than seven is reported (lint).
- [ ] AC-NRL-13 (scripted input): in a window of 400 dp height with 7 destinations the column scrolls with a visible thumb; the header and footer stay fixed; focusing the last destination by keyboard scrolls it fully into view with its 5 dp ring.
- [ ] AC-NRL-14 (scripted input): with a screens rail, navigating to a screen by any route makes its destination the only one with `current` page within one frame; choosing a destination navigates once.
- [ ] AC-NRL-15 (pixel check): the pill colour change completes 150 ms to 183 ms after the choice at 60 Hz; expand and collapse completes 250 ms to 283 ms; with reduced motion both complete on the next frame.
- [ ] AC-NRL-16 (contrast script): the pairs listed under Accessibility measure at least 4.5:1 in light and dark; the ring at least 3:1 against `surface` and `secondary_container`.
- [ ] AC-NRL-17 (scripted input): a rail and a standard drawer are never both laid out at any width in 320 to 2000 dp.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/NavigationRail_View.tdl`, `NavigationRailItem_View.tdl`, `NavigationRailScreens_View.tdl`, `NavigationRailScreen_View.tdl` and the matching `_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py` (`navigation_rail`), `tess-ui:docs/components/navigation-rail.md`, tests `tess-ui:tests/test_navigation_rail.py` | Partly meets. Meets AC-NRL-1 (80 px `surface` column; pill corners 16 and 28), AC-NRL-2 in part (`label_medium`, selected pill and colours, tested; label weight not prominent when active, not verified), AC-NRL-3 at default only (80, 44 top, 12 apart, pill 56 by 32, tested; no density levels: fails compact and dense), AC-NRL-4 at default only (220 wide, 20 side padding, 56 high pill; expanded width is fixed, no 220 to 360 range), AC-NRL-8 in part (header and footer slots; one Tab stop), AC-NRL-9 in part (destinations `link`, `current` page, tested; container `group` named Navigation, no `navigation` role in the engine), AC-NRL-13 not met (the column does not scroll; it aligns only), AC-NRL-14 (the screens rail follows `app.current_screen`, tested). Fails AC-NRL-5 and AC-NRL-6 (no size-class switching; the caller decides), AC-NRL-7 (arrow keys move focus and also choose: `On_Focus_Enter` writes `Selected`), AC-NRL-17 and AC-NRL-12 (no lint). Used by `tess-ui:examples/tutorial` and `tess-ui:examples/window_dock` through `NavigationRailScreens`; the plain `NavigationRail` is unused. The modal expanded rail, sections with headings and the growing pill are not built |
| tess-shell | none | Absent. The shell has no navigation rail; the nearest shell elements are a vertical Bar, the [[Dock]] and the Workspaces module, specified separately; `Text_Rotation` for a vertical Bar is not built |
| tre | `tre:docs/reference/node.md`, `tre:docs/guide/accessibility.md` | Mechanism only: `link` role, `current` state, focus groups by arrow keys are the toolkit's; no `navigation` role; no size-class switching (tess-ui computes `width_class`) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Width, pill, spacing and expanded sizes per density level | desktop information density; MD3 gives touch sizes | [[ADR-0002 Desktop density levels and target sizes]] |
| Baseline 2022 rail (80 dp, active label `on_surface`); Expressive 96 dp width, 64 dp item and `secondary` label not adopted | ADR-0006 names each Expressive adoption; only the expanded rail is adopted | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Expanded rail adopted (Expressive); it replaces the standard drawer for few destinations | already built in tess-ui; fits desktop width | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Selection does not follow focus; Enter or Space chooses | a screen change per arrow press is disruptive; APG tabs allow selection to follow focus only when the panel loads instantly | [[14 Accessibility Basics]] |
| Arrow keys, Home and End specified | desktop keyboard-first use; MD3 documents no keyboard model | [[14 Accessibility Basics]] |
| Rail removed at compact width; modal drawer takes over | MD3 puts a navigation bar at the bottom on compact windows, a touch pattern that Tesserae desktop does not specify | [[10 Layout Overflow and Scrolling]] |
| Vertical scroll of the destination column with a scrollbar | owner rule for every scroll container; MD3 does not specify overflow | [[ADR-0003 Scrollbar rule]] |
| Pill grows from the icon (Expressive) not adopted; the pill fades in | engine has no per-node size animation of this kind in the view; keeps motion simple | [[Deviations from MD3]] |

## Sources

- Material Web navigation rail tokens (container width 80 px, indicator 56 by 32 px, `corner-full`, container `surface` level 0 shape none, icon 24 px, active icon `on-secondary-container`, active label `on-surface`, inactive `on-surface-variant`, state layers `on-surface`, badge `error` 6 px and 16 px large, label `label-medium`), verified 2026-11-21: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-rail.scss
- Material Web expanded and collapsed rail tokens (collapsed 96 px or 80 px narrow, top space 44 px, item container 64 px; expanded width 220 to 360 px, vertical trailing space 20 px, horizontal item indicator 56 px, icon-label space 8 px, label `label-large`; modal expanded rail `surface-container` level 2): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-nav-rail-collapsed.scss, `_md-comp-nav-rail-expanded.scss`, `_md-comp-nav-rail-item.scss`, `_md-comp-nav-rail-item-vertical.scss`, `_md-comp-nav-rail-item-horizontal.scss` (same folder).
- Material Components Android Navigation Rail guide (collapsed and expanded rail, Expressive changes, header slot with menu and FAB, menu gravity, expanded margin 20 dp, titles for screen readers): https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationRail.md
- WAI-ARIA APG navigation landmark (links, `aria-current`, unique labels): https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/navigation.html
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- tess-ui documentation: `tess-ui:docs/components/navigation-rail.md`; window size classes `tess-ui:src/tess_ui/tokens.py`.
- Not verified: the three to seven destination count on the MD3 specification page (script-rendered app) #needs-verification; the expanded label colours #needs-verification; the dot badge reading #needs-verification.
