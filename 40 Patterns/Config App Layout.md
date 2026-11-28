---
title: Config App Layout
type: pattern
status: draft
owner: phil
created: 2026-11-27
updated: 2026-11-28
tags: [pattern, layout, dock, config-app]
related: ["[[Dock]]", "[[Dock Panel]]", "[[Tabs]]", "[[Splitter]]", "[[Status Bar]]", "[[Preview Pane]]", "[[Menu Bar]]", "[[Toolbar]]", "[[Title Bar]]", "[[Iconography]]", "[[Keyboard Navigation]]", "[[Forms and Settings]]", "[[11 Interaction]]", "[[15 Writing]]", "[[Spacing and Density]]", "[[ADR-0029 Desktop density and type scale]]"]
depends_on: ["[[Dock]]", "[[Preview Pane]]"]
---

# Config App Layout

> [!info] Summary
> The window layout of the Tesserae Shell configuration application: a docked arrangement with Files and Structure on the left, Editor and View in the centre, Properties on the right and Problems under the centre. The layout, the names and the sizes are decisions of the owner (2026-11-27, relayed by the Orchestrator) and are recorded here as decisions, not as verified claims. Status in code: in progress (tess-ui `apps/shell_config`; not re-checked). Material Design 3 has no counterpart; the parts are [[Dock]], [[Dock Panel]], [[Tabs]], [[Splitter]] and [[Status Bar]].

## Purpose

One agreed layout so the keyboard order, the names read by assistive technology and the acceptance criteria of the configuration application are testable, and so a later tool of the same kind can copy it.

## When to use and not

- Use when: an application edits a structured file with a file list, a structure tree, a text editor, a visual preview, a property form and a list of findings.
- Do not use when: the tool has one form and nothing else ([[Forms and Settings]]).

## Anatomy

1. Left zone, full height: panels Files and Structure as tabs (a [[Dock]] zone).
2. Centre zone: panels Editor and View as tabs.
3. Right zone, full height: the panel Properties (the form of the selected block).
4. Bottom zone, under the centre only: the panel Problems ([[Dock]] corner rule: side zones run the full height).
5. [[Menu Bar]] (File, Edit, View, Shell) under the [[Title Bar]], then the [[Toolbar]] of icon buttons above the dock, and a [[Status Bar]] under the dock (see Menus and toolbar).

## Decisions (owner, 2026-11-27)

