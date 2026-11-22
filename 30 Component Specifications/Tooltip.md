---
title: Tooltip
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, overlay, tooltip, owner-feedback]
related: ["[[12 Overlays]]", "[[Popup]]", "[[Owner Feedback 2026-11-20]]", "[[Scrollbar and Scroll Container]]", "[[Form Row]]", "[[Switch]]", "[[Icon Button]]", "[[Colour Roles]]", "[[Elevation]]", "[[Shape]]", "[[Typography]]", "[[Spacing and Density]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0004 Tooltip rule]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0009 State layer percentages]]"]
---

# Tooltip

> [!info] Summary
> A tooltip names or explains one control when the pointer rests on it or keyboard focus reaches it. The Material Design 3 counterparts are the plain tooltip (a short label) and the rich tooltip (subhead, text, actions), both listed under [Tooltips](https://m3.material.io/components/tooltips/overview) (page is a script-rendered app and was not readable here; values below come from the sources named in the Sources section). This note implements [[ADR-0004 Tooltip rule]] completely and is the reference for owner feedback F2, F8 and F9 ([[Owner Feedback 2026-11-20]]). Source of truth in code: see the last section.

## Purpose

A tooltip gives the name or a short explanation of one control (icon button, switch, label, reset button) without taking room in the layout. It is a hint, never the only place where information lives.

## When to use and not

- Use when: a control has no visible text (icon button) and needs a name; a control needs one extra sentence of explanation that the label does not carry; the text is short.
- Do not use when: the information is required to operate the control (put it in the label, [[Form Row]] helper text or [[Text Field]] supporting text); the content has interactive parts beyond one or two actions (use a [[Popup]] flyout or [[Dialog]]); the content is an error or a status that must be seen without hovering.
- Do not put a tooltip on a row, group, panel or container. The trigger is the smallest element that carries the label, icon, switch, button or reset (ADR-0004, owner feedback F8).

## Anatomy

1. Trigger: the control node that owns the tooltip (a label, an icon, a switch, a button, a reset button). Hover over any descendant of the trigger counts as hover over the trigger.
2. Container: opaque rounded rectangle, always drawn with the text.
3. Subhead (rich only): one line.
4. Supporting text: wraps at the maximum width.
5. Actions (rich only): at most two text buttons.
6. Gap: 4 dp between trigger edge and container edge.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Plain | Names a control or states one short fact | Container `inverse_surface`, text `inverse_on_surface`, no shadow, hoverable for 150 ms grace (ADR-0011), never takes focus |
| Rich | One explanation with a subhead and up to two actions | Container `surface_container`, elevation level 2, hoverable for 150 ms grace (ADR-0011), actions reachable by keyboard |

## States

| State | Visual change | Token values |
|---|---|---|
| Hidden | Not in the layer stack, no node in the accessibility tree | not applicable |
| Pending (hover) | Nothing visible; delay timer runs from pointer enter | 500 ms ([[ADR-0004 Tooltip rule]]) |
| Shown | Container and text drawn, opaque | plain: `inverse_surface` / `inverse_on_surface`; rich: `surface_container` / `on_surface_variant` |
| Action hover, focus, pressed (rich action) | State layer in `primary` over the action | 8 percent, 10 percent, 10 percent ([[ADR-0009 State layer percentages]], values verified against `md.comp.rich-tooltip.action.*` tokens, see Sources) |
| Disabled action | Not applicable: a rich tooltip action is never disabled; omit it instead | not applicable |

## Tokens used

| Part | Plain | Rich |
|---|---|---|
| Container colour | `inverse_surface` | `surface_container` |
| Text colour | `inverse_on_surface` | supporting text `on_surface_variant`; subhead `on_surface_variant`; action label `primary` |
| Shape | `extra_small` (4 dp) | `medium` (12 dp) |
| Elevation | level 0 | level 2 (3 dp in MD3 elevation numbers) |
| Type | `body_small` (12/16) | subhead `title_small` (14/20), text `body_medium` (14/20), actions `label_large` (14/20) |

Roles: [[Colour Roles]]. Shape: [[Shape]]. Elevation: [[Elevation]]. Type: [[Typography]]. All values verified in Sources.

## Sizing and density

Tooltip geometry does not scale with the density level ([[Spacing and Density]]); it is the same at `default`, `compact` and `dense`.

| Measure | Plain | Rich |
|---|---|---|
| Minimum height | 24 dp | not specified (content height) |
| Minimum width | 40 dp | not specified |
| Maximum width | 200 dp | 320 dp |
| Horizontal padding | 8 dp | 16 dp |
| Vertical padding | 4 dp | 28 dp from the top edge to the subhead line, 24 dp from the subhead to the first text line, 16 dp below the text, 8 dp below the actions, per Compose M3 constants (see Sources) #needs-verification |
| Action minimum height | not applicable | 36 dp, at least 24 dp pointer target ([[ADR-0002 Desktop density levels and target sizes]]) |
| Gap to trigger | 4 dp | 4 dp |

A tooltip is never a pointer target except a rich tooltip and its actions; the 24 dp minimum target applies to the actions only.

## Dimensions and defaults

Tooltip geometry does not change with density, so the three columns are equal. Plain and rich rows are labelled by part. Maximum width: plain 200, rich 320.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| plain container | min height | - | 24 | 24 | 24 | [[Tooltip]], Sizing and density | tess-ui: no hook; tess-shell: yes (Min_Height); tre: yes (min_height) |
| plain container | min width | - | 40 | 40 | 40 | [[Tooltip]], Sizing and density | tess-ui: no hook; tess-shell: yes (Min_Width); tre: yes (min_width) |
| plain container | height | - | N/A: sized by the text (at least the 24 dp minimum) | N/A: sized by the text | N/A: sized by the text | [[Tooltip]], Layout and overflow | tess-ui: no hook; tess-shell: yes (Height); tre: yes (height) |
| plain container | padding | `space.2`, `space.3` | 4 8 4 8 | 4 8 4 8 | 4 8 4 8 | [[Tooltip]], Sizing and density | tess-ui: no hook; tess-shell: yes (Padding); tre: yes (padding) |
| rich container | padding | `space.5` | 16 16 16 16 | 16 16 16 16 | 16 16 16 16 | [[Tooltip]], Sizing and density (16 horizontal, 16 below the text; the top follows the Compose M3 constants #needs-verification) | tess-ui: no hook; tess-shell: yes (Padding); tre: yes (padding) |
| tooltip | margin | - | N/A: the placement gap to the trigger sets the position, not a margin | N/A: placement gap sets position | N/A: placement gap sets position | [[Anchored Placement]] | tess-ui: no hook; tess-shell: yes (Margin); tre: yes (margin) |
| tooltip | gap | `space.2` | 4 | 4 | 4 | [[Tooltip]], Anatomy part 6 (trigger to container) | tess-ui: no hook; tess-shell: yes (Spacing); tre: yes (gap) |
| tooltip | border width | - | 0 | 0 | 0 | [Material Web plain tooltip tokens](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-plain-tooltip.scss) (no outline token) | tess-ui: no hook; tess-shell: yes (Border_Width); tre: yes (border_width) |
| tooltip | border color | - | N/A: neither tooltip draws a border | N/A: neither tooltip draws a border | N/A: neither tooltip draws a border | [Material Web token file](https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-plain-tooltip.scss)  | tess-ui: no hook; tess-shell: yes (Border_Color); tre: yes (border_color) |
| plain container | corner radius | `shape.extra_small` | 4 | 4 | 4 | [[Shape]] | tess-ui: no hook; tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| rich container | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]] | tess-ui: no hook; tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| plain text | font | `body_small` | 12/16/400/0.4 | 12/16/400/0.4 | 12/16/400/0.4 | [[Typography]] | tess-ui: no hook; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| rich subhead | font | `title_small` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: no hook; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| rich text | font | `body_medium` | 14/20/400/0.25 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]] | tess-ui: no hook; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| rich action | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: no hook; tess-shell: n/a: a shell tooltip holds no action buttons; tre: yes (font_size, font_weight, line_height) |
| rich action | min height | - | 36 | 36 | 36 | [[Tooltip]], Sizing and density (at least the 24 dp target) | tess-ui: no hook; tess-shell: n/a: a shell tooltip holds no action buttons; tre: yes (min_height) |
| tooltip | icon size | - | N/A: a tooltip holds text and text buttons, no icon | N/A: text and text buttons only | N/A: text and text buttons only | [[Tooltip]], Anatomy | tess-ui: n/a: a tooltip holds no icon; tess-shell: n/a: a tooltip holds no icon; tre: n/a: a tooltip holds no icon |
| plain container | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: no hook; tess-shell: yes (Elevation); tre: yes (shadows) |
| rich container | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]] | tess-ui: no hook; tess-shell: yes (Elevation); tre: yes (shadows) |

