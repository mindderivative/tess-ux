---
title: Accessibility Tree
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, foundation, accessibility, engine]
related: ["[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Active Descendant]]", "[[Text Selection]]", "[[Layer Window]]", "[[Popup Window]]", "[[Application Window]]", "[[Scrollbar and Scroll Container]]", "[[Tooltip]]", "[[Focus Ring]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[14 Accessibility Basics]]", "[[Accessibility Rules]]"]
aliases: ["Accessibility tree (AccessKit)"]
---

# Accessibility Tree

> [!info] Summary
> Every frame the engine builds an accessibility tree (AccessKit) from the node tree and gives it to the platform's screen reader. This note states what the specification requires of every node that appears in it: role, name, state, value, relations, live region and the window announce queue. The rules for people are in [[14 Accessibility Basics]] and [[Accessibility Rules]]; this note is the contract between those rules and the engine. MD3 states [accessibility foundations](https://m3.material.io/foundations/accessible-design/overview) without an engine contract.

## Purpose

Make every Tesserae element readable and operable through assistive technology, with names, roles, states and announcements that the spec can test without a screen reader.

## When to use and not

- Use when: any node is interactive, informative or a live status.
- Do not use when: a node is decorative: hide it (`a11y_hidden`), do not give it a role.

## Anatomy

1. Node: role, label (name), description, value (text or number with min, max, step, value text), states (`checked`, `selected`, `expanded`, `pressed`, `disabled`, `invalid`, `busy`, `current`), `level`.
2. Relations: `describedby`, `controls`, `active_descendant` ([[Active Descendant]]).
3. Actions: focus, activate (as `click`), increment, decrement, set value, expand, collapse, scroll into view.
4. Live region: `live` polite or assertive on a node.
5. Announce queue: per window, `announce(text, politeness)`.
6. Text container: a selectable or linked text node exposes runs, selection and link children ([[Text Selection]]).
7. Bounds in window coordinates, including scroll shift and transforms.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Interactive node | controls | role, name, state, focusable |
| Informative node | status text, images with `Label` | name, no focus |
| Live region | snackbar message, error | `live` set; announced when its name changes or it enters the tree |
| Window announcement | events with no node | `announce`, one per accessibility update |
| Hidden node | decoration | `a11y_hidden` or `visible: false` |

## States

State flags are set by the control, never by the author (shell keys `Checked`, `Selected`, `Expanded` are written by the block that has them).

| State | Tree effect | Notes |
|---|---|---|
| Focused | focus follows keyboard focus; `focus_visible` true for keyboard and AT | [[Focus Ring]] |
| Disabled | announced disabled; does not stop focus, clicks or keys | the control must stop them itself (AR-7) |
| Hidden by `visible: false` | removed from tree, tab order and hit testing | no layout space |
| Hidden by `a11y_hidden` | removed from tree only; stays on screen and in tab order | do not hide a focusable node |
| Busy | `busy` flag | loading states |

## Tokens used

None: the tree carries no colour. Contrast and target tokens are in [[Colour Roles]] and [[Spacing and Density]].

## Sizing and density

Not applicable: nodes report bounds in window pixels; target size rules are in [[14 Accessibility Basics]] and checked by geometry, not by the tree.

## Dimensions and defaults

