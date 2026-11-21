---
title: Status Bar
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, navigation, status, owner-feedback]
related: ["[[Toolbar]]", "[[Top App Bar]]", "[[Tabs]]", "[[Pagination]]", "[[Accessibility Announcements]]", "[[Snackbar]]", "[[Linear Progress Indicator]]", "[[Progress Bar]]", "[[Tooltip]]", "[[Dialog]]", "[[Keyboard Navigation]]", "[[Owner Feedback 2026-11-20]]", "[[Spacing and Density]]", "[[Colour Roles]]", "[[Typography]]", "[[Iconography]]", "[[State Layers]]", "[[Focus Ring]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0004 Tooltip rule]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]"]
depends_on: ["[[Colour Roles]]", "[[Typography]]", "[[Spacing and Density]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]"]
---

# Status Bar

> [!info] Summary
> A thin strip at the bottom of a window that reports what the application just did and what state it is in: a message at the start, context in the middle, state and position at the end. Material Design 3 has no status bar; the specification uses MD3 surface and label styles. Source of truth in code: see Status in code. The config application builds a status line by hand; it is the evidence for the content and announcement rules.

## Purpose

Tells the user the result of the last action ("Saved", "Check found 2 problems") and the standing state ("Shell: running", "Ln 4, Col 2") without a dialog and without moving focus.

## When to use and not

- Use when: a desktop window has a long-lived task area and needs a stable place for results and state.
- Do not use when: the message needs a response (use a [[Dialog]]); the message is brief and tied to one action with an undo (use a [[Snackbar]]); the bar holds commands (use a [[Toolbar]]); the information is required to use a control (put it in the label or helper text, not only in the bar).
- One status bar per window, at the bottom, full width.

## Anatomy

1. Container (role `group`, name "Status"), `surface_container`.
2. Three sections: start (message and notes), centre, end. The centre section is centred on the bar whatever the sides hold.
3. Note: an icon (optional) and a text, not pressable.
4. Item: a note with a value that can be pressed; a state layer, a tooltip.
5. Progress edge: a 4 dp [[Linear Progress Indicator]] along the top edge, determinate (0 to 1) or indeterminate.
6. Error icon (optional) before a message that reports an error.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Message only | a bar that says one thing | one note at the start |
| Sectioned | context and state items | start, centre and end sections |
| With progress | a task is running | progress edge shown, `busy` set |

## States

| State | Visual change | Token values |
|---|---|---|
| Rest | `surface_container` container; text and icons `on_surface_variant` | [[Colour Roles]] |
| Message is an error | error icon (16 dp) before the text and the text in `error`; the icon is the non-colour carrier | `error` role |
| Item hover | state layer 8 percent in `on_surface_variant`, corner 4 dp | [[State Layers]] |
| Item focus (keyboard) | state layer 10 percent and the focus ring (inward) | [[Focus Ring]] |
| Item pressed | state layer 10 percent | [[State Layers]] |
| Busy or progress | 4 dp indicator on the top edge in `primary` over `surface_container_highest` | progress track |
| Item disabled | text 38 percent, no focus, pointer or key | [[State Layers]] |

## Tokens used

[[Colour Roles]]: container `surface_container`, text and icons `on_surface_variant`, error `error`, progress `primary`. [[Typography]]: `label_small` (11 / 16, weight 500; minimum text size 11 dp). [[Iconography]]: 16 dp icons. [[Spacing and Density]]. [[Motion]]: layer fade.

## Sizing and density

The bar's height does not scale with the density level: 24 dp at default, compact and dense. The bar is a reporting strip; 24 dp is the minimum pointer target ([[ADR-0002 Desktop density levels and target sizes]]) and the `label_small` line is 16 dp, so a pressable item has the full bar height as hit area and there is no room to shrink it.

