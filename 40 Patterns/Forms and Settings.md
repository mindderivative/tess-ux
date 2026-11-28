---
title: Forms and Settings
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, forms, settings, config-app]
related: ["[[40 Patterns]]", "[[Form Row]]", "[[Validation]]", "[[Error States]]", "[[Notifications]]", "[[Banner]]", "[[Keyboard Navigation]]", "[[Accordion]]", "[[Text Field]]", "[[Switch]]", "[[Button]]", "[[Icon Button]]", "[[Dialog]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Spacing and Density]]", "[[07 Spacing and Density Rules]]", "[[14 Accessibility Basics]]", "[[Owner Feedback 2026-11-20]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]"]
depends_on: ["[[Form Row]]", "[[Validation]]", "[[Spacing and Density]]"]
---

# Forms and Settings

> [!info] Summary
> How a page of named values is laid out and behaves: the row grid, groups, apply versus live, reset and defaults, the dirty state, a banner when the file changes on disk, and undo. Tesserae pattern; MD3 has no form or settings pattern (it specifies the controls). The reference implementation is the configuration app, `tess-ui:apps/shell_config`; the row is [[Form Row]].

## Problem

Tools that edit configuration need many rows to stay scannable, writes that cannot destroy a file, and a clear answer to "is this saved, applied, different from the default?". tess-ui has no form view: the config app builds rows, group headers, toolbar, status line and banner by hand, and owner feedback F6, F7 and F8 came from that form ([[Owner Feedback 2026-11-20]]; [[Gaps and Contradictions]], "Config app coverage notes").

## Purpose

One rule set for rows, groups, commit timing, defaults, dirty state and external change, so every Tesserae settings page behaves the same and the config app is the testable reference.

## When to use and not

- Use when: a page edits a set of named values with defaults (preferences, a configuration file, a theme).
- Do not use when: a single value is asked in context ([[Dialog]] with one field); a wizard; a data table of records ([[List]]); a command palette.

## Rules

