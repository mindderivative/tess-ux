---
title: Active Descendant
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, behaviour, accessibility, engine, tesserae-specific]
related: ["[[Accessibility Tree]]", "[[List]]", "[[List Item]]", "[[Text Field]]", "[[Menu]]", "[[Focus Ring]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[Accessibility Tree]]", "[[14 Accessibility Basics]]"]
---

# Active Descendant

> [!info] Summary
> Active descendant lets a node that keeps the keyboard (a search field) tell assistive technology which row of a list under it is current, while keyboard focus stays on the field. It has no MD3 counterpart; the pattern is the WAI-ARIA `aria-activedescendant` of the [combobox pattern](https://www.w3.org/WAI/ARIA/apg/patterns/combobox/). It is unreleased in the engine (TRE-REQ-023).

## Purpose

Let a user type in a field and move through results with Up and Down while the screen reader reads the current result.

## When to use and not

- Use when: a text field keeps focus and arrows move a selection in a list or menu below it (launcher results, a combobox).
- Do not use when: focus moves to the rows themselves (use real focus and [[List]]); the list has no field above it.

## Anatomy

1. Container node: the field (role `textbox`, later `combobox`) that keeps keyboard focus.
2. Target node: the current row (role `listitem`, a name, `selected` true).
3. Relation: `active_descendant` set on the field; cleared with `None`.
4. Visual current-row mark: the list's selection style, not a focus ring, since focus is on the field.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Result list | launcher | arrows move the current row, Enter activates it |
| Combobox popup | field with options | popup list opened by Down or typing; Escape closes it |
| Fallback | where the platform does not deliver the relation | polite `announce` of the current row's name |

## States

| State | Visual change | Token values |
|---|---|---|
| No current row | field only | none |
| Current row | row shows selected state | `secondary_container` background with state layer per [[List Item]] |
| Target hidden or destroyed | relation drops; reads back `None` | none |

## Tokens used

Selection colours as [[List Item]] ([[Colour Roles]], [[State Layers]]); no new token.

## Sizing and density

Not applicable: rows are [[List Item]] rows at 40, 32, 24 dp ([[Spacing and Density]]).

## Layout and overflow

The current row is scrolled into view by the least distance that shows it when it changes ([[Scrollbar and Scroll Container]]). The engine's automatic scroll follows focus only, and focus does not move, so the widget calls `scroll_into_view()` on the row (rule of the spec, not an engine promise).

## Behaviour

- Keyboard: Up and Down move the current row and set `active_descendant`; at the first or last row they stop or wrap as the owning pattern says (a launcher wraps, a menu does not #needs-verification); Home and End go to the ends; Enter activates the current row; Escape clears the field or closes the list; Tab leaves the field.
- Keyboard focus does not move: `focused` stays true on the field and no focus or unfocus event fires.
- Pointer: hovering a row does not set the relation; a click activates the row.
- Touch: as pointer.

## Tooltip and overlay behaviour

Not applicable: the list is a popup or panel of the owning pattern ([[Popup]], [[Menu]]).

## Motion

Not applicable: the relation changes at once; the row highlight follows [[Motion]] of the list item.

## Accessibility

- Give the row a role (`listitem`) and a name ("Firefox, application") so there is something to read; the field has a name and `controls` pointing to the list.
- How platforms say it: AccessKit moves the focused state from the field to the row, so on Linux a reader sees `StateChanged(focused)` move to the row and back; it sends no `ActiveDescendantChanged`. Use a polite `announce` of the row name as a fallback where a platform does not deliver the relation. Not tried with Orca, NVDA or VoiceOver.
- Target hidden from the tree is left out; one that is destroyed reads back `None`.
- Result count changes are announced politely, once per query, not per keystroke ([[Accessibility Tree]]).

## Dark and light

Not applicable.

## Defaults

`active_descendant` unset (None) on every node.

## Acceptance criteria

- [ ] AC-ADE-1 (AT tree assertion): after `field.set(active_descendant=row)`, the accessibility tree marks the row as the active descendant (or as focused) and `field.get("focused")` stays true.
- [ ] AC-ADE-2 (scripted input): setting `active_descendant` fires no `focus` or `unfocus` event on the field or the row.
- [ ] AC-ADE-3 (scripted input): in a launcher with 10 results, pressing Down three times sets the relation to the fourth row each time in order, and the row is fully inside the viewport after each key.
- [ ] AC-ADE-4 (AT tree assertion): `field.set(active_descendant=None)` returns the tree to the field as the only current node.
- [ ] AC-ADE-5 (AT tree assertion): a hidden target is absent from the update and a destroyed target reads back `None`.
- [ ] AC-ADE-6 (AT tree assertion): the current row has a role and a non-empty name, and the field has `controls` naming the list.
- [ ] AC-ADE-7 (scripted input): where the relation is not delivered, a polite announce of the row name is raised once per change (fallback), and the queue stays at 16 or fewer.
- [ ] AC-ADE-8 (pixel check): the current row shows the selected style and no focus ring; the ring stays on the field.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | none found for `active_descendant` in `tess-ui:src` | absent: fails AC-ADE-1 to 8 |
| tess-shell | `tess-shell:docs/design/60 Quality/Accessibility.md` (Launcher waits for tre), `tess-shell:src/tess_shell/modules/context.py` (`announce`) | absent: no `active_descendant` key; fallback announcements exist (AC-ADE-7 not verified) |
| tre | `tre:docs/guide/accessibility.md` (Active descendant), `tre:crates/engine-core/src/tree/access.rs`, `tre:crates/engine-core/src/access.rs` | partly meets: property on any node, same-window target, hidden target left out; unreleased (TRE-REQ-023); no `ActiveDescendantChanged` on Linux |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Tesserae-specific behaviour (MD3 has none) | search-and-list patterns keep focus in the field | [[ADR-0001 MD3 role names are the specification vocabulary]] |

## Sources

- `tre:docs/guide/accessibility.md` (Active descendant), `tre:crates/engine-core/src/tree/access.rs`.
- WAI-ARIA 1.2 `aria-activedescendant` mapping (read: focus event moves to the referenced element, cleared attribute returns focus to the container): https://www.w3.org/TR/wai-aria-1.2/. APG combobox pattern: https://www.w3.org/WAI/ARIA/apg/patterns/combobox/.
