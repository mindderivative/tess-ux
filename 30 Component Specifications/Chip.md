---
title: Chip
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, selection, input, chip]
related: ["[[Button]]", "[[Icon Button]]", "[[Checkbox]]", "[[Radio Button]]", "[[Segmented Button]]", "[[Text Field]]", "[[Tooltip]]", "[[Form Row]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Typography]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Colour Roles]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]", "[[Button]]"]
---

# Chip

> [!info] Summary
> A compact element that starts an action (assist), toggles a filter (filter), shows a value the user entered (input) or offers a reply or next step (suggestion): the Material Design 3 [chips](https://m3.material.io/components/chips/overview), with three density levels and a keyboard model for a group of chips. Source of truth in code: see Status in code.

## Purpose

Show a small, labelled item the user can act on without leaving the context: run a quick action, narrow a list, review and remove entered tags, or accept a suggestion.

## When to use and not

- Use when: the item is short (a word or two); several items sit side by side; the item is a filter, a tag or a shortcut.
- Do not use when: the action is the main action of a form (use [[Button]]); the choice is one of a fixed few on a bar (use [[Segmented Button]]); the item is a setting that applies at once ([[Switch]]); the item is a single yes or no with a label ([[Checkbox]]); the entry is long free text ([[Text Field]]).

## Anatomy

1. Container: a rounded rectangle, 32 dp high at default, corner `small` (8 dp), outline 1 dp `outline_variant` or a raised surface.
2. Leading icon (optional): 18 dp. A selected filter chip shows a check in its place.
3. Avatar (optional, input chip): 24 dp circle with letters or an image.
4. Label: one line in `label_large`.
5. Close button (input chip, optional): an 18 dp icon with a hit area of at least 24 dp wide and the full chip height.
6. State layer: over the whole container, drawn on hover, focus and press ([[State Layers]]).
7. Focus ring: around the container, keyboard focus only ([[Focus Ring]]).

## Variants

| Variant | Use | Selected state | Role | Differences |
|---|---|---|---|---|
| Assist | start an action (add to calendar, share) | none | `button` | optional leading icon in `primary` |
| Filter | narrow a result set | yes: `secondary_container`, check replaces the icon | `checkbox` in a multiple-choice group, `radio` in a single-choice group | selected or not |
| Input | a piece of entered data (a tag, a recipient) | optional | `button` (the chip), `button` (the close) | optional avatar, optional close |
| Suggestion | a generated reply or query | none | `button` | label `on_surface_variant` |
| Elevated (modifier) | the chip sits on a patterned surface | as the variant | as the variant | `surface_container_low` fill, elevation level 1, no outline |

A chip group (`ChipGroup`) holds chips of one kind: assist and suggestion (`none` mode: each chip acts), filter (`single` or `multiple` mode) or input (`input` mode with an entry field after the last chip).

## States

State layer percentages come from [[State Layers]] ([[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]]). The layer colour is the label colour of the state. Colours from the Material Web chip tokens ([assist](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-assist-chip.scss), [filter](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filter-chip.scss), [input](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-input-chip.scss), [suggestion](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-suggestion-chip.scss)):

| State | Container | Outline | Label | Icon |
|---|---|---|---|---|
| Assist, rest | none | 1 dp `outline_variant` | `on_surface` | `primary` |
| Suggestion, rest | none | 1 dp `outline_variant` | `on_surface_variant` | `primary` |
| Filter and input, unselected | none | 1 dp `outline_variant` | `on_surface_variant` | `on_surface_variant` |
| Filter and input, selected | `secondary_container` | none | `on_secondary_container` | `on_secondary_container` |
| Elevated, unselected | `surface_container_low`, level 1 | none | as the variant | as the variant |
| Elevated filter, selected | `secondary_container` | none | `on_secondary_container` | `on_secondary_container` |
| Hover, focus, pressed | as rest | as rest | as rest | layer 8, 10, 10 percent |
| Dragged (reorder, not built) | as rest | as rest | as rest | layer 16 percent |
| Disabled | `on_surface` at 12 percent if selected, else none | 1 dp `on_surface` at 12 percent | `on_surface` at 38 percent | `on_surface` at 38 percent |
| Keyboard focus | as the state | as the state | as the state | focus ring 3 dp, offset 2 dp, role `secondary` |

The suggestion label colour is the value of the latest token set; the v0_192 set was not compared #needs-verification. Selection is never shown by colour alone: a selected filter chip shows the check and loses its outline ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).

## Tokens used

[[Colour Roles]] (roles above), [[Typography]] (`label_large` for the label, `label_medium` for avatar letters), [[Shape]] (container `small` 8 dp, avatar and close `corner-full`), [[Elevation]] (level 1 for elevated), [[Motion]] (colour fade `short3` 150 ms), [[Spacing and Density]], [[State Layers]], [[Focus Ring]].

## Sizing and density

MD3 values (Material Web tokens, all four chip kinds): container height 32 dp, shape `corner-small`, leading icon 18 dp, avatar 24 dp, trailing icon 18 dp, outline 1 dp (0 dp selected); Material Web gives a touch target of 48 dp ([`chips/internal/_shared.scss`](https://github.com/material-components/material-web/blob/main/chips/internal/_shared.scss): `.touch { height: 48px }`); Android: `chipMinHeight` 32 dp and `chipMinTouchTargetSize` 48 dp ([Chip docs](https://github.com/material-components/material-components-android/blob/master/docs/components/Chip.md)). Horizontal padding 16 dp (8 dp beside an icon, avatar or close) and the gap of 8 dp between parts are those of tess-ui's chip stylesheet #needs-verification (not read from the Material Web internals).

Rule: container height is 32 dp at default, 28 dp at compact and 24 dp at dense (the dense row of a list); icon, avatar and close icon scale down with the height.

| Level | Container height | Icon and close icon | Avatar | Padding, no leading part | Padding beside icon, avatar, close | Gap between parts | Gap between chips |
|---|---|---|---|---|---|---|---|
| default | 32 dp | 18 dp | 24 dp | 16 dp | 8 dp | 8 dp | 8 dp |
| compact | 28 dp | 18 dp | 20 dp | 12 dp | 8 dp | 8 dp | 8 dp |
| dense | 24 dp | 16 dp | 18 dp | 8 dp | 4 dp | 4 dp | 4 dp |

The compact and dense rows are Tesserae design choices #needs-verification-as-design-choice.

- Pointer target: the whole container, at least 24 by 24 dp at every level ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)). In a touch context the hit area is 48 dp high, centred, without overlapping a neighbouring chip's hit area.
- The close button of an input chip has its own hit area: at least 24 dp wide and the full container height, inside the container; the painted icon is smaller than the hit area. The label's hit area ends where the close hit area begins.

## Dimensions and defaults

Container, icon, avatar, outline and shape come from the Material Web chip tokens (all four kinds); padding and gaps are the tess-ui chip stylesheet values; compact and dense are Tesserae choices (#needs-verification-as-design-choice).

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | 32 | 28 | 24 | [md-comp-filter-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filter-chip.scss); compact and dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | min width | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| container | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| container | padding | `space.5` | 0 16 0 16 | 0 12 0 12 | 0 8 0 8 | tess-ui:src/tess_ui/views/Chip_Stylesheet.tdl (no leading part); compact and dense: design choice, proposed ADR: chip paddings | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container (leading icon or avatar) | padding | `space.3` | 0 16 0 8 | 0 12 0 8 | 0 8 0 4 | tess-ui:src/tess_ui/views/Chip_Stylesheet.tdl (8 beside the leading part); compact and dense: design choice, proposed ADR: chip paddings | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container | margin | - | N/A: the chip group or parent sets the outer space | N/A: the chip group or parent sets the outer space | N/A: the chip group or parent sets the outer space | [[Spacing and Density]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| container | gap | `space.3` | 8 | 8 | 4 | tess-ui:src/tess_ui/views/Chip_Stylesheet.tdl (between parts); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| chip group | gap | `space.3` | 8 | 8 | 4 | tess-ui:src/tess_ui/views/ChipGroup_View.tdl (between chips and between wrapped rows); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| container | border width | - | 1 | 1 | 1 | [md-comp-filter-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filter-chip.scss) (0 when selected or elevated) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| container | border color | `outline_variant` | `outline_variant` | `outline_variant` | `outline_variant` | [md-comp-assist-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-assist-chip.scss) | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container | corner radius | `shape.small` | 8 | 8 | 8 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| container | elevation | `elevation.level0` | 0 | 0 | 0 | [md-comp-filter-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filter-chip.scss) (flat; the elevated modifier is level 1) | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| container (elevated) | elevation | `elevation.level1` | 1 | 1 | 1 | [md-comp-filter-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filter-chip.scss) | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| label | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| leading icon | icon size | - | 18 | 18 | 16 | [md-comp-filter-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filter-chip.scss); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| avatar | height | - | 24 | 20 | 18 | [md-comp-input-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-input-chip.scss); compact and dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| avatar | corner radius | `shape.full` | 12 | 10 | 9 | [[Shape]] (half of the avatar) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| avatar | font | `label_medium` | 12/16/500/0.5 | 12/16/500/0.5 | 12/16/500/0.5 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| close button | height | - | 32 | 28 | 24 | [[Chip]], Sizing and density (the full container height) | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| close button | min width | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.5.8 | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| close button | icon size | - | 18 | 18 | 16 | [md-comp-input-chip](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-input-chip.scss); dense: design choice, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| close button | corner radius | `shape.full` | 16 | 14 | 12 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |

## Layout and overflow

- The label is one line. A chip is as wide as its parts, with a maximum width of 256 dp; a longer label truncates with an ellipsis at the end ([[10 Layout Overflow and Scrolling]]) and the full label appears in the chip's tooltip.
- The icon, avatar and close button keep their size and are vertically centred in the container; the label text is centred by its line box (AC-DEN-9 in [[Spacing and Density]]).
- A chip group wraps onto new rows; the row gap equals the chip gap. A group never scrolls sideways (a horizontally scrolling group is a separate request) and a chip that is wider than the group truncates its label to the group width.
- In `input` mode the entry field follows the last chip in the same wrapping flow and takes at least 96 dp.

## Behaviour

- Pointer: press shows the pressed layer; release inside the chip runs the action once (assist, suggestion), toggles the selection once (filter) or does the input chip's primary action (usually edit or select); leaving before release cancels. A press on the close button of an input chip removes the chip and does not press the chip.
- Keyboard, one chip: Space and Enter activate the focused chip (a filter chip toggles). Delete or Backspace on a focused input chip removes it. Tesserae rule: Material Web gives no key for removal #needs-verification.
- Keyboard, group (roving focus):
  - The group is one Tab stop; Tab enters on the chip that was last focused, else the first enabled chip, and the next Tab leaves the group.
  - Left Arrow and Right Arrow move focus to the previous and next enabled chip (Material Web chip set: Left, Right, Home, End); Up Arrow and Down Arrow also move along the visual order in tess-ui; Home and End move to the first and last chip. Focus does not wrap.
  - In `single` mode moving the focus also chooses the chip (as a radio group, [[Radio Button]]); in `multiple` mode focus does not change the selection.
  - After Delete removes an input chip, focus moves to the next chip, else the previous, else the entry field.
  - In `input` mode, Enter in the entry field adds a chip with the typed text when it is not empty and not already present, then clears the field.
  - Disabled chips are skipped (soft-disabled chips that stay focusable are optional per Material Web `soft-disabled`).
- Touch: tap on the 48 dp hit area acts like a press.
- Events: assist and suggestion fire one action event per activation; filter fires one change event per toggle; input fires one removal event per removal and one add event per addition; setting the selection from code raises no event.

## Tooltip and overlay behaviour

Per [[ADR-0004 Tooltip rule]] the tooltip belongs to the control, never to the group.

- A chip may carry one tooltip, on the container; when its label is truncated the tooltip shows the full label.
- The close button carries its own tooltip "Remove {label}" and hovering it shows that tooltip only.
- A press dismisses the tooltip; none returns until the pointer leaves, re-enters and 500 ms pass. Keyboard focus shows it at once ([[Tooltip]]).
- A chip opens no overlay; a filter chip with a menu (dropdown filter) is not specified here.

## Motion

Colour and background fade `short3` 150 ms (tess-ui `Chip_Stylesheet.tdl`: `Transition { Background: 150 }`); elevation changes `short4` 200 ms ([[Motion]]). Reduced motion: state changes in one frame ([[14 Accessibility Basics]]).

## Accessibility

- Role: assist, suggestion and input chips are `button`; a filter chip is `checkbox` with `checked` in a `multiple` group and `radio` with `checked` in a `single` group; the group is `group` (multiple, none, input) or `radiogroup` (single) with a name ([[Accessibility Rules]]).
- Name: the label; an avatar and icon are hidden from assistive technology unless they carry meaning; the close button is a `button` named "Remove {label}"; Material Web adds `aria-label` to chips whose label needs more context ([chip docs](https://github.com/material-components/material-web/blob/main/docs/components/chip.md)).
- State: a selected filter chip exposes `checked` true; a disabled chip is exposed as disabled.
- Announcement: removal of an input chip announces "{label} removed" through a polite live region ([[14 Accessibility Basics]]); adding announces "{label} added".
- Contrast: label against the container at least 4.5 to 1; outline `outline_variant` is decorative (selection and focus carry the state); the focus ring at least 3 to 1.
- Target sizes as in Sizing and density.

## Dark and light

All roles; follows the scheme ([[Theme Following the System]]). AC-CHP-9 runs in both.

## Defaults

Assist variant; outlined (not elevated); density from the container; no icon, no avatar, not removable; `none` mode for a group.

## Acceptance criteria

- [ ] AC-CHP-1 (token test): container height is 32, 28 and 24 dp, corner 8 dp, outline 1 dp (0 dp selected), icon 18, 18 and 16 dp, avatar 24, 20 and 18 dp at the three levels. Pass: all values equal.
- [ ] AC-CHP-2 (geometry check): padding (16, 12, 8 dp without leading part; 8, 8, 4 dp beside icon, avatar or close), gap between parts (8, 8, 4 dp) and gap between chips (8, 8, 4 dp) at the three levels at scale 1.0 and 2.0. Pass: equal to the dp.
- [ ] AC-CHP-3 (geometry check): the hit area of every chip is at least 24 by 24 dp at every level; the close button's hit area is at least 24 dp wide and the full container height; in a touch context the chip's hit area is at least 48 dp high; close and label hit areas do not overlap. Pass: measured bounds at or above the limits.
- [ ] AC-CHP-4 (token test): colours per the States table for the four variants, selected and unselected, and elevated: container, outline width and colour, label, icon, layer opacities 0.08, 0.10, 0.10, disabled label 0.38 and disabled outline 0.12. Pass: values equal.
- [ ] AC-CHP-5 (scripted input): Space and Enter on a focused assist chip fire one action event; on a filter chip they toggle once and fire one change event; on a disabled chip nothing fires and Tab skips it. Pass: counts and state equal.
- [ ] AC-CHP-6 (scripted input): in a group of four chips with the second disabled: one Tab stop; Right moves 1 to 3; Left moves back; Home and End go to the first and last enabled chip; no wrap at the ends. Pass: the focused chip equals the expected chip each time.
- [ ] AC-CHP-7 (scripted input): in `single` mode, moving focus with the arrows chooses the focused chip and unchooses the previous; in `multiple` mode the arrows change focus only and Space toggles. Pass: selection list equals the expected list.
- [ ] AC-CHP-8 (scripted input): input mode: typing "a" and Enter adds a chip once, clears the field; typing the same text again adds nothing; Delete on a focused chip removes it and moves focus to the next chip, else the previous, else the entry field; a press on the close button removes the chip and does not fire the chip's own press. Pass: chip list, focus owner and event counts equal.
- [ ] AC-CHP-9 (contrast script): light and dark, label against container (`secondary_container` selected, surface unselected, `surface_container_low` elevated): at least 4.5 to 1 in every variant and state; focus ring against the group surface at least 3 to 1. Pass: ratios at or above the limits.
- [ ] AC-CHP-10 (AT tree assertion): assist, suggestion and input chips have role `button` and the label as name; a filter chip has role `checkbox` (multiple) or `radio` (single), `checked` equal to the selection and `disabled` equal to the state; the group has role `group` or `radiogroup` and a name; the close button is a `button` named "Remove {label}". Pass: all equal.
- [ ] AC-CHP-11 (geometry check): a label wider than 256 dp truncates with an ellipsis and the chip is 256 dp wide; the icon and close button stay inside the container; a group wider than its parent wraps to new rows. Pass: widths and wrap rows equal.
- [ ] AC-CHP-12 (scripted input): hover the chip 600 ms: exactly its own tooltip (full label when truncated) is visible, no group tooltip; hover the close button: only its tooltip; a press dismisses it. Pass: visible tooltip count and owner equal.
- [ ] AC-CHP-13 (pixel check): a selected filter chip shows the check in place of the leading icon and has no outline pixels; an unselected one shows a 1 dp outline. Pass: check mask inside the 18 dp icon box; outline pixel counts equal.
- [ ] AC-CHP-14 (scripted input): with reduced motion on, a selection change completes in one frame. Pass: container fill at its final colour in the first frame after the event.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Chip_View.tdl`, `tess-ui:src/tess_ui/views/Chip_Stylesheet.tdl`, `tess-ui:src/tess_ui/views/ChipGroup_View.tdl`, `tess-ui:docs/components/chips.md` | partly meets: 32 dp height, 8 dp corner, `label_large`, 18 dp icon, 24 dp avatar, padding 16 and 8, gap 8, outline 1 dp `outline_variant`, selected `secondary_container`, check replaces icon, elevated level 1, disabled not focusable, one Tab stop with arrows and `single` mode choosing with focus (AC-CHP-4 partly, AC-CHP-5, AC-CHP-7 meet by reading, unrun). Fails: no density (AC-CHP-1, AC-CHP-2 at compact and dense); the close container is 18 by 18 dp, below 24 dp (AC-CHP-3); suggestion label `on_surface`, token value `on_surface_variant` (AC-CHP-4); disabled outline and container 12 percent not set in the stylesheet, only `Disabled` dimming (AC-CHP-4); filter chips in `single` mode are `checkbox`, not `radio`, and the group is `group`, not `radiogroup` (AC-CHP-10); close button named `'Remove ' + label` ✓; no Home and End, no Delete or Backspace removal (AC-CHP-6, AC-CHP-8); no 256 dp maximum width or ellipsis rule (AC-CHP-11); no tooltips (AC-CHP-12); not built: dragging to reorder, sideways scrolling group |
| tess-shell | none | absent |
| tre | none (composed from box and text nodes) | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Container 28 dp at compact and 24 dp at dense (MD3 32 dp) | desktop rows; 24 dp keeps the minimum target | [[ADR-0002 Desktop density levels and target sizes]] |
| Pointer target 24 dp minimum, 48 dp in touch contexts | WCAG 2.2 SC 2.5.8 | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed layer 10 percent; focus ring 3 dp, offset 2 dp, role `secondary` instead of the outline colour change | foundation rule for all controls | [[ADR-0009 State layer percentages]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Delete or Backspace removes a focused input chip; the close button is not a keyboard stop | desktop keyboard-first use; fewer Tab stops | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Single-choice filter chips are `radio` with a `radiogroup`, arrows choose | APG radio group model | [[ADR-0006 MD3 baseline with named Expressive adoptions]] (convention only) |
| Maximum width 256 dp with ellipsis and tooltip | overflow rule of chapter 10 | [[ADR-0004 Tooltip rule]] |

## Sources

- Material Web chip tokens, latest: [assist](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-assist-chip.scss), [filter](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filter-chip.scss), [input](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-input-chip.scss), [suggestion](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-suggestion-chip.scss): container height 32 px, `corner-small`, icon 18 px, avatar 24 px, outline widths, label and icon colours, disabled opacities 0.38 and 0.12 (verified 2026-11-21).
- [Material Web chip docs](https://github.com/material-components/material-web/blob/main/docs/components/chip.md) and [chip set internals](https://github.com/material-components/material-web/blob/main/chips/internal/chip-set.ts): chip set as toolbar, Left, Right, Home and End keys, soft-disabled, `aria-label` guidance; [`_shared.scss`](https://github.com/material-components/material-web/blob/main/chips/internal/_shared.scss): 48 px touch target (verified).
- [Material Components Android Chip](https://github.com/material-components/material-components-android/blob/master/docs/components/Chip.md): min height 32 dp, min touch target 48 dp.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.11, 2.5.8; [WAI-ARIA Authoring Practices radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/).
- The m3.material.io chips page could not be fetched (script-rendered site).
- Code: `tess-ui:src/tess_ui/views/Chip_View.tdl`, `Chip_Stylesheet.tdl`, `ChipGroup_View.tdl`, `tess-ui:docs/components/chips.md`.