| Topic | Decision |
|---|---|
| Panels | fixed: the user cannot close, add or move panels (no `Closable`, no drag between zones); tabs only choose which panel of a zone is shown |
| Default sizes | left 240 dp, right 380 dp, bottom 160 dp (the right zone was 320 dp in the owner's 2026-11-27 decision; raised to 380 dp on 2026-11-28 because the widest Properties rows need about 420 px, tess-ui #405; an owner-informed change, the owner is told) |
| Names | Files, Structure, Editor, View, Properties, Problems (sentence case, [[15 Writing]]); "Problems" and not "Errors", because findings include warnings |
| F6 order | Files, Structure, Editor, View, Properties, Problems |
| View | a live visual mockup of the shell with the Panel as the desktop, fidelity level A, drawn as a [[Preview Pane]] |

## Layout and sizes

- Zone sizes are the defaults above, resizable with the zone handles ([[Dock]] AC-DCK-3, AC-DCK-4) and clamped as the Dock says (120 dp minimum, 70 percent of the room). The centre zone keeps its minimum at narrow widths ([[Dock]] AC-DCK-13).
- Density is `compact` for configuration tools ([[Spacing and Density]]).
- The Problems zone is empty and hidden when there are no findings ([[Dock]] AC-DCK-12); its panel and tab appear when the first finding is listed.

## Behaviour

- Selecting a node in Structure shows its block in Properties and, in Editor, places the caret at the block; View is a one-way picture of the file and does not select ([[Preview Pane]] rule 7).
- A row in Problems opens its place in Editor (`file:line:column`, [[15 Writing]]) and moves focus there.
- Editor and View are tabs of the centre zone, so exactly one is shown; F6 skips the one that is not shown ([[11 Interaction]]).
- The layout (zone sizes, shown tab per zone) is saved and restored ([[Dock]] AC-DCK-9).

## Keyboard

F6 and Shift+F6 cycle Files, Structure, Editor, View, Properties, Problems and wrap; a pane that is not shown or has no focusable content is skipped, Problems joins when it lists something. Tab inside a zone strip is one stop with arrows between tabs ([[Dock]] AC-DCK-8). F6 leaves the Editor, which takes Tab for itself. Every layout function has a keyboard path ([[Dock]] AC-DCK-15).

## Accessibility

- Zone strips: role `tablist` named "{Side} panels" ([[Dock]] AC-DCK-10): "Left panels", "Right panels", "Bottom panels", "Centre panels" (an English spelling choice, #needs-verification).
- Each panel: role `tabpanel` named by its title. View is one `img` region with a description ([[Preview Pane]] AC-PRV-3).
- Problems: a change of the number of findings raises one polite announcement, "3 problems", through the status bar ([[Status Bar]] AC-STB-7).

## Acceptance criteria

- [ ] AC-CFG-1 (geometry check): at 1100 by 700 dp with default sizes, the left zone is 240 dp wide and the right zone 380 dp wide, both full height; the bottom zone is 160 dp high and spans only the width between them; the centre fills the rest. Pass: rectangles equal.
- [ ] AC-CFG-2 (AT tree assertion): the panel titles read, in tree order, Files, Structure, Editor, View, Properties, Problems; no panel is named Form, Text or Errors. Pass: names equal.
- [ ] AC-CFG-3 (scripted input): F6 from Files goes to Structure, Editor (when Editor is the shown centre tab), Properties, Problems (when it has findings) and wraps; with View shown instead of Editor, F6 goes Structure, View, Properties; Shift+F6 reverses. Pass: focus order equals in each case.
- [ ] AC-CFG-4 (scripted input): no panel has a close button and a tab drag does not change a panel's zone (a press on a tab and a move of 40 dp leaves it in place); the tab menu offers no move. Pass: zone of each panel unchanged.
- [ ] AC-CFG-5 (scripted input): with no findings the bottom zone and its handle are absent and the centre zone takes the room; adding one finding shows the zone at 160 dp. Pass: rectangles equal.
- [ ] AC-CFG-6 (scripted input): activating a Problems row moves focus to the Editor with the caret at the row's line and column, and shows the Editor tab when View was shown. Pass: focus owner, caret and shown tab equal.
- [ ] AC-CFG-7 (scripted input): saving and restoring the layout after resizing every zone and selecting the other tab of each zone gives equal sizes and shown tabs. Pass: equal.
- [ ] AC-CFG-8 (review): the View obeys every rule of [[Preview Pane]] and shows the Panel as the desktop at fidelity A (the shell's structure and theme, not its behaviour); a reviewer lists no interactive element in the View. Pass: zero violations.
- [ ] AC-CFG-9 (AT tree assertion, menu bar): below the title bar the window has a `menubar` (today a `group` if the engine lacks the role) named "Menu bar" with the titles File, Edit, View, Shell in that order and the mnemonics F, E, V, S; each menu lists the entries of the menu map with their shortcuts as the key shortcut; no entry exists for a command the application lacks. Pass: names, order, shortcuts equal.
- [ ] AC-CFG-10 (scripted input, menu commands): from every control including the Editor: Alt+F opens File; Ctrl+S saves once with the menu closed; choosing View, Theme, Dark sets the theme and exactly one radio entry is checked; Shell, Apply as I edit flips the check and the toolbar toggle together. Pass: state and counts equal.
- [ ] AC-CFG-11 (scripted input, command parity): for each toolbar item, the menu entry of the same name has the same enabled state at every step of a script that edits, saves, checks and reloads; a toolbar command that is not a menu entry fails. Pass: equal at each step.
- [ ] AC-CFG-12 (geometry check, density): at `compact` the menu bar is 32 dp and the toolbar 40 dp high with 32 dp icon buttons (20 dp icons); the Files and Structure trees are `dense` (24 dp rows, 13/18 text); control heights, switches and dropdowns in Properties are 32 dp ([[ADR-0029 Desktop density and type scale]], [[Spacing and Density]] AC-DEN-2). Pass: rectangles and text roles equal.
- [ ] AC-CFG-13 (scripted input, toolbar): the toolbar is one Tab stop, Right and Left move between its items and skip the dividers between the three groups, a tooltip shows the name and the shortcut on hover and on keyboard focus, and no toolbar item has visible text. Pass: focus order, tooltip text and tree equal ([[Toolbar]] AC-TLB-15, AC-TLB-16).

## Menus and toolbar

Decisions of this record follow the owner feedback of 2026-11-28 (the top bar of text buttons is not a toolbar; add a top menu with File, Edit, View; make the toolbar a real one) and the specifications [[Menu Bar]] and [[Toolbar]]. They are proposals until the owner confirms the menu map.

Order from the top: [[Title Bar]], [[Menu Bar]], [[Toolbar]], the dock, [[Status Bar]]. The Tab order is menu bar, toolbar, then the panels in F6 order; the menu bar is reached by Alt or F10, the toolbar by Tab. Application density is `compact` (32 dp bar, 40 dp toolbar of 32 dp icon buttons with 20 dp icons); the Files and Structure panels are `dense` ([[ADR-0029 Desktop density and type scale]]).

### Menu map

Shortcuts are those the application already has; a blank cell means no shortcut today (none is invented). Mnemonics are the underlined letters; titles `&File`, `&Edit`, `&View`, `&Shell` are unique.

| Menu | Entries (shortcut) |
|---|---|
| `&File` | New file... (Ctrl+N); Save (Ctrl+S); separator; Rename file... (F2); Duplicate file (Ctrl+Alt+D); Delete file (Delete in Files); separator; Reload from disk (Ctrl+Shift+L) and Keep my version (Ctrl+Shift+U), enabled only while the file changed on disk; separator; Quit (Ctrl+Q) |
| `&Edit` | Undo (Ctrl+Z); Redo (Ctrl+Y, Ctrl+Shift+Z shown as Ctrl+Y); separator; Format file; separator; submenu Structure: Add child block... (Ctrl+Shift+N), Duplicate block (Ctrl+Shift+D), Move block into... (Ctrl+Shift+M), Move up (Alt+Up), Move down (Alt+Down), Remove block (Ctrl+Shift+Delete) |
| `&View` | submenu Theme, radio: System, Light, Dark (Ctrl+Shift+T cycles them); submenu Go to: Files, Structure, Editor, View, Properties, Problems (enabled only when it lists something); the commands show the panel's tab and move focus there, F6 and Shift+F6 cycle them; separator; Reset layout (default zone sizes and tabs) |
| `&Shell` | Check (F5); Reload shell (Ctrl+Shift+R); separator; Apply as I edit, a check item (Ctrl+Shift+A) |

Quit (Ctrl+Q) and Reset layout are the two commands that do not exist in the application today (read at `origin/main`); they are proposed here. Everything else is an existing command with its existing shortcut. A command that cannot run is disabled and keeps its place (Save while the file is not changed, Undo with nothing to undo, Reload shell while the shell is not running, Reload from disk when the file did not change).

### Toolbar

Icon buttons with tooltips (name and shortcut), in three groups; every toolbar command is also a menu entry, with the same name and shortcut:

| Group | Items (icon, tooltip) |
|---|---|
| File | `save` "Save (Ctrl+S)", `undo` "Undo (Ctrl+Z)", `redo` "Redo (Ctrl+Y)" |
| Edit | `format_align_left` "Format file" |
| Shell | `task_alt` "Check (F5)", `refresh` "Reload shell (Ctrl+Shift+R)", `autorenew` toggle "Apply as I edit (Ctrl+Shift+A)", on or off |

The icon names are Material Symbols names offered as a starting point; the project picks the icons ([[Iconography]]). The "Apply as I edit" Switch leaves the toolbar (a switch is a setting, not a command, and the desktop toolbar holds none): it becomes the toggle above and the check item in the Shell menu. The title text that shared the toolbar leaves it (the window title carries it). Save is no longer a filled text button: the unsaved state shows as the enabled state of Save.

### Keyboard

Alt or F10 focuses the menu bar; Alt+F, Alt+E, Alt+V and Alt+S open the four menus; Escape returns focus to where it was ([[Menu Bar]]). F6 cycles panels only (the menu bar and the toolbar are not F6 stops); Tab walks the toolbar as one stop ([[Toolbar]]). The existing shortcuts keep working with every menu closed, from any control including the Editor, which takes Tab for itself.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` | in progress: the docked layout is built; the toolbar is still a row of seven controls (text buttons and a Switch) and there is no menu bar (read at `origin/main`, not run; AC-CFG-9 to AC-CFG-13 fail) |
| tess-shell | not applicable | not applicable |
| tre | not applicable | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | a tool window layout for a configuration application | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Open questions

- Whether 380 dp still suits the longest Properties rows: the widest need about 420 px, so such a row is clipped or wrapped at the default ([[10 Layout Overflow and Scrolling]] applies).
- Corner ownership is specified in [[Dock]] AC-DCK-17; tess-ui's `Dock` behaviour is not re-checked.
- Panels are fixed (decision above), so the View menu offers "Go to" commands and the tab choice, not show and hide; if the owner wants panels hidden by the user, that reverses the decision of 2026-11-27 and needs a new record.
- Not in the menus because the application has no such command today (read at `origin/main`): Open (the Files panel opens a file), Save as (Duplicate file and Rename file do it), Close file, Find, Cut, Copy, Paste, Select all (the Editor has its own keys). Add them when the command exists; a menu never lists a command that does nothing.
- Help menu (keyboard shortcuts list, about) is not specified: no such view exists.

## Sources

- Owner decision of 2026-11-27 relayed by the Orchestrator (decisions, not verified claims).
- [[Dock]], [[Dock Panel]], [[Preview Pane]], [[Keyboard Navigation]], [[11 Interaction]].
- [[Menu Bar]], [[Toolbar]]: the menu map and the toolbar of the application follow from the owner feedback of 2026-11-28 (a top menu with File, Edit, View and a toolbar of icons with tooltips); the shortcuts are those of `tess-ui:apps/shell_config/src/tess_shell_config/shortcuts.py` (read at `origin/main`, not run).
