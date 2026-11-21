---
title: Drag and Drop
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, behaviour, drag, engine, shell]
related: ["[[Drag and Drop Pattern]]", "[[Drag and Drop|Drag Interaction]]", "[[Panel and Surface]]", "[[Layer Window]]", "[[Application Window]]", "[[Node Graph]]", "[[Scrollbar and Scroll Container]]", "[[Focus Ring]]", "[[State Layers]]", "[[Accessibility Tree]]", "[[14 Accessibility Basics]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[14 Accessibility Basics]]", "[[State Layers]]"]
aliases: ["Drag And Drop", "Pointer capture and drag", "OS file drag and drop", "Panel drag (docking)"]
---

# Drag and Drop

> [!info] Summary
> The capability note: what dragging the engine and shell support today (pointer capture, panel docking drags, margin drags of layer surfaces, slider drags, OS file drops), and the constraints every drag must meet. The interaction pattern (cues, targets, cancel) is [[Drag and Drop Pattern]]. MD3 describes the [gesture](https://m3.material.io/foundations/interaction/gestures) and the dragged state layer, not an API.

## Purpose

State which drags exist, what each reports, and the rules that make a drag usable: a non-drag alternative, a cancel, a visible dragged state.

## When to use and not

- Use when: the operation is moving or sizing something by pointer (panel rearranging, margins, sliders, node positions) or receiving files from the OS.
- Do not use when: a click, key or menu command does the job; dragging must never be the only way to do something (WCAG 2.2 SC 2.5.7).

## Anatomy

1. Source: the node whose `pointer_down` starts the drag and captures the pointer.
2. Pointer capture: events continue to the source after the pointer leaves it; ends on release or `release_pointer()`.
3. Target: a zone or node under the pointer (`dock_target`, `file_hover`).
4. Drop and cancel events: `dock_drop`, `file_drop`, `file_hover_cancel`, `pointer_cancel`.
5. Feedback: highlight over the target and the dragged state of the source, drawn by the framework (the engine draws nothing).

## Variants

| Variant | Use | Engine support | Non-drag alternative |
|---|---|---|---|
| Pointer capture drag | sliders, resize handles, node moves | `capture_pointer`, `release_pointer` | keys (arrows) on the control |
| Panel drag (docking) | rearrange panels between zones | `start_panel_drag`, `dock_target`, `dock_drop` | `dock_panel(side, panel)` from a "Move to" menu |
| Surface drag by margin | movable layer panel | `window_region: drag_margin`, `moved` event | not built |
| Window drag | undecorated window | `window_region: drag` (OS moves it) | OS window menu |
| OS file drop | open files | `file_hover`, `file_drop`, `file_hover_cancel` (X11, Windows, macOS; never on Wayland) | an Open command with a file dialog |
| Content drag and drop | lists, trees, between apps | not built | n/a |

## States

State layer percentages from [[State Layers]]: dragged 16 percent.

| State | Visual change | Token values |
|---|---|---|
| Source dragged | dragged state layer on the source, cursor `grabbing` | `on_surface` 16 percent |
| Source grabbable | cursor `grab` | none |
| Valid target | highlight over the target zone | role `primary` at 12 percent, border 2 dp `primary` (Tesserae choice #needs-verification) |
| Invalid target | cursor `not_allowed`, no highlight | none |
| Cancelled | source returns to its start place, no change | none |

## Tokens used

[[State Layers]] (dragged), [[Colour Roles]] (`primary` for targets), [[Focus Ring]] for the keyboard path, [[Motion]] for the return animation.

## Sizing and density

Not applicable by density. Drag handles are at least 24 dp by 24 dp (48 dp in touch contexts, [[Spacing and Density]]). A drag starts after the pointer moves at least 4 dp from the press (Tesserae choice #needs-verification) so a click never drags.

## Dimensions and defaults

Dragging has no box of its own: the engine draws nothing, and the framework draws a target highlight and the dragged state. Rows give the handle size, the start distance and the target highlight. The values are the same at every density; in a touch context the handle minimum is 48 dp ([[Spacing and Density]]). The start distance and the target highlight are Tesserae design choices #needs-verification.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| drag handle | height | - | N/A: the handle keeps the height of its control; only a floor is set here | N/A: same as the Default column | N/A: same as the Default column | [[Drag and Drop#Sizing and density]] | tess-ui: yes (style height); tess-shell: yes (Height); tre: yes (height) |
| drag handle | min width | - | 24 | 24 | 24 | [[Spacing and Density]] (24 dp pointer minimum; 48 in touch contexts) | tess-ui: yes (style min_width); tess-shell: yes (Min_Width); tre: yes (min_width) |
| drag handle | min height | - | 24 | 24 | 24 | [[Spacing and Density]] (24 dp pointer minimum; 48 in touch contexts) | tess-ui: yes (style min_height); tess-shell: yes (Min_Height); tre: yes (min_height) |
| drag handle | padding | - | N/A: the handle's padding belongs to the control that hosts it | N/A: same as the Default column | N/A: same as the Default column | [[Drag and Drop#Sizing and density]] | tess-ui: yes (style padding of the host); tess-shell: yes (Padding of the host); tre: yes (padding of the host) |
| drop target | margin | - | N/A: a hovered target never changes its size or position, so no space is added | N/A: same as the Default column | N/A: same as the Default column | [[Drag and Drop#Layout and overflow]] | tess-ui: n/a: a hovered target adds no space; tess-shell: n/a: a hovered target adds no space; tre: n/a: a hovered target adds no space |
| press to first drag move (start distance) | gap | - | 4 | 4 | 4 | design choice, proposed ADR drag start distance, [[Drag and Drop#Sizing and density]] (AC-DND-8) | tess-ui: no hook; tess-shell: no hook; tre: n/a: the engine has no pointer drag threshold, the app code decides |
| valid drop target highlight | border width | - | 2 | 2 | 2 | design choice, proposed ADR drop target highlight, [[Drag and Drop#States]] | tess-ui: no hook; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no drop highlight |
| valid drop target highlight | border color | `primary` | `primary` | `primary` | `primary` | design choice, proposed ADR drop target highlight, [[Colour Roles]] | tess-ui: via theme role primary; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no drop highlight |
| drop target | corner radius | - | N/A: the highlight follows the shape of the target zone | N/A: same as the Default column | N/A: same as the Default column | [[Shape]] | tess-ui: n/a: the highlight follows the target zone; tess-shell: n/a: element absent in tess-shell; tre: n/a: tre draws no drop highlight |
| drag source and target | font | - | N/A: dragging draws no text; the dragged control keeps its own type role | N/A: same as the Default column | N/A: same as the Default column | [[Typography]] | tess-ui: n/a: dragging draws no text; tess-shell: n/a: dragging draws no text; tre: n/a: dragging draws no text |
| drag source and target | icon size | - | N/A: dragging draws no icon; the cursor is the OS cursor | N/A: same as the Default column | N/A: same as the Default column | [[Iconography]] | tess-ui: n/a: dragging draws no icon; tess-shell: n/a: dragging draws no icon; tre: n/a: dragging draws no icon |
| dragged source | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]], [[State Layers]] (the dragged state is a 16% layer, no shadow) | tess-ui: yes (style elevation); tess-shell: yes (Elevation percentage); tre: yes (shadows) |

## Layout and overflow

- A dragged preview, if any, is a layer above everything and is clipped to the window ([[12 Overlays]]).
- Dragging near an edge of a scroll container scrolls it: not built in the engine; a long list that needs it must also offer key moves.
- A drop target never changes its own size while hovered.

## Behaviour

- Pointer: press captures; moves report window and local positions; Escape cancels a drag in progress (spec; the engine ends the drag only on release or `undock_panel`); release over a target drops; release elsewhere cancels.
- Keyboard: every drag has a key equivalent: arrow keys move a node or a slider; a Move command places a panel; a file is opened by a command. A pointer-only drag fails WCAG 2.2 SC 2.5.7.
- Touch: long-press then drag is not specified.
- File drag on Wayland does not fire events (the toolkit under the engine does not implement it); a Wayland session must offer an Open command.
- OS file drag gives no position of its own: the target is the node under the pointer's last known position, which on some platforms is where the drag entered; for a full-window drop target listen on the window.

## Tooltip and overlay behaviour

A tooltip open when a drag starts is dismissed (activation or press of the trigger, [[ADR-0004 Tooltip rule]]). A drag does not open overlays.

## Motion

Direct manipulation follows the pointer with no easing; a cancelled drag returns in 200 ms `easing-standard` and immediately under reduced motion ([[Motion]]).

## Accessibility

- Announce the result of a drop politely ("Panel moved to the right dock") once, through the live region or `announce` ([[Accessibility Tree]]).
- The source has a role and a name; the keyboard alternative is documented in its note.
- A dragged state is not colour only: cursor and a layer shape change.

## Dark and light

Roles per scheme.

## Defaults

No drag unless a node starts one; `file_drop` events go to the node under the pointer and the window listener.

## Acceptance criteria

- [ ] AC-DND-1 (scripted input): a node that calls `capture_pointer` on `pointer_down` keeps receiving `pointer_move` after the pointer leaves its box and stops on release or `release_pointer`.
- [ ] AC-DND-2 (scripted input): `start_panel_drag(panel)`, a move over the right zone and a release over it move the panel and fire `dock_drop` with `panel` and `side: right`; a release over no zone changes nothing.
- [ ] AC-DND-3 (scripted input): `dock_panel("right", panel)` moves a docked panel exactly as a drop does (the keyboard path), and a "Move to" command exists for each dockable panel.
- [ ] AC-DND-4 (scripted input): a simulated `file_hover`, `file_drop` with two paths fires one event with both paths on the node under the pointer and on the window listener; `file_hover_cancel` fires when the drag leaves.
- [ ] AC-DND-5 (review): every drag in a project has a keyboard or command alternative, or the audit lists it as failing WCAG 2.2 SC 2.5.7. On Wayland, a file drop has an Open command.
- [ ] AC-DND-6 (pixel check): the dragged source shows the 16 percent dragged layer and cursor `grabbing`; a valid target shows its highlight; both vanish on release or cancel.
- [ ] AC-DND-7 (scripted input): Escape during a drag cancels it, the source returns to its start place and no drop event fires.
- [ ] AC-DND-8 (scripted input): a pointer move of 3 dp after the press does not start a drag and the release is a click; 5 dp starts it.
- [ ] AC-DND-9 (AT tree assertion): after a drop the result is announced once, politely.

## Status in code

| Project | Path | Status per spec |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/docking.py` (`Dock`: zones, `dock_target`, `dock_drop`, `move`, halves), `tess-ui:src/tess_ui/app.py` (`on_file_drop`), `tess-ui:src/tess_ui/widgets/media.py` (node drag, arrow keys) | partly meets: panel drag with a `move` call as non-drag path; node graph drag with arrow keys (meets AC-DND-1); file drop handler exists, not on Wayland; no Escape cancel (fails AC-DND-7, not verified); no content drag and drop; the start distance (`DRAG_THRESHOLD` 4) and the drop highlight (`HIGHLIGHT_ALPHA`, `HIGHLIGHT_OUTLINE` 2) are module constants of `docking.py` with no theme or style hook (project request) |
| tess-shell | `tess-shell:src/tess_shell/surfaces/manager.py` (Movable Panel by `drag_margin`, saved positions), `tess-shell:src/tess_shell/binder/controls.py` (`Slides` drag) | partly meets: Panel Movable, Slider drag and Peek DRAG trigger only; no keyboard way to move a panel (fails AC-DND-5), no content drag and drop; the drag start distance has no key (project request) |
| tre | `tre:docs/guide/events-and-input.md` (Pointer, Files dragged from the OS), `tre:docs/guide/docking.md`, `tre:docs/reference/layer-window.md` (drag by margin), `tre:docs/reference/window.md` | partly meets: capture, docking drag and drop events, file events (not Wayland), margin and window drags; in-app drag and drop is app code; no drag cancel by Escape; no auto-scroll |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Required non-drag alternative for every drag | WCAG 2.2 SC 2.5.7 | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Dragged layer 16 percent, as MD3 | none | [[ADR-0009 State layer percentages]] |

## Sources

- `tre:docs/guide/events-and-input.md`, `tre:docs/guide/docking.md`, `tre:docs/reference/layer-window.md`, `tre:docs/reference/window.md`.
- `tess-ui:src/tess_ui/docking.py`, `tess-shell:src/tess_shell/surfaces/manager.py`.
- WCAG 2.2 SC 2.5.7 Dragging Movements (verified: all functionality that uses dragging can be achieved by a single pointer without dragging): https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html.
- MD3 gestures (JavaScript app #needs-verification): https://m3.material.io/foundations/interaction/gestures.
