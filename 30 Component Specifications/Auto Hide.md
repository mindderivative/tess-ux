---
title: Auto Hide
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, behaviour, shell, bar, auto-hide, not-built]
related: ["[[Bar]]", "[[Frame]]", "[[Peek]]", "[[Frame#Anatomy|Frame Strip]]", "[[12 Overlays#Motion and reduced motion|Surface Animation]]", "[[Auto Hide|Content Fade]]", "[[Frame#Anatomy|Reserved Space]]", "[[Frame#Anatomy|Input Region]]", "[[Keyboard Navigation|Shortcut Mode]]", "[[11 Interaction#Shortcuts and conflicts|Global Shortcuts]]", "[[Keyboard Navigation]]", "[[Popup]]", "[[Top App Bar]]", "[[Panel and Surface]]", "[[12 Overlays]]", "[[Motion]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0006 MD3 baseline with named Expressive adoptions]]", "[[ADR-0002 Desktop density levels and target sizes]]"]
---

# Auto Hide

> [!info] Summary
> Auto hide slides a Bar out past its screen edge after the pointer has left it and brings it back when the pointer touches a thin hover strip on that edge. Tesserae-only behaviour; the nearest Material Design 3 pattern is the Top app bar scroll behaviour (the bar leaves and returns with scrolling, see [Top app bar](https://m3.material.io/components/top-app-bar/overview)). Status: designed and decided, not built; every key is "Not built" in the shell loader. Source of truth in code: see Status in code.

Auto hide is not an MD3 element. The Top app bar hides on scroll and returns on a reverse scroll (Material Components Android `layout_scrollFlags`, `enterAlways`); a desktop Bar hides on pointer absence and returns on pointer presence at the edge. The decisions below are the owner's of 2026-10-27, amended on 2026-11-21 by [[ADR-0021 Shortcut Mode reveals a hidden Bar]].

> [!important] Decision: Shortcut Mode reveals a hidden Bar (OQ-25, closed 2026-11-21, [[ADR-0021 Shortcut Mode reveals a hidden Bar]])
> A hidden Bar is revealed by [[Keyboard Navigation|Shortcut Mode]], a keyboard path with no always-on key: entering the mode shows the Bar and keeps it visible while the mode is active, focus starts where the shell's focus rule 4 says (the Frame or the developer's default focus surface) and `Next_Focus` reaches the Bar; leaving the mode or pressing Escape hides it again per `Auto_Hide` and `Auto_Hide_Delay`; a Bar that holds keyboard focus is not hidden. Plain keys still do not reveal a Bar (`Reveal_Key` default none, 2026-10-27), so [[Accessibility Rules]] AR-9 passes through the mode.

## Purpose

Give the screen back to windows when the Bar is not in use, without moving windows more than once and without losing the way back.

## When to use and not

- Use when: a [[Bar]] is wide or tall enough that the user wants the space back (a top bar on a small laptop screen, a dock).
- Do not use when: the Bar holds status the user must see at a glance without moving the pointer (a battery warning, a recording indicator); a Frame strip should rest as a sliver (use [[Peek]]); the surface is a Panel (use its `Animation` and `Hide_After`, see [[Panel and Surface]]).
- Auto hide acts on Bars. A Frame strip has the same abilities (hidden, collapsed, peeking, animated) and reaches them through [[Peek]]; hiding a plain strip with no `Peek` is not built.

## Anatomy

1. Bar surface: keeps its size; the edge-side margin animates to -(thickness - strip) while hidden.
2. Hover strip: the thin part of the Bar that stays on the screen edge and takes the pointer while the rest is out. Its thickness is open #needs-verification (a strip at the screen edge is reached by pushing the pointer against the edge, so a depth of 1 dp to a few dp suffices).
3. Delay timer: `Auto_Hide_Delay` milliseconds, started when the pointer leaves the Bar.
4. Reserved zone: set to the full zone while the Bar is out, 0 when it is hidden.
5. Reveal paths: pointer on the strip, Shortcut Mode (keyboard, [[ADR-0021 Shortcut Mode reveals a hidden Bar]]), shell actions `Show`, `Hide`, `Toggle` with `Target`.

## Variants

| Variant | Use | Differences |
|---|---|---|
| Slide | Default | the edge margin animates; content fades with the slide |
| Fade | `Animation { Type: FADE }` | opacity only, no margin change |
| None | `Animation { Type: NONE }` or `Duration: 0` | instant |
| Floating Bar (`Gap` above 0) | dock | the gap goes out with the Bar; the zone is 0 while hidden |
| Non-reserving Bar (`Reserve: false` or a layer other than `TOP`) | overlay dock | no zone to release; only the slide |

## States

| State | Visual change | Token values |
|---|---|---|
| Visible | Bar fully shown; zone full | fill `surface` |
| Waiting | pointer left the Bar; delay running; no visual change | `Auto_Hide_Delay` 1000 ms proposed |
| Hiding | margin slides out, content fades | 200 ms ([[Motion]] `short4`) |
| Hidden | only the hover strip is on screen; zone 0; strip takes the pointer | zone 0 |
| Showing | zone set first, margin slides in, content fades in | 200 ms |

## Tokens used

| Part | Role or token |
|---|---|
| Duration | `Animation.Duration`, default 200 ms ([[Motion]] `short4`) |
| Easing | shell `standard`; exit shorter than enter is a Tesserae rule in [[Motion]] (rule 3), not applied here: hide and show use the same duration (decided 2026-10-27, one `Animation`) |
| Delay | `Auto_Hide_Delay` ms |
| Strip | transparent; no role |

Roles of the Bar itself are in [[Bar]].

## Sizing and density

- The Bar keeps its full window size while hidden; a size of 0 never arises, so the Bar's zero-size creation check does not apply.
- Hidden offset: -(thickness - strip) on the edge-side margin; the strip equals the thickness left on screen.
- The hover strip spans the Bar's full length along the edge and is at least 1 dp deep. A hover strip below 24 dp is allowed because the screen edge makes the target effectively unbounded in the pointer's direction and the equivalent keyboard controls exist (WCAG 2.2 SC 2.5.8 exception) #needs-verification.
- Density does not change these values.

## Dimensions and defaults

Auto hide adds no painted part: the Bar keeps its own values ([[Bar]]). The rows give the hover strip and the hidden offset; the strip depth is open #needs-verification-as-design-choice, proposed in the ADR "Shell surface dimensions". Density does not change these values.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| hover strip | height | - | 1 | 1 | 1 | design choice, proposed ADR Shell surface dimensions (minimum depth; a few dp suffices at the screen edge), [[Auto Hide#Sizing and density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (size of the LayerWindow, input_region) |
| hover strip | min height | - | 1 | 1 | 1 | [[Auto Hide#Sizing and density]] (WCAG 2.2 SC 2.5.8 exception) | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (size of the LayerWindow) |
| hover strip | min width | - | N/A: the strip spans the Bar's full length along the edge, so it has no width of its own | N/A: same as default | N/A: same as default | [[Auto Hide#Sizing and density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the strip spans the Bar's length, no width of its own |
| hover strip | padding | - | N/A: the strip is transparent and holds no content | N/A: same as default | N/A: same as default | [[Auto Hide#Tokens used]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the strip is transparent and has no such part |
| Bar | margin | - | N/A: the hidden edge margin is -(thickness - strip), so it depends on the Bar thickness | N/A: same as default | N/A: same as default | [[Auto Hide#Sizing and density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (margin of the LayerWindow, negative accepted) |
| hover strip | gap | - | N/A: the strip has no child parts to space | N/A: same as default | N/A: same as default | [[Auto Hide#Anatomy]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the strip is transparent and has no such part |
| hover strip | border width | - | 0 | 0 | 0 | [[Auto Hide#Tokens used]] (transparent, no role) | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (border_width) |
| hover strip | border color | - | N/A: the strip is transparent and draws no border | N/A: same as default | N/A: same as default | [[Auto Hide#Tokens used]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the strip is transparent and has no such part |
| hover strip | corner radius | - | N/A: the strip is transparent and draws no shape | N/A: same as default | N/A: same as default | [[Auto Hide#Tokens used]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the strip is transparent and has no such part |
| hover strip | font | - | N/A: the strip shows no text; the Bar's text fades out with the slide | N/A: same as default | N/A: same as default | [[Bar]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the strip is transparent and has no such part |
| hover strip | icon size | - | N/A: the strip shows no icon | N/A: same as default | N/A: same as default | [[Bar]] | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: n/a: the strip is transparent and has no such part |
| hover strip | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] (the shadow margin moves off screen while hidden) | tess-ui: n/a: element absent in tess-ui; tess-shell: n/a: element absent in tess-shell; tre: yes (shadows) |

## Layout and overflow

- While hidden, nothing of the Bar's content is clickable except what lies in the strip; content does not paint outside the strip.
- A Bar with a shadow grows by the shadow margin; while hidden the shadow margin is also moved off screen and the input region shrinks to the strip ([[Frame#Anatomy|Input Region]]).
- Two Bars on one edge hide independently; the compositor orders their zones.

## Behaviour

- Pointer: the pointer leaving the Bar (body and strip, and any popup the Bar opened) starts the delay; the pointer returning before it ends cancels the hide and the next leave starts a full delay; the pointer on the strip while hidden reveals the Bar.
- Hide sequence (decided 2026-10-27): slide the Bar out by animating the edge margin (a negative margin slides it past the edge; the compositor accepts it), then set the exclusive zone to 0 when the slide ends.
- Show sequence: set the zone first, then slide in. Windows reflow once per hide and once per show, not on every frame.
- Keyboard (decided 2026-11-21, [[ADR-0021 Shortcut Mode reveals a hidden Bar]]): `Reveal_Key` default none (2026-10-27; the key was removed from the loader on 2026-11-17 because `Auto_Hide` is not built, and returns with it), so no plain key reveals a Bar. `Enter_Shortcut_Mode` reveals every auto-hidden Bar of the shell and keeps it visible while the mode is active, as it already shows every peek of a Frame; focus starts where the shell's focus rule 4 puts it (the Frame, or the surface the developer set as default focus; with no Frame and no default, the first revealed surface in `Tab_Index` order) and `Next_Focus` moves it to the first focusable module of the Bar ([[Keyboard Navigation|Shortcut Mode]]). `Exit_Shortcut_Mode` or Escape hides the Bar again after `Auto_Hide_Delay`. A Bar that holds keyboard focus is not hidden while it holds it.
- Actions: `Show`, `Hide`, `Toggle` with `Target: <Bar name>` reveal and hide a Bar and are also reachable from a global shortcut ([[11 Interaction#Shortcuts and conflicts|Global Shortcuts]]).
- Open popup: proposed: while a Popup opened from a module of the Bar is open, the Bar stays out; the delay starts when the popup closes ([[Popup]]).
- Fullscreen: a fullscreen window covers the Bar; the hover strip takes no input while a fullscreen window is active on the monitor.
- Multi-monitor: each Bar hides on its own monitor; the zone of the others is unchanged.
- Touch: no hover; a touch context shows the Bar, or reveals it by an edge swipe (not specified; no touch shell target).

## Tooltip and overlay behaviour

A hidden Bar shows no tooltip. A tooltip or popup opened from a module while the Bar is out keeps it out (proposed above); both are separate surfaces ([[Tooltip]], [[Popup]]).

## Motion

- Hide and show use the Bar's `Animation` (type `SLIDE` or `FADE`, `Duration` 200 ms); content fades with the slide by default ([[Auto Hide|Content Fade]]).
- A margin animation is one small commit per step with no buffer change; the zone is set once at the start of a show and once at the end of a hide ([[12 Overlays#Motion and reduced motion|Surface Animation]]).
- Reduced motion: hide and show are instant (no slide, no fade); the zone still changes once and windows reflow once.
- A new trigger during an animation replaces it from the current value ([[Motion]] rule 7).

## Accessibility

- A hidden Bar is not in the tab order and its window keeps its accessible name; a reveal by keyboard announces the Bar's name politely and `Next_Focus` moves focus to its first focusable module (initial focus stays where the shell's focus rule 4 puts it).
- A Bar with a recording or warning indicator that must be seen is not hidden: the author does not set `Auto_Hide: true` for it (a design rule of this note, not a WCAG requirement).
- Time limit: the delay is an author setting between 0 and a large value; no content is lost when the Bar hides, so WCAG 2.2 SC 2.2.1 does not apply.
- Reduced motion: see Motion.
- Keyboard path: see Behaviour; Shortcut Mode reveals a hidden Bar, so AR-9 passes ([[ADR-0021 Shortcut Mode reveals a hidden Bar]]).

## Dark and light

No difference; the Bar's colours follow the scheme ([[Bar]]).

## Defaults

| Setting | Default |
|---|---|
| `Auto_Hide` | `false` (owner decision 2026-11-21, [[ADR-0022 Bar Auto_Hide default is off]], supersedes the 2026-10-27 default `true`; an application opts in with `Auto_Hide: true`) |
| `Auto_Hide_Delay` | 1000 ms (proposed, to be tuned in testing) |
| `Reveal_Key` | none (removed from the loader until Auto Hide is built) |
| `Visible` | `true` (starts shown) |
| `Animation` | slide 200 ms |

## Acceptance criteria

Check types follow [[Test Method]]. Criteria AC-AHD-3 to AC-AHD-21 assume a Bar written with `Auto_Hide: true` (the default is off, [[ADR-0022 Bar Auto_Hide default is off]]); AC-AHD-1 and AC-AHD-2 check the default. All criteria currently fail because the feature is not built; the table in Status in code gives the per-key state.

- [ ] AC-AHD-1 (token test, default): a Bar written without `Auto_Hide` has `Auto_Hide` false and `Auto_Hide_Delay` 1000; `Auto_Hide: true` turns the behaviour on and leaves the delay at 1000. Pass: values equal in the shell schema export.
- [ ] AC-AHD-2 (scripted input, off by default): with no `Auto_Hide` written, or `Auto_Hide: false`, and the pointer away for 60 s the Bar stays visible and the zone is unchanged; with `Auto_Hide: true` the same scenario hides it after the delay. Pass: Bar state visible; zone equal.
- [ ] AC-AHD-3 (scripted input, delay): with the pointer leaving the Bar at t = 0, for a Bar with `Auto_Hide: true` the slide starts at 1000 ms (one frame tolerance) by default and at 3000 ms with `Auto_Hide_Delay: 3000`; the pointer returning at 900 ms cancels the hide and the next leave starts a full delay. Pass: start times as stated.
- [ ] AC-AHD-4 (geometry check, hide sequence): during the hide the Bar window size stays unchanged, the edge margin goes to -(thickness - strip) over 200 ms (±1 frame), the zone is the full zone during the slide and 0 after it. Pass: margin and zone samples as stated; the window origin moves only along the edge's perpendicular.
- [ ] AC-AHD-5 (geometry check, show sequence): on reveal the zone becomes full before the first slide frame and the margin returns to its start value after 200 ms (±1 frame). Pass: zone full at frame 0 of the slide; margin equal at the end.
- [ ] AC-AHD-6 (scripted input, reflow once): a maximised window receives at most one configure event for a hide and at most one for a show. Pass: counts at most 1 and 1.
- [ ] AC-AHD-7 (scripted input, hover strip): while hidden, the input region equals the strip rectangle (full Bar length by the strip depth, ±1 dp); a pointer press 2 dp beyond the strip reaches the window below; a pointer on the strip reveals the Bar within 500 ms. Pass: region size, pass-through and reveal time as stated.
- [ ] AC-AHD-8 (scripted input, no default key): with no `Reveal_Key` written, no global shortcut for the Bar is registered. Pass: registered shortcut count 0 for the Bar.
- [ ] AC-AHD-9 (scripted input, keyboard path, ADR-0021): `Enter_Shortcut_Mode` reveals the hidden Bar and keeps it visible while the mode is active; initial focus is on the Frame (or the developer's default focus surface), and one `Next_Focus` per surface in `Tab_Index` order puts focus on the Bar's first focusable module; `Exit_Shortcut_Mode` returns focus to the previous window and restarts the delay. Pass: Bar visible within 300 ms of the mode key; the focus owner right after entering is the Frame, not the Bar; after the `Next_Focus` presses the focus owner is the Bar's first focusable module. Hand check on KWin for the mode's keyboard.
- [ ] AC-AHD-10 (scripted input, focus holds the Bar, ADR-0021): while the Bar holds the keyboard it does not hide, whatever the delay; it hides after the delay once focus leaves. Pass: state visible for 5 s with focus; hiding begins after the delay.
- [ ] AC-AHD-11 (scripted input, popup holds the Bar, proposed): with a Popup from a Bar module open and the pointer in the popup, the Bar stays out; closing the popup starts the delay. Pass: Bar state visible until delay after close.
- [ ] AC-AHD-12 (scripted input, actions): `Hide`, `Show` and `Toggle` with `Target: <Bar name>` hide and show it with the same sequences as the pointer. Pass: states as stated.
- [ ] AC-AHD-13 (scripted input, reduced motion): with reduced motion on, hide and show reach the end state on the next frame with no intermediate margin value and no opacity between 0 and 1; the zone changes once. Pass: sampled margins are the start and end values only.
- [ ] AC-AHD-14 (pixel check, content fade): at slide progress 0.5 the content opacity is 0.5 (±0.05); with `Content_Fade: false` it is 1. Pass: opacities as stated.
- [ ] AC-AHD-15 (scripted input, multi-monitor): hiding the Bar on monitor 1 leaves monitor 2's Bar and zone unchanged. Pass: monitor 2 state and zone equal.
- [ ] AC-AHD-16 (scripted input, fullscreen): while a fullscreen window is active on the monitor, a pointer at the edge reveals nothing and the hover strip takes no input. Pass: Bar state hidden; press reaches the fullscreen window.
- [ ] AC-AHD-17 (pixel check, idle): a hidden Bar with no module update commits 0 frames over 5 s. Pass: frame count 0.
- [ ] AC-AHD-18 (scripted input, live change): a reload that sets `Auto_Hide: false` on a hidden Bar shows it and restores its zone in one step. Pass: Bar visible and zone full after the reload frame.
- [ ] AC-AHD-19 (AT tree assertion): a hidden Bar's modules are not in the tab order; after a keyboard reveal the Bar's name is announced politely once. Pass: tab order count 0 while hidden; announcement count 1.
- [ ] AC-AHD-20 (scripted input, Escape and leaving the mode, ADR-0021): with the Bar revealed by Shortcut Mode, Escape and `Exit_Shortcut_Mode` each start the delay and the Bar hides after `Auto_Hide_Delay` (1000 ms by default, one frame tolerance); with `Auto_Hide: false` it stays visible. Pass: hide start times as stated.
- [ ] AC-AHD-21 (scripted input, plain keys do not reveal, ADR-0021): with the Bar hidden and no mode active, a press of each of 20 plain keys (letters, digits, Tab, Enter, arrows) leaves the Bar hidden and the zone at 0. Pass: Bar state hidden after 20 of 20 presses.

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/schema/docs.py` ("Not built" for `Auto_Hide`, `Auto_Hide_Delay`, `Visible` of a Bar, `Animation` of a Bar, `Input_Region` of a Bar), `tess-shell:src/tess_shell/schema/blocks.py` (`Reveal_Key` removed, error `removed-key`), `tess-shell:docs/guide/surfaces.md#bar` ("A Bar cannot be hidden by a command or a shortcut") | Absent for Bars: AC-AHD-1 to AC-AHD-19 fail. The building blocks exist for Frame strips and melded Panels (slide by contour, content fade, reduced motion, `Show`, `Hide`, `Toggle` by name in `surfaces/frame.py`); a strip hides only through `Peek`. The Bar placement function already supports a size that never reaches 0 (`surfaces/bar.py`). |
| shell vault | `shell-vault:40 Specifications/Surfaces/Bar.md` (Auto-hide, decided 2026-10-27), `shell-vault:40 Specifications/Surfaces/Frame.md` | Source design. The vault says on by default; the owner changed that on 2026-11-21 to off by default ([[ADR-0022 Bar Auto_Hide default is off]]). The vault's default delay of 1000 ms is proposed; the hover strip thickness is open. |
| tess-ui | not applicable | Application windows use the [[Top App Bar]] scroll behaviour, outside the shell. |
| tre | `tre:docs/reference/layer-window.md` | Mechanism only: negative margins accepted on KWin and sway, `exclusive_zone` live through `set()`, margin animation, input region. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| Hide on pointer absence and show on pointer presence at the edge (MD3 Top app bar: scroll direction) | a desktop shell has a pointer and no scrolling content under the Bar | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Off by default, opt in with `Auto_Hide: true` | owner decision 2026-11-21: apps opt in; supersedes the earlier default on with opt-out (2026-10-27) | [[ADR-0022 Bar Auto_Hide default is off]] |
| Hide and show take the same duration (MD3 and the Tesserae motion rule: exit shorter than enter) | one `Animation` block for both directions | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| The reserved zone changes once at the end of the hide and the start of the show | a zone change is a configure round trip; animating it would reflow windows on every frame | none (compositor limit) |

## Sources

- Top app bar scroll behaviour (`layout_scrollFlags`, `enterAlways`, lift on scroll), Material Components Android: https://github.com/material-components/material-components-android/blob/master/docs/components/TopAppBar.md (verified 2026-11-21).
- Layer-shell protocol (exclusive zone includes margin; negative margins; anchors): https://wayland.app/protocols/wlr-layer-shell-unstable-v1.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; SC 2.1.1 Keyboard: https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html ; SC 2.3.3 Animation from Interactions: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html.
- Shell: `shell-vault:40 Specifications/Surfaces/Bar.md`, `shell-vault:40 Specifications/Surfaces/Frame.md`, `shell-vault:40 Specifications/Surfaces/Panel.md`; `tess-shell:src/tess_shell/schema/docs.py`, `tess-shell:src/tess_shell/schema/blocks.py`, `tess-shell:docs/guide/surfaces.md#bar` (origin/main, 2026-11-21).
