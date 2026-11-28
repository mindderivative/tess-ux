---
title: Pagination
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, navigation, pagination]
related: ["[[Toolbar]]", "[[Top App Bar]]", "[[Tabs]]", "[[Status Bar]]", "[[Carousel]]", "[[Button]]", "[[Icon Button]]", "[[List]]", "[[Scrollbar and Scroll Container]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "[[Tooltip]]", "[[Keyboard Navigation]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Button]]", "[[Icon Button]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]"]
---

# Pagination

> [!info] Summary
> Page navigation for content that arrives in pages: previous and next, page numbers with an ellipsis for the stretches left out, a compact "3 of 12" form and a dot form for carousels. A Tesserae element with no Material Design 3 counterpart; the nearest MD3 patterns are the page indicator of the [Carousel](https://m3.material.io/components/carousel/overview) and the common [buttons](https://m3.material.io/components/buttons/overview). Source of truth in code: see Status in code.

## Purpose

Moves the user through numbered pages of one result set and shows where they are and how many there are.

## When to use and not

- Use when: the data source delivers pages (a search with 200 results in pages of 20) and the user must jump to a page.
- Do not use when: the whole list can scroll (use [[List]] in a [[Scrollbar and Scroll Container]], with virtual rows for long lists); the pages are views of different kinds (use [[Tabs]]); the steps are a wizard.
- Dots form: only for a [[Carousel]] or a short sequence of at most 10 pages. More than 10: numbers or the compact form.
- Not built and not specified here: an items-per-page control, a total item count and a jump-to field (tess-ui lists them as gaps).

## Anatomy

1. Container (role `group`, name "Pagination").
2. Previous: an [[Icon Button]] (`chevron_left`), name "Previous page".
3. Page slots (numbers form): a [[Button]] per shown page, the current one filled.
4. Ellipsis: an inert "…" for each stretch left out.
5. Next: an [[Icon Button]] (`chevron_right`), name "Next page".
6. Summary (compact form): "3 of 12" text between the arrows.
7. Dots (dot form): a button per page with an 8 dp mark inside a 24 dp hit area.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Numbers (default) | result sets, up to many pages | at most 6 numbers and 2 ellipses shown: the first, the last and the current page and its neighbours always show |
| Compact | narrow places | previous, "3 of 12", next; no number buttons |
| Dots | carousel and short sequences | one dot per page, the current one `primary` |

Windowing rule (from `tess-ui:src/tess_ui/views/Pagination_View.tdl`): with 7 pages or fewer all numbers show. With more, the first page, the last page, the current page and the pages beside it show, plus page 2 when the current page is 4 and the second-to-last page when the current page is the last but three (so a stretch of one page shows its number, not an ellipsis); an ellipsis stands for each other stretch left out. At most 6 numbers and 2 ellipsis show, so the control has at most 10 controls (previous, 6 numbers, 2 ellipses, next). The Python `pagination()` widget uses a different rule (7 slots by `max_visible`); the specification follows the view.

## States

State layer percentages from [[State Layers]]: hover 8, focus 10, pressed 10 percent; disabled content 38 percent.

| State | Visual change | Token values |
|---|---|---|
| Number rest | text button: label `primary`, no container | [[Button]] text variant |
| Current page | filled button: container `primary`, label `on_primary`; `current` is `page` | [[Button]] filled variant |
| Hover, focus, pressed | state layers 8, 10, 10 percent in the label colour; focus ring | [[State Layers]], [[Focus Ring]] |
| Previous or next disabled | `on_surface` at 38 percent; at the first page previous, at the last page next; no focus, pointer or key | [[State Layers]] |
| Ellipsis | text `on_surface_variant`, inert, hidden from the accessibility tree | [[Colour Roles]] |
| Dot current | mark `primary` | [[Colour Roles]] |
| Dot other | mark `outline` at least 3 to 1 against the surface | [[Colour Roles]] |

The current page differs from the others by container (filled) and by `current`, not by colour alone (AR-18). In tess-ui the other dots are `outline_variant`, which MD3 sets as a decorative divider colour and which is expected to fall below 3 to 1 against `surface` #needs-verification.

## Tokens used

[[Colour Roles]] as in States. [[Typography]]: page numbers `label_large` (14 / 20, weight 500; `title_dense` 13 / 18 at dense); summary `label_large` (same). [[Shape]]: number buttons and arrows `corner_full`, dots circle. [[Motion]]: layer fade `short3`. [[Spacing and Density]].

## Sizing and density

| Level | Button and arrow size | Number min width | Icon (arrows) | Gap between controls | Ellipsis width | Dot hit area | Dot mark |
|---|---|---|---|---|---|---|---|
| default | 40 dp | 40 dp | 24 dp | 4 dp | 40 dp | 24 dp | 8 dp |
| compact | 32 dp | 32 dp | 20 dp | 4 dp | 32 dp | 24 dp | 8 dp |
| dense | 28 dp | 28 dp | 20 dp | 2 dp | 28 dp | 24 dp | 6 dp |

- Sizes follow [[Button]] and [[Icon Button]] (40, 32, 28 dp); the number buttons are circles at their minimum width and pill-shaped when a number needs more width (page 1000).
- The dot's hit area is 24 dp at every level (the floor of [[ADR-0002 Desktop density levels and target sizes]]); in a touch context 48 dp, then adjacent dots overlap only if spacing is below 48 dp, so touch dots are spaced 48 dp centre to centre. The mark itself stays small.
- The label is vertically centred in the button by construction ([[Button]], AC-BTN-2).
- Gaps are 4 dp (default, compact) and 2 dp (dense); hit areas do not overlap ([[Spacing and Density]], AC-DEN-8).

## Dimensions and defaults

Values agree with Sizing and density above. Button paddings follow [[Button]] and [[Icon Button]]; the dot values and gaps are Tesserae choices #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | `density.control_height` | 40 | 32 | 28 | [[Button]], [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | padding | - | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Pagination]] Anatomy (the controls touch the container edge) | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container | margin | - | N/A: the parent places the control | N/A: same as the default level | N/A: same as the default level | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| container | gap | `space.2`, `space.1` | 4 | 4 | 2 | [[Pagination]] Sizing and density, design choice, proposed ADR: pagination gaps and dots per density | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| container | border width | - | 0 | 0 | 0 | [[Pagination]] Tokens used (no border drawn) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| container | border color | - | N/A: the container and the filled current page draw no border | N/A: same as the default level | N/A: same as the default level | [[Pagination]] States | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| number button | height | `density.control_height` | 40 | 32 | 28 | [[Button]], [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| number button | min width | - | 40 | 32 | 28 | [[Pagination]] Sizing and density | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| number button | min height | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| number button | padding | `space.3` | 0 8 0 8 | 0 8 0 8 | 0 8 0 8 | [[Button]] (text variant padding 12, 8, 8; the pagination button grows with its digits), design choice, proposed ADR: pagination gaps and dots per density | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| number button | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| number button | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 13/18/500/0.1 | [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| arrow button | height | `density.control_height` | 40 | 32 | 28 | [[Icon Button]], [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| arrow button | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Icon Button]], [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| ellipsis | min width | - | 40 | 32 | 28 | [[Pagination]] Sizing and density | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| dot | min width | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[ADR-0002 Desktop density levels and target sizes]] (hit area) | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| dot | min height | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[ADR-0002 Desktop density levels and target sizes]] (hit area) | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| dot | height | - | 8 | 8 | 6 | [[Pagination]] Sizing and density (mark), design choice, proposed ADR: pagination gaps and dots per density | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| dot | corner radius | `shape.full` | 4 | 4 | 3 | [[Shape]] (circle) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| dot, other | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Roles]], [[Pagination]] States (the mark is a fill; the role is the mark colour) | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |

## Layout and overflow

- The control is as wide as its controls and never wraps. A place narrower than the full number form (up to 10 controls) switches to the compact form; narrower than previous plus summary plus next, the summary shrinks with an ellipsis and the arrows stay ([[10 Layout Overflow and Scrolling]]).
- A page number never truncates; its button grows with its digits.
- The dot form never exceeds 10 dots; more pages switch to the compact form.
- Pagination sits at the end of the content it pages (below a list or table, aligned to the end) or centred under a carousel. It does not scroll with the content it pages.

## Behaviour

- Pointer: a click on a number goes to that page; previous and next step by one; a press, move out, release changes nothing; the page change takes effect once per activation.
- Keyboard ([[Keyboard Navigation]]): the control is one Tab stop (a roving group, horizontal): Tab enters on the current page, Left and Right move between enabled controls (previous, numbers, next) without wrap, Home and End go to the first and last control, Enter and Space activate. Disabled controls are skipped. After activation focus stays on the control that was activated; if that control is now an ellipsis position or removed by windowing, focus moves to the current page's button. tess-ui makes every control a Tab stop (the roving group is a Tesserae choice, [[Toolbar]] rule).
- Page Up and Page Down are not bound by the control; the content region owns them.
- Touch: tap; swipe on a carousel belongs to [[Carousel]].

## Tooltip and overlay behaviour

Previous and next carry plain tooltips ("Previous page", "Next page") on the icon buttons ([[ADR-0004 Tooltip rule]], [[Tooltip]]); number buttons need none, a dot carries its name ("Page 3") as a tooltip on the dot. The container and the summary carry none. No overlay.

## Motion

The current-page fill changes with the layer fade (`short3`, 150 ms); a page change redraws the slots at once without sliding; dots do not animate between pages unless the carousel does. Reduced motion: no change needed.

## Accessibility

- Role: `group` named "Pagination" (the engine has no `navigation` role, `tre:docs/reference/node.md`; WAI-ARIA recommends a `navigation` landmark with a label, candidate request); children are buttons.
- Names: "Previous page", "Next page", "Page n" for each number and dot; the current one has `current` set to `page` ([WAI-ARIA `aria-current`](https://www.w3.org/TR/wai-aria-1.2/#aria-current)); the summary text "3 of 12" is the visible name of the position.
- Announcements: when the page changes, one polite announcement "Page n of N" is made by the control (not by the focused button, whose name does not change); the compact summary is a polite live region; the ellipsis is hidden; repeating the same page announces nothing ([[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]], [[14 Accessibility Basics]]).
- Keys: as in Behaviour. Disabled previous and next are announced as disabled and take no input.
- Contrast: label on container and on surface at least 4.5 to 1; dots at least 3 to 1 against the surface (WCAG 2.2 SC 1.4.3, 1.4.11).
- The focus ring is not clipped ([[Focus Ring]]).

## Dark and light

All roles follow the scheme ([[Theme Following the System]]); contrast criteria run in both.

## Defaults

Numbers form, page 1, density per container, windowing as above, previous and next shown. tess-ui defaults: `Page` 1, `Pages` 1, `Compact` false, `Dots` false.

## Acceptance criteria

- [ ] AC-PGN-1 (token test): buttons and arrows 40, 32, 28 dp at default, compact, dense; gaps 4, 4, 2 dp; dot hit area 24 dp and mark 8, 8, 6 dp; arrow icons 24, 20, 20 dp. Pass: values equal.
- [ ] AC-PGN-2 (scripted input): with `Pages` 12 the shown list for current page 1, 4, 6, 9 and 12 equals `1 2 … 12`, `1 2 3 [4] 5 … 12`, `1 … 5 [6] 7 … 12`, `1 … 8 [9] 10 11 12` and `1 … 11 [12]` (current in brackets); the count of numbers never exceeds 6 and of ellipses 2; with 7 pages or fewer all numbers show. Pass: lists equal.
- [ ] AC-PGN-3 (scripted input): previous is disabled on page 1 and next on the last page (no focus, no pointer, no key) and enabled otherwise; activation changes the page by one and writes it back once. Pass: page and counts equal.
- [ ] AC-PGN-4 (scripted input): the control is one Tab stop; Tab enters on the current page; Left, Right, Home, End move among enabled controls without wrap; Enter and Space activate once; focus after activation is on the activated control or the current page's button. Pass: focus owner equals at each step.
- [ ] AC-PGN-5 (AT tree assertion): the container is a `group` named "Pagination" (a `navigation` role when the engine has one); previous and next are buttons named "Previous page" and "Next page" with `disabled` set at the ends; each number and dot is a button named "Page n"; exactly one has `current` equal to `page`; ellipses are absent from the tree. Pass: all equal.
- [ ] AC-PGN-6 (scripted input): changing the page raises exactly one polite announcement "Page n of N"; activating the current page raises none; the compact summary text equals "n of N". Pass: announce queue equals.
- [ ] AC-PGN-7 (geometry check): every control's hit area is at least 24 dp by 24 dp (48 dp in a touch context) and hit areas do not overlap. Pass: bounds at or above limits, zero intersection.
- [ ] AC-PGN-8 (geometry check): in a place too narrow for the numbers form the control uses the compact form; a summary wider than its space ends with an ellipsis and the arrows stay; no pixel lies outside the container. Pass: form and pixels equal.
- [ ] AC-PGN-9 (token test): current page container `primary` and label `on_primary`; other numbers label `primary`; ellipsis `on_surface_variant`; dots `primary` and `outline`; state layers 8, 10, 10 percent; disabled 38 percent. Pass: role references and values equal.
- [ ] AC-PGN-10 (contrast script): in light, dark and high contrast, labels on their containers at least 4.5 to 1 and a non-current dot mark against the surface at least 3 to 1. Pass: ratios at or above limits.
- [ ] AC-PGN-11 (pixel check): the current page differs from the other numbers and from a disabled arrow by a filled container, not colour alone (greyscale render). Pass: renders differ.
- [ ] AC-PGN-12 (geometry check): the dot form with more than 10 pages is refused or shows the compact form; with 10 pages or fewer it shows one dot per page. Pass: form equals.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Pagination_View.tdl`, `tess-ui:src/tess_ui/views/Pagination_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py`, `tess-ui:docs/components/pagination.md` | partly meets. Previous and next with names, disabled at the ends, windowing with an ellipsis and the single-page stretch rule, current filled with `current: page`, compact "3 of 12" with `Live: polite`, dots with 24 dp hit area and 8 dp mark, numbers named "Page n", ellipsis hidden (AC-PGN-2 meets by reading, AC-PGN-3 meets by reading, AC-PGN-5 partly: `group`). Fails: no density (Button size `s`, arrows default, AC-PGN-1); every control is a Tab stop, not one roving stop (AC-PGN-4); no page-change announcement except in the compact form (AC-PGN-6); dots `outline_variant` (AC-PGN-10 unmeasured, expected to fail); no narrow-place switch (AC-PGN-8); no 10-dot cap (AC-PGN-12); the ellipsis slot is a fixed 40 dp; the Python widget (`pagination()`) has 40 dp circles and `max_visible` 7 with a 0-based current; `COMPONENT_LIST.md` still says Python only |
| tess-ui | `tess-ui:apps/`, `tess-ui:examples/` | not used: no app or example uses pagination |
| tess-shell | none | absent |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no pagination component | desktop result sets need a page control | none (Tesserae element) |
| Heights 40, 32, 28 dp and dot hit area 24 dp | desktop density and target size | [[ADR-0002 Desktop density levels and target sizes]] |
| One Tab stop with arrow keys, Home and End | desktop keyboard-first; same group rule as [[Toolbar]] | none |
| Non-current dots in `outline` (3 to 1) rather than a lower-contrast role | WCAG 2.2 SC 1.4.11 | none |
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |

## Sources

- No MD3 pagination: the nearest patterns are the carousel page indicator and the text and filled buttons ([[Button]]); the m3.material.io pages could not be fetched #needs-verification.
- [WAI-ARIA 1.2 `aria-current`](https://www.w3.org/TR/wai-aria-1.2/#aria-current): value `page` marks the current item of a set of links or buttons.
- [WAI-ARIA Authoring Practices: toolbar](https://www.w3.org/WAI/ARIA/apg/patterns/toolbar/): the roving group rule reused here.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.3, 1.4.11, 2.5.8, 4.1.3.
- Code: `tess-ui:docs/components/pagination.md`, `tess-ui:src/tess_ui/views/Pagination_View.tdl`, `tess-ui:src/tess_ui/views/Pagination_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py`.