## Layout and overflow

- Text wraps at the maximum width. Height grows; there is no truncation and no horizontal overflow. Text never extends past the container (the container is sized by the text).
- Placement: `below` the trigger by default, aligned to the trigger start; `above`, `start`, `end` are allowed. When the preferred side lacks room and the opposite side has more, the tooltip flips; then it shifts to stay inside the window. The container always lies completely inside the window (or, in a layer-surface host such as a bar, completely inside the output, see Tooltip and overlay behaviour).
- Corner placements (`top_start`, `top_end`, `bottom_start`, `bottom_end`, `center`) are not flipped and are a tess-ui extension; the spec rule on clipping still holds.
- A tooltip needs no scrollbar: its content is short by definition. Content that would exceed the window height is a sign the content belongs in a [[Popup]] flyout or [[Dialog]].

## Behaviour

- Pointer: the delay timer starts when the pointer enters the trigger (any descendant included) and is cancelled when the pointer leaves it. At 500 ms of continuous hover the tooltip shows. The tooltip is removed 150 ms after the pointer leaves the trigger, unless the pointer enters the tooltip in that time (next item). Pointer press on the trigger removes it and no tooltip shows again until the pointer has left and re-entered the trigger or keyboard focus arrives.
- Plain and rich tooltips are hoverable and persistent ([[ADR-0011 Tooltip hover grace for all tooltips]], WCAG 1.4.13): when the pointer leaves the trigger the tooltip stays open for a grace period of 150 ms; moving the pointer from the trigger onto the tooltip keeps it open, and leaving both the trigger and the tooltip closes it 150 ms after the pointer left the last of them. Pointer events on a tooltip do not reach the element underneath; a tooltip never takes focus. Escape dismisses it without moving the pointer or focus, and it does not show again until the pointer has left and re-entered the trigger or keyboard focus arrives.
- Keyboard: focus that arrives by keyboard (Tab, Shift+Tab, arrow navigation, programmatic focus after a key event) shows the tooltip at once, within one frame. Focus that arrives by mouse click does not. Escape removes it without moving focus. A tooltip shown by focus is removed when focus leaves the trigger. A rich tooltip with actions is reached by Tab from the trigger (see Accessibility).
- Touch: a long press on the trigger shows the tooltip; it is removed after 1500 ms or on the next touch outside it #needs-verification (1500 ms is the Compose M3 non-persistent duration; official MD3 duration not readable).
- One tooltip at a time: showing one removes every other.

