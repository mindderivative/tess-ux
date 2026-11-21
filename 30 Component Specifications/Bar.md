---
title: Bar
type: component
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-21
tags: [component, surface, shell, bar, layer-shell]
related: ["[[Panel and Surface]]", "[[Popup]]", "[[Frame]]", "[[Auto Hide]]", "[[Peek]]", "[[Launcher]]", "[[Volume OSD]]", "[[Dock]]", "[[Bar#Variants|Vertical Bar]]", "[[Top App Bar]]", "[[Layer Window]]", "[[Frame#Anatomy|Reserved Space]]", "[[Frame#Anatomy|Input Region]]", "[[Keyboard Navigation|Shortcut Mode]]", "[[Keyboard Navigation]]", "[[Tasks Module]]", "[[Workspaces Module]]", "[[Tray Module]]", "[[Clock Module]]", "[[12 Overlays]]", "[[Owner Feedback 2026-11-20]]", "[[Colour Roles]]", "[[Elevation]]", "[[Shape]]", "[[Motion]]", "[[Spacing and Density]]", "[[Accessibility Rules]]", "[[Test Method]]", "[[Deviations from MD3]]"]
depends_on: ["[[ADR-0001 MD3 role names are the specification vocabulary]]", "[[ADR-0002 Desktop density levels and target sizes]]", "[[ADR-0005 Theme follows the system]]", "[[ADR-0006 MD3 baseline with named Expressive adoptions]]"]
---

# Bar

