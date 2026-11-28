---
title: Config App Layout
type: pattern
status: draft
owner: phil
created: 2026-11-27
updated: 2026-11-27
tags: [pattern, layout, dock, config-app]
related: ["[[Dock]]", "[[Dock Panel]]", "[[Tabs]]", "[[Splitter]]", "[[Status Bar]]", "[[Preview Pane]]", "[[Keyboard Navigation]]", "[[Forms and Settings]]", "[[11 Interaction]]", "[[15 Writing]]", "[[Spacing and Density]]"]
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
5. Toolbar above the dock and a [[Status Bar]] under it, as today.

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

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` | in progress: the docked layout is being built; not re-checked |
| tess-shell | not applicable | not applicable |
| tre | not applicable | not applicable |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Element added that MD3 lacks | a tool window layout for a configuration application | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Open questions

- Whether 380 dp still suits the longest Properties rows: the widest need about 420 px, so such a row is clipped or wrapped at the default ([[10 Layout Overflow and Scrolling]] applies).
- Corner ownership is specified in [[Dock]] AC-DCK-17; tess-ui's `Dock` behaviour is not re-checked.

## Sources

- Owner decision of 2026-11-27 relayed by the Orchestrator (decisions, not verified claims).
- [[Dock]], [[Dock Panel]], [[Preview Pane]], [[Keyboard Navigation]], [[11 Interaction]].
