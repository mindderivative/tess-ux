---
title: Adoption tess-shell
type: adoption
status: draft
owner: phil
created: 2026-11-21
updated: 2026-11-22
tags: [adoption, tess-shell, worklist]
related: ["[[70 Adoption]]", "[[Audit Template]]", "[[17 Conformance]]", "[[Open Questions]]", "[[Adoption tre]]", "[[Tooltip]]", "[[Bar]]", "[[Auto Hide]]", "[[State Layers]]", "[[Menu Item]]", "[[Clock Module]]", "[[Tray Module]]", "[[Keyboard Navigation]]", "[[ADR-0009 State layer percentages]]", "[[ADR-0011 Tooltip hover grace for all tooltips]]", "[[ADR-0020 The engine never blocks the design]]", "[[UXREQ-001 Two-axis scroll view with the specified scrollbar]]", "[[UXREQ-008 Outline property for focus rings]]"]
depends_on: ["[[Audit Template]]", "[[17 Conformance]]", "[[Test Method]]"]
---

# Adoption tess-shell

> [!info] Summary
> The severity-ordered worklist of what tess-shell must change to meet the specifications, built from the `Status in code` rows of every note that names tess-shell and checked against `tess-shell` at origin/main commit `42cdfb5` (committed 2026-11-20), then corrected against the tess-shell bot's own read of its code on origin/main. It is not an audit: no test was run, no result below is `pass`, and the coverage counts are approximate. Counts: 26 open findings (P0 0, P1 13, P2 13; TSH-008 and TSH-084 are blocked on shell features), 31 fixed and 3 implemented with the merge pending the owner check (TSH-010, TSH-050, TSH-051), after the tess-shell audit against main (schema 1.30, 2026-11-22; taken from the shell bot, not re-checked here). Seven open rows are held on an owner or engine decision or are partly done (see Held findings). No owner decision is open (OQ-23, state layers, was closed on 2026-11-22 with a yes). OQ-25 (Bar auto-hide against keyboard reachability) was closed on 2026-11-21 by [[ADR-0021 Shortcut Mode reveals a hidden Bar]].

## Method and header

| Item | Value |
|---|---|
| Project | tess-shell |
| Project commit read | `42cdfb5` on origin/main (2026-11-20) |
| Vault state | Phase 3, 2026-11-21 |
| Basis | the `Status in code` rows of the component, foundation, pattern and chapter notes; each key finding re-read in the code at the commit above |
| Dropped | findings the code no longer shows: TSH-016 (Tab leaves the Text Editor since tre 0.6.8) and TSH-062 (the fallback shadow is `#00000066`), listed under Fixed since the audit |
| Severity | P0 blocks use; P1 breaks a rule of the specification; P2 polish |
| Not done | no test run, no screenshot, no screen reader; items marked unverified stay `not run` per [[17 Conformance]] |

Verified in code at `42cdfb5`:

