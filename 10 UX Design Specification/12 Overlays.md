---
title: 12 Overlays
type: chapter
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [chapter, overlays, interaction]
related: ["[[01 Principles and Scope]]", "[[10 Layout Overflow and Scrolling]]", "[[14 Accessibility Basics]]", "[[Owner Feedback 2026-11-20]]", "[[Tooltip]]", "[[Popup]]", "[[Menu]]", "[[Dialog]]", "[[Panel and Surface]]", "[[Scrim]]", "[[Elevation]]", "[[Motion]]", "[[Focus Ring]]", "[[Colour Roles]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0003 Scrollbar rule]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# 12 Overlays

> [!info] Summary
> Principle-level rules for everything drawn above application content: tooltips, popups and menus, dialogs, sheets, snackbars. They fix the layers and routes, the z-order, placement, dismissal, focus, the scrim and the one-overlay-at-a-time rules, and link to the component notes that carry the values. Material Design 3 describes each overlay as a component; the cross-component rules here are Tesserae's, built on WAI-ARIA Authoring Practices, WCAG 2.2 and the engine's layer model (see Sources).

## Scope and terms

An overlay is a surface that is drawn above the content of a window or of an output and goes away without navigation. The engine mechanism is a layer (a node tree stacked above the window content, `show_layer` in tre) or a window of its own (a compositor popup window, a layer-surface window). Terms: opener (the control or surface that caused the overlay), anchor (the rectangle the overlay is placed against), trigger (what causes a tooltip), modal (blocks input to everything beneath).

| Overlay | Component note | Modal | Focus on open | Scrim | Dismissed by |
|---|---|---|---|---|---|
| Tooltip | [[Tooltip]] | no | none (stays on trigger) | none | pointer leave, Escape, scroll, press, activation, trigger removal, window focus loss, another tooltip |
| Popup, menu, flyout | [[Popup]], [[Menu]] | no | into the overlay | none | Escape, outside press (consumed), press on another surface, opener toggle, parent closed, window focus loss, choosing an item |
| Dialog | [[Dialog]] | yes | into the dialog | `scrim` at 32 percent | action, Escape and scrim press when dismissible |
| Side sheet, drawer (modal) | component notes outside this slice | yes | into the sheet | `scrim` | as Dialog |
| Snackbar | component note outside this slice | no | none | none | timeout, action, close control |
| Shell Panel on the overlay layer (Launcher, OSD) | [[Panel and Surface]] | per Panel | exclusive keyboard for a Launcher | none | Escape, hide, `Hide_After` |

## Principles

1. An overlay is temporary and answers to its opener: it is placed against it, it returns focus to it, and it goes away when the opener goes away.
2. The user can always leave: every overlay can be dismissed by keyboard (Escape or Tab) and by pointer, except an alert dialog, which has a visible action instead.
3. The most modal overlay wins: a modal removes the non-modal overlays beneath it; a popup removes tooltips; nothing non-modal stays open under a modal.
4. Overlays are opaque and inside the window. A tooltip or popup is never drawn without a container, and never extends past the window or output without being repositioned (owner feedback F9, [[Owner Feedback 2026-11-20]]).
5. Overlays do not hold the only copy of information. A tooltip text is also the trigger's description; a menu item label is the item's name.
6. The keyboard never gets lost. Opening an overlay moves focus deliberately, and the mechanism that dismisses it must not take focus (the Launcher failure on KWin, 2026-11-20).

## Layers and routes

Three routes exist; a spec note names which one an overlay uses.

| Route | What it is | Clipping | Cost | Use |
|---|---|---|---|---|
| In-window layer | A node tree stacked above the window content (tre `show_layer`); engine places, flips, shifts, routes input and sends `dismiss` | Clipped to the host window | Negligible | Tooltips, menus, dialogs, snackbars in an application window |
| Popup window | A compositor-placed window with a grab (`xdg_popup` through tre `PopupWindow`); size fixed for its life; Wayland layer-shell only; needs an open layer or popup window as parent | Not clipped by the parent surface | One small window (a bar's worth of memory) | Menus and tooltips that must extend past a shell bar or panel |
| Overlay layer window | A transparent output-sized layer window on the `OVERLAY` layer that draws overlays with `show_layer` | Clipped to the output | Hundreds of MB while open | Overlays that span outputs, a Launcher or OSD as a Panel |

Rules:

- A layer in a layer-surface host (bar, panel) is clipped to that surface. An overlay that does not fit inside the host uses the popup-window route or the overlay layer route.
- A launcher or menu opened by shortcut or IPC has no user-action serial for a grab; it is a Panel on the overlay layer with exclusive keyboard, never a focused popup.
- tre has no tooltip primitive, no menu node and no scrim (it offers `window.after` and `window.every` timers, but no hover-delay service): the toolkit builds them (tess-ui) or the shell does (tess-shell).

## Z-order

Higher rank always draws above lower rank, whatever the order of opening; equal rank stacks in order of opening.

| Rank | Overlay |
|---|---|
| 0 | Window content |
| 1 | Standard (non-modal) sheets and docked panels |
| 2 | Snackbars |
| 3 | Popups, menus, flyouts |
| 4 | Scrim and modal surfaces (dialog, modal sheet, modal drawer) |
| 5 | Tooltips |

A tooltip of a control inside a dialog therefore shows above the dialog and its scrim. A control beneath the scrim does not show a tooltip: tooltips of controls blocked by a modal do not open. tre stacks layers in order of opening, so a toolkit that must keep this order sorts or closes layers itself.

## Placement

- Anchored placement: preferred side (`below` by default, start-aligned), flip to the opposite side when the preferred side lacks room and the opposite has more, then shift along the other axis to stay inside the window or output. The gap between anchor and overlay is 4 dp for a tooltip and 0 dp for a menu by default; a project may set the gap per overlay (the shell uses 4 dp for tray menus).
- The visible body is what is placed. A transparent shadow margin never counts for gap, flip or shift, and takes no input.
- The overlay rectangle always lies inside the window or output rectangle.
- Overlays follow their anchor when it moves with layout; a tooltip instead dismisses when an ancestor scrolls.
- Overlays larger than the available space are clamped to it and scroll ([[ADR-0003 Scrollbar rule]]); a tooltip never scrolls: it wraps at its maximum width.
- Corner placements (the centre of the overlay on a corner or centre of the anchor) are explicit exceptions that are not flipped.

## Dismissal

| Cause | Tooltip | Popup, menu | Dialog |
|---|---|---|---|
| Escape | dismisses | closes the innermost level, focus returns to opener | closes when dismissible |
| Press outside | not applicable (a press on the trigger dismisses) | dismisses and is consumed | press on the scrim dismisses when dismissible, consumed |
| Press on another surface of the application | not applicable | closes a focused popup, consumed | blocked by the scrim |
| Scroll of an ancestor of the anchor | dismisses | follows the anchor, or closes when the project says so | not applicable |
| Pointer leaves | dismisses after the 150 ms grace; the pointer may move onto the tooltip meanwhile ([[ADR-0011 Tooltip hover grace for all tooltips]]) | no effect | no effect |
| Activation of the trigger or opener | dismisses | toggles (closes, does not reopen) | not applicable |
| Anchor removed or hidden | dismisses | closes | not applicable |
| Window loses focus | dismisses | closes (explicit grab ends) | stays open |
| Another overlay of the same class opens | dismisses | closes (submenu chain excepted) | refused by default |

Escape closes only the topmost dismissible overlay. A press inside an overlay never dismisses the overlays beneath it, so a submenu keeps its parent open. An outside press that dismisses is consumed: it does not reach the element beneath and does not reactivate the opener.

## Focus

- Opening: tooltips take no focus; popups and menus move focus into the overlay (first enabled item, or the text input of a launcher); dialogs move focus by the initial-focus rule in [[Dialog]].
- Scope: each open layer is its own focus scope; Tab stays inside a modal; a menu closes on Tab and moves focus out to the control after the opener.
- Closing: focus returns to the control that was focused when the overlay opened, with its focus-visible state preserved; when that control is gone, to the nearest logical element ([[Focus Ring]]: the ring shows for keyboard focus only).
- The text-input rule: in an overlay with a text input, a pointer press on a non-focusable area inside the overlay keeps focus on the text input; the click-away mechanism holds no keyboard focus.
- No keyboard trap: Escape or a visible action always leaves (WCAG 2.2 SC 2.1.2).

## Scrim

Only modal surfaces draw a scrim: colour role `scrim`, opacity 0.32, whole window, below the modal and above everything else; one scrim under the topmost modal. Details and tests: [[Scrim]]. An invisible click-away layer is not a scrim and draws nothing.

## One overlay at a time

- Tooltip: at most one visible; showing one hides the others.
- Popup: at most one open, plus the chain of its submenus (parent and one open child per level, depth at most 3 in the shell).
- Modal: at most one dialog or modal sheet open; a modal opened over a modal is refused by default.
- Cross-class: opening a popup hides every tooltip; opening a modal closes every popup and hides every tooltip outside it; a tooltip never opens over a focused popup for a trigger outside the popup.

## Motion and reduced motion

No overlay requires animation. Where a project animates, durations come from [[Motion]]; the scrim timings are in [[Scrim]]. With reduced motion on, every overlay appears and disappears in one frame ([[Accessibility Rules]]).

## Overlays in shell layer-surface hosts

| Element | Route | Note |
|---|---|---|
| Tray menu, context menu, calendar flyout | popup window, focused grab | opened in response to input on a shell surface |
| Module tooltip | popup window, no grab | hover only today; keyboard focus path is a gap |
| Launcher | Panel on the overlay layer, exclusive keyboard | Escape closes it; no click-catcher with a grab |
| Volume OSD | Panel, click-through (`Input_Region: []`) | hides itself after a delay |
| Dialog | none exists | would be a Panel on the overlay layer (design note, not a promise) |

## Owner feedback served by this chapter

| Feedback | Rule | Where |
|---|---|---|
| F2 tooltips stay after hover leaves | Dismissal table | [[Tooltip]] AC-TIP-4 to AC-TIP-8, AC-OVL-2 |
| F8 tooltip on the whole row, several tooltips, covering the panel | Trigger is the control; one tooltip at a time | [[Tooltip]] AC-TIP-1, AC-TIP-2, AC-TIP-9; AC-OVL-2 |
| F9 tooltip text with no background after a click on a switch | Opaque container, clipped to the window, mouse click never shows a tooltip | [[Tooltip]] AC-TIP-10, AC-TIP-11, AC-TIP-15; AC-OVL-7 |
| Launcher unreadable with no stylesheet | Surfaces resolve from roles with the default stylesheet | [[Panel and Surface]] AC-PNL-1 |
| Click-away layer under the Launcher, keyboard taken | The text-input rule; the dismiss mechanism holds no keyboard | [[Popup]] AC-POP-6, AC-POP-7; AC-OVL-9 |

## Accessibility

Roles: tooltip layers are hidden from the tree and their text is the trigger's description; menus `menu` with `menuitem`; dialogs `dialog` (`alertdialog` where available) named by their headline; a popup window is one more window of the application with a name. While a modal is open, content beneath is inactive. Contrast of overlay text on its container at least 4.5:1 in light and dark. See [[14 Accessibility Basics]] and [[Accessibility Rules]].

## Acceptance criteria

Scenario tests follow [[Test Method]]: toolkit key and pointer simulation and the frame clock; items marked manual are hand checks on a real compositor.

- [ ] AC-OVL-1 (scripted input, z-order): open a popup, then a dialog; open a tooltip for a control inside the dialog. Pass: the popup is closed, the layer stack order is dialog above content and tooltip above dialog, and a pixel sample inside the tooltip shows the tooltip container colour.
- [ ] AC-OVL-2 (scripted input, invariant test, one at a time): run a scripted scenario of 200 random pointer moves, key presses, scrolls and openings across triggers, menus and dialogs, sampling the layer stack every frame. Pass: at every frame at most 1 tooltip, at most one popup chain (one parent and one open child per level), at most 1 modal.
- [ ] AC-OVL-3 (scripted input, Escape order): with a dialog open and a menu opened from it, Escape closes the menu only (dialog still open), the second Escape closes the dialog; with a tooltip also showing, the first Escape closes the tooltip only.
- [ ] AC-OVL-4 (scripted input, consumed outside press): for a popup and a dismissible dialog, a press on a button beneath runs 0 handlers and dismisses the overlay.
- [ ] AC-OVL-5 (scripted input, focus return): for each of tooltip (Escape), menu, popup and dialog, after closing the focused node is the opener and its focus-visible state equals its state before opening.
- [ ] AC-OVL-6 (scripted input, modality): opening a dialog hides every tooltip and closes every popup within one frame; tooltips of controls beneath the scrim do not open (hover for 1 s: 0 layers).
- [ ] AC-OVL-7 (geometry check, inside the window): for each overlay type, with the anchor at each window edge and corner and after the window shrinks by 20 percent while open, the overlay rectangle is inside the window rectangle and the gap is as specified when no flip or shift occurred.
- [ ] AC-OVL-8 (scripted input, anchor follows): move the anchor of an open menu by 50 dp through layout; the menu rectangle follows within one frame (±1 px); for a tooltip, scrolling an ancestor removes it within one frame.
- [ ] AC-OVL-9 (scripted input, event log, keyboard retention): showing an overlay that takes text input never produces a keyboard-lost event within 500 ms, and typed characters appear in the input; the click-away mechanism is active during the test (manual on KWin).
- [ ] AC-OVL-10 (pixel check, no scrim for non-modal): opening a menu, a popup and a tooltip leaves the window background pixels unchanged outside the overlay and its shadow ([[Scrim]] AC-SCR-5); a dialog changes them to 0.68 of the original within 2 levels.
- [ ] AC-OVL-11 (scripted input, window focus): with a tooltip and a popup open, window focus loss closes both within one frame; an open dialog stays open.
- [ ] AC-OVL-12 (geometry check, route): a menu 200 dp tall opened from a 32 dp high layer-surface bar is fully visible (corner pixels read the container colour); a menu in an application window is inside the window.
- [ ] AC-OVL-13 (scripted input, reduced motion): with reduced motion on, the first frame after opening draws each overlay type complete, and the frame after closing draws none.
- [ ] AC-OVL-14 (AT tree assertion): each open overlay exposes the roles and names above; a tooltip layer is hidden and its text is the trigger's description; with a dialog open, no node beneath is focusable.
- [ ] AC-OVL-15 (review): no overlay is the only place where required information appears; a reviewer checks every tooltip text against the control's label and helper text.

## Status in code

| Project | Where | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/composed.py` (tooltips, `Overlay` wiring), `tess-ui:src/tess_ui/overlays.py`, `tess-ui:docs/guide/overlays.md` | Partly meets. Layers with engine placement, Escape and outside-press dismissal, modal scrim at 32 percent, Tab kept inside a modal, focus return exist; no z-order ranks (layers stack in order of opening), no one-at-a-time rule across classes, tooltips not dismissed on scroll, rich tooltip actions not keyboard reachable, dialog initial focus not built. |
| tess-shell | `tess-shell:src/tess_shell/surfaces/popup.py`, `tess-shell:src/tess_shell/surfaces/manager.py`, Launcher in `tess-shell:src/tess_shell/shipped/Applications/` | Partly meets. Popup windows with grab, flip and slide, one popup at a time, shadow click-through, focus return; tooltip is hover only; Escape closure is done by the shell itself and is not verified on KWin; the click-away catcher of M7k failed the owner hand check of 2026-11-20 (keyboard taken, revert PR #111); no dialog, scrim or snackbar. |
| tre | `tre:docs/reference/layers.md`, `tre:docs/reference/layer-window.md` | Mechanisms only: layers, modal input blocking, flip and shift, `dismiss`, popup windows, input regions; no tooltip, menu, scrim or timers. |

## Sources

- tre layer model (stacked in order of opening, placement flip then shift, modal blocks input and keeps Tab inside, `dismiss` on outside press and on Escape for the topmost dismissible layer, press inside a layer never dismisses layers beneath, each layer its own focus scope, `hide_layer` returns focus, the engine draws no scrim): `tre:docs/reference/layers.md`. Window clipping, popup window and overlay layer routes and their cost: `tre:docs/reference/layer-window.md`, `tre:docs/guide/menus-from-a-bar.md`.
- WAI-ARIA Authoring Practices: tooltip (`https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/`), modal dialog (`https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/`), menu and menubar (`https://www.w3.org/WAI/ARIA/apg/patterns/menubar/`). WCAG 2.1 SC 1.4.13 Content on Hover or Focus (`https://www.w3.org/WAI/WCAG21/Understanding/content-on-hover-or-focus.html`); WCAG 2.2 SC 2.1.2 No Keyboard Trap (`https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html`).
- xdg-shell `xdg_popup.grab` (dismissed on outside click, keyboard use or lock; denied grab dismisses; needs a user action serial): `https://wayland.app/protocols/xdg-shell`.
- Material Web component tokens for menu, dialog, plain and rich tooltip, scrim: `https://github.com/material-components/material-web/tree/main/tokens`.
- The z-order ranks, cross-class closing rules and the window-focus-loss rule are Tesserae design choices, not MD3 values #needs-verification-as-design-choice.
- Shell vault: `shell-vault:40 Specifications/Surfaces/Popup.md`, `shell-vault:00 Home/M7 Build Log.md` (M7k).
