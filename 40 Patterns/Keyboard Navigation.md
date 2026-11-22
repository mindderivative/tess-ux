---
title: Keyboard Navigation
type: pattern
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [pattern, keyboard, focus, accessibility]
related: ["[[40 Patterns]]", "[[11 Interaction]]", "[[14 Accessibility Basics]]", "[[12 Overlays]]", "[[Focus Ring]]", "[[Selection]]", "[[Drag and Drop Pattern]]", "[[Forms and Settings]]", "[[Notifications]]", "[[Tree]]", "[[List]]", "[[Menu]]", "[[Dialog]]", "[[Popup]]", "[[Accordion]]", "[[Text Field]]", "[[Tooltip]]", "[[Scrollbar and Scroll Container]]", "[[11 Interaction#Shortcuts and conflicts|Global Shortcuts]]", "[[Keyboard Navigation|Shortcut Mode]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Gaps and Contradictions]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0013 Focus and pressed state layer 10 percent]]"]
depends_on: ["[[11 Interaction]]", "[[Focus Ring]]"]
---

# Keyboard Navigation

> [!info] Summary
> The pattern for building a keyboard-complete window: how focus is structured (stops, groups, panes), in what order it moves, what it skips, where it goes when something closes, and how shortcuts are shown. The key tables themselves (global map, Escape order, Enter and Space, arrow groups, typeahead, shortcut rules) live in [[11 Interaction]]; this note decides which structure each part of a window uses and tests it. Tesserae-specific; the references are the [WAI-ARIA APG keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/) and WCAG 2.2.

## Problem

Each project handles focus differently: tess-ui has `Focus_Group` and no pane cycling in the toolkit (F6 exists only in the config app), the shell orders surfaces with positive `Tab_Index` and a shortcut mode, the engine has `tab_index` and no key handling for a `virtual_list`, and `active_descendant` is unreleased ([[Gaps and Contradictions]], summary items 8 and 11 and the tre evidence "Virtual list"). The owner's rule is keyboard first ([[01 Principles and Scope]]).

## Purpose

Make every window operable by keyboard alone with few stops, a predictable order, never a trap, and focus that always lands somewhere sensible.

## When to use and not

- Use when: laying out any window, panel or popup with more than one interactive control.
- Do not use when: a single control stands alone; its keys are in its own note.

## Rules