| Fact | Evidence |
|---|---|
| Six literal tooltip cards (`Background: $color.surface_raised`, `Corner_Radius: 8`, `Elevation: 20%`) in Audio, Battery, Clock, Media, Network and Tray_Item | `tess-shell:src/tess_shell/shipped/Audio/Audio_Module.tdl:52-58`, `Battery/Battery_Module.tdl:43-49`, `Clock/Clock_Module.tdl:26-32`, `Media/Media_Module.tdl:53-59`, `Network/Network_Module.tdl:42-48`, `Tray_Item/Tray_Item_Module.tdl:34-40` |
| Tooltips sit on `Role: GROUP` roots in Battery, Network and Media | `Battery_Module.tdl:38`, `Network_Module.tdl:37`, `Media_Module.tdl:47` |
| Tooltip exit delay default 200 ms (ADR-0011 asks 150 ms) | `tess-shell:src/tess_shell/schema/model.py:129`, `schema/shell.py:2076` |
| Bar keys `Auto_Hide`, `Auto_Hide_Delay`, `Visible`, `Animation`, `Input_Region`, `Meld`, `Padding`, `Class`, `Attach_To` documented "Not built"; `Reveal_Key` removed | `tess-shell:src/tess_shell/schema/docs.py:191-203,270-278`, `schema/blocks.py:438` |
| Frame `Children`, `Meld`, `Border_Tile` and others "Not built" | `schema/docs.py:236,339-340` |
| Tray item and spacing literals 18 and 6 | `Tray/Tray_Module.tdl:27,31`, `Tray_Item/Tray_Item_Module.tdl:16` |
| Menu item height 28, padding 10, icon 16 literals | `MenuItem/MenuItem_Module.tdl:37,40,52-53` |
| Menu item pressed fill is `primary`, hover is `outline`; no state layers | `Stylesheets/Default_Stylesheet.tdl:121-123` |
| Pressed menu item text `on_surface` on `primary` measures 2.58 to 1 in Dark (`#E4EAF1` on `#5B97C9`) and 2.89 to 1 in Light (`#16202B` on `#2F6B9A`) | `Themes/Default_Theme.tdl:15-20,72-76`; ratios computed from the hex values |
| Clock Face `Foreground: "#ffffff"` literal; against Light `surface` `#F4F7FA` it measures 1.08 to 1 | `Clock/Clock_Style.tdl:13`; ratio computed |
| `Tab_Index` is the ordering model (positive indices rank first) | `tess-shell:src/tess_shell/binder/build.py:643-657`, `binder/focus.py:71-72` |
| No `F6` anywhere in `src` | text search of origin/main `src` |
| Tasks closes a window on middle click only | `Tasks/Tasks_Module.tdl:61` |
| Audio changes volume on scroll through `On_Scroll` | `Audio/Audio_Module.tdl:50` |
| Tray has no key path to the menu | `Tray/Tray_Module.tdl`, `Tray_Item/Tray_Item_Module.tdl` (no key handler) |

## Worklist by theme

Rows are ordered by severity within each theme. Every AC id exists in the vault.

### Tooltips

Six tooltip cards repeat one literal block, and five of the six triggers are `GROUP` roots or boxes rather than the control the tooltip describes ([[Tooltip]], [[ADR-0011 Tooltip hover grace for all tooltips]]).

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-004 | P1 | Status: in tess-shell PR 151. Six literal tooltip cards differ from the plain tooltip look | AC-TIP-13, AC-TIP-21, AC-MOD-AUD-10, AC-MOD-BAT-9, AC-MOD-CLK-5, AC-MOD-MED-10, AC-MOD-NET-8, AC-MOD-TRI-8 | the six paths listed under "Verified in code" | Replace the six blocks with one shipped tooltip card style read from tokens | [[Tooltip]] |
| TSH-008 | P2 | held: blocked on a shell feature (dynamic tooltips in `For` plus `Class` on a module call). Applications rows have no tooltip for cut text | AC-MOD-APP-8 | `tess-shell:src/tess_shell/shipped/Applications/Applications_Module.tdl` | Add the cut-text tooltip on the row label | [[Applications Module]] |

### Keyboard reachability

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-015 | P1 | Status: in tess-shell PR 150. No F6 landmark cycling between surfaces | AC-KBN-3 | text search of origin/main `src` finds none | Add F6 and Shift+F6 over Bar, Panels and the focused window | [[Keyboard Navigation]] |

### State feedback

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-020 | P1 | OQ-23 closed 2026-11-22: the owner adopted the MD3 state layers for the shell. The shell has no state layers; states change `Background`, `Border_Color` or `Opacity` (Toggle and Checkbox hovered 0.85, pressed 0.7; disabled 0.5 on all widgets) Update (2026-11-22, tess-shell audit against main, schema 1.30): state layers implemented; the 15, 105 and 150 ms fades wait for tre 0.6.12; OQ-23 is closed (the owner adopted the state layers on 2026-11-22). | AC-STL-1, AC-STL-2, AC-STL-3, AC-STL-5, AC-C09-1, AC-C09-2, AC-C09-4 | `tess-shell:src/tess_shell/shipped/Stylesheets/Default_Stylesheet.tdl:43-83,121-123` | Owner decides adopt or declare a deviation; do not fix until then | [[State Layers]], [[ADR-0009 State layer percentages]] |
| TSH-022 | P1 | OQ-23 closed (adopted). Toggle gets the generic focus ring; hover and pressed are opacity, not state layers Update (2026-11-22, tess-shell audit against main, schema 1.30): as TSH-020 (Toggle hover and pressed layers); fades wait for tre 0.6.12. | AC-MOD-TGL-4 | `tess-shell:src/tess_shell/shipped/Toggle/Toggle_Module.tdl`, `Stylesheets/Default_Stylesheet.tdl:57` | Follow TSH-020 | [[Toggle]] |
| TSH-023 | P2 | Status: in tess-shell PR 152. Task Item minimised shows as opacity 0.5 only, the disabled look | AC-MOD-TIT-7 | `tess-shell:src/tess_shell/shipped/Task_Item/Task_Item_Style.tdl` | Use an icon or text state cue, not the disabled opacity | [[Task Item]] |

