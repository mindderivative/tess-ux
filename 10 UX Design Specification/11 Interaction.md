---
title: 11 Interaction
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, interaction, keyboard, pointer, touch]
related: ["[[01 Principles and Scope]]", "[[10 Layout Overflow and Scrolling]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[15 Writing]]", "[[17 Conformance]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Focus Ring]]", "[[State Layers]]", "[[Motion]]", "[[Spacing and Density]]", "[[Button]]", "[[Icon Button]]", "[[Switch]]", "[[Text Field]]", "[[Menu]]", "[[Popup]]", "[[Dialog]]", "[[Tooltip]]", "[[Tree]]", "[[Tree Node]]", "[[List]]", "[[List Item]]", "[[Accordion]]", "[[Scrollbar and Scroll Container]]", "[[Owner Feedback 2026-11-20]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]", "[[ADR-0012 Scrollbar thumb opacity and hit area exception]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[01 Principles and Scope]]", "[[14 Accessibility Basics]]", "[[Focus Ring]]", "[[State Layers]]"]
---

# 11 Interaction

> [!info] Summary
> How a person operates a Tesserae application with a pointer, a keyboard or a finger: the global keyboard map (Tab order, F6 pane cycling, Escape order, Enter and Space, arrow groups, typeahead, shortcuts), pointer rules (hover versus focus, double click, context menu, cursor shapes, drag and drop), touch rules (tap, long press, pan) and the three input matrices that a scripted test runs row by row. Component notes state their own keys and link here for the shared ones. Keyboard first is principle 1 of [[01 Principles and Scope]].

## Scope

Covers input rules that hold across elements. Not covered here: overlay placement and dismissal ([[12 Overlays]]), focus ring geometry ([[Focus Ring]]), state layer values ([[State Layers]]), scroll keys and scrollbar geometry ([[Scrollbar and Scroll Container]]), roles and names ([[14 Accessibility Basics]]). Where a component note defines a key (Tree, List, Menu, Text Field), this chapter names the shared rule and the component keeps the details. Wording of labels is in [[15 Writing]].

Evidence base: the config app key map (`tess-ui:apps/shell_config/README.md`, table "Keys", and `tess-ui:apps/shell_config/src/tess_shell_config/shortcuts.py`), the tess-ui interaction guide (`tess-ui:docs/guide/interaction.md`), the tre input model (`tre:docs/guide/events-and-input.md`, `tre:docs/reference/events.md`, `tre:docs/reference/node.md`), the tess-shell keyboard guide (`tess-shell:docs/guide/keyboard.md`) and the shell vault note `shell-vault:50 Design System/Standard Modules.md` (Keyboard Operation). Rules without a source in those files or in a cited standard are Tesserae design choices and carry `#needs-verification-as-design-choice`.

## Principles

1. Every pointer action has a keyboard path and every keyboard action is visible to assistive technology (WCAG 2.2 SC 2.1.1; [[14 Accessibility Basics]]).
2. Hover is an enhancement. Nothing is available only on hover; every hover effect has a focus equivalent ([[ADR-0004 Tooltip rule]], [[State Layers]]).
3. Activation happens on release of the press that began on the same control, so a press can be cancelled by moving away (WCAG 2.2 SC 2.5.2 Pointer Cancellation).
4. A key belongs to the innermost thing that uses it: the focused control, then an open overlay, then the focused region, then the application, then the shell or desktop. A rule below that overrides this order says so.
5. A control that cannot act takes no focus and no key; its pointer press is taken, so nothing behind it fires ([[Accessibility Rules]] AR-7).
6. Input never changes the layout under the pointer between press and release.

## Focus model

- Tab and Shift+Tab move focus in visual and reading order. Tab order equals tree order. A positive `tab_index` and the shell's `Tab_Index` are not used to reorder controls; order is fixed by layout ([[14 Accessibility Basics]]: "no positive tab indexes"). A negative `tab_index` removes a node from the order and is allowed for nodes reached another way (roving group members).
- Focus wraps within the window: Tab from the last control moves to the first; Shift+Tab from the first moves to the last. Inside a modal layer focus never leaves the layer ([[12 Overlays]], Focus).
- A composite widget is one Tab stop and uses arrow keys inside (roving focus, below). Examples: [[Tree]], [[List]], [[Menu]], toolbar, tab list, radio group, [[Accordion]] headers when grouped.
- A disabled control, a hidden control and the content of a collapsed container take no focus ([[Accessibility Rules]] AR-7).
- A click focuses the nearest focusable node under the pointer (tre). Focus from a pointer press does not show the focus ring; focus from the keyboard or assistive technology does (`focus_visible`; [[Focus Ring]] AC-FOC-3). A text field shows its focus indicator in both cases ([[Text Field]]).
- Focus that arrives never triggers an action or opens a dialog (WCAG 2.2 SC 3.2.1 On Focus). Opening a tooltip on focus is not an action ([[ADR-0004 Tooltip rule]]).
- A focused item is scrolled into view by the least distance ([[Scrollbar and Scroll Container]]).
- The initial focus of a window is the first control in Tab order, or the control the application names; a dialog follows its own rule ([[Dialog]]).

