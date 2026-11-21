---
title: Text Selection
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, behaviour, text, engine, tesserae-specific]
related: ["[[Text Field]]", "[[Terminal]]", "[[Accessibility Tree]]", "[[Colour Roles]]", "[[State Layers]]", "[[Typography]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Tooltip]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[14 Accessibility Basics]]", "[[Colour Roles]]"]
---

# Text Selection

> [!info] Summary
> Text selection lets the user select static text (a `selectable` text node), copy it and have assistive technology read the selection; text inputs and terminals have their own selection. MD3 states no selection behaviour (Compose `SelectionContainer` is the nearest reference); this is a Tesserae specification built on the engine's behaviour.

## Purpose

Let users copy values (paths, versions, error messages) and read-only text, as the overflow rule needs: truncated text is available by selection and copy where the element is selectable ([[10 Layout Overflow and Scrolling]]).

## When to use and not

- Use when: the text is data a user may copy (a directory path, an error, a value shown in a read-only row).
- Do not use when: the text is a label inside a button or row (a selectable text claims the pointer over its box and would swallow the clicks of its parent); the text is editable ([[Text Field]]); the text is terminal output ([[Terminal]]).

## Anatomy

1. Selectable text node (`Selectable: true`).
2. Selection range (UTF-8 byte offsets; equal ends are a caret).
3. Highlight: the text colour at 30 percent behind the selected glyphs.
4. Cursor: I-beam over selectable text.
5. Selection in the accessibility tree: a text container with runs, link children and a text selection.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Single text | one label or value | press and drag within it |
| Multi-text document | paragraphs as separate nodes | a drag across nodes selects like one text |
| Input selection | text field | separate; Copy takes the focused input's selection first |
| Terminal selection | terminal | cell range `(start_row, start_col, end_row, end_col)` |

## States

| State | Visual change | Token values |
|---|---|---|
| Unselected | normal text | none |
| Selected range | highlight behind glyphs | text colour at 30 percent (engine); Tesserae requires a role-based colour, see Tokens |
| Caret (equal ends) | no highlight | none |
| Disabled | not selectable | disabled content 38 percent per [[State Layers]] |

## Tokens used