### Density and sizes

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-037 | P2 | Status: not started (tess-shell starts it now). Default icon size 16 literal where list and menu icons are 24 | AC-ICO-1, AC-C08-1 | `tess-shell:src/tess_shell/shipped/Icon/Icon_Module.tdl`, `MenuItem/MenuItem_Module.tdl:52-53` | Take icon size from the density tokens | [[Iconography]] |
| TSH-039 | P2 | Status: not started (tess-shell starts it now). Modules use pixel literals not the spacing tokens | AC-DEN-1 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:47-55` | Replace literals by `$space` tokens when TSH-034 lands | [[Spacing and Density]] |

### Contrast

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-042 | P1 | Status: in tess-shell PR 148. No contrast script over the shipped themes exists | AC-COL-3, AC-COL-4, AC-LNC-15, AC-LNC-17 | `tess-shell:docs/design/60 Quality/Accessibility.md` (rule 9 asks for it) | Add a script that checks every role pair in the three modes | [[Colour Roles]], [[Launcher]] |
| TSH-043 | P1 | Status: in tess-shell PR 148. The token `accent` on `surface` measures 4.38 Dark and 3.82 Light, below the 4.5 text requirement; no shipped file uses `accent` as text (`shipped/`), so it is a token finding. The specification now says accent is never text ([[ADR-0025 Shell outline and high contrast status colours, accent never text]], AC-COL-12); the contrast tool lists the token as a known violation | AC-COL-3 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl:22` | Keep `accent` to non-text uses or darken the token; lint text uses | [[Colour Roles]] |
| TSH-090 | P1 | Status: in tess-shell PR 148. Dark `outline` `#55657A` on `surface_raised` measures 2.69 to 1 (Button border, card edge; needs 3 to 1); the specification raises it to `#5F7188` (3.61 on `surface`, 3.21 on `surface_raised`) | AC-COL-4, AC-COL-3 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` | Set Dark `Color.Outline` to `#5F7188` | [[Colour Roles]] |
| TSH-091 | P1 | Status: in tess-shell PR 148. High_Contrast on a Light scheme leaves `error`, `warning` and `success` at their Light values, which measure 3.21, 3.54 and 3.27 to 1 on the black High_Contrast surface (needs 4.5, 7 at the high level); the specification sets explicit High_Contrast values `#F2958C`, `#E6BB6A`, `#8CCB9A` (9.45, 11.68, 11.12 on black) | AC-COL-4, AC-COL-3 | `tess-shell:src/tess_shell/shipped/Themes/Default_Theme.tdl` (High_Contrast block) | Add the three High_Contrast colours | [[Colour Roles]] |

