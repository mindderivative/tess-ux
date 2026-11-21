---
title: Top App Bar
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, navigation, app-bar]
related: ["[[Toolbar]]", "[[Tabs]]", "[[Status Bar]]", "[[Pagination]]", "[[Title Bar|Window Title Bar]]", "[[Title Bar]]", "[[Icon Button]]", "[[Search]]", "[[Menu]]", "[[Tooltip]]", "[[Navigation Rail]]", "[[Scrollbar and Scroll Container]]", "[[Keyboard Navigation]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Icon Button]]", "[[Colour Roles]]", "[[Typography]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]"]
---

# Top App Bar

> [!info] Summary
> The bar at the top of a screen or content region: a navigation icon, the title and up to three action icons. Material Design 3 counterpart: [Top app bar](https://m3.material.io/components/top-app-bar/overview) (small, centre-aligned, medium, large). Source of truth in code: see Status in code. It is not the window's title bar ([[Title Bar|Window Title Bar]]).

## Purpose

Names the current screen and holds the few actions that belong to it, with a control to go back or open navigation.

## When to use and not

- Use when: a screen or a page inside a window needs a title and one to three global actions.
- Do not use when: the bar holds many commands (use a [[Toolbar]]); the bar is window chrome with window buttons and a drag region (use [[Title Bar|Window Title Bar]] and [[Title Bar]]); the bar reports state (use [[Status Bar]]); the bar switches views (use [[Tabs]]); the bar is a search field (use [[Search]]).
- A window uses one top app bar at most. A custom window title area may host it (`App(borderless=True)` in tess-ui), then it is also a drag region by the title bar rule.

## Anatomy

1. Container (role `group`, named by the title), on `surface`.
2. Navigation icon (optional): an [[Icon Button]] (`menu` or `arrow_back`).
3. Title: one line, ellipsis; the page heading.
4. Action icons: up to three [[Icon Button]]s at the end.
5. Large title (medium and large only): a second row under the icons with a bigger title.
6. Scrolled container colour, shown while content is under the bar.

## Variants

| Variant | Height (default) | Title | Notes |
|---|---|---|---|
| Small | 64 dp | `title_large`, beside the navigation icon | MD3 default |
| Centre-aligned | 64 dp | `title_large`, centred | at most one action |
| Medium | 112 dp | `headline_small` on a second row | collapses to small on scroll |
| Large | 152 dp | `headline_medium` on a second row | collapses to small on scroll |
| Frosted (Tesserae) | as above | as above | container 72 percent of its colour with a 20 px backdrop blur |

Heights and typescale per [Material Web top app bar tokens](https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192) (small and centred 64 px, medium 112 px, large 152 px; headline `title-large`, `headline-small`, `headline-medium`). Medium and large exist at the default density only; at compact and dense they render as small (design choice: a desktop window has no use for a 152 dp header).

## States

The bar has no state layer. Its icon buttons carry the [[Icon Button]] states ([[State Layers]]: hover 8, focus 10, pressed 10 percent).

| State | Visual change | Token values |
|---|---|---|
| Rest (at top) | container `surface`, no shadow | `surface`, elevation level 0 |
| Scrolled | container `surface_container` (tonal level 2), no shadow; the change is 200 ms | `surface_container` |
| Collapsed (medium, large) | shows as small; height eases to 64 dp | tess-ui `Collapsed` |
| Contextual action mode | selection bar replaces the bar | not built; see Variants (not specified here) |

In Material Web the on-scroll container is `surface_container` with level 2 elevation, both marked deprecated in the latest tokens ([latest small tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-top-app-bar-small.scss)); Tesserae draws the colour change and no shadow.

## Tokens used

[[Colour Roles]]: container `surface` or `surface_container`; title and navigation icon `on_surface`; action icons `on_surface_variant` (the Material Web trailing icon colour; tess-ui draws actions in the default icon tint). [[Typography]]: `title_large` (22 / 28), `headline_small` (24 / 32), `headline_medium` (28 / 36), compact `title_medium` (16 / 24), dense `title_small` (14 / 20). [[Shape]]: `corner_none`. [[Elevation]]: level 0. [[Motion]]: height and colour 200 ms. [[Spacing and Density]].

## Sizing and density

| Level | Bar height | Icon button | Icon | Title role | Padding at the ends | Title offset without a navigation icon | Gap navigation icon to title |
|---|---|---|---|---|---|---|---|
| default | 64 dp | 40 dp | 24 dp | `title_large` | 4 dp | 16 dp | 12 dp |
| compact | 48 dp | 32 dp | 20 dp | `title_medium` | 4 dp | 12 dp | 8 dp |
| dense | 40 dp | 28 dp | 20 dp | `title_small` | 4 dp | 8 dp | 8 dp |

- Heights are the Material 3 value at default and 8 dp more than the icon button at compact and dense; paddings, title roles and gaps are design choices. The 64 dp default equals MD3.
- Medium and large: 112 and 152 dp at default only; the large title has 12 dp horizontal padding in tess-ui and 16 dp in MD3 (`CollapsingToolbarLayout` expanded title margin 16 dp, [Android top app bar](https://github.com/material-components/material-components-android/blob/master/docs/components/TopAppBar.md)).
- Action icons: at most three; each icon button hit area at least 24 dp by 24 dp (48 dp in a touch context).
- The title line box is centred vertically in the first row by construction (28 dp line in 64 dp: 18 dp above and below; 24 in 48: 12; 20 in 40: 10).

## Dimensions and defaults

Values agree with Sizing and density above; compact and dense heights, paddings, title roles and gaps are Tesserae choices #needs-verification-as-design-choice. Medium and large exist at the default density only.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container, small | height | - | 64 | 48 | 40 | https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192 (64), design choice, proposed ADR: top app bar heights per density | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container, medium | height | - | 112 | N/A: medium renders as small at compact | N/A: medium renders as small at dense | https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192 | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container, large | height | - | 152 | N/A: large renders as small at compact | N/A: large renders as small at dense | https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192 | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | min height | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| container | padding | `space.2` | 0 4 0 4 | 0 4 0 4 | 0 4 0 4 | design choice, proposed ADR: top app bar heights per density, [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container | margin | - | N/A: the window or pane places the bar edge to edge | N/A: same as the default level | N/A: same as the default level | [[Top App Bar]] Anatomy | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| container | border width | - | 0 | 0 | 0 | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-top-app-bar-small.scss | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| container | border color | - | N/A: the bar draws no border; the scrolled state changes the container colour | N/A: same as the default level | N/A: same as the default level | https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-top-app-bar-small.scss | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| title | padding | `space.5`, `space.4`, `space.3` | 0 0 0 16 | 0 0 0 12 | 0 0 0 8 | [[Top App Bar]] Sizing and density (offset without a navigation icon), design choice, proposed ADR: top app bar heights per density | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| title | font | `title_large`, `title_medium`, `title_small` | 22/28/400/0 | 16/24/500/0.15 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| title, medium | font | `headline_small` | 24/32/400/0 | N/A: medium renders as small at compact | N/A: medium renders as small at dense | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| title, large | font | `headline_medium` | 28/36/400/0 | N/A: large renders as small at compact | N/A: large renders as small at dense | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| title, medium and large | padding | `space.5` | 0 16 0 16 | N/A: renders as small at compact | N/A: renders as small at dense | https://github.com/material-components/material-components-android/blob/master/docs/components/TopAppBar.md (16) | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| navigation icon and title | gap | - | 12 | 8 | 8 | [[Top App Bar]] Sizing and density, design choice, proposed ADR: top app bar heights per density | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| action icon button | height | `density.icon_button_container` | 40 | 32 | 28 | [[Icon Button]], [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| action icon button | min width | - | 40 | 32 | 28 | [[Icon Button]] (square container) | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| action icon button | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Icon Button]], [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |

## Layout and overflow

- Title: single line (`Max_Lines 1`), ellipsis at the end, the full title as the accessible name and as a tooltip on the title text when truncated (ADR-0004); the title shrinks (`Min_Width 0`) before icons do. The navigation icon and the actions never shrink or overlap.
- More than three actions: the surplus goes into a [[Menu]] under a More icon button (the third slot); MD3 allows an overflow menu in the same way. A bar with more commands than that is a [[Toolbar]].
- The bar spans the width of its region; the large title wraps to at most two lines, then ends with an ellipsis ([[10 Layout Overflow and Scrolling]]).
- The bar does not scroll; the content under it does. Scrolled colour applies when the content's scroll offset is above zero.

## Behaviour

- Pointer: icon buttons as [[Icon Button]]; the bar's title is not a control. With window controls (frameless windows), the bar's empty area is a drag region (see [[Title Bar|Window Title Bar]]).
- Keyboard: the navigation icon and the actions are Tab stops in visual order (start to end); no roving group, because at most four controls ([[Keyboard Navigation]]). Enter and Space activate. The title is a heading, not focusable.
- Touch: tap on 48 dp hit areas in a touch context.
- Collapse: bound to the scroll offset of the content under the bar (`At_Top` of a scroll view), one-way; the user cannot collapse the bar by hand.

## Tooltip and overlay behaviour

Each icon carries a plain tooltip with its name on the icon button ([[ADR-0004 Tooltip rule]], [[Tooltip]]); a truncated title carries a tooltip on the title text. The bar and the large title row carry none. The only overlay is the overflow [[Menu]], which returns focus to the More icon on close.

## Motion

Bar height and colour change 200 ms (`short4`) in tess-ui; MD3 collapses with the scroll offset. Reduced motion: height and colour change at once. Titles do not animate.

## Accessibility

- Role: `group` named by the title (the engine has no `banner` or `toolbar` role, `tre:docs/reference/node.md`); the title is a heading level 1 (`Heading: 1`).
- Names: navigation icon "Navigation" by default (project sets "Open navigation" or "Back"), actions by their labels; every icon button has a name equal to its tooltip (AR-3).
- Keys: as in Behaviour.
- Contrast: title on container 4.5 to 1 (`on_surface` on `surface` and `surface_container`); icons 3 to 1 (WCAG 2.2 SC 1.4.3, 1.4.11).
- Frosted container: the text contrast is measured against the worst case behind the blur (the page background), not the container colour alone #needs-verification.
- No announcement when the bar collapses or its colour changes.

## Dark and light

All roles follow the scheme ([[Theme Following the System]]); AC-TAB-8 runs in both.

## Defaults

Small variant, 64 dp at default density, `surface`, no frost, navigation icon label "Navigation", no actions. A medium or large bar collapses only when the caller binds `Collapsed`.

## Acceptance criteria

- [ ] AC-TAB-1 (token test): bar height 64, 48, 40 dp for small and centre-aligned at default, compact, dense; 112 and 152 dp for medium and large at default and 64, 48, 40 dp at compact and dense; icon button 40, 32, 28 dp; icon 24, 20, 20 dp. Pass: values equal.
- [ ] AC-TAB-2 (geometry check): the title line box and the icon buttons are vertically centred in the first row at each level and scale 1.0 and 2.0 (within 0.5 dp). Pass: offsets within 0.5 dp.
- [ ] AC-TAB-3 (geometry check): a title longer than the available width ends with an ellipsis, the icons keep their size and position, no pixel lies outside the bar, and a tooltip with the full title shows on the title text. Pass: ellipsis present, zero pixels outside, tooltip text equals the title.
- [ ] AC-TAB-4 (token test): rest container `surface`, scrolled `surface_container`, title `on_surface`, navigation icon `on_surface`; no literal colour; medium title `headline_small`, large `headline_medium`, small `title_large`. Pass: role references and roles equal.
- [ ] AC-TAB-5 (scripted input): with the scroll offset above zero the container resolves to `surface_container` within 200 ms (one frame with reduced motion); back at the top it returns to `surface`; a medium or large bar with `Collapsed` true measures 64 dp and returns to its full height when false. Pass: colours and heights equal.
- [ ] AC-TAB-6 (scripted input): Tab visits the navigation icon, then each action, in visual order, then leaves the bar; Enter and Space on each activate once; Escape does nothing in the bar. Pass: focus order and activation counts equal.
- [ ] AC-TAB-7 (AT tree assertion): the bar is a `group` named by the title; the title node is a heading level 1; the navigation icon and each action have role `button` and a non-empty name equal to their tooltip; icons are hidden. Pass: all equal.
- [ ] AC-TAB-8 (contrast script): in light, dark and high contrast, `on_surface` on `surface` and on `surface_container` at least 4.5 to 1; action icons on the container at least 3 to 1. Pass: ratios at or above limits.
- [ ] AC-TAB-9 (geometry check): icon button hit areas at least 24 dp by 24 dp (48 dp in a touch context), no overlap with the title area. Pass: bounds at or above limits.
- [ ] AC-TAB-10 (scripted input): with more than three actions the third slot is a More button that opens a menu holding the rest in order; Escape closes it and returns focus to the More button. Pass: menu rows and focus owner equal.
- [ ] AC-TAB-11 (pixel check): under keyboard focus each icon button shows the focus ring (3 dp, 2 dp offset, `secondary`) and the bar's clip never cuts it. Pass: ring pixels present, none clipped.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TopAppBar_View.tdl`, `tess-ui:src/tess_ui/views/TopAppBar_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py` | partly meets. Four variants (64, 64, 112, 152 dp), `Collapsed` and `Scrolled` (surface to surface_container, 200 ms), frosted, title `Max_Lines 1` with ellipsis, heading 1, every icon an Icon Button with name and tooltip, up to three actions, role group named by the title (AC-TAB-1 partly: default only; AC-TAB-3 partly: ellipsis yes, title tooltip not read; AC-TAB-4 meets by reading; AC-TAB-5 meets by reading; AC-TAB-7 partly: group and heading, no banner role). Fails: no density (AC-TAB-1, AC-TAB-2 unmeasured); actions beyond three are cut by `actions[:3]` with no More menu (AC-TAB-10); the Python widget draws 48 px icon buttons; contextual action mode not built; action icons not `on_surface_variant` (AC-TAB-4) |
| tess-ui | `tess-ui:apps/shell_config/` | not used: the config app has no top app bar |
| tess-shell | none | absent (the shell panel is a [[Bar]], not an app bar) |
| tre | `tre:docs/guide/custom-title-bars.md` | not applicable: custom title bars are window chrome ([[Title Bar|Window Title Bar]]) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Heights 48 and 40 dp at compact and dense; medium and large only at default | desktop density; no use for tall headers in windows | [[ADR-0002 Desktop density levels and target sizes]] |
| Title roles `title_medium` and `title_small` at compact and dense | smaller bar | [[ADR-0002 Desktop density levels and target sizes]] |
| On scroll only the container colour changes, no shadow | the shadow tokens are deprecated in Material Web; tonal separation is enough | none |
| Frosted variant (translucent with blur) | tess-ui effect; not in MD3 | [[ADR-0006 MD3 baseline with named Expressive adoptions]] #needs-verification |
| More than three actions overflow into a menu | no hidden command (chapter 10) | none |
| Hit area is the icon button, 24 dp floor, 48 dp in touch contexts | desktop target size | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- [Material Web top app bar tokens, v0_192 listing](https://github.com/material-components/material-web/tree/main/tokens/versions/v0_192) and the files `_md-comp-top-app-bar-small.scss`, `-small-centered`, `-medium`, `-large`: container height 64, 64, 112, 152 px, title-large, headline-small, headline-medium, leading icon 24 px, on-scroll container `surface-container`.
- [Material Web latest small tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-top-app-bar-small.scss): container elevation level 0, on-scroll tokens deprecated.
- [Material Components Android top app bar](https://github.com/material-components/material-components-android/blob/master/docs/components/TopAppBar.md): lift on scroll colour `surfaceContainer`, expanded title margin 16 dp, overflow menu.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.3, 1.4.11, 2.5.8.
- Code: `tess-ui:docs/components/top-app-bar.md`, `tess-ui:src/tess_ui/views/TopAppBar_View.tdl`, `tess-ui:src/tess_ui/views/TopAppBar_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py`.
- The m3.material.io top app bar page could not be fetched; the contextual action mode is not specified for lack of a verified source #needs-verification.