> [!info] Summary
> A Bar is a shell surface attached to one screen edge that reserves space, so maximised windows stop short of it. A top Bar holds the clock, workspaces, tray and system modules; a bottom or side Bar holds a dock or a side bar. Tesserae-only element. The nearest Material Design 3 patterns are the [Top app bar](https://m3.material.io/components/top-app-bar/overview), the [Navigation bar](https://m3.material.io/components/navigation-bar/overview) and the [Navigation rail](https://m3.material.io/components/navigation-rail/overview); MD3 has no component that reserves desktop screen space. Source of truth in code: see Status in code.

A Bar is not an MD3 element. Where the Navigation bar (a bottom strip of destinations), the Top app bar (a top strip with title and actions) or the Navigation rail (a vertical strip) say something that applies to an edge strip, this note takes it and names it. Everything about reserving space, layers and monitors comes from the layer-shell protocol and the shell design, not from MD3.

## Purpose

Give the shell a permanent strip of status and launch controls along a screen edge, in a place windows do not cover, without taking the keyboard unless asked.

## When to use and not

- Use when: the content is shell-wide, always present and tied to an edge (clock, workspace switcher, tray, task list, dock).
- Do not use when: the surface reserves nothing and floats or moves ([[Panel and Surface]], a Panel); the surface is a ring around the whole output ([[Frame]]; a thick Frame edge, a strip, does a Bar's job inside the Frame); the content is a menu or flyout ([[Popup]]); the content shows for a moment ([[Volume OSD]]); the strip is inside an application window (use [[Top App Bar]] or a toolbar there).
- A dock is a Bar ([[Dock]]); a side bar is a Bar on `LEFT` or `RIGHT` ([[Bar#Variants|Vertical Bar]]).

## Anatomy

1. Surface: one layer-shell window per Bar per monitor, anchored to the edge ([[Layer Window]]).
2. Body: the painted container (fill role, optional border, corner radius, shadow). With a shadow the surface is larger than the body: a transparent margin holds the shadow and takes no input.
3. Content: one root container, usually a `FlexBox` with start, centre and end groups pushed apart by `Spacer`s; modules and blocks inside.
4. Gap: with `Gap` above 0 the Bar floats off its edge but stays attached; the gap is reserved space.
5. Reserved zone: the space the compositor keeps free of maximised windows.
6. Hover strip (when [[Auto Hide]] is built): a thin input area on the edge while the Bar is hidden.

## Variants

| Variant | Keys (top Bar shown) | Use |
|---|---|---|
| Full-span flush | `Edge: TOP`, `Width: EXPAND`, `Height: 32` | Top bar, bottom bar |
| Floating full-span | as above plus `Gap: 8` | A bar that looks detached; still reserves its space |
| Short, centred | `Edge: BOTTOM`, `Width: 560`, `Height: 64`, `Alignment: CENTER` | Dock |
| Short, at one end | `Alignment: START` or `END`, `Offset` | Corner bar |
| Vertical | `Edge: LEFT` or `RIGHT` | Side bar; children laid out vertically ([[Bar#Variants|Vertical Bar]]) |
| Non-reserving | `Layer: BOTTOM` or `OVERLAY`, or `Reserve: false` | Decorative strip, a dock that floats over windows |

## States

| State | Visual change | Token values |
|---|---|---|
| Visible | Body and content drawn | fill `surface` |
| Hidden (built only through a Frame strip today; the Bar `Visible` key is not built) | Not drawn, zone 0 | not applicable |
| Showing, Hiding | Slide of an edge margin, zone set once | see [[Auto Hide]] |
| Closed | Window destroyed (monitor removed) | not applicable |
| Keyboard focused | The focused module shows the focus ring ([[Focus Ring]]) | ring 3 dp, role `secondary` |

A Bar has no pointer-hover or pressed state of its own; its modules carry the state layers ([[State Layers]], [[Button]], [[Icon Button]]).

## Tokens used

| Part | Role or token |
|---|---|
| Fill | `surface` (shell `$color.surface`); MD3 Navigation bar uses `surface_container`, see Deviations |
| Text and icons | `on_surface`; secondary text `on_surface_variant` (shell `$color.on_surface_muted`) |
| Border | `outline_variant` if set; none by default |
| Shape | flush Bar `none` (0 dp; the MD3 Navigation bar container shape is `corner-none`); floating Bar `medium` (12 dp, proposed) |
| Elevation | flush Bar level 0; floating Bar level 2 (shell: `Elevation: 20%`) |
| Spacing | steps from [[Spacing and Density]]; vertical padding 4 dp |
| Motion | `Animation.Duration` 200 ms ([[Motion]] `short4`), reduced motion instant |

Roles and shell mapping: [[Colour Roles]]. A Bar has no look of its own: it uses the same keys and tokens as a Panel (`Background`, `Fill` as an alias in a Bar's `Style`, `Opacity`, `Elevation`, `Shadows`, `Shadow_Bleed`), see [[Panel and Surface]].

## Sizing and density

The thickness across the edge is `Height` for a top or bottom Bar and `Width` for a left or right Bar. A Bar that holds controls is at least the tallest control plus 8 dp (4 dp above, 4 dp below) so the focus ring and state layer have room. This is a Tesserae design choice built on [[ADR-0002 Desktop density levels and target sizes]] #needs-verification.

| Level | Control height | Minimum Bar thickness | Module row padding x |
|---|---|---|---|
| default | 40 | 48 | 12 |
| compact | 32 | 40 | 8 |
| dense | 28 | 36 | 4 |

- Length along the edge: pixels, a percentage of the output, `AUTO` (shrink to content) or `EXPAND` (edge to edge). `Min_` and `Max_` keys bound each size.
- Hit areas of modules are at least 24 by 24 dp ([[Spacing and Density]]); in a touch context 48 by 48 dp.
- Material counterparts for scale: Navigation bar container height 80 dp, icon 24 dp (`md.comp.navigation-bar.container.height` 80px, `icon.size` 24px, verified in Sources); Navigation rail default width 80 dp. A desktop Bar is thinner by design.

## Dimensions and defaults

Thickness, padding and gaps are Tesserae design choices built on the control heights of [[ADR-0002 Desktop density levels and target sizes]]; the choice rows are proposed in the ADR "Shell surface dimensions" #needs-verification-as-design-choice. A flush Bar is the default; the floating Bar rows carry the values that change with `Gap` above 0.

| Part | Property | Token | Default | Compact | Dense | Source | Settable |
|---|---|---|---|---|---|---|---|
| body | height | `density.control_height` + 8 | 48 | 40 | 36 | design choice, proposed ADR Shell surface dimensions, [[ADR-0002 Desktop density levels and target sizes]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Height); tre: yes (size of the LayerWindow) |
| body | min height | `density.control_height` + 8 | 48 | 40 | 36 | design choice, proposed ADR Shell surface dimensions, [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Height); tre: yes (min_height) |
| module hit area | min width | - | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.2 SC 2.5.8 (48 in a touch context) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Width); tre: yes (min_width) |
| module hit area | min height | - | 24 | 24 | 24 | [[Spacing and Density]], WCAG 2.2 SC 2.5.8 (48 in a touch context) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Min_Height); tre: yes (min_height) |
| body | padding | `space.2`, `density.row_padding_x` | 4 12 4 12 | 4 8 4 8 | 4 4 4 4 | design choice, proposed ADR Shell surface dimensions, [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook; tre: yes (padding) |
| body | margin | `Gap` | 0 | 0 | 0 | [[Bar#Defaults]] (`Gap` 0; 8 for a floating Bar, which reserves it) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Gap); tre: yes (margin of the LayerWindow) |
| content | gap | `space.3`, `space.2` | 8 | 8 | 4 | design choice, proposed ADR Shell surface dimensions, [[Spacing and Density]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Spacing); tre: yes (gap) |
| body | border width | - | 0 | 0 | 0 | [[Bar#Tokens used]] (no border by default), MD3 Navigation bar has none | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook; tre: yes (border_width) |
| body | border color | `outline_variant` | N/A: no border by default; `outline_variant` when a border is set | N/A: same as default | N/A: same as default | [[Colour Roles]] | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook; tre: yes (border_color) |
| flush body | corner radius | `shape.none` | 0 | 0 | 0 | [[Shape]], MD3 `md.comp.navigation-bar.container.shape` corner-none | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook; tre: yes (corner_radius) |
| floating body | corner radius | `shape.medium` | 12 | 12 | 12 | design choice, proposed ADR Shell surface dimensions, [[Shape]] | tess-ui: n/a: element absent in tess-ui; tess-shell: no hook; tre: yes (corner_radius) |
| module label | font | `label_large`, `label_medium` | 14/20/500/0.1 | 14/20/500/0.1 | 12/16/500/0.5 | [[Typography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Font_Size, Font_Weight, Line_Height); tre: yes (font_size, font_weight, line_height) |
| module icon | icon size | `density.icon_button_icon` | 24 | 20 | 20 | [[Spacing and Density]], [[Iconography]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Width, Height of the SVG block); tre: yes (width, height of the svg node) |
| flush body | elevation | `elevation.level0` | 0 | 0 | 0 | [[Elevation]] | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation in Style); tre: yes (shadows) |
| floating body | elevation | `elevation.level2` | 2 | 2 | 2 | [[Elevation]] (shell `Elevation: 20%`) | tess-ui: n/a: element absent in tess-ui; tess-shell: yes (Elevation in Style); tre: yes (shadows) |

## Layout and overflow

- Contents lay out as a `FlexBox` on the Bar's main axis: horizontal for `TOP` and `BOTTOM`, vertical for `LEFT` and `RIGHT`. Text on a vertical Bar is not rotated; `Text_Rotation` is opt-in and not built.
- Single-line text is vertically centred in the Bar's thickness: the line box has the same space above and below within 1 px ([[Spacing and Density]], AC-DEN-9).
- Text in a module ends in an ellipsis at its maximum width; no module paints outside the Bar body ([[10 Layout Overflow and Scrolling]]).
- Size rules: `EXPAND` along the Edge stretches; `EXPAND` across the Edge resolves to `Max_` else `Min_` else 0. A Bar whose size across or along resolves to 0 is not created; a warning names the Bar and the key to set (`Min_Height` for a top or bottom Bar, `Min_Width` for a side Bar). The check runs at creation only and never blocks hiding or peeking.
- When the content is wider than the Bar, the Bar does not scroll (one row of modules); the author sets `Max_` sizes or hides modules. A scrollable Bar is not specified.

## Behaviour

- Pointer: a click on a module acts on the module. The body takes the pointer; the shadow margin does not (the input region is the body). Hover opens nothing on the Bar itself; tray and clock hover tooltips belong to the modules ([[Tooltip]]).
- Keyboard: a Bar takes no keyboard by default (`Keyboard: NONE`; Tab does nothing in it). `ON_DEMAND` gives it the keyboard after a click. A Bar that holds a text field takes `ON_DEMAND` whatever is written, and the shell logs a warning when `NONE` was written. Keyboard-only access to a Bar is through [[Keyboard Navigation|Shortcut Mode]] (`Enter_Shortcut_Mode`, then `Next_Focus` and `Previous_Focus` by `Tab_Index`) and the Bar's `Shortcut_Mode` key; see [[Keyboard Navigation]]. A hidden or auto-hidden Bar is revealed by Shortcut Mode, which moves focus to it; leaving the mode or pressing Escape hides it again per `Auto_Hide` and `Auto_Hide_Delay`; a Bar that holds keyboard focus is not hidden; plain keys do not reveal it ([[ADR-0021 Shortcut Mode reveals a hidden Bar]], [[Auto Hide]]).
- Touch: modules take 48 by 48 dp hit areas in a touch context.
- Reservation: the zone is the thickness plus `Gap` when `Layer` is `TOP` and `Reserve` is true. The compositor adds the margin to the zone, so a Bar with `Height: 32` and `Gap: 8` reserves 48 px (measured on KWin 6.8.2 and sway, 2026-11-04): 8 px above the Bar, the Bar, 8 px below. A Bar reserves on its own output only.
- Layers: `BOTTOM`, `TOP` or `OVERLAY`; default `TOP`. Reserved space exists only on `TOP`. `BACKGROUND` is not offered. The layer-shell protocol leaves the order of two surfaces on one layer undefined, so a surface that must draw over a Bar is on a higher layer.
- Fullscreen: a fullscreen window covers every shell surface; a maximised window stops at the zone ([[12 Overlays]]).
- Multi-monitor: a Bar belongs to a `Monitor` block, so to one monitor. A Bar imported by several `Monitor` blocks appears on each. When a monitor is removed its Bar closes; when it returns the Bar is created again. Another monitor's Bar is not touched.
- Popups: a popup opened from a Bar module hangs off the Bar and is clipped by nothing; see [[Popup]]. Dismissal rules are in [[Popup]] (AC-POP-*).

## Tooltip and overlay behaviour

A Bar carries no tooltip. Each module that needs one puts it on its own control ([[Tooltip]], [[ADR-0004 Tooltip rule]], [[ADR-0011 Tooltip hover grace for all tooltips]]). A tooltip or popup opened from a Bar is a Popup surface placed against the module rectangle with the shell's gap ([[Popup]]); it never takes the Bar's layer.

## Motion

- Show and hide of a Bar: slide of the edge margin by `Animation { Type: SLIDE, Duration: 200 }` or fade, `Content_Fade` on by default; not built for a Bar (`Animation` is "Not built"). Rules in [[Auto Hide]] and [[Auto Hide|Content Fade]].
- A margin animation is one small commit per step; the zone changes once, at the start of a show and at the end of a hide, so windows reflow once ([[12 Overlays#Motion and reduced motion|Surface Animation]]).
- Reduced motion: show and hide are instant, no slide, no fade.
- An idle Bar draws no frames between module updates.

## Accessibility

- Role and name: tre publishes the Bar as one window of the application; the window node has no accessible name in tre, so the shell sets one per Bar ("Top bar", "Dock"). Modules inside carry roles, labels and states ([[Accessibility Rules]] AR-1, AR-2).
- Keys: Tab walks the focusable modules when the Bar takes the keyboard; Enter and Space activate a focused button ([[Button]]).
- Every action reachable by pointer is reachable by keyboard (AR-9) through [[Keyboard Navigation|Shortcut Mode]] or a global shortcut ([[11 Interaction#Shortcuts and conflicts|Global Shortcuts]]). For an auto-hidden Bar, Shortcut Mode reveals it ([[ADR-0021 Shortcut Mode reveals a hidden Bar]], [[Auto Hide]]).
- Contrast: `on_surface` on the fill at least 4.5 to 1 in light, dark and high contrast; the measured shell pairs are 14.87, 15.31 and 21.00 ([[Colour Roles]]).
- Announcements: the shell speaks changes through one window of the shell (the Frame, else the Bar), by owner decision of 2026-11-19; whether Orca reads an unfocused window is untested ([[14 Accessibility Basics#Announcements and live regions|Accessibility Announcements]]).
- Screen position: a screen reader gets the tree but no screen position for a layer surface.

## Dark and light

The fill and text resolve from the scheme at draw time ([[ADR-0005 Theme follows the system]]); there is no literal colour in a Bar. A shell started with no `Appearance.Stylesheets` key falls back to the `Default` stylesheet (shell ADR-0022, accepted 2026-11-21), so a Bar's text and icons stay readable in both schemes (owner feedback S1, [[Owner Feedback 2026-11-20]]).

## Defaults

| Setting | Default |
|---|---|
| `Layer` | `TOP` |
| `Reserve` | `true` |
| `Gap` | 0 |
| `Keyboard` | `NONE` |
| `Alignment` | `CENTER` (no effect on an `EXPAND` axis) |
| `Auto_Hide` | `true` in the design, not built; a Bar is always shown today |
| `Auto_Hide_Delay` | 1000 ms proposed, not built |
| Fill | `surface` |
| Thickness | 48 dp at the default level (proposed) |

## Acceptance criteria

Check types follow [[Test Method]]. Geometry checks run at scale 1.0, 1.25 and 2.0 and compare in dp.

- [ ] AC-BAR-1 (geometry check, mapping): the placement function returns, on a 1920 px wide output, for `TOP`, `EXPAND`, 32: anchor top,left,right, size (0, 32), margin (0,0,0,0), zone 32; with `Gap: 8`: margin (8,0,0,0), zone 40; `BOTTOM`, 560, 64, `CENTER`: anchor bottom, size (560, 64), zone 64; `TOP`, 400, 32, `START`, `Offset: 200`: anchor top,left, margin (0,0,0,200), zone 32, exclusive edge top; the same with `END`, `Offset: 40`: anchor top,right, margin (0,-40,0,0). Pass: 5 of 5 rows exact.
- [ ] AC-BAR-2 (geometry check, hand check on KWin): with a full-span top Bar of `Height: 32` a maximised window starts 32 px below the top edge; with `Gap: 8` it starts 48 px below (zone plus margin). Pass: equal to the pixel on KWin 6.8 and sway.
- [ ] AC-BAR-3 (geometry check, layer): a Bar on `BOTTOM` or `OVERLAY` with `Reserve: true` has exclusive zone 0 and a maximised window ignores it; the same Bar on `TOP` reserves. Pass: reserved space 0 and thickness respectively.
- [ ] AC-BAR-4 (scripted input, load error): writing `Exclusive_Zone` on a Bar whose `Layer` is not `TOP` fails at load with an error that names the file, the Bar and the key. Pass: error count 1 with those three names. Status today: the key is reported as "not built".
- [ ] AC-BAR-5 (geometry check, size rules): a top Bar with `Height: EXPAND` and `Max_Height: 40` is 40 dp thick; with neither `Max_` nor `Min_` it is not created and the warning names `Min_Height`; with `Height: 0` the same. A hidden Bar can still be shown ([[Auto Hide]]). Pass: sizes and messages as stated.
- [ ] AC-BAR-6 (scripted input, multi-monitor): with two monitors and a Bar imported by both, both show it; removing one monitor closes only that Bar (window count 2 to 1); adding it back creates it again within 2 s at the same geometry. Pass: counts and geometry equal.
- [ ] AC-BAR-7 (geometry check, vertical): a Bar on `LEFT` lays its children out in one column with no text rotation; the children's x positions are equal (within 1 dp) and y positions increase. Pass: monotonic y, equal x, glyph baseline horizontal.
- [ ] AC-BAR-8 (geometry check, density): a Bar holding a `Button`, a switch row and an icon button measures at least 48, 40 and 36 dp thick at default, compact and dense, and the tallest control has 4 dp of free space above and below (±1 dp). Pass: values equal or greater.
- [ ] AC-BAR-9 (token test, no literals): no `Background`, `Fill` or text colour of a Bar or its modules is a hex literal; each is a role or theme token. Pass: zero literal fills (see AC-PNL-2).
- [ ] AC-BAR-10 (contrast script): `on_surface` and `on_surface_variant` on the Bar fill reach 4.5 to 1 in the dark, light and high contrast modes of the shipped theme. Pass: 6 of 6 pairs at least 4.5.
- [ ] AC-BAR-11 (scripted input, shadow and input region): with `Elevation: 20%` on a Bar, a press 2 dp outside the body inside the shadow margin reaches the window underneath; the reserved space is the same with and without the shadow. Pass: underlying window receives the press; zone equal.
- [ ] AC-BAR-12 (scripted input, keyboard default): with `Keyboard: NONE` a Tab key press changes no focus inside the Bar; with `ON_DEMAND`, after a click on a module, Tab moves focus between its focusable modules in `Tab_Index` order. A Bar with a text field and `Keyboard: NONE` takes `ON_DEMAND` and logs one warning. Pass: focus path as stated and warning count 1.
- [ ] AC-BAR-13 (scripted input, keyboard-only): from a state with no pointer events, `Enter_Shortcut_Mode` then `Next_Focus` visits each focusable module of the Bar once in `Tab_Index` order and `Exit_Shortcut_Mode` returns focus to the previous window. Pass: visit list equals the module list; no module visited twice.
- [ ] AC-BAR-14 (AT tree assertion): each Bar window has a non-empty accessible name; each module root has a role and a non-empty name; decorative glyphs are hidden. Pass: 0 nodes without a name among interactive nodes (AR-1, AR-5).
- [ ] AC-BAR-15 (pixel check, idle): over 5 s with no module update, the Bar commits 0 frames. Pass: frame count 0.
- [ ] AC-BAR-16 (scripted input, fullscreen): a fullscreen window on a monitor hides or covers the Bar and releases its zone on that monitor; leaving fullscreen restores both. Pass: zone 0 then restored; the other monitor's Bar unchanged. Hand check on KWin.
- [ ] AC-BAR-17 (scripted input, not-built keys): writing each of `Exclusive_Zone`, `Input_Region`, `Auto_Hide`, `Auto_Hide_Delay`, `Visible`, `Attach_To`, `Meld`, `Animation`, `Text_Rotation`, `Padding`, `Class` in a Bar yields a loader message naming the key as not built. Pass: 11 of 11. When a key is built its row here is replaced by that key's own criterion.
- [ ] AC-BAR-18 (contrast script, no stylesheet): with no `Appearance.Stylesheets` key, a Bar module's text contrast against the Bar fill is at least 4.5 to 1 in light and dark (owner feedback S1). Pass: 2 of 2.
- [ ] AC-BAR-19 (geometry check, hit areas): every interactive node in a Bar has a hit area of at least 24 by 24 dp (48 by 48 in a touch context) read from the engine hit test. Pass: zero smaller targets ([[Spacing and Density]], AC-DEN-7).
- [ ] AC-BAR-20 (review, no look of its own): the style keys a Bar accepts (`Background`, `Fill`, `Opacity`, `Elevation`, `Shadows`, `Shadow_Bleed`) are a subset of the keys a Panel accepts and use the same tokens (see AC-PNL-10). Pass: reviewer finds no Bar-only look key.
- [ ] AC-BAR-21 (scripted input, hidden Bar reachable by keyboard, ADR-0021): with a hidden Bar, `Enter_Shortcut_Mode` shows it and moves focus to it; Escape or `Exit_Shortcut_Mode` hides it again after `Auto_Hide_Delay`; while it holds keyboard focus it is not hidden; a plain key press with no mode active leaves it hidden. Pass: states as stated (the same checks as AC-AHD-9, AC-AHD-10, AC-AHD-20 and AC-AHD-21 in [[Auto Hide]]).

## Status in code

| Project | Path | Status |
|---|---|---|
| tess-shell | `tess-shell:src/tess_shell/surfaces/bar.py` (placement function), `tess-shell:src/tess_shell/schema/blocks.py` (Bar root, not-built keys), `tess-shell:src/tess_shell/schema/docs.py`, `tess-shell:docs/guide/surfaces.md#bar` | Partly meets. Meets AC-BAR-1, AC-BAR-3 (zone 0 off `TOP`), AC-BAR-5, AC-BAR-11, AC-BAR-12 in design (unit tests of the placement function, not run here). Not built, so AC-BAR-17 holds and the dependent behaviour fails: `Exclusive_Zone` (AC-BAR-4), `Input_Region`, `Auto_Hide`, `Auto_Hide_Delay`, `Visible`, `Attach_To`, `Meld`, `Animation`, `Text_Rotation`, `Padding`, `Class`; `Reveal_Key` was removed (PR 59). A Bar cannot be hidden. AC-BAR-8 not run: no density setting, shipped examples use `Height: 32`. AC-BAR-13 depends on Shortcut Mode, whose keyboard on KWin is not checked. |
| tess-shell | `tess-shell:src/tess_shell/surfaces/hotplug.py` | Meets AC-BAR-6 in design: surfaces are matched by key and output; a removed monitor closes its windows and a returning monitor recreates them. |
| tess-shell | `tess-shell:src/tess_shell/surfaces/bar.py` (dimensions) | Dimension difference: shipped examples set `Height: 32` (thickness 32) against the table's 48 dp thickness at default; no density setting exists (AC-BAR-8). Settable: a Bar takes no `Padding`, and its `Style` takes no `Border_Width`, `Border_Color` or `Corner_Radius` (the table's body padding, border and radius cannot be set on the Bar itself). |
| shell vault | `shell-vault:40 Specifications/Surfaces/Bar.md`, `shell-vault:40 Specifications/Surfaces/Surface Types.md` | Source design. Acceptance line 2 of the vault says a dock with `Gap: 8` and `Height: 64` sets a zone of 72; the measurement of 2026-11-04 says the compositor reserves thickness plus twice the gap (80). This note follows the measurement. |
| tess-ui | not applicable | Application windows use [[Top App Bar]] and toolbars; tess-ui draws no shell surface. |
| tre | `tre:docs/reference/layer-window.md` | Mechanism only: `LayerWindow` with `layer`, `anchor`, `size`, `margin`, `exclusive_zone`, `exclusive_edge`, `keyboard`, `input_region`. Not applicable as a component. |

## Deviations from Material Design 3

| Deviation | Reason | ADR |
|---|---|---|
| A Bar has no MD3 component; it reserves screen space through layer-shell | desktop shell element | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Fill `surface` at level 0 instead of the Navigation bar's `surface_container` at level 2 | the shell ground colour is the Bar ground; separation by tone, shadow only when floating | [[ADR-0001 MD3 role names are the specification vocabulary]] |
| Thickness 48, 40, 36 dp (MD3 Navigation bar 80 dp) | desktop density, one-line modules | [[ADR-0002 Desktop density levels and target sizes]] |
| Text is not rotated on a vertical Bar | readability; rotation is opt-in and not built | [[ADR-0006 MD3 baseline with named Expressive adoptions]] |
| Keyboard default is none; access by Shortcut Mode | a layer surface that grabs the keyboard unasked steals it from windows | none (shell design of 2026-10-27) |

## Sources

- Navigation bar container 80 px, icon 24 px, container `surface_container`, level 2, shape `corner-none`, active indicator 64 by 32: https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-comp-navigation-bar.scss (verified 2026-11-21).
- Navigation rail default width 80 dp (Material Components Android docs): https://github.com/material-components/material-components-android/blob/master/docs/components/NavigationRail.md ; top app bar size dimens: https://github.com/material-components/material-components-android/blob/master/lib/java/com/google/android/material/appbar/res/values/dimens.xml (small height token not resolved #needs-verification).
- Layer-shell protocol (exclusive zone includes the margin, anchors, layers): https://wayland.app/protocols/wlr-layer-shell-unstable-v1.
- WCAG 2.2 SC 2.5.8 Target Size (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ; SC 1.4.3: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html ; SC 2.1.1 Keyboard: https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html.
- Shell: `shell-vault:40 Specifications/Surfaces/Bar.md`, `shell-vault:40 Specifications/Surfaces/Surface Types.md`, `shell-vault:30 Decisions/ADR-0010 Surface Shadows.md`, `shell-vault:30 Decisions/ADR-0022 Default Stylesheet.md`; `tess-shell:src/tess_shell/surfaces/bar.py`, `tess-shell:src/tess_shell/schema/docs.py`, `tess-shell:docs/guide/surfaces.md#bar` (read on origin/main, 2026-11-21).