### Surfaces not built

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-053 | P1 | Bar and Popup `Animation` not built (no popup show and hide animation) | AC-BAR-17, AC-AHD-13 | `tess-shell:src/tess_shell/schema/docs.py:278,330` | Build `Animation` with the motion tokens and reduced motion | [[Bar]], [[Popup]] |
| TSH-054 | P1 | OQ-23 closed (adopted); the level model follows. Frame `Elevation`, `Shadows`, `Shadow_Bleed` not built; one shadow list scaled by percent Update (2026-11-22, tess-shell audit against main, schema 1.30): Frame shadow in the ring shader and Elevation levels 1 to 5 implemented; the path build waits for tre 0.6.12. | AC-FRM2-11, AC-PNL-5, AC-ELV-3 | `tess-shell:src/tess_shell/binder/shadow.py`, `schema/docs.py:339-340` | After OQ-23, build the keys | [[Frame]], [[Panel and Surface]], [[Elevation]] |
| TSH-055 | P2 | Status: not started. Panel `Margin`, `Padding`, `Class`, `Exclusive_Zone` and Bar `Padding`, `Class`, `Text_Rotation` not built | AC-BAR-17, AC-PNL-4 | `tess-shell:src/tess_shell/schema/docs.py:203,275-276,307-310` | Build `Padding` and `Class` first | [[Panel and Surface]], [[Bar]] |
| TSH-056 | P2 | Status: not started (tess-shell starts it now). Peek handle colour is a literal; handle nodes not exposed; single trigger only | AC-PEK-14, AC-PEK-16, AC-PEK-18 | `tess-shell:src/tess_shell/surfaces/frame.py` (`_handle_colour`), `surfaces/handle.py` | Colour from a role; expose the handle as a named control | [[Peek]], [[Dock]] |
| TSH-057 | P2 | The Launcher is a Panel with an output-sized catcher since M7k, so it no longer takes the popup grab. Ordinary focused Popups still use the PopupWindow grab, which steals the keyboard on KWin: popups that need keyboard input fault there. Popup Escape closed by the shell is not verified on KWin | AC-POP-1, AC-POP-6, AC-POP-7 | `tess-shell:src/tess_shell/surfaces/popup.py` (`_key`) | Run the hand checks on KWin for a keyboard Popup and record | [[Popup]] |

### Theming

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-061 | P1 | No persistent user override of the scheme; first-frame behaviour with a slow portal not tested | AC-TH-4, AC-TH-5, AC-TH-7 | `tess-shell:src/tess_shell/services/portal.py`, `appearance.py` | Add a settings key for the override | [[Theme Following the System]] |
| TSH-064 | P2 | The tooltip cards use tokens (`$color.surface_raised`), not hex fallbacks; `Corner_Radius: 8` and `Elevation: 20%` are repeated literals outside the theme Update (2026-11-22, tess-shell audit against main, schema 1.30): partly done (tess-shell audit). | AC-TIP-13 | the six tooltip files | Resolved by TSH-004 | [[Colour Roles]] |

### Accessibility roles

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-070 | P1 | held: Orca is not installed on the owner's machine, so this is a hand check. Launcher, announcements and `active_descendant` for the Launcher list are untested | AC-MOD-APP-1, AC-LNC-20 | `tess-shell:docs/design/60 Quality/Accessibility.md`, `docs/design/00 Home/Hand Checks.md` | Run the hand checks when Orca is available | [[Accessibility Tree]], [[Launcher]] |
| TSH-072 | P2 | Status: not started. There is no Accordion module; Expander is the module. It has no header and no keys of its own, and the controlling Button carries `expanded` | AC-ACC-09 | `tess-shell:src/tess_shell/shipped/Expander/Expander_Module.tdl` | Document the pairing of Expander and Button | [[Expander]] |
| TSH-073 | P2 | Status: in tess-shell PR 152. Tray attention shows an AttentionIcon cue when the app sends one; otherwise it is colour plus border only | AC-MOD-TRI-7 | `tess-shell:src/tess_shell/shipped/Tray_Item/Tray_Item_Style.tdl` | Add a shape cue for items without an AttentionIcon | [[Tray Item]] |

### Blocks not built

| ID | Severity | Finding | Failing ACs | Evidence | Suggested fix | Spec note |
|---|---|---|---|---|---|---|
| TSH-080 | P1 | held: UXREQ-001 (needs a tre hook). ScrollBox has no scrollbar of either axis; `Scroll_Snap` and `On_Scroll` not built Update (2026-11-22, tess-shell audit against main, schema 1.30): scrollbars for ScrollBox and the Popup scroll view are built; `Scroll_Snap` and `On_Scroll` are still not built. | AC-SCB-02, AC-SCB-03, AC-SCB-04, AC-SCB-05, AC-SCB-06, AC-SCB-07, AC-SCB-08, AC-SCB-09, AC-SCB-12, AC-SCB-13, AC-BLK-SBX-5, AC-LAY-7, AC-LAY-8 | `tess-shell:src/tess_shell/schema/blocks.py` (`ScrollBox`) | Build the block on the hook ([[UXREQ-001 Two-axis scroll view with the specified scrollbar]]) | [[ScrollBox]], [[Scrollbar and Scroll Container]] |
| TSH-081 | P2 | Status: in tess-shell PR 153. Text Selection: no copy command (Ctrl+C is in tess-shell PR 153, merge pending) | AC-SEL-10 | `tess-shell:src/tess_shell/schema/blocks.py` (`Selectable`) | Add Ctrl+C on a selectable Text | [[Text Selection]] |
| TSH-082 | P2 | Status: not started. List has no empty text; selection is single only; no multi select rules | AC-EMP-1, AC-SLT-1, AC-SLT-2, AC-SLT-3, AC-SLT-4, AC-SLT-6, AC-SLT-9 | `tess-shell:src/tess_shell/shipped/List/List_Module.tdl` | Add an `Empty` slot and the multi-select keys | [[Empty States]], [[Selection]] |
| TSH-084 | P2 | held: blocked on a shell feature (events to a non-root block of a composite TextInput). Text Input has no error, helper text or `invalid` state | AC-VAL-3, AC-VAL-5 | `tess-shell:src/tess_shell/shipped/TextInput/TextInput_Module.tdl` | Add `Error` and `Helper` slots | [[Validation]], [[Text Field]] |

