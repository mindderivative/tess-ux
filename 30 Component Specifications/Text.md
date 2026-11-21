---
title: Text
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, content, text]
related: ["[[Text Field]]", "[[Link]]", "[[Text Selection]]", "[[03 Typography and Text Rules#Truncation across components|Text Truncation]]", "Text Measurement", "[[Text|Rich Text]]", "[[Text|Rich Text Span]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Form Row]]", "[[List Item]]", "[[Button]]", "[[Typography]]", "[[Colour Roles]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[03 Typography and Text Rules]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Typography]]", "[[Colour Roles]]", "[[10 Layout Overflow and Scrolling]]"]
---

# Text

> [!info] Summary
> The text element: a run of read-only text set in one of the 15 Material Design 3 (MD3) type roles, with wrapping, ellipsis, optional selection and optional links. MD3 counterpart: the [type scale](https://m3.material.io/styles/typography/overview). The editable text box is [[Text Field]]. Source of truth in code: see the last section.

## Purpose

Every label, heading, description, value and message in a Tesserae interface is a text element. This note holds the rules for the element itself: which type role it uses, when it wraps, how it ends when it does not fit, how it is selected, how it is centred in its control and how it reads to a screen reader. The principles for overflow and centring are in chapter [[10 Layout Overflow and Scrolling]]; this note applies them to the element and states what a test measures. Type values are in [[Typography]].

## When to use and not

- Use when: the words are not edited by the user: labels, headings, body text, values, status lines.
- Do not use when: the user edits the words ([[Text Field]]), the words activate something (a whole-line [[Link]], a [[Button]]), or part of a longer text is a link (use rich text runs with a `link`, [[Text|Rich Text]]).
- A text that names a control belongs to that control's note (button label, [[List Item]] headline); this note states the rules they share.

## Anatomy

1. Content: the characters, in one style or in runs of different styles ([[Text|Rich Text Span]]).
2. Line box: the line height of the type role; a block of lines stacks line boxes.
3. Ellipsis (when truncated): the glyph `…` (U+2026) ending the last visible line.
4. Selection highlight (when selectable): the role `primary` at 30 percent behind the glyphs.
5. Link spans (optional): runs with a `link`, `primary` and underlined.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Single line | labels, values, titles in a row | `Wrap: none`, `Overflow: ellipsis` |
| Wrapping block | descriptions, help text, dialog body | `Wrap: word`, optional `Max_Lines` |
| Heading | section titles | `Heading` level 1 to 6 for assistive technology |
| Selectable | values the user may copy (paths, ids, errors) | `Selectable: true` |
| Rich | text with links, bold or code runs | `Runs` |
| Marquee | a one-line text that scrolls instead of truncating | the shell's Marquee text module; allowed only where the module note says so, never as a replacement for the ellipsis rule |

## States

Static text has few states; the colour carries meaning through roles, not through state layers.

| State | Visual change | Token values |
|---|---|---|
| Rest | colour from the role of the context: `on_surface` for primary text, `on_surface_variant` for secondary and supporting text | [[Colour Roles]] |
| Selected (a range of characters) | highlight `primary` at 30 percent, glyph colour unchanged | `tre:docs/guide/text.md` |
| Truncated | ends with `…`; tooltip on the owning control shows the full text | [[10 Layout Overflow and Scrolling]] |
| Disabled (inside a disabled control) | `on_surface` at 38 percent | [[State Layers]] |
| Error text | `error` role | [[Colour Roles]] |
| Focus (selectable text) | no ring on the text; the text is not a tab stop unless it is a link | [[Focus Ring]] |

Text on a coloured container takes the matching `on_` role (`on_primary_container` on `primary_container`) so that contrast holds in both schemes.

## Tokens used

- Colour roles above; `Foreground` is required and is always a role reference, never a literal ([[Colour Roles]]).
- Type: one of the 15 roles of [[Typography]] (`display_*`, `headline_*`, `title_*`, `body_*`, `label_*`); tess-ui and tess-shell name the role (`Typography_Role`) or the shell's five roles ([[Typography]], mapping table). A text that sets size and family by hand without a role is a defect unless the note of the owning component says why.
- Role choice by use at the three densities:

| Use | default | compact and dense |
|---|---|---|
| Control label, row label, list headline, menu item | `body_large` (16 on 24) or `label_large` (14 on 20) for buttons | `body_medium` (14 on 20) |
| Supporting text, captions, helper and error text | `body_small` (12 on 16) | `body_small` |
| Section title in a panel | `title_medium` (16 on 24) | `title_small` (14 on 20) |
| Dialog title | `headline_small` (24 on 32) | `title_large` (22 on 28) |
| Page or window title | `headline_medium` (28 on 36) | `headline_small` |
| Display text, clocks, large numerals | `display_*` | `headline_*` |

  The mapping is a Tesserae choice built on the role sizes of [Material Web typescale tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss) and the density rule that body text is 14 dp at compact and dense ([[ADR-0002 Desktop density levels and target sizes]]) #needs-verification-as-design-choice.
- Tracking: the engine draws roles with no tracking unless the theme sets `MD3_TRACKING` (`tess-ui:docs/components/text.md`); the per-role values are in [[Typography]].
- Spacing: text has no padding of its own; the container supplies it ([[Spacing and Density]]).

## Sizing and density

- A single-line text is as high as the line height of its role: 24, 20, 16 dp for `body_large`, `body_medium`, `body_small` ([[Typography]]). Density changes the role used (table above), not the role's own size.
- Width: a text that hugs its content is the measured text width plus 2 px (`tre:docs/guide/text.md`, "Sizing text to its content", Text Measurement); a text in a flex row has `Min_Width 0` so it can shrink and truncate ([[10 Layout Overflow and Scrolling]]).
- Minimum text size: 11 dp (`label_small`) is the smallest role; no text is set below 11 dp. Body text in a wrapping block has a minimum container width of 120 dp ([[10 Layout Overflow and Scrolling]]).
- Maximum measure: a reading paragraph is at most 840 dp wide ([[10 Layout Overflow and Scrolling]]).
- A selectable text and a link have a pointer hit area of at least 24 by 24 dp when they act alone (a standalone link); inline links in a sentence are exempt ([WCAG 2.2 SC 2.5.8](https://www.w3.org/TR/WCAG22/#target-size-minimum), exception for inline targets).

## Layout and overflow

This section applies chapter [[10 Layout Overflow and Scrolling]]; it does not restate its principles.

- Single line (`Wrap: none`): content that exceeds the width is cut and ended with `…` (`Overflow: ellipsis`). Silent clipping (`Overflow: clip`) of text that can exceed its box is a defect (F5). The default of the engine is `clip` (`tre:docs/guide/text.md`; `Overflow` default `clip` in tess-ui and tess-shell), so a text that can exceed its box sets `ellipsis` explicitly, or the project's stylesheet does it for every Text (`Label { Overflow: ELLIPSIS }`, `tess-shell:src/tess_shell/shipped/Label/Label_Module.tdl`).
- Paths and file names: middle truncation keeps the last segment ([[03 Typography and Text Rules#Truncation across components|Text Truncation]]); this is a project computation, the engine ellipsis ends the line only.
- Wrapping block (`Wrap: word`): breaks at word boundaries; a word longer than the container breaks at a glyph boundary; line height from the role; `Max_Lines` cuts at n lines and the last ends with `…` when `Overflow` is `ellipsis`. Without `Max_Lines` the block grows and its container scrolls ([[Scrollbar and Scroll Container]], [[ADR-0003 Scrollbar rule]]).
- Alignment: `Text_Align` is `start`, `center` or `end`; `start` is the default and means left in a left-to-right locale. Numbers in columns align `end`. A centred label is centred in its box, not by padding.
- Vertical centring: a single-line text in a control is centred on the control's content box by construction: the line box has the role's line height and the space above equals the space below within 1 px at every density ([[10 Layout Overflow and Scrolling]], AC-DEN-9). The engine places a text node at the top of its box; a control centres it by `Align_Content: center` (tess-ui, tess-shell) or by computing equal padding, never by a hand-tuned asymmetric padding (F7). A project whose engine has no vertical-align property computes the padding from the control height.
- Baseline: when a text shares a row with an icon or a value, the row centres the line boxes; baseline alignment between texts of different roles in one row is the row's property, not the text's ([[Form Row]]).
- Hugging width: `Width` and `Height` default to `fit-content` in tess-shell because tre lays out an unset width as 0 (`tess-shell:src/tess_shell/schema/blocks.py`, `shell-vault:41 TDL Reference/Block Reference.md`, Text).

## Behaviour

- Pointer: static text takes no pointer events unless it is selectable or has a link; hover shows no change except the I-beam over selectable text and a hand over a link (`tre:docs/guide/text.md`).
- Selection (`Selectable: true`): press and drag selects; double-click selects a word; triple-click selects a line; a drag that starts in one selectable text and moves into others selects across them; a press anywhere else clears the selection; the selection is `primary` at 30 percent ([[Text Selection]], `tre:docs/guide/text.md`).
- Keyboard (selectable text with a selection): Ctrl+A selects all of the text, Ctrl+C copies, Shift+Left, Shift+Right extend by a character, Ctrl+Shift+Left and Ctrl+Shift+Right by a word, Shift+Up and Shift+Down by a line, Shift+Home and Shift+End to the start and end of the line (`tre:docs/guide/text.md`). Unselected static text is not focusable and not in the Tab order; a selectable text that a keyboard user must be able to copy is reachable through the focusable control that owns it (the row, the field label), or its container exposes a "Copy" command; a text that is the only copy of an error message or a path is selectable and the owning control exposes a copy action #needs-verification-as-design-choice.
- Links in text: [[Link]] and [[Text|Rich Text]].
- Touch: a long press selects a word on a selectable text where the platform does; otherwise as pointer.
- IME: not applicable (static text takes no composition).

## Tooltip and overlay behaviour

Static text opens no overlay. When the text is truncated, the control that carries the text shows the full text in a tooltip ([[ADR-0004 Tooltip rule]], [[Tooltip]]): the tooltip is on that control (the row, the label, the cell), not on a group, and appears only while the text is truncated. The full text is also available by selection and copy where the text is selectable, and through the accessible name; a tooltip is never the only way to read it ([[14 Accessibility Basics]]).

## Motion

None. A text that changes its content changes at once; a marquee text scrolls (shell Marquee module) and respects reduced motion by stopping and truncating with an ellipsis ([[14 Accessibility Basics]]).

## Accessibility

- A static text is not an accessibility node of its own in tre: "a text node's words are not exposed alone, so the block that holds them carries the `Label`" (`shell-vault:41 TDL Reference/Block Reference.md`). The accessible name of a control comes from its visible text or its `Label` property; a text beside a control is associated with it as the control's name ([[Form Row]]).
- A selectable text, a selected range or a text with a link is exposed as a text container: a label role, a run per line and per link stretch, each link a `link` node with its URL; the selection is reported so a screen reader can read it and move through it (`tre:docs/guide/accessibility.md`, "Text, selection and links").
- Headings: `Heading` 1 to 6 exposes the role `heading` with the level (tess-ui `Heading`); a title that looks like a heading but has none fails AC-TXT-9. Heading levels do not skip (a level 3 follows level 2 or 3).
- Language: the content language is exposed where the engine allows it #needs-verification (tre accessibility page does not document a language property).
- Live text: a text that changes after the user acted (a status line, a count, an error) is a polite live region (tess-ui `A11y { Live: polite }`); text that updates every second (clocks) is not live.
- Contrast: normal text 4.5 to 1, large text (at least 24 dp, or 18.66 dp bold) 3 to 1, against its container, in both schemes ([WCAG 1.4.3](https://www.w3.org/TR/WCAG22/#contrast-minimum)). Text spacing: a project that lets the user change line height to 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 times the font size loses no content ([WCAG 1.4.12](https://www.w3.org/TR/WCAG22/#text-spacing)) #needs-verification: the engine has no user text-spacing setting.
- Text is never the image of text; icons that carry meaning have a text name.
- See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Dark and light

The colour is a role; the scheme recomputes it ([[Theme Following the System]]). The contrast criterion runs in both schemes. A literal colour in a text style is a defect.

## Defaults

- Role: `body_medium` in a control at compact and dense, `body_large` at default; `Wrap: word` for a block (engine default), `none` for a label.
- `Overflow: ellipsis` for every text that can exceed its box (a project default, not the engine's).
- `Text_Align: start`; not selectable; no heading; foreground `on_surface`.
- The engine default `clip` is not accepted as the project default (see AC-TXT-3).

## Acceptance criteria

- [ ] AC-TXT-1 (token test): every text in a stylesheet or view names a type role of [[Typography]] and a `Foreground` that is a role reference; no text sets only a literal size and colour. Pass: zero violations in a lint over the project's views and stylesheets.
- [ ] AC-TXT-2 (token test): the type role values equal the table of [[Typography]] (size, line height, weight; tracking where the theme sets it): `body_large` 16 on 24, `body_medium` 14 on 20, `body_small` 12 on 16, `label_large` 14 on 20, `title_medium` 16 on 24. Pass: values equal.
- [ ] AC-TXT-3 (scripted input): a single-line text with `Wrap: none` set to a string at least 3 times wider than its box ends with `…` and no pixel of text lies outside the box; the same text in a flex row next to a fixed-width icon does not push the icon out of the container. Pass: ellipsis present, zero pixels outside, icon position unchanged (F5).
- [ ] AC-TXT-4 (geometry check): a wrapping block 200 dp wide with `Wrap: word` and a 600-character text has no line wider than 200 dp; a single word of 40 characters without a break breaks at a glyph boundary and fits; with `Max_Lines: 3` the visible lines are 3 and the third ends with `…`. Pass: line widths at most the container, line count 3, ellipsis present.
- [ ] AC-TXT-5 (geometry check): a single-line text with the role `body_medium` in a control 32 dp high has the space above its line box and below it differing by at most 1 px; the same at 40 dp with `body_large` and at 28 dp with `body_medium`, at scale 1.0, 1.25 and 2.0. Pass: difference at most 1 px (AC-DEN-9, F7).
- [ ] AC-TXT-6 (pixel check): a render of "Hg" in a 32 dp control has the vertical centre of its glyph bounding box within 1 px of the control's vertical centre. Pass: offset at most 1 px.
- [ ] AC-TXT-7 (scripted input): on a selectable text, double-click selects the word under the pointer, triple-click selects the line, press-drag selects the dragged range, a press elsewhere clears it, Ctrl+A selects all, Ctrl+C places the selected text in the clipboard, and the highlight is the role `primary` at 30 percent with the glyph colour unchanged. Pass: selection range, clipboard and highlight colour equal.
- [ ] AC-TXT-8 (scripted input): a drag from one selectable paragraph into the next selects the rest of the first, the start of the second and every selectable text between; the drag over a non-selectable node keeps the selection it had. Pass: selection ranges equal.
- [ ] AC-TXT-9 (AT tree assertion): a `Heading: 2` text has role `heading` and level 2; a selectable text with a link exposes a text container with a `link` node holding its URL; a selection is reported; headings in a window do not skip levels. Pass: roles, levels and URL equal.
- [ ] AC-TXT-10 (contrast script): in light and dark, `on_surface` text on `surface`, `on_surface_variant` on `surface`, `error` text on `surface`, and each `on_*` text on its container have contrast at least 4.5 to 1 (3 to 1 for text of 24 dp and larger). Pass: ratios at or above the limits.
- [ ] AC-TXT-11 (scripted input): a truncated text shows the tooltip of its owning control after the hover delay with the full string, none while it is not truncated, and none on its group ([[ADR-0004 Tooltip rule]]). Pass: tooltip text equals the full string when truncated, zero otherwise.
- [ ] AC-TXT-12 (geometry check): no text in the project is painted below 11 dp and a text that hugs its content measures width plus 2 px within 1 px of the shaper's measure at scale 1.0 and 2.0. Pass: sizes and widths within tolerance.
- [ ] AC-TXT-13 (token test): with reduced motion set, a marquee text does not scroll and ends with `…`. Pass: no frame-to-frame offset in a 2 s capture, ellipsis present.
- [ ] AC-TXT-14 (review): the project's stylesheet sets `Overflow: ellipsis` on every Text and Label rule that has no scroll container ancestor, and records any exception with its reason. Pass: reviewer finds no silent clip.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/` (the `Text` node of the engine bridge), `tess-ui:docs/components/text.md`, `tess-ui:src/tess_ui/tokens.py` | partly meets: `Typography_Role`, `Wrap`, `Overflow`, `Max_Lines`, `Text_Align`, `Selectable`, `Runs`, `Heading` exist (AC-TXT-1, AC-TXT-4, AC-TXT-7, AC-TXT-9 meet as documented, unmeasured); `Foreground` is required so the view does not build without it, which supports AC-TXT-1; `Overflow` defaults to `clip` and the ellipsis is opt-in per node (AC-TXT-14 fails unless each view sets it); per-role tracking is off unless the theme sets `MD3_TRACKING` (AC-TXT-2 partial); no density rule for the role choice (the role table above is not enforced) |
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` | partly meets: the directory text neither wrapped nor ellipsised and ran past its container in the 2026-11-20 demo (AC-TXT-3 fails, F5); single-line text top-aligned in fields (AC-TXT-5 fails, F7) |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/binder/tables.py`, `tess-shell:src/tess_shell/shipped/Label/Label_Module.tdl`, `shell-vault:41 TDL Reference/Block Reference.md` | partly meets: `Text` with `Wrap`, `Max_Lines`, `Selectable`, `On_Link`, `Overflow` (`CLIP` or `ELLIPSIS`) exists; `Label` sets `Wrap: NONE`; the default is `CLIP` (AC-TXT-14 fails by default); shell type roles are 5 names (`caption` and four more) mapped to MD3 roles in [[Typography]]; `Width` and `Height` default to `fit-content` (a bridge for tre); no `Heading` property in the Text block table of the block reference (AC-TXT-9 absent for headings) |
| tre | `tre:docs/guide/text.md`, `tre:docs/guide/accessibility.md`, `tre:docs/reference/window.md` | meets as the primitive: `wrap`, `max_lines`, `overflow` (`clip`, `ellipsis`), `align`, `selectable`, spans with `link`, selection model, measuring (`measure_text`), accessibility text container; draws a text at the top of its box (no vertical align), so centring is the parent's job (AC-TXT-5) |

Evidence: F5, F7 in [[Owner Feedback 2026-11-20]].

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:docs/components/text.md`, `tess-ui:src/tess_ui/tokens.py` | exists, partial |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:src/tess_shell/shipped/Label/Label_Module.tdl` | exists, partial |
| shell vault | `shell-vault:41 TDL Reference/Block Reference.md` | spec of the block |
| tre | `tre:docs/guide/text.md` | engine primitive |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Body text 14 dp (`body_medium`) in controls at compact and dense where MD3 uses `body_large` 16 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Ellipsis rule for every single-line text, middle truncation for paths | desktop content such as paths and file names | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Selection and copy of read-only text is a property of the text | desktop users copy values; MD3 is silent | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| No deviation in the 15 type roles and their sizes, line heights, weights | roles are MD3's | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- [Material Web typescale tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-typescale.scss): sizes, line heights, weights, tracking.
- tre text, selection and links: `tre:docs/guide/text.md`; accessibility: `tre:docs/guide/accessibility.md`.
- tess-ui text documentation: `tess-ui:docs/components/text.md`; shell block reference: `shell-vault:41 TDL Reference/Block Reference.md`.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.3, 1.4.12, 2.5.8.
- Chapter rules: [[10 Layout Overflow and Scrolling]], [[03 Typography and Text Rules]].
- The role-by-use table is a Tesserae choice; the MD3 mapping of roles to uses on m3.material.io could not be read (script-rendered site) and is marked #needs-verification.
