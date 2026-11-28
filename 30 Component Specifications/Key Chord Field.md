---
title: Key Chord Field
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-28
tags: [component, input, keyboard, tesserae-specific]
related: ["[[Text Field]]", "[[Button]]", "[[Icon Button]]", "[[Form Row]]", "[[Key Chord Field|Key Chord Recorder]]", "[[11 Interaction#Shortcuts and conflicts|Global Shortcuts]]", "[[Keyboard Navigation]]", "[[Validation]]", "[[Forms and Settings]]", "[[Tooltip]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Shape]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[Text Field]]", "[[Button]]", "[[Spacing and Density]]", "[[State Layers]]", "[[Focus Ring]]"]
---

# Key Chord Field

> [!info] Summary
> A field that holds a keyboard shortcut as text (`Ctrl+Shift+F1`) with a button that records the next key press as the chord. Tesserae-specific: Material Design 3 (MD3) has no counterpart; the spec rests on the outlined [[Text Field]], the [[Button]] and the WAI-ARIA keyboard rules. Source of truth in code: see the last section.

## Purpose

People set their own shortcuts in the configuration app (`tess-ui:apps/shell_config/...`, `shell-vault:40 Specifications/Configuration Application.md`). Typing `Ctrl+Alt+Shift+Meta+Key` by hand is error-prone, and a recorded chord is exact. The field supports both: record, or type and have the text read and written in the canonical form. The recorder logic is [[Key Chord Field|Key Chord Recorder]]; this note specifies the field the person sees.

## When to use and not

- Use when: the value is a keyboard shortcut for a global or an application action.
- Do not use when: the value is any other text ([[Text Field]]), a single key for an in-app control the person presses once (a hint, not a setting), or text that merely contains a plus sign.
- The label and the row belong to [[Form Row]]; the key chord field specifies the field only.

## Anatomy