## Global keyboard map

Keys every Tesserae application MUST honour. A project may add keys; it MUST NOT bind these to anything else.

| Key | Context | Result | Source |
|---|---|---|---|
| Tab, Shift+Tab | anywhere except a control that documents otherwise | next, previous Tab stop | tre events guide; WCAG 2.2 SC 2.4.3 |
| Tab in a single-line text field | text field | leaves the field | tess-shell guide |
| Tab in a multi-line text field | text field | leaves the field unless `tab_navigates` is false; then Escape, then Tab | [[Text Field]] AC-TXF-8 |
| F6, Shift+F6 | window with two or more panes | focus to the next, previous pane (below) | config app README; `#needs-verification` as a cross-platform convention |
| Escape | anywhere | closes the topmost transient thing (Escape order below) and nothing else | [[12 Overlays]] AC-OVL-3 |
| Enter | focused button, link, menu item, list or tree row | activates | tre: Enter fires `click` |
| Space | focused button, switch, checkbox | activates or toggles | [[Switch]], [[Button]] |
| Arrow keys, Home, End, Page Up, Page Down | inside a composite widget | move within it (arrow groups below) | APG |
| Arrow keys, Home, End, Page Up, Page Down | focused node that does not use them | scroll the nearest scroll container ([[Scrollbar and Scroll Container]]) | tre 0.4.2 |
| Printable character | inside a list, tree or menu | typeahead | below |
| Menu key, Shift+F10 | focused item with a context menu | opens its context menu | APG keyboard interface table |
| Ctrl+C, Ctrl+X, Ctrl+V, Ctrl+A | text field | clipboard and select all | tre text input |
| Ctrl, Alt or Meta with any key | anywhere | shortcut: never navigation and never scroll | tre events reference |
| Alt+Space | borderless window | opens the system menu (on by default, [[ADR-0015 System menu default in borderless windows]]) | [[Window]], [[Title Bar]] AC-TTB-18 |
| Alt+Shift+B (proposed) | anywhere in a window with a banner | moves focus to the current banner's first action; proposed default, collision check required | [[ADR-0019 Banner and snackbar focus chords]], [[Banner]] AC-BNR-7 |
| Alt+Shift+N (proposed) | anywhere in a window with a snackbar | moves focus to the current snackbar's action; proposed default, collision check required | [[ADR-0019 Banner and snackbar focus chords]], [[Snackbar]] AC-SNK-9 |
| Ctrl+Shift+Escape (proposed) | focus in a terminal block | moves focus to the next focusable element outside the terminal; reserved before the program receives keys; proposed default, collision check against the shell's shortcut map required | [[ADR-0018 Terminal escape chord]], [[Terminal]] AC-BLK-TRM-3 |

### Tab order rules

1. Order follows visual reading order: top to bottom, then start to end, with columns visited whole in a multi-column layout.
2. A toolbar, tab list, radio group, tree, list, menu and the rows of a table are one stop each.
3. Toolbar, side navigation and primary content are visited in that order; the panes of a window are also reachable by F6.
4. Tab from outside a composite widget focuses the item last focused in it, else the selected item, else the first enabled item (AC-TRE-02, AC-LST-02). Shift+Tab returns to the same item.
5. A control created or revealed after the window opens joins the order at its layout position. Removing the focused control moves focus to the next control in order, or to the container when there is none ([[Tree]] AC-TRE-14 sets the case of a branch).

### F6 pane cycling

The config app is the reference: F6 moves focus to the next area in the order Files, Structure, Editor, View, Properties, Problems (Problems when it lists something; owner decision for the docked layout, 2026-11-27, [[Config App Layout]]; the previous order was Files, Structure, Form, Text, Problems); Shift+F6 moves to the previous one; the keys wrap (`tess-ui:apps/shell_config/README.md`; `REGIONS` in `tess-ui:apps/shell_config/src/tess_shell_config/shortcuts.py`). F6 is the way out of the text editor, which takes Tab for itself.

Rules:

- A window with two or more panes (regions of [[Panel and Surface]] that hold focusable content) defines an ordered list of panes. The order equals visual order (start to end, top to bottom) unless the application documents another.
- F6 moves to the next pane; Shift+F6 to the previous; both wrap.
- Focus lands on the control last focused in that pane, else on its first focusable control. A pane that is hidden, empty of focusable controls or collapsed to a rail is skipped; a pane that appears (Problems with findings) joins the cycle.
- Each pane has a name that assistive technology reads when focus enters ([[14 Accessibility Basics]]); the name is not the only cue, so the pane also shows a focus change in the ring of the control it contains.
- F6 works from any control, including controls that take Tab (multi-line text fields) and a focused tree or list. A modal layer owns its own focus scope: F6 does nothing inside a dialog.
- F6 is reserved: an application binds no other action to it.
- In a window with a single pane, F6 does nothing.

A shell surface set (Bar, Panel, Frame) uses the shell's own focus-walking actions (`Next_Focus`, `Previous_Focus` in shortcut mode, `tess-shell:docs/guide/keyboard.md`); F6 across shell surfaces is not specified.

