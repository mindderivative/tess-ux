---
title: File Dialog
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, dialog, file, picker, keyboard, containment]
related: ["[[Dialog]]", "[[Scrim]]", "[[Text Field]]", "[[Button]]", "[[Icon Button]]", "[[Switch]]", "[[List]]", "[[List Item]]", "[[Menu]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Form Row]]", "[[Deviations from MD3]]"]
depends_on: ["[[Dialog]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
---

# File Dialog

> [!info] Summary
> A modal, in-app dialog for choosing files to open, a folder, or a folder plus a name to save under, with a path bar, a trail of folder buttons, a list of entries (folders first, then files), file-type filters and full keyboard use. Material Design 3 has no file dialog (see Sources); the note builds on the MD3 [Dialog](https://m3.material.io/components/dialogs/overview) ([[Dialog]]), list, text field and menu. Source of truth in code: the last section.

## Purpose

Let a person point an application at a file or folder without a window of the operating system, and let a script or test drive the same choice. The dialog never reads or writes file contents; it answers with absolute paths (`tess-ui:docs/components/file-dialogs.md`).

## When to use and not

- Use when: the app needs one or several existing files (`open`), a folder and a file name (`save`), or a folder (`folder`) on a desktop file system.
- Do not use when: the choice is among a few known options ([[Choice Picker]], [[Menu]]); the value is an icon, font or colour ([[Icon Picker]], [[Font List]], [[Colour Picker]]); the user can type a short path and does not need browsing (a [[Text Field]] with a Browse [[Button]] opens this dialog, as the config app does for path keys).
- A confirmation of a destructive step inside the dialog ("Replace file?") uses a nested [[Dialog]], not a message line.

## Anatomy

1. Scrim and modal surface: [[Dialog]] container over [[Scrim]] (`surface_container_high`, 28 dp corners, elevation level 3, 24 dp padding, 12 dp gap).
2. Headline (`headline_small`, `on_surface`, heading level 2): `Open file`, `Save file` or `Choose folder`.
3. Toolbar: [[Icon Button]] Back, Forward, Up, Home, Refresh, then the path field ([[Text Field]]) filling the rest of the row.
4. Places (sidebar of fixed locations: Home, Desktop, Documents, Downloads, mounted volumes, bookmarks). Not built (see Status in code); specified under Places.
5. Crumbs: the folders of the current path as text [[Button]]s separated by chevron icons.
6. Column header row: icon column (24 dp), Name, Size (80 dp, end aligned), Modified (140 dp), in `label_large`, `on_surface_variant`.
7. Entry list: a virtual [[List]] of rows, each with a 24 dp icon, name (`body_large`, one line, ellipsis), size and modified time (`body_medium`, `on_surface_variant`). A [[Scrollbar and Scroll Container]] on the end edge.
8. Filter control (file types, menu button) and a switch for names that start with a dot.
9. Save only: file name [[Text Field]]; save and folder modes: New folder [[Button]].
10. Message line (role `alert`, `error`) and empty-folder note (`on_surface_variant`).
11. Actions: Cancel (text [[Button]]) and the accept [[Button]] (`Open`, `Save` or `Choose`), right-aligned.
12. Preview pane (optional, not built).

## Variants

| Variant | Use | Differences |
|---|---|---|
| `open` single | one existing file | accept is off until a file is picked; a folder is never an answer |
| `open` multiple | several files | Ctrl and Shift extend picks; Ctrl+A picks every file; `Value` is a list |
| `save` | folder and name | the name field starts with `Filename`; a name without extension takes the extension of the filter in use; an existing file asks "Replace file?" |
| `folder` | one folder | only folders are listed; nothing picked means the shown folder |
| Rooted | restrict to a tree | `Root` bounds the path bar, Up, Back, Home, crumbs and links |

## States

| State | Visual change | Token values |
|---|---|---|
| Row rest | transparent | row container `transparent`, name `on_surface` |
| Row hover | state layer | `on_surface` at the hover opacity of [[State Layers]] |
| Row cursor (keyboard) | cursor row filled and focus ring | `surface_container_highest`; [[Focus Ring]] |
| Row picked | filled | `secondary_container`, name `on_secondary_container` |
| Row disabled | not applicable: rows are entries, an unreadable entry shows as a message | not applicable |
| Toolbar button disabled | Back, Forward, Up are disabled when there is no history or no parent | 0.38 on content |
| Accept disabled | until there is something to give | 0.38 on content, 0.12 on container |
| Empty folder | note "empty" in the list area | `on_surface_variant` |
| Error | folder unreadable, gone, a file, or a bad save name: message under the list, dialog stays usable | `error`, role `alert` |
| Loading | a folder read is one listing; a read longer than 200 ms shows an indeterminate progress indicator in the list area | specified here; not built |

## Tokens used

Roles in [[Colour Roles]]; type roles `headline_small`, `label_large`, `body_large`, `body_medium` in [[Typography]]; corner 28 dp (dialog) and 12 dp (row) in [[Shape]]; elevation level 3 in [[Elevation]]; state layers in [[State Layers]]; ring in [[Focus Ring]]. Folder and file glyphs use [[Iconography]] at 24 dp, `on_surface_variant`.

## Sizing and density

The dialog panel is `Width` 720 dp by default (480 to 1080); the window clamps it as [[Dialog]] does for its margin, but the 280 to 560 dp width range of [[Dialog]] does not apply (see Deviations). Density follows [[Spacing and Density]]; the dialog applies the level of its project to controls and rows:

| Part | default | compact | dense | Code today |
|---|---|---|---|---|
| Toolbar icon button container | 40 | 32 | 28 | 40 (IconButton default) |
| Path field height | 40 | 32 | 28 | 40 |
| Crumb button height | 40 | 32 | 28 | 36 container, `xs` button |
| List row height (`Row_Height`) | 40 | 32 | 24 | 40 at every level |
| Column header row | 40 | 32 | 24 | 32 |
| Row horizontal padding | 12 | 8 | 4 | 8 |
| Icon-to-name gap | 8 | 8 | 4 | 12 |
| Row icon | 24 | 20 | 20 | 24 |
| Visible rows (`Rows`) | 8 | 8 | 8 | 8 (3 to 20) |

The panel padding stays 24 dp and the gap 12 dp at every level (a dialog is a container, not a row). A touch context raises every hit area to 48 dp without changing painted sizes ([[Spacing and Density]], Target sizes).

## Layout and overflow

- Vertical centring: icon, name, size and time are centred on the row height; the text line box is centred within 1 px ([[10 Layout Overflow and Scrolling]]).
- Name: one line, end ellipsis, minimum width 0 so the size and time columns never move; the full name is available by a tooltip on the name text only when truncated ([[Tooltip]], ADR-0004).
- Paths: every place that shows a path as plain text truncates in the middle with `…` (U+2026) so the first segment and the file or folder name stay visible, for example `~/Documents/…/2026/plan.tdl`. This covers the path field when not focused, a message that names a path, and the accessible description of an entry. A focused path field scrolls its caret into view and shows the whole text ([[10 Layout Overflow and Scrolling]], middle ellipsis for paths).
- Crumbs: when the trail is wider than the toolbar, the leading crumbs collapse into one `…` button that opens a [[Menu]] of the hidden folders; the last crumb stays visible and a crumb never wraps.
- Columns: Size 80 dp and Modified 140 dp are fixed; Name takes the rest. Below 480 dp panel width the Modified column is hidden before Name shrinks below 160 dp.
- Scrolling: the entry list scrolls vertically with a visible [[Scrollbar and Scroll Container]] thumb when more than `Rows` entries exist ([[ADR-0003 Scrollbar rule]]); a folder of ten thousand entries builds only the visible rows plus three rows past each edge. No horizontal scroll: rows truncate.
- A window smaller than the panel shrinks the panel to the window minus 2 times the 24 dp margin ([[Dialog]]).

## Places

Places is a column at the start edge of the panel, 160 dp wide at default (120 at dense), `body_medium` rows with a 24 dp icon, role `list` named "Places". It holds fixed entries (Home, Desktop, Documents, Downloads), mounted volumes and bookmarks added by the user. Activating a place goes to that folder, as the Home button does. A bookmark is added with Ctrl+D and removed from its context [[Menu]]. The sidebar is hidden below 600 dp panel width. This is a specification; the code has no places sidebar (Not built).

## Path entry

- The path field takes a path, `~`, or `~/…`; Enter goes there; an entry that is not a folder shows "not a folder" in the message line and keeps the old folder.
- Ctrl+L focuses the path field and selects its text (desktop convention; not in code today). Typing `/` in the list is not a jump key.
- Tab completion: Tab in the path field completes the unique prefix of the next segment; a second Tab opens a list of candidates. Not built.
- The path field mirrors the current folder after every navigation.

## Behaviour

- Pointer: a click picks a row; Ctrl and Shift (multiple) flip and extend picks; a double click on a folder enters it, on a file accepts it. A click on a crumb goes to that folder. The wheel scrolls the list. Drag and drop of files into the list is not built.
- Keyboard: the entry list has focus when the dialog opens. Tab order: list, then Back, Forward, Up, Home, Refresh, path field, crumbs, filter, hidden switch, name field (save), New folder, Cancel, accept. Focus is trapped in the dialog ([[Dialog]]).

| Key (in the list) | Action |
|---|---|
| Up, Down | move the cursor row and pick it |
| Page Up, Page Down | move by `Rows` rows |
| Home, End | first, last row |
| Shift plus a move key | extend the pick (multiple only) |
| Ctrl plus click | flip a pick (multiple only) |
| Ctrl+A | pick every file (multiple only) |
| Enter | open the folder, or choose the file and accept |
| Backspace | go up one folder |
| Alt+Left, Alt+Right | Back, Forward |
| Printable characters | jump to the next name that starts with them; the buffer resets after 1 s |
| Escape | cancel and close, writing `Open` false |

- Touch: rows use the 48 dp touch hit area; the wheel is replaced by drag scroll.
- Save: when the name has no extension the extension of the filter in use is added; a name with `/` or `\` or the name of a folder is a problem shown in the message line; an existing file opens a nested "Replace file?" [[Dialog]] with Cancel and Replace.
- The dialog never raises on a failed read: the message says why and the dialog stays where it was.

## Tooltip and overlay behaviour

- Tooltips belong to controls only (ADR-0004, ADR-0011): the five toolbar [[Icon Button]]s show their label (Back, Forward, Up, Home, Refresh) after 500 ms on hover and at once on keyboard focus; the filter button shows the current filter; a truncated name shows its full name. A row, the toolbar and the panel carry no tooltip.
- The dialog is a modal overlay ([[12 Overlays]]) with a scrim; a press on the scrim and Escape cancel. Initial focus is the entry list. On close focus returns to the opener.
- The filter menu and the crumb overflow menu are [[Menu]]s anchored to their buttons.

## Motion

The panel enters and exits as [[Dialog]] does ([[Motion]]); row focus and picks change without animation. Reduced motion removes the enter and exit transform and keeps a fade of at most 100 ms.

## Accessibility

- Role `dialog`, modal, named by the headline. The entry list is role `listbox` (multiselectable when `Multiple`) with rows `option` named by the file name and `selected` when picked; code uses `list` and `listitem` (see Status). The crumbs are a `group` named "Folders in the path". Every icon button has an accessible name. The message line is role `alert`, live polite.
- Selection announcements: moving the cursor announces the entry name, kind ("folder" or "file"), size and position ("3 of 120"); extending a pick announces "n selected" once per key press, not per row; entering a folder announces the folder name and the entry count.
- Keys: the table above; every pointer action has a key equivalent.
- Contrast: text pairs at least 4.5:1, icons and the cursor fill at least 3:1 ([[Colour Roles]]); `secondary_container` against `surface_container_high` is a fill, the row name uses `on_secondary_container`.
- Target size: at least 24 by 24 dp at every density ([[ADR-0002 Desktop density levels and target sizes]]).

## Dark and light

Roles only ([[Theme Following the System]]); no value is literal. The dialog follows the window theme.

## Defaults

Mode `open`, one file, `Width` 720 dp, `Rows` 8, hidden names off, filters `All files`, start at `Root` then the working folder, sort folders first then files, each case-insensitive. Default level: `default` unless the project sets one.

## Acceptance criteria

- [ ] AC-FDL-1 (geometry check): at default, compact and dense a list row is 40, 32 and 24 dp high and toolbar icon button containers are 40, 32 and 28 dp, at scale 1.0 and 2.0.
- [ ] AC-FDL-2 (AT tree assertion): the panel has role `dialog` with the headline as name; the list is `listbox` or `list` with an accessible name; each row has a name equal to its file name and `selected` equals pick state.
- [ ] AC-FDL-3 (scripted input): on open the entry list holds focus; Tab 20 times then Shift+Tab 20 times never leaves the dialog and follows the order in Behaviour.
- [ ] AC-FDL-4 (scripted input): in a folder of 20 entries Down, Up, Home, End, Page Down move the cursor to rows 1, 0, 0, 19 and min(19, Rows) and never past the ends; the cursor row is scrolled into view.
- [ ] AC-FDL-5 (scripted input): Enter on a folder enters it and the path field text equals its absolute path; Backspace goes up; Alt+Left and Alt+Right retrace the history.
- [ ] AC-FDL-6 (scripted input): typing "ba" within 1 s moves the cursor to the next name starting with "ba" (case-insensitive); after 1 s idle the buffer is empty.
- [ ] AC-FDL-7 (scripted input): in a `multiple` dialog Ctrl+A picks every file and no folder; Shift+Down extends by one row; Ctrl plus click flips one row; `Value` is a list of absolute paths in list order.
- [ ] AC-FDL-8 (scripted input): in `save` mode the name "plan" with filter `*.tdl` yields `plan.tdl`; "a/b" and the name of a folder show a message of role `alert` and keep accept disabled; an existing name opens a nested dialog "Replace file?" and writes `Value` only after Replace.
- [ ] AC-FDL-9 (scripted input): Escape and a press on the scrim close the dialog, write `Open` false and call `On_Cancel` once; `Value` is unchanged; focus returns to the opener within one frame.
- [ ] AC-FDL-10 (pixel check): a 300 dp wide file name in a 100 dp wide name cell ends in `…` and shows no ink beyond the cell; the Size and Modified columns keep their x positions.
- [ ] AC-FDL-11 (geometry check): an unfocused path field whose text exceeds its width shows the first segment, `…` and the last segment (middle ellipsis); the last character of the text is visible; a focused field shows the caret.
- [ ] AC-FDL-12 (geometry check): with a trail wider than the toolbar the last crumb is fully visible and the leading crumbs are replaced by one `…` button that opens a menu listing each hidden folder.
- [ ] AC-FDL-13 (scripted input): a tooltip appears on the Back button after 500 ms of hover and immediately on keyboard focus, and none appears over a row, the toolbar background or the panel; Escape, a press, a scroll of the list and leaving the button remove it ([[Tooltip]]).
- [ ] AC-FDL-14 (geometry check): a folder of 10000 entries builds at most `Rows` + 6 row nodes; the list shows a scrollbar thumb whose length is at least the minimum thumb length of [[Scrollbar and Scroll Container]].
- [ ] AC-FDL-15 (scripted input): with `Root` set, the path field, Up, Back, Home, crumbs and a symlink leading out all fail to leave the root and show a message.
- [ ] AC-FDL-16 (scripted input): an unreadable folder shows a message of role `alert` in `error` and the previous folder stays listed; no exception reaches the app.
- [ ] AC-FDL-17 (scripted input): Ctrl+L focuses the path field and selects its text; Enter with a valid folder navigates; with an invalid path the old folder stays and the message names the problem.
- [ ] AC-FDL-18 (geometry check): when Places exists, its column is 160 dp wide at default, and activating Documents sets the path field to the Documents folder; the column is hidden at a panel width below 600 dp.
- [ ] AC-FDL-19 (contrast script): row name on `secondary_container` uses `on_secondary_container` at least 4.5:1, `on_surface_variant` size text on `surface_container_high` at least 4.5:1, in light and dark at standard contrast.
- [ ] AC-FDL-20 (review): the note states overflow per axis and every control has a tooltip or a visible text name; a reviewer finds no tooltip on a row or container.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/FileDialog_View.tdl`, `tess-ui:src/tess_ui/views/FileDialog_Stylesheet.tdl`, `tess-ui:src/tess_ui/file_browser.py`, `tess-ui:src/tess_ui/file_controls.py`, `tess-ui:src/tess_ui/file_dialog.py`, `tess-ui:docs/components/file-dialogs.md` | partly meets. Passes AC-FDL-3, 4, 5, 6, 7, 8, 9, 15, 16 by documented behaviour (not run here). Fails AC-FDL-1 at compact and dense (row 40, header 32, no density input), AC-FDL-2 (role `list` and `listitem` rather than `listbox` and `option`), AC-FDL-11 and AC-FDL-12 (path field and crumb buttons do not truncate in the middle or collapse), AC-FDL-17 (no Ctrl+L), AC-FDL-18 (no places) |
| tess-ui | Not built, recorded as status per the component doc | places sidebar and bookmarks, preview, drag and drop, renaming and deleting, sorting by a column, a column for file type, the Windows hidden flag, a folder tree, drives on their own |
| tess-shell | `tess-ui:apps/shell_config` path keys (Browse button opens the shipped dialog) | partly meets: uses the toolkit dialog unchanged; the shell itself has no file dialog |
| tre | none | not applicable: the engine draws rows; the dialog lives in tess-ui |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element has no MD3 counterpart | desktop applications need a file chooser; built from MD3 dialog, list, text field, menu | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Row 40, 32, 24 dp and padding 12, 8, 4 dp | desktop information density | [[ADR-0002 Desktop density levels and target sizes]] |
| Tooltips on toolbar buttons and truncated names only, never on rows | owner feedback F2, F8 | [[ADR-0004 Tooltip rule]] |
| Entry list scrollbar always visible when it overflows | desktop pointer use | [[ADR-0003 Scrollbar rule]] |
| Panel width 480 to 1080 dp (MD3 and [[Dialog]] 280 to 560 dp) | a file list with size and time columns needs width | [[ADR-0002 Desktop density levels and target sizes]] |
| Middle ellipsis for paths | the end of a path identifies it | [[ADR-0004 Tooltip rule]] |

## Sources

- tess-ui component doc and views: `tess-ui:docs/components/file-dialogs.md`, `tess-ui:src/tess_ui/views/FileDialog_View.tdl`, `tess-ui:src/tess_ui/views/FileDialog_Stylesheet.tdl`.
- WAI-ARIA APG dialog (modal) https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ and listbox https://www.w3.org/WAI/ARIA/apg/patterns/listbox/ (Home, End, Page Up and Page Down, Space, type-ahead recommended). Verified reachable 2026-11-21.
- WCAG 2.2 SC 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, SC 4.1.3 https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html, SC 1.4.3 https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html, SC 1.4.11 https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html.
- MD3 Dialog https://m3.material.io/components/dialogs/overview (page is a JavaScript app; values taken from [[Dialog]]).
- The 200 ms threshold for a loading indicator and the Ctrl+L, Ctrl+D shortcuts are desktop conventions, not from a cited standard #needs-verification.