1. Text field: an outlined [[Text Field]] holding the canonical chord text, or the placeholder "Not set" while empty.
2. Record button: a keyboard icon (24 dp, 20 dp at compact and dense) and the text "Record"; while recording it reads "Press keys" and the modifiers held so far (`Press keys Ctrl+Shift+`).
3. Message line (inside the field's supporting text): the reason a typed text is refused, or the reason a key cannot be recorded.
4. Conflict note (specified, not built): supporting text naming the action that already uses the chord.
5. Label: the field's name ("Reveal key"); the accessible name of the group.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Single chord | the shipped field | one `Modifier+...+Key` value; empty is no shortcut |
| Two-step chord (`Ctrl+K Ctrl+S`) | not built; not part of the shell's shortcut value form ([[11 Interaction#Shortcuts and conflicts|Global Shortcuts]] defines one chord) | specified only if [[11 Interaction#Shortcuts and conflicts|Global Shortcuts]] adds sequences; until then a field refuses a value with a space |
| With conflict list | settings with many shortcuts | adds the conflict note and a link to the conflicting entry |

## States

State layers and focus come from [[State Layers]] and [[Focus Ring]]; the text field takes the states of the outlined [[Text Field]].

| State | Visual change | Token values |
|---|---|---|
| Rest | field outline 1 dp `outline`; button: outline 1 dp `outline`, transparent container, icon and text `on_surface_variant`, corner 12 dp, padding 16 dp left and right | `tess-ui:src/tess_ui/views/KeyChordField_Stylesheet.tdl` |
| Hover (button) | 8 percent layer of `on_surface_variant` | [[State Layers]] |
| Focus (field) | outline 2 dp `primary`, caret `primary` | as [[Text Field]] |
| Focus (button, keyboard) | 10 percent layer plus focus ring 3 dp `secondary` offset 2 dp | [[Focus Ring]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Recording | button container `primary_container`, icon and text `on_primary_container`, `pressed` exposed; the text shows the modifiers held; the field shows the previous chord unchanged | `tess-ui:src/tess_ui/views/KeyChordField_View.tdl` |
| Refused text | field outline, label and message `error`; the typed text stays to be mended; `Value` unchanged | as [[Text Field]] error |
| Value not a chord (set by the app) | shown in the error colours, kept | `tess-ui:docs/components/key-chord-fields.md` |
| Disabled | whole field and button `on_surface` at 38 percent; records and reads nothing | [[State Layers]] |

Recording is signalled by text and by `pressed`, not by colour alone ([WCAG 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color)).

## Tokens used

- Colour: roles as in the State table ([[Colour Roles]]).
- Type: chord text `body_large` at default, `body_medium` at compact and dense; button text `label_large` ([[Typography]]).
- Shape: field corners 4 dp; button corner 12 dp (tess-ui) ([[Shape]]).
- Spacing and density: [[Spacing and Density]].

## Sizing and density

| Level | Field height | Record button height | Button horizontal padding | Gap field to button | Icon |
|---|---|---|---|---|---|
| default | 40 dp | 40 dp | 16 dp | 8 dp | 24 dp |
| compact | 32 dp | 32 dp | 12 dp | 8 dp | 20 dp |
| dense | 28 dp | 28 dp | 8 dp | 4 dp | 20 dp |

- The field and the button share the height of the density level ([[ADR-0002 Desktop density levels and target sizes]], [[Spacing and Density]]). tess-ui draws the button 56 dp high (`Min_Height: 56`) with 16 dp padding at every density; the spec value at default is 40 dp (the Button height) and the compact and dense paddings 12 and 8 dp are design choices #needs-verification-as-design-choice.
- Field width: at least 160 dp so that the longest chord fits (`Ctrl+Alt+Shift+Meta+PageDown` is 28 characters, about 190 dp at `body_medium`); the field has `Flex: fill` in its row and `min-width: 0`.
- Hit area at least 24 by 24 dp, 48 by 48 dp in a touch context.
- Vertical centring by construction, as [[Text Field]] (AC-DEN-9); the button label and icon are centred in the button.

## Dimensions and defaults

The control is a row of an outlined field and a Record button. Vertical padding of the field is `(height - line height) / 2`. Compact and dense paddings of the button are design choices #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| control | height | `density.control_height` | 40 | 32 | 28 | Sizing table, [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| control | padding | `space.0` | 0 0 0 0 | 0 0 0 0 | 0 0 0 0 | [[Spacing and Density]], the field and the button carry their own padding | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| control | margin | - | N/A: the parent container or Form Row sets the outer space | N/A: same as default | N/A: same as default | [[Spacing and Density]], [[Form Row]] | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| control | gap | `space.3` | 8 | 8 | 4 | Sizing table (gap field to button), [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| control | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| field | height | `density.control_height` | 40 | 32 | 28 | Sizing table, [[Text Field]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| field | min width | - | 160 | 160 | 160 | Sizing section (the longest chord fits), [[Spacing and Density]] | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| field | min height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], the 24 dp pointer minimum is met at every level | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| field | padding | `density.field_padding_x` | 8 12 8 12 | 6 8 6 8 | 4 8 4 8 | [[Spacing and Density]], vertical = (height - line box) / 2 | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| field | border width | - | 1 | 1 | 1 | [Material Web outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss), 2 when focused | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| field | border color | `outline` | `outline` | `outline` | `outline` | States table, [[Text Field]], `primary` when focused, `error` when refused | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| field | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]], Tokens used section | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| field | font | `body_large` / `body_medium` | 16/24/400/0.5 | 14/20/400/0.25 | 13/18/400/0.25 | [[Typography]], Tokens used section; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme (family, size, weight), no hook for line height and tracking; tess-shell: n/a: element absent in tess-shell; tre: yes (font_family, font_size, font_weight), hardcoded in tre (text_input takes no line_height or letter_spacing) |
| Record button | height | `density.control_height` | 40 | 32 | 28 | Sizing table, [[Button]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| Record button | min height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]], the 24 dp pointer minimum is met at every level | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| Record button | min width | - | N/A: the width equals the wider of the "Record" and "Press keys" contents | N/A: same as default | N/A: same as default | Layout and overflow section, [[Button]] | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| Record button | padding | - | 0 16 0 16 | 0 12 0 12 | 0 8 0 8 | Sizing table, `tess-ui:src/tess_ui/views/KeyChordField_Stylesheet.tdl` (16 at default); compact and dense: design choice, proposed ADR: compact and dense sizes of composite input controls | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| Record button | gap | `density.icon_label_gap` | 8 | 8 | 4 | icon to label, [[Spacing and Density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| Record button | border width | - | 1 | 1 | 1 | States table (outline 1 dp `outline`), [[Button]] | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| Record button | border color | `outline` | `outline` | `outline` | `outline` | States table, [[Button]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| Record button | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]], Tokens used section (tess-ui 12) | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| Record button | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 13/18/500/0.1 | [[Typography]], Tokens used section; compact and dense: [[ADR-0029 Desktop density and type scale]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| Record button | icon size | - | 24 | 20 | 20 | Anatomy section, [[Iconography]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |

## Layout and overflow

- The control is a horizontal row: field (fills), button (fixed). The message line is the field's supporting text and wraps to at most 2 lines ([[Text Field]]).
- A chord longer than the field truncates with an ellipsis while unfocused and scrolls while focused ([[10 Layout Overflow and Scrolling]]).
- The button label never truncates: the button has a fixed minimum width equal to its content. While recording, the text "Press keys Ctrl+Shift+" may be wider than "Record"; the button's width is fixed to the wider text so the row does not shift (a design rule, not in tess-ui #needs-verification-as-design-choice).

## Behaviour

- Pointer: a press on the button starts a recording; a press elsewhere in the field places the caret. Leaving the button ends a recording.
- Recording (button focused, or after a press on it):

| Input | Result |
|---|---|
| Modifier alone (Ctrl, Alt, Shift, Meta, a lock key) | never finishes; the button shows the modifiers held so far |
| A key that is not a modifier | finishes: `Value` is written as `Ctrl+Alt+Shift+Meta+Key`, `On_Change` is called, the field shows it, `Recording` is false |
| Escape alone | cancels, the chord stays as it was |
| Backspace alone | clears: `Value` is empty, `On_Change` is called |
| Escape or Backspace with a modifier | recorded as a chord (`Ctrl+Escape`) |
| Enter and Space while recording | recorded as chords (the Enter or Space that started the recording from the keyboard does not record itself) |
| A key no chord can have (`print_screen`) | named under the field, recording continues |
| Tab | moves focus and ends the recording; Tab cannot be recorded without a modifier (Ctrl+Tab, Alt+Tab record) |

  Starting a recording from the keyboard: Tab to the button and press Enter or Space.
- Typing (field focused): the text is read when Enter is pressed or the field is left, never per key. Any case and the usual names are read (`ctrl+shift+f1`, `Control + Return`, `super+pgup`, `Esc`, `Del`, `arrow_left`) and written back canonically (`Ctrl+Enter`). Anything else is refused: `Value` stays, the error colours and the reason show, the text stays. Typing nothing clears the shortcut. A value set by the app is shown as it is and is not rewritten until the person commits it.
- Canonical form: modifiers in the order Ctrl, Alt, Shift, Meta, then one key, joined by `+`. Named keys are in title case (`Escape`, `Enter`, `Backspace`, `Tab`, `Space`, `Delete`, `Insert`, `Home`, `End`, `PageUp`, `PageDown`, `Left`, `Right`, `Up`, `Down`); `Plus`, `Minus`, `Comma`, `Period` name the characters that cannot be written in a plus-joined text; function keys `F1` to `F24`; a letter is upper case; media and hardware keys use the X names without `XF86` (`AudioMute`, `MonBrightnessUp`); `XF86AudioMute` is read and written back without the prefix. The shell reads the same form and aliases (`Return`, `Esc`, `Del`, `Ins`, `PgUp`, `PgDown`) and writes only the canonical form (`shell-vault:40 Specifications/Integration/Global Shortcuts.md`, Key Names).
- Conflict (specified, not built): on commit the field compares the chord with the shortcuts the project knows (its own entries; the desktop's where the shell can detect them, `shell-vault:40 Specifications/Integration/Global Shortcuts.md`, Conflict warnings). A conflict is a warning, not an error: the value is written and the supporting text names the action ("Also used by Toggle launcher"). The desktop wins at run time, so the warning says so for desktop conflicts.
- Touch: the button works by tap; recording needs a hardware keyboard, so on a touch-only device the button is disabled with the reason in the tooltip.
- IME: while recording, IME is off for the button (a key press is a key press, not a composition); in the text field the field is plain text and composition text is shown inline and committed before reading ([[Text Field]]).
- Validation hooks: refused text and conflicts use the field's supporting text. When and how errors appear: [[Validation]] and [[Forms and Settings]].

## Tooltip and overlay behaviour

The record button carries a tooltip with its name and, while idle, the hint "Press, then type the shortcut. Escape cancels, Backspace clears." The field container has none ([[ADR-0004 Tooltip rule]]). The control opens no overlay.

## Motion

None beyond the state changes of [[Text Field]] and [[Button]] (at most 150 ms). Reduced motion: no ripple, steady caret ([[14 Accessibility Basics]]).

## Accessibility

- The group has role `group` named by the label (tess-ui: `A11y { Role: group, Label: <| label |> }`).
- The field is a `textbox` named by the label; the error is its description and a polite live region; `invalid` while refused.
- The button has role `button` and the name "Record {label}", or while recording "Recording {label}: press the keys, Escape cancels, Backspace clears", and is `pressed` while recording (`tess-ui:src/tess_ui/views/KeyChordField_View.tdl`).
- Announcements: starting a recording announces the "Recording" name once; the finished chord is announced by the field's new value, in words the screen reader reads from the text ("Control plus Shift plus F1" is the platform's reading of the text); a refused key announces the reason as a polite live region.
- Keys: the field and the button are both in the Tab order; recording never traps focus (Tab leaves and ends the recording; a chord that includes Tab needs a modifier).
- Contrast: chord text 4.5 to 1; outline 3 to 1; button text on `primary_container` 4.5 to 1 ([WCAG 1.4.3, 1.4.11](https://www.w3.org/TR/WCAG22/)).
- A person who cannot press chords (sticky keys, one hand) uses typing: the typed path has no time pressure and no simultaneous keys.
- See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Dark and light

All colours are roles; the control follows the system theme ([[Theme Following the System]]); AC-KCF-10 runs in both.

## Defaults

- Label "Shortcut"; placeholder "Not set"; empty value (no shortcut).
- Outlined variant; density from the container (`compact` in config tools).
- Single chord; conflicts not checked until a project supplies the list.

## Acceptance criteria

- [ ] AC-KCF-1 (scripted input): record `Ctrl+Shift+F1`: press the button, press Ctrl (button shows `Press keys Ctrl+`), Shift, F1: `Value` equals `Ctrl+Shift+F1`, `Recording` is false and `On_Change` was called once. Pass: values and call count equal.
- [ ] AC-KCF-2 (scripted input): modifiers pressed in any order (Shift, Meta, Alt, Ctrl, then A) record as `Ctrl+Alt+Shift+Meta+A`. Pass: `Value` equals the canonical text.
- [ ] AC-KCF-3 (scripted input): while recording, Escape alone leaves `Value` unchanged and `Recording` false; Backspace alone sets `Value` to empty and calls `On_Change`; Ctrl+Escape records `Ctrl+Escape`. Pass: values equal.
- [ ] AC-KCF-4 (scripted input): while recording, Shift alone, Ctrl alone and Caps Lock alone do not finish the recording; `print_screen` alone shows its message and recording continues. Pass: `Recording` true after each.
- [ ] AC-KCF-5 (scripted input): type `control + return` and press Enter: `Value` equals `Ctrl+Enter`; type `Ctrl+Shift` and leave the field: `Value` unchanged and the field shows the error; type the empty text: `Value` is empty. Pass: values and `invalid` flag equal.
- [ ] AC-KCF-6 (scripted input): a table of 30 names and aliases (`Esc`, `Del`, `arrow_left`, `PgUp`, `super+pgup`, `XF86AudioMute`, `ctrl+plus`) commits to the canonical form of [[11 Interaction#Shortcuts and conflicts|Global Shortcuts]] and is read back by the shell parser to the same chord. Pass: all 30 equal.
- [ ] AC-KCF-7 (scripted input): a value set by the app (`ctrl+shift+f1`) is displayed as given and `Value` is not rewritten until the person commits; a value that is not a chord is displayed in the error colours. Pass: text and `Value` equal.
- [ ] AC-KCF-8 (scripted input): with a keyboard only, Tab reaches the field, then the button; Enter on the button starts a recording and the Enter does not record itself; the next key records; focus stays on the button. Pass: focus sequence and `Value` equal.
- [ ] AC-KCF-9 (AT tree assertion): the group has role `group` and the label as name; the field is a `textbox` with the label as name and `invalid` plus the message as description when refused; the button has role `button`, the name "Record {label}" idle and "Recording {label}: ..." while recording, and `pressed` true while recording. Pass: all properties equal.
- [ ] AC-KCF-10 (contrast script): in light and dark, chord text on the field container 4.5 to 1 or more, outline 3 to 1 or more, recording button text on `primary_container` 4.5 to 1 or more, error text 4.5 to 1. Pass: ratios at or above the limits.
- [ ] AC-KCF-11 (token test): field and button heights equal 40, 32, 28 dp at default, compact, dense; the two heights are equal at each level; no literal colour in the stylesheet. Pass: values equal, every colour a role reference.
- [ ] AC-KCF-12 (geometry check): the recording button's width is the same before and during recording at each density, and the row does not shift by more than 0.5 dp. Pass: widths equal within 0.5 dp.
- [ ] AC-KCF-13 (geometry check): the longest chord (`Ctrl+Alt+Shift+Meta+PageDown`) fits the field at the default width without ellipsis at each density; a longer value truncates with an ellipsis and no pixel lies outside the container. Pass: ellipsis rule and zero overflow pixels.
- [ ] AC-KCF-14 (scripted input): with a conflict list supplied, committing a chord that another action uses writes the value and shows the supporting text naming that action; the field is not `invalid`. Pass: value written, text equal, flag false. (Applies when the project supplies the list; otherwise `not applicable`.)
- [ ] AC-KCF-15 (geometry check): hover over the field container for 600 ms shows no tooltip; hover over the button shows its tooltip ([[ADR-0004 Tooltip rule]]). Pass: zero tooltips on the field, one on the button.
- [ ] AC-KCF-16 (scripted input): a disabled field takes no focus, no key and records nothing; the disabled button is not in the Tab order. Pass: `Value` unchanged and no focus.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/KeyChordField_View.tdl`, `KeyChordField_Stylesheet.tdl`, `tess-ui:src/tess_ui/chord_controls.py`, `tess-ui:src/tess_ui/key_chords.py` | partly meets: recording, modifier preview, Escape cancel, Backspace clear, canonical order, typed reading, error text, group, field and button roles, `pressed` while recording exist (AC-KCF-1 to AC-KCF-5, AC-KCF-7 to AC-KCF-9 meet as documented, unmeasured); button `Min_Height: 56` at every density and no density setting (AC-KCF-11 fails); the button width changes with its text (AC-KCF-12 not met); no conflict list (AC-KCF-14 fails); no two-step chords; key names for a keypad and some media keys unknown (AC-KCF-6 partial: documented media keys exist); no tooltip documented on the button (AC-KCF-15 unmeasured); what Tab does while recording is not documented (AC-KCF-8 partial) |
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (`KeyChordField`), `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`KeyChordWidget`) | partly meets: the field is used for `key_chord` keys and refuses text that is not a chord; shown in the settings form |
| tess-shell | none (the shell reads the value; no field) ; `shell-vault:40 Specifications/Integration/Global Shortcuts.md` (parser, key names) | not applicable for the field; the parser must accept every canonical value (AC-KCF-6 is the shared test) |
| tre | none (engine reports keys; no recorder) | not applicable |
| tess-ui | same files, Dimensions and defaults | differs: Record button 56 high (`Min_Height: 56`), spec 40/32/28 (AC-KCF-11); no density setting, padding 16 at every level, spec 16/12/8 |

Evidence: `tess-ui:docs/components/key-chord-fields.md`.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/KeyChordField_View.tdl`, `tess-ui:src/tess_ui/chord_controls.py`, `tess-ui:docs/components/key-chord-fields.md` | exists, partial |
| shell vault | `shell-vault:40 Specifications/Integration/Global Shortcuts.md` (Key Names, Decided 2026-11-13) | spec of the value form |
| tess-shell | none | not applicable |
| tre | none | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Compact and dense text follow the desktop type scale (body_medium 14/20, body_dense 13/18; title_dense for labels) | Desktop density: text must match 32 and 28 dp controls | [[ADR-0029 Desktop density and type scale]] |
| The element exists although MD3 has no key chord field | settings app needs recorded shortcuts | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Field and button heights 40, 32, 28 dp | desktop density | [[ADR-0002 Desktop density levels and target sizes]] |
| Recording state is shown by text and `pressed`, plus a container colour | colour must not be the only cue | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |

## Sources

- tess-ui key chord field documentation: `tess-ui:docs/components/key-chord-fields.md`.
- Key names and the shell's shortcut value: `shell-vault:40 Specifications/Integration/Global Shortcuts.md`.
- [Material Web outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss) for the field; [Material Web button docs](https://github.com/material-components/material-web/blob/main/docs/components/button.md) for the button.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 1.4.1, 1.4.3, 1.4.11, 2.1.2 (no keyboard trap: the recording ends on Tab), 2.5.8.
- MD3 has no such element: stated from the absence in the Material Web component list.