The tree is data, not a painted part: it carries bounds, role, name and state and no sizes of its own. The only dimensions it must report are the target sizes of the nodes it exposes, which geometry tests check ([[14 Accessibility Basics]]). The three level columns repeat one value.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| tree | height | - | N/A: the tree has no geometry; each node reports the bounds of the node it describes | N/A: same as the Default column | N/A: same as the Default column | [[Accessibility Tree#Sizing and density]] | tess-ui: n/a: the tree is data with no geometry; tess-shell: n/a: the tree is data with no geometry; tre: n/a: the tree is data with no geometry |
| interactive node bounds | min width | - | 24 | 24 | 24 | [[Spacing and Density]] (24 dp pointer minimum, WCAG 2.2 SC 2.5.8) | tess-ui: yes (style min_width on the node); tess-shell: yes (Min_Width on the block); tre: yes (min_width on the node) |
| interactive node bounds | min height | - | 24 | 24 | 24 | [[Spacing and Density]] (24 dp pointer minimum, WCAG 2.2 SC 2.5.8) | tess-ui: yes (style min_height on the node); tess-shell: yes (Min_Height on the block); tre: yes (min_height on the node) |
| tree | padding | - | N/A: the tree draws nothing, so it has no content box to pad | N/A: same as the Default column | N/A: same as the Default column | [[Accessibility Tree#Tokens used]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | margin | - | N/A: the tree is not laid out; bounds come from the node tree | N/A: same as the Default column | N/A: same as the Default column | [[Accessibility Tree#Layout and overflow]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | gap | - | N/A: the tree has no children laid out in a row or column | N/A: same as the Default column | N/A: same as the Default column | [[Accessibility Tree#Layout and overflow]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | border width | - | N/A: the tree draws no border; a focus indicator is the node's own | N/A: same as the Default column | N/A: same as the Default column | [[Focus Ring]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | border color | - | N/A: the tree carries no colour | N/A: same as the Default column | N/A: same as the Default column | [[Accessibility Tree#Tokens used]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | corner radius | - | N/A: the tree carries no shape | N/A: same as the Default column | N/A: same as the Default column | [[Accessibility Tree#Tokens used]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | font | - | N/A: the tree carries names as text, not type roles; the widget draws the text | N/A: same as the Default column | N/A: same as the Default column | [[Typography]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | icon size | - | N/A: an icon is exposed by name only, its size is the widget's | N/A: same as the Default column | N/A: same as the Default column | [[Iconography]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |
| tree | elevation | - | N/A: the tree has no depth or shadow | N/A: same as the Default column | N/A: same as the Default column | [[Elevation]] | tess-ui: n/a: the tree is data and draws nothing; tess-shell: n/a: the tree is data and draws nothing; tre: n/a: the tree is data and draws nothing |

## Layout and overflow

Not applicable: the tree has no layout. Bounds include scroll shift; a node scrolled out of view keeps bounds outside the viewport; focus and assistive `scroll_into_view` scroll it in ([[Scrollbar and Scroll Container]]). Truncated text keeps the full text as its name ([[10 Layout Overflow and Scrolling]], AC-LAY-13).

## Behaviour

- Roles the engine knows: button, checkbox, radio, switch, slider, progressbar, link, textbox, tab, tablist, tabpanel, menu, menuitem, dialog, alert, list, listitem, tree, treeitem, heading, img, group, none, separator. Roles it lacks (table, row, cell, combobox, searchbox, tooltip, status, toolbar, menuitemcheckbox, scrollbar) cannot be set; the specification treats these as candidate requests where it needs them ([[14 Accessibility Basics]] names `tooltip`, `searchbox`, `menuitemcheckbox`).
- Activation arrives as `click`; increment, decrement, expand, collapse and set value arrive as `a11y_action`; `scroll_into_view` is answered by the engine after listeners run.
- Keyboard: an assistive request to focus a node behaves as Tab.
- Names: the visible label text first; an icon-only control's name equals its tooltip text ([[Tooltip]]); a text node's words are not exposed on their own, so the widget that shows them carries the label.
- Announce queue: `announce(text, politeness)` raises one announcement per call; calls are heard in call order, each update carries the oldest waiting message, six messages take six frames (about 100 ms at 60 Hz), the queue holds 16 and keeps the newest; empty text or any politeness other than polite and assertive raises `ValueError`; it works on windows, layer windows and popup windows and for hidden modules; nothing is heard unless a reader is connected; duplicates are the caller's to remove.

## Tooltip and overlay behaviour

A tooltip's text is also the control's description (and the name for icon-only controls); the tooltip is never the only source of information ([[ADR-0004 Tooltip rule]]). A modal layer scopes focus; its role is `dialog`.

## Motion

Not applicable. Reduced motion and high contrast are read by the engine (`reduced_motion`, `high_contrast`) and are not tree attributes.

## Accessibility

Requirements per node:

- Every focusable or interactive node has a role and a non-empty name (WCAG 2.2 SC 4.1.2).
- Name begins with the visible label (SC 2.5.3).
- Status messages are polite live regions or polite announcements; assertive only for what must be acted on (SC 4.1.3). One announcement per user action unless it has independent results.
- A node hidden from the tree is not focusable; a relation to a hidden or destroyed node is dropped.
- Not tried with Orca, NVDA or VoiceOver; checked against AccessKit's consumer and, for announcements, AT-SPI's `Announcement` signal on a private bus.
- Missing in the engine: set size and position in set for rows of a virtual list (needed by AC-LAY-13), and an exposed scrollbar role (candidate requests).

## Dark and light

Not applicable.

## Defaults

A node has role `none`, no name, no states, no live setting, in the tree unless hidden; text inputs and terminals are `textbox`.

## Acceptance criteria

- [ ] AC-AXT-1 (AT tree assertion): in each shipped view, every node that is focusable or has a click handler has a role other than `none` and a non-empty name. Pass: zero violations.
- [ ] AC-AXT-2 (AT tree assertion): for every node whose name differs from its visible label, the name begins with the label text (label in name).
- [ ] AC-AXT-3 (AT tree assertion): a switch exposes role `switch` and `checked` equal to its state after each toggle; a slider exposes value, min, max and step, and `set_value` 0.75 reads back 0.75.
- [ ] AC-AXT-4 (scripted input): `announce("A")` then `announce("B")` in one loop turn produce two updates, A before B, over two frames, with polite and assertive politeness kept.
- [ ] AC-AXT-5 (scripted input): 20 calls to `announce` leave 16 pending and the first four are dropped; the same text announced twice is announced twice.
- [ ] AC-AXT-6 (scripted input): `announce("")` and `announce("x", "loud")` raise `ValueError`.
- [ ] AC-AXT-7 (AT tree assertion): a live region (`live: polite`) whose text changes produces one announcement; a node with `a11y_hidden` produces none; a node with `visible: false` is absent from the tree and Tab order.
- [ ] AC-AXT-8 (scripted input): a simulated `scroll_into_view` request on an off-screen row brings it inside the viewport (offset read back).
- [ ] AC-AXT-9 (AT tree assertion): a disabled control exposes `disabled` and takes no focus, click or key (AR-7).
- [ ] AC-AXT-10 (AT tree assertion): `describedby` and `controls` list only nodes that are alive, visible and in the same window.
- [ ] AC-AXT-11 (AT tree assertion): a truncated label's name equals the full text.
- [ ] AC-AXT-12 (review): a screen reader pass on one view per project with Orca, NVDA and VoiceOver is recorded as pass, fail or not run (AR-29); today all three are not run.
- [ ] AC-AXT-13 (AT tree assertion): rows of a virtual list expose set size and position. Fails today in the engine.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/a11y.py`, `tess-ui:tests/test_a11y*.py` | partly meets: roles, names and states set by controls and views; tests assert them; no real screen reader run (AC-AXT-12 not run); AC-AXT-13 not verified |
| tess-shell | `tess-shell:src/tess_shell/schema/blocks.py` (`ROLES`, `A11Y_STATE`, `Live`, `A11y_Hidden`), `tess-shell:src/tess_shell/modules/context.py` (`ctx.announce`), `tess-shell:src/tess_shell/surfaces/manager.py` (announce through one window) | partly meets: roles, state, live keys, announcements through the first open window of the module; Orca not installed, announcements and Launcher untested (AC-AXT-12 not run); `Role` set lacks tooltip, searchbox, combobox, table roles |
| tre | `tre:crates/engine-core/src/tree/access.rs`, `tre:crates/engine-core/src/access.rs`, `tre:docs/guide/accessibility.md` | partly meets: tree built every frame; announce queue of 16 in call order; relations; text container; `disabled` announce only; no set size or position (fails AC-AXT-13); role list fixed |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Engine-level contract for the tree | MD3 states principles and no tree API | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| `disabled` does not stop input in the engine; controls must | engine design | [[ADR-0004 Tooltip rule]] |

## Sources

- `tre:docs/guide/accessibility.md`, `tre:crates/engine-core/src/tree/access.rs`, `tre:docs/reference/node.md`.
- WAI-ARIA 1.2 (roles, `aria-live`, relations): https://www.w3.org/TR/wai-aria-1.2/ (read).
- WCAG 2.2 SC 4.1.2, 4.1.3, 2.5.3: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html and https://www.w3.org/TR/WCAG22/.
- MD3 accessibility (JavaScript app #needs-verification): https://m3.material.io/foundations/accessible-design/overview.