### Escape rule order

Escape closes one thing per press and does nothing else: it never leaves the window, quits, blurs the focus or clears a selection. The press goes to the first of these that exists:

1. A drag in progress: the drag is cancelled and the dragged item returns to its origin (below).
2. An IME composition in progress in a text field: the composition is cancelled.
3. A visible tooltip.
4. The innermost open level of a menu or popup chain (a submenu before its parent), with focus returning to the parent item ([[Menu]] AC-MEN-11).
5. A control's own transient state that it documents (an open list or picker of the focused control is a popup and falls under 4; an inline edit with an uncommitted value reverts only where [[Text Field]] says so).
6. The topmost dismissible dialog; an alert dialog ignores Escape ([[Dialog]] AC-DLG-8).

Where nothing exists, Escape is not consumed and passes up to the application. After a close, focus returns to the opener with its focus-visible state preserved ([[12 Overlays]], Focus; AC-OVL-5).

### Enter and Space

| Control | Enter | Space |
|---|---|---|
| Button, Icon Button, link, menu item, tab | activates once | activates once (menu item and button) |
| Switch, Checkbox | does nothing | toggles once |
| Radio button | does nothing | chooses |
| List row, tree row | activates (opens, runs the default action) | chooses (selection); in a multi-select list toggles |
| Tree branch | chooses and toggles ([[Tree]] AC-TRE-07) | chooses, does not toggle |
| Accordion header | toggles | toggles |
| Text field, single line | commits the value (submit) | types a space |
| Text field, multi-line | inserts a newline | types a space |
| Disabled control | nothing | nothing |

A key held down does not repeat an activation or a toggle: one press of the key makes one action (tess-shell Toggle rule, `tess-shell:docs/guide/keyboard.md`). The pressed state shows while the key is held ([[State Layers]]).

### Arrow-key groups and roving focus

A group is a set of related items that are one Tab stop. Roving focus is the technique of the WAI-ARIA Authoring Practices roving tabindex ([APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/)): exactly one item of the group is in the Tab order, the others are reachable by arrow keys; tess-ui expresses it with `Focus_Group: vertical` or `horizontal`.

| Rule | Value |
|---|---|
| Orientation | vertical groups use Up and Down; horizontal groups use Left and Right; the other pair does nothing, so it can scroll the container |
| Home, End | first and last enabled item |
| Page Up, Page Down | (viewport minus 10 percent) divided by row height, rounded down (list, tree, menu with scrolling) |
| Wrap | menus, radio groups, toolbars and tab lists wrap at the ends; lists, trees and tables do not; a component note may state otherwise |
| Disabled items | skipped by arrows, Home, End and typeahead |
| Right-to-left | horizontal arrows mirror |
| Arrows and selection | arrows move focus and do not change the chosen item; choosing is Space or Enter. A single-choice group where focus equals choice (radio group, tabs with automatic activation, the shell List) states so in its note |
| Entering the group | the last focused, else the selected, else the first enabled item |

### Typeahead

- Applies in list, tree, menu and other roving groups when focus is not in a text input.
- A printable character focuses the next enabled item whose accessible label starts with the typed text, case-insensitive, starting after the focused item and wrapping.
- The same character typed again cycles through items that start with it. Several characters typed within the buffer time form one prefix.
- The buffer is cleared after 1 s with no key ([[Tree]] AC-TRE-06, [[List]] AC-LST-04, the shell List). No match: focus does not move and nothing is announced.
- [[Menu]] AC-MEN-9 states a 500 ms window; this conflicts with the 1 s above (conflict recorded in the audit of [[17 Conformance]] until the Menu note is aligned).
- Typeahead never activates an item.

### Shortcuts and conflicts

1. A shortcut is a modifier plus one key (or a function key). A single printable character without a modifier is never a shortcut unless the user can turn it off or remap it (WCAG 2.2 SC 2.1.4 Character Key Shortcuts).
2. Delivery order for a key press: the focused control (text editing keys, arrows in a list); an open overlay; the pane's own shortcuts; the application's shortcuts; global shortcuts of the shell or the desktop. The first that takes the key stops it.
3. A key held with Ctrl, Alt or Meta belongs to the application, not to a widget, except the Ctrl keys a text field takes itself (select all, copy, cut, paste, word movement) (`tess-ui:docs/guide/view-language.md`, Focus; `tre:docs/reference/events.md`).
4. The desktop wins conflicts: a key the desktop already owns is not taken; the action is registered with no key and one warning is logged (`tess-shell:docs/guide/keyboard.md`, "The desktop wins").
5. Within one scope no two actions share a key. When they do, both lose it and one warning names both (tess-shell rule), and a test of the shortcut table fails.
6. The Tesserae shortcut vocabulary (design choice, from the config app): Ctrl+S save, Ctrl+Z undo, Ctrl+Y and Ctrl+Shift+Z redo, Ctrl+N new, F2 rename, F5 refresh or run check, Delete remove, Alt+Up and Alt+Down move an item, Ctrl+Shift+letter for application actions that have no common key. Other actions use the same keys with the same meaning in every Tesserae application #needs-verification-as-design-choice.
7. Every shortcut is shown where its action is shown: in a menu item's shortcut text, and in the tooltip or accessible description of its control (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` puts the key in the label, for example "Add a child block (Ctrl+Shift+N)"; `shell-vault:40 Specifications/Integration/Global Shortcuts.md` shows keys in tooltips). Key names are written with `+` and capitalised: `Ctrl+Shift+N`.
8. Ctrl on Linux and Windows is Cmd on macOS #needs-verification-as-design-choice.
9. Global shortcuts of the shell work while no shell surface has focus and are registered with the desktop's shortcut service, so the user changes them in System Settings; the file gives only a default (`tess-shell:docs/guide/keyboard.md`).
10. Chords marked proposed in the global keyboard map (Alt+Shift+B, Alt+Shift+N, Ctrl+Shift+Escape) are defaults, not rules: before a project adopts one it checks it against the shell's shortcut map, the desktop's own keys and each application's map (rules 4 and 5 above and AC-INT-13) and records the result and any replacement chord ([[ADR-0018 Terminal escape chord]], [[ADR-0019 Banner and snackbar focus chords]]). A terminal block keeps one escape chord whatever the project chooses.