1. Stops: every interactive control is one Tab stop; a composite (tree, list, menu, toolbar, tab list, radio group, table body) is one stop with arrow keys inside (roving focus, `Focus_Group` in tess-ui). A window of 40 rows of controls inside a list is one stop for the list, not 40 ([[11 Interaction]], Focus model).
2. Order: visual reading order, equal to tree order; no positive `tab_index` and no positive shell `Tab_Index` to reorder controls (AC-INT-5; [[14 Accessibility Basics]]). The shell's `Tab_Index` ordering is a documented departure in the shell (see Deviations) and lowers to layout order when the shell adopts the rule.
3. Panes: a window with two or more panes (tree, form, text, problems) gets F6 and Shift+F6 to cycle panes in a fixed order, wrapping, working from any control including a multi-line text field and a focused tree; a pane that is hidden when empty joins the cycle when it gains content; F6 does nothing in a modal layer and is bound to nothing else (config app: Files, Structure, Form, Text, Problems). Tab still walks every stop inside a pane.
4. Entering a pane or composite: focus goes to the last focused item, else the selected item, else the first enabled item; leaving by Tab goes to the next stop in order, and Shift+Tab to the previous; coming back by F6 restores the same item.
5. Skips: a disabled control, a hidden control, a control with zero size, and the content of a collapsed container (closed accordion or tree branch, `Expander`) take no focus and are passed by Tab, arrows, Home, End and typeahead. A control that is disabled while focused hands focus to the next stop in order the same frame, never to the window. The exception is a hidden shell Bar or Panel: Shortcut Mode shows it and keeps it visible (initial focus stays where the shell's focus rule 4 puts it, `Next_Focus` reaches it), and leaving the mode or Escape hides it again; plain keys do not reveal it ([[ADR-0021 Shortcut Mode reveals a hidden Bar]], [[Auto Hide]]).
6. No trap: Tab always leaves every control; a multi-line text field leaves by Tab unless `tab_navigates` is false, and then documents Escape followed by Tab; a modal layer holds focus inside by design and Escape or an action leaves it ([[12 Overlays]]).
7. Focus return: closing a popup, menu, tooltip-owning overlay or dialog by Escape, activation or outside press returns focus to the opener with its focus-visible state; when the opener is gone, focus goes to the nearest logical control (the next sibling, else the container), never to nothing; deleting the focused row moves focus to the next row, else the previous, else the container; reload of a view keeps focus on a block that still exists ([[11 Interaction]], Click outside and focus return; shell Popup rule).
8. Initial focus: a window focuses the first stop or the one the app names; a dialog focuses its first field, or the safe action (Cancel) for a destructive confirmation; an opened popup with a text field focuses that field ([[Dialog]], [[Popup]]).
9. Visibility: the focus indicator shows for keyboard focus only (never after a pointer press, except text fields), is never covered or clipped, and the focused item scrolls into view by the least distance, with an inset ring where a clipped scroll container would cut the ring ([[Focus Ring]], [[Scrollbar and Scroll Container]], WCAG 2.2 SC 2.4.7, 2.4.11).
10. Reaching everything: every command has a path without a pointer: a control in the Tab order, an arrow-group item, a menu item, or a shortcut. Hover-only information is reachable on focus ([[ADR-0004 Tooltip rule]]); drag has Alt+arrow and a menu ([[Drag and Drop Pattern]]); selection has Space, Shift and Ctrl rules ([[Selection]]).
11. Shortcuts shown: every shortcut appears where its command appears: trailing text in a menu item (right-aligned, never truncated before the label), and in the tooltip or accessible description of its control: "Add a child block (Ctrl+Shift+N)". Key names are written `Ctrl+Shift+N`, capitalised, joined by `+`. A shortcut list is available from a menu or a Help action ([[11 Interaction]], Shortcuts and conflicts).
12. Shortcuts never collide: one action per key within a scope; a key with Ctrl, Alt or Meta is never navigation or scroll; no single-character shortcut without a modifier unless it can be turned off; the desktop wins conflicts ([[11 Interaction#Shortcuts and conflicts|Global Shortcuts]]).
13. Windows of the shell: a surface that takes the keyboard declares it (`Keyboard: ON_DEMAND`; `EXCLUSIVE` only while a mode shows); shortcut mode walks surfaces with `Next_Focus` and `Previous_Focus` and Escape leaves it with focus returning to the window that had it ([[Keyboard Navigation|Shortcut Mode]]). Shortcut Mode also ends when the keyboard goes to another window: the shell ends it 300 ms after its last surface has lost the keyboard to another client (a move from one shell surface to another does not end it), because the keys of the mode (Escape, F6, the arrows) then reach that other window and the user cannot leave the mode by keyboard. There is a way out regardless of keyboard focus: the command `tesserae-shell leave-shortcut-mode`. The mode has no timeout. Found by the owner on a real KWin, 2026-11-22: Escape did nothing because another window held the keyboard, and F6 went to Chrome.
14. Announcements: focus moves are announced by the platform from role, name and state; the app adds polite announcements only where the engine cannot move focus (a text field with a result list uses `active_descendant` where released, else a polite announce of the row, [[14 Accessibility Basics]]).
15. Time: no key action depends on a timing other than typeahead (1 s buffer), type-ahead is never an action, and a held key repeats navigation but never repeats an activation or toggle ([[11 Interaction]]).

## Decision table

| Part of a window | Structure | Tab stops | Inside keys | Cross-pane |
|---|---|---|---|---|
| Toolbar | `Focus_Group: horizontal` | 1 | Left, Right, Home, End; wraps | Tab |
| Tree, list, table | roving group | 1 | arrows, Home, End, Page, typeahead; no wrap | F6 |
| Menu, menu bar | roving group in a popup | 1 | arrows; wraps; Right opens, Left closes submenu | Escape returns to opener |
| Tab list | `Focus_Group: horizontal` | 1 | arrows; Space or Enter activates (manual) or follows focus (automatic, stated) | Tab into panel |
| Radio group | roving group | 1 | arrows move focus and choice together | Tab |
| Form | rows in layout order | 1 per control, plus 1 per enabled reset | Tab | F6 to other panes |
| Accordion | each header a stop, or a group | 1 per header | Enter, Space toggle | Tab |
| Dialog | modal scope | its controls | Tab wraps inside | none; focus returns on close |
| Text field, single line | field | 1 | editing keys; Tab leaves | Tab |
| Text editor, multi line | field | 1 | Tab leaves unless `tab_navigates` is false | F6 leaves always |
| Banner, snackbar | group | 1 per action while shown | Enter, Space | F6 reaches it |
| Shell surfaces | per-surface order, shortcut mode | per surface | `Next_Focus`, `Previous_Focus` | shortcut mode keys |
| Virtual list | roving group over data rows | 1 | needs engine key support ([[UXREQ-002 Virtual list keys and scroll to index]]) | F6 |

## Examples (short snippets only)

```tdl
Container { Focus_Group: horizontal, Children { Button { Label: Save } Button { Label: Undo } } }
```

```text
Config app: Tab (stops)  F6 / Shift+F6 (panes: Files, Structure, Form, Text, Problems)
            Ctrl+Shift+N "Add a child block (Ctrl+Shift+N)"   Menu key / Shift+F10  context menu
```

## States

| State | Visual change | Token values |
|---|---|---|
| Focused (keyboard) | ring 3 dp wide, 2 dp offset, role `secondary`, state layer 10 percent | [[Focus Ring]], [[ADR-0013 Focus and pressed state layer 10 percent]] |
| Focused (pointer) | no ring | [[11 Interaction]] |
| Focused item in an unfocused group | roving item marked as the group's entry; no ring | [[Focus Ring]] |
| Pane cycled by F6 | ring on the entry item; the pane heading may show a 2 dp `primary` underline (design choice) | [[Colour Roles]] |
| Disabled | not focusable | [[State Layers]] |

## Sizing and density

Focus ring dimensions do not change with density ([[Focus Ring]]); a ring on a control at dense (28 dp) fits inside the 2 dp gap between rows of the form at that density (`space.1`). Hit areas for pointer follow 24 dp ([[Spacing and Density]]).

## Accessibility

- Role, name and state of every stop per [[Accessibility Rules]]; the label is not a stop.
- Roving groups expose one tab stop and the group role (`toolbar`, `tablist`, `radiogroup`, `tree`, `listbox`, `menu`).
- `focus_visible` distinguishes keyboard from pointer focus (tre `focus` event).
- A keyboard user reaches everything a pointer user can: WCAG 2.2 SC 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11, 3.2.1.

## Acceptance criteria

These criteria test the structure of a window; the key tables of [[11 Interaction]] (AC-INT-1 to AC-INT-26) test each key.

- [ ] AC-KBN-1 (scripted input): in a window with a toolbar, a tree, a list, a form of 6 controls and a text editor, Tab visits exactly one stop for the toolbar, one for the tree, one for the list, 6 for the form and one for the editor, in layout order, then wraps; Shift+Tab reverses. Pass: visited ids equal the layout list.
- [ ] AC-KBN-2 (token test): no `tab_index` or `Tab_Index` above 0 appears in the project's views, stylesheets and shell files. Pass: scan finds zero.
- [ ] AC-KBN-3 (scripted input): F6 cycles the panes in the stated order and wraps; Shift+F6 reverses; F6 works from a multi-line text field and a focused tree; F6 does nothing while a dialog is open; a pane hidden when empty joins the cycle when filled. Pass: focus owners equal.
- [ ] AC-KBN-4 (scripted input): Tab from outside a composite focuses its last focused item, else its selected item, else its first enabled item; F6 back to a pane restores the same item. Pass: focus owners equal.
- [ ] AC-KBN-5 (scripted input): a disabled control, a hidden control and children of a collapsed accordion, tree branch or `Expander` are never focused by Tab, Shift+Tab, arrows, Home, End or typeahead; disabling the focused control moves focus to the next stop within one frame. Pass: visited set excludes them; focus owner equals.
- [ ] AC-KBN-6 (scripted input): no trap: from every control of a reference view, Tab sequences of 50 presses return to the start; in a multi-line field with `tab_navigates` false, Escape then Tab leaves. Pass: the start control is reached.
- [ ] AC-KBN-7 (scripted input): focus return. For a menu, a popup, a dialog and a dropdown closed by Escape, by activation and by outside press, focus equals the opener afterwards with focus-visible true after a keyboard open; with the opener removed, focus equals the next sibling or the container, never nothing. Pass: focus owners equal in all 12 cases.
- [ ] AC-KBN-8 (scripted input): deleting the focused row of a list by key moves focus to the next row, else the previous, else the container. Pass: focus owners equal.
- [ ] AC-KBN-9 (scripted input): initial focus of a window is the first stop or the named control; a destructive confirmation dialog starts on Cancel; a popup with a text field starts on the field. Pass: focus owners equal.
- [ ] AC-KBN-10 (pixel check): under keyboard focus each stop shows the ring (3 dp, 2 dp offset, `secondary`); after a pointer press no ring shows except in text fields; the ring is visible when the focused control is at the edge of a scroll container (inset ring). Pass: ring pixels present or absent as stated, none clipped.
- [ ] AC-KBN-11 (geometry check): a focused item outside the viewport scrolls into view by the least distance (the item fits entirely, offset at most one row beyond needed). Pass: item bounds inside the viewport; scroll delta minimal.
- [ ] AC-KBN-12 (scripted input): every action of each documented view is performed by key events only. Pass: every action's effect observed (AC-A11Y-4).
- [ ] AC-KBN-13 (scripted input): every shortcut of the application table is present in a menu item's shortcut text or in the tooltip or description of its control, written in the `Ctrl+Shift+N` form, and the table has no duplicate key in one scope. Pass: strings present for 100 percent; zero duplicates.
- [ ] AC-KBN-14 (scripted input): a key with Ctrl, Alt or Meta does not scroll a container or move focus; a printable character in a focused list never runs an application action. Pass: scroll offsets and handler counts equal.
- [ ] AC-KBN-15 (scripted input): a key held for 1 s on a button, switch or checkbox fires one action; held arrows in a list repeat navigation. Pass: activation counts and focus moves equal.
- [ ] AC-KBN-16 (AT tree assertion): each roving group exposes the group role, one stop and the item roles, and the focused item is exposed as focused (or as `active_descendant` where released). Pass: roles and flags equal.
- [ ] AC-KBN-17 (scripted input): in the shell, a surface with `Keyboard: NONE` takes no key; `ON_DEMAND` takes keys after a click; shortcut mode walks surfaces in order with `Next_Focus` and `Previous_Focus`, and Escape leaves it with focus on the previous window (the other ways out are AC-KBN-18 and AC-KBN-19). Pass: key delivery and focus owners equal (hand check on a real compositor, recorded as "not automated").
- [ ] AC-KBN-18 (scripted input): with the shell in Shortcut Mode, a second client takes the keyboard: the mode is off within 1 s (300 ms plus one frame, with a second of margin), the revealed Bar or Panel hides again per its delay, and Escape and F6 are no longer consumed by the shell. A move of the keyboard from one shell surface to another does not end the mode. Pass: mode state off at 1 s in the first case, on in the second. Hand check on a real compositor, recorded as "not automated" where the compositor cannot be scripted.
- [ ] AC-KBN-19 (scripted input): with the shell in Shortcut Mode and the keyboard held by another window, running `tesserae-shell leave-shortcut-mode` ends the mode within 1 s whatever holds the keyboard; the mode never ends by timeout (after 10 minutes with the keyboard on a shell surface it is still on). Pass: states as stated.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:docs/guide/interaction.md`, `tess-ui:docs/guide/view-language.md` (`Focus_Group`), `tess-ui:src/tess_ui/composed.py` (roving, typeahead), `tess-ui:apps/shell_config/README.md` (keys table, F6) | partly meets: `Focus_Group` makes toolbars, tabs, menus, radio sets and lists one stop (AC-KBN-1, AC-KBN-16 by reading); disabled controls skipped (AC-KBN-5 partly); shortcut text in labels in the config app (AC-KBN-13 partly); F6 cycling only in the config app, not a toolkit feature (AC-KBN-3 app level); Dialog default-action focus not built (AC-KBN-9 fails); no scan for positive `tab_index` (AC-KBN-2 unmeasured); ring not shown for plain nodes except `Rect` and `Container` ("Not yet covered"; AC-KBN-10 partly) |
| tess-shell | `tess-shell:docs/guide/keyboard.md`, `tess-shell:src/tess_shell/binder/focus.py`, `tess-shell:src/tess_shell/surfaces/focus.py`, `tess-shell:src/tess_shell/surfaces/popup.py`, `shell-vault:40 Specifications/Integration/Focus and Keyboard.md` | partly meets: interactive modules are one stop, List and Menu take arrows, closed `Expander` and disabled blocks skipped, Popup returns focus to opener, reload keeps focus, shortcut mode and `Next_Focus` (AC-KBN-1, AC-KBN-5, AC-KBN-7, AC-KBN-17 by reading); `Tab_Index` positive ordering is the documented model (AC-KBN-2 fails); no F6 (AC-KBN-3 absent for the shell); focus return on KWin not verified (OQ-14); the ring shows only on blocks that take `Shadows` (AC-KBN-10 partly) |
| tre | `tre:docs/guide/events-and-input.md` (`tab_index`, `focus_visible`), `tre:docs/guide/accessibility.md` (`active_descendant`), `tre:docs/guide/nodes-and-layout.md` | not applicable as engine: tab order by tree order with `tab_index`, `focus_visible`, no pane, group or shortcut concept; `virtual_list` has no keys; `active_descendant` unreleased; Ctrl, Alt or Meta keys are not navigation |

Request candidates: a toolkit F6 pane cycle (a `Pane` marker on a view) in tess-ui; virtual list keys ([[UXREQ-002 Virtual list keys and scroll to index]]); a scan test for positive tab indexes; routed through the Orchestrator.

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| F6 pane cycling and a Tab-stop-per-composite model | MD3 is touch-first and gives no desktop keyboard model | none; desktop keyboard-first ([[01 Principles and Scope]]) |
| Shell `Tab_Index` positive ordering kept until the shell adopts layout order | the shell orders surfaces across windows, which layout order cannot express | none; recorded for the audit |
| Shortcut text in tooltips and menu items | desktop discoverability | [[ADR-0004 Tooltip rule]] |

## Sources

- [WAI-ARIA APG: Developing a keyboard interface](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/): composite widgets as one tab stop with roving `tabindex` or `aria-activedescendant`; authors "strongly advised not to use tabindex" values above 0 for order. Verified 2026-11-21.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): SC 2.1.1 Keyboard, 2.1.2 No Keyboard Trap, 2.1.4 Character Key Shortcuts, 2.4.3 Focus Order, 2.4.7 Focus Visible, 2.4.11 Focus Not Obscured (Minimum), 3.2.1 On Focus.
- [Material Web menu docs](https://github.com/material-components/material-web/blob/main/docs/components/menu.md) for trailing shortcut text in menu items #needs-verification (trailing supporting text token not confirmed in `_md-comp-menu-item.scss`; see [[Menu]]).
- F6 as a pane-cycling key is a Windows and Linux desktop convention; it is not in the APG #needs-verification.
- Code: `tess-ui:apps/shell_config/README.md`; `tess-shell:docs/guide/keyboard.md`; `tre:docs/guide/events-and-input.md`; [[Gaps and Contradictions]]; table of keys and rules: [[11 Interaction]].
