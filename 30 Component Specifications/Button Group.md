---
title: Button Group
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, action, expressive]
related: ["[[Button]]", "[[Icon Button]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[Split Button]]", "[[Segmented Button]]", "[[Menu]]", "[[Toolbar]]", "[[10 Layout Overflow and Scrolling]]"]
depends_on: ["[[Button]]", "[[Colour Roles]]", "[[Shape]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Button Group

> [!info] Summary
> A set of related [[Button]]s laid out together: the Material Design 3 Expressive [button group](https://m3.material.io/components/button-groups/overview), standard (spaced) or connected (2 dp apart, joined corners), as a row of actions, a choice of one, or a set of toggles. Adopted as a named Expressive element ([[ADR-0006 MD3 baseline with named Expressive adoptions]]). Source of truth in code: see Status in code.

## Purpose

Makes related buttons read as one set with an even gap and, in the choice modes, as one control: view switches (Day, Week, Month), text styles (Bold, Italic), related actions (Copy, Paste).

## When to use and not

- Use when: two to five related buttons share size and variant; the set offers a mode choice that shows in the button state.
- Do not use when: the choice is a form value in a dense form (use a [[Segmented Button]] or a radio group); a default action plus alternatives (use a [[Split Button]]); more than five items (use a [[Menu]] or the overflow button below).
- Segmented versus connected group: the [[Segmented Button]] is the baseline 2022 control; a connected group in `single` or `multiple` mode is its Expressive successor and has the same semantics. A view uses one of them, not both, for the same kind of choice.

## Anatomy

1. Group container (no paint of its own).
2. Buttons, each a [[Button]] (label, optional icon) of one variant and size.
3. Gap: 8 dp standard, 2 dp connected (4 dp inner corners in tess-ui).
4. Overflow button (optional), an [[Icon Button]] with the more icon that opens a [[Menu]] of the buttons that did not fit (Android `overflowMode` menu).

## Variants

| Variant | Gap | Corners |
|---|---|---|
| Standard | 8 dp (design choice; Android default 12 dp #needs-verification) | each button keeps its own full corners |
| Connected | 2 dp | outer corners of the first and last button `full`, inner corners 4 dp (tess-ui; Android connected style: 8 dp) #needs-verification |

Modes (what the buttons mean): `none` (actions), `single` (one chosen), `multiple` (any number chosen). Orientation: horizontal or vertical (a column, the corners swap to top and bottom). Variants of each button: filled, tonal, elevated, outlined, text, as [[Button]]; a connected `single` or `multiple` group uses the [[Button]] toggle form (tess-ui `Toggle`: container and shape swap while selected).

## States

Each button has the states of [[Button]] (hover 8, focus 10, pressed 10 percent; disabled 38 and 12 percent). Group states:

| State | Visual change |
|---|---|
| Selected button (single, multiple) | toggle colours and shape of [[Button]]; `pressed` true |
| Pressed button | the pressed button widens by 15 percent and its neighbours give way by the same total width (Android `childSizeChange` 15 percent in pressed state); the group's overall width stays constant (Expressive, #needs-verification for the spec's number) |
| Group disabled | every button disabled; one disabled button does not disable the others |

## Tokens used

As [[Button]] ([[Colour Roles]], [[Shape]], [[Typography]], [[Elevation]]); [[Spacing and Density]] for the gap; [[Motion]] for the widening.

## Sizing and density

Heights are those of [[Button]] ([[ADR-0002 Desktop density levels and target sizes]]): 40, 32, 28 dp at default, compact, dense; the Expressive sizes XS to XL (32, 40, 56, 96, 136 px in tess-ui) apply at default only, as for [[Button]].

| Level | Standard gap | Connected gap | Inner corner (connected) | Overflow button |
|---|---|---|---|---|
| default | 8 | 2 | 4 | 40 by 40 |
| compact | 8 | 2 | 4 | 32 by 32 |
| dense | 4 | 2 | 4 | 28 by 28 |

- All buttons in a group share one height. A button's width is its content width plus its [[Button]] padding; equal widths (flexible) are an author option.
- The hit areas never overlap; in a connected group the 2 dp gap is in neither (at least 24 by 24 dp each, the Button rule).
- The label of each button is vertically centred as in [[Button]].

## Dimensions and defaults

The group paints nothing and adds no padding; every button follows [[Button]]. The dense standard gap and the connected inner corner are design choices (#needs-verification-as-design-choice).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| group container, buttons | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| button | min width | - | 64 | 48 | 48 | as [[Button]]; [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| button | min height | `target.min` | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8, [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| button (touch hit area) | min height | `target.touch` | 48 | 48 | 48 | [[Spacing and Density]], touch context only | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| group container | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | the group has no paint of its own, [[Button Group]] Anatomy | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| button (no icon) | padding | `space.*` | 0 24 0 24 | 0 16 0 16 | 0 12 0 12 | as [[Button]]; [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| group container | margin | - | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | N/A: the parent container sets the outer space | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| buttons (standard) | gap | `space.3` | 8 | 8 | 4 | [[Button Group]] Sizing; design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| buttons (connected) | gap | `space.1` | 2 | 2 | 2 | [[Button Group]] Sizing, [Android ButtonGroup](https://github.com/material-components/material-components-android/blob/master/docs/components/ButtonGroup.md) | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| button (icon to label) | gap | `density.icon_label_gap` | 8 | 8 | 4 | as [[Button]], [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| group container | border width | - | 0 | 0 | 0 | the group draws no border; each button draws its own as [[Button]] | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| button (outlined variant) | border width | - | 1 | 1 | 1 | as [[Button]] | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| group container | border color | - | N/A: the group draws no border; border is the button's | N/A: the group draws no border; border is the button's | N/A: the group draws no border; border is the button's | [[Button Group]] Anatomy | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| button (outlined variant) | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| button (standard, and outer corners when connected) | corner radius | `shape.full` | 20 | 16 | 14 | [[Shape]] (half the height) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| button (connected inner corners) | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]]; design choice, [[ADR-0006 MD3 baseline with named Expressive adoptions]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| button label | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height, letter_spacing) |
| button icon | icon size | - | 18 | 18 | 16 | as [[Button]], [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| overflow button | height | `density.icon_button_container` | 40 | 32 | 28 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| overflow button | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Spacing and Density]], [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| group container, buttons | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]]; an elevated-variant button rests at level 1 as [[Button]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| focus ring (each button) | border width | - | 3 | 3 | 3 | [[Focus Ring]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring (each button) | border color | `secondary` | `secondary` | `secondary` | `secondary` | [[Focus Ring]] | tess-ui: via App(focus_ring=) ring colour argument; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring (each button) | margin | - | 2 2 2 2 | 2 2 2 2 | 2 2 2 2 | [[Focus Ring]] (offset outside the button) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |

## Layout and overflow

- A group wider than its region wraps only when standard; a connected group never wraps. Instead the buttons that do not fit move to the overflow button's [[Menu]], from the end, keeping order; a button in a `single` or `multiple` group that is selected and overflowed shows its selection in the menu item ([[10 Layout Overflow and Scrolling]]).
- Labels do not wrap: ellipsis per button with the full label as the tooltip on that button.
- The group never draws outside its region and buttons never overlap.

## Behaviour

- Pointer: each button as [[Button]]; in `single` a press selects that button (no deselect by pressing the selected one); in `multiple` a press toggles it; in `none` a press runs the action.
- Keyboard: Tab and Shift+Tab move over the group as follows. `single`: one Tab stop (the selected button, or the first when none), Left and Right (Up and Down in a column) move focus and selection together, wrapping at the ends, skipping disabled buttons; Space selects. `multiple`: each button its own Tab stop (WAI-ARIA toggle button semantics), Enter and Space toggle; the arrows also move focus. `none`: each button its own Tab stop; the arrows do not move focus (ordinary actions). The tess-ui build uses one Tab stop for every mode (design difference, see Status).
- Touch: tap per button; hit areas 48 dp high in touch contexts.

## Tooltip and overlay behaviour

Tooltips only on a button whose label is truncated or hidden (icon-only buttons need one), never on the group ([[ADR-0004 Tooltip rule]]). The overflow menu is a [[Menu]] ([[Popup]]); focus returns to the overflow button on close.

## Motion

Pressed widening and neighbour give-way: 100 ms ease; selected shape and colour change `short3` 150 ms #needs-verification; reduced motion: instant.

## Accessibility

- Role: `single`: `radiogroup` with children `radio` (checked from selection); `multiple`: `group` with children `button` having `pressed`; `none`: `group` with children `button`. The group has a name when the surrounding context does not name it ([WAI-ARIA radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/), [button](https://www.w3.org/TR/wai-aria-1.2/#button)).
- Name of each button: its label; an icon-only button has the label as name ([[Icon Button]] rule).
- Overflow button: name "More", `haspopup` menu, `expanded`.
- Selection is exposed by state, not by colour alone: selected buttons also differ by shape (connected) or check (variant dependent), at least 3 to 1 against the unselected container (WCAG 1.4.11).

## Dark and light

As [[Button]]; AC-BTG-9 runs in both.

## Defaults

Mode none, variant filled, size small (40 dp), standard gap, horizontal, not connected.

## Acceptance criteria

- [ ] AC-BTG-1 (token test): gap 8 (4 at dense) standard and 2 connected; connected inner corners 4 dp, outer `full`; button heights equal [[Button]] at each density. Pass: values equal.
- [ ] AC-BTG-2 (geometry check): all buttons share one height; hit areas are at least 24 by 24 dp, do not overlap, and no button lies outside the group's region. Pass: heights equal, overlap 0, bounds inside.
- [ ] AC-BTG-3 (scripted input): `single`: one Tab stop; Right then Left move focus and selection with wrap; a disabled button is skipped; Space selects; pressing the selected button leaves it selected. Pass: selection and focus sequence equal.
- [ ] AC-BTG-4 (scripted input): `multiple`: every button is a Tab stop; Enter and Space toggle exactly one button; result list equals toggled values. Pass: lists equal.
- [ ] AC-BTG-5 (scripted input): `none`: every button is a Tab stop; a press or Enter runs that action once and records its value. Pass: counts and value equal.
- [ ] AC-BTG-6 (AT tree assertion): `single` exposes `radiogroup` with `radio` children and `checked` equal to the selection; `multiple` exposes `group` with `button` children and `pressed`; `none` exposes `group` with `button` children; names are non-empty. Pass: all equal.
- [ ] AC-BTG-7 (geometry check): a group narrower than its content shows an overflow button, the hidden buttons are in its menu in order, and no button is clipped. Pass: visible plus menu items equal the item list, clipped pixels 0.
- [ ] AC-BTG-8 (geometry check): while a button is pressed it widens by 15 percent and the group width changes by at most 1 dp. Pass: width ratio 1.15 ±0.02, group width change at most 1 dp.
- [ ] AC-BTG-9 (contrast script): light and dark, label on container at least 4.5 to 1; selected against unselected container at least 3 to 1 or a second non-colour cue present. Pass: ratios at or above limits.
- [ ] AC-BTG-10 (scripted input): icon-only buttons show a tooltip with the label on hover; the group itself never shows one; a press hides it. Pass: tooltip text equal.
- [ ] AC-BTG-11 (review): a view uses a connected group or a segmented button for one kind of choice, not both. Pass: review.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/ButtonGroup_View.tdl`, `tess-ui:src/tess_ui/widgets/buttons.py` (`button_group`), `tess-ui:docs/components/button-groups.md`, test `tess-ui:tests/test_button_group.py` | partly meets: modes none, single, multiple, `Connected` 2 px gap with 4 px inner corners and full outer corners, vertical orientation, Button toggle with `Selected` (AC-BTG-1 partly: heights are Button's, gap 8 at every density; AC-BTG-3 meets by reading for `single`, but the group uses one Tab stop for `multiple` and `none` too: AC-BTG-4 and AC-BTG-5 fail), group role only, no `radiogroup`, `radio` or `pressed` roles stated (AC-BTG-6 fails or unverified), pressed widening and overflow button not built (AC-BTG-7, AC-BTG-8 fail), icon-only tooltips not set (AC-BTG-10 unverified), no density |
| tess-ui | `tess-ui:src/tess_ui/views/ButtonGroup_View.tdl` dimensions | differs: standard gap 8 at every density (spec 4 at dense; AC-BTG-1); overflow button absent (AC-BTG-8) |
| tess-shell | none found | absent |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Button group (standard and connected) adopted though Expressive | needed for the choice and action sets | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Gap 8 dp standard (4 dp dense); Android default is 12 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Heights 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Per-mode Tab stops (single: one, others: each) | desktop keyboard-first and APG | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- [Material Components Android ButtonGroup](https://github.com/material-components/material-components-android/blob/master/docs/components/ButtonGroup.md): standard and connected groups, sizes XS to XL, standard spacing 12 dp default, connected 2 dp spacing with 8 dp inner corners and full outer corners, child size change 15 percent when pressed, overflow mode with a 3-dot icon.
- [Material Components Android SplitButton](https://github.com/material-components/material-components-android/blob/master/docs/components/SplitButton.md).
- [WAI-ARIA APG radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/); [WAI-ARIA 1.2 button](https://www.w3.org/TR/wai-aria-1.2/#button) (pressed); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.3, 1.4.11, 2.5.8.
- Code: `tess-ui:docs/components/button-groups.md`. Material Web has no button group component; the m3.material.io page could not be fetched.
