---
title: Split Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, action, expressive]
related: ["[[Button]]", "[[Icon Button]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[Menu]]", "[[Popup]]", "[[Button Group]]", "[[12 Overlays]]"]
depends_on: ["[[Button]]", "[[Colour Roles]]", "[[Shape]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Menu]]"]
---

# Split Button

> [!info] Summary
> A main action joined to a menu button that opens related actions: the Material Design 3 Expressive [split button](https://m3.material.io/components/split-button/overview), a specialised connected [[Button Group]] of a [[Button]] and a menu button. Adopted as a named Expressive element ([[ADR-0006 MD3 baseline with named Expressive adoptions]]). Source of truth in code: see Status in code.

## Purpose

Runs the usual action with one press (Send, Save) and offers the variants of it (Send later, Save as draft) in a menu without a second control.

## When to use and not

- Use when: one action is the default and two to seven related alternatives exist.
- Do not use when: the alternatives are unrelated (use a [[Menu]] on an [[Icon Button]]); there is no default action (use a [[Button]] that opens a [[Menu]]); the choice persists as a state (use a [[Segmented Button]]).

## Anatomy

1. Main button: label (`label_large`) and an optional leading icon, a [[Button]] of the same variant.
2. Gap between the two buttons, 2 dp.
3. Trailing menu button: a chevron (18 dp at default and compact, 16 dp at dense), an icon-only [[Button]] of the same variant.
4. Menu: a [[Menu]] anchored below the trailing button, opened by it ([[Popup]]).
5. State layers and focus rings, one per button ([[State Layers]], [[Focus Ring]]).

## Variants

Filled, tonal, elevated, outlined, text: exactly the [[Button]] variants, both parts use the same one. Elevation, container, label and outline roles are the Button table. Forms: action-and-menu (the default); toggle form where the trailing button is checkable (Android: the trailing button is checkable with an animated chevron) is the same as the "menu open" state below and has no separate selected colour #needs-verification.

## States

Each button has the states of [[Button]] (rest, hover 8, focus 10, pressed 10 percent, disabled 38 and 12 percent), independently.

| State | Visual change |
|---|---|
| Menu open | the trailing button shows the pressed look held while the menu shows; its chevron is turned over (180 degrees); its corners are fully round on all four ([[Shape]] `full`) |
| Disabled | both parts disabled together; a split button with a disabled main part only is not allowed (disable the whole control, or hide the control) |
| Loading | the main button may show the Button loading state; the trailing button is disabled meanwhile |

Corner shape at rest: outer corners `full`, inner corners 4 dp (tess-ui). Material Components Android defaults `innerCornerSize` to none and spacing to 2 dp; the connected group uses 8 dp inner corners; Tesserae takes 4 dp #needs-verification.

## Tokens used

[[Colour Roles]] and [[Elevation]] from [[Button]]; [[Shape]] (`full`, 4 dp inner = `extra_small`); [[Motion]] (chevron turn and corner change 100 ms, `short3` 150 ms for the layer #needs-verification); [[Spacing and Density]].

## Sizing and density

MD3 (Android docs): five sizes XS to XL like label buttons, gap between the two buttons 2 dp ([Material Components Android SplitButton](https://github.com/material-components/material-components-android/blob/master/docs/components/SplitButton.md): `spacing` default 2dp). The trailing width per size is not published in the sources reachable to the tools #needs-verification.

Tesserae by density; the control heights follow [[Button]] and [[ADR-0002 Desktop density levels and target sizes]]; the trailing widths are design choices:

| Level | Height | Main padding (no icon; with icon leading, trailing) | Trailing button width | Chevron | Gap |
|---|---|---|---|---|---|
| default | 40 | 24; 16, 24 | 48 | 18 | 2 |
| compact | 32 | 16; 12, 16 | 40 | 18 | 2 |
| dense | 28 | 12; 8, 12 | 32 | 16 | 2 |

- Both buttons have the same height; the pair's overall width is main width plus 2 dp plus trailing width. Sizes xs to xl of tess-ui (32, 40, 56, 96, 136 px) are the Expressive sizes of [[Button]], valid at default only.
- The trailing button's hit area is at least 24 by 24 dp (it is at least 32 by 28 dp) and 48 dp high in touch contexts. The two hit areas do not overlap; the 2 dp gap belongs to neither.
- Label vertically centred as for [[Button]].

## Layout and overflow

- The main label is one line with an end ellipsis; the trailing button keeps its width. The full label is the name and the tooltip of the main button.
- The menu follows [[Menu]] and [[12 Overlays]]: it opens below the trailing button, flipped above when it does not fit, its width at least the width of the whole split button, with a scroll when taller than the window ([[10 Layout Overflow and Scrolling]]).
- A row that runs out of width moves the split button last, as a [[Button]] with the same menu ([[Button]] Layout rule).

## Behaviour

- Pointer: press on the main part runs the action once; press on the trailing part toggles the menu; a press outside or Escape closes the menu; a press dismisses the tooltip.
- Keyboard: Tab reaches the main button, then the trailing button (two Tab stops). On either: Enter and Space press it; Down opens the menu and moves focus to its first row; Up on the trailing button opens it and focuses the last row ([WAI-ARIA APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/)). A press by pointer opens the menu without moving focus into it. Escape closes the menu and returns focus to the trailing button. Choosing a row runs its action, closes the menu and returns focus to the trailing button.
- Touch: tap on the hit areas.

## Tooltip and overlay behaviour

Tooltips only on the buttons: the trailing button shows "More options for {label}" (a tooltip on the control, [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]); the main button has one only for a truncated label. No tooltip on the group. The tooltip closes when the menu opens. The menu is a [[Menu]] popup; focus returns to the trailing button on close ([[Popup]]).

## Motion

Chevron rotates 180 degrees over 100 ms and the trailing corners change at the same time; reduced motion: instant. State layer and elevation as [[Button]].

## Accessibility

- Role of the container: `group` named with the main label. Main part: role `button`, name = label. Trailing part: role `button`, `haspopup` menu, `expanded` true while the menu shows, name "More options for {label}" (WCAG 2.5.3: the name does not need to repeat visible text because the trailing button shows none).
- The menu follows the accessibility of [[Menu]] (role `menu`, items `menuitem`).
- Contrast, focus ring: as [[Button]]; each button's ring is not clipped by its neighbour (the 2 dp gap and the ring offset overlap by design: the ring of the focused button draws on top).

## Dark and light

As [[Button]]; AC-SPB-9 runs in both.

## Defaults

Variant filled, size at the container's density, menu placement below. No toggle form.

## Acceptance criteria

- [ ] AC-SPB-1 (token test): heights 40, 32, 28 dp at default, compact, dense for both buttons; paddings, trailing widths 48, 40, 32 and chevron sizes equal the Sizing table. Pass: values equal.
- [ ] AC-SPB-2 (geometry check): the gap between main and trailing button is 2 dp at every density and the two hit areas do not overlap. Pass: gap 2 dp, overlap 0.
- [ ] AC-SPB-3 (token test): outer corners `full`, inner corners 4 dp at rest; with the menu open the trailing button has `full` on all four corners and the chevron is rotated 180 degrees. Pass: values equal.
- [ ] AC-SPB-4 (token test): variant roles and state layer opacities (8, 10, 10; disabled 38 and 12 percent) equal those of [[Button]] on each part. Pass: values equal.
- [ ] AC-SPB-5 (scripted input): Tab order is main, trailing; Enter and Space on main: 1 action, no menu; Enter and Space on trailing: menu opens; Down on either opens the menu with the first row focused; Escape closes and focus is on the trailing button; choosing a row closes the menu and sets the chosen value once. Pass: sequence outcomes equal.
- [ ] AC-SPB-6 (AT tree assertion): container role `group` named by the label; main role `button`; trailing role `button` with `haspopup` menu, `expanded` equal to the menu state and a non-empty name. Pass: all equal.
- [ ] AC-SPB-7 (geometry check): the main label line box is vertically centred (offset at most 0.5 dp) at each density; a label longer than the available width shows an ellipsis and the trailing button keeps its width. Pass: offset at most 0.5 dp, ellipsis present, widths equal.
- [ ] AC-SPB-8 (scripted input): a pointer press on the trailing button opens the menu without moving focus into it; a press outside closes it; opening the menu closes any tooltip; hover over the trailing button shows a tooltip; no tooltip appears over the group gap. Pass: events equal.
- [ ] AC-SPB-9 (contrast script): light and dark, label on container at least 4.5 to 1, chevron on container at least 3 to 1, outline at least 3 to 1 for the outlined variant. Pass: ratios at or above limits.
- [ ] AC-SPB-10 (geometry check): the menu opens below the trailing button, is flipped above when below does not fit, is at least as wide as the whole split button and lies fully inside the window. Pass: bounds as stated.
- [ ] AC-SPB-11 (pixel check): under keyboard focus the focused part shows the ring 3 dp wide, 2 dp outside, role `secondary`, drawn over the neighbour. Pass: measured ring equals.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/SplitButton_View.tdl`, `tess-ui:src/tess_ui/widgets/buttons.py` (`split_button`), `tess-ui:docs/components/split-buttons.md`, test `tess-ui:tests/test_split_button.py` | partly meets: two Buttons 2 px apart, outer corners full and inner 4, round trailing while open, chevron swaps up and down (a swap, not a turn), group role, trailing `Expanded` and name "More options for ..." (AC-SPB-2, AC-SPB-3, AC-SPB-6 meet by reading), Tab reaches both, Down opens with focus on first row, press opens without focus (AC-SPB-5, AC-SPB-8 meet by reading; Up on trailing not documented), trailing width equals an icon-only Button of the size, not the table (AC-SPB-1 fails at compact and dense, as Button), tooltip on the trailing button not set (AC-SPB-8 partly), `haspopup` not set (AC-SPB-6 partly), no toggle form, no density |
| tess-shell | none found | absent |
| tre | none | not applicable |

No app or example uses it.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Split button adopted although it is an Expressive component (not in the 2022 baseline) | useful for save and send with variants | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Heights 40, 32, 28 dp and smaller trailing widths | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Two Tab stops and Up/Down menu keys on both parts | desktop keyboard-first | [[ADR-0002 Desktop density levels and target sizes]] |
| Hit area is the container with a 24 dp floor | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- [Material Components Android SplitButton](https://github.com/material-components/material-components-android/blob/master/docs/components/SplitButton.md): new in Expressive, a special type of connected button group; five sizes as label buttons; spacing 2 dp; trailing button checkable with animated chevron; content description for the chevron button.
- [Material Components Android ButtonGroup](https://github.com/material-components/material-components-android/blob/master/docs/components/ButtonGroup.md): connected group spacing 2 dp, inner corners 8 dp.
- [WAI-ARIA APG menu button](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.3, 1.4.11, 2.5.3, 2.5.8.
- Button values: [[Button]]. Code: `tess-ui:docs/components/split-buttons.md`.
- Material Web has no split button component; the m3.material.io page could not be fetched (script-rendered).