## Pointer

### Press, click and cancel

- A primary press on an enabled control starts a press (pressed state layer, ripple); the click fires when the release lands on the same control. A release elsewhere cancels with no handler call (tre: `click` only if `pointer_up` is on the same node).
- A press on a disabled control is taken and does nothing; a clickable card behind it does not fire ([[Accessibility Rules]] AR-7).
- Clickable nodes nest innermost first: a button in a clickable card or a checkbox in a clickable row runs only its own handler (`tess-ui:docs/guide/interaction.md`).
- Middle and side buttons make no click in the engine (`tre:docs/guide/events-and-input.md`); the specification gives them no action.
- Text is never the target of a press: a press on a button's label lands on the button.
- Scroll wheel: one notch moves 40 dp, Shift plus wheel scrolls horizontally, and a wheel over an inner container at its end scrolls the outer one ([[Scrollbar and Scroll Container]] AC-SCB-11).

### Hover versus focus

| Aspect | Hover | Keyboard focus |
|---|---|---|
| State layer | 8 percent of the content colour ([[State Layers]]) | 10 percent ([[ADR-0013 Focus and pressed state layer 10 percent]]) |
| Combined | focus wins: one layer shows, 10 percent, not 18 ([[State Layers]] AC-STL-4) | |
| Ring | none | 3 dp, offset 2 dp, `secondary`, keyboard focus only ([[Focus Ring]]) |
| Tooltip | after 500 ms, one at a time | immediately ([[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]) |
| Content | adds no information that focus lacks | everything hover shows is also shown on focus |
| Disabled | no effect | cannot be focused |
| Touch | none exists; tap is a click | not applicable |

A change on hover never moves other content (principle 6). Hover that reveals a control (a row action) is allowed only when the same control is reachable by Tab and appears on focus of the row or its controls.

### Double click

- Two primary presses on the same control within 400 ms and within 4 dp form a double click (tess-ui `DOUBLE_CLICK` 0.4 s in `tess-ui:src/tess_ui/composed.py`; the 4 dp slop is a design choice #needs-verification-as-design-choice). tre has no double-click event for the pointer; touch has `tap` with `count` 2 (`tre:docs/reference/events.md`). The platform double-click interval may replace 400 ms where the engine exposes it #needs-verification.
- The first click does what a single click does (select, focus); the second adds an accelerator: open, edit or rename the item, expand a splitter pane that is `collapsible`, select the word in text. A double click is never the only way to do the action; a keyboard key does the same (Enter to open, F2 to rename).
- In a text field a double click selects the word under the pointer and a triple click the line or string (tre 0.6.7).

### Context menu

- Triggers: secondary click (pointer), the Menu key and Shift+F10 (keyboard; Shift+F10 is the APG key for the context menu on Windows and Linux), long press (touch).
- A context menu is a [[Menu]] opened as a [[Popup]]. From the pointer it opens at the pointer position; from the keyboard it opens at the focused item (the start edge of its bottom edge), with the first enabled item highlighted.
- Selection first: a secondary click on an unselected row selects it before the menu opens; on a selected row in a multi-selection the selection stays.
- The menu contains every action also available by button or shortcut for that item, each with its shortcut text. An item with no context menu ignores all three triggers (nothing opens).
- Escape closes it and returns focus to the item that held it ([[12 Overlays]]).
- A shell surface may also own a context menu opened by secondary click (tray menu).

### Cursor shapes

tre sets the pointer shape per node and descendants inherit it (`tre:docs/reference/node.md`). Material Design 3 does not define cursors; these are Tesserae choices #needs-verification-as-design-choice, matching what tess-ui controls set (`cursor="pointer"` enabled, `"default"` disabled, `tess-ui:src/tess_ui/controls.py`).

| Situation | Shape |
|---|---|
| Button, Icon Button, Switch, Checkbox, Radio, Slider handle, Chip, tab, link | `pointer` |
| Disabled control | `default` |
| List, tree, menu and table rows | `default` |
| Text field, selectable text | `text` |
| Draggable handle at rest, while dragging | `grab`, `grabbing` |
| Splitter vertical divider, horizontal divider | `col_resize`, `row_resize` |
| Window or panel edge resize | `ew_resize`, `ns_resize`, `nesw_resize`, `nwse_resize` |
| Drop target that refuses the dragged data | `not_allowed` |
| Work that blocks input, work in the background | `wait`, `progress` |

### Drag and drop overview

- A drag begins when the pointer moves 4 dp from the press point with the primary button down (design choice) on an item that declares itself draggable; below 4 dp the gesture is a click. The press point and the thing that moves are the same node; pointer capture keeps events coming after the pointer leaves it (`tre:docs/guide/events-and-input.md`).
- Every drag has a keyboard equivalent that reaches the same result (WCAG 2.2 SC 2.5.7 Dragging Movements): moving a block with Alt+Up and Alt+Down and "Move to" (config app), arrows on a splitter ([[Scrollbar and Scroll Container]] rules apply to scroll).
- Feedback while dragging: cursor `grabbing`; the dragged state layer 16 percent ([[State Layers]]); a drop target that accepts shows its highlight, one that refuses shows `not_allowed`.
- Escape cancels a drag (Escape order, step 1). A drop outside any target cancels.
- Files dragged from the operating system arrive as `file_hover`, `file_drop`, `file_hover_cancel` to the node under the pointer; this works on Windows, macOS and X11 and not on Wayland (`tre:docs/guide/events-and-input.md`). An application that takes file drops also offers an Open action by keyboard.
- Details per element (list reorder, dock panels, node graph) live in the component notes ([[Splitter]], [[Dock Panel]], [[Node Graph]]) and the pattern [[Drag and Drop]].

### Selection rules overview

| Model | Pointer | Keyboard |
|---|---|---|
| Single choice | click chooses; the chosen item stays chosen when clicked again | arrows move focus; Space or Enter chooses |
| Multiple choice | click chooses only that item; Ctrl+click toggles; Shift+click extends from the anchor | Space toggles; Shift+Up and Shift+Down extend; Ctrl+Up and Ctrl+Down move focus without changing the choice; Ctrl+A chooses all #needs-verification-as-design-choice |
| Text | drag selects; double click a word; triple click a line | Shift+arrows, Ctrl+Shift+arrows by word, Ctrl+A |
| Activation versus selection | double click or Enter activates (opens) | Enter activates; selection never opens |

A selection is shown by `secondary_container` or the state layer of the component and by a non-colour cue (mark or position) ([[14 Accessibility Basics]] AC-A11Y-16). The chosen item and the focused item are separate; the focus ring marks focus ([[Tree]] AC-TRE-07).

## Touch

- A touch context uses 48 dp hit areas ([[ADR-0002 Desktop density levels and target sizes]]).
- A tap is a click: the first finger is also the pointer and hovers what it is over while down. A tap with `count` 2 is a double tap.
- A long press is a touch held in place for 500 ms (tre `long_press`: half a second). It opens the context menu of the item, or the tooltip of an icon-only control where the control has no other long-press meaning (`tess-ui:src/tess_ui/composed.py` shows a tooltip on `long_press`). The finger may move at most 10 px (tre `touch_slop`) before the gesture becomes a pan and the long press is cancelled.
- Pan scrolls the scroll view or virtual list under the finger, content following the finger; a flick faster than about 150 px/s coasts to rest; there is no overscroll bounce (`tre:docs/guide/events-and-input.md`).
- Swipe (600 px/s or more after 40 px) and pinch are for the application's own surfaces (canvas, node graph); they never carry the only path to an action (WCAG 2.2 SC 2.5.1 Pointer Gestures: single-pointer alternative exists).
- A touch within `touch_target_slop` of a control counts as on it when set; the default is 0 and a touch UI sets 10 px (design choice #needs-verification-as-design-choice).
- Tooltips are not shown by tap; hover content has a tap equivalent in the visible label ([[ADR-0004 Tooltip rule]]).
- The engine's touch handling was written and tested with simulated touches, not on a touch screen (`tre:docs/guide/events-and-input.md`); touch rows are scripted tests and hand checks on a touch device.

## Click outside and focus return

Rules in one place, owned by [[12 Overlays]]:

| Case | Rule |
|---|---|
| Press outside a popup, menu | closes it; the press is consumed and does not reach the element beneath nor reactivate the opener |
| Press on the scrim | closes a dismissible dialog; an alert dialog stays |
| Press inside an overlay | never closes the overlays beneath |
| Press on the opener while its overlay is open | toggles (closes, does not reopen) |
| Close by Escape, outside press, activation | focus returns to the opener with its focus-visible state; when the opener is gone, to the nearest logical control |
| Text-input overlay (launcher) | a press on a non-focusable area inside keeps the text input focused; the dismiss mechanism holds no keyboard |
| Window loses focus | tooltips and popups close; a dialog stays |

## Input matrices

Rows are test cases: a test drives the input in the given context and compares the result. IDs are used by the acceptance criteria. Counts of handler calls are exact.

### Pointer matrix

| ID | Input | Context | Result |
|---|---|---|---|
| P-1 | press and release on the same control | enabled button | `click` once; pressed layer shows during the press |
| P-2 | press on control, release on another | enabled button | no click |
| P-3 | press and release | disabled control over a clickable card | 0 handlers, the card does not fire |
| P-4 | click | button inside a clickable card | button handler once, card handler 0 |
| P-5 | secondary click | row with a context menu | the row is selected, the menu opens at the pointer |
| P-6 | secondary click | element with no context menu | nothing opens, no click |
| P-7 | two presses within 400 ms and 4 dp | list row | first click selects; second opens (activation); one `open` call |
| P-8 | press, move 3 dp, release | draggable item | a click, no drag |
| P-9 | press, move 5 dp | draggable item | drag begins, cursor `grabbing` |
| P-10 | middle button press | any control | no handler runs |
| P-11 | wheel notch, Shift plus wheel | scroll container | 40 dp vertical, 40 dp horizontal |
| P-12 | pointer enters | enabled control | hover layer 8 percent within 15 ms; tooltip after 500 ms where it has one |
| P-13 | pointer press | button | button focused with no ring; text field focused with its indicator |
| P-14 | press outside | open menu | menu closes, handler beneath 0 |

### Keyboard matrix

| ID | Input | Context | Result |
|---|---|---|---|
| K-1 | Tab x N, then Shift+Tab x N | window of 6 controls and one tree | visits each stop once in visual order; wraps; the tree is one stop |
| K-2 | F6 four times, then Shift+F6 | window of 4 panes | focus enters pane 2, 3, 4, 1, then pane 4 |
| K-3 | F6 | focus in a multi-line text field | focus leaves to the next pane |
| K-4 | Escape | tooltip, menu with open submenu, dialog open together | tooltip closes; then submenu; then menu; then dialog; one per press |
| K-5 | Escape | nothing transient open | not consumed; no state changes |
| K-6 | Enter | focused button | one click; no repeat while held |
| K-7 | Space | focused switch | toggles once; Enter does nothing |
| K-8 | Enter, Space | focused disabled button | nothing, focus cannot reach it |
| K-9 | Down x3, Up x1, End, Home | list of 10 | rows 4, 3, 10, 1; no wrap |
| K-10 | Down at last, Up at first | menu | wraps to first, last |
| K-11 | Right, Left | vertical list | no change of focus; the container scrolls horizontally if it can |
| K-12 | typed "ba" within 1 s, then "x" after 1.5 s | list with Banana, Barley, Xenon | Banana focuses; after the pause "x" focuses Xenon |
| K-13 | Page Down | list 400 dp tall, 40 dp rows | focus moves 9 rows |
| K-14 | Menu key, Shift+F10 | focused row with a context menu | menu opens at the row, first enabled item highlighted |
| K-15 | Ctrl+A, Ctrl+C | focused text field | selects all, copies; no scroll |
| K-16 | Ctrl+Down | focused scroll container | no scroll (shortcut) |
| K-17 | a registered shortcut and a second action with the same key | shortcut table | the check fails: both entries reported |
| K-18 | Space, Shift+Down | multi-select list | toggles the focused row; extends the selection by one |

### Touch matrix

| ID | Input | Context | Result |
|---|---|---|---|
| T-1 | tap | enabled button | one `click` |
| T-2 | two taps close in time and place | list row | `tap` with `count` 2; the double-click action once |
| T-3 | touch held 500 ms in place | row with a context menu | menu opens; no click on lift |
| T-4 | touch held and moved 12 px | row | the long press is cancelled and the content pans |
| T-5 | pan | scroll view | content follows the finger; flick at 400 px/s coasts to rest |
| T-6 | touch lands 8 dp beside a 24 dp button with `touch_target_slop` 10 | touch UI | counts as on the button |
| T-7 | tap | icon-only control | no tooltip; the accessible name still exists |
| T-8 | pinch | canvas | `pinch` with `scale`; a keyboard command does the same zoom |

## Status in code

| Project | Where | Status |
|---|---|---|
| tess-ui | `tess-ui:docs/guide/interaction.md`, `tess-ui:src/tess_ui/interaction.py`, `tess-ui:src/tess_ui/composed.py` (`Focus_Group`, typeahead, splitter double click `DOUBLE_CLICK` 0.4, tooltips on `long_press`), `tess-ui:apps/shell_config/src/tess_shell_config/shortcuts.py` (F6, Shift+F6, shortcuts, Menu key, Shift+F10) | Partly meets. Meets: Enter and Space click, roving groups with Home, End and typeahead, focus ring for keyboard focus only, hover 8 and focus 10 percent layers, innermost-handler rule, disabled controls swallow clicks, `cursor` pointer and default on controls, Escape closes overlays, config app F6 cycle, Menu key and Shift+F10 for the Structure menu. Gaps: F6 is app code in the config app and not a toolkit service; the platform double-click interval is not read; there is no shared shortcut table that fails on duplicates; menu typeahead window differs (500 ms in the Menu note against 1 s); no Page Up and Page Down on a plain list; touch is simulated only. |
| tess-shell | `tess-shell:docs/guide/keyboard.md`, `shell-vault:50 Design System/Standard Modules.md`, `tess-shell:src/tess_shell/surfaces/popup.py` | Partly meets. One Tab stop per interactive module, `Tab_Index` ordering (against "no positive tab indexes"), roving List and Menu, Enter and Space, global shortcuts with desktop-wins and duplicate-key rules, Escape closes a popup in code (OQ-14: not verified on KWin), popup returns focus to the opener. Gaps: no F6; the ring only on blocks that take `Shadows`; no hover state layer; surfaces take the keyboard only when `Keyboard` says so; no context-menu key; touch not exercised. |
| tre | `tre:docs/guide/events-and-input.md`, `tre:docs/reference/events.md`, `tre:docs/reference/node.md` | Mechanisms only, by design: Tab order with `tab_index`, `focus_visible`, `focusable`, Enter and Space as `click`, keyboard scrolling, `cursor` shapes, `capture_pointer`, touch events with long press, pan, swipe, pinch and `touch_slop`, file drag and drop (not on Wayland). No roving group, no typeahead, no F6, no double-click or Shift+F10 or Menu key event, no pane concept. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Keyboard-first model: roving groups, typeahead, F6, Escape order | Material Design describes touch first; desktop use needs a complete key map (principle 1) | [[ADR-0002 Desktop density levels and target sizes]] covers target sizes only; the key map itself has no ADR #needs-verification-as-design-choice |
| Hover layer 8 and focus layer 10 percent with focus winning | Material Web latest tokens; older tokens use 12 | [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Hover grace of 150 ms for all tooltips and tooltip on keyboard focus | WCAG 2.2 SC 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Cursor shapes, double click timing, drag threshold, context menu keys | MD3 specifies none for pointer input | none; design choices |
| Scrollbar hit area 12 dp below 24 dp target | equivalent keyboard scrolling | [[ADR-0012 Scrollbar thumb opacity and hit area exception]] |

## Acceptance criteria

- [ ] AC-INT-1 (scripted input): run the keyboard matrix rows K-1 to K-18 against a project's reference view. Pass: each row's result equals the table; rows whose control the view lacks are recorded "not applicable" with the control named.
- [ ] AC-INT-2 (scripted input): run the pointer matrix rows P-1 to P-14. Pass: each result equals the table; handler counts are exact.
- [ ] AC-INT-3 (scripted input): run the touch matrix rows T-1 to T-8 with simulated touches. Pass: each result equals the table; the audit records "hand check not run" for the touch device.
- [ ] AC-INT-4 (scripted input): in a window of 10 focusable controls including a tree and a list, Tab 12 times. Pass: the visited ids equal the layout order list, each stop once, the tree and the list are one stop each and the 11th Tab wraps to the first.
- [ ] AC-INT-5 (token test): no `tab_index` greater than 0 and no `Tab_Index` greater than 0 appears in the project's views and stylesheets. Pass: a scan finds zero.
- [ ] AC-INT-6 (scripted input): F6 cycle. In a window with panes A, B, C and D (D hidden when empty), F6 from A reaches B, C, A in order; when D gains content it joins after C; Shift+F6 reverses; from a multi-line text field F6 leaves the field. Pass: the focused pane after each key equals the expectation.
- [ ] AC-INT-7 (scripted input): Escape order. Open a dialog, from it a menu with an open submenu, and show a tooltip; press Escape 4 times. Pass: after each press exactly one of tooltip, submenu, menu, dialog has closed, in that order, and focus is the opener after each close.
- [ ] AC-INT-8 (scripted input): with nothing transient open, Escape in a focused control changes no state and is reported as not consumed. Pass: zero state changes, the application's Escape handler is called once.
- [ ] AC-INT-9 (scripted input): Enter and Space. For each control type of the Enter and Space table present in the view, the key result equals the table; a key held for 1 s fires 1 action. Pass: action counts equal.
- [ ] AC-INT-10 (scripted input): roving group. For a list, a tree, a menu and a toolbar: Tab enters on the right item (last focused, else selected, else first), arrows follow the orientation and wrap rule of the roving-group table, Home and End reach the ends, disabled items are skipped. Pass: focused item after each key equals the expectation.
- [ ] AC-INT-11 (scripted input): typeahead. With items Apple, Avocado, Banana, Berry, a disabled Bean: "b" focuses Banana, "b" again Berry, "b" again wraps to Banana; "be" within 1 s focuses Berry and never Bean; after 1.1 s idle "a" focuses Apple. Pass: the sequence is observed.
- [ ] AC-INT-12 (scripted input): a single printable character typed in a focused list does not run an application action. Pass: the application shortcut table contains no entry without a modifier, or the entry has a documented off switch (WCAG 2.2 SC 2.1.4).
- [ ] AC-INT-13 (token test): the shortcut table of the application (all keys registered by the view and the application) has no duplicate key within one scope and every entry has an action name. Pass: duplicates 0.
- [ ] AC-INT-14 (scripted input): every shortcut in the table is shown in the tooltip or accessible description of its control, or in a menu item's shortcut text. Pass: strings are present for 100 percent of entries.
- [ ] AC-INT-15 (scripted input): a key with Ctrl, Alt or Meta held never scrolls a scroll container and never navigates; Ctrl+A, Ctrl+C, Ctrl+X, Ctrl+V act in a focused text field. Pass: scroll offset unchanged, clipboard behaviour as expected.
- [ ] AC-INT-16 (scripted input): pointer cancellation. Press on a button, move the pointer off it, release. Pass: handler calls 0 and the pressed layer is removed within one frame of the release.
- [ ] AC-INT-17 (pixel check): hover and focus. A control under the pointer shows 8 percent of `on_surface`, the same control under keyboard focus shows 10 percent and the ring, and with both holding shows 10 percent. Pass: composited pixels within 1 per 8-bit channel.
- [ ] AC-INT-18 (scripted input): disabled. A disabled control takes no focus (Tab skips it), a press on it runs 0 handlers including those of a clickable ancestor, and it shows `default` cursor. Pass: counts 0.
- [ ] AC-INT-19 (scripted input): double click. Two clicks at 390 ms apart and 3 dp apart run the double-click action once; two clicks at 410 ms apart or 5 dp apart run 0 (fake clock). Pass: action counts equal.
- [ ] AC-INT-20 (scripted input): context menu. A secondary click, the Menu key and Shift+F10 on a focused row each open the same menu for that row, the keyboard ones at the row and the pointer one at the pointer; Escape closes it and focus is the row. Pass: menu node and anchor positions equal the expectation (within 1 dp).
- [ ] AC-INT-21 (scripted input): cursor. The `cursor` property read from each control type in the Cursor shapes table equals the table value, enabled and disabled. Pass: all values equal.
- [ ] AC-INT-22 (scripted input): drag. A press with a 3 dp move is a click; with a 5 dp move it starts a drag with cursor `grabbing`; Escape during the drag restores the origin with 0 drop calls; the same result is reachable by the documented key sequence. Pass: states and counts equal.
- [ ] AC-INT-23 (scripted input): selection. In a multi-select list, click selects one, Ctrl+click toggles, Shift+click extends from the anchor, Space toggles, Shift+Down extends; arrows alone change no selection. Pass: the selected sets equal the expectation.
- [ ] AC-INT-24 (scripted input): touch. A touch held 500 ms in place opens the context menu with no click on lift; moved 12 px it pans and opens nothing. Pass: events observed.
- [ ] AC-INT-25 (review): every element note's Behaviour section states its keys, and every key is consistent with the global keyboard map. Pass: a reviewer finds zero contradictions; the Menu typeahead window is listed as an open conflict until aligned.
- [ ] AC-INT-26 (review): no action or information is available only on hover, only by double click, only by drag or only by a gesture. Pass: reviewer list empty for each documented view.
- [ ] AC-INT-27 (review): each chord marked proposed in the global keyboard map has a recorded collision check (shell shortcut map, desktop keys, application map) with the result, or a recorded replacement chord; a terminal block has exactly one reserved escape chord that is not delivered to its program. Pass: record present for 3 of 3 chords; zero unrecorded collisions.

## Sources

- Config app key map and F6 order: `tess-ui:apps/shell_config/README.md`, `tess-ui:apps/shell_config/src/tess_shell_config/shortcuts.py`, `tess-ui:docs/guide/shell-config.md`.
- tess-ui interaction: `tess-ui:docs/guide/interaction.md`, `tess-ui:docs/guide/view-language.md` (Focus, Dragging), `tess-ui:src/tess_ui/composed.py`, `tess-ui:src/tess_ui/controls.py`.
- tre input: `tre:docs/guide/events-and-input.md`, `tre:docs/reference/events.md`, `tre:docs/reference/node.md`, `tre:docs/guide/text.md`.
- tess-shell: `tess-shell:docs/guide/keyboard.md`, `shell-vault:50 Design System/Standard Modules.md` (Keyboard Operation), `shell-vault:40 Specifications/Integration/Global Shortcuts.md`.
- WAI-ARIA Authoring Practices keyboard interface (roving tabindex, aria-activedescendant, key table with Shift+F10 for the context menu): `https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/` (verified 2026-11-21).
- WCAG 2.2 success criteria: 2.1.1 Keyboard, 2.1.2 No Keyboard Trap, 2.1.4 Character Key Shortcuts, 2.4.3 Focus Order, 2.4.7 Focus Visible, 2.5.1 Pointer Gestures, 2.5.2 Pointer Cancellation, 2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum), 3.2.1 On Focus (titles checked in `https://www.w3.org/TR/WCAG22/`, 2026-11-21).
- The F6 pane convention outside the config app is not verified against a platform source #needs-verification. Values for double-click slop, drag threshold, cursor choices and the shortcut vocabulary are Tesserae design choices #needs-verification-as-design-choice.
- Material Web focus ring and state layers: see [[Focus Ring]] and [[State Layers]].
