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

Palette entries map to roles: `background` is `surface_container_lowest`, `foreground` is `on_surface`, `selection` is `primary` at 30 percent with the text colour unchanged (as [[Text Selection]]), `cursor` is `primary` (Tesserae choices, #needs-verification as design). The 16 ANSI colours need 4.5 to 1 against `background` for text (WCAG 2.2 SC 1.4.3); black on a dark background fails in most schemes and needs a palette check. Font: a monospace role of [[Typography]].

## Sizing and density

Not applicable by density: the box follows `Columns`, `Rows` and the font; 80 by 24 at 13 dp is the shell default (#needs-verification). Minimum 20 columns by 5 rows in a panel.

## Dimensions and defaults

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| grid | height | - | 432 | 432 | 432 | [[Terminal]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: via rows and font_size (the box follows its grid and font) |
| grid | min height | - | 90 | 90 | 90 | [[Terminal]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| grid | min width | - | N/A: 20 columns need the cell width of the monospace face, which the engine reports | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| grid | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Terminal]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (padding, the cells draw inside it) |
| grid | margin | - | N/A: the parent container sets the outer space | N/A: same as default | N/A: same as default | [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| grid | gap | - | N/A: cells abut; the program places every character | N/A: same as default | N/A: same as default | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: cells abut and the program places every character |
| grid | border width | - | 0 | 0 | 0 | [[Terminal]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (stroke_width) |
| grid | border color | - | N/A: no border; focus is shown by the ring | N/A: same as default | N/A: same as default | [[Terminal]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (stroke_color) |
| focus ring | border width | - | 3 | 3 | 3 | [[Focus Ring]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring | border color | `secondary` | `secondary` | `secondary` | `secondary` | [[Focus Ring]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| focus ring | margin | `space.1` | 2 | 2 | 2 | [[Focus Ring]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no focus ring |
| grid | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| grid | font | - | 13/18/400/0 | 13/18/400/0 | 13/18/400/0 | design choice, proposed ADR Terminal monospace font size, [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: hardcoded in tre (font_size is a property, but MONOSPACE_FONT_FAMILY in engine-render/src/text.rs and the line height from the font metrics are fixed) |
| grid | icon size | - | N/A: the grid draws characters only | N/A: same as default | N/A: same as default | [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the grid draws characters only |
| grid | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

The grid is 80 by 24 cells: height 24 x 18 = 432 and minimum 5 x 18 = 90. The font row is the monospace face at 13 sp with 18 sp line height (the shell default size; #needs-verification-as-design-choice); [[Typography]] has no monospace role, so the face is a Tesserae choice. Nothing here changes with density: the box follows `Columns`, `Rows` and the font.

## Layout and overflow

- The box size equals the grid; a window resize changes `Columns` and `Rows` and tells the shell program.
- Overflow: scrollback by wheel; the engine terminal has its own history and no scrollbar; a scrollbar per [[Scrollbar and Scroll Container]] is required by [[ADR-0003 Scrollbar rule]] when history exists (candidate request).
- No ellipsis; lines wrap or cut as the program decides.
- Hit testing: the whole box.

## Behaviour

- Pointer: press and drag selects cells; wheel scrolls history.
- Keyboard: while focused every key goes to the shell except the reserved escape chord (below); Ctrl plus a letter sends its control byte (Ctrl+C interrupts), Ctrl+Shift+C copies the selection. Tab belongs to the shell.
- Keyboard trap and escape chord ([[ADR-0018 Terminal escape chord]]): the terminal takes every key, so without a way out a keyboard user cannot leave it by Tab (WCAG 2.2 SC 2.1.2). A terminal block reserves one chord, Ctrl+Shift+Escape, that moves focus to the next focusable element outside the terminal. The chord is reserved before the program receives keys, so it is never sent to the program, and it is shown in the block's description. A project may change the chord and must keep one. Ctrl+Shift+Escape is a proposed default: the shell's shortcut map needs a collision check (the chord is also the task-manager shortcut of Windows and of some desktops). The engine or framework must reserve the chord; the engine does not yet (candidate UXREQ).
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
- [ ] AC-BLK-TRM-3 (scripted input): with focus in the terminal, Ctrl+Shift+Escape (or the project's recorded replacement chord) moves focus to the next focusable node outside the terminal and a plain Tab does not ([[ADR-0018 Terminal escape chord]]). Pass: focused node id after each of the two inputs.
- [ ] AC-BLK-TRM-4 (contrast script): each of the 16 ANSI colours against the palette `background` has at least 4.5 to 1 in the light and the dark palette, or the palette marks the colour as decorative-only.
- [ ] AC-BLK-TRM-5 (token test): every palette entry resolves to a role of [[Colour Roles]].
- [ ] AC-BLK-TRM-6 (AT tree assertion): the terminal exposes role `textbox` with a name; with focus it is the focused node.
- [ ] AC-BLK-TRM-7 (pixel check): a focused terminal shows the focus ring with 3 dp thickness and 2 dp offset.
- [ ] AC-BLK-TRM-8 (scripted input): a TDL file that places a Terminal block cannot start a process: no `Command` key is accepted.
- [ ] AC-BLK-TRM-9 (scripted input): the escape chord is reserved before the program receives keys: with a recording program on the pty, pressing the chord delivers zero bytes to it, and every other key sequence (Escape, Ctrl+Shift+C, Ctrl+C, Tab) is delivered or handled as AC-BLK-TRM-2 states. Pass: byte count 0 for the chord and the expected bytes for the others.
- [ ] AC-BLK-TRM-10 (AT tree assertion): the terminal's description (accessible description) names the escape chord, and a visible hint or the block's help text shows it; a project that changes the chord keeps the description in step. Pass: description text contains the chord string in each project.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-shell | `shell-vault:41 TDL Reference/Block Reference.md` (Terminal, post-v1); no `Terminal` in `tess-shell:src/tess_shell/schema/blocks.py` | absent: fails AC-BLK-TRM-1 to 7, 9 and 10 (AC-BLK-TRM-8 holds by absence) |
| tess-ui | none | absent |
| tre | `tre:docs/guide/text.md` (Terminal), `tre:docs/reference/properties.md`, `tre:crates/engine-py/src/terminal.rs` | partly meets: PTY, grid, scrollback, palette, selection; no escape chord (fails AC-BLK-TRM-3, AC-BLK-TRM-9, AC-BLK-TRM-10; [[ADR-0018 Terminal escape chord]] needs the engine to reserve the chord); no scrollbar. Settable: the font family (`MONOSPACE_FONT_FAMILY`) and the line height (font metrics) cannot be set, `font_size` can (engine request) |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Terminal element with no MD3 counterpart | shell feature | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tre:docs/guide/text.md` (Terminal), `tre:docs/reference/properties.md`, `shell-vault:41 TDL Reference/Block Reference.md` (Terminal, R4).
- WCAG 2.2 SC 2.1.2 No Keyboard Trap: https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html. SC 1.4.3: https://www.w3.org/TR/WCAG22/.
