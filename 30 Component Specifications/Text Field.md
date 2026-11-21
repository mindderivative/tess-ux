---
title: Text Field
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, input, owner-feedback]
related: ["[[Owner Feedback 2026-11-20]]", "[[Switch]]", "[[Form Row]]", "[[Scrollbar and Scroll Container]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[State Layers]]", "[[Focus Ring]]", "[[Iconography]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0009 State layer percentages]]"]
depends_on: ["[[Colour Roles]]", "[[Typography]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Text Field

> [!info] Summary
> An editable text box, single-line or multi-line, with an optional label, supporting text, icons and error state: the Material Design 3 [text field](https://m3.material.io/components/text-fields/overview) in its filled and outlined variants, sized by density for desktop. Source of truth in code: see the last section.

## Purpose

The user types, pastes or edits one piece of text: a name, a path, a number with a unit, a search query, a note. Owner feedback F7 ([[Owner Feedback 2026-11-20]]) showed single-line text sitting at the top of its box; this note makes vertical centring a property of the construction, not of hand-tuned padding.

## When to use and not

- Use when: the value is free or loosely constrained text.
- Do not use when: the value is one of a small set (use a Menu or a segmented control), a boolean (use [[Switch]]), or a number that needs stepping and range refusal (use a Spin Box, specified later).
- A label and a field that live in one settings row belong to [[Form Row]]; the Text Field specifies the field only.

## Anatomy

1. Container: the filled fill or the outlined border.
2. Leading icon (optional, 24 dp icon, 20 dp at compact and dense).
3. Prefix text (optional), such as a currency sign.
4. Input area: the typed text, placeholder, caret and selection.
5. Suffix text (optional), such as a unit.
6. Trailing icon or button (optional): clear, reveal password, error icon.
7. Label: the field's name. Two placements ([[ADR-0023 Text Field label placement by density]]): a floating label inside the container that rises, smaller, when the field has focus or text (MD3, default density only, container 56 dp), or an external label above the container (any density; the only placement at compact and dense). The accessible name is always the `Label` property, in both placements.
8. Active indicator (filled only): a line along the bottom edge of the container.
9. Supporting text (optional): help or error message below the container.
10. Character counter (optional): in the supporting row, trailing side.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Filled | default for forms and dialogs | container role `surface_container_highest`, active indicator 1 dp, 2 dp when focused, top corners 4 dp, square bottom (token `corner-extra-small-top`) |
| Outlined | dense forms, config panels, fields on a filled surface | outline 1 dp role `outline`, 2 dp role `primary` when focused, all corners 4 dp (`corner-extra-small`) |
| Floating label | default density, forms and dialogs that follow MD3 | the label sits inside the container and rises when the field has focus or text; the container is 56 dp high and holds the label; not available at compact and dense |
| External label | every density; the only label placement at compact and dense | the label sits above the container, outside its height; the container is 40, 32 or 28 dp; label and field form one block |
| Single-line | one line of text | content never wraps; long content follows the overflow rule below |
| Multi-line | notes, descriptions, log text | Enter inserts a newline; vertical scroll, optional resize |
| Password | secrets | text replaced by bullets, no copy, no cut, reveal toggle |
| Read-only | selectable, copyable, not editable | focusable; no edit; no caret blink |
| Disabled | not available | not focusable, no input, not selectable |

Sources for the variant values: [Material Web filled text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-text-field.scss) and [outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss).

## States

State layer percentages and the focus ring come from [[State Layers]] and [[Focus Ring]]. A text field does not draw a state layer over its container; MD3 changes the active indicator, the outline and the label colour instead.

| State | Visual change | Token values |
|---|---|---|
| Rest | filled: container `surface_container_highest`, indicator 1 dp `on_surface_variant`; outlined: outline 1 dp `outline`; label `on_surface_variant`; input text `on_surface`; supporting text `on_surface_variant` | Material Web `filled-text-field` and `outlined-text-field` tokens |
| Hover | filled: indicator `on_surface`; outlined: outline `on_surface`; label and supporting text `on_surface` | same files |
| Focus (focused field, pointer or keyboard) | filled: indicator 2 dp `primary`; outlined: outline 2 dp `primary`; label `primary`; caret `primary` | same files |
| Keyboard focus | as Focus; no separate focus ring around the container because the 2 dp indicator or outline is the focus indicator | review |
| Error | indicator or outline `error`; label `error`; supporting text `error`; trailing error icon `error`; input text stays `on_surface`; stays `error` while hovered and focused | same files |
| Disabled | input text, label, icons and supporting text `on_surface` at 38 percent; filled container `on_surface` at 4 percent; indicator 1 dp `on_surface` at 38 percent; outlined outline `on_surface` at 12 percent | same files (`disabled-*` tokens) |
| Read-only | rest look, caret not drawn, selection allowed | design choice, review |
| Placeholder shown | text colour `on_surface_variant` while the field is empty and focused, or has no label | [Material Web text-field](https://github.com/material-components/material-web/blob/main/docs/components/text-field.md) |

Selection fill: role `primary` at 30 percent behind the text, text colour unchanged. The role follows Compose Material 3 `rememberTextSelectionColors` (`primary`; MD3 alpha 0.4, https://github.com/androidx/androidx/blob/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/MaterialTheme.kt; the Material Web text field tokens give the caret colour and no selection colour); the alpha is 30 percent because 40 percent gives body text only 3.74 to 1 on the dark `surface_bright` container (see [[Text Selection]]). The engine draws the text colour at 30 percent for a text input that sets its own fill and the scheme's `secondary_container` otherwise (`tre:docs/guide/text.md`). Caret colour: role `primary` (Material Web `caret-color` token). A project that cannot read these roles keeps the engine default (caret = text colour) and records it in its audit.

## Tokens used

- Colour roles as listed in the State table: [[Colour Roles]].
- Type: input and label `body_large` (16 dp on 24 dp) at default density; `body_medium` (14 dp on 20 dp) at compact and dense; floating label and supporting text `body_small` (12 dp on 16 dp). Values: [Material Web typescale tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss). See [[Typography]].
- Shape: filled top corners 4 dp, bottom square; outlined 4 dp ([[Shape]]).
- Spacing and density: [[Spacing and Density]].

## Sizing and density

Heights and padding from [[Spacing and Density]] under [[ADR-0002 Desktop density levels and target sizes]]:

| Level | Single-line container height | Horizontal padding | Text line box | Vertical space above and below the line box |
|---|---|---|---|---|
| default | 40 dp | 12 dp | 24 dp (`body_large`) | 8 dp |
| compact | 32 dp | 8 dp | 20 dp (`body_medium`) | 6 dp |
| dense | 28 dp | 8 dp | 20 dp (`body_medium`) | 4 dp |

- Vertical centring is by construction: the input area's content box is the line box, and the container centres it (flex centring or equal computed padding). Authors do not tune top and bottom padding by hand. Rule: space above the line box equals space below to within 0.5 dp, at every density and at scale factors 1.0, 1.25 and 2.0 (see AC-TXF-1).
- Minimum pointer target: 24 dp high and wide ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum)), met by 28 dp at dense; 48 dp hit area in touch contexts.
- Leading and trailing icon containers use the icon button sizes of [[Icon Button]] when pressable (clear, reveal); a decorative icon is 24 dp (20 dp at compact and dense) and takes no pointer.
- MD3 filled field height is 56 dp: it is the height of the floating label variant at default density (the label rises inside the container). The Tesserae heights above are the height of the field without a floating label, and a recorded deviation from MD3 (see the Deviations table). The tess-ui `TextField` view is 280 px wide by default; a field in a flexible row has a minimum width of 48 dp so it never collapses to zero, per [[10 Layout Overflow and Scrolling]] #needs-verification-as-design-choice.

### Label placement by density

Decision: [[ADR-0023 Text Field label placement by density]]. A floating label cannot sit inside a 32 or 28 dp container (it needs the 12 dp label line above the 24 dp or 20 dp input line), so:

| Level | Floating label variant | External label variant | Container height | Label to container gap | Block height (label line 16 plus gap plus container) |
|---|---|---|---|---|---|
| default | allowed, container 56 dp, label inside | allowed | 56 floating; 40 external or no label | 4 dp (external) | 60 dp external |
| compact | not available | the only placement | 32 dp | 4 dp | 52 dp |
| dense | not available | the only placement | 28 dp | 2 dp | 46 dp |

- The single-line container height (AC-TXF-3) never includes an external label; the label and the gap are outside it and the label does not change the container height or the vertical centring of the input text.
- A field with a label at compact or dense density renders the external label even when the application asks for the floating variant; the application does not need two code paths.
- A field without a label (a field in a [[Form Row]], whose row label names it) has the container alone.
- The placeholder is a hint, not the label: it disappears on input, so the accessible name comes from the `Label` property whenever one is set (AC-TXF-18); a field with a placeholder and no label is allowed only where a nearby visible text names it (the Form Row label).

## Dimensions and defaults

Single-line outlined field unless the Part says filled. Vertical padding is `(height - line height) / 2`, so the line box is centred by construction (AC-TXF-1). The dimensions follow the Sizing table; values not stated there come from the Material Web text field tokens. Rows marked as design choice carry #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container | min width | - | 48 | 48 | 48 | design choice, proposed ADR: minimum width of single-line input controls, [[Spacing and Density]] | tess-ui: yes (style min_width); tess-shell: yes (Min_Width); tre: yes (min_width) |
| container | min height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], the 24 dp pointer minimum is met at every level | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| container | padding | `density.field_padding_x` | 8 12 8 12 | 6 8 6 8 | 4 8 4 8 | [[Spacing and Density]] (horizontal), vertical = (height - line box) / 2 from the Sizing table | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| container | margin | - | N/A: the parent container or Form Row sets the outer space | N/A: same as default | N/A: same as default | [[Spacing and Density]], [[Form Row]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| container | gap | `density.icon_label_gap` | 8 | 8 | 4 | [[Spacing and Density]] (icon, prefix, input, suffix and trailing button sit in one row) | tess-ui: yes (style gap); tess-shell: n/a: the TextField block has no row of parts to space; tre: yes (gap) |
| container | border width | - | 1 | 1 | 1 | [Material Web outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss), 2 when focused | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| container | border color | `outline` | `outline` | `outline` | `outline` | MD3 outlined text field tokens, `primary` when focused, `error` in error | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| container | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]], MD3 text fields are flat | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |
| active indicator | height | - | 1 | 1 | 1 | [Material Web filled text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-text-field.scss), 2 when focused (filled variant only) | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| active indicator | border color | `on_surface_variant` | `on_surface_variant` | `on_surface_variant` | `on_surface_variant` | MD3 filled text field tokens, `primary` when focused, `error` in error | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container (filled) | corner radius | `shape.extra_small_top` | 4 4 0 0 | 4 4 0 0 | 4 4 0 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| input | font | `body_large` / `body_medium` | 16/24/400/0.5 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]], Tokens used section | tess-ui: via type role in the theme (family, size, weight), no hook for line height and tracking; tess-shell: yes (Font_Family, Font_Size, Font_Weight), no hook for Line_Height and letter spacing; tre: yes (font_family, font_size, font_weight), hardcoded in tre (text_input takes no line_height or letter_spacing) |
| container (floating label variant) | height | - | 56 | N/A: the floating label variant is not available at compact | N/A: the floating label variant is not available at dense | MD3 filled text field container height (Material Web `textfield` min-height 56 px), [[ADR-0023 Text Field label placement by density]] | tess-ui: yes (style height); tess-shell: n/a: the TextField block draws no floating label; tre: yes (height) |
| external label | height | - | 16 | 16 | 16 | [[Typography]] (`body_small` line height), design choice, [[ADR-0023 Text Field label placement by density]] | tess-ui: yes (style height); tess-shell: n/a: the TextField block draws no label; tre: yes (height) |
| external label | margin | `space.2` | 0 0 4 0 | 0 0 4 0 | 0 0 2 0 | design choice, [[ADR-0023 Text Field label placement by density]] (gap between the label and the container) #needs-verification-as-design-choice | tess-ui: yes (style margin); tess-shell: n/a: the TextField block draws no label; tre: yes (margin) |
| external label | font | `body_small` | 12/16/400/0.4 | 12/16/400/0.4 | 12/16/400/0.4 | [[Typography]], design choice, [[ADR-0023 Text Field label placement by density]] | tess-ui: via type role in the theme; tess-shell: n/a: the TextField block draws no label; tre: yes (font_size, font_weight, line_height) |
| label | font | `body_small` | 12/16/400/0.4 | 12/16/400/0.4 | 12/16/400/0.4 | [[Typography]], floating label | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| supporting text | font | `body_small` | 12/16/400/0.4 | 12/16/400/0.4 | 12/16/400/0.4 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| supporting text | margin | `space.2` | 4 0 0 0 | 4 0 0 0 | 4 0 0 0 | MD3 filled text field `supporting-text-top-space` 4, https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-text-field.scss | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| supporting text | padding | `space.4` | 0 12 0 12 | 0 8 0 8 | 0 8 0 8 | [[Spacing and Density]], aligned with the field text edge | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| leading icon | icon size | - | 24 | 20 | 20 | [[Iconography]] (text field leading and trailing icon row) | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| trailing icon button | height | `density.icon_button_container` | 40 | 32 | 28 | [[Icon Button]], [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| trailing icon button | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Spacing and Density]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| trailing icon button | min height | - | 24 | 24 | 24 | WCAG 2.2 SC 2.5.8 pointer minimum, 48 in a touch context | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |

