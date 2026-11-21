---
title: Volume OSD
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, shell, osd, panel, overlay]
related: ["[[Panel and Surface]]", "[[Popup]]", "[[Launcher]]", "[[Bar]]", "[[Volume OSD|On-Screen Display]]", "[[Audio Module]]", "[[Progress Indicator|Progress Bar]]", "[[Snackbar]]", "[[Frame#Anatomy|Input Region]]", "[[Layer Window]]", "[[12 Overlays#Motion and reduced motion|Surface Animation]]", "[[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]", "[[12 Overlays]]", "[[14 Accessibility Basics]]", "[[Colour Roles]]", "[[Shape]]", "[[Elevation]]", "[[Motion]]", "[[Iconography]]", "[[Spacing and Density]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0007 Icon set and Material Symbols deviation]]"]
---

# Volume OSD

> [!info] Summary
> The Volume OSD is a small card that shows an icon, the output's name, a bar and the percentage (or "Muted") for a moment when the default output's volume or mute changes, then hides itself. It is the `Volume_OSD` module in a click-through Panel on the overlay layer. Tesserae-only element; the nearest Material Design 3 pattern is the [Snackbar](https://m3.material.io/components/snackbar/overview) (a transient, non-modal message that goes away on its own), with a linear [progress indicator](https://m3.material.io/components/progress-indicators/overview) inside. Source of truth in code: see Status in code.

The OSD is not an MD3 element. A snackbar tells the user the result of an action and may carry one action; the OSD only reflects a state the user just changed with a key. It has no action, takes no keyboard and no pointer, and says nothing aloud itself.

## Purpose

Confirm a volume or mute change that the user made with a hardware key or a slider, without taking focus and without covering controls.

## When to use and not

- Use when: a system value changes through a key or another program and the user needs a glance of feedback (volume, mute).
- Do not use when: the user must act or confirm ([[Dialog]]); the message needs to stay until read ([[Snackbar]]); the value is permanent status ([[Audio Module]] in a [[Bar]]); the surface needs input (a [[Popup]] or Panel).
- Brightness and other values are not specified: no brightness service exists.

## Anatomy

1. Panel: floating, anchored to the bottom edge with an inset of 80 dp, 300 dp wide and 64 dp high, layer `OVERLAY`, `Keyboard: NONE`, `Input_Region: []`, `Visible: false`.
2. Container: fill `surface_container` (shell `$color.surface_raised`), corner radius 12 dp, shadow.
3. Icon: 24 dp glyph chosen by level; a crossed speaker when muted.
4. Output name: 12 dp muted text above the bar; optional (`show_name`).
5. Bar: a progress bar from 0 to 100, full width of its column; dimmed to 40 percent opacity when muted.
6. Readout: 16 dp, weight 600, 64 dp wide, end-aligned: "45 %" or "Muted".

## Variants

| Variant | Use | Differences |
|---|---|---|
| With name | Default | `show_name: true` shows the output's name above the bar |
| Without name | Tighter card | `show_name: false` |
| Muted | Mute on | crossed speaker icon, the word "Muted", bar at 40 percent opacity |

## States

| State | Visual change | Token values |
|---|---|---|
| Hidden | Surface kept mapped, draws nothing, takes no input | not applicable |
| Shown | Card drawn; timer `duration` runs | container `surface_container`, elevation 20 percent |
| Level change while shown | Bar and readout update; the timer restarts | bar animates its width ([[Progress Indicator|Progress Bar]]) |
| Muted | icon shape, word "Muted", bar at 0.4 opacity | three cues, none by colour alone |

There is no hover, focus or pressed state: the card is click-through and never focused.

## Tokens used

| Part | Role or token |
|---|---|
| Container | `surface_container` (shell `$color.surface_raised`) |
| Shape | `medium` 12 dp (shell literal) |
| Elevation | level 2 (shell `Elevation: 20%`) |
| Output name | `on_surface_variant`, 12 dp (`body-small`) |
| Readout | `on_surface`, 16 dp weight 600 |
| Bar fill / track | `primary` / `outline`, pill shape (`full`) |
| Icon | `on_surface` ([[Iconography]]) |
| Scrim | none |
| Motion | bar width transition; the show and hide `Animation` is optional |

Roles and shell mapping: [[Colour Roles]]. MD3 Snackbar uses `inverse_surface`, `inverse_on_surface`, level 3 and shape `extra_small` (verified in Sources); the OSD does not, see Deviations.

## Sizing and density

| Item | Value |
|---|---|
| Card | 300 by 64 dp, bottom inset 80 dp, centred horizontally |
| Padding | 16 dp left and right, 8 dp top and bottom |
| Gaps | 12 dp between icon, body and readout; 6 dp between name and bar |
| Content width | 268 dp: icon 24, gap 12, body 156, gap 12, readout 64 |
| Icon | 24 dp |
| Bar height | 8 dp (the shell progress bar is a 160 by 8 pill; here 100 percent of the body) |

The card is a display, not a control, so it does not follow the density levels; it scales with the window scale factor. It has no interactive part, so the 24 dp target size does not apply (WCAG 2.2 SC 2.5.8 covers pointer targets).

## Dimensions and defaults

The card is a display, not a control: it does not follow the density levels, so the three columns hold the same values. Card size, paddings, gaps and the readout weight are Tesserae design choices recorded as built, proposed in the ADR "Shell surface dimensions" #needs-verification-as-design-choice.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| card | height | `Height` | 64 | 64 | 64 | [[Volume OSD#Sizing and density]], design choice, proposed ADR Shell surface dimensions | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height of the Panel); tre: yes (size of the LayerWindow) |
| card | min width | `Width` | 300 | 300 | 300 | [[Volume OSD#Sizing and density]], design choice, proposed ADR Shell surface dimensions | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width of the Panel); tre: yes (size of the LayerWindow) |
| card | padding | `space.3`, `space.5` | 8 16 8 16 | 8 16 8 16 | 8 16 8 16 | [[Volume OSD#Sizing and density]], design choice, proposed ADR Shell surface dimensions | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Padding); tre: yes (padding) |
| card | margin | `Inset` | 0 0 80 0 | 0 0 80 0 | 0 0 80 0 | [[Volume OSD#Defaults]] (bottom inset 80) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Inset of the Panel); tre: yes (margin of the LayerWindow) |
| card | gap | `space.4` | 12 | 12 | 12 | [[Volume OSD#Sizing and density]] (between icon, body and readout) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Spacing); tre: yes (gap) |
| body | gap | - | 6 | 6 | 6 | [[Volume OSD#Sizing and density]] (between name and bar; off the spacing steps), design choice, proposed ADR Shell surface dimensions | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Spacing); tre: yes (gap) |
| bar | height | - | 8 | 8 | 8 | [[Volume OSD#Sizing and density]] (MD3 linear progress track is 4) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height); tre: yes (height) |
| readout | min width | - | 64 | 64 | 64 | [[Volume OSD#Layout and overflow]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Width); tre: yes (min_width) |
| card | border width | - | 0 | 0 | 0 | [[Volume OSD#Tokens used]] (no border) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Width in the Panel Style); tre: yes (border_width) |
| card | border color | - | N/A: the card draws no border | N/A: same as default | N/A: same as default | [[Volume OSD#Tokens used]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Border_Color in the Panel Style); tre: yes (border_color) |
| card | corner radius | `shape.medium` | 12 | 12 | 12 | [[Shape]], [[Volume OSD#Tokens used]] (shell literal 12) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius in the Panel Style); tre: yes (corner_radius) |
| bar | corner radius | `shape.full` | 4 | 4 | 4 | [[Shape]] (pill, half of the 8 dp height) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Corner_Radius); tre: yes (corner_radius) |
| output name | font | `body_small` | 12/16/400/0.4 | 12/16/400/0.4 | 12/16/400/0.4 | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| readout | font | `title_medium` | 16/24/600/0.15 | 16/24/600/0.15 | 16/24/600/0.15 | [[Volume OSD#Tokens used]] (weight 600 is off the scale: `title_medium` is 500), design choice, proposed ADR Shell surface dimensions | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| level icon | icon size | - | 24 | 24 | 24 | [[Volume OSD#Sizing and density]], [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| card | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]] (shell `Elevation: 20%`) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation in the Panel Style); tre: yes (shadows) |

## Layout and overflow

- The output's name ends in an ellipsis at the body width; it never wraps and never paints outside the container ([[10 Layout Overflow and Scrolling]]).
- The readout is fixed at 64 dp and end-aligned so the bar does not change width as the digits change; "100 %" and "Muted" fit.
- Single-line text is vertically centred in the card row: the icon, body and readout are centred on the card's middle line (Align_Items centre).
- The card is placed 80 dp above the bottom edge of the output, centred horizontally, as an overlay; it does not reserve space.

## Behaviour

- Trigger: the module follows the sound server (`ctx.audio`) and shows its Panel when the default output's volume or mute changes (`ctx.surface.show`). It then hides the Panel `duration` milliseconds after the last change; a change in that time restarts the time.
- Silent cases: nothing shows at start, for the first reading of the server, after a server restart, for a switch of the default output (the new output is a silent baseline), or for a change of the microphone or of the list of outputs.
- Pointer: none; `Input_Region: []` makes the whole Panel click-through; a press anywhere reaches the window below.
- Keyboard: none; the Panel never takes the keyboard (`Keyboard: NONE`), so typing in another window is not interrupted.
- Touch: none.
- Placement: an overlay above windows and above bars. Whether it shows above the Plasma panels on KWin is not checked (hand check pending, see the shell vault).
- Fullscreen: a fullscreen window covers the OSD unless the shell offers an opt-out; the shell vault leaves open whether an OSD can show over a fullscreen game.
- Multi-monitor: the Panel belongs to the Monitor that holds it; a volume change shows it on that monitor only.

## Tooltip and overlay behaviour

No tooltip: the card has no control ([[Tooltip]]). It is a transient overlay, not modal, with no scrim, no focus and no dismissal by the user; it dismisses itself ([[12 Overlays]], [[12 Overlays#Dismissal|Dismissal]]).

## Motion

- The bar animates its width on a change (a progress bar transition, 100 ms [[Motion]] `short2` is the shell's `short` duration).
- Show and hide: none by default (the Panel appears and hides at once). A Panel `Animation { Type: FADE, Duration: 200 }` may be added ([[12 Overlays#Motion and reduced motion|Surface Animation]]).
- Reduced motion: show, hide and the bar transition are instant; the display time `duration` is unchanged.
- The card stays on screen for `duration` (1500 ms default) after the last change.

## Accessibility

- Role and name: the card is a group named "Volume, {output}, <45 %|muted>" that holds a progress bar named "Volume" with a value of 0 to 100; the icon and the two texts are hidden from assistive technology because the group's name says what they say.
- It is not a live region. The Audio module's `announce` parameter speaks the change through one window of the shell, so a screen reader hears it once ([[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]; whether Orca reads an unfocused window is untested).
- Muted is shown by the icon's shape, by the word "Muted" and by the dimmed bar, never by colour alone (WCAG 2.2 SC 1.4.1).
- Contrast: readout `on_surface` and name `on_surface_variant` on the container at least 4.5 to 1 (the shell pairs are 13.23 and 7.08 in dark, 16.46 and 7.20 in light); the bar fill `primary` on the container at least 3 to 1 (5.12 dark, 5.69 light, 11.29 high contrast). The track `outline` on the container is 2.69 (dark), 3.63 (light) and 21.00 (high contrast): the dark track is below 3 to 1, which is accepted because the value is also given as text (the readout); WCAG 2.2 SC 1.4.11 asks 3 to 1 for graphics needed to understand the content.
- Display time: the card is a status message of a change the user caused; the same value is available in the Audio module and by keyboard ([[14 Accessibility Basics]]). The time is an author setting from 0 to 60000 ms (WCAG 2.2 SC 2.2.1 applies to time limits on content the user needs to read; a user who needs longer sets `duration`).
- Targets: not applicable, no interactive part.

## Dark and light

The container, text, bar and icon resolve from the scheme; the shipped theme's `surface_raised` is `#1B222B` in dark and `#FFFFFF` in light. The module's own classes set only type size, weight and the muted colour; the colours of the bar come from the Default stylesheet, so a shell with no stylesheet key gets them through ADR-0022's fallback (owner feedback S1, [[Owner Feedback 2026-11-20]]).

## Defaults

| Setting | Default |
|---|---|
| `duration` | 1500 ms (0 to 60000) |
| `show_name` | `true` |
| Panel | `Layer: OVERLAY`, `Keyboard: NONE`, `Input_Region: []`, `Visible: false`, `Anchor: [BOTTOM]`, `Inset: [0, 0, 0, 80]`, `Width: 300`, `Height: 64` |
| Style | `Background: $color.surface_raised`, `Corner_Radius: 12`, `Elevation: 20%` |
| Where | not shipped as a Panel: the user writes the Panel (the guide shows the example) |

## Acceptance criteria

Check types follow [[Test Method]]. Hand checks follow the shell's hand-check kit.

- [ ] AC-OSD-1 (token test, Panel): the guide's Panel for the module has `Layer: OVERLAY`, `Keyboard: NONE`, `Input_Region: []`, `Visible: false`, `Anchor: [BOTTOM]`, `Inset: [0, 0, 0, 80]`, `Width: 300`, `Height: 64` and a `Background` role. Pass: 8 of 8 equal; the loader accepts it with 0 warnings.
- [ ] AC-OSD-2 (scripted input, trigger and time): a volume change from 40 to 45 shows the Panel within 1 frame, the readout reads "45 %", and the Panel hides at 1500 ms (one frame tolerance) after the change; a second change at 1000 ms keeps it shown and hides it at 2500 ms. Pass: show and hide times as stated.
- [ ] AC-OSD-3 (scripted input, silent cases): with each of these events nothing shows: server start, the first reading, a server restart, a switch of the default output, a microphone volume change, a change of the list of outputs. Pass: Panel show count 0 for 6 of 6 events.
- [ ] AC-OSD-4 (scripted input, mute): a mute change shows the Panel with the crossed-speaker icon, the readout "Muted" and the bar at opacity 0.4 (±0.02); a change back shows the level icon and the bar at 1.0. Pass: icon id, readout text and opacity as stated.
- [ ] AC-OSD-5 (scripted input, click-through and keyboard): with the OSD shown, a pointer press on the card reaches the window below (handler count 1 below, 0 on the card) and a key press reaches the previously focused window; the Panel's keyboard-gained event count is 0. Pass: counts as stated.
- [ ] AC-OSD-6 (geometry check, layout): at scale 1.0, 1.25 and 2.0 the card is 300 by 64 dp, the icon 24 by 24 dp, the content padding 16 dp horizontally and 8 dp vertically, the gaps 12 dp (and 6 dp between name and bar), the readout 64 dp wide, the bar 8 dp high and 156 dp wide with the name shown; the card's bottom edge is 80 dp above the output's bottom edge and its centre is the output's horizontal centre (±1 dp). Pass: equal to the dp. Placement relative to a bottom Bar is a hand check.
- [ ] AC-OSD-7 (geometry check, overflow): an output name of 200 characters ends in an ellipsis and ends within the body width; the readout does not change width between "5 %", "100 %" and "Muted"; no glyph lies outside the container. Pass: ellipsis present; readout width constant (±0); 0 pixels outside.
- [ ] AC-OSD-8 (AT tree assertion): the root is a group named "Volume, {output}, <45 %>" (or "muted"); it holds one progress bar named "Volume" with value 45 and maximum 100; the icon and the two texts are hidden; no live region is present on the module. Pass: tree equals the description.
- [ ] AC-OSD-9 (scripted input, announce once): one volume change produces exactly one polite announcement (from the Audio module) and none from the OSD. Pass: announcement count 1 with the OSD present; politeness polite.
- [ ] AC-OSD-10 (contrast script): `on_surface` and `on_surface_variant` on `surface_container` reach 4.5 to 1, and `primary` on `surface_container` reaches 3 to 1, in dark, light and high contrast. Pass: 9 of 9 pairs (computed from the shipped theme: all pass).
- [ ] AC-OSD-11 (pixel check, muted not by colour alone): in a screenshot with mute on, a version of the frame converted to grey scale still differs from the level frame at the icon region (more than 5 percent of its pixels differ) and shows the word "Muted". Pass: both conditions true.
- [ ] AC-OSD-12 (scripted input, reduced motion): with reduced motion on, show and hide reach the end state on the next frame and the bar width reaches its value on the next frame; the display time is unchanged. Pass: end states on frame 1; hide at 1500 ms.
- [ ] AC-OSD-13 (scripted input, params): `duration: 0` is accepted and hides the Panel at once after showing; `duration: 60001` is a load error; `show_name: false` removes the name text. Pass: results as stated.
- [ ] AC-OSD-14 (scripted input, hand check on KWin): on a real KWin 6 session the card shows above a maximised window and above a Plasma panel at its place, and a click on it reaches the window below. Pass: three observations true (recorded by the checker with date). Not yet checked.
- [ ] AC-OSD-15 (token test, no literals): the module's colours are roles or tokens; the only literal in the module style is the opacity 0.4 of the muted bar. Pass: 0 literal colours.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/shipped/Volume_OSD/Volume_OSD_Module.tdl`, `Volume_OSD_Style.tdl`, `Volume_OSD_Module.py`, `tess-shell:docs/guide/modules.md#volume_osd`, `tess-shell:docs/guide/surfaces.md#panel` | Partly meets. Meets AC-OSD-1 to AC-OSD-5, AC-OSD-8, AC-OSD-9, AC-OSD-13 in design (25 module tests reported in the shell vault, not run here; four deliberate breaks each caught). Not run on a real compositor: AC-OSD-14 (look, layer above the Plasma panels, click-through). AC-OSD-6 and AC-OSD-7 not measured. AC-OSD-10 passes by the computed pairs. AC-OSD-15: the 0.4 opacity is a literal in the module; the bar colours come from the Default stylesheet. Not shipped as a Panel: the user writes it (decided as built, owner decision pending on a one-line enabler). |
| shell vault | `shell-vault:40 Specifications/Modules/Volume OSD Module.md` | Source design, status review; its example Panel is 260 by 60, the module comment and guide use 300 by 64: this note follows the module. |
| tess-ui | not applicable | tess-ui has a [[Snackbar]] for application windows; no OSD. |
| tess-shell | `tess-shell:src/tess_shell/shipped/Volume_OSD/Volume_OSD_Style.tdl` (dimensions) | Dimension difference: the readout is 16 dp weight 600, off the type scale (`title_medium` is weight 500); the table keeps 600 as built, pending the proposed ADR. |
| tre | `tre:docs/reference/layer-window.md` | Mechanism only: `LayerWindow` on `overlay`, `input_region=[]`, `keyboard="none"`. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Container `surface_container`, level 2, shape 12 dp (MD3 Snackbar `inverse_surface`, level 3, shape 4 dp) | the shell's one raised surface colour serves every card; the OSD is a card, not an inverted message | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| No action and no dismiss control (MD3 Snackbar has an optional action and close) | the OSD only reflects a state change | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Auto-hide 1500 ms, restarted by each change | a volume key can repeat; MD3 Snackbar durations are presets #needs-verification | none (shell design) |
| Click-through and no keyboard | it must not take input from the windows below | none (shell design) |
| Icons from the Material Design Icons set | project icon set | [[ADR-0007 Icon set and Material Symbols deviation]] |

## Sources

- Snackbar tokens: container `inverse_surface`, text `inverse_on_surface`, level 3, shape `corner-extra-small`, single-line height 48 px, two-line 68 px: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-snackbar.scss (verified 2026-11-21). Snackbar duration presets named without numbers: https://github.com/material-components/material-components-android/blob/master/docs/components/Snackbar.md (#needs-verification for ms values).
- Shape scale: https://github.com/material-components/material-web/blob/main/tokens/versions/v0_192/_md-sys-shape.scss.
- WCAG 2.2 SC 1.4.1 Use of Color: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html ; SC 1.4.3 and 1.4.11: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html , https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html ; SC 2.2.1 Timing Adjustable: https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html ; SC 4.1.3 Status Messages: https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html.
- Shell: `shell-vault:40 Specifications/Modules/Volume OSD Module.md`, `shell-vault:40 Specifications/Surfaces/Panel.md`; `tess-shell:src/tess_shell/shipped/Volume_OSD/`, `tess-shell:docs/guide/modules.md#volume_osd` (origin/main, 2026-11-21). Contrast pairs computed for this note from the shipped theme values (`primary`, `outline`, `surface_raised`) with the WCAG formula.