## Fixed since the audit

| ID | Finding | Fix | Failing ACs it cleared | Spec note |
|---|---|---|---|---|
| TSH-016 | Text Editor took Tab and could not leave the field | Tab leaves the Text Editor since tre 0.6.8 | AC-MOD-TED-4 | [[Text Editor]] |
| TSH-062 | A theme without `Elevation.Max` drew `#00000040` while the shipped theme says `#00000066` (the audit note was stale) | `DEFAULT_MAX` in `tess-shell:src/tess_shell/binder/shadow.py` is `#00000066` on main, equal to the theme; no deviation | AC-ELV-3 | [[Elevation]] |
| TSH-001 | Tooltip sits on the `GROUP` root of Battery and Network instead of on one control | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-BAT-1, AC-MOD-BAT-5, AC-MOD-NET-1, AC-MOD-NET-4 | [[Battery Module]], [[Network Module]] |
| TSH-002 | Audio tooltip on the group root, not on the controls | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-AUD-5, AC-MOD-AUD-6 | [[Audio Module]] |
| TSH-003 | Media has a tooltip on the root and a second on the Marquee | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-MED-5, AC-MOD-MED-6 | [[Media Module]] |
| TSH-005 | Tooltip exit delay is 200 ms where ADR-0011 asks a 150 ms grace; a tooltip is hoverable today (the pointer can enter it), only the close delay differs | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-TIP-4 | [[Tooltip]] |
| TSH-006 | No Escape, scroll or press dismissal; hover only | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-TIP-1 | [[Tooltip]] |
| TSH-007 | Workspaces and Task Item have no tooltip on the item; Task Item has a Marquee tooltip inside | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-WSP-4, AC-MOD-TIT-4, AC-MOD-TIT-5 | [[Workspaces Module]], [[Task Item]] |
| TSH-011 | Tray has no key path to an item or its menu | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-TRY-4, AC-MOD-TRI-4 | [[Tray Module]], [[Tray Item]] |
| TSH-012 | Task close is middle click only; Delete key absent | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-TIT-3 | [[Task Item]] |
| TSH-013 | Volume changes by scroll and secondary click with no key path | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-AUD-4 | [[Audio Module]] |
| TSH-014 | `Tab_Index` positive ordering is the documented model; the specification forbids positive indices | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-KBN-2 | [[Keyboard Navigation]] |
| TSH-017 | No keyboard way to move a Movable Panel | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-DND-5, AC-DND-1, AC-DND-2 | [[Drag and Drop]], [[Drag and Drop Pattern]] |
| TSH-018 | The focus ring is generic (`Shadows` ring from `model/look.py`) and reaches Workspaces; what remains is the Orca hand check, which is TSH-070 | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-A11Y-1 | [[Workspaces Module]], [[Accessibility Tree]] |
| TSH-021 | Focus ring is 2 px in `primary`, no offset, and only on blocks that take `Shadows` | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-FOC-1, AC-FOC-2 | [[Focus Ring]] |
| TSH-024 | Disabled opacity is 0.5 where the specification is 0.38 | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-LSI-08, AC-MEN-6 | [[List Item]], [[Menu]] |
| TSH-030 | The tray item hit area is 24 by 24 dp (meets the 24 dp minimum); the 18 is the icon. Icon 18 and spacing 6 are literals, where the density rows ask a 40, 32 or 28 dp hit area, icon 24, 20, 20 and gap 4 | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-TRY-7, AC-MOD-TRI-2 | [[Tray Module]], [[Tray Item]] |
| TSH-031 | Menu item row 28 dp, padding 10, icon 16 literals at default and compact; menu minimum width 160 not 112 | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-MIT-4, AC-MOD-TRM-5, AC-MEN-1, AC-MEN-2, AC-MEN-3 | [[Menu Item]], [[Tray Menu]], [[Menu]] |
| TSH-032 | The Audio and Media controls are Button modules, 32 dp with a 16 dp icon at every density | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-AUD-8, AC-MOD-MED-8 | [[Audio Module]], [[Media Module]] |
| TSH-033 | Task Item height is derived (icon 18 plus padding), not a literal; icon 18, padding 6 and gap 6 are literals, so it is 24 high rather than 40, 32, 28 by density. Workspaces height is text plus padding 10 | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-TIT-6, AC-MOD-WSP-6 | [[Task Item]], [[Workspaces Module]] |
| TSH-034 | No density setting; list rows 40, Button 32, Checkbox box 18, Toggle 40 by 22 are literals below 24 dp targets | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-DEN-1, AC-LSI-01, AC-LSI-02, AC-LSI-03, AC-LSI-06, AC-MOD-TGL-4 | [[Spacing and Density]], [[List Item]], [[Toggle]] |
| TSH-035 | Applications rows 40 dp, padding 10, width 456 literal | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-APP-5, AC-MOD-APP-6, AC-LNC-13 | [[Applications Module]], [[Launcher]] |
| TSH-036 | Badge dot is 8 by 8 and pill 18 high, 11 px; specification 6 and 16 | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-BDG-1, AC-BDG-2 | [[Badge]] |
| TSH-038 | Label overflow default is `CLIP`; Network name not truncated | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-LBL-2, AC-MOD-LBL-3 | [[Label]], [[Network Module]] |
| TSH-040 | Pressed menu item text `on_surface` on `primary` measures 2.58 to 1 in Dark and 2.89 to 1 in Light; the pressed fill is also used by the tray menu | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-MIT-5, AC-MOD-TRM-8 | [[Menu Item]], [[Tray Menu]] |
| TSH-041 | Clock Face foreground is the literal `#ffffff`; on the Light `surface` `#F4F7FA` it measures 1.08 to 1 | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-CLK-6 | [[Clock Module]] |
| TSH-044 | Launcher hover fill `surface_raised` equals the card fill | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-LNC-18 | [[Launcher]] |
| TSH-063 | Shape scale has 5 of 7 steps; dialog and rich tooltip steps cannot be expressed | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-SHP-2, AC-C04-1 | [[Shape]] |
| TSH-085 | Marquee has no hover pause | done on tess-shell main (tess-shell audit, schema 1.30; not re-checked here) | AC-MOD-MQT-7 | [[Marquee Text]] |
| TSH-060 | The theme `Reduced_Motion` block was empty and `EMPHASIZED` differed from the table | `Reduced_Motion` sets every duration to 0 in `Default_Theme.tdl`; `EMPHASIZED` is (0.2, 0, 0, 1) in `binder/motion.py` (checked in tess-shell origin/main, 5377644) | `tess-shell:src/tess_shell/binder/motion.py`, `Themes/Default_Theme.tdl:67-70` | [[Motion]] |
| TSH-071 | Tooltip carriers had role `GROUP` | Battery and Network roots are `IMG` with the tooltip as description; the Audio tooltip sits on the controls (checked in origin/main, 5377644; Media root is still a `GROUP` without a tooltip) | the three root files | [[Accessibility Tree]] |


