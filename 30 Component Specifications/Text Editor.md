---
title: Text Editor
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, text-input, keyboard]
related: ["[[Text Field]]", "[[Text Box]]", "[[Form Row]]", "[[Scrollbar and Scroll Container]]", "[[14 Accessibility Basics#Reduced motion|Reduced Motion]]", "[[State Layers#Disabled scheme|Disabled State]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "[[Keyboard Navigation]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Text Editor

> [!info] Summary
> A Text Editor is a multi-line editable text field: the shell's module over a multi-line [[Text Field]]. The Material Design 3 counterpart is the [text field](https://m3.material.io/components/text-fields/overview) with several lines. This note covers what the module adds; the field's look, states and keys are in [[Text Field]]. Source of truth in code: see the last section.

## Purpose

Edits notes, descriptions or messages of several lines.

## When to use and not

- Use when: the user types more than one line.
- Do not use when: one line is enough (use [[Text Field]]); the text is read-only prose (use [[Text Box]]); the content is code with highlighting (post-v1).

## Anatomy

1. Field: a multi-line [[Text Field]], `Width` 320 dp by default, `Lines` 4.
2. Placeholder: `Text Editor::placeholder`, shown while empty.
3. Name: `Label`, else the `Placeholder`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Wrapped | Default (`Wrap: WORD`) | breaks lines at the width by word |
| Unwrapped | `Wrap: NONE` | keeps each line whole and scrolls sideways |
| Read-only | `Read_Only: true` | selectable and copyable, not editable |

## States

States, colours and tokens are those of [[Text Field]] (rest, hover, focus, error, disabled, read-only). This module adds: Empty (placeholder shown), Full (`Max_Length` reached: further input is refused and the supporting text may show the count), Disabled (`Enabled` false: no focus, no key, opacity per [[State Layers#Disabled scheme|Disabled State]]).

## Tokens used

Container, label, placeholder, caret and selection tokens: see [[Text Field]]. Type `body_medium` at compact and dense, `body_large` at default (per [[Text Field]]).

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Height from `Lines` | lines x 24 + 16 | lines x 20 + 12 | lines x 20 + 8 | [[Text Field]] line box and vertical space; `Lines` 4 gives 112, 92, 88 dp; spec derived from the [[Text Field]] table #needs-verification-as-design-choice |
| Horizontal padding | 12 | 8 | 8 | [[Text Field]] |
| Default width | 320 | 320 | 320 | param `Width` |
| Minimum width | 48 | 48 | 48 | [[Text Field]] minimum so the field never collapses |

## Dimensions and defaults

The container is the outlined variant of [[Text Field]] #needs-verification-as-design-choice. Heights are for `Lines` 4.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | 112 | 92 | 88 | [[Text Editor]] (Sizing: lines x 24 + 16, lines x 20 + 12, lines x 20 + 8, for `Lines` 4) | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| container | min width | - | 48 | 48 | 48 | [[Text Editor]] (Sizing), [[Text Field]] | tess-ui: yes (style min_width); tess-shell: yes (Min_Width); tre: yes (min_width) |
| container | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.2 SC 2.5.8 | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| container | padding | `density.field_padding_x` | 8 12 8 12 | 6 8 6 8 | 4 8 4 8 | [[Text Field]] (horizontal 12, 8, 8; vertical 8, 6, 4), [[Spacing and Density]] | tess-ui: yes (style padding); tess-shell: yes (Padding); tre: yes (padding) |
| container | margin | - | N/A: the parent form row sets the outer space | N/A: same as the default column | N/A: as in Default | [[Form Row]] | tess-ui: yes (style margin); tess-shell: yes (Margin); tre: yes (margin) |
| container | gap | - | N/A: one text area; the placeholder overlays it | N/A: same as the default column | N/A: as in Default | [[Text Editor]] (Anatomy) | tess-ui: yes (style gap); tess-shell: yes (Spacing); tre: yes (gap) |
| container | border width | - | 1 | 1 | 1 | [[Text Field]] outlined variant (outline 1 dp, 2 dp when focused) | tess-ui: yes (style border_width); tess-shell: yes (Border_Width); tre: yes (border_width) |
| container | border color | `outline` | `outline` | `outline` | `outline` | [[Text Field]] (focus `primary`, error `error`), [[Colour Roles]] | tess-ui: yes (style border_color); tess-shell: yes (Border_Color); tre: yes (border_color) |
| container | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]], [[Text Field]] outlined variant; design choice, proposed ADR: text editor uses the outlined variant | tess-ui: yes (style corner_radius); tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| text | font | `body_large` | 16/24/400/0.5 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]], [[Text Field]] | tess-ui: via type role in the theme; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| container | icon size | - | N/A: the editor has no icon | N/A: same as the default column | N/A: as in Default | [[Iconography]] | tess-ui: via widget icon size; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]]; a field is flat | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |

## Layout and overflow

