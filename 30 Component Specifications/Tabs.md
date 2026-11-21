---
title: Tabs
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, navigation, tabs]
related: ["[[Top App Bar]]", "[[Toolbar]]", "[[Pagination]]", "[[Status Bar]]", "[[Segmented Button]]", "[[Navigation Rail]]", "[[Dock Panel]]", "[[Badge]]", "[[Divider]]", "[[Tooltip]]", "[[Menu]]", "[[Icon Button]]", "[[Scrollbar and Scroll Container]]", "[[Keyboard Navigation]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[Iconography]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Colour Roles]]", "[[Typography]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]"]
---

# Tabs

> [!info] Summary
> A tab bar: one row of tabs that switch between panels of content at the same level of hierarchy, with an indicator under the selected tab. Material Design 3 counterpart: [Tabs](https://m3.material.io/components/tabs/overview) (primary and secondary). Source of truth in code: see Status in code.

## Purpose

The user chooses one of several parallel views (General, Keys, Advanced) and sees only that view. The bar shows all choices at once, names each one, and marks the current one.

## When to use and not

- Use when: two or more peer views of one subject share a region, only one is shown at a time, and the user switches often.
- Do not use when: the choices are a filter or a mode of one list (use [[Segmented Button]]); the choices are app destinations (use [[Navigation Rail]]); the views are panels the user arranges (use [[Dock Panel]]); the choices set an option value (use a radio set or [[Switch]]); there is one view only.
- Use one type per bar: primary tabs at the top of a view, secondary tabs inside a primary tab's panel. Do not nest more than two bars.
- Do not put actions in a tab bar; a [[Toolbar]] holds actions.

## Anatomy

1. Bar container (role `tablist`), full width of the region, on `surface`.
2. Tab (role `tab`): hit area, state layer, label, optional icon, optional [[Badge]].
3. Label, `title_small`.
4. Icon (optional), 24 dp at default, 20 dp at compact and dense ([[Iconography]]).
5. Active indicator under the selected tab.
6. Divider along the bottom edge ([[Divider]]).
7. Panel (role `tabpanel`): the content of the selected tab, owned by the author, adjacent to the bar.
8. Overflow scrollbar thumb, only when the tabs do not fit ([[ADR-0003 Scrollbar rule]]).

## Variants

| Variant | Use | Differences |
|---|---|---|
| Primary | top-level views of a screen or window | indicator 3 dp tall, `primary`, top corners rounded 3 dp, as wide as the label (icon-and-label: the wider of label and icon) and centred in the tab; selected label and icon `primary`; with an icon above the label the bar is 64 dp tall at default |
| Secondary | sub-views inside a panel | indicator 2 dp tall, `primary`, full tab width, square; selected label `on_surface`; inactive `on_surface_variant`; no stacked icon form |
| Fixed | few tabs that fit | each tab is bar width divided by the tab count, never below the tab minimum width |
| Scrollable | more tabs than fit | tabs take their content width between 72 and 264 dp; the bar scrolls horizontally |
| Automatic activation (default) | the panel shows without noticeable delay | focus moves the selection |
| Manual activation | the panel costs more than 100 ms to build or switching has side effects | arrows move focus only; Enter or Space selects |

Fixed and scrollable are the two Android modes ([Material Components Android tabs](https://github.com/material-components/material-components-android/blob/master/docs/components/Tabs.md): fixed tabs share the width and do not scroll, scrollable tabs have min width 72 dp and max width 264 dp). The activation modes come from the [WAI-ARIA Authoring Practices tabs pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/): automatic is recommended when panels appear without noticeable latency. The 100 ms threshold is a Tesserae choice.

## States

State layer percentages from [[State Layers]]: hover 8, focus 10, pressed 10 percent ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]); disabled content 38 percent.

| State | Visual change | Token values |
|---|---|---|
| Inactive rest | label and icon `on_surface_variant` (primary tab and secondary tab) | Material Web `inactive-*` tokens |
| Active (selected) | primary: label and icon `primary`; secondary: label `on_surface`, icon `on_surface`; indicator shown | `active-*` tokens |
| Hover | state layer 8 percent; primary inactive: `on_surface` layer, active: `primary` layer; secondary: `on_surface` | Material Web primary and secondary navigation tab tokens |
| Focus (keyboard) | state layer 10 percent and the focus ring (inward variant, 3 dp, `secondary`) | [[Focus Ring]] |
| Pressed | state layer 10 percent; primary inactive pressed layer is `primary`, active `primary`, secondary `on_surface` | tokens |
| Disabled | label and icon `on_surface` at 38 percent; the tab takes no focus, pointer or key (the engine flag only announces) | [[State Layers]] |
| Selected and focused | both layers add: the indicator stays, the ring shows | review |

The selected state differs from inactive by the indicator (a shape) as well as colour (AR-18).

## Tokens used

[[Colour Roles]]: bar `surface`, selected `primary`, inactive `on_surface_variant`, layers `on_surface` and `primary`, ring `secondary`. [[Typography]]: label `title_small` (14 / 20, weight 500). [[Shape]]: container `corner_none`; primary indicator top corners 3 dp. [[Motion]]: indicator slide. [[Spacing and Density]]: heights and paddings. Material Web token files: [primary navigation tab](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-primary-navigation-tab.scss) (indicator height 3 px, container height 48 px, with icon and label 64 px, icon 24 px, container `surface`) and [secondary navigation tab](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-secondary-navigation-tab.scss) (indicator 2 px, container 48 px, icon 24 px, active label `on_surface`).

## Sizing and density

MD3: bar 48 dp, 64 dp for icon above label, indicator 3 dp (primary) or 2 dp (secondary).

Tesserae by density ([[ADR-0002 Desktop density levels and target sizes]]; the bar heights are derived from the control heights 40, 32, 28 plus 8, a design choice):

| Level | Bar height | Icon above label (primary) | Icon beside label | Icon | Tab horizontal padding | Icon to label gap |
|---|---|---|---|---|---|---|
| default | 48 dp | 64 dp | allowed (48 dp) | 24 dp | 12 dp | 8 dp |
| compact | 40 dp | not offered (icon beside label) | 40 dp | 20 dp | 12 dp | 8 dp |
| dense | 32 dp | not offered (icon beside label) | 32 dp | 20 dp | 8 dp | 4 dp |

- Indicator height is 3 dp (primary) and 2 dp (secondary) at all levels.
- Tab minimum width 72 dp (scrollable, Android `tabMinWidth`), maximum 264 dp (`tabMaxWidth`); a fixed bar gives each tab bar width divided by tab count and switches to scrollable when that quotient falls below 72 dp.
- The hit area is the whole tab (full bar height by tab width), at least 24 dp by 24 dp; 48 dp high in a touch context ([[Spacing and Density]], WCAG 2.2 SC 2.5.8).
- The label line box (20 dp) is centred vertically by construction: 14, 10 and 6 dp above and below at 48, 40 and 32 dp (derived, not tokens). With an icon beside the label both are centred on the bar's middle line.

## Dimensions and defaults

Values agree with Sizing and density above; bar heights and compact and dense paddings are Tesserae choices #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| bar | height | `density.control_height` plus 8 | 48 | 40 | 32 | https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-primary-navigation-tab.scss (48), design choice, proposed ADR: tab bar height per density, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| bar, primary with icon above label | height | - | 64 | N/A: not offered, the icon sits beside the label (40) | N/A: not offered, the icon sits beside the label (32) | https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-primary-navigation-tab.scss | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| bar | padding | - | N/A: the tab carries the horizontal padding, the bar none | N/A: same as the default level | N/A: same as the default level | [[Tabs]] Sizing and density | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| bar | margin | - | N/A: the region sets the outer space; the panel sits directly under the divider | N/A: same as the default level | N/A: same as the default level | [[Tabs]] Layout and overflow | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| bar | gap | - | 0 | 0 | 0 | [[Tabs]] Anatomy (tabs touch, each carries its own padding) | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| bar | border width | - | 0 | 0 | 0 | https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-primary-navigation-tab.scss | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| bar | border color | - | N/A: the bar draws no border; the divider is its own part | N/A: same as the default level | N/A: same as the default level | [[Tabs]] Anatomy | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| bar | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| bar | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| tab | min width | - | 72 | 72 | 72 | https://github.com/material-components/material-components-android/blob/master/docs/components/Tabs.md (`tabMinWidth`) | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| tab | min height | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| tab | padding | `space.4`, `space.3` | 0 12 0 12 | 0 12 0 12 | 0 8 0 8 | design choice, proposed ADR: tab bar height per density, [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| tab | margin | - | N/A: tabs touch; spacing is the tab padding | N/A: same as the default level | N/A: same as the default level | [[Tabs]] Sizing and density | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| tab | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Tabs]] Sizing and density, [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| tab | font | `title_small` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| tab | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Iconography]], [[Spacing and Density]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| tab | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| tab | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| active indicator, primary | height | - | 3 | 3 | 3 | https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-primary-navigation-tab.scss | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| active indicator, primary | corner radius | - | 3 3 0 0 | 3 3 0 0 | 3 3 0 0 | https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-primary-navigation-tab.scss (top corners) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| active indicator, secondary | height | - | 2 | 2 | 2 | https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-secondary-navigation-tab.scss | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| active indicator, secondary | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] (square) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| divider | height | - | 1 | 1 | 1 | [[Divider]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| divider | border color | `outline_variant` | `outline_variant` | `outline_variant` | `outline_variant` | [[Divider]], [[Colour Roles]] | tess-ui: yes (style background); tess-shell: n/a: element absent in tess-shell; tre: yes (background) |

## Layout and overflow

- The label is one line. A label wider than the tab's maximum width (264 dp) or its share of a fixed bar ends with an ellipsis; the icon and padding stay ([[10 Layout Overflow and Scrolling]]). The full label is the accessible name and the tooltip of the tab (ADR-0004).
- Overflow rule for the tab bar: scroll, not a menu. A bar whose tabs do not fit scrolls horizontally with a visible scrollbar thumb ([[ADR-0003 Scrollbar rule]], [[Scrollbar and Scroll Container]]); the thumb sits below the divider so that it does not cover the indicator. Every tab is reachable by pointer (wheel and thumb) and by keyboard. The vertical wheel scrolls the bar horizontally while the pointer is over it.
- The focused and the selected tab are scrolled fully into view; on resize the selected tab stays in view. A tab never paints outside the bar and is never clipped without a way to scroll to it (hard rules 1 and 3 of chapter 10).
- Overflow by a menu listing every tab (as for a [[Toolbar]]) is not part of this specification; a project with very many tabs (more than 12) uses a [[List]] or [[Navigation Rail]] instead.
- The bar is as wide as its region; the panel sits directly under the divider; the indicator and divider move with the scroll.

## Behaviour

- Pointer: click on a tab selects it once; press, move out, release selects nothing; hover shows the layer; a click on the selected tab changes nothing.
- Keyboard ([WAI-ARIA tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/), [[Keyboard Navigation]]): the bar is one Tab stop (roving focus). Tab enters the bar on the selected tab (the first tab when none is selected) and the next Tab leaves the bar into the panel or the next control. Right Arrow moves focus to the next tab, Left Arrow to the previous, both wrapping at the ends. Home focuses the first tab, End the last. Disabled tabs are skipped. Automatic activation: focus moves the selection; manual: Enter or Space selects the focused tab. Up and Down do nothing in a horizontal bar. A vertical bar (not specified here) swaps the axes.
- Touch: tap on the tab; swipe on the bar scrolls it; swiping the panel to change tabs is not specified.
- Closing and reordering tabs belong to [[Dock Panel]] and a document tab strip; this note does not specify them.

## Tooltip and overlay behaviour

A tab whose label is fully visible and that has an icon and label needs no tooltip. A tab with a truncated label or an icon only carries a plain tooltip on the tab itself with the full label (500 ms on hover, at once on keyboard focus, [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]], [[Tooltip]]). The bar and the panel carry no tooltip. Tabs open no overlay.