| Level | Height | Text | Icon | Horizontal padding of the bar | Padding inside an item | Gap icon to text | Gap between items |
|---|---|---|---|---|---|---|---|
| default | 24 dp | `label_small` | 16 dp | 8 dp | 4 dp | 4 dp | 16 dp |
| compact | 24 dp | `label_small` | 16 dp | 8 dp | 4 dp | 4 dp | 16 dp |
| dense | 24 dp | `label_small` | 16 dp | 4 dp | 4 dp | 4 dp | 8 dp |

- Heights and paddings are design choices anchored on the tess-ui values (24 dp, 8 dp, 4 dp, gap 16 dp); the dense reductions are Tesserae choices.
- The text line (16 dp) is centred vertically in the bar by construction (4 dp above and below).
- A pressable item's hit area is its width by 24 dp (at least 24 dp by 24 dp); in a touch context 48 dp high, which overlaps the bar edge and is allowed only at the window edge ([[Spacing and Density]]).
- The progress edge is 4 dp, drawn over the top edge, and adds no height.
- A project that needs a taller bar (the config app builds 32 dp with 8 dp padding all round) states it in a project ADR; it then fails AC-STB-1 by design.

## Layout and overflow

- Single line everywhere: every text has `Max_Lines 1` and an ellipsis at its end; the full text is available as a tooltip on that note or item (ADR-0004) and is the item's name ([[10 Layout Overflow and Scrolling]]). A text that shrinks needs `Min_Width 0` on its container.
- Narrow window: space is taken in this order. First the start message shrinks to an ellipsis, down to 120 dp. Then the centre section drops its items, then the end section drops items from the left. Within a section the author's list order is the priority: the first item is dropped last, the last item first. Dropped items disappear from the bar; their text stays available through the item's own command or a menu in the host. The error message is never dropped before the other items. This is a Tesserae rule; tess-ui has no hiding ("Not built").
- No wrapping, no scrolling; the bar never paints outside the window and never grows taller.
- The sections are a grid of `1fr auto 1fr` so the centre section stays centred.