## Implemented, merge pending the owner check

Implemented in tess-shell PR 131, merged only after the owner's KWin check (tess-shell audit against main, schema 1.30; not re-checked here). They leave the open counts and return to them if the check fails.

| ID | Finding | Failing ACs | Spec note |
|---|---|---|---|
| TSH-010 | `Auto_Hide`, `Auto_Hide_Delay` and the Shortcut Mode reveal must be built together ([[ADR-0021 Shortcut Mode reveals a hidden Bar]]); the default is off ([[ADR-0022 Bar Auto_Hide default is off]]), so only a Bar that opts in with `Auto_Hide: true` hides, which | AC-AHD-8, AC-AHD-9, AC-AHD-10, AC-AHD-20, AC-AHD-21, AC-BAR-13, AC-BAR-21 | [[Auto Hide]], [[Bar]] |
| TSH-050 | `Auto_Hide`, `Auto_Hide_Delay`, `Reveal_Key` absent: a Bar cannot be hidden; built together with the Shortcut Mode reveal (TSH-010) | AC-AHD-1, AC-AHD-2, AC-AHD-3, AC-AHD-4, AC-AHD-5, AC-AHD-6, AC-AHD-7, AC-AHD-12, AC-AHD-13 | [[Auto Hide]] |
| TSH-051 | Bar `Visible`, `Input_Region`, `Exclusive_Zone` not built | AC-BAR-4, AC-BAR-17 | [[Bar]] |