Wraps by word at the width (`Wrap: WORD`) or scrolls sideways (`NONE`); scrolls vertically when the text is taller than `Lines`; the caret stays in view. A scrollbar follows [[ADR-0003 Scrollbar rule]] ([[Scrollbar and Scroll Container]]). Vertical alignment: first line at the top padding.

## Behaviour

- Pointer: click places the caret; drag selects; double click selects a word; wheel scrolls.
- Keyboard: typing, arrows, Home, End, Shift selects, Ctrl+A, Ctrl+C, Ctrl+X, Ctrl+V; Enter inserts a newline (no submit event); Page Up and Page Down move by the viewport minus 10 percent. Tab must leave the field (AR-15); in the engine Tab inserts a tab character and there is no property that lets Tab through (tess-shell request T-048). Until then spec requires Escape then Tab to leave and the field's description says so.
- Touch: tap places the caret; long press selects a word.
- Events: `On_Changed` (`event.old`, `event.new`) and `On_Text_Commit` (`event.text`).

## Tooltip and overlay behaviour

No tooltip by default; a tooltip on the field (the control) is allowed for a hint that is not in the label or the placeholder ([[Tooltip]], ADR-0004). The field opens no overlay; an input-method popup is the platform's.

## Motion

The caret blinks steady under reduced motion ([[14 Accessibility Basics#Reduced motion|Reduced Motion]]); there is no other animation.

## Accessibility

- Role: `TEXTBOX`, multi-line; name `Label` else `Placeholder` (the author must give one); `read_only` and `disabled` from the state.
- Keys: as Behaviour; Tab must not trap focus (WCAG 2.2 SC 2.1.2).
- Announcements: the field does not announce typing; an error or a limit reached is announced politely once ([[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]).
- Contrast: text 4.5:1, the outline or indicator 3:1 ([[Text Field]]).

## Dark and light

Colours follow the scheme through [[Text Field]] tokens ([[Theme Following the System]]).

## Defaults

| Setting | Default |
|---|---|
| `Lines` | 4 |
| `Wrap` | `WORD` |
| `Width` | 320 dp |
| `Max_Length` | 0 (no limit) |
| `Read_Only` | false |

## Acceptance criteria

- [ ] AC-MOD-TED-1 (AT tree assertion): the node has role `TEXTBOX`, a non-empty name (`Label`, else `Placeholder`), `read_only` and `disabled` equal to the params.
- [ ] AC-MOD-TED-2 (scripted input): Enter inserts a newline and raises no submit; typing raises `On_Changed` once per change with `old` and `new`; setting `Text` from the module raises none.
- [ ] AC-MOD-TED-3 (scripted input): `Max_Length` 10: the eleventh character is refused and the text length stays 10.
- [ ] AC-MOD-TED-4 (scripted input): Tab moves focus out of the field, or, where the engine inserts a tab, Escape then Tab does and the field description states it; a keyboard-only user can leave the field.
- [ ] AC-MOD-TED-5 (geometry check): with `Lines` 4 the field is 112, 92 and 88 dp high at default, compact and dense and the horizontal padding 12, 8 and 8 dp.
- [ ] AC-MOD-TED-6 (scripted input): a 40 line text scrolls vertically; the caret line is inside the viewport after Ctrl+End; with `Wrap: WORD` no line exceeds the width.
- [ ] AC-MOD-TED-7 (pixel check): the placeholder shows while empty, in `on_surface_variant`, and disappears on the first character.
- [ ] AC-MOD-TED-8 (contrast script): text 4.5:1 and indicator 3:1 in Light, Dark and High_Contrast.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/TextEditor/TextEditor_Module.tdl`, `TextEditor_Module.py` | partly meets: role, name from `Label` or `Placeholder`, `Read_Only`, `Max_Length`, `Wrap`, `Lines`, events (meets AC-MOD-TED-1, -2, -3, -6, -7 by reading); Tab inserts a tab and cannot leave the field (fails AC-MOD-TED-4); no density, `Lines` height from the engine (AC-MOD-TED-5 unverified) |
| tess-shell | `tess-shell:src/tess_shell/shipped/TextEditor/TextEditor_Module.tdl` (dimensions) | not verified: the module sets only `Lines` and `Width`; padding, border, radius and font come from the engine `text_input` defaults, not read #needs-verification; letter spacing (tracking) has no hook in tess-shell |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (TextEditor) | exists |
| tess-ui | `tess-ui:src/tess_ui/views/TextField_View.tdl` | see [[Text Field]] (multi-line variant) |
| tre | `text_input` with `multiline` | partly meets: Tab inserts a tab unless `tab_navigates` is set (available since tre 0.6.8) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Heights by density, 40 dp single-line base | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Escape then Tab as the documented way out until the engine lets Tab through | WCAG 2.2 SC 2.1.2 | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- Material Web text field tokens (filled container height 56 px): https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-filled-text-field.scss (see [[Text Field]]).
- WCAG 2.2 SC 2.1.2 No Keyboard Trap: https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `tess-shell:src/tess_shell/shipped/TextEditor/TextEditor_Module.tdl` (comment on Tab, T-048).