The engine paints the highlight in the text colour at 30 percent. The specification asks that the highlight resolves from role `secondary_container` and the selected text stays `on_secondary_container`, so contrast is guaranteed by the pair (Tesserae design choice, #needs-verification: MD3 gives no text-selection token in the Material Web tokens read for this note). Until the engine exposes a selection colour for static text, 30 percent of `on_surface` is accepted if AC-SEL-8 passes. A text input uses its own `selection_fill` ([[Text Field]]).

## Sizing and density

Not applicable: selection has no size. Hit area is the text box; a text smaller than 24 dp high still has a selectable box (inline text exception of WCAG 2.2 SC 2.5.8).

## Layout and overflow

- Selection never changes layout. Truncated text (ellipsis) is selected in full: the selection covers the hidden text, and Copy yields the whole string.
- Selection does not scroll the view while dragging over non-selectable content; it keeps what it had.
- Moving past the start or end of a text continues into the neighbouring selectable text.

## Behaviour

- Pointer: press and drag selects; double-click selects a word, triple-click a line; a press anywhere else clears the selection; a drag across selectable texts selects start text from the press to its end, whole texts between, and the last text up to the pointer; copy joins pieces with a newline.
- Keyboard: Ctrl+C copies; Ctrl+A selects all of the text the selection started in; Shift+Left and Shift+Right move the end by a character; Shift+Home and Shift+End to start or end; Ctrl+Shift+Left and Right by a word; Shift+Up and Shift+Down by a line keeping the column. While a static selection exists these keys belong to it: a scroll view does not scroll for Shift+Up and Shift+Down and `key_down` listeners do not hear Ctrl+Shift+Left or Right.
- Keyboard start: a selection can start only with the pointer in the engine today; a keyboard-only user cannot begin a selection in static text (fails WCAG 2.2 SC 2.1.1 as far as copying goes; candidate request: Tab-focusable selectable text with Shift+arrows from a caret). Copying through the tooltip or a copy command on the control is the alternative.
- Touch: long-press selection is not specified.
- Links: a span with `link` fires the `link` event on click (press and release with no selection in between), shows a hand cursor, and is styled by the author.

## Tooltip and overlay behaviour

Selecting text dismisses nothing; a tooltip on a truncated selectable text stays on the text node, not the row ([[ADR-0004 Tooltip rule]]).

## Motion

None: the highlight appears at once.

## Accessibility

A selectable, selected or linked text node is exposed as a text container (role label by default) with a run per line and per link boundary; each link is a `link` node with its URL; the selection is reported as a text selection and a reader can set it. Per-character positions assume left-to-right text. Built and checked against AccessKit's consumer; not tried with NVDA, VoiceOver or Orca ([[Accessibility Tree]]). The highlight contrasts 4.5 to 1 with the selected text (WCAG 2.2 SC 1.4.3).

## Dark and light

Highlight and text per scheme; the contrast check runs in both.

## Defaults

`Selectable` false; selection none; cursor default; highlight text colour at 30 percent.

## Acceptance criteria

- [ ] AC-SEL-1 (scripted input): press and drag over characters 2 to 8 of a selectable text sets `selection` to (2, 8) and Ctrl+C puts exactly that substring on the clipboard.
- [ ] AC-SEL-2 (scripted input): double-click selects the word under the pointer and triple-click selects the line.
- [ ] AC-SEL-3 (scripted input): with a selection, Shift+Right extends it by one character, Ctrl+Shift+Right by one word, Shift+Down by one line keeping the column, Ctrl+A selects the whole text.
- [ ] AC-SEL-4 (scripted input): a drag from paragraph 1 to paragraph 3 selects the tail of 1, all of 2 and the head of 3; Copy returns the pieces joined with newlines.
- [ ] AC-SEL-5 (scripted input): a press outside any selectable text clears every selection; a text that is not `selectable` swallows no click meant for its parent button.
- [ ] AC-SEL-6 (AT tree assertion): a selected text exposes a text selection with the same start and end as `selection`; a link exposes a `link` node with its URL, and the click action fires the `link` event with `href`.
- [ ] AC-SEL-7 (scripted input): text truncated with an ellipsis, selected and copied, yields the full string.
- [ ] AC-SEL-8 (contrast script): selected text over its highlight reaches 4.5 to 1 in light and dark for body, label and title roles.
- [ ] AC-SEL-9 (pixel check): the cursor over selectable text is an I-beam unless the node sets its own cursor, and a hand over a link.
- [ ] AC-SEL-10 (review): a value that users copy (path, version, error) is selectable, or has a copy command on its control; a reviewer finds none that is neither.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/schema/tess-ui-widget-schema.json` (`selectable` key on text widgets), `tess-ui:docs/components/text.md` | partly meets: key exists; AC-SEL-7, 8, 10 not verified; engine highlight colour fixed |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (`Text` `Selectable`, default false) | partly meets: key built; no copy command; AC-SEL-10 not verified |
| tre | `tre:docs/guide/text.md` (Rich text and selectable text), `tre:crates/engine-py/src/text_interaction.rs`, `tre:docs/guide/accessibility.md` (Text, selection and links) | meets AC-SEL-1 to 6, 9 by documented behaviour; highlight is the text colour at 30 percent and has no setting; no keyboard start (WCAG gap) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Static text selection with copy as a behaviour | desktop users copy paths and values | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Highlight from a role pair rather than the text colour at 30 percent | guaranteed contrast | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tre:docs/guide/text.md` (Rich text and selectable text), `tre:docs/guide/accessibility.md`, `tre:crates/engine-py/src/text_interaction.rs`.
- WCAG 2.2 SC 1.4.3, 2.1.1, 2.5.8: https://www.w3.org/TR/WCAG22/.
- Material Web tokens: no text-selection token was found in `tokens/versions/latest/sass` for the components read (text field uses `selection` handled by the browser) #needs-verification.