## Held findings

These rows wait on a decision or a hook, not on shell work; each carries `held: <reason>` in its Finding text.

| ID | Held on | Waiting for |
|---|---|---|
| TSH-020 | tre 0.6.12 | state layers are implemented in the shell (OQ-23 closed 2026-11-22: adopted); the 15, 105 and 150 ms fades wait for tre 0.6.12 |
| TSH-022 | tre 0.6.12 | follows TSH-020 (Toggle hover and pressed) |
| TSH-054 | tre 0.6.12 | the path build waits for tre 0.6.12 |
| TSH-070 | Orca | a hand check; Orca is not installed on the owner's machine |
| TSH-008 | shell feature | dynamic tooltips in `For` plus `Class` on a module call |
| TSH-084 | shell feature | events to a non-root block of a composite TextInput (the `Error` and `Helper` slots) |
| TSH-080 | not built | `Scroll_Snap` and `On_Scroll` on ScrollBox (the scrollbars are built) |

## Won't do

| ID | Finding | Reason |
|---|---|---|
| TSH-052 | Bar `Meld` and `Attach_To` not built; Frame `Meld` not built | Won't do (decision of bot:Orchestrator under its UX-vault delegation, 2026-11-22): a Bar in the Frame is a Frame strip (a thick edge with peek and hide); [[Frame]] AC-FRM2-11 and [[Bar]] AC-BAR-17 list `Meld` and `Attach_To` as intentionally not built and the Bar specification gives them no behaviour; the 'not built' wording of AC-BAR-17 stays. |
| TSH-083 | Rectangle block offers no `Hit_Shape` | The [[Rectangle Block]] specification does not offer `Hit_Shape` (it belongs to [[Path Block]]); a Rectangle that must let clicks through is a transparent box. The row was wrong and its AC citation (AC-BLK-RCT-5, a tree assertion) did not test it. |

## Engine hooks needed

The tre hooks that tess-shell rows need; the table of what each unlocks is in [[Adoption tre]]. Under [[ADR-0020 The engine never blocks the design]] the shell owns the look and the engine offers the hook.

- [[UXREQ-001 Two-axis scroll view with the specified scrollbar]]: TSH-080
- [[UXREQ-008 Outline property for focus rings]] (approved): TSH-021

## AC coverage by note (approximate)

Counts come from the prose of each `Status in code` row, not from a run. "Meets" means met by reading or by design; "fails" means a failing id is named; "open" means named as unverified or not run. The ids are those the rows name.

