---
title: Segmented Button
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, selection]
related: ["[[Button]]", "[[Icon Button]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[State Layers]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]", "[[Button Group]]", "[[Switch]]", "[[Form Row]]", "[[10 Layout Overflow and Scrolling]]"]
depends_on: ["[[Button]]", "[[Colour Roles]]", "[[Shape]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Segmented Button

> [!info] Summary
> Two to five connected segments in one outlined pill, for choosing one option or several: Material Design 3 [segmented buttons](https://m3.material.io/components/segmented-buttons/overview) (2022 baseline). Source of truth in code: see Status in code.

## Purpose

Chooses among a small set of related, mutually visible options (Day, Week, Month; Bold, Italic) where seeing all options at once helps and the choice applies at once.

## When to use and not

- Use when: two to five options with short labels or icons; single choice (a radio set) or multiple (a set of toggles).
- Do not use when: more than five options or long labels (use a list, a menu or radio buttons); the choice has a default action with alternatives (use a [[Split Button]]); an on or off setting (use a [[Switch]]); a set of commands, not choices (use a [[Button Group]] in `none` mode).
- The Expressive connected [[Button Group]] in `single` or `multiple` mode has the same semantics; a view uses one of them for one kind of choice.

## Anatomy

1. Container: one pill, 1 dp `outline` border, shape `full`, clipped.
2. Segments, each a pressable area with its own state layer.
3. Dividers: 1 dp `outline` lines between segments.
4. Icon (optional), 18 dp; a selected segment shows a check in its place (or before the label when it has no icon).
5. Label, `label_large`.
6. Focus ring on the focused segment ([[Focus Ring]]).

## Variants

| Variant | Behaviour | Exposed role |
|---|---|---|
| Single choice | exactly one segment is selected (one is selected at all times once a value exists) | radio group |
| Multiple choice | any number selected, including none | group of toggle buttons |

Segment content: label only, icon only, icon plus label. Selected: container `secondary_container`, label and icon `on_secondary_container`. Unselected: no container, label and icon `on_surface`. Material Web [outlined segmented button tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-segmented-button.scss).

## States

State layer colour: `on_secondary_container` on a selected segment, `on_surface` on an unselected one; percentages from [[State Layers]] (hover 8, focus 10, pressed 10 percent, [[ADR-0013 Focus and pressed state layer 10 percent]]).

| State | Visual change | Token values |
|---|---|---|
| Rest | as Variants | roles |
| Hover | state layer 8 percent on the segment only | [[State Layers]] |
| Focus (keyboard) | state layer 10 percent on the segment; focus ring 3 dp, 2 dp offset, role `secondary`, around the segment inside the pill | [[Focus Ring]] |
| Pressed | state layer 10 percent | [[State Layers]] |
| Selected | container and check as above | roles |
| Disabled (segment or whole control) | label and icon `on_surface` at 38 percent; outline and dividers `on_surface` at 12 percent; the selected container `on_surface` at 12 percent; no state layer | Material Web `disabled-*` tokens: icon 0.38, label 0.38, outline 0.12 |

A disabled segment is not focusable and not selectable; arrows skip it. The control suppresses input itself ([[Button]] rule).

## Tokens used

[[Colour Roles]], [[Shape]] (`full`), [[Typography]] (`label_large`), [[Motion]], [[Spacing and Density]], [[Iconography]].

## Sizing and density

MD3 from Material Web: container height 40 px, outline 1 px, shape `corner-full`, icon 18 px, label `label-large` ([tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-segmented-button.scss)). Segment padding is not a token in v0_192 #needs-verification; tess-ui uses 12 dp each side with gap 8.

Tesserae by density ([[ADR-0002 Desktop density levels and target sizes]]; control heights binding like [[Button]], paddings are design choices #needs-verification):

| Level | Height | Segment padding (each side) | Icon | Gap icon to label | Minimum segment width |
|---|---|---|---|---|---|
| default | 40 | 12 | 18 | 8 | 48 |
| compact | 32 | 12 | 18 | 8 | 40 |
| dense | 28 | 8 | 16 | 4 | 32 |

- Segments are equal width when the author asks for a fixed width control, else content width; a segment is never narrower than its minimum.
- The segment is the hit area: at least 24 dp wide and the full height; 48 dp high in touch contexts. Dividers are 1 dp and belong to no hit area.
- The label is vertically centred in the segment (space above equals space below ±0.5 dp) at every density.
- Selecting never changes the control's width: the check replaces the icon, or for a label-only segment it reserves its 18 dp width in every segment of the control (design choice, avoids a layout jump #needs-verification).

## Layout and overflow

- Two to five segments. A sixth segment is an error of use; the control does not wrap. A label that does not fit ends with an ellipsis; the full label is the name and the tooltip on that segment ([[10 Layout Overflow and Scrolling]]).
- Fits the width of its parent only when the author sets it; otherwise it is as wide as its segments.

## Behaviour

- Pointer: press and release inside a segment selects it (single) or toggles it (multiple); pressing the selected segment in single choice leaves it selected; a press starting in one segment and ending in another selects nothing.
- Keyboard, single choice ([WAI-ARIA APG radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/)): one Tab stop (the selected segment, else the first enabled one); Left and Right move focus and select, wrapping, skipping disabled segments; Space selects the focused segment. Home and End are not defined by APG and are optional #needs-verification.
- Keyboard, multiple choice: each segment is a Tab stop; Space and Enter toggle it; Left and Right move focus without changing selection.
- Touch: tap on the segment.

## Tooltip and overlay behaviour

A segment shows a plain tooltip on itself when its label is truncated or it has an icon only ([[ADR-0004 Tooltip rule]], [[Tooltip]]); never on the whole control. No overlay.

## Motion

Selection fills over `short3` 150 ms with the check fading in 100 ms #needs-verification; reduced motion: instant. State layer fade as [[Button]].

## Accessibility

- Single choice: role `radiogroup` containing `radio` segments, `checked` on the selected one. Multiple choice: role `group` containing `button` segments with `pressed` (equally a `checkbox` with `checked` is valid; the vault uses `button` plus `pressed`, the toggle button pattern) ([WAI-ARIA toggle button](https://www.w3.org/WAI/ARIA/apg/patterns/button/)).
- The control has a name from its context (a label or a [[Form Row]] label) when it stands for a form value.
- A segment's name is its label; an icon-only segment has a name too ([[Icon Button]] rule).
- Contrast: selected label on `secondary_container` at least 4.5 to 1; the pill outline against the surface at least 3 to 1; selected against unselected is carried by container, check and shape, not colour alone (WCAG 1.4.11, 1.4.1).

## Dark and light

All roles; AC-SEG-9 runs in both schemes ([[Theme Following the System]]).

## Defaults

Single choice, height from the density level, equal-minimum segments, no preselected value in multiple choice, the first value selected in single choice when the model is empty #needs-verification (design choice).

## Acceptance criteria

- [ ] AC-SEG-1 (token test): heights 40, 32, 28 dp at default, compact, dense; paddings, icon sizes (18, 18, 16) and gaps equal the Sizing table; border 1 dp `outline`; shape `full`. Pass: values equal.
- [ ] AC-SEG-2 (token test): selected container `secondary_container`, selected label and icon `on_secondary_container`, unselected label and icon `on_surface`, dividers `outline`; no literal colour. Pass: every colour is a role reference.
- [ ] AC-SEG-3 (token test): state layer opacities 8, 10, 10 percent from [[State Layers]], layer colour per segment as the States section; disabled label and icon 38 percent, outline and dividers 12 percent; a disabled segment has no layer. Pass: values equal.
- [ ] AC-SEG-4 (scripted input): single choice: one Tab stop on the selected segment; Right and Left move focus and selection with wrap and skip a disabled segment; Space selects; a press on the selected segment keeps it selected; press in one segment, release in another selects nothing. Pass: focus and selection sequence equal.
- [ ] AC-SEG-5 (scripted input): multiple choice: each enabled segment is a Tab stop; Space and Enter toggle one segment; arrows move focus only; the bound list equals the toggled values. Pass: lists equal.
- [ ] AC-SEG-6 (AT tree assertion): single choice exposes `radiogroup` with `radio` children and `checked` equal to the model; multiple exposes `group` with `button` children and `pressed` equal to the model; every segment has a non-empty name; `disabled` is set for disabled segments. Pass: all equal.
- [ ] AC-SEG-7 (geometry check): the label line box is vertically centred (offset at most 0.5 dp) at each density and scale 1.0, 1.25, 2.0; selecting a segment changes the control width by at most 0.5 dp. Pass: values within limits.
- [ ] AC-SEG-8 (geometry check): each segment hit area is at least 24 dp wide and the full height at every density (48 dp high in touch); a label longer than its segment shows an ellipsis and no text pixel lies outside the pill. Pass: bounds at or above limits, zero pixels outside.
- [ ] AC-SEG-9 (contrast script): light and dark, label on container at least 4.5 to 1 (selected and unselected), pill outline on the surface at least 3 to 1. Pass: ratios at or above limits.
- [ ] AC-SEG-10 (pixel check): under keyboard focus the ring is 3 dp wide, 2 dp outside the segment, role `secondary`, drawn inside the pill clip without being cut; absent under mouse-click focus. Pass: measured ring equals, clipped pixels 0.
- [ ] AC-SEG-11 (scripted input): hover over an icon-only or truncated segment shows a tooltip with its label on that segment; hover over the control gap or a full-label segment shows none. Pass: tooltip text equal or absent as stated.
- [ ] AC-SEG-12 (review): two to five segments per control. Pass: review of each use.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/SegmentedButton_View.tdl`, `tess-ui:src/tess_ui/widgets/buttons.py` (`segmented_button`), `tess-ui:docs/components/segmented-buttons.md`, test `tess-ui:tests/test_segmented_button.py` | partly meets: outlined pill 40 high, 1 px `outline`, `full` shape, clipped, dividers, selected `secondary_container` with check replacing the icon, `label_large`, 18 px icon, padding 12, gap 8 (AC-SEG-2 meets; AC-SEG-1 meets at default, fails compact and dense: height literal 40); single choice selects on focus with one Tab stop and arrows, multiple choice toggles with arrows moving focus (AC-SEG-4, AC-SEG-5 meet by reading; wrap and skip stated for disabled); roles are `radio` or `checkbox` under a `group` container: no `radiogroup` role and multiple uses `checkbox` (AC-SEG-6 fails); disabled sets opacity 0.38 on the whole segment including the selected container and divider (AC-SEG-3 fails); selecting an unselected label-only segment adds the check and widens the control (AC-SEG-7 fails); no tooltip support per segment (AC-SEG-11 not built); segment text colour literal `on_surface` is a role (meets) |
| tess-shell | none found | absent |
| tre | none | not applicable |

No app or example uses it.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Heights 40, 32, 28 dp; smaller paddings at dense | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Baseline (2022) segmented button kept although Expressive replaces it by the connected [[Button Group]] | both are specified; the segmented button is the compact form | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Hit area is the segment with a 24 dp floor; 48 dp high only in touch contexts | WCAG 2.2 SC 2.5.8, desktop | [[ADR-0002 Desktop density levels and target sizes]] |
| Focus and pressed state layer 10 percent | latest tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Multiple choice exposes `button` with `pressed` | the toggle button pattern fits a pressable segment | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- [Material Web outlined segmented button tokens v0_192](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-segmented-button.scss): container-height 40 px, outline 1 px, shape corner-full, with-icon icon size 18 px, selected container `secondary-container`, selected label and icon `on-secondary-container`, unselected `on-surface`, disabled label and icon 0.38, disabled outline 0.12.
- [WAI-ARIA APG radio group](https://www.w3.org/WAI/ARIA/apg/patterns/radio/), [toggle button](https://www.w3.org/WAI/ARIA/apg/patterns/button/); [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.3, 1.4.11, 2.5.8.
- Code: `tess-ui:docs/components/segmented-buttons.md`. The "two to five segments" rule is from the m3.material.io page, which could not be fetched #needs-verification.