## Layout and overflow

- Horizontal alignment: start (left in left-to-right locales). Numeric fields may align end by explicit property.
- Single-line content is one line. It never wraps and never draws outside the container ([[10 Layout Overflow and Scrolling]]: content never overflows its container).
- Overlong single-line content, field not focused: truncated with an ellipsis at the end of the visible line. Engine: `overflow="ellipsis"` (`tre:docs/guide/text.md`, "Long lines in a text input").
- Overlong single-line content, field focused: the ellipsis is removed and the text scrolls horizontally so the caret stays inside the content box; at least 1 character width of text remains visible on each side of the caret when the text allows. Engine: `overflow="ellipsis"` shows the ellipsis "until the input has the focus, then it scrolls".
- On blur the text scrolls back to the start and the ellipsis returns.
- Prefix and suffix never truncate before the input text; the input area has `min-width: 0` so it can shrink, the container never overflows its parent.
- Multi-line: wrap `word` by default; `wrap none` allowed (then it scrolls both ways). Vertical overflow shows a vertical [[Scrollbar and Scroll Container|scrollbar]] when the content exceeds the box; horizontal overflow (wrap none) shows a horizontal one. The caret is scrolled into view on edit and on caret movement.
- Multi-line minimum: 3 lines at the field's line height by default, configurable from 1; resize handle optional, vertical only, snaps to the line height, never below the minimum #needs-verification-as-design-choice.
- Label: an external label sits above the container with a 4, 4 and 2 dp gap, wraps, and aligns its left edge with the container's left edge; the floating label truncates with an ellipsis and the tooltip rule applies to the label control only; an external label wraps. Supporting text wraps to a second line at most 2 lines, then ellipsis, and its full text is exposed as the accessible description.
- Character counter: `n / max`, trailing in the supporting row, `body_small`.

