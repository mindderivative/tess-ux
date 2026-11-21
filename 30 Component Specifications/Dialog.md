---
title: Dialog
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, overlay, dialog, modal]
related: ["[[12 Overlays]]", "[[Scrim]]", "[[Popup]]", "[[Menu]]", "[[Tooltip]]", "[[Button]]", "[[Icon Button]]", "[[Text Field]]", "[[Panel and Surface]]", "[[Scrollbar and Scroll Container]]", "[[Colour Roles]]", "[[Elevation]]", "[[Shape]]", "[[Typography]]", "[[Spacing and Density]]", "[[Focus Ring]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0001 MD3 role names are the specification vocabulary]]"]
---

# Dialog

> [!info] Summary
> A dialog interrupts the current task to ask for a decision or to give needed information; it is modal, drawn on a raised surface over a scrim. Material Design 3 counterpart: [Dialogs](https://m3.material.io/components/dialogs/overview) (basic and full-screen). The shell has no dialog element. Source of truth in code: see the last section.

## Purpose

Get a decision or acknowledgement before anything else can happen, with minimal text and at most a few actions.

## When to use and not

- Use when: the user must confirm a destructive or irreversible step, choose among a few options, or read information that blocks the workflow; the window is compact and a task needs the full window (full-screen form).
- Do not use when: the content is a hint ([[Tooltip]]), a list of commands ([[Menu]]), or transient and non-blocking ([[Popup]], a snackbar); the task has many steps (use a page or a Panel).
- A dialog does not open another dialog.

## Anatomy

1. Scrim: the whole window, `scrim` role at 32 percent ([[Scrim]]).
2. Container: the panel.
3. Icon (optional): 24 dp, `secondary`.
4. Headline: `headline_small`, `on_surface`.
5. Supporting text or content: `body_medium`, `on_surface_variant`.
6. Divider: 1 dp, shown above the actions (and under the headline) only when the content scrolls.
7. Actions: text buttons, right-aligned, dismissive action before confirming action.
8. Full-screen form: header of 56 dp with close icon button, title, and one confirming action; content scrolls beneath.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Basic | Confirmations, short choices | Container `surface_container_high`, shape `extra_large` (28 dp), elevation level 3, centred |
| Alert | Blocks until an action is chosen | Basic with Escape and scrim press disabled; role `alertdialog` where the platform has it |
| Full-screen | Compact windows, multi-field tasks | Container `surface`, shape `none`, elevation level 0, fills the window, header 56 dp |

## States

| State | Visual change | Token values |
|---|---|---|
| Closed | Nothing in the layer stack | not applicable |
| Open | Scrim and container drawn, focus inside | see Tokens used |
| Content scrolled | Divider shown above actions (and below header in full-screen) | divider 1 dp, `outline` |
| Action hover, focus, pressed | State layer `primary` over the action | 8, 10, 10 percent ([[ADR-0009 State layer percentages]]) |

## Tokens used

| Part | Role or token |
|---|---|
| Scrim | `scrim` at 32 percent opacity ([[Scrim]]) |
| Container (basic) | `surface_container_high`, `extra_large` (28 dp), level 3 |
| Container (full-screen) | `surface`, `none` (0 dp), level 0 |
| Icon | `secondary`, 24 dp |
| Headline | `headline_small`, `on_surface` |
| Supporting text | `body_medium`, `on_surface_variant` |
| Actions | `label_large`, `primary` |
| Full-screen header | 56 dp, title `title_large` in `on_surface`, header action `label_large` in `primary` |
| Divider | 1 dp, `outline` |

See [[Colour Roles]], [[Shape]], [[Elevation]], [[Typography]]. Values verified in Sources.

## Sizing and density

- Width: minimum 280 dp, maximum 560 dp; the container stays 24 dp inside the window on every side (maximum height is the smaller of 560 dp and the window height minus 48 dp); minimum height 140 dp. When the window is narrower than 328 dp (280 plus 48) the dialog uses the full-screen form #needs-verification-as-design-choice. Default width 312 dp (tess-ui default) #needs-verification against the MD3 spec page.
- Padding 24 dp on all sides (headline top padding 24 dp, actions row padding 16 dp top, 24 dp sides and bottom, gap between actions 8 dp). These are not density-scaled: dialogs are rare and spacious by design.
- The action buttons follow the density level for height ([[Spacing and Density]]: 40 / 32 / 28 dp), at least 24 dp.
- Full-screen header height 56 dp at every density.

## Dimensions and defaults

Dialog paddings and the 24 dp window inset are not density-scaled (dialogs are rare and spacious by design, [[Dialog#Sizing and density]]); only the action buttons follow the density level. Values for the basic form unless the Part names another form.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| container | height | - | N/A: the content height decides, between 140 and the smaller of 560 and the window height minus 48 | N/A: same as default | N/A: same as default | [[Dialog#Sizing and density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | min width | - | 280 | 280 | 280 | [[Dialog#Sizing and density]] (maximum 560, default 312) | tess-ui: yes (style min_width); tess-shell: n/a: element absent in tess-shell; tre: yes (min_width) |
| container | min height | - | 140 | 140 | 140 | [[Dialog#Sizing and density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| action button | min height | `target.min` | 24 | 24 | 24 | [[Spacing and Density]] | tess-ui: yes (style min_height); tess-shell: n/a: element absent in tess-shell; tre: yes (min_height) |
| action button | height | `density.control_height` | 40 | 32 | 28 | [[Spacing and Density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| full-screen header | height | - | 56 | 56 | 56 | [[Dialog#Sizing and density]] | tess-ui: yes (style height); tess-shell: n/a: element absent in tess-shell; tre: yes (height) |
| container | padding | `space.6` | 24 24 24 24 | 24 24 24 24 | 24 24 24 24 | MD3 [Android Dialog guide](https://github.com/material-components/material-components-android/blob/master/docs/components/Dialog.md); tess-ui `Dialog_Stylesheet.tdl` | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| actions row | padding | `space.5`, `space.6` | 16 24 24 24 | 16 24 24 24 | 16 24 24 24 | [[Dialog#Sizing and density]] | tess-ui: yes (style padding); tess-shell: n/a: element absent in tess-shell; tre: yes (padding) |
| container | margin | `space.6` | 24 24 24 24 | 24 24 24 24 | 24 24 24 24 | [[Dialog#Sizing and density]] (the container stays 24 dp inside the window on every side) | tess-ui: yes (style margin); tess-shell: n/a: element absent in tess-shell; tre: yes (margin) |
| actions | gap | `space.3` | 8 | 8 | 8 | [[Dialog#Sizing and density]] | tess-ui: yes (style gap); tess-shell: n/a: element absent in tess-shell; tre: yes (gap) |
| container | border width | - | 0 | 0 | 0 | MD3 [Android Dialog guide](https://github.com/material-components/material-components-android/blob/master/docs/components/Dialog.md) (the container has no outline) | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| container | border color | - | N/A: the dialog container draws no border; separation is the shadow and the scrim | N/A: same as default | N/A: same as default | [[Elevation]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| divider | border width | `md.comp.divider.thickness` | 1 | 1 | 1 | [[Dialog#Tokens used]] | tess-ui: yes (style border_width); tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| divider | border color | `outline` | `outline` | `outline` | `outline` | [[Dialog#Tokens used]] | tess-ui: yes (style border_color); tess-shell: n/a: element absent in tess-shell; tre: yes (border_color) |
| container (basic, alert) | corner radius | `shape.extra_large` | 28 | 28 | 28 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| container (full-screen) | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]] | tess-ui: yes (style corner_radius); tess-shell: n/a: element absent in tess-shell; tre: yes (corner_radius) |
| headline | font | `headline_small` | 24/32/400/0 | 24/32/400/0 | 24/32/400/0 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| supporting text | font | `body_medium` | 14/20/400/0.25 | 14/20/400/0.25 | 14/20/400/0.25 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| actions | font | `label_large` | 14/20/500/0.1 | 14/20/500/0.1 | 14/20/500/0.1 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| full-screen title | font | `title_large` | 22/28/400/0 | 22/28/400/0 | 22/28/400/0 | [[Typography]] | tess-ui: via type role in the theme; tess-shell: n/a: element absent in tess-shell; tre: yes (font_size, font_weight, line_height) |
| icon | icon size | - | 24 | 24 | 24 | [[Iconography]], [[Dialog#Tokens used]] | tess-ui: via widget icon size; tess-shell: n/a: element absent in tess-shell; tre: yes (width, height of the svg node) |
| container (basic, alert) | elevation | `elevation.level_3` | 3 | 3 | 3 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |
| container (full-screen) | elevation | `elevation.level_0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: yes (style elevation); tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

## Layout and overflow

- The container is centred in the window. Content taller than the container scrolls inside the container (the headline and actions stay fixed) with a visible scrollbar thumb ([[ADR-0003 Scrollbar rule]]); a divider appears above the actions while content is scrolled, and under the headline when content is scrolled away from the top.
- Actions stack vertically when they do not fit on one row (the sum of their widths plus 8 dp gaps exceeds the width minus 48 dp); none overflows the container horizontally.
- Headline and supporting text wrap; text in actions is a single line; long labels truncate with an ellipsis and keep the full accessible name.
- When the window resizes while a dialog is open, the scrim keeps filling the window and the container stays centred and within the limits above.

## Behaviour

- Pointer: a press on the scrim dismisses a dismissible dialog with no result; a press inside the container never dismisses it. Input beneath the scrim (presses, hovers, wheel) reaches nothing.
- Keyboard: on open, focus moves into the dialog (initial focus rule below). Tab and Shift+Tab cycle among the focusable elements of the dialog only; focus never reaches content beneath. Escape closes a dismissible dialog with no result (and returns focus to the opener); on an alert dialog Escape does nothing. Enter on a focused action runs it. Space runs it too.
- Initial focus: the element marked as initial focus; else the first focusable content element (a text field in a form dialog); for a dialog whose confirming action is destructive and not easily reversible, the least destructive action (the cancel action); for an information dialog with no input, the first action. If content is long enough that focusing its first interactive element would scroll the start out of view, focus goes to the dialog title (not tabbable) instead.
- Action order: dismissive action first, confirming action last; actions are aligned to the end edge of the container. The confirming action is the rightmost in left-to-right layouts.
- Result: an action closes the dialog and returns the value of the action; dismissal returns no result.
- Touch: same as pointer; actions have at least 48 dp target in touch contexts ([[ADR-0002 Desktop density levels and target sizes]]).

## Tooltip and overlay behaviour

A dialog is a modal layer: a scrim of its own, one dialog at a time, above every non-modal overlay. Opening a dialog removes any visible tooltip and closes any open [[Popup]]. Tooltips of controls inside the dialog show above it ([[12 Overlays]], z-order). On close, focus returns to the control that was focused when it opened (to the nearest logical element when that control is gone). A dialog does not open from a popup that stays open; the popup closes first.

## Motion

Material Web's default dialog opens with the dialog sliding down 50 px over 500 ms (emphasized easing), the container growing from 35 percent to 100 percent of its height over 500 ms, the scrim fading from 0 to 0.32 over 500 ms (linear), headline and content fading in over 250 ms and actions over 300 ms; it closes with a 150 ms slide up (emphasized accelerate) and a 150 ms scrim fade ([[Scrim]], [[Motion]]). Tesserae takes the scrim timings as they are in [[Scrim]]; the slide and container grow are optional. Tesserae durations are not an MD3 spec value: the figures are the Material Web implementation. With reduced motion on, the dialog and scrim appear and disappear in one frame.

## Accessibility

- Role `dialog`, named by the headline; an alert dialog uses `alertdialog` where the platform has it. tess-ui notes tre has no `alertdialog` role; an alert is then a `dialog` with Escape and scrim press disabled and the description set to the supporting text.
- Modal: content beneath is not focusable and not reachable by assistive technology while the dialog is open (the engine blocks input; whether its nodes are hidden from the accessibility tree is not verified) #needs-verification.
- Focus trap with an exit: Tab is trapped on purpose; Escape and a visible close or cancel action provide the exit (WCAG 2.2 SC 2.1.2 allows the trap because it is escapable). A dismissible dialog always has a visible close control or cancel action.
- Contrast: `on_surface` on `surface_container_high`, `on_surface_variant` on `surface_container_high`, `primary` on `surface_container_high` each at least 4.5:1 in light and dark.
- Announcement: opening a dialog announces its role and name; an alert dialog announces its description too.

## Dark and light

All colours are roles ([[Theme Following the System]]). The scrim is `scrim` at 32 percent in both schemes; the container `surface_container_high` is a lighter surface in dark and a slightly darker surface than `surface` in light.

## Defaults

| Setting | Default |
|---|---|
| Form | basic |
| Width | 312 dp (280 to 560) |
| Scrim | `scrim` at 32 percent |
| Dismissible | yes (Escape, scrim press) |
| Actions | at most 3 text buttons, dismissive before confirming |
| Content height limit | scrolls beyond the available height |

## Acceptance criteria

Scripted input follows [[Test Method]] (toolkit key and pointer simulation, frame clock).

- [ ] AC-DLG-1 (pixel check and token test, pixel and token check, container): basic dialog container pixel equals `surface_container_high` of the active scheme (alpha 255), radius 28 dp, elevation level 3; full-screen: `surface`, radius 0, level 0, size equals the window size.
- [ ] AC-DLG-2 (pixel check, scrim): a window pixel under the scrim equals the underlying pixel blended with `scrim` at 32 percent (±1 per channel) at the four window corners and the centre; after resizing the window by 100 dp both ways, the scrim still covers the whole window.
- [ ] AC-DLG-3 (geometry check, size): requested widths 100, 312, 900 give container widths 280, 312, 560 dp; a window 300 dp wide gives the full-screen form; container edges are at least 24 dp from the window edges and the maximum height is min(560, window height − 48) dp.
- [ ] AC-DLG-4 (geometry check, padding): headline top padding 24 dp, side padding 24 dp, icon 24 dp square in `secondary`, actions row padding 16 dp top and 24 dp bottom and sides, gap between actions 8 dp (±0.5 dp).
- [ ] AC-DLG-5 (token test, type): headline `headline_small` in `on_surface`; supporting text `body_medium` in `on_surface_variant`; action labels `label_large` in `primary`.
- [ ] AC-DLG-6 (scripted input, initial focus): for (a) a form dialog, focus is on the first text field after one frame; (b) a destructive confirmation, focus is on the cancel action; (c) an information dialog, focus is on its first action; (d) a dialog with an element marked initial focus, focus is on it. Pass: focused node id equals the expectation.
- [ ] AC-DLG-7 (scripted input, focus trap): press Tab 30 times and then Shift+Tab 30 times; after each press the focused node is inside the dialog. Pass: 60 of 60.
- [ ] AC-DLG-8 (scripted input, Escape): Escape closes a dismissible dialog with an empty result and focus is on the opener within one frame; an alert dialog stays open on Escape and on a scrim press and closes only on an action.
- [ ] AC-DLG-9 (scripted input, scrim and blocked input): a press on the scrim closes a dismissible dialog; a press on the container does not; while open, a press, a wheel event and a key press aimed at content beneath produce 0 handler calls.
- [ ] AC-DLG-10 (scripted input, action result): pressing an action closes the dialog and delivers that action's value exactly once; dismissal delivers no value.
- [ ] AC-DLG-11 (geometry check, action order and fit): actions are ordered dismissive, then confirming, left to right, right-aligned to the container padding; with actions whose width sum exceeds the available width they stack and none exceeds the container.
- [ ] AC-DLG-12 (scripted input, scrolling): content 1000 dp tall in a 400 dp container scrolls with a visible scrollbar thumb; the headline and actions stay fixed; the divider above the actions is shown while content is scrolled and hidden at the end of the scroll; keyboard focus moves into view.
- [ ] AC-DLG-13 (geometry check, full-screen): header 56 dp tall, close icon button at the start, title `title_large`, one confirming action at the end, content scrolls beneath, divider shown under the header once content is scrolled.
- [ ] AC-DLG-14 (AT tree assertion): the container has role `dialog` (or `alertdialog`), an accessible name equal to the headline, and the supporting text as description; with a dialog open, content beneath is not focusable.
- [ ] AC-DLG-15 (contrast script): the three pairs of Accessibility each at least 4.5:1 in both schemes.
- [ ] AC-DLG-16 (scripted input, focus return and exclusivity): closing returns focus to the opener; opening a dialog while another is open is refused by default, following [[Scrim]] rule 7 (one scrim under the topmost modal; a project spec may allow stacking); a visible tooltip and an open popup are gone within one frame after the dialog opens.
- [ ] AC-DLG-17 (scripted input, motion): with animation on, scrim opacity reaches 0.32 between 500 ms and 533 ms after open and 0 between 150 ms and 183 ms after close ([[Scrim]] AC-SCR-9); with reduced motion on, the first frame after open draws the dialog and scrim at full opacity.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-ui | `tess-ui:src/tess_ui/views/Dialog_View.tdl`, `Dialog_Stylesheet.tdl`, `FileDialog_View.tdl`, `tess-ui:src/tess_ui/overlays.py` (`Dialog`), `tess-ui:src/tess_ui/spec/build.py` (scrim `scrim@32%`), `tess-ui:docs/components/dialogs.md`, tests `tess-ui:tests/test_dialog.py` | Partly meets. Meets AC-DLG-1 (28 px, 24 padding, `surface_container_high`, level 3; full-screen `surface`, 0, 0, tested), AC-DLG-2 (scrim role at 32 percent, follows window size), AC-DLG-3 in part (width held 280 to 560, default 312, tested; no 24 dp window inset and no full-screen switch below 328 dp, the caller chooses with `Fullscreen`), AC-DLG-4 in part (padding 24 and gap 16 between parts rather than 8 and 16 for the actions row), AC-DLG-5, AC-DLG-7 (modal keeps Tab inside), AC-DLG-8 (Escape and scrim press dismiss, `Dismissible: false` ignores them, tested), AC-DLG-9, AC-DLG-10, AC-DLG-11 (stacks when they do not fit), AC-DLG-12 (a line shows above the actions once scrolled, tested; `Max_Height` 480), AC-DLG-13 (56 px bar, tested; allows several actions where MD3 has one confirming action). Fails or not built: AC-DLG-6 (focusing a default action or first field is documented as not built), AC-DLG-14 in part (role `dialog` named by headline; no `alertdialog`; hiding of content beneath not verified). AC-DLG-15, AC-DLG-16 and AC-DLG-17 not verified. |
| tess-shell | none | Absent. The shell has no dialog or modal surface; `Role: DIALOG` and the `$color.scrim` token exist with no consumer. An element would be a Panel on the overlay layer with exclusive keyboard (design note only, not a promise). |
| tre | `tre:docs/reference/layers.md` | Mechanism only: `show_layer(modal=True)` blocks input beneath, moves focus to the layer's first focusable node, keeps Tab inside, delivers `dismiss` on a press outside and on Escape; the engine draws no scrim (a window-sized box inside the layer). |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Several actions allowed in the full-screen header | tess-ui allows `Actions` list there; MD3 has one confirming action | [[Deviations from MD3]] |
| Dialog metrics do not scale with density | Rare, spacious surface; actions still follow density | [[ADR-0002 Desktop density levels and target sizes]] |
| Alert dialog is a `dialog` role where `alertdialog` is missing | Engine limit | [[Deviations from MD3]] |

## Sources

- Dialog tokens (container `surface-container-high`, elevation `level3`, shape `corner-extra-large`, headline `headline-small` in `on-surface`, supporting text `body-medium` in `on-surface-variant`, action label `label-large` in `primary`, action state layers in `primary`, icon size 24 px in `secondary`, divider 1 px in `outline`), verified: `https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-dialog.scss` and `.../v0_192/_md-comp-dialog.scss`.
- Full-screen dialog tokens (container `surface`, elevation `level0`, shape `corner-none`, header height 56 px, header headline `title-large` in `on-surface`, header action `label-large` in `primary`), verified: `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-full-screen-dialog.scss`.
- Scrim token (colour `scrim`, opacity 0.32), verified: `https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-comp-scrim.scss`.
- Layout (min width 280 px, max width and max height `min(560px, 100% - 48px)`, min height 140 px, padding 24 px, headline padding 24 px 24 px 0, actions padding 16 px 24 px 24 px with 8 px gap, right-aligned, dividers on scroll), verified: `https://github.com/material-components/material-web/blob/main/dialog/internal/_dialog.scss`.
- Behaviour (focus trap on by default, `autofocus` attribute selects the initial focus, `cancel` event on scrim click or Escape, alert type): `https://github.com/material-components/material-web/blob/main/docs/components/dialog.md`.
- WAI-ARIA Authoring Practices modal dialog pattern (Tab cycles within, Escape closes, initial focus guidance including least destructive action and a non-tabbable title for long content, focus returns to the invoker, a visible close button): `https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/`.
- WCAG 2.2 Understanding SC 2.1.2 No Keyboard Trap: `https://www.w3.org/WAI/WCAG22/Understanding/no-keyboard-trap.html`.
- The MD3 spec pages (`https://m3.material.io/components/dialogs/specs`) are a script-rendered app and were not readable; the default width 312 dp and the action order come from tess-ui and the Material Web sample markup #needs-verification.
- tess-ui dialog documentation: `tess-ui:docs/components/dialogs.md`, `tess-ui:docs/guide/overlays.md`.
