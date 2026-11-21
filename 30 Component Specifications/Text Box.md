---
title: Text Box
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, module, text]
related: ["[[Text]]", "[[Label]]", "[[Text Editor]]", "[[Text Selection]]", "[[03 Typography and Text Rules#Truncation across components|Text Truncation]]", "[[Scrollbar and Scroll Container]]", "[[State Layers#Disabled scheme|Disabled State]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[Motion]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# Text Box

> [!info] Summary
> A Text Box shows read-only text that wraps over several lines, with an optional line limit and optional selection. It is a thin module over the [[Text]] block; the editable counterpart is [[Text Editor]]. The Material Design 3 reference is the [type scale](https://m3.material.io/styles/typography/overview). Source of truth in code: see the last section.

## Purpose

Shows a paragraph, a description or a message that needs more than one line.

## When to use and not

- Use when: multi-line text the user reads and may select.
- Do not use when: the text is one line (use [[Label]]); the user edits it (use [[Text Editor]]); long content needs scrolling in its own region (put the Text Box in a [[Scrollbar and Scroll Container]]).

## Anatomy

1. Text: wraps by word at the box width.
2. Selection (optional): pointer selection and copy when `Selectable` is true.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Wrapped | Default, `Wrap: WORD` | wraps at the width |
| Unwrapped | `Wrap: NONE` | keeps lines as written, cut at the box (sideways scroll waits for the ScrollBox in code) |
| Limited | `Max_Lines` above 0 | shows at most that many lines, ends with an ellipsis |
| Selectable | `Selectable: true` | focusable, selection and copy |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | `on_surface` text | [[Text]] |
| Selected text (when `Selectable`) | Selection highlight in `primary` at a contrast of at least 3:1 against the text background ([[Text Selection]]) | [[Colour Roles]] |
| Focus (when `Selectable`) | Focus ring 3 dp, 2 dp offset | [[Focus Ring]] |
| Disabled | Opacity 0.5 (`TextBox:disabled`) | [[State Layers#Disabled scheme|Disabled State]] |
| Empty | No text, zero height unless `Height` is set | not applicable |
| Hover, pressed | Not applicable: no action | not applicable |

## Tokens used

Colour `on_surface`; type `body_medium` (shell body 14/20); optional `on_surface_variant`; no container.

## Sizing and density

| Measure | default | compact | dense | Note |
|---|---|---|---|---|
| Line height | 20 | 20 | 20 | `body_medium` |
| Minimum width | 120 | 120 | 120 | [[Text]]: a wrapping block is at least 120 dp wide |
| Maximum measure | 840 | 840 | 840 | [[Text]] |

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| text | height | `body_medium` | N/A: grows with the text, 20 per line (`Max_Lines` limits it) | N/A: same as the default column | N/A: as in Default | [[Text Box]] (Sizing, Layout) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height); tre: n/a: element absent in tre |
| text | min width | - | 120 | 120 | 120 | [[Text Box]] (Sizing), [[Text]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Width); tre: n/a: element absent in tre |
| text | min height | - | 20 | 20 | 20 | [[Text Box]] (Sizing: line height 20 for one line) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Height); tre: n/a: element absent in tre |
| text | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]]; no container, so no padding; code sets none | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Padding); tre: n/a: element absent in tre |
| text | margin | - | N/A: the parent column sets the outer space | N/A: same as the default column | N/A: as in Default | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Margin); tre: n/a: element absent in tre |
| text | gap | - | N/A: lines are spaced by the 20 dp line height, no extra gap | N/A: same as the default column | N/A: as in Default | [[Text Box]] (Sizing), [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Spacing); tre: n/a: element absent in tre |
| text | border width | - | 0 | 0 | 0 | [[Text Box]] (Tokens used: no container) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width); tre: n/a: element absent in tre |
| text | border color | - | N/A: the Text Box draws no border | N/A: same as the default column | N/A: as in Default | [[Text Box]] (Tokens used) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color); tre: n/a: element absent in tre |
| text | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]]; no container | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: n/a: element absent in tre |
| text | font | `body_medium` | 14/20/400/0.25 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]]; code shell `body` 14/400/20 | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: n/a: element absent in tre |
| text | icon size | - | N/A: the Text Box draws text only | N/A: same as the default column | N/A: as in Default | [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width, Height of the SVG block); tre: n/a: element absent in tre |
| text | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]], [[Text Box]] (no container) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation percentage); tre: n/a: element absent in tre |