1. Layout: one [[Form Row]] per value on a grid: label column, control column, reset button, help line, error line. The label column has the same width in every row of a form (160, 120, 96 dp at default, compact, dense, [[Form Row]]); controls start at the same x. Below 400 dp content width the label stacks above the control.
2. Groups: related rows sit under a group header, an [[Accordion]] header (role `button`, `expanded`), not a row. The first group is open, Enter or Space on the header toggles it, and the open choice is remembered by group name; a group with a required missing value or a refused value opens by itself unless the user closed it (config app, `tess-ui:apps/shell_config/src/tess_shell_config/form.py`). Group gap 24 dp, row gap 8, 4, 2 dp at default, compact, dense.
3. Commit timing (decision table): a text or number field commits on Enter or when focus leaves it; a switch, choice, colour or list edit commits at once; nothing is written while the user types ([[Validation]]).
4. Apply versus live: the form states one mode for the whole page. Live (the config app's "Apply as I edit" on): each commit is written and applied at once and checked. Staged (off, default in the config app): commits change the document in the window only; Save writes; the toolbar shows the dirty state. The mode switch is a [[Switch]] in the toolbar, persisted in the app state (config app `settings.json`), with the shortcut Ctrl+Shift+A and its name in the description. A page that has side effects the user cannot take back (starting a service) is staged with an explicit Apply.
5. Dirty state: a modified document shows "Unsaved changes" in the status line and the file name in the Files area with a text marker (not only colour); an unsaved row (staged mode) shows its reset button enabled. Leaving with unsaved changes asks: Save, Discard, Cancel in a [[Dialog]], with Cancel the focused action; closing the window does the same.
6. Defaults and reset: every row has a default (from the schema). A row whose value differs from the default or is set explicitly in the file is modified: its reset button is enabled, otherwise disabled with its width reserved. Reset removes the key or writes the default, is one undo step and moves focus to the row's first control ([[Form Row]]). A page-level "Reset all in this group" is a [[Button]] in the group header that asks for confirmation when more than one row would change, and is one undo step.
7. Undo: every commit, structure edit and reset is one undo step (Ctrl+Z, Ctrl+Y or Ctrl+Shift+Z); undo restores the file bytes it replaced; an undone row returns to its previous value and dirty state; undo history is per file and is dropped on Reload of that file.
8. Saving: write to a temporary file in the same folder and rename it over the old one; a failed write leaves the old file whole, keeps the user's changes in the window and names the cause ([[Error States]]); the first save of a session copies the old content to a backup folder; opening and saving without change leaves the bytes identical.
9. External change: when the open file changes on disk, a [[Banner]] above the form says "File changed on disk" with Reload (take the disk's version, drop unsaved changes of that file and its undo history) and Keep mine (the next save replaces the disk's). The app's own saves never raise it. A save over a changed file is refused until the user chooses. The banner is announced assertively when unsaved changes exist, polite otherwise; Ctrl+Shift+L reloads and Ctrl+Shift+U keeps (config app keys).
10. Validation per [[Validation]]: refuse and keep the text, show the range inline, list document findings in a problems list that opens the key on Enter or click.
11. Areas and focus: a form page with panes (tree, properties form, editor, view, problems) is reachable by F6 and Shift+F6 in order; F6 is also the way out of a text editor that takes Tab ([[Keyboard Navigation]]).
12. Help: the label carries the tooltip with the setting's description (500 ms hover), the help line shows it on focus within the row, and the control's accessible description carries it; the row, group and form carry no tooltip ([[ADR-0004 Tooltip rule]]).
13. A key the schema reserves or a value the widget cannot show is shown as text and is never rewritten unless edited; unknown keys are listed in a "Not in the schema" group and are not silently dropped.
14. Density: a form uses the compact level in a config tool ([[07 Spacing and Density Rules]]); controls 32 dp high, rows as in the table of [[Form Row]]; the form scrolls in a container with both bars when content overflows ([[Scrollbar and Scroll Container]]).
15. Destructive actions in the form (delete a block, delete a file) go to a recoverable place (the config app moves a file to a trash folder in its state folder) and are one undo step where the file model allows it.

## Decision table

| Value kind | Control | Commit on | Reset | Validation |
|---|---|---|---|---|
| Boolean | [[Switch]] | change | yes | none (cannot be wrong) |
| Enum, few choices | button opening a list, or radio | choice | yes | none |
| Number, whole, percent, duration | [[Text Field]] with unit suffix; Up and Down step within the range | Enter or focus leaves | yes | range refusal |
| Text, path, name | [[Text Field]] (path adds Browse) | Enter or focus leaves | yes | pattern, existence |
| Colour, icon, font | picker button | pick | yes | none |
| Key chord | record field | key chord complete | yes | chord syntax |
| List of items | list editor with Add, Move, Remove | each change | yes | length, unique |
| Block with required keys | Add, Open, Reset buttons | click | yes | required keys |
| A value an expression sets | shown as text | edit of the text | no | parse |

## Examples (short snippets only)

```text
Row grid, compact (label 120, gap 8, control fills, reset 32):
| Gap          | [ 8      px ] [reset] |
|              | From 0 to 9          |   help line on focus within
```

```text
Ctrl+Shift+A   toggle Apply as I edit        F6 / Shift+F6   next / previous area
Ctrl+Z / Ctrl+Y   undo / redo                 Ctrl+S          save
Ctrl+Shift+L   reload from disk              Ctrl+Shift+U    keep mine
```

## States

| State | Visual change | Token values |
|---|---|---|
| Clean | no marker; reset disabled | [[Form Row]] |
| Modified row | reset enabled; choice button tonal | [[Form Row]] |
| Document dirty | status line text "Unsaved changes", file marker text | `body_small` |
| Live mode on | switch on; each commit writes | [[Switch]] |
| Disk change | banner `tertiary_container`, alert icon, Reload and Keep mine | [[Banner]] |
| Saving | status line text; Save button `busy` | [[Loading States]] |
| Invalid row | error line, `invalid` | [[Validation]] |
| Read-only folder | Save fails with message, edits kept | [[Error States]] |

## Sizing and density

Row, control, reset, label column and gap values per density are in [[Form Row]] and [[Spacing and Density]] (control 40, 32, 28 dp; reset icon 24, 20, 20 dp; row gap 8, 4, 2 dp; label column 160, 120, 96 dp). Group header height equals the control height. The banner has padding 8 dp, gap 8 dp, icon 18 dp, buttons at the density height. The form content width has no maximum; a text field fills the control column with minimum width 0.

## Accessibility

- Each row: control name equals the label, description equals the help text, error line polite ([[Form Row]]).
- Every action (rows, buttons, menu entries, areas) works from the keyboard alone; Tab order follows the F6 order of [[Config App Layout]] (Files, Structure, Editor, View, Properties, Problems), after the toolbar; F6 cycles areas.
- Group headers are buttons with `expanded`; the banner is a group named "File changed on disk" with a live text.
- The dirty state and modified state have text, not colour alone (SC 1.4.1).
- Undo and redo are available by key and by toolbar button with names.

## Acceptance criteria

- [ ] AC-FST-1 (geometry check): in a form of 12 rows the control column left edge is identical (0.5 dp) in every row and the label column width equals the density value (160, 120, 96 dp). Pass: equal.
- [ ] AC-FST-2 (scripted input): a field commits on Enter and on focus leaving, and not while typing: after typing three characters the document is unchanged. Pass: document equal before Enter, changed after.
- [ ] AC-FST-3 (scripted input): in live mode a switch change writes the file once; in staged mode it changes the document and not the file until Save. Pass: file write count equals.
- [ ] AC-FST-4 (scripted input): the mode switch persists across an app restart and Ctrl+Shift+A toggles it. Pass: state equal after restart and after the key.
- [ ] AC-FST-5 (AT tree assertion): a document with unsaved changes shows the text "Unsaved changes" in the status line and the file entry carries a text marker in its name; a clean document shows neither. Pass: strings equal.
- [ ] AC-FST-6 (scripted input): closing with unsaved changes opens a dialog with Save, Discard, Cancel, initial focus on Cancel; Cancel leaves the window open and the changes intact. Pass: focus owner and state equal.
- [ ] AC-FST-7 (scripted input): a row with a non-default value has its reset enabled; activating it removes or defaults the key, disables the reset, keeps its x position and width, moves focus to the first control and is undone by one Ctrl+Z. Pass: values, geometry (0.5 dp) and focus equal.
- [ ] AC-FST-8 (scripted input): ten edits followed by ten Ctrl+Z return the file to its original bytes; ten Ctrl+Y reproduce the edited bytes. Pass: byte equality.
- [ ] AC-FST-9 (scripted input): a save to a read-only folder fails, leaves the old file whole, keeps the window state, and shows an error naming the cause; a save of an unchanged opened file leaves the bytes identical. Pass: bytes and message equal.
- [ ] AC-FST-10 (scripted input): changing the open file on disk from outside raises the banner with Reload and Keep mine; the app's own save does not; a save before choosing is refused; Reload drops unsaved changes and resets the undo history; Keep mine lets the next save replace the disk. Pass: banner presence and file contents equal at each step.
- [ ] AC-FST-11 (AT tree assertion): the banner is a group with a name and a live text; its announcement is assertive with unsaved changes and polite without. Pass: politeness equals.
- [ ] AC-FST-12 (scripted input): F6 moves focus Files, Structure, Editor, View, Properties, Problems (when it has rows) and wraps; Shift+F6 reverses; F6 from the editor leaves it; a pane that is not shown (a tab not selected) is skipped. The config app is the reference ([[Config App Layout]]). Pass: focus order equals.
- [ ] AC-FST-13 (scripted input): a group header toggles with Enter and Space; the open state is remembered by group name when another block is chosen and back; a group with a refused value opens by itself. Pass: expanded flags equal.
- [ ] AC-FST-14 (scripted input): hovering the label for 500 ms shows one tooltip with the description; the row, group and form show none; focus within the row shows the help line and does not move the control. Pass: tooltip counts and geometry equal ([[Form Row]] AC-FRM-4, AC-FRM-12).
- [ ] AC-FST-15 (scripted input): every action of the page is performed by key events only. Pass: every action's effect observed (AC-A11Y-4).
- [ ] AC-FST-16 (review): the form states its apply mode, every row has a default, and no destructive action lacks undo or a recoverable place. Pass: checklist per form.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:apps/shell_config` (`Views/Main_View.tdl`, `form.py`, `widgets.py`, `session.py`, `watcher.py`, `README.md`), `tess-ui:docs/guide/shell-config.md` | partly meets as the reference: row grid, label box, reset, help on focus, polite error line, groups with remembered open state, mode switch with Ctrl+Shift+A, undo and redo, atomic save with backup, disk-change banner with Reload and Keep mine, F6 area cycling, trash on delete, Menu key and Shift+F10 (AC-FST-2, AC-FST-3, AC-FST-4, AC-FST-8 to AC-FST-10, AC-FST-12, AC-FST-13 by reading); label column fixed 120 and compact only (AC-FST-1 partly); no tess-ui form, group or banner view, everything is hand built (the pattern has no shipped element); banner uses `Live: assertive` always (AC-FST-11 partly); close-with-unsaved dialog and "Unsaved changes" text not verified (AC-FST-5, AC-FST-6 unmeasured); single-line text field centring is by padding (F7) |
| tess-shell | none | absent: the shell has no settings forms; its config is edited by the config app and files |
| tre | `tre:docs/reference/node.md` flags | not applicable: no form concept; `invalid`, `description`, `read_only` flags only |

Request candidates: shipped `FormRow`, `FormGroup` and `Banner` views in tess-ui so apps stop hand building them; routed through the Orchestrator.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Label beside the control instead of a floating or in-field label | scan by a fixed label column | [[ADR-0002 Desktop density levels and target sizes]] |
| Persistent per-row reset and a staged or live mode | defaults matter in configuration files | none; design choice |
| Banner as a page-level surface | external changes need a persistent message | none; see [[Notifications]] |
| Commit on Enter or focus leave | desktop forms with many rows | none; see [[Validation]] |

## Sources

- No MD3 form or settings pattern exists: [Material Web components](https://github.com/material-components/material-web/tree/main/docs/components) and [Android components](https://github.com/material-components/material-components-android/tree/master/docs/components) list controls only (checked 2026-11-21) #needs-verification (m3.material.io).
- [WCAG 2.2 SC 3.3.4 Error Prevention](https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html), [SC 2.1.1](https://www.w3.org/TR/WCAG22/#keyboard), [SC 1.4.1](https://www.w3.org/TR/WCAG22/#use-of-color); [WAI-ARIA APG Disclosure pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/) for group headers.
- Code, the reference implementation: `tess-ui:apps/shell_config/README.md` ("The form", "Check, saving and the shell", "What it keeps and what it never does", keys table); `tess-ui:docs/guide/shell-config.md`; `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`.
- Owner feedback F6, F7, F8: [[Owner Feedback 2026-11-20]]; gaps: [[Gaps and Contradictions]].
