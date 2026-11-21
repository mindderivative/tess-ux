---
title: Validation
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, validation, forms]
related: ["[[40 Patterns]]", "[[Forms and Settings]]", "[[Error States]]", "[[Notifications]]", "[[Form Row]]", "[[Text Field]]", "[[Switch]]", "[[Button]]", "[[Spin Box]]", "[[List Editor]]", "[[Colour Roles]]", "[[Typography]]", "[[Spacing and Density]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
depends_on: ["[[Form Row]]", "[[Text Field]]"]
---

# Validation

> [!info] Summary
> When a value is checked, what happens to a wrong value, where the message appears (inline or in a summary), how a text field looks when it is wrong, and what a screen reader hears. The MD3 counterpart is the text field error state and supporting text ([text fields](https://m3.material.io/components/text-fields/overview)); form-level rules are Tesserae's, with the config app as the reference implementation.

## Problem

Validation exists per component only: `TextField` has `Error`, `Checkbox` and `RadioButton` have `error`, the engine has `invalid` and `description` flags, and the config app refuses out-of-range numbers and shows the range itself; no form-level pattern exists and the shell's `TextInput` has no error or helper text ([[Gaps and Contradictions]], summary item 8 and "Validation: per component only").

## Purpose

Prevent wrong values reaching a file or a command, and tell the user what is wrong and what is allowed, at the moment and place they can fix it.

## When to use and not

- Use when: a control accepts typed or chosen values that have a type, a range, a pattern, a length, a uniqueness or a cross-field rule.
- Do not use when: the failure is not about the value (a disk write failed: [[Error States]]); the control can only produce valid values (a [[Switch]], a choice of an enum: no validation message is needed).
- Prefer constraint to correction: a stepper with min and max, a unit suffix and an enum choice make errors impossible and need no message.

## Rules

1. When to validate (decision table): typing never produces an error message. A value is validated on commit: Enter, Tab or focus leaving the field, activating Apply or Save. Exceptions: a character that can never be valid (a letter in a whole-number field) is refused at once and the text stays; a required field is not reported as missing until the user left it or tried to submit.
2. After a field showed an error, it re-validates on every change so the message disappears as soon as the value is valid.
3. Refuse, do not coerce: a value outside its range, a non-number or a pattern mismatch writes nothing, keeps the typed text in the field and states the rule with the allowed range ("Must be from 0 to 9", "at least 0"). The config app does this: "a value outside the minimum and maximum is refused with the range, nothing is written and the typed text stays" (`tess-ui:apps/shell_config/README.md`, "The form").
4. The message sits under the control, in the error line of the [[Form Row]], in `body_small` and the `error` role with an icon; it replaces the help line while it is shown and the help line returns when the value is valid. No layout jump beyond the line itself: space for one line is reserved only if the form sets `reserve_error_line`; otherwise the line appears below and the rows below move by exactly one line height (16 dp) (design choice, #needs-verification-as-design-choice).
5. The control shows the error state: outline or indicator in `error`, label in `error`, trailing error icon, `invalid` true ([[Text Field]]; Material Web `error-outline-color`, `error-label-text-color`, `error-supporting-text-color` are the `error` role). Focus keeps the focus ring; an error at rest and at focus is distinguishable from normal by the icon and message, not by colour alone.
6. Messages say what is allowed, not only what is wrong: range, pattern, accepted forms, with an example for patterns ("Write a chord like Ctrl+Shift+K").
7. Inline versus summary: one invalid value is reported inline only. A form with several invalid values reports each inline and, on submit, adds a summary at the top of the form (or a problems list for document-scale checks) that lists each problem as a link; activating a link moves focus to that control. The summary does not replace the inline messages.
8. Document-scale checks (a whole file against a schema) use a problems list: severity icon plus word (Error, Warning, Note), place (`file:line:column`), the message and what to write instead; Enter on a finding opens its place and focuses the control (config app, `tess-ui:apps/shell_config/src/tess_shell_config/problems.py`).
9. Submit with errors: the primary action is not disabled by invalid values (a disabled button explains nothing); activating it validates all fields, shows the summary and moves focus to the first invalid control. Exception: an action that is impossible without a value stays disabled with the reason as its description.
10. Announcement: an error is announced once when it appears (polite live region on the error line); typing more characters does not announce again while the message is unchanged; the summary is announced as "N problems" once on submit ([[14 Accessibility Basics]], SC 3.3.1, 4.1.3).
11. Required fields carry the text "required" under the label, not only an asterisk; optional is the default and is not marked.
12. Cross-field rules (end after start) report on the field the user changed last and name the other field in the message.
13. Validation runs off the main thread when it can take over 50 ms and shows [[Loading States]] on the field (`busy`); the config app runs `check` on a worker thread with a 10 s timeout.

## Decision table

| Case | Check on | Message | Control keeps text | Announce |
|---|---|---|---|---|
| Impossible character (letter in a whole-number field) | key press | none, character not inserted | yes | no |
| Out of range, bad pattern, bad length | commit (Enter, Tab out, Apply) | inline, with the allowed range | yes, nothing written | polite once |
| Required and empty | leaving the field or submit | inline "required" marker turns `error`, message "Enter a value" | not applicable | polite once |
| Uniqueness or cross-field | commit | inline on the last changed field, names the other | yes | polite once |
| Several invalid fields on submit | submit | inline each plus summary with links | yes | summary count once |
| A document against a schema | save, check, apply | problems list rows | not applicable | status line plus count |
| Async check (name taken) | commit, after 300 ms idle | inline after the result, field `busy` meanwhile | yes | polite once |

## Examples (short snippets only)

```tdl
TextInput {
  Text: <| value |>
  Error: <| range_error |>
  Supporting: "From 0 to 9"
  A11y { Label: Gap, Description: "From 0 to 9" }
}
```

Config app range refusal: a number field with a unit suffix; entering 12 where the range is 0 to 9 writes nothing, keeps `12` in the field and the `row_error` line reads "must be from 0 to 9" (wording from `Refused` in `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py`).

## States

| State | Visual change | Token values |
|---|---|---|
| Valid | no message; help line when focus is within the row | `on_surface_variant` |
| Invalid | outline or indicator `error`, label `error`, trailing `error` icon 18 dp, message `body_small` `error` | [[Colour Roles]], [[Typography]] |
| Invalid and focused | as invalid plus focus ring 3 dp, 2 dp offset | [[Focus Ring]] |
| Required and missing | text "required" in `label_small`, `error` | [[Form Row]] |
| Checking | field `busy`, no message | [[Loading States]] |
| Disabled | no validation, no message | 38 percent |

## Sizing and density

The error line is `body_small`, 16 dp line height, gap above it `space.1` (2 dp) at default and compact, 0 at dense; the icon is 18, 18, 16 dp; the control height is unchanged by the error state (40, 32, 28 dp, [[Spacing and Density]], [[ADR-0002 Desktop density levels and target sizes]]).

## Accessibility

- `invalid` true on the control; the message is its description (`describedby` to the error line) in addition to the help text; the error line is a polite live region.
- The summary is a group named "Problems" with links; each link names the field and the problem.
- Error text against the surface at least 4.5 to 1; the control outline against the surface at least 3 to 1.
- No timeout on a message (WCAG 2.2 SC 2.2.1); the message stays until the value is valid.

## Acceptance criteria

- [ ] AC-VAL-1 (scripted input): typing "1", "2" into a field with range 0 to 9 raises no message while typing; Enter shows the message and writes nothing; the field text still reads "12". Pass: message count 0 before Enter and 1 after, written value unchanged, text equal.
- [ ] AC-VAL-2 (scripted input): after an error, changing the text to "5" removes the message and `invalid` within one frame of the change and Enter writes 5. Pass: flag false, value 5.
- [ ] AC-VAL-3 (token test): the invalid state uses the roles `error` for outline or indicator, label, supporting text and icon; no literal. Pass: role references only.
- [ ] AC-VAL-4 (pixel check): an invalid field differs from a valid one in the icon and message pixels, not colour alone (greyscale render). Pass: difference present in greyscale.
- [ ] AC-VAL-5 (AT tree assertion): an invalid field has `invalid` true and its description contains the message; the error line is a polite live region; one announcement per distinct message. Pass: flag, description and count equal.
- [ ] AC-VAL-6 (scripted input): a form with three invalid values and a submit shows three inline messages and a summary of three links; activating the second link focuses the second control; focus after submit is on the first invalid control before any link is activated. Pass: counts and focus owners equal.
- [ ] AC-VAL-7 (geometry check): when an error line appears below a control, the control's y position does not change and the rows below move by the error line height (16 dp, 0.5 dp). Pass: offsets equal.
- [ ] AC-VAL-8 (contrast script): error text at least 4.5 to 1 and error outline at least 3 to 1 against the surface in light and dark. Pass: ratios at or above the limits.
- [ ] AC-VAL-9 (scripted input): a required empty field shows no error until it loses focus once or submit is activated; then the text "required" is under the label. Pass: states equal at each step.
- [ ] AC-VAL-10 (scripted input): a submit with invalid values is not blocked by a disabled primary button: the primary button is enabled and activating it validates all fields. Pass: button enabled, validation ran.
- [ ] AC-VAL-11 (AT tree assertion): a problems list row exposes the severity word, place, message and fix text; activating it with Enter focuses the control of the key. Pass: row name contains the four parts, focus owner equals.
- [ ] AC-VAL-12 (geometry check): the message wraps within the control column and ends with an ellipsis after 3 lines; no pixel lies outside the row. Pass: lines at most 3, zero pixels outside.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TextField_View.tdl` (`Error`, `Supporting`), `tess-ui:apps/shell_config/src/tess_shell_config/widgets.py` (`Refused`), `Main_View.tdl` (`row_error`, `problems_list`), `problems.py` | partly meets: `TextField` error look with icon and `invalid` (AC-VAL-3, AC-VAL-4, AC-VAL-5 meet by reading); the config app refuses out-of-range, non-number and pattern values with the range, keeps text, polite `row_error` (AC-VAL-1, AC-VAL-5), problems list with icon and word and click or Enter to the key (AC-VAL-11); no form summary with links (AC-VAL-6 fails), no re-validation rule in the toolkit (AC-VAL-2 app-level), no required-marker rule in the toolkit (AC-VAL-9 app-level), the plain `TextInput` has no error or helper (the config app single-line field is a `TextInput`) |
| tess-shell | `shell-vault:40 Specifications/Runtime/Validation and Errors.md`, `tess-shell:src/tess_shell/shipped/TextInput/` | partly meets for files: eight-stage pipeline reports `file:line:column`, what is wrong and what to write (AC-VAL-11 analogue on the console); `TextInput` module has no error, helper text or `invalid` (AC-VAL-3, AC-VAL-5 fail) |
| tre | `tre:docs/reference/node.md` (`invalid`, `description`), `tre:docs/guide/text.md` (`max_length`, `read_only`) | not applicable: flags and a length limit only; no visual, no message |

Request candidates: `Error` and `Supporting` on the plain `TextInput` view in tess-ui and on the shell `TextInput` module; a form summary view; routed through the Orchestrator.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Validation on commit, not on every keystroke, except impossible characters | typing must not flash errors on desktop forms with many fields | none; design choice |
| Summary plus inline for several errors | MD3 shows per-field text only | none; design choice |
| Message states the allowed range | WCAG 2.2 SC 3.3.3 Error Suggestion | none |
| Error line below the control column of a [[Form Row]] | label beside the control layout | [[ADR-0002 Desktop density levels and target sizes]] |

## Sources

- [Material Web text field docs](https://github.com/material-components/material-web/blob/main/docs/components/text-field.md): error state, `error-text` replaces supporting text, `required` and `reportValidity`; [outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss): `error-outline-color`, `error-label-text-color`, `error-supporting-text-color` are the `error` role. Verified 2026-11-21.
- [WCAG 2.2 SC 3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html), [SC 3.3.3 Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html), [SC 3.3.4 Error Prevention](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html), [SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html).
- [WAI-ARIA 1.2 `aria-invalid`, `aria-describedby`, `alert`](https://www.w3.org/TR/wai-aria-1.2/).
- The commit-time rule, 300 ms async idle, one-line reserve and 16 dp line height are design choices #needs-verification-as-design-choice.
- Code: `tess-ui:apps/shell_config/README.md` ("The form"); `tre:docs/reference/node.md`; [[Gaps and Contradictions]].
