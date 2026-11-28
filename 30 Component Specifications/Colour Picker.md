---
title: Colour Picker
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, input, colour, picker, slider, contrast]
related: ["[[Colour Roles]]", "[[Popup]]", "[[Text Field]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[State Layers]]", "[[Shape]]", "[[Elevation]]", "[[Typography]]", "[[14 Accessibility Basics#Contrast|Contrast]]", "[[Form Row]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Colour Roles]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
---

# Colour Picker

> [!info] Summary
> A control that chooses a colour from a saturation-value square, hue and alpha strips, hex and channel fields and a row of theme-role swatches, inline or behind a swatch button in a popup. Material Design 3 has no colour picker (see Sources). This note also specifies its parts, the colour area, colour strip and colour swatches, as one unit. Source of truth in code: the last section.

## Purpose

Let a person choose a colour for something they make (a block, a theme key in the config app) with the pointer or the keyboard alone, see the result against the surface it will sit on, and read and write it as text.

## When to use and not

- Use when: the value is a colour that is not a fixed choice of the theme.
- Do not use when: the choice is one of a few named roles with no custom colour ([[Choice Picker]], [[Menu]]); the value is an icon ([[Icon Picker]]) or a font ([[Font List]]); the input is a free text that may be a colour name ([[Text Field]]).

## Anatomy

1. Trigger (popup variant): a square swatch button showing the colour over a chequerboard when alpha is below 1, with a 1 dp `outline` border.
2. Layer (popup variant): a [[Popup]] surface (`surface_container`, 12 dp corners, 16 dp padding, level 2).
3. Square (colour area): saturation across, value up, for the current hue; 256 by 176 dp; a 20 dp handle.
4. Hue strip (colour strip, channel hue): 256 by 24 dp, 0 to 360 degrees.
5. Alpha strip (channel alpha): 256 by 24 dp, clear to the colour over a 6 dp chequerboard, 0 to 100 percent.
6. Hex field ([[Text Field]]): `#rrggbb` or `#rrggbbaa`.
7. Channel fields: red, green, blue, alpha, whole numbers 0 to 255, 58 dp wide, 8 dp gap.
8. Role swatches (colour swatches): 28 dp circles, 4 dp gap, wrapping; the theme roles.
9. Contrast row: ratio against a reference surface; specified below, not built.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Inline | the picker is the content of a panel | all parts always visible |
| Popup | a form row, a launcher | trigger swatch opens the layer next to it; Escape or a press outside closes it |
| Opaque only | a key that allows no alpha | alpha strip and alpha field are absent, not disabled; the value never has alpha digits |
| With alpha | a key that allows alpha | the alpha strip and field show |

## States

| State | Visual change | Token values |
|---|---|---|
| Trigger rest | swatch of the value | border `outline` 1 dp |
| Trigger hover, focus, pressed | state layer, ring, ripple | `on_surface` at 8, 10, 10 percent ([[State Layers]], [[ADR-0013 Focus and pressed state layer 10 percent]]); [[Focus Ring]] |
| Trigger open | layer shown, `Expanded` true | none |
| Disabled | the picker does not open and fades | 0.38 on content |
| Handle focus | ring around the 20 dp handle | [[Focus Ring]] |
| Handle dragged | handle follows the pointer; the halo grows | state layer at the pressed value |
| Field invalid | field in error colours, `invalid` true; the value keeps its last valid colour | `error`, `on_error_container` |
| Role swatch selected | the swatch whose colour equals the value is drawn selected (ring and check) | `on_surface` ring, 2 dp |

## Tokens used

[[Colour Roles]] (swatch defaults and all surfaces), [[Shape]] (trigger 8 dp, layer 12 dp, swatches full), [[Elevation]] (level 2), [[Typography]] (`body_medium` in fields, `label_small` for the contrast row), [[Spacing and Density]], [[State Layers]], [[Focus Ring]]. The handle ring is white at 2 dp over the colour with a 1 dp outer shadow so it keeps 3:1 against any colour (WCAG 1.4.11).

## Sizing and density

| Part | default | compact | dense | Code today |
|---|---|---|---|---|
| Trigger swatch | 40 | 32 | 28 | 40 at every level |
| Hex and channel field height | 40 | 32 | 28 | field default (text field) |
| Layer padding | 16 | 12 | 8 | 16 |
| Gap between parts | 12 | 8 | 8 | 12 |
| Square | 256 by 176 | 256 by 176 | 256 by 176 | 256 by 176 |
| Strip height | 24 | 24 | 24 | 24 |
| Role swatch | 28 | 28 | 28 | 28, gap 4 |
| Handle | 20 | 20 | 20 | 20 |

The square, strips and swatches keep their size at every level: they are drawing surfaces, and their hit area must stay at least 24 by 24 dp ([[ADR-0002 Desktop density levels and target sizes]]). In a touch context the strips are 48 dp high and the swatches 48 dp.

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| Trigger swatch | height | `density.control_height` | 40 | 32 | 28 | [[Colour Picker]] Sizing, [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger swatch | border width | - | 1 | 1 | 1 | [[Colour Picker]] Anatomy part 1 | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger swatch | border color | `outline` | `outline` | `outline` | `outline` | [[Colour Picker]] Anatomy part 1, [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Trigger swatch | corner radius | `shape.small` | 8 | 8 | 8 | [[Colour Picker]] Tokens used, [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | min width | - | 256 | 256 | 256 | [[Colour Picker]] Layout and overflow (panel width) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | padding | `space.5` | 16 16 16 16 | 12 12 12 12 | 8 8 8 8 | [[Colour Picker]] Sizing | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | margin | `space.3` | 8 8 8 8 | 8 8 8 8 | 8 8 8 8 | [[Colour Picker]] Layout and overflow (window less 8 dp margin) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | gap | `space.4` | 12 | 8 | 8 | [[Colour Picker]] Sizing (gap between parts) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | corner radius | `shape.medium` | 12 | 12 | 12 | [[Colour Picker]] Tokens used, [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | border width | - | 0 | 0 | 0 | [[Popup]] (a popup surface is separated by its level 2 shadow) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Layer | border color | - | N/A: the layer draws no border; the level 2 shadow separates it | N/A: same as default | N/A: same as default | [[Colour Picker]] Anatomy part 2 | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Layer | elevation | `elevation.level2` | 2 | 2 | 2 | [[Colour Picker]] Tokens used, [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Square | height | - | 176 | 176 | 176 | [[Colour Picker]] Sizing (256 by 176) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Hue and alpha strip | height | - | 24 | 24 | 24 | [[Colour Picker]] Sizing (48 in a touch context) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Hex and channel field | height | `density.control_height` | 40 | 32 | 28 | [[Colour Picker]] Sizing, [[Spacing and Density]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Channel field | min width | - | 58 | 58 | 58 | [[Colour Picker]] Anatomy part 7 | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Hex and channel field | font | `body_medium` | 14/20/400/0.25 | 14/20/400/0.25 | 13/18/400/0.25 | [[Colour Picker]] Tokens used, [[Typography]]; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Contrast row | font | `label_small` | 11/16/500/0.5 | 11/16/500/0.5 | 11/16/500/0.5 | [[Colour Picker]] Tokens used, [[Typography]] | tess-ui: via theme typography (role label_small); tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Role swatch | height | - | 28 | 28 | 28 | [[Colour Picker]] Sizing | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Role swatches | gap | `space.2` | 4 | 4 | 4 | [[Colour Picker]] Sizing | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Role swatch | corner radius | `shape.full` | 14 | 14 | 14 | [[Colour Picker]] Tokens used (full on 28 dp), [[Shape]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Handle | height | - | 20 | 20 | 20 | [[Colour Picker]] Sizing | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Handle ring | border width | - | 2 | 2 | 2 | [[Colour Picker]] Tokens used (white ring, 1 dp outer shadow) | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell (only the tess-ui config app uses it); tre: n/a: element absent in tre |
| Handle ring | border color | - | N/A: the ring is white by design, so it keeps 3:1 over any colour; white is not a role | N/A: same as default | N/A: same as default | [[Colour Picker]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Picker | font | - | N/A: text roles are given on the fields and the contrast row | N/A: same as default | N/A: same as default | [[Colour Picker]] Tokens used | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |
| Picker | icon size | - | N/A: the picker draws no icon glyph; handle and swatches are drawn shapes | N/A: same as default | N/A: same as default | [[Colour Picker]] Anatomy | tess-ui: n/a: the default is N/A so the element has no such value; tess-shell: n/a: the default is N/A so the element has no such value; tre: n/a: the default is N/A so the element has no such value |

## Layout and overflow

- The panel is 256 dp wide; the layer never exceeds the window minus 8 dp margin and is placed by [[Popup]] (flip to the side with room).
- Role swatches wrap to further lines; the panel never scrolls horizontally. When the window is shorter than the layer, the layer content scrolls vertically with a [[Scrollbar and Scroll Container]] ([[10 Layout Overflow and Scrolling]]).
- Fields show the value on one line and never truncate a hex value (9 characters fit in 58 dp at `body_medium`; the hex field is 256 dp wide).
- Vertical centring: field text is centred in the field height at every level.

## Colour format rules

- The value is text: `#rrggbb`, or `#rrggbbaa` when alpha is below 1. Digits are lowercase. A fully opaque colour never carries alpha digits. A set followed by a read returns the same text.
- Input accepts upper and lower case hex and writes lowercase. `#fff`, `red`, `rgb()` and any other form is an error that names the widget; the field keeps its last valid value and shows the error colours with `invalid` true. Leaving the field or Escape restores the text of the value.
- Channel fields take whole numbers 0 to 255; alpha 0 to 255 in the channel field and 0 to 100 percent on the strip. A value outside the range is invalid; the arrows step by 1, by 10 with Shift, clamp at the ends.
- Theme role swatches write the resolved opaque hex of the role in the active scheme at the active contrast level ([[Colour Roles]]), not a role name. The role row therefore changes with the theme; the stored value does not.
- Roles in the row by default, in order: `primary`, `secondary`, `tertiary`, `error`, `surface`, `on_surface`, `primary_container`, `secondary_container`; the app may name others.
- Hue memory: a grey or black has no hue; the picker keeps the last hue so a drag through white or black ends where it began, and a drag of the hue strip keeps saturation and value.

## Contrast display

The contrast row is specified here and is not built. It shows the contrast ratio between the value (alpha composited over the reference) and a reference colour, so a person choosing a text or icon colour sees at once whether it passes.

- Reference: the role `surface` by default; the app may set another role or a hex. A label names it ("on surface").
- Formula: WCAG 2.2 relative luminance of sRGB; ratio = (L1 + 0.05) / (L2 + 0.05) with L1 the lighter ([[14 Accessibility Basics#Contrast|Contrast]], [[Colour Roles]] for the table of role pairs). The value is composited over the reference before measuring when its alpha is below 1.
- Display: `4.53:1`, two decimals, truncated toward zero, never rounded up, so 4.499 shows `4.49:1` and does not claim 4.5.
- Marks: three text marks, each with words and an icon, not colour alone: "Text AA" at 4.5, "Large text and UI" at 3.0, "Text AAA" at 7.0, each "pass" or "fail".
- Announcements: the row is a `status` region; the ratio is announced when a drag ends, a key step lands or a field is committed, not on every drag frame.
- The row is optional: an app turns it on with a reference; hidden by default in the config app because most keys are not text colours.

## Behaviour

- Pointer: a press or drag on the square sets saturation and value and keeps hue and alpha; on a strip it sets that channel; a press on a role swatch sets the value; a press on the trigger opens and, pressed again, closes the layer; a press outside closes it.
- `On_Change` fires after each user change, including during a drag; a change the app makes by setting the value does not fire it.
- Keyboard. Tab order: trigger (popup), square, hue, alpha, hex, red, green, blue, alpha field, role swatches.

| Control | Key | Action |
|---|---|---|
| Square | Left, Right | saturation minus, plus 1 percent; Shift 10 percent |
| Square | Up, Down | value plus, minus 1 percent; Shift 10 percent |
| Square | Page Up, Page Down | value plus, minus 10 percent |
| Square | Home, End | saturation to 0, 100 percent |
| Strip | Left, Right (or Up, Down) | 1 degree or 1 percent; Shift 10 |
| Strip | Page Up, Page Down | 10 degrees or 10 percent |
| Strip | Home, End | the ends |
| Field | Enter, blur | commit when valid |
| Field | Up, Down | step 1; Shift 10 |
| Field | Escape | restore the value text |
| Swatches | Left, Right | move between swatches (roving, one Tab stop) |
| Swatch | Enter, Space | set the value |
| Layer | Escape | close and return focus to the trigger |

- Touch: handles keep a 48 dp hit area; the layer opens as a [[Popup]] anchored to the trigger.

## Tooltip and overlay behaviour

Tooltips belong to controls only ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]): the trigger shows the colour text (`#4682b4`); each role swatch shows the role name and its hex ("primary #6750a4"); each strip handle shows its value ("hue 210 degrees") while hovered or focused; the square, the layer and the panel carry none. The layer is a [[Popup]] ([[12 Overlays]]): focus moves to the square on open, returns to the trigger on close. 500 ms hover delay, immediate on keyboard focus, one tooltip at a time.

## Motion

None on drag. The layer fades in 150 ms and out in 100 ms ([[Motion]]); reduced motion makes both 0 ms.

## Accessibility

- The picker is a `group` named by `Label`. The trigger is a `button` named "Label: #hex" with `Expanded`. The square is a `slider` named "Saturation and value" whose value text reads "saturation 40 percent, value 80 percent"; each strip is a `slider` named "Hue" or "Alpha" with value text in degrees or percent; sliders accept increment, decrement and set. Fields are `textbox` named by channel with `invalid` when not a colour. Role swatches are `button` named by role and `pressed` when selected.
- Announcements: key steps announce the new value text once per step; drag announces at release; an invalid field announces its error once; the contrast row announces as above.
- Contrast: handle ring against any colour at least 3:1; field text at least 4.5:1; role swatch ring at least 3:1 ([[Colour Roles]]).
- Target size: every swatch, handle and field hit area at least 24 by 24 dp at every density.
- The colour is never the only carrier: the hex text and the contrast marks state it in words.

## Dark and light

Roles only; the role row shows the role colours of the active scheme and the chequerboard uses `surface_container_highest` and `outline_variant` ([[Theme Following the System]]). The stored value is theme independent.

## Defaults

`Value` `#000000`, inline, role row as above, label "Colour", alpha strip shown, contrast row off, level per project.

## Acceptance criteria

- [ ] AC-CLP-1 (token test): setting `#ABCDEF` reads back `#abcdef`; `#ffffffff` reads back `#ffffff`; `#ffffff80` stays `#ffffff80`; `#fff`, `red` and `rgb(1,2,3)` raise an error naming the widget.
- [ ] AC-CLP-2 (scripted input): typing `#12345` in the hex field leaves the value unchanged and sets `invalid`; `#123456` sets the value immediately; Escape restores the text of the value.
- [ ] AC-CLP-3 (scripted input): in a channel field, 256 and -1 are invalid; Up from 255 stays 255; Shift+Down from 20 gives 10.
- [ ] AC-CLP-4 (scripted input): on the square Right then Left returns to the start value; Shift+Right changes saturation by 10 percent; End sets saturation 100; Page Up raises value by 10 percent; hue and alpha stay.
- [ ] AC-CLP-5 (scripted input): dragging the square to a corner of black and back leaves the hue field's degrees unchanged.
- [ ] AC-CLP-6 (AT tree assertion): the picker is a `group` with a name; the square and both strips have role `slider` with value text "saturation N percent, value M percent", "N degrees" and "N percent"; the hex field has role `textbox` and `invalid` true for a bad entry.
- [ ] AC-CLP-7 (scripted input): Tab order is square, hue, alpha, hex, red, green, blue, alpha field, then the first role swatch (one stop for the row); Left and Right move between role swatches; Escape closes a popup and focus lands on the trigger.
- [ ] AC-CLP-8 (geometry check): at default, compact and dense the trigger swatch is 40, 32 and 28 dp square and each field height is 40, 32 and 28 dp; the square is 256 by 176 dp and strips 24 dp high at every level.
- [ ] AC-CLP-9 (geometry check): every swatch, handle and field has a hit area of at least 24 by 24 dp at each density and at least 48 by 48 dp in a touch context.
- [ ] AC-CLP-10 (token test): the default role row holds exactly `primary`, `secondary`, `tertiary`, `error`, `surface`, `on_surface`, `primary_container`, `secondary_container`; pressing a swatch sets the resolved opaque hex of the role in the active scheme; the swatch with that hex shows selected.
- [ ] AC-CLP-11 (contrast script): with reference `#ffffff` the contrast row for `#000000` shows `21.00:1`; for a value of ratio 4.4999 it shows `4.49:1` and "Text AA fail"; for 3.0000 it shows "Large text and UI pass".
- [ ] AC-CLP-12 (pixel check): the handle ring measures at least 3:1 against the square pixel under it at the corners and the centre of the square, in light and dark.
- [ ] AC-CLP-13 (scripted input): an opaque-only key shows no alpha strip and no alpha field and rejects `#rrggbbaa` with a message; a with-alpha key shows both.
- [ ] AC-CLP-14 (scripted input): a tooltip appears on a role swatch after 500 ms hover and at once on focus, names the role and hex, and none appears over the square or the layer background; Escape, scroll, press and leaving remove it.
- [ ] AC-CLP-15 (scripted input): `On_Change` fires on each user change and not on an app-set value; a disabled picker neither opens nor changes.
- [ ] AC-CLP-16 (AT tree assertion): a key step on a strip yields one announcement with the new value text; a drag yields one at release.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/ColourPicker_View.tdl`, `ColourPickerPanel_View.tdl`, `ColourPicker_Stylesheet.tdl`, `tess-ui:src/tess_ui/colour_controls.py`, `tess-ui:docs/components/colour-pickers.md` | partly meets. Passes AC-CLP-1 to 7, 10, 13 (alpha strip always shown, see tess-shell row), 15 by documented behaviour. Fails AC-CLP-8 at compact and dense (no density), AC-CLP-11 (no contrast row), AC-CLP-12 and AC-CLP-14 (no tooltips on swatches), AC-CLP-16 (not shown) |
| tess-ui (dimensions) | `tess-ui:src/tess_ui/views/ColourPicker_Stylesheet.tdl` | Differences in [[#Dimensions and defaults]]: layer padding 16 and gap 12 at all levels, spec 12 and 8 at compact, 8 and 8 at dense; trigger swatch 40 at all levels, spec 32 and 28 (AC-CLP-8). Square 256 by 176, strips 24, role swatch 28 with gap 4 and handle 20 meet the table. Not settable from the project layer (no hook): the panel width 256, gap 12, square 176, strips 24, channel width 58 (inline in `ColourPickerPanel_View.tdl`) and the field height 40, role swatch 28, handle 20 and ring 2 (class constants in `colour_controls.py`) |
| tess-ui | Not built (component doc) | HSL and OKLCH spaces, an eyedropper, a recent-colours row, a swatch row for the theme's colours of the other mode, alpha digits from an `rgb()` colour |
| tess-shell | `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`ColourWidget`) | partly meets: the config app uses the popup picker with alpha only when the key allows it (the widget refuses an alpha write otherwise) but the panel still shows the alpha strip, so AC-CLP-13 fails |
| tre | none | not applicable: the engine draws gradients; the picker lives in tess-ui |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |
| Element has no MD3 counterpart | MD3 chooses colours for a theme, not content; desktop editors need a square, strips, fields | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Trigger and field heights 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Contrast row with truncated ratio | WCAG 1.4.3 and 1.4.11 apply to a colour the user picks | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Focus and pressed state layer 10 percent | latest Material Web tokens | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Tooltips on swatches and handles, not on the surface | owner feedback | [[ADR-0004 Tooltip rule]] |

## Sources

- tess-ui: `tess-ui:docs/components/colour-pickers.md`, `tess-ui:src/tess_ui/views/ColourPicker_Stylesheet.tdl`, `tess-ui:src/tess_ui/views/ColourPickerPanel_View.tdl`, `tess-ui:src/tess_ui/colour_controls.py` (HANDLE 20, strip thickness 12 track, swatch 28, gap 4).
- WAI-ARIA APG slider https://www.w3.org/WAI/ARIA/apg/patterns/slider/ and multi-thumb slider https://www.w3.org/WAI/ARIA/apg/patterns/slider-multithumb/ (arrows, Page Up and Page Down, Home, End). APG has no two-dimensional slider; the square follows the code and one slider with two value texts #needs-verification.
- WCAG 2.2 SC 1.4.3 https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html (4.5:1, 3:1 large text), SC 1.4.11 https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html (3:1), SC 4.1.3 https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html. The rule that a ratio is truncated, not rounded up, is a Tesserae rule #needs-verification.
- AAA 7:1 for text is WCAG SC 1.4.6, not re-read here #needs-verification.
- No MD3 colour picker exists; Material Web has no picker component (https://github.com/material-components/material-web/tree/main/docs/components lists none).
