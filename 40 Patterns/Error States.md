---
title: Error States
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, state, error]
related: ["[[40 Patterns]]", "[[Empty States]]", "[[Loading States]]", "[[Validation]]", "[[Notifications]]", "[[Banner]]", "[[Snackbar]]", "[[Dialog]]", "[[Button]]", "[[Text Field]]", "[[Form Row]]", "[[Colour Roles]]", "[[Typography]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
depends_on: ["[[Colour Roles]]", "[[Validation]]"]
---

# Error States

> [!info] Summary
> How the interface reports that something failed (a read, a write, a command, a connection) as opposed to a value that is wrong ([[Validation]]): where the message goes, what it says, how the user recovers. MD3 colours the `error` roles and specifies field errors; the rest is Tesserae's. Source of truth in code: see Status in code.

## Problem

Failures reach the user in five unrelated ways today: a `row_error` text in the config form, a message row in the Problems list, the status line, an `invalid` flag, and a log line the user never sees. The engine has only the `invalid`, `description` and `live` flags and no error visual ([[Gaps and Contradictions]], summary item 8 and the tre evidence "Empty, loading and error states have no engine support"). The shell reports file errors as `file:line:column` on the console (`shell-vault:40 Specifications/Runtime/Validation and Errors.md`).

## Purpose

Say what failed, what is still safe, and what to do next, in the place where the user is looking.

## When to use and not

- Use when: an operation or a load failed, a source is unavailable, or a result is wrong for a reason the user did not type.
- Do not use when: a typed value is out of range ([[Validation]]); the container is merely empty ([[Empty States]]); information needs no action ([[Notifications]]).

## Rules

1. Scope chooses the surface (decision table). The message sits as close as possible to what failed and never covers it.
2. A message has three parts in this order: what happened ("Could not save settings.tdl"), the cause when known ("The folder is read-only"), and the next step ("Choose another folder" or a Retry action). No error codes alone, no stack traces in the UI; the technical detail goes to the log and to an optional "Details" disclosure.
3. The message states what is unchanged when it is true: "Your changes are still in the window" (the config app keeps edits after a failed save, `tess-ui:apps/shell_config/README.md`).
4. Error colour is never the only carrier: every error has the `error` icon and text ([[14 Accessibility Basics]], SC 1.4.1). Text and icon use `error` on `surface` or `on_error_container` on `error_container`, at least 4.5 to 1.
5. Recoverable errors offer exactly one primary action (Retry, Choose another, Reload); a second action is Dismiss or Details.
6. An error that blocks work stays until resolved or dismissed (banner, inline, dialog). A passing failure (a copy that failed) may use a [[Snackbar]] with Retry, which stays at least 10 s because it carries an action (design choice, #needs-verification-as-design-choice).
7. Errors are announced once when they appear: polite for inline and banner, assertive only when data is lost or the app cannot continue ([[14 Accessibility Basics]]). The announced text is the message; a repeat of the same failure within 2 s is not announced again.
8. A failed load keeps the stale content visible when it exists and marks it ("Showing saved data") rather than replacing it with an error.
9. A load that ends in an error replaces the loading indicator ([[Loading States]]) in the same frame and clears `busy`.
10. Focus does not move to a banner or inline error unless the user caused it by activating a control (then focus goes to the first control that needs attention, or the error's action). A modal [[Dialog]] error takes focus and returns it on close.
11. Unrecoverable: an error dialog with one confirm button, the app state saved first where possible.

## Decision table

| Scope of the failure | Surface | Persistence | Announce | Example |
|---|---|---|---|---|
| One field value | inline under the field ([[Validation]]) | until fixed | polite | number out of range |
| One row or item of a list | inline row message with icon | until fixed | polite | a finding row in the Problems list |
| A region (a list, a panel) failed to load | error state in the region with Retry | until retried | polite | files list unreadable |
| The open document or page | [[Banner]] at the top of the page, action | until resolved | polite; assertive if data may be lost | file changed on disk |
| A background action finished with failure | [[Snackbar]] with Retry | 10 s minimum, or until dismissed | polite | copy failed |
| An action the user must answer | modal [[Dialog]] | until answered | assertive | discard unsaved changes |
| The app or the shell cannot continue | error dialog or console plus log | until closed | assertive | shell start failed |

## Examples (short snippets only)

```tdl
Container {
  Name: region_error
  A11y { Role: group, Label: "Files could not be read" }
  Children {
    Icon { Icon: error, Style { Foreground: error } }
    Text { Text: "Could not read the folder. It may have been removed." Live: polite }
    Button { Label: Retry, Variant: tonal, On_Click: reload }
  }
}
```

The config app marks problem rows with an icon and a word (Error, Warning, Note) so colour is not alone (`tess-ui:apps/shell_config/src/tess_shell_config/problems.py`, `SEVERITY_ICONS`).

## States

| State | Visual change | Token values |
|---|---|---|
| Inline error | `error` icon 18 dp and text `body_small` in `error` | [[Colour Roles]] |
| Region error | centred icon 24 dp, text `body_medium` `on_surface`, action button | [[Typography]] |
| Banner error | container `error_container`, content `on_error_container`, 1 action | [[Banner]] |
| Dialog error | [[Dialog]] with `error` icon, headline, one or two actions | [[Dialog]] |
| Retrying | action shows loading, `busy` | [[Loading States]] |

## Sizing and density

Inline error text `body_small` (12 dp on 16 dp, [[Typography]]); icon 18 dp at default and compact, 16 dp at dense; gap icon to text 8, 8, 4 dp (`density.icon_label_gap`, [[Spacing and Density]]); the retry button follows the control height 40, 32, 28 dp.

## Accessibility

- The message is a live region (polite) or announced through `window.announce`; the owner of the failed control has `invalid` true when the error is about its value.
- The description of the failed node references the message (`describedby`).
- No auto-dismiss of an error that needs a decision (WCAG 2.2 SC 2.2.1).

## Acceptance criteria

- [ ] AC-ERR-1 (pixel check): every error message shows an icon and text; a greyscale render still differs from the non-error state. Pass: icon pixels and text present in each of the scope surfaces.
- [ ] AC-ERR-2 (contrast script): error text on its surface at least 4.5 to 1 and the error icon at least 3 to 1, in light and dark, for inline, banner and region forms. Pass: ratios at or above the limits.
- [ ] AC-ERR-3 (AT tree assertion): when an error appears, exactly one live announcement carries the message; the same message raised again within 2 s adds none. Pass: announcement count equals 1.
- [ ] AC-ERR-4 (scripted input): a failed save leaves the edited content in place and the message states it; a failed load that has stale content keeps the content visible. Pass: content equal before and after.
- [ ] AC-ERR-5 (scripted input): focus does not move when a banner or inline error appears from a background event; after the user activates a control that fails, focus is on the error's action or the first control needing attention. Pass: focus owner equals.
- [ ] AC-ERR-6 (scripted input): the Retry action runs the failed operation once per activation, shows `busy` while it runs and replaces the error on success. Pass: counts and flags equal.
- [ ] AC-ERR-7 (geometry check): an error message of 300 characters in a 240 dp wide container wraps, ends in an ellipsis after 4 lines with a Details disclosure, and no pixel lies outside the container. Pass: lines at most 4, zero pixels outside.
- [ ] AC-ERR-8 (scripted input): an error [[Snackbar]] with an action stays at least 10 s with the pointer elsewhere and is not shown for an error that blocks work. Pass: display time at least 10 s.
- [ ] AC-ERR-9 (token test): error colours are the roles `error`, `error_container`, `on_error_container`; no literal. Pass: role references only.
- [ ] AC-ERR-10 (review): the message names what happened, the cause when known and the next step; no raw exception text. Pass: reviewer checklist per error string in a view.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/TextField_View.tdl` (`Error`), `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (`row_error`, disk banner, problems list) | partly meets: text field `Error` gives the error look and an error icon and is `invalid` (AC-ERR-1, AC-ERR-9 meet by reading); the config app has icon plus word per finding, a failed save keeps edits (AC-ERR-4), `row_error` is polite (AC-ERR-3); no shared region error view (the decision table row fails), Snackbar duration 4000 ms default fails AC-ERR-8 for action snackbars; no 2 s repeat guard (AC-ERR-3 partly) |
| tess-shell | `shell-vault:40 Specifications/Runtime/Validation and Errors.md`, `tess-shell:src/tess_shell/shipped/Image/` (broken-image `error.png`) | partly meets: file errors carry file, line, column and what to write on the console and the log (AC-ERR-10 for files); no on-screen error surface for module failures; modules show a broken-image icon for unknown icon names; AC-ERR-1 to AC-ERR-8 unmeasured |
| tre | `tre:docs/reference/node.md` (`invalid`, `description`, `live`) | not applicable: flags only, no visual; `connection_lost` (0.6.10) is an event the app turns into a message |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A scope table choosing among inline, banner, snackbar and dialog | MD3 treats them as separate components without a selection rule | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Snackbar with an action stays at least 10 s | WCAG 2.2 SC 2.2.1 and keyboard reachability on desktop | none; design choice |
| No focus move for background errors | avoids stealing focus from the user | none; design choice |

## Sources

- [Material Web text field docs](https://github.com/material-components/material-web/blob/main/docs/components/text-field.md) (error text replaces supporting text, `error` styling) and [outlined text field tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-outlined-text-field.scss) (`error-*` colours are the `error` role).
- [Material Components Android: Snackbar](https://github.com/material-components/material-components-android/blob/master/docs/components/Snackbar.md) ("retrying an action that had failed"; one snackbar at a time).
- [WCAG 2.2 SC 1.4.1, 3.3.1 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html), [SC 3.3.3 Error Suggestion](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html), [SC 4.1.3](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html), [SC 2.2.1](https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html).
- The 10 s minimum and the 2 s repeat guard are design choices #needs-verification-as-design-choice.
- Code: `tess-ui:docs/components/text-fields.md`; `tess-ui:apps/shell_config/README.md`; `shell-vault:40 Specifications/Runtime/Validation and Errors.md`; [[Gaps and Contradictions]].