## Motion

- Indicator slides to the new tab: X and width over 250 ms (`medium1`; Android `tabIndicatorAnimationDuration` 250 ms; tess-ui `Transition` 250 ms), easing `emphasized` in the Python widget. [[Motion]].
- Scroll into view of a focused tab: 250 ms, `standard`.
- State layer fade: `short3` 150 ms.
- Reduced motion: the indicator jumps and the scroll is immediate ([[14 Accessibility Basics]], AR-27).
- The panel change is immediate; a cross-fade is optional and at most 90 ms out and 210 ms in.

## Accessibility

- Roles: bar `tablist` (label required, for example "Settings sections"), each tab `tab`, each panel `tabpanel` ([WAI-ARIA 1.2 tab](https://www.w3.org/TR/wai-aria-1.2/#tab)). The engine has the three roles (`tre:docs/reference/node.md`). Exactly one tab has `selected`. A tab's `controls` points to its panel and the panel's name is the tab's label (the engine has `controls`, `labelledby` is not in the engine docs, so the panel label repeats the text).
- Name: the label text; an icon-only tab's name is its tooltip text; a badge adds its value to the name ("Inbox, 3 new") by the badge's own rule ([[Badge]]).
- Keys: as in Behaviour. A tab panel without focusable content is itself reachable by Tab (APG `tabindex 0`) so the next Tab after the bar lands on the content region.
- Contrast: selected label `primary` and inactive label `on_surface_variant` against `surface` at least 4.5 to 1; the indicator against `surface` at least 3 to 1 (WCAG 2.2 SC 1.4.3, 1.4.11).
- Announcement: selection change is read by the reader from the focused tab's `selected` state; no extra announce call.
- Focus: ring inside the tab (inward variant, [[Focus Ring]]) so a clipping scroll container never hides it (AC-FOC-5).

## Dark and light

All roles resolve per scheme ([[Theme Following the System]]); contrast criteria run in both and in high contrast.

## Defaults

Primary, fixed, automatic activation, density per container (default 48 dp), indicator under the selected tab, selected tab the first when none is given, divider shown. tess-ui defaults: variant `primary`, `Tab_Width` 120.

## Acceptance criteria

- [ ] AC-TBS-1 (token test): bar heights 48, 40, 32 dp at default, compact, dense; 64 dp for the icon-above-label primary bar at default only; indicator 3 dp (primary) and 2 dp (secondary) at all levels; icon 24, 20, 20 dp. Pass: values equal.
- [ ] AC-TBS-2 (geometry check): the label line box is vertically centred in the bar at each level and scale 1.0 and 2.0 (space above equals space below within 0.5 dp); with an icon beside the label both centres lie on the bar's middle line within 0.5 dp. Pass: offsets within tolerance.
- [ ] AC-TBS-3 (geometry check): tab minimum width 72 dp and maximum 264 dp; in a fixed bar each tab is bar width over tab count, and a bar with count times 72 dp greater than its width is scrollable. Pass: widths equal the rule.
- [ ] AC-TBS-4 (geometry check): hit area of every tab at least 24 dp by 24 dp (48 dp high in a touch context) and tab hit areas do not overlap. Pass: bounds at or above the limits, zero intersection.
- [ ] AC-TBS-5 (AT tree assertion): the bar has role `tablist` and a name; every tab has role `tab` and a non-empty name; exactly one tab has `selected` true; each tab's `controls` resolves to a node with role `tabpanel` that is visible only for the selected tab. Pass: all equal.
- [ ] AC-TBS-6 (scripted input): Tab from the control before the bar focuses the selected tab; the next Tab leaves the bar to the panel or next control; Shift+Tab returns to the selected tab; the bar is exactly one Tab stop. Pass: focus owner equals at each step.
- [ ] AC-TBS-7 (scripted input): with focus on a tab, Right, Left, Home and End move focus to next (wrapping from last to first), previous (wrapping), first and last; a disabled tab is skipped; Up and Down move nothing. Pass: focus owner equals the expected tab after each key.
- [ ] AC-TBS-8 (scripted input): automatic mode: after Right the focused tab is selected and its panel is visible within one frame; manual mode: after Right the selection is unchanged and after Enter, then separately Space on another tab, it changes once each. Pass: selection and panel equal.
- [ ] AC-TBS-9 (scripted input): pointer click selects once; press, move out, release selects nothing; a disabled tab takes no focus, click or key. Pass: selection change counts equal.
- [ ] AC-TBS-10 (token test): state layers equal 8, 10, 10 percent in the colours of the States table for primary and secondary, disabled content 38 percent; every colour is a role reference. Pass: values equal, no literal colour.
- [ ] AC-TBS-11 (pixel check): under keyboard focus the focus ring is 3 dp wide, role `secondary`, inside the tab bounds, not clipped by the bar or a scroll container, absent after a mouse click. Pass: ring pixels present inside bounds, none clipped.
- [ ] AC-TBS-12 (geometry check): a label longer than the tab's maximum or share shows an ellipsis and no text pixel lies outside the tab; hover for 600 ms shows a tooltip with the full label, keyboard focus shows it at once, press or Escape dismisses it. Pass: ellipsis present, zero pixels outside, tooltip text equals the label.
- [ ] AC-TBS-13 (scripted input): with tabs whose summed minimum width exceeds the bar width, the bar shows a horizontal scrollbar thumb, the focused tab and the selected tab lie fully inside the viewport after each arrow key and after a resize, and the last tab is reachable by End and by the pointer. Pass: bounds inside viewport, thumb present, last tab focused.
- [ ] AC-TBS-14 (contrast script): in light, dark and high contrast, selected label (`primary`, or `on_surface` for secondary) and inactive label on `surface` at least 4.5 to 1; indicator on `surface` at least 3 to 1. Pass: ratios at or above limits.
- [ ] AC-TBS-15 (scripted input): the indicator reaches its new position and width in 250 ms (within one frame); with reduced motion simulated true it reaches it within one frame. Pass: frame counts equal.
- [ ] AC-TBS-16 (AT tree assertion): an icon-only tab has a non-empty name equal to its tooltip text and a decorative icon hidden; a tab with a badge has the badge value in its name. Pass: names equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Tabs_View.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py`, `tess-ui:docs/components/tabs.md` | partly meets. Role `tablist` on the bar, `tab` with label and `Selected`, `Focus_Group: horizontal` (one Tab stop, Left and Right with wrap, Home and End, type-ahead, `tess-ui:src/tess_ui/composed.py`), focus enter selects (automatic only), indicator 3 dp rounded top, 12 dp inset, slides 250 ms, bar 48 and 64 dp, title_small, primary and on_surface_variant colours, divider (AC-TBS-5 partly, AC-TBS-7 meets by reading, AC-TBS-1 partly). Fails: no `tabpanel`, no `controls` (AC-TBS-5); no manual activation (AC-TBS-8); no density (AC-TBS-1); fixed `Tab_Width` 120 and no scrolling bar (AC-TBS-3, AC-TBS-13: "Not built"); label has no `Max_Lines` or ellipsis and no tooltip (AC-TBS-12); no per-tab disabled (AC-TBS-9); selected-first rule not read (AC-TBS-6 unmeasured); secondary label stays `primary` when selected, not `on_surface` (AC-TBS-10); indicator spans tab width minus 24, not the label (primary); the Python `tabs()` spans the label |
| tess-ui | `tess-ui:src/tess_ui/docking.py` (dock panel tab strips) | role `tablist`, Left and Right arrows; specified in [[Dock Panel]] |
| tess-shell | none (the shell has no tab element; `Workspaces` shows workspaces, not tabs) | absent |
| tre | `tre:docs/reference/node.md` | not applicable: roles `tab`, `tablist`, `tabpanel` and `controls` exist; no tab widget; roving focus is built by tess-ui |

Evidence: no app or example in tess-ui uses `Tabs` outside the gallery; the config app has no tabs.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Bar heights 48, 40, 32 dp; icon above label only at default | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Icon 20 dp at compact and dense | smaller container | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the tab, 24 dp floor, 48 dp in touch contexts | desktop target size | [[ADR-0002 Desktop density levels and target sizes]] |
| Tab bar overflow scrolls with a visible scrollbar thumb | scrollbar rule: content never silently clipped | [[ADR-0003 Scrollbar rule]] |
| Focus ring inward, 3 dp, `secondary` | the ring must not be clipped by the bar or a scroller | [[ADR-0009 State layer percentages]] |
| Manual activation mode and roving focus keys (Home, End, wrap) | desktop keyboard-first use, WAI-ARIA tabs pattern | none (no ADR needed; Tesserae-only behaviour) |
| Focus and pressed state layers 10 percent (Material Web v0_192 has 12) | latest token set | [[ADR-0013 Focus and pressed state layer 10 percent]] |

## Sources

- [Material Web primary navigation tab tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-primary-navigation-tab.scss) and [secondary navigation tab tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-secondary-navigation-tab.scss): heights, indicator, icon size, layer colours.
- [Material Web tabs documentation](https://github.com/material-components/material-web/blob/main/docs/components/tabs.md): primary and secondary, `active` selection, change event.
- [Material Components Android tabs](https://github.com/material-components/material-components-android/blob/master/docs/components/Tabs.md): height 48 dp or 72 dp, fixed and scrollable modes, min width 72 dp, max width 264 dp, indicator animation 250 ms, content descriptions.
- [WAI-ARIA Authoring Practices: tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/): roles, keys, automatic and manual activation, panel `tabindex`.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.3, 1.4.11, 2.1.1, 2.5.8.
- Code: `tess-ui:src/tess_ui/views/Tabs_View.tdl`, `tess-ui:docs/components/tabs.md`, `tess-ui:docs/guide/view-language.md` (`Focus_Group`), `tre:docs/reference/node.md` (roles).
- The m3.material.io tabs page could not be fetched; the 64 dp icon-and-label height comes from the Material Web token `with-icon-and-label-text-container-height`.