## Tooltip and overlay behaviour

This section is the rule set of [[ADR-0004 Tooltip rule]] stated per owner feedback item.

| Owner feedback | Rule | Acceptance criteria |
|---|---|---|
| F2 tooltips do not disappear when hover leaves | Leaving the trigger removes the tooltip within one frame; scroll of any ancestor, pointer press, activation, trigger removed and window focus loss remove it too | AC-TIP-4, AC-TIP-5, AC-TIP-6, AC-TIP-7, AC-TIP-8 |
| F8 tooltip on the whole row, two tooltips, cover the panel, do not go away | Trigger is the control, never a row or container; hovering the label shows only the label's own tooltip, hovering the switch only the switch's; one tooltip at a time | AC-TIP-1, AC-TIP-2, AC-TIP-9 |
| F9 click on the switch drew tooltip text over everything with no background | A tooltip is always opaque and clipped to the window; a mouse click never shows a tooltip; a press removes it | AC-TIP-10, AC-TIP-11, AC-TIP-12, AC-TIP-15 |

Dismissal summary (all within one frame, 17 ms at 60 Hz, after the event is handled): pointer leave of the trigger, Escape, scroll of any ancestor of the trigger (including the window root), pointer press on the trigger, activation of the trigger by keyboard (Enter, Space), removal or hiding of the trigger, window loses focus, another tooltip shows.