Config app evidence (`tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, container `status_bar`): a horizontal Container with padding 8 and gap 8 holds an error icon (18 dp, only while the status is an error), the status Text (`body_small`, `Live: polite`, `Flex: expand_horizontal`, `Min_Width 0`, colour `error` or `on_surface_variant`) and the shell state Text ("Shell: not asked yet", `Max_Lines 1`, ellipsis). It is not the shipped `StatusBar`. Its height is 32 dp (8 + 16 + 8), the background is the window `surface` (no container colour), the status text has no `Max_Lines` and no ellipsis, and the role is `group` named "Status" with a description.

## Behaviour

- Pointer: a plain note is not interactive. An item with a value presses once on release inside it; hover shows the state layer.
- Keyboard: pressable items are Tab stops in visual order (start, centre, end), no roving group for the two to four items usually present ([[Keyboard Navigation]]); with five or more pressable items the bar becomes one roving group (arrows, Home, End) #needs-verification as design choice. Enter and Space activate. Notes take no focus.
- Message lifetime: a message stays until replaced; it is not cleared by a timer. An error message stays at least until the user's next action. A new action's message replaces the old one at once.
- The bar never takes focus by itself and never steals it when a message changes.
- Touch: tap on an item.

## Tooltip and overlay behaviour

A note or item that has a tooltip shows it on that note or item only: the control that carries the text, not the bar or the section (ADR-0004, ADR-0011; tess-ui attaches `Tooltip` to the note container). A truncated text always has one with its full text. 500 ms hover, immediate on keyboard focus, dismissed on press or Escape. A pressable item may open a [[Popup]] or [[Menu]] above it ("Go to line"); focus returns to the item on close.

## Motion

State layer `short3` (150 ms in the Specification; tess-ui 15 ms hover). Message text changes at once without animation. The progress edge animates by the [[Linear Progress Indicator]] rules; with reduced motion the indeterminate form shows as a static partial bar #needs-verification. Nothing slides.

## Accessibility

- Role: `group` named "Status" (the engine has no `status` role, `tre:docs/reference/node.md`; a request to tre would add `status` for the live region), with a description of what it reports. Pressable items are role `button` named by their text.
- Announcement rules (WCAG 2.2 SC 4.1.3 status messages; [[14 Accessibility Basics]], [[Accessibility Announcements]]):
  1. The message text is a polite live region; a change of text is announced once, after the reader finishes the current speech. The bar is never assertive.
  2. Only the item whose text changed is announced, not the whole bar. The live attribute sits on the message and item text nodes, not on a group that would re-read every item.
  3. A text set to its current value is not announced again.
  4. A message that changes more often than once per second is announced at most once per second with the latest text (design choice); the intermediate texts are skipped.
  5. A progress update is not announced per step. The progress edge has role `progressbar` with `value_min` 0, `value_max` 1 and the value (indeterminate: no value), and `busy` is set on the bar while it runs. The end of the task is announced by the message ("Check finished: 2 problems"). Progress is read on request, not pushed.
  6. An error message is announced politely with its error icon hidden from the tree and the word "error" in the message text ("Error: could not write file"). If the user must act, the status bar is the wrong element: use a [[Dialog]].
  7. A message is not the only place where information lives: every result of an action is also visible in the place the action happened (a failing field shows its own error, a failed check lists problems).
- Name and keys: an item's name is its visible text; the tooltip adds a description, not the only name.
- Contrast: `on_surface_variant` on `surface_container` at least 4.5 to 1; `error` on `surface_container` at least 4.5 to 1 (11 dp text is small text); icons 3 to 1.
- Colour is not the only carrier of the error state: the icon and the word differ from a normal message.

## Dark and light

All roles follow the scheme ([[Theme Following the System]]); AC-STB-8 runs in both and in high contrast.

## Defaults

Height 24 dp, `surface_container`, `label_small`, `on_surface_variant`, a message at the start, no progress, bar width equal to its place. A project that sets a different height records it in a project ADR.

## Acceptance criteria

- [ ] AC-STB-1 (token test): height 24 dp at default, compact and dense; text role `label_small`; icon 16 dp; paddings and gaps equal the Sizing table. Pass: values equal.
- [ ] AC-STB-2 (geometry check): the text line box is vertically centred in the bar (space above equals space below within 0.5 dp) at scale 1.0 and 2.0, with and without an icon. Pass: offsets within 0.5 dp.
- [ ] AC-STB-3 (geometry check): a start message longer than the available width ends with an ellipsis, no text pixel lies outside the bar and a tooltip with the full text shows on that note only; the bar stays 24 dp tall. Pass: ellipsis present, zero pixels outside, tooltip text equals the message.
- [ ] AC-STB-4 (scripted input): with the window narrowed in steps, the start message shrinks first (not below 120 dp), then centre items drop, then end items drop from the lowest priority; no two items overlap and no item is clipped at any width. Pass: the dropped set equals the rule at each width.
- [ ] AC-STB-5 (token test): container `surface_container`, text and icons `on_surface_variant`, error text `error`, progress `primary`; no literal colour. Pass: role references.
- [ ] AC-STB-6 (scripted input): a pressable item activates once on Enter, once on Space, once on a pointer press and release inside, zero on press, move out and release; a plain note takes no focus; disabled items take no focus or key. Pass: counts equal.
- [ ] AC-STB-7 (scripted input): announce queue: setting the message to a new text raises one polite announcement with that text only; setting the same text again raises none; ten changes within 500 ms raise at most one announcement per second, the last text included; a progress change from 0.1 to 0.9 raises none; the end message raises one. Pass: queue contents equal.
- [ ] AC-STB-8 (contrast script): in light, dark and high contrast, `on_surface_variant` and `error` on `surface_container` at least 4.5 to 1; icons at least 3 to 1. Pass: ratios at or above limits.
- [ ] AC-STB-9 (AT tree assertion): the bar is a `group` named "Status"; each pressable item has role `button` and a name equal to its text; the progress edge has role `progressbar` with its value; `busy` is true while progress or busy shows; the error icon is hidden and the message text contains the word "error". Pass: all equal.
- [ ] AC-STB-10 (pixel check): in an error message the greyscale render differs from a normal message by the icon and the text, not only by colour. Pass: renders differ in at least one non-colour feature.
- [ ] AC-STB-11 (geometry check): a pressable item's hit area is at least 24 dp by 24 dp (its width by the bar height) and hit areas do not overlap. Pass: bounds at or above limits.
- [ ] AC-STB-12 (scripted input): a changed message never moves focus; an error message remains after 10 s with no user action and is replaced by the next action's message at once. Pass: focus owner and text equal.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/StatusBar_View.tdl`, `tess-ui:src/tess_ui/views/StatusBar_Stylesheet.tdl`, `tess-ui:src/tess_ui/widgets/navigation.py` | partly meets. 24 dp, `label_small`, `surface_container`, `on_surface_variant`, 16 dp icons, padding 8, gap 16 (AC-STB-1, AC-STB-5 meet by reading); three sections with a centred middle; items with a state layer, tooltip and role `button`; 4 dp progress edge; role `group` with `Live: polite` on the whole bar, not on the changed item (AC-STB-7 partly, AC-STB-9 partly); texts have no `Max_Lines` or ellipsis (AC-STB-3 fails); no dropping or hiding of items ("Not built", AC-STB-4 fails); no error state or icon (AC-STB-10 not built); progress has no announcement rule read (AC-STB-7 unmeasured); no density (all levels 24 dp, which meets) |
| tess-ui | `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl` (container `status_bar`) | partly meets: hand-built, not the shipped `StatusBar`. Polite live text node (AC-STB-7 partly, changed text only because the live attribute is on the status text), error icon plus `error` colour plus text (AC-STB-10 meets), role `group` named "Status" (AC-STB-9 partly); height 32 dp (AC-STB-1 fails), container colour `surface` not `surface_container` (AC-STB-5 fails), status text `body_small` 12 / 16 not `label_small` (AC-STB-1 fails), status text without ellipsis (AC-STB-3 fails), shell state text with ellipsis (meets); no tooltips |
| tess-shell | none (the shell has module bars; see [[Bar]]) | absent |
| tre | `tre:docs/guide/accessibility.md` | not applicable: live regions and `announce` exist; no `status` role |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| The element exists although MD3 has no status bar | desktop convention; the config app and any editor need a stable place for results | none (Tesserae element) |
| Height 24 dp at every level | 24 dp is the desktop minimum target; the line is 16 dp | [[ADR-0002 Desktop density levels and target sizes]] |
| `label_small` 11 dp text on `surface_container` | MD3 label and surface styles; 11 dp is the minimum text size | none |
| Hover state layer on pressable items at 8 percent with corner 4 dp | MD3 hover value, small shape | [[ADR-0002 Desktop density levels and target sizes]] |
| Narrow-window rule drops items by priority | no clipping rule (chapter 10) | none |

## Sources

- No MD3 page: the Material 3 component list has no status bar ([Material 3 components](https://m3.material.io/components)); the page could not be fetched, so the statement rests on `tess-ui:docs/components/status-bar.md`, which says the same #needs-verification.
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) SC 1.4.1, 1.4.3, 1.4.11, 2.5.8, 4.1.3 (status messages).
- [WAI-ARIA 1.2 live regions](https://www.w3.org/TR/wai-aria-1.2/#live_region_roles): `status` role is polite, `alert` is assertive.
- Code: `tess-ui:docs/components/status-bar.md`, `tess-ui:src/tess_ui/views/StatusBar_View.tdl`, `tess-ui:src/tess_ui/views/StatusBar_Stylesheet.tdl`, `tess-ui:apps/shell_config/src/tess_shell_config/Views/Main_View.tdl`, `tre:docs/guide/accessibility.md` (live regions, `announce`), `shell-vault:40 Specifications/Configuration Application.md` (status bar line "no shell is running").
- The `label_small` size (11 / 16) is from [[Typography]].