| Note | Meets (by reading) | Fails | Open |
|---|---|---|---|
| [[Audio Module]] | AC-MOD-AUD-1, 2, 7, 9 | AC-MOD-AUD-4, 5, 6, 8, 10 | none named |
| [[Battery Module]] | AC-MOD-BAT-2, 6, 8 | AC-MOD-BAT-1, 5, 9 | none named |
| [[Clock Module]] | AC-MOD-CLK-1, 4 | AC-MOD-CLK-5, 6 | none named |
| [[Media Module]] | AC-MOD-MED-1, 2, 3, 4, 7, 11 | AC-MOD-MED-5, 6, 8, 10 | none named |
| [[Network Module]] | AC-MOD-NET-2, 5, 7 | AC-MOD-NET-1, 4, 8 | none named |
| [[Tray Module]] | AC-MOD-TRY-1, 2, 3, 8 | AC-MOD-TRY-4, 7 | none named |
| [[Tray Item]] | AC-MOD-TRI-1, 3, 5, 6 | AC-MOD-TRI-2, 4, 8 | AC-MOD-TRI-7 |
| [[Task Item]] | AC-MOD-TIT-1, 2 | AC-MOD-TIT-3, 4, 5, 6, 7 | none named |
| [[Tasks Module]] | AC-MOD-TSK-1, 2, 3, 4, 8 | AC-MOD-TSK-9 | none named |
| [[Menu Item]] | AC-MOD-MIT-1, 2, 3, 6, 7 | AC-MOD-MIT-4, 5 | none named |
| [[Tray Menu]] | AC-MOD-TRM-1, 2, 4 | AC-MOD-TRM-5, 8 | AC-MOD-TRM-3 |
| [[Workspaces Module]] | AC-MOD-WSP-1, 2, 3, 7 | AC-MOD-WSP-4, 6 | AC-MOD-WSP-5 |
| [[Volume OSD]] | AC-OSD-1 to 5, 8, 9, 13 | AC-OSD-15 in part | AC-OSD-6, 7, 14 |
| [[Bar]] | AC-BAR-1, 3, 5, 6, 11, 12, 17 | AC-BAR-4 | AC-BAR-8, 13 |
| [[Auto Hide]] | none | AC-AHD-1 to 19 | none |
| [[Frame]] | AC-FRM2-19, 21 (recorded measurements) | AC-FRM2-11 | AC-FRM2-20, 22, 23 |
| [[Popup]] | AC-POP-3, 4, 8, 10, 11, 12 | AC-POP-6, 7 | AC-POP-1, 9 |
| [[Menu]] | AC-MEN-7, 8, 10, 12 | AC-MEN-1 to 6, 9 | AC-MEN-11, 14 in part |
| [[Tooltip]] | AC-TIP-3, 16, 17 | AC-TIP-4, 13, 21 | AC-TIP-1 |
| [[Launcher]] | AC-LNC-1, 2 to 9, 11, 16, 19 | AC-LNC-13, 18 | AC-LNC-10, 15, 17, 20 |
| [[Peek]] | the built keys (owner KWin check 2026-11-08) | AC-PEK-14, 16, 18 | AC-PEK-3, 17 |
| [[State Layers]] | none | AC-STL-1, 2, 3, 5 | none |
| [[Focus Ring]] | none | AC-FOC-1, 2 | none |
| [[Colour Roles]] | AC-COL-7 | AC-COL-3, 4 | none |
| [[Keyboard Navigation]] | AC-KBN-1, 5, 7, 17 | AC-KBN-2, 3 | none |

## Questions for the tess-shell bot

1. Is the default tooltip `Exit_Delay` of 200 ms set in one place (`schema/model.py:129`) so one change reaches all six cards, and is a hoverable tooltip feasible with the popup window route?
2. Can a `Tooltip` move off a `GROUP` root onto a child in Battery, Network and Audio without changing the module parameters?
3. Does `Enter_Shortcut_Mode` already reveal a hidden surface, so that AC-AHD-9 needs only the Bar `Visible` key? (Input to TSH-010; the rule itself is decided in [[ADR-0021 Shortcut Mode reveals a hidden Bar]].)
4. Is there a global key or shortcut that a Bar could use to reveal itself today, given that `Reveal_Key` was removed in PR 59?
5. Does the `StatusNotifier` tray item expose a menu request (`ContextMenu`) that a Menu key could call?
6. Can the stylesheet express a state layer (an overlay fill with an opacity) without a new tre hook? (Input to OQ-23.)
7. Is the default tooltip card (`Elevation: 20%`) meant to match the Popup shadow, and is a theme level model planned?
8. Where does the density setting belong (theme, settings or a module parameter), and has an owner decision been recorded?
9. Does any test or script measure contrast over the shipped themes, and was the 2.58 to 1 pressed pair known?
10. Has the click-away catcher fault of 2026-11-20 (revert PR #111) a new fix, and does it change the Launcher popup grab rows AC-POP-6 and AC-POP-7?

## Open owner decisions

| Id | Question | Related rows |
|---|---|---|
| OQ-23 | Closed 2026-11-22: yes, the shell adopts the MD3 state layers ([[ADR-0009 State layer percentages]]). | TSH-020, TSH-022, TSH-054, TSH-023, TSH-024, TSH-040 |
