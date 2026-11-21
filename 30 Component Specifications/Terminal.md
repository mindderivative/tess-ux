---
title: Terminal
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, block, terminal, primitive, post-v1]
related: ["[[Text Selection]]", "[[Text Field]]", "[[Scrollbar and Scroll Container]]", "[[Colour Roles]]", "[[Focus Ring]]", "[[Typography]]", "[[14 Accessibility Basics]]", "[[Accessibility Tree]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[14 Accessibility Basics]]", "[[Colour Roles]]"]
aliases: ["Terminal node"]
---

# Terminal

> [!info] Summary
> A Terminal runs a shell on a pseudo-terminal and shows its character grid with a scrollback; it takes every key while focused. It has no MD3 counterpart. In the shell it is post-v1 and has no `Command` key by design (a module's Python supplies the process). Source of truth in code: see Status in code.

## Purpose

Embed a command line in a window or panel.

## When to use and not

- Use when: the user needs a real shell or program output with escape sequences.
- Do not use when: output is plain read-only text (a Text block with `Selectable`); input is one line (a [[Text Field]]).

## Anatomy

1. Grid of `Columns` by `Rows` cells in a monospace font (`Font_Size`).
2. Cursor, selection, scrollback (`Scrollback_Lines`).
3. Palette: 16 ANSI colours, foreground, background, cursor, selection.

## Variants

Not applicable: one variant; embedded in a panel or a window.

## States

| State | Visual change | Token values |
|---|---|---|
| Rest, unfocused | cursor drawn hollow or hidden by the owner | `palette.cursor` role |
| Focused (keyboard) | [[Focus Ring]] around the terminal box; cursor drawn | ring 3 dp, offset 2 dp, role `secondary` |
| Selection | cell highlight | `palette.selection` role |
| Exited | owner shows a message in the grid or an overlay; not specified here | none |

## Tokens used

Palette entries map to roles: `background` is `surface_container_lowest`, `foreground` is `on_surface`, `selection` is `secondary_container` at 100 percent with text `on_secondary_container`, `cursor` is `primary` (Tesserae choices, #needs-verification as design). The 16 ANSI colours need 4.5 to 1 against `background` for text (WCAG 2.2 SC 1.4.3); black on a dark background fails in most schemes and needs a palette check. Font: a monospace role of [[Typography]].

## Sizing and density

Not applicable by density: the box follows `Columns`, `Rows` and the font; 80 by 24 at 13 dp is the shell default (#needs-verification). Minimum 20 columns by 5 rows in a panel.

## Layout and overflow

- The box size equals the grid; a window resize changes `Columns` and `Rows` and tells the shell program.
- Overflow: scrollback by wheel; the engine terminal has its own history and no scrollbar; a scrollbar per [[Scrollbar and Scroll Container]] is required by [[ADR-0003 Scrollbar rule]] when history exists (candidate request).
- No ellipsis; lines wrap or cut as the program decides.
- Hit testing: the whole box.

## Behaviour

- Pointer: press and drag selects cells; wheel scrolls history.
- Keyboard: while focused every key goes to the shell, Ctrl plus a letter sends its control byte (Ctrl+C interrupts), Ctrl+Shift+C copies the selection. Tab belongs to the shell.
- Keyboard trap: the engine terminal takes every key, so a keyboard user cannot leave it by Tab (WCAG 2.2 SC 2.1.2). The specification requires a documented escape sequence (a chord the terminal does not forward, for example Ctrl+Shift+Tab or Escape then Tab #needs-verification) and a visible hint; the engine does not provide one yet (candidate UXREQ).
- Touch: not specified.

## Tooltip and overlay behaviour

Not applicable: no tooltip on the grid.

## Motion

Cursor blink 530 ms on and off is a Tesserae choice #needs-verification; with reduced motion the cursor is steady ([[14 Accessibility Basics]]).

## Accessibility

Role `TEXTBOX`, focusable, with a name (for example "Terminal"). The engine exposes the visible grid as text through `get("text")`; whether a screen reader reads new output is not verified (no live region on the terminal). New output is not announced automatically; the owner may announce a summary politely ([[Accessibility Tree]]). Not tried with Orca, NVDA or VoiceOver.

## Dark and light

Palette is two sets (dark and light) of the roles above; the terminal follows the scheme ([[Theme Following the System]]).

## Defaults

80 by 24, 5000 lines of scrollback (the example value; the engine default is not stated #needs-verification), role `TEXTBOX`, focusable.

## Acceptance criteria

- [ ] AC-BLK-TRM-1 (geometry check): `Columns` 80 and `Rows` 24 at font size 13 give a box whose width equals 80 cell widths and height 24 cell heights within 1 px.
- [ ] AC-BLK-TRM-2 (scripted input): with focus in the terminal, Ctrl+C sends byte 0x03 and Ctrl+Shift+C copies the selection without sending a byte.
- [ ] AC-BLK-TRM-3 (scripted input): the documented escape chord moves focus out of the terminal to the next focusable node and a plain Tab does not.
- [ ] AC-BLK-TRM-4 (contrast script): each of the 16 ANSI colours against the palette `background` has at least 4.5 to 1 in the light and the dark palette, or the palette marks the colour as decorative-only.
- [ ] AC-BLK-TRM-5 (token test): every palette entry resolves to a role of [[Colour Roles]].
- [ ] AC-BLK-TRM-6 (AT tree assertion): the terminal exposes role `textbox` with a name; with focus it is the focused node.
- [ ] AC-BLK-TRM-7 (pixel check): a focused terminal shows the focus ring with 3 dp thickness and 2 dp offset.
- [ ] AC-BLK-TRM-8 (scripted input): a TDL file that places a Terminal block cannot start a process: no `Command` key is accepted.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `shell-vault:41 TDL Reference/Block Reference.md` (Terminal, post-v1); no `Terminal` in `tess-shell:src/tess_shell/schema/blocks.py` | absent: fails AC-BLK-TRM-1 to 8 (AC-BLK-TRM-8 holds by absence) |
| tess-ui | none | absent |
| tre | `tre:docs/guide/text.md` (Terminal), `tre:docs/reference/properties.md`, `tre:crates/engine-py/src/terminal.rs` | partly meets: PTY, grid, scrollback, palette, selection; no escape chord (fails AC-BLK-TRM-3); no scrollbar |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Terminal element with no MD3 counterpart | shell feature | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tre:docs/guide/text.md` (Terminal), `tre:docs/reference/properties.md`, `shell-vault:41 TDL Reference/Block Reference.md` (Terminal, R4).
- WCAG 2.2 SC 2.1.2 No Keyboard Trap: https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html. SC 1.4.3: https://www.w3.org/TR/WCAG22/.