## Layout and overflow

Wraps by word at the width; the caller gives a `Width` or places it in a column that sets one. Height grows with the text unless `Max_Lines` limits it. `Max_Lines` cuts with an ellipsis on the last line. Vertical alignment: top of the text box. A very long text belongs in a scroll container ([[10 Layout Overflow and Scrolling]]); the Text Box does not scroll itself.

## Behaviour

- Pointer: when `Selectable`, drag selects; double click selects a word; copy with Ctrl+C.
- Keyboard: when `Selectable` the box is focusable; Shift+arrows extend a selection, Ctrl+A selects all, Ctrl+C copies; otherwise not focusable.
- Touch: long press selects a word when `Selectable`.

## Tooltip and overlay behaviour

No tooltip by default. A cut text (`Max_Lines`) may show the full text in a tooltip on the Text Box itself (the control). 500 ms, 150 ms grace ([[Tooltip]]). The box opens no overlay.

## Motion

Not applicable: no animation.

## Accessibility

- Role: none, with `Label` = the text; a Text Box that holds the main content of a view takes `Role: TEXTBOX` and a `Label` from the author, and `read_only`.
- Keys: as Behaviour.
- Announcements: none; a changing message uses a polite announcement ([[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]).
- Contrast 4.5:1 for text, 3:1 for the selection highlight.

## Dark and light

Text and selection roles follow the theme mode ([[Theme Following the System]]).

## Defaults

| Setting | Default |
|---|---|
| `Wrap` | `WORD` |
| `Max_Lines` | 0 (no limit) |
| `Selectable` | false |

## Acceptance criteria

- [ ] AC-MOD-TBX-1 (scripted input): a 300 character text in a 200 dp box wraps by word, no line is wider than 200 dp and no word is split except a word wider than the box.
- [ ] AC-MOD-TBX-2 (pixel check): with `Max_Lines` 3 the text shows 3 lines and the third ends with `…`.
- [ ] AC-MOD-TBX-3 (scripted input): with `Selectable` true, a drag selects, Ctrl+A selects all and Ctrl+C copies the selected text; with false, none of these act.
- [ ] AC-MOD-TBX-4 (AT tree assertion): the node exposes the whole text as its name (or as the `TEXTBOX` value when it holds main content) and `read_only` true.
- [ ] AC-MOD-TBX-5 (static check): a Text Box that exceeds the window height is inside a scroll container (no content past the window edge).
- [ ] AC-MOD-TBX-6 (contrast script): text 4.5:1 against the surface and the selection highlight 3:1 against the text, in Light, Dark and High_Contrast.
- [ ] AC-MOD-TBX-7 (geometry check): line height 20 dp with `body_medium`; minimum width 120 dp.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/TextBox/TextBox_Module.tdl`, `TextBox_Module.py` | partly meets: word wrap, `Max_Lines`, `Selectable`, name = text, disabled look (meets AC-MOD-TBX-1, -2, -3, -4 by reading); sideways scroll of `Wrap: NONE` waits for the ScrollBox; no minimum width |
| tess-shell | `tess-shell:src/tess_shell/shipped/TextBox/TextBox_Module.tdl` (dimensions) | differs: no minimum width (spec 120); letter spacing (tracking) has no hook in tess-shell |
| shell-vault | `shell-vault:50 Design System/Standard Modules.md` (TextBox) | exists |
| tess-ui | none | not applicable: tess-ui uses [[Text]] |
| tre | `text` node | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Read-only multi-line text; no MD3 component | MD3 has type roles, not a text box | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- Material Web typography tokens: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-typescale.scss
- WCAG 2.2 SC 1.4.3 and 1.4.11: https://www.w3.org/TR/WCAG22/
- Tesserae sources: `shell-vault:50 Design System/Standard Modules.md`, `tess-shell:docs/guide/modules.md#textbox`.