Layer route: in an application window the tooltip is a layer over the window content, clipped to the window by the engine. In a layer-surface host (a shell bar) a layer is clipped to the host surface, so a tooltip that does not fit inside the bar uses the popup-window route ([[Popup]]); see AC-TIP-16.

## Motion

No enter or exit animation is required. Where a project animates, enter and exit durations come from [[Motion]] (`short2`, 100 ms is the recommended upper bound; tess-shell ships a 200 ms fade by default, [[ADR-0027 Shell popup and tooltip fade]]; #needs-verification-as-design-choice, MD3 gives no tooltip duration in the sources read). With reduced motion on, the tooltip appears and disappears in one frame ([[Accessibility Rules]]).

## Accessibility

- Role: the container carries no role of its own in the accessibility tree (tess-ui sets `a11y_hidden`); the tooltip text is exposed as the trigger's accessible description, or as its name when the trigger has no label (icon button). A screen reader never needs the layer.
- Keys: Escape dismisses (WAI-ARIA Authoring Practices tooltip pattern: Escape dismisses, focus stays on the trigger, tooltip widgets do not receive focus; see Sources). A rich tooltip with actions: Tab from the trigger moves focus to the first action, Tab moves between actions and leaves the tooltip after the last action to the next control after the trigger, Shift+Tab goes back, Enter or Space runs the action and removes the tooltip, Escape removes the tooltip and returns focus to the trigger.
- WCAG 2.2 SC 1.4.13 Content on Hover or Focus requires dismissible (Escape), hoverable (150 ms grace for all tooltips, [[ADR-0011 Tooltip hover grace for all tooltips]], see AC-TIP-17) and persistent (no auto-removal on hover or keyboard focus; the 1500 ms touch dismissal does not apply to pointer or keyboard).
- Contrast: tooltip text on its container at least 4.5:1 in light and dark (AC-TIP-12); rich tooltip action label `primary` on `surface_container` at least 4.5:1.
- Target size: rich tooltip actions at least 24 dp high and wide.
- Announcements: the tooltip text is not announced as a live region; it is the trigger's description.

## Dark and light

Colours resolve from the active colour scheme ([[Theme Following the System]]). The plain tooltip is the inverse of the surface: light box in the dark scheme, dark box in the light scheme. This is MD3 behaviour, not a bug: the container is opaque, so F1 ("all white except tooltips") concerned the rest of the app, not the tooltip ([[Owner Feedback 2026-11-20]]).

## Defaults

| Setting | Default |
|---|---|
| Hover delay | 500 ms |
| Keyboard focus delay | 0 ms (within one frame) |
| Grace period (plain and rich) | 150 ms |
| Plain max width | 200 dp |
| Rich max width | 320 dp |
| Placement | `below`, flip, shift |
| Gap | 4 dp |

## Acceptance criteria

The fake clock is the frame-driven clock of the toolkit test window (in tess-ui `window.advance(ms)` with `window.simulate(...)`, see `tess-ui:tests/test_overlays.py`). "One frame" is 17 ms at 60 Hz (one `advance(17)`). Layer count is the number of tooltip layers in the layer stack. Test methods follow [[Test Method]].

- [ ] AC-TIP-1 (static check, trigger scope, F8): over every view tree of a project, no node that carries a tooltip has role `group`, `list`, `listitem`, `tree`, `treeitem` (row), `tabpanel`, `dialog` or `menu`, and no node that carries a tooltip has a descendant that carries a tooltip. Pass: zero violations.
- [ ] AC-TIP-2 (scripted input, F8): for a [[Form Row]] with label, switch and reset button, each with its own tooltip text, move the pointer onto the label, wait 600 ms on the fake clock: exactly 1 layer, text equals the label's tooltip. Repeat for the switch and the reset button. Pass: exactly 1 layer each time and the text matches the hovered control. A control without its own tooltip: 0 layers.
- [ ] AC-TIP-3 (scripted input, delay): pointer enters trigger at t0. At t0+499 ms the layer count is 0; at t0+500 ms (plus one frame tolerance, so by t0+517 ms) it is 1. A pointer that leaves at t0+300 ms and stays away for 1000 ms never shows a tooltip.
- [ ] AC-TIP-4 (scripted input, F2): with a tooltip shown, move the pointer out of the trigger and away from the tooltip, advance 149 ms: layer count 1; advance to 150 ms plus one frame: layer count 0 and no tooltip node in the tree. Applies to plain and rich variants (ADR-0011); entering the tooltip within the grace keeps it, see AC-TIP-17.
- [ ] AC-TIP-5 (scripted input, Escape): with a tooltip shown by hover or by keyboard focus, press Escape and advance one frame. Pass: layer count 0, the focused node is unchanged, and with a hover tooltip the pointer position is unchanged (no pointer move needed). The tooltip does not show again until the pointer re-enters or focus re-arrives.
- [ ] AC-TIP-6 (scripted input, scroll, F2): with a tooltip shown for a trigger inside a scroll container, send a wheel event to the container (and separately a scrollbar drag, a Page Down key on the container). Advance one frame. Pass: layer count 0 for each of the three scroll causes.
- [ ] AC-TIP-7 (scripted input, activation): with a tooltip shown, press the pointer on the trigger (pointer down), advance one frame: layer count 0. Then hold the pointer on the trigger for 1500 ms: layer count stays 0. Repeat with keyboard focus and Enter, and with Space: layer count 0 after one frame.
- [ ] AC-TIP-8 (scripted input, lifetime): with a tooltip shown, (a) remove the trigger from the tree, (b) hide the trigger, (c) send window focus loss. Advance one frame after each. Pass: layer count 0 after each.
- [ ] AC-TIP-9 (scripted input, one at a time): move the pointer from trigger A to a non-nested trigger B with A's tooltip shown, sampling the layer count on every frame for 1200 ms. Pass: the count is never greater than 1 on any sampled frame, and after 500 ms on B the only layer is B's. Also: keyboard focus moving from A to B shows B and removes A within one frame.
- [ ] AC-TIP-10 (scripted input, F9): click (pointer down and up) on a switch with the pointer staying in place for 1500 ms. Pass: zero tooltip layers at every sampled frame after the press. Mouse-click focus produces no tooltip; Tab to the switch shows its tooltip within one frame.
- [ ] AC-TIP-11 (pixel check, opaque container, F9): for a plain and a rich tooltip, in light and dark schemes, read the pixel at the container's left padding area (a pixel with no glyph) and at the container's centre-top padding. Pass: both pixels equal the container role colour of the active scheme (`inverse_surface` plain, `surface_container` rich) with alpha 255. A tooltip node whose container fill alpha is below 255 fails.
- [ ] AC-TIP-12 (contrast script): in light and dark schemes, contrast of `inverse_on_surface` on `inverse_surface` at least 4.5:1; of `on_surface_variant` on `surface_container` at least 4.5:1; of `primary` on `surface_container` at least 4.5:1. Pass: all six values meet the ratio.
- [ ] AC-TIP-13 (token test, geometry): plain tooltip container: radius 4 dp, horizontal padding 8 dp, vertical padding 4 dp, min height 24 dp, max width 200 dp, no shadow, type `body_small`, gap to trigger 4 dp. Rich: radius 12 dp, horizontal padding 16 dp, max width 320 dp, elevation level 2, subhead `title_small`, text `body_medium`, action `label_large` in `primary`, action min height 36 dp. Pass: each measured value equals the specified value ±0.5 dp.
- [ ] AC-TIP-14 (geometry check, wrapping): with a text of 400 characters, the plain tooltip width is 200 dp, its height grows, and the text bounding box lies inside the container padding box (no overflow). Pass: container width at most 200 dp (320 dp rich) and text box within container.
- [ ] AC-TIP-15 (geometry check, clipping, F9): place the trigger at each of the four window edges and four corners (trigger 24 dp square touching the edge) and show its tooltip. Pass: the tooltip container rectangle is inside the window rectangle in all 8 cases, and its gap to the trigger is 4 dp when no flip or shift was needed.
- [ ] AC-TIP-16 (geometry check, layer-surface host): for a trigger in a bar window 32 dp high, show a tooltip 24 dp high plus gap that does not fit in the bar. Pass: the tooltip is fully visible (a pixel check at its four corners reads the container colour) and is shown through the popup-window route, not clipped by the bar surface.
- [ ] AC-TIP-17 (scripted input, grace, plain and rich): for each variant, tooltip shown; pointer leaves the trigger and enters the tooltip within 150 ms: layer count stays 1 and stays 1 while the pointer rests on the tooltip. Pointer leaves the trigger and does not enter: layer count 0 by 150 ms plus one frame. Pointer leaves the tooltip: layer count 0 by 150 ms plus one frame. Pointer returning to the trigger within 150 ms keeps the tooltip. A click at a tooltip's position does not reach the element underneath (hit test returns the tooltip node).
- [ ] AC-TIP-18 (scripted input, rich keyboard path): Tab to the trigger of a rich tooltip with two actions; Tab again focuses action 1; Tab focuses action 2; Shift+Tab returns to action 1; Enter on action 1 runs its handler once and removes the tooltip; Escape (in a fresh run) removes the tooltip and focus is on the trigger. Pass: the focused node id after each key equals the expected one and the handler count is 1.
- [ ] AC-TIP-19 (AT tree assertion): for every control with a tooltip, the accessibility tree node has `description` equal to the tooltip text, or `label` equal to it when the control has no other visible or programmatic label. Pass: zero controls without it. A tooltip layer node is `a11y_hidden`.
- [ ] AC-TIP-20 (review): no tooltip carries information that is not available elsewhere (label, description, helper text). Pass: a reviewer finds no violation in the project's tooltip list.
- [ ] AC-TIP-21 (pixel check, scheme): in light and dark schemes the plain tooltip container pixel equals the active scheme's `inverse_surface`, taken from the scheme object, not from a literal. A tooltip drawn with a colour literal fails (token test: zero colour literals in the tooltip builder).
- [ ] AC-TIP-22 (scripted input, touch): long press on a trigger shows the tooltip; with no further touch it is removed at 1500 ms plus one frame; a touch outside it removes it within one frame #needs-verification.
- [ ] AC-TIP-23 (scripted input, reduced motion): with reduced motion on, the first frame after the 500 ms delay draws the tooltip at full opacity and the frame after leave draws none.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/composed.py` (`_wire_tooltips`, `_show_tip`, `_hide_tip`, `TIP_DELAY`, `TIP_GRACE`, `TIP_WIDTH`), `tess-ui:src/tess_ui/overlays.py` (`Tooltip`, `Popover`), `tess-ui:docs/components/tooltips.md`, tests `tess-ui:tests/test_tooltip.py`, `tess-ui:tests/test_overlays.py` | Partly meets. Meets AC-TIP-3 (500 ms, tested), AC-TIP-5 (Escape listener per showing tooltip), AC-TIP-10 only in part (keyboard focus shows at once and `focus_visible` is read, `getattr(event, "focus_visible", True)` defaults to showing when the event lacks the attribute), AC-TIP-11 and AC-TIP-21 in part (fill from the scheme, opaque; the scheme falls back to `tokens.BASELINE` when none). The 150 ms grace (`TIP_GRACE`) exists for rich tooltips only today, so AC-TIP-4 and AC-TIP-17 fail for plain tooltips (plain tooltips are removed on leave and are not hit testable, [[ADR-0011 Tooltip hover grace for all tooltips]]). Fails AC-TIP-1 (the toolkit allows a tooltip on any node; the shipped form puts the doc tooltip on the label box only, the rule is not enforced), AC-TIP-6 (not dismissed on scroll), AC-TIP-7 (pointer press hides, keyboard activation does not), AC-TIP-9 (`_show_tip` does not hide other showing tips; only each node's own leave handler hides its tip, so nested triggers can show two), AC-TIP-13 (one `TIP_WIDTH` 200 for rich as well, rich text 12 not `body_medium` 14, ink `on_surface` instead of `on_surface_variant`, literal fonts and radii not token lookups), AC-TIP-18 (rich actions not reachable by keyboard, documented as not built), AC-TIP-8 in part (trigger removal handled in `_wire_tooltips`; window focus loss not verified), AC-TIP-22 and AC-TIP-23 not verified. Container sizes, padding, gap, radius, fonts and elevation are literals in `_show_tip`, so they have no hook. |
| tess-shell | `tess-shell:src/tess_shell/surfaces/popup.py` (`hover`, `_open_tooltip`, `_arm_exit`), `tess-shell:src/tess_shell/schema/blocks.py` (Popup, Tooltip key), module tooltips in `tess-shell:src/tess_shell/shipped/Clock/Clock_Module.tdl` and five more | Partly meets. Delay 500 ms and exit delay 200 ms (AC-TIP-3 meets the delay; the exit delay of 200 ms differs from the 150 ms grace of [[ADR-0011 Tooltip hover grace for all tooltips]], so AC-TIP-4 and AC-TIP-17 fail until it is 150 ms and the tooltip is hoverable), tooltip is a popup window so it is not clipped by the bar (AC-TIP-16 meets by design, not verified on KWin), `Tooltip` key on any block (AC-TIP-1 not enforced). Absent: keyboard focus path (hover only), Escape, scroll dismissal, press dismissal (decision D64: a tooltip stays open on a press), one-at-a-time is met (one popup at a time, `current`). Card literals repeated in six modules, `Elevation: 20%`, `Corner_Radius: 8`, `surface_raised`; not the plain tooltip look (AC-TIP-13, AC-TIP-21 fail). |
| tre | `tre:docs/reference/layers.md`, `tre:docs/guide/layers.md` (Tooltips and snackbars) | Not applicable as a component: the engine has no tooltip primitive, timers for delay, or placement beyond layer flip and shift. Layers are clipped to the host window; `show_layer(..., dismissible=False)` leaves closing to the app. AC-TIP-1 for a tooltip on a label `Text` needs a tre hook: a text node is not hit-testable today (tre request P2, approved by the Orchestrator 2026-11-21). |

Evidence: [[Owner Feedback 2026-11-20]] F2 (no scroll or leave handling visible in `_wire_tooltips`: leave exists for the trigger node, but nested nodes and scroll do not remove a showing tip), F8 (`pointer_enter` fires per subtree in tre, so a tooltip on a container is entered by hovering any descendant, which is a likely cause of the whole-row tooltips [INFERENCE]; the toolkit does not prevent a tooltip on a row), F9 (the cause of a tooltip text without background is not located in `_show_tip`, which always sets a fill; candidates [INFERENCE]: a mouse-click focus event without `focus_visible` showing a tip at once, a layer not hidden by `_hide_tip`, a stale layer; AC-TIP-10 and AC-TIP-11 pin the required behaviour).

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Hover delay 500 ms | MD3 sources read (Flutter M3 default wait 0 ms, Compose long-press only) give no desktop hover delay; desktop toolkits use about 500 ms and the code already uses it | [[ADR-0004 Tooltip rule]] |
| Tooltip on keyboard focus is shown within one frame | Keyboard users have no hover; matches WAI-ARIA tooltip pattern | [[ADR-0004 Tooltip rule]] |
| Dismiss on scroll, press and activation | WCAG 1.4.13 dismissible; prevents the F2 and F9 symptoms | [[ADR-0004 Tooltip rule]] |
| Grace period 150 ms for plain and rich tooltips | Hoverable condition of WCAG 1.4.13 | [[ADR-0011 Tooltip hover grace for all tooltips]] |
| Rich tooltip actions reachable by Tab | Keyboard access; MD3 describes touch and pointer | [[ADR-0004 Tooltip rule]] |
| Trigger is the control, never a row or group | Owner feedback F8; MD3 has no row-level tooltip, so this is a restriction rather than a deviation | [[ADR-0004 Tooltip rule]] |
| tess-shell fades in 200 ms by default (`short4`), `SLIDE` refused | Fade is the only transition that does not move a compositor-placed popup; the design choice of the shell | [[ADR-0027 Shell popup and tooltip fade]] |

## Sources

- Plain tooltip tokens (container `inverse-surface`, shape `corner-extra-small`, text `inverse-on-surface`, type `body-small`), verified: `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-plain-tooltip.scss` and `.../latest/sass/_md-comp-plain-tooltip.scss`.
- Rich tooltip tokens (container `surface-container`, elevation `level2`, shape `corner-medium`, subhead `title-small` in `on-surface-variant`, supporting text `body-medium` in `on-surface-variant`, action `label-large` in `primary`, action hover, focus, pressed state layers in `primary`), verified: `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-rich-tooltip.scss`.
- Elevation level 2 equals 3 (dp): `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-elevation.scss`. State layer opacities hover 0.08, focus 0.1, pressed 0.1, dragged 0.16, disabled 0.38 (latest): `https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-state.scss` (the older `v0_192` set has focus and pressed 0.12).
- Dimensions (plain min height 24 dp, min width 40 dp, padding 8 by 4 dp, max width 200 dp, rich max width 320 dp, rich horizontal padding 16 dp, action min height 36 dp, gap to anchor 4 dp, non-persistent duration 1500 ms), verified in the Compose Material 3 implementation: `https://github.com/androidx/androidx/blob/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/Tooltip.kt` and `https://github.com/androidx/androidx/blob/androidx-main/compose/foundation/foundation/src/commonMain/kotlin/androidx/compose/foundation/BasicTooltip.kt`. These are an implementation of MD3, not the MD3 spec page. #needs-verification against `https://m3.material.io/components/tooltips/specs`.
- Flutter Material 3 tooltip: wait duration 0, show duration 1500 ms, exit duration 100 ms: `https://github.com/flutter/flutter/blob/master/packages/flutter/lib/src/material/tooltip.dart`.
- WCAG 2.1 SC 1.4.13 Content on Hover or Focus (dismissible, hoverable, persistent): `https://www.w3.org/WAI/WCAG21/Understanding/content-on-hover-or-focus.html`.
- WAI-ARIA Authoring Practices tooltip pattern (Escape dismisses, focus stays on the trigger, tooltip does not receive focus, remains open while the cursor is over the trigger or the tooltip): `https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/`.
- tre layers (placement flip and shift, `dismissible=False`, layer clipped to window): `tre:docs/reference/layers.md`, `tre:docs/reference/layer-window.md`.
- Shell tooltip behaviour (500 ms enter, 200 ms exit, tooltip popup is not focusable): `shell-vault:40 Specifications/Surfaces/Popup.md`.