## Behaviour

- Pointer: press places the caret; double-click selects a word; triple-click selects a line; press-drag selects; a press on the trailing clear button clears and keeps focus in the field. Pointer shape over the input area: text I-beam.
- Keyboard (focused single-line field):

| Keys | Result |
|---|---|
| Printable keys | insert text at the caret or replace the selection |
| Left, Right | move caret one character; with Ctrl one word; with Shift extend the selection |
| Home, End | caret to line start, end; with Shift extend; with Ctrl to text start, end |
| Ctrl+A | select all |
| Ctrl+C, Ctrl+X, Ctrl+V | copy, cut, paste (copy and cut do nothing in a password field) |
| Ctrl+Z, Ctrl+Shift+Z | undo, redo |
| Backspace, Delete | delete before, after the caret; with Ctrl one word |
| Enter | submit (single-line); newline (multi-line) |
| Tab, Shift+Tab | move focus to the next or previous control; in a multi-line field Tab moves focus too, unless the field sets `tab_navigates` false (then Tab inserts a tab and Escape then Tab leaves; documented in the field's description) |
| Escape | clears only in a search field (the field has role `searchbox`); in any other field it does nothing to the text and the key goes to the enclosing dialog or popup |
| Up, Down (multi-line) | move caret one line; Page Up, Page Down move one viewport minus 10 percent |

- Touch: a tap places the caret and shows the platform keyboard if the platform has one; a 48 dp hit area (see Sizing).
- IME: composition (pre-edit) text is shown inline at the caret with the platform's underline, and the candidate window is positioned at the caret and stays inside the window. Max length counts committed text only. The engine passes the caret rectangle to the platform; tess-ui draws no composition of its own (`tess-ui:docs/components/text-fields.md`).
- Max length: counts characters, not bytes; typing and paste are cut at the limit (`tre:docs/guide/text.md`, `max_length`); the counter shows `n / max`.
- Caret blink: when idle and focused the caret blinks 530 ms on, 530 ms off (the tess-ui `Caret_Blink` default; MD3 gives no value #needs-verification-as-design-choice); a keystroke or click restarts the cycle with the caret solid. Under reduced motion ([[14 Accessibility Basics]]) the caret is steady. The tre engine default is steady (`caret_blink` unset).

## Tooltip and overlay behaviour

The tooltip belongs to the control that carries the label or icon ([[ADR-0004 Tooltip rule]]): the field itself has no tooltip; a trailing icon button has one ([[Icon Button]]); the label of a [[Form Row]] may carry the row's documentation tooltip, never the field container. A text field that suggests values opens a [[Menu]] under the field; focus stays in the field, Up and Down move through suggestions, Escape closes the menu and then, if pressed again, does nothing else. Full tooltip rules: [[Tooltip]].

## Motion

- Label rise: 150 ms, easing `emphasized` per [[Motion]]; size changes at once where the engine cannot ease a font size (tess-ui, `tess-ui:docs/components/text-fields.md`).
- Border and indicator colour changes: `short3` (150 ms) at most.
- Reduced motion: no label glide, no colour fade, steady caret.

## Accessibility

- Role: `textbox` (single-line and multi-line), `searchbox` for a search field; a password field has role `textbox` with obscured value and the platform password hint ([WAI-ARIA textbox](https://www.w3.org/TR/wai-aria-1.2/#textbox)).
- Name: the visible label text. An external label is associated: the label node's text is the field's accessible name (tess-ui and tess-shell expose it as the `Label` property; AC-TXF-9). A field with a placeholder and no label uses the placeholder as the name and the shell warns when neither exists.
- Description: supporting text and error text are the accessible description; the field is invalid (`invalid`) while an error is shown.
- Required: a required field shows a text cue (an asterisk plus the words in the label or description), not colour only ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).
- Error: the error text is a live region, polite, announced once when it appears; the field is not re-announced on every keystroke.
- States exposed: disabled, read-only, invalid, expanded (when it owns a suggestion popup), multi-line.
- Focus indicator: 2 dp indicator or outline in `primary`; contrast at least 3 to 1 against the adjacent colour ([WCAG 1.4.11](https://www.w3.org/TR/WCAG22/#non-text-contrast)); text 4.5 to 1.
- See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Dark and light

All colours are roles ([[Colour Roles]]); the field has no literal colour. Under dark and light the filled container, outline, label and text are recomputed by the scheme; the field follows the system theme ([[Theme Following the System]]). AC-TXF-11 checks the contrast in both.

## Defaults

- Variant: outlined in config-style tools, filled elsewhere (project ADR).
- Density: from the container or project; the config tool default is `compact` (32 dp).
- Overflow: single-line `ellipsis` until focus; multi-line `wrap word`, 3 lines.
- Caret blink 530 ms, steady under reduced motion; selection `primary` at 30 percent.

## Acceptance criteria

- [ ] AC-TXF-1: Vertical centring, geometry check. For a single-line field at each density (default, compact, dense) and scale 1.0, 1.25, 2.0, the top of the text line box and the bottom of the text line box lie inside the container with a space above that differs from the space below by at most 0.5 dp. Pass: for 40/32/28 dp, space above equals space below ±0.5 dp (8/6/4 dp for the type roles in Sizing). Owner feedback F7.
- [ ] AC-TXF-2: Pixel check. In a render of a single-line field with the text "Hg" at compact density, the vertical centre of the glyph bounding box (cap height top to descender bottom) is within 1 px of the vertical centre of the container. Pass: offset at most 1 px.
- [ ] AC-TXF-3: Token test. The single-line container heights, without a floating label, equal 40, 32 and 28 dp for default, compact, dense and the horizontal paddings equal 12, 8, 8 dp; an external label never changes the container height. Pass: values equal with and without an external label.
- [ ] AC-TXF-4: Geometry check. Horizontal text alignment: the left edge of the first glyph lies at container left edge plus horizontal padding plus leading icon plus gap if any (±1 px). Pass: within 1 px.
- [ ] AC-TXF-5: Scripted input and geometry check. Set a single-line field to a string at least 3 times wider than the content box, blur: the rendered text ends with the ellipsis glyph and no pixel of text lies outside the container. Pass: ellipsis present, zero pixels of text beyond the container bounds. Owner feedback F5 class.
- [ ] AC-TXF-6: Scripted input. Focus the same field and press End: the ellipsis is gone, the caret x lies inside the content box, and the end of the text is visible. Press Home: the start is visible. Pass: caret inside the content box at both keys.
- [ ] AC-TXF-7: Scripted input. Ctrl+A selects all text; Home, End, Shift+Home, Shift+End move and extend as the Keyboard table says; Tab leaves a single-line field and the next focusable control gets focus; Escape leaves the text unchanged in a non-search field and clears it in a `searchbox`. Pass: field value and selection equal the table in each step.
- [ ] AC-TXF-8: Scripted input. Multi-line: Enter inserts a newline; Page Down moves the caret by the viewport height minus 10 percent (±1 line); Ctrl+End scrolls the caret into view; Tab moves focus out of the field (unless `tab_navigates` is false and documented, then Escape then Tab does). A vertical scrollbar thumb exists when content exceeds the box and does not exist otherwise. Pass: values equal.
- [ ] AC-TXF-9: AT tree assertion. The field node has role `textbox` (or `searchbox`), a non-empty name equal to the label text, an accessible description equal to the supporting or error text when present, `invalid` true while an error is shown, `read_only` and `disabled` set from the state, and `obscured` true for a password. Pass: all properties equal.
- [ ] AC-TXF-10: Scripted input. A read-only field takes focus, allows selection and copy, rejects typing; a disabled field takes no focus and no key. A password field rejects copy and cut. Pass: value unchanged, clipboard unchanged.
- [ ] AC-TXF-11: Contrast script. In the light and dark scheme the pairs input text on container, label on container, supporting text on surface, error text on surface have contrast at least 4.5 to 1; the active indicator or outline against the surface at least 3 to 1. Pass: ratios at or above the limits.
- [ ] AC-TXF-12: Token test. The state colours (rest, hover, focus, error, disabled) of the filled and outlined variants resolve to the roles in the State table and no literal colour exists in the field's stylesheet. Pass: every colour property is a role reference.
- [ ] AC-TXF-13: Scripted input. A field with `Max_Length` n rejects the (n+1)th character and the counter reads `n / n`. Pass: text length equals n.
- [ ] AC-TXF-14: Scripted input. IME: an injected pre-edit string shows inline, the candidate rectangle reported to the platform lies inside the window, and a commit inserts the text once. Pass: value and rectangle as stated (engine support dependent: record `not testable` where the platform cannot be driven).
- [ ] AC-TXF-15: Scripted input and review. With reduced motion set, the caret does not blink and the label does not glide. Pass: caret visible in all frames of a 2 s capture.
- [ ] AC-TXF-16: Geometry check. No tooltip is bound to the field container, only to the label or to an icon button inside the field ([[ADR-0004 Tooltip rule]]); hover over the container shows none within 600 ms. Pass: zero tooltips.
- [ ] AC-TXF-17 (geometry check): label placement by density. At compact and dense a field with a label shows the label above the container: label bottom edge to container top edge is 4 dp at compact and 2 dp at dense (plus or minus 0.5 dp), the container height is 32 and 28 dp, and no label pixel lies inside the container. Pass: gaps and heights as stated, also when the floating variant was requested.
- [ ] AC-TXF-18 (AT tree assertion): the accessible name of a labelled field is the `Label` property in both placements and does not change when the placeholder is shown or hidden; a field with a placeholder and a label exposes the placeholder only as description or hint. Pass: name equals the label text in every state.
- [ ] AC-TXF-19 (geometry check): at default density the floating label variant has a 56 dp container with the label inside (the label line within the top 16 dp), and the external variant has a 40 dp container with the label above; both keep the input text centred in the space below the label (AC-TXF-1 applies to the input area). Pass: heights 56 and 40; the vertical centring tolerance of AC-TXF-1.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TextField_View.tdl`, `TextField_Stylesheet.tdl` | partly meets: roles for container, indicator, label, icons and error colours match the State table (AC-TXF-12 meets for the TextField view); filled corner 4 dp top, indicator 1 dp rest and 2 dp focus match; disabled is a whole-field 0.38 opacity, not the per-part 4, 12 and 38 percent scheme (AC-TXF-12 fails on disabled); no density setting (AC-TXF-3 fails); suggestions not keyboard-reachable (AC-TXF-7 partial); IME composition not drawn by tess-ui (AC-TXF-14 depends on engine) |
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (config field, `TextInput` 32 px high, padding 8 left and right) | partly meets: heights equal compact (AC-TXF-3 meets for compact); vertical centring by hand-tuned top and bottom padding because the engine `text_input` has no vertical-align property (AC-TXF-1 and AC-TXF-2 unmeasured; F7 reported failing in the 2026-11-20 demo); ellipsis until focus via engine `overflow` is configurable and not verified in the app (AC-TXF-5, AC-TXF-6 unmeasured) |
| tess-shell | `tess-shell:src/tess_shell/shipped/TextInput/TextInput_Module.tdl` | partly meets: role textbox with `Label` else `Placeholder` as name (AC-TXF-9 meets for name), `Read_Only`, `Max_Length`, `Password` keys exist; no density, no error or helper text, no label variants (AC-TXF-3, AC-TXF-11, AC-TXF-12 absent) |
| tre | engine `text_input` node (`tre:docs/guide/text.md`) | not applicable (primitive): provides `overflow`, `wrap`, `max_length`, `read_only`, `obscured`, `caret_blink`, `caret_color`, `selection_fill`; no vertical-align property; draws no focus ring or state layer; IME candidate window drawn by the platform at the caret |
| tess-ui | same files, Dimensions and defaults | differs: no density setting (container fixed, AC-TXF-3 fails); config field `TextInput` 32 high with hand-tuned vertical padding where the spec derives 6 (AC-TXF-1); disabled is whole-field 0.38 opacity |

Evidence: F5, F7 in [[Owner Feedback 2026-11-20]].

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TextField_View.tdl`, `tess-ui:src/tess_ui/views/TextField_Stylesheet.tdl`, `tess-ui:docs/components/text-fields.md` | exists, see Status in code; not settable: line height and tracking of the typed text (`_text_field_props` drops `line_height` and `letter_spacing`) |
| tess-shell | `tess-shell:src/tess_shell/shipped/TextInput/TextInput_Module.tdl` | exists; not settable: line height and letter spacing of the typed text (no `Line_Height` key on `TextField`) |
| tre | `tre:docs/guide/text.md` (text input properties) | engine primitive; hardcoded: `text_input` takes no `line_height` or `letter_spacing` |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Container height 40, 32, 28 dp instead of 56 dp (MD3 height from Material Web `textfield/demo` min-height 56 px and the label plus padding stack #needs-verification) | desktop density, config panels hold many fields | [[ADR-0002 Desktop density levels and target sizes]] |
| Body text `body_medium` at compact and dense | 20 dp line box fits 32 and 28 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| Label may be external (above the field), and is the only placement at compact and dense | a floating label does not fit a 32 or 28 dp container; forms with aligned label column ([[Form Row]]) | [[ADR-0023 Text Field label placement by density]] |
| Keyboard focus indicator is the 2 dp indicator or outline, no extra ring | MD3 text fields draw no separate ring | [[ADR-0009 State layer percentages]] |
| Escape clears only in search fields | keyboard-first rule | [[ADR-0010 Document structure of the specifications]] (convention only) |

## Sources

- [Material Web text-field docs](https://github.com/material-components/material-web/blob/main/docs/components/text-field.md): labels, aria-label for external labels, textarea rows.
- [Material Web filled text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-filled-text-field.scss): indicator heights 1 and 2 px, disabled opacities 0.38 and 0.04, container shape extra small top, `caret-color` primary, body_large input, body_small supporting text.
- [Material Web outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss): outline width 1 px, focus 2 px, disabled outline opacity 0.12, container shape extra small.
- [Material Web typescale tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss): body large 1 rem on 1.5 rem; body medium 0.875 rem on 1.25 rem; body small 0.75 rem on 1 rem.
- [Material Components Android TextField](https://github.com/material-components/material-components-android/blob/master/docs/components/TextField.md): icon minimum size 48 dp, minimum width 56 dp without label, maximum 488 dp.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.1, 1.4.11, 2.5.8.
- tre text input properties: `tre:docs/guide/text.md`.
- MD3 text field 56 dp container and the label stack could not be fetched from m3.material.io (a script-rendered site) and are marked #needs-verification.
